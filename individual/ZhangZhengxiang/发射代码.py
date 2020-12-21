import time
import RPi.GPIO as GPIO
import pigpio

class keypad(object):
  KEYPAD=[
    ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['*','0','#','D']]
  ROW    =[12,16,20,21]#行
  COLUMN =[6,13,19,26]#列
 
#初始化函数
def __init__():
  GPIO.cleanup()
  GPIO.setmode(GPIO.BCM)

#取得键盘数函数
def getkey():
  GPIO.setmode(GPIO.BCM)
#设置列输出低
  for i in range(len(keypad.COLUMN)):
    GPIO.setup(keypad.COLUMN[i],GPIO.OUT)
    GPIO.output(keypad.COLUMN[i],GPIO.LOW)
#设置行为输入、上拉
  for j in range(len(keypad.ROW)):
    GPIO.setup(keypad.ROW[j],GPIO.IN,pull_up_down=GPIO.PUD_UP)
#检测行是否有键按下，有则读取行值
  RowVal=-1
  for i in range(len(keypad.ROW)):
    RowStatus=GPIO.input(keypad.ROW[i])
    if RowStatus==GPIO.LOW:
       RowVal=i
       #print('RowVal=%s' % RowVal)
#若无键按下,则退出，准备下一次扫描
  if RowVal<0 or RowVal>3:
    exit()
    return
#若第RowVal行有键按下，跳过退出函数，对掉输入输出模式
#第RowVal行输出高电平，
  GPIO.setup(keypad.ROW[RowVal],GPIO.OUT)
  GPIO.output(keypad.ROW[RowVal],GPIO.HIGH)
#列为下拉输入
  for j in range(len(keypad.COLUMN)):
    GPIO.setup(keypad.COLUMN[j],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#读取按键所在列值
  ColumnVal=-1
  for i in range(len(keypad.COLUMN)):
    ColumnStatus=GPIO.input(keypad.COLUMN[i])
    if ColumnStatus==GPIO.HIGH:
      ColumnVal=i
#等待按键松开
      while GPIO.input(keypad.COLUMN[i])==GPIO.HIGH:
        time.sleep(0.05)
        #print ('ColumnVal=%s' % ColumnVal)
#若无键按下，返回
  if ColumnVal<0 or ColumnVal>3:
    exit()
    return
  #exit()
  return keypad.KEYPAD[RowVal][ColumnVal]
 
def exit():
 
  import RPi.GPIO as GPIO
  for i in range(len(keypad.ROW)):
    GPIO.setup( keypad.ROW[i],GPIO.IN,pull_up_down=GPIO.PUD_UP)
  for j in range(len( keypad.COLUMN)):
    GPIO.setup( keypad.COLUMN[j],GPIO.IN,pull_up_down=GPIO.PUD_UP)
 

 
if __name__ == "__main__": 

  pi = pigpio.pi()
  pi.set_mode(17,pigpio.OUTPUT)
  pi.write(17,0)
  key=None
  
  while True:
      key=getkey()

      if key == '1':#DLDLDDLD
        st = time.time()
        time.sleep(0.01)
        pi.write(17,1)
        time.sleep(0.01)
        pi.write(17,0)
        time.sleep(0.01)
        pi.write(17,1)
        time.sleep(0.01)
        pi.write(17,0)
        time.sleep(0.02)
        pi.write(17,1)
        time.sleep(0.01)
        pi.write(17,0)
        time.sleep(0.01)
        et = time.time()
        print(et-st)

      if key == '2':#LDLDLDLD
        st = time.time()
        for i in range(0,4):
            pi.write(17,1)
            time.sleep(0.01)
            pi.write(17,0)
            time.sleep(0.01)
        et = time.time()
        print(et-st)

      # if key == '3':LLDDDLLD
      #   st = time.time()
      #   pi.write(17,1)
      #   time.sleep(0.02)
      #   pi.write(17,0)
      #   time.sleep(0.03)
      #   pi.write(17,1)
      #   time.sleep(0.02)
      #   pi.write(17,0)
      #   time.sleep(0.01)
      #   et = time.time()
      #   print(et-st)

      if key == '*':
        pi.write(17,1)
        time.sleep(0.02)
        pi.write(17,0)
        time.sleep(0.1)
        break
      
  pi.stop() 
  GPIO.cleanup()
  pwm.stop()