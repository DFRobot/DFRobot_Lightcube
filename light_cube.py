import time
from machine import Pin

heart1=[0x00,0x18,0x3c,0x7e,0xff,0xff,0x66,0x00]
heart2=[0x00,0x00,0x18,0x3c,0x7e,0x66,0x00,0x00]
heart3=[0x00,0x00,0x00,0x18,0x3c,0x00,0x00,0x00]

input1=Pin(19,Pin.OUT)
input2=Pin(23,Pin.OUT)
input3=Pin(18,Pin.OUT)
input4=Pin(0 ,Pin.OUT)

enable1=Pin(21,Pin.OUT)
enable2=Pin(22,Pin.OUT)
enable3=Pin(14,Pin.OUT)
enable4=Pin(4 ,Pin.OUT)

output1=Pin(25,Pin.OUT)
output2=Pin(26,Pin.OUT)
output3=Pin(27,Pin.OUT)
output4=Pin(9 ,Pin.OUT)
output5=Pin(10,Pin.OUT)
output6=Pin(13,Pin.OUT)
output7=Pin(5 ,Pin.OUT)
output8=Pin(2 ,Pin.OUT)

class lightcube():
  def c_output(self,num):
    output1.value(num&0x01)
    output2.value(num&0x02)
    output3.value(num&0x04)
    output4.value(num&0x08)
    output5.value(num&0x10)
    output6.value(num&0x20)
    output7.value(num&0x40)
    output8.value(num&0x80)

  def c_input(self,num):
    input1.value(num&0x01)
    input2.value(num&0x02)
    input3.value(num&0x04)
    input4.value(num&0x08)
 
  def c_enable(self,num):
    enable1.value(num&0xe)
    enable2.value(num&0xd)
    enable3.value(num&0xb)
    enable4.value(num&0x7)

  def c_light(self,dec,line,num):
    self.c_enable(dec)
    self.c_input(line)
    self.c_output(num)
    self.c_output(0x00)

  def show_circle(self,layer,t):
    c1=0+layer
    c2=8+layer
    i=0
    while i<t:
      self.c_light(1,c1,0x00)
      i+=1
    i=0
    while i<t:
      self.c_light(1,c1,0x01)
      i+=1
    i=0
    while i<t:
      self.c_light(1,c1,0x03)
      i+=1
    i=0
    while i<t:
      self.c_light(1,c1,0x07)
      i+=1
    i=0
    while i<t:
      self.c_light(1,c1,0x0f)
      i+=1
    i=0
    while i<t:
      self.c_light(1,c1,0x1f)
      i+=1
    i=0
    while i<t:
      self.c_light(1,c1,0x3f)
      i+=1
    i=0
    while i<t:
      self.c_light(1,c1,0x7f)
      i+=1
    i=0
    while i<t:
      self.c_light(1,c1,0xff)
      i+=1
    i=0
    while i<t:
      self.c_light(1,c1,0xfe)
      self.c_light(1,c2,0x80)
      i+=1
    i=0
    while i<t:
      self.c_light(1,c1,0xfc)
      self.c_light(1,c2,0x80)
      self.c_light(2,c1,0x80)
      i+=1
    i=0 
    while i<t:
      self.c_light(1,c1,0xf8)
      self.c_light(1,c2,0x80)
      self.c_light(2,c1,0x80)
      self.c_light(2,c2,0x80)
      i+=1
    i=0 
    while i<t:
      self.c_light(1,c1,0xf0)
      self.c_light(1,c2,0x80)
      self.c_light(2,c1,0x80)
      self.c_light(2,c2,0x80)
      self.c_light(4,c1,0x80)
      i+=1
    i=0 
    while i<t:
      self.c_light(1,c1,0xe0)
      self.c_light(1,c2,0x80)
      self.c_light(2,c1,0x80)
      self.c_light(2,c2,0x80)
      self.c_light(4,c1,0x80)
      self.c_light(4,c2,0x80)
      i+=1
    i=0 
    while i<t:
      self.c_light(1,c1,0xc0)
      self.c_light(1,c2,0x80)
      self.c_light(2,c1,0x80)
      self.c_light(2,c2,0x80)
      self.c_light(4,c1,0x80)
      self.c_light(4,c2,0x80)
      self.c_light(8,c1,0x80)
      i+=1
    i=0 
    while i<t:
      self.c_light(1,c1,0x80)
      self.c_light(1,c2,0x80)
      self.c_light(2,c1,0x80)
      self.c_light(2,c2,0x80)
      self.c_light(4,c1,0x80)
      self.c_light(4,c2,0x80)
      self.c_light(8,c1,0x80)
      self.c_light(8,c2,0x80)
      i+=1
    i=0
    while i<t:
      self.c_light(1,c2,0x80)
      self.c_light(2,c1,0x80)
      self.c_light(2,c2,0x80)
      self.c_light(4,c1,0x80)
      self.c_light(4,c2,0x80)
      self.c_light(8,c1,0x80)
      self.c_light(8,c2,0xc0)
      i+=1
    i=0
    while i<t:
      self.c_light(2,c1,0x80)
      self.c_light(2,c2,0x80)
      self.c_light(4,c1,0x80)
      self.c_light(4,c2,0x80)
      self.c_light(8,c1,0x80)
      self.c_light(8,c2,0xe0)
      i+=1
    i=0
    while i<t:
      self.c_light(2,c2,0x80)
      self.c_light(4,c1,0x80)
      self.c_light(4,c2,0x80)
      self.c_light(8,c1,0x80)
      self.c_light(8,c2,0xf0)
      i+=1
    i=0
    while i<t:
      self.c_light(4,c1,0x80)
      self.c_light(4,c2,0x80)
      self.c_light(8,c1,0x80)
      self.c_light(8,c2,0xf8)
      i+=1
    i=0
    while i<t:
      self.c_light(4,c2,0x80)
      self.c_light(8,c1,0x80)
      self.c_light(8,c2,0xfc)
      i+=1
    i=0
    while i<t:
      self.c_light(8,c1,0x80)
      self.c_light(8,c2,0xfe)
      i+=1
    while i<t:
      self.c_light(8,c2,0xff)
      i+=1
    i=0
    while i<t:
      self.c_light(8,c1,0x01)
      self.c_light(8,c2,0x7f)
      i+=1
    i=0
    while i<t:
      self.c_light(4,c2,0x01)
      self.c_light(8,c1,0x01)
      self.c_light(8,c2,0x3f)
      i+=1
    i=0
    while i<t:
      self.c_light(4,c1,0x01)
      self.c_light(4,c2,0x01)
      self.c_light(8,c1,0x01)
      self.c_light(8,c2,0x1f)
      i+=1
    i=0  
    while i<t:
      self.c_light(2,c2,0x01)
      self.c_light(4,c1,0x01)
      self.c_light(4,c2,0x01)
      self.c_light(8,c1,0x01)
      self.c_light(8,c2,0x0f)
      i+=1
    i=0  
    while i<t:
      self.c_light(2,c2,0x01)
      self.c_light(2,c1,0x01)
      self.c_light(4,c1,0x01)
      self.c_light(4,c2,0x01)
      self.c_light(8,c1,0x01)
      self.c_light(8,c2,0x07)
      i+=1
    i=0
    while i<t:
      self.c_light(1,c2,0x01)
      self.c_light(2,c2,0x01)
      self.c_light(2,c1,0x01)
      self.c_light(4,c1,0x01)
      self.c_light(4,c2,0x01)
      self.c_light(8,c1,0x01)
      self.c_light(8,c2,0x03)
      i+=1
    i=0
    while i<t:
      self.c_light(1,c2,0x01)
      self.c_light(1,c1,0x01)
      self.c_light(2,c2,0x01)
      self.c_light(2,c1,0x01)
      self.c_light(4,c1,0x01)
      self.c_light(4,c2,0x01)
      self.c_light(8,c1,0x01)
      self.c_light(8,c2,0x01)
      i+=1

  def show_cross(self,t):
    for j in range(7,15):
      i=0
      while i<t:
        self.c_light(0,15-j,0xff)
        self.c_light(0,j   ,0xff)
        i+=1
    for j in range(7,16):
      i=0
      while i<t:
        self.c_light(0,22-j,0xff)
        self.c_light(0,j-7 ,0xff)
        i+=1

  def show_heart(self,t):
    i=0
    while i<t:
       for j in range(0,7):
        self.c_light(1,j ,heart1[j])
        i+=1
    i=0 
    while i<t:
       for j in range(8,15):
        self.c_light(1,j ,heart1[j-8])
        i+=1
    i=0
    while i<t:
       for j in range(0,7):
        self.c_light(2,j ,heart1[j])
        i+=1
    i=0
    while i<t:
       for j in range(8,15):
        self.c_light(2,j ,heart2[j-8])
        i+=1
    i=0
    while i<t:
       for j in range(0,7):
        self.c_light(4,j ,heart2[j])
        i+=1
    i=0
    while i<t:
       for j in range(8,15):
        self.c_light(4,j ,heart2[j-8])
        i+=1
    i=0
    while i<t:
       for j in range(0,7):
        self.c_light(8,j ,heart3[j])
        i+=1
    i=0
    while i<t:
       for j in range(8,15):
        self.c_light(8,j ,heart3[j-8])
        i+=1
    i=0
    while i<t:
       for j in range(0,7):
        self.c_light(8,j ,heart3[j])
        i+=1
    i=0
    while i<t:
       for j in range(8,15):
        self.c_light(4,j ,heart2[j-8])
        i+=1
    i=0
    while i<t:
       for j in range(0,7):
        self.c_light(4,j ,heart2[j])
        i+=1
    i=0
    while i<t:
       for j in range(8,15):
        self.c_light(2,j ,heart2[j-8])
        i+=1
    i=0
    while i<t:
       for j in range(0,7):
        self.c_light(2,j ,heart1[j])
        i+=1
    i=0 
    while i<t:
       for j in range(8,15):
        self.c_light(1,j ,heart1[j-8])
        i+=1
    i=0
    while i<t:
       for j in range(0,7):
        self.c_light(1,j ,heart1[j])
        i+=1
