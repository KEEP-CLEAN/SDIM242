import smbus 
import wiringpi as GPIO

bus = smbus.SMBus(1)

def arrayList1():
    List1 = []
    count = 0
    while count < 300:
        n1 = GPIO.micros()#get the time before readbyte
        y = bus.read_byte(0x48)
        n2 = GPIO.micros()#get the time after readbyte
        List1.append(y)
        n3 = n2 - n1
        print(n3)
        count = count + 1
    return List1

if __name__ == "__main__":
    while True:
        if bus.read_byte(0x48)>50:
            List2 = arrayList1()
            x = len(List2)
            num = 0 
            i = 0
            while i < x-1:
                if List2[i] > 50 and List2[i+1] <40:
                    num = num+1
                i = i + 1
            print(List2)
            print(num)