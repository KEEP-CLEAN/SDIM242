import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.OUT)
pwm = GPIO.PWM(2, 100)
pwm.start(0)

while True:
    print("pls input dt: ")
    dt = input()
    pwm.ChangeDutyCycle(int(dt))
