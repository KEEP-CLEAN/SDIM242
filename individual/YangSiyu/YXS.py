import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

out1 = 7
out2 = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)

while(1):
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.LOW)
    
    print( "First calibrate by giving some +ve and -ve values.....")
    x1=int(input())
    if x1==0:
        GPIO.output(out1,GPIO.LOW)
        GPIO.output(out2,GPIO.HIGH)
        time.sleep(3)
    else:
        GPIO.output(out1,GPIO.HIGH)
        GPIO.output(out2,GPIO.LOW)
        time.sleep(3)

GPIO.output(out1,GPIO.LOW)
GPIO.output(out2,GPIO.LOW)
GPIO.cleanup()

    