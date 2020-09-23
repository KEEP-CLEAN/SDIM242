import RPi.GPIO as GPIO                 
import time                               

GPIO.setmode(GPIO.BCM)                

GPIO.setup(17, GPIO.OUT)

pwm = GPIO.PWM(17,80)

pwm.start(0)

if __name__ == '__main__':
    try:
        while True:                       
            #GPIO.output(17, True)       
            #time.sleep(1)               
            #GPIO.output(17, False)      
            #time.sleep(1)
            for i in xrange(0,51,1):
                pwm.ChangeDutyCycle(i)
                time.sleep(.02)
            for i in xrange(50,-1,-1):
                pwm.ChangeDutyCycle(i)
                time.sleep(.02)
    finally:
        GPIO.cleanup()                  