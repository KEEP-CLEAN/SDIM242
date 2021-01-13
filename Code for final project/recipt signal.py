import smbus 
import time
import RPi.GPIO as GPIO

bus = smbus.SMBus(1)

Data1 = [0,1,0,1,0,0,1,0]
Data2 = [1,0,1,0,1,0,1,0]
#Data3 = [1,1,0,0,0,1,1,0]

out1 = 11
out2 = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)

ConveyorBelt = False
LinearActuator = False

def Datalist():
    List = []
    count = 0
    while count < 8:
        y = bus.read_byte(0x48)
        time.sleep(0.02)
        if y > 100:
            List.append(1)
        else:
            List.append(0)
        count = count + 1
    print (List)
    return List

if __name__ == "__main__":
    while True:
        if bus.read_byte(0x48) > 100:
            data = Datalist()
            if((data==Data1).all()):
                if(ConveyorBelt):
                    print ("Pressing 1. Deactivate convoyer belt.")
                    ConveyorBelt = False
                else:
                    print ("Pressing 1. Activate convoyer belt.")
                    ConveyorBelt = True

            if((data==Data2).all()):
                if(LinearActuator):

                    GPIO.output(out1,GPIO.LOW)
                    GPIO.output(out2,GPIO.HIGH)
                    time.sleep(5)
                    print ("Pressing 2. Going backward.")
                    LinearActuator = False
                else:
                    
                    GPIO.output(out1,GPIO.HIGH)
                    GPIO.output(out2,GPIO.LOW)
                    time.sleep(5)
                    print ("Pressing 2. Pushing forward.")
                    LinearActuator = True

      