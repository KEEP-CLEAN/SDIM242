import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

out1 = 13
out2 = 11
out3 = 15
out4 = 12

ENA = 31
ENB = 32

i=0
positive=0
negative=0
y=0

GPIO.setmode(GPIO.BOARD)
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

while(1):
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.LOW)
    GPIO.output(out3,GPIO.LOW)
    GPIO.output(out4,GPIO.LOW)
    x1=int(input())
    if x1 < 20:
        for x in range(x1):
            pwm1.ChangeDutyCycle(x)
            pwm2.ChangeDutyCycle(x)
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            print (x)
            time.sleep(0.5)
    else:
        for x in range(20):
            pwm1.ChangeDutyCycle(x)
            pwm2.ChangeDutyCycle(x)
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(0.5)
            print(x)
        for x in range(20,x1):
            pwm1.ChangeDutyCycle(x)
            pwm2.ChangeDutyCycle(x)
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(0.5)
            print(x)
GPIO.output(out1,GPIO.LOW)
GPIO.output(out2,GPIO.LOW)
GPIO.output(out3,GPIO.LOW)
GPIO.output(out4,GPIO.LOW)
GPIO.cleanup()
pwm1.stop()
pwm2.stop()
    