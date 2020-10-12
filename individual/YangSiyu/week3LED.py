import RPi.GPIO as GPIO               
import time                         
GPIO.setmode(GPIO.BCM)               

GPIO.setup(10, GPIO.OUT)
GPIO.setwarnings(False)

if __name__ == '__main__':
    try:
        while True:                   
            GPIO.output(10, True)       
            time.sleep(1)              
            GPIO.output(10, False)     
            time.sleep(1)            
    finally:
        GPIO.cleanup()               
