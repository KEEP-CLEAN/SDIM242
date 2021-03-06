﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

import spidev,time
import sys,cmd,shlex,types
from mcp2515 import *

spi = spidev.SpiDev(0,0)

def mcp2515_reset():
    tmpc = [0xc0]
    spi.writebytes(tmpc)

def mcp2515_writeReg(addr, val):
    buf = [0x02, addr, val]
    spi.writebytes(buf)

def mcp2515_readReg(addr):
    buf = [0x03, addr, 0x55]
    buf = spi.xfer2(buf)
    return int(buf[2])

def mcp2515_init():
    mcp2515_reset()
    time.sleep(2)
    #???ò?????Ϊ125Kbps
    #set CNF1,SJW=00,????Ϊ1TQ,BRP=49,TQ=[2*(BRP+1)]/Fsoc=2*50/8M=12.5us
    mcp2515_writeReg(CNF1,CAN_125Kbps);
    #set CNF2,SAM=0,?ڲ?????????߽???һ?β?????PHSEG1=(2+1)TQ=3TQ,PRSEG=(0+1)TQ=1TQ
    mcp2515_writeReg(CNF2,0x80|PHSEG1_3TQ|PRSEG_1TQ);
    #set CNF3,PHSEG2=(2+1)TQ=3TQ,ͬʱ??CANCTRL.CLKEN=1ʱ?趨CLKOUT????Ϊʱ?????ʹ??λ
    mcp2515_writeReg(CNF3,PHSEG2_3TQ);

    mcp2515_writeReg(TXB0SIDH,0xFF)#???ͻ?????0??׼??ʶ????λ
    mcp2515_writeReg(TXB0SIDL,0xEB)#???ͻ?????0??׼??ʶ????λ(??3λΪ??????չ??ʶ??ʹ??λ)
    mcp2515_writeReg(TXB0EID8,0xFF)#???ͻ?????0??չ??ʶ????λ
    mcp2515_writeReg(TXB0EID0,0xFF)#???ͻ?????0??չ??ʶ????λ

    mcp2515_writeReg(RXB0SIDH,0x00)#??ս??ջ?????0?ı?׼??ʶ????λ
    mcp2515_writeReg(RXB0SIDL,0x00)#??ս??ջ?????0?ı?׼??ʶ????λ
    mcp2515_writeReg(RXB0EID8,0x00)#??ս??ջ?????0????չ??ʶ????λ
    mcp2515_writeReg(RXB0EID0,0x00)#??ս??ջ?????0????չ??ʶ????λ
    mcp2515_writeReg(RXB0CTRL,0x40)#??????????չ??ʶ??????Ч??Ϣ
    mcp2515_writeReg(RXB0DLC,DLC_8)#???ý??????ݵĳ???Ϊ8???ֽ?

    mcp2515_writeReg(RXF0SIDH,0xFF)#?????????˲??Ĵ???n??׼??ʶ????λ
    mcp2515_writeReg(RXF0SIDL,0xEB)#?????????˲??Ĵ???n??׼??ʶ????λ(??3λΪ??????չ??ʶ??ʹ??λ)
    mcp2515_writeReg(RXF0EID8,0xFF)#?????????˲??Ĵ???n??չ??ʶ????λ
    mcp2515_writeReg(RXF0EID0,0xFF)#?????????˲??Ĵ???n??չ??ʶ????λ

    mcp2515_writeReg(RXM0SIDH,0xFF)#???????????μĴ???n??׼??ʶ????λ
    mcp2515_writeReg(RXM0SIDL,0xE3)#???????????μĴ???n??׼??ʶ????λ
    mcp2515_writeReg(RXM0EID8,0xFF)#?????????˲??Ĵ???n??չ??ʶ????λ
    mcp2515_writeReg(RXM0EID0,0xFF)#?????????˲??Ĵ???n??չ??ʶ????λ

    mcp2515_writeReg(CANINTF,0x00)#???CAN?жϱ?־?Ĵ?????????λ(??????MCU???)
    mcp2515_writeReg(CANINTE,0x01)#????CAN?ж?ʹ?ܼĴ????Ľ??ջ?????0???ж?ʹ??,????λ??ֹ?ж?

    mcp2515_writeReg(CANCTRL,REQOP_NORMAL|CLKOUT_ENABLED)#??MCP2515????Ϊ????ģʽ,?˳?????ģʽ

    #tmpc = mcp2515_readReg(CANSTAT)#??ȡCAN״̬?Ĵ?????ֵ
    #tmpd = int(tmpc[0]) & 0xe0
    #if OPMODE_NORMAL!=tmpd:#?ж?MCP2515?Ƿ??Ѿ?????????ģʽ
    #    mcp2515_writeReg(CANCTRL,REQOP_NORMAL|CLKOUT_ENABLED)#?ٴν?MCP2515????ΪXXģʽ,?˳?????ģʽ
    print '\r\nMCP2515 Initialized.\r\n'


def mcp2515_write(buf):
    for i in range(50):
        time.sleep(2) #ͨ???????ʱԼnms(??׼ȷ)
        if not mcp2515_readReg(TXB0CTRL)&0x08:#???ٶ?ĳЩ״ָ̬??,?ȴ?TXREQ??־????
            break
    N = len(buf)
    for j in range(N):
        mcp2515_writeReg(TXB0D0+j,buf[j])#???????͵?????д?뷢?ͻ???Ĵ???

    mcp2515_writeReg(TXB0DLC,N)#????֡?????͵????ݳ???д?뷢?ͻ?????0?ķ??ͳ??ȼĴ???
    mcp2515_writeReg(TXB0CTRL,0x08)#?????ͱ???

def mcp2515_read():
    N = 0
    buf = []
    if mcp2515_readReg(CANINTF) & 0x01:
        N = mcp2515_readReg(RXB0DLC)#??ȡ???ջ?????0???յ??????ݳ???(0~8???ֽ?)
        for i in range(N):
            buf.append(mcp2515_readReg(RXB0D0+i))#??CAN???յ??????ݷ???ָ????????
    mcp2515_writeReg(CANINTF,0)#????жϱ?־λ(?жϱ?־?Ĵ?????????MCU????)
    return buf

class MyCmd(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt='wyq@rpi2 ~ $ '
        mcp2515_init()

    def emptyline(self):
        pass

    def do_test(self,arg):
        lex = shlex.shlex(arg)
        for x in lex:
            print x

    def do_exit(self,arg):
        return True

    def do_mcp(self,arg):
        lex = shlex.shlex(arg)
        try:
            for x in lex:
                if x=='-':
                    opt = lex.next()
                    if opt.lower()=='init':
                        mcp2515_init()
                    elif opt.lower()=='w':
                        buf = []
                        for i in lex:
                            buf.append(int(i))
                        mcp2515_write(buf)
                    elif opt.lower()=='r':
                        buf = mcp2515_read()
                        print 'Received:',len(buf)
                        for i in buf:
                            print hex(int(i))
                    else:
                        pass
        except BaseException, e:
            print e

    def do_help(self,arg):
        print '????MCP2515??CAN?շ???????'
        print 'Author:????ǿ QQ:917888229 Date:2016-8-18'
        print '????ָ??: mcp -w XX YY ZZ'
        print '????ָ??: mcp -r'
        print '?س?ʼ??: mcp -init'


if __name__=='__main__':
    mycmd = MyCmd()
    mycmd.cmdloop()