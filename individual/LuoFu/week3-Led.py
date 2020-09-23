import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)
pwm = GPIO.PWM(23, 100)
pwm.start(0)
while True:
    print("pls input dt: ")
    dt = input()
    pwm.ChangeDutyCycle(int(dt))
    GPIO.output(23, GPIO.HIGH)
    time.sleep(2)
    pwm.stop()
    break
