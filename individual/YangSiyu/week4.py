
import smbus   
import time
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
pwm = GPIO.PWM(7,320) 

bus = smbus.SMBus(1)         
def setup(Addr):
    global address
    address = Addr

def read(chn): #channel
    if chn == 0:
        bus.write_byte(address,0x40)   #
    if chn == 1:
        bus.write_byte(address,0x41)
    if chn == 2:
        bus.write_byte(address,0x42)
    if chn == 3:
        bus.write_byte(address,0x43)
    bus.read_byte(address)         # 
    return bus.read_byte(address)  #

def write(val):
    temp = val  # 
    temp = int(temp) #
    # print temp to see on terminal else comment out
    bus.write_byte_data(address, 0x40, temp) 
    #

if __name__ == "__main__":
    setup(0x48) 
 
    while True:
        print ('kk  AIN0 = ', read(0))  
#         print 'll AIN1 = ', read(1)  
#         print 'hh AIN2 = ', read(2)
        
        tmp = read(0)
        tmp = tmp*(255-125)/255+125
        if(read(0)>117):
            GPIO.output(7,GPIO.HIGH)
        if(read(0)<117):
            GPIO.output(7,GPIO.LOW)
        write(tmp)
        time.sleep(0.1)

