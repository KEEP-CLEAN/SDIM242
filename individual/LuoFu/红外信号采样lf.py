#SMBus (System Management Bus,系统管理总线)
import smbus   #在程序中导入“smbus”模块 
import time
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
pwm = GPIO.PWM(7,320) 

# for RPI version 1, use "bus = smbus.SMBus(1)"
# 0 代表 /dev/i2c-0， 1 代表 /dev/i2c-1 ,具体看使用的树莓派那个I2C来决定
bus = smbus.SMBus(1)  #创建一个smbus实例 

def setup(Addr):
    global address
    address = Addr

def read(chn): #channel
    if chn == 0:
        bus.write_byte(address,0x40)#发送一个控制字节到设备，0×40：@
    #if chn == 1:
    #    bus.write_byte(address,0x41)#0x41：A
    #if chn == 2:
    #    bus.write_byte(address,0x42)#0x41：B
    #if chn == 3:
    #    bus.write_byte(address,0x43)#0x41：C
    bus.read_byte(address)   # 从设备读取单个字节，而不指定设备寄存器
    return bus.read_byte(address)#返回address通道输入的模拟值A/D转换后的数字

def write(val):
    temp = val
    temp = int(temp)
    bus.write_byte_data(address, 0x40, temp) #写入字节数据，将数字值转化成模拟值从AOUT输出

#创建一个数组，记录采样数据
def arrayList1():
    List1 = []
    count = 0
    while count < 0.05:
        List1.append(read(0))
        time.sleep(0.0005)
        count = count + 0.0005
    return List1


if __name__ == "__main__":#当模块直接运行时，以下代码也会被运行
    setup(0x48) #在树莓派终端上使用命令“sudo i2cdetect -y 1”，查询出PCF8591的地址为0x48
    while True:
        if read(0)>50:
            List2=arrayList1()
            x = len(List2)
            num = 0 # 波峰数目
            i= 0
            while i<x-1:
                if List2[i] > 50 and List2[i+1] <5:
                    num = num+1
                i = i+1
            print(List2)
            print(num)        
        #print'kk  AIN0 = ', read(0)   #电位计模拟信号转化的数字值
        #tmp = read(0)
        #tmp = tmp*(255-125)/255+125# 125以下LED不会亮，所以将“0-255”转换为“125-255”，调节亮度时灯不会熄灭
        #if(read(0)>100):
        #    GPIO.output(7,GPIO.HIGH)
        #if(read(0)<100):
        #    GPIO.output(7,GPIO.LOW)
        #write(tmp)
        #time.sleep(0.1)

