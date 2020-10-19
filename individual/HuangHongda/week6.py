
#coding:utf-8
import RPi.GPIO as GPIO  ##引入GPIO模块
import time              ##引入time库
import datetime
from lcd1602 import *
# from datetime import *
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

cPin = 4
GPIO.setup(cPin,GPIO.IN)  ##设置为接收模式
out1 = 19
out2 = 16
out3 = 26
out4 = 20
ENA = 6
ENB = 12

i=0
positive=0
negative=0
y=0


GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(ENB,GPIO.OUT)


print( "First calibrate by giving some +ve and -ve values.....")

pwm1 = GPIO.PWM(ENA, 50)
pwm2 = GPIO.PWM(ENB, 50)
pwm1.start(0)
pwm2.start(0)


GPIO.output(out1,GPIO.LOW)
GPIO.output(out2,GPIO.LOW)
GPIO.output(out3,GPIO.LOW)
GPIO.output(out4,GPIO.LOW)
x1=int(input())
x2=int(input())
pwm1.ChangeDutyCycle(x1)
pwm2.ChangeDutyCycle(x1)

    
if x2==0:
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.HIGH)
    GPIO.output(out3,GPIO.LOW)
    GPIO.output(out4,GPIO.HIGH)
    
else:
    GPIO.output(out1,GPIO.HIGH)
    GPIO.output(out2,GPIO.LOW)
    GPIO.output(out3,GPIO.HIGH)
    GPIO.output(out4,GPIO.LOW)
    
start_time = datetime.datetime.now()
count=0
status=0
lcd = lcd1602()
lcd.clear()
# lcd.message("hello world!")
while True:
    temp=GPIO.input(cPin)
    if status != temp:
        count = count+1
    status = temp
    end_time = datetime.datetime.now()
    interval = (end_time-start_time).seconds
    if interval > 5:
        speed = count/(20)/2*(60/5)
        lcd = lcd1602()
        lcd.clear()
        lcd.message("Speed is %d RPM" %speed)
        break
GPIO.output(out1,GPIO.LOW)
GPIO.output(out2,GPIO.LOW)
GPIO.output(out3,GPIO.LOW)
GPIO.output(out4,GPIO.LOW)
GPIO.cleanup()
pwm1.stop()
pwm2.stop()
        

