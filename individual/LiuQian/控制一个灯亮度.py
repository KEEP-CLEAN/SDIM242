import RPi.GPIO as GPIO
channels = [24,23,10,9,11,25,8,7]
x = channels

GPIO.setmode(GPIO.BCM)
GPIO.setup(x,GPIO.OUT)
GPIO.setwarnings(False)

for x in channels:
    pwm = GPIO.PWM(x, 100)
    pwm.start(0)

while True:
    print("pls input dt: ")
    dt = input()
    pwm.ChangeDutyCycle(int(dt))