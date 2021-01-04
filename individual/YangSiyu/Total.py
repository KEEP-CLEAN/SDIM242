#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

#IR modulus pin
PIN = 38;

# L298N pin
# 35 conneccts to In2;36 connects to In1 
out1 = 35
out2 = 36

# GM6020 pin
ENA = 11


GPIO.setmode(GPIO.BOARD)
# L298N
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
# GM6020
GPIO.setup(ENA,GPIO.OUT)
#  IR modulus
GPIO.setup(PIN,GPIO.IN,GPIO.PUD_UP)

pwm1 = GPIO.PWM(ENA, 50)
pwm1.start(0)
pwm1.ChangeDutyCycle(0)

print("irm test start...")

def exec_cmd(key_val):
#     rod shrinks
    if(key_val==0x45):
        print("Button 1")
        GPIO.output(out1,GPIO.LOW)
        GPIO.output(out2,GPIO.HIGH)
        time.sleep(6)
#rod extends
    elif(key_val==0x46):
        print("Button 2")
        GPIO.output(out1,GPIO.HIGH)
        GPIO.output(out2,GPIO.LOW)
        time.sleep(6)
# the band moves
    elif(key_val==0x47):
        print("Button 3")
        pwm1.ChangeDutyCycle(5)
# the band stops
    elif(key_val==0x44):
        print("Button 4")
        pwm1.ChangeDutyCycle(0)

# recognize infrared signal 
try:
    while True:
        if GPIO.input(PIN) == 0:
            count = 0
            while GPIO.input(PIN) == 0 and count < 200:
                count += 1
                time.sleep(0.00006)

            count = 0
            while GPIO.input(PIN) == 1 and count < 80:
                count += 1
                time.sleep(0.00006)

            idx = 0
            cnt = 0
            data = [0,0,0,0]
            for i in range(0,32):
                count = 0
                while GPIO.input(PIN) == 0 and count < 15:
                    count += 1
                    time.sleep(0.00006)

                count = 0
                while GPIO.input(PIN) == 1 and count < 40:
                    count += 1
                    time.sleep(0.00006)

                if count > 8:
                    data[idx] |= 1<<cnt
                if cnt == 7:
                    cnt = 0
                    idx += 1
                else:
                    cnt += 1
            if data[0]+data[1] == 0xFF and data[2]+data[3] == 0xFF:
                 print("Get the key: 0x%02x" %data[2])
                 exec_cmd(data[2])
                 
                 
except KeyboardInterrupt:
    GPIO.cleanup();

GPIO.output(out1,GPIO.LOW)
GPIO.output(out2,GPIO.LOW)
GPIO.cleanup()
