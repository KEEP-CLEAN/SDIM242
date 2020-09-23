import RPi.GPIO as GPIO
import time
channels = [23,24,10,9,11,25,8,7]
x = channels
GPIO.setmode(GPIO.BCM)

GPIO.setup(x, GPIO.OUT)

if __name__ == '__main__':
    try:
        while True:
            GPIO.output(x, True)
            time.sleep(1)
            GPIO.output(x, False)
            time.sleep(1)
    finally:
        GPIO.cleanup()