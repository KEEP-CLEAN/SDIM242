import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

def blink():
    GPIO.output(24,GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(24,GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.output(25,GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(25,GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.output(11,GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(11,GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.output(8,GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(8,GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.output(10,GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(10,GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.output(7,GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(7,GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.output(9,GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(9,GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.output(23,GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(23,GPIO.LOW)
    time.sleep(0.1)
    
try:
    while True:
        
        blink()
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()