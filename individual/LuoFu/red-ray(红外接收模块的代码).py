#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

PIN = 17;

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

pwm1 = GPIO.PWM(5, 100)
pwm2 = GPIO.PWM(6, 100)
pwm3 = GPIO.PWM(13, 100)
pwm4 = GPIO.PWM(19, 100)

print("irm test start...")

def exec_cmd(key_val):
    if(key_val==0x45):
        print("Button 1")
        print("blue LED lights")
        pwm1.start(0)
        pwm1.ChangeDutyCycle(50)
        GPIO.output(5, GPIO.HIGH)
        time.sleep(0.5)
        pwm1.stop()
    elif(key_val==0x46):
        print("Button 2")
        print("green LED lights")
        pwm2.start(0)
        pwm2.ChangeDutyCycle(50)
        GPIO.output(6, GPIO.HIGH)
        time.sleep(0.5)
        pwm2.stop()
    elif(key_val==0x47):
        print("Button 3")
        print("red LED lights")
        pwm3.start(0)
        pwm3.ChangeDutyCycle(50)
        GPIO.output(13, GPIO.HIGH)
        time.sleep(0.5)
        pwm3.stop()
    elif(key_val==0x44):
        print("Button 4")
        print("white LED lights")
        pwm4.start(0)
        pwm4.ChangeDutyCycle(50)
        GPIO.output(19, GPIO.HIGH)
        time.sleep(0.5)
        pwm4.stop()
    elif(key_val==0x40):
        print("Button NEXT")
    elif(key_val==0x43):
        print("Button PLAY/PAUSE")
    elif(key_val==0x07):
        print("Button VOL-")
    elif(key_val==0x15):
        print("Button VOL+")
    elif(key_val==0x09):
        print("Button EQ")
    elif(key_val==0x16):
        print("Button 0")
    elif(key_val==0x19):
        print("Button 100+")
    elif(key_val==0x0d):
        print("Button 200+")
    elif(key_val==0x0c):
        print("Button 1")
    elif(key_val==0x18):
        print("Button 2")
    elif(key_val==0x5e):
        print("Button 3")
    elif(key_val==0x08):
        print("Button 4")
    elif(key_val==0x1c):
        print("Button 5")
    elif(key_val==0x5a):
        print("Button 6")
    elif(key_val==0x42):
        print("Button 7")
    elif(key_val==0x52):
        print("Button 8")
    elif(key_val==0x4a):
        print("Button 9")

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
