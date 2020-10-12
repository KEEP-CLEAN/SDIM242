import time
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)            
GPIO.setup(10, GPIO.OUT)          
GPIO.output(10, GPIO.LOW)       
 
p = GPIO.PWM(10, 100)          
p.start(0)                       
try:
    while 1:
        for dc in range(0, 101, 5):       
            p.ChangeDutyCycle(dc)         
            time.sleep(0.1)              
        for dc in range(100, -1, -5):     
            p.ChangeDutyCycle(dc)         
            time.sleep(0.1)              
except KeyboardInterrupt:                
    pass
p.stop()
GPIO.cleanup()