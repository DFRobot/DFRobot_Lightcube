import time
from machine import Pin

num_0=[0x00,0x3C,0x24,0x24,0x24,0x24,0x24,0x3C]
num_1=[0x00,0x7C,0x10,0x10,0x10,0x14,0x18,0x10]
num_2=[0x00,0x7C,0x04,0x04,0x7C,0x40,0x40,0x7C]
num_3=[0x00,0x7C,0x40,0x40,0x7C,0x40,0x40,0x7C]
num_4=[0x00,0x40,0x40,0x40,0x7C,0x44,0x44,0x44]
num_5=[0x00,0x7C,0x40,0x40,0x7C,0x04,0x04,0x7C]
num_6=[0x00,0x7C,0x44,0x44,0x7C,0x04,0x04,0x7C]
num_7=[0x00,0x40,0x40,0x40,0x40,0x40,0x40,0x7C]
num_8=[0x00,0x7C,0x44,0x44,0x7C,0x44,0x44,0x7C]
num_9=[0x00,0x7C,0x40,0x40,0x7C,0x44,0x44,0x7C]

word_A=[0x00,0x44,0x44,0x7C,0x44,0x44,0x28,0x10]
word_B=[0x00,0x3C,0x44,0x44,0x3C,0x44,0x44,0x3C]
word_C=[0x00,0x38,0x44,0x04,0x04,0x04,0x44,0x38]
word_D=[0x00,0x1C,0x24,0x44,0x44,0x44,0x24,0x1C]
word_E=[0x00,0x3C,0x04,0x04,0x3C,0x04,0x04,0x3C]
word_F=[0x00,0x04,0x04,0x04,0x3C,0x04,0x04,0x7C]
word_G=[0x00,0xB8,0xC4,0xE4,0x04,0x04,0x44,0x38]
word_H=[0x00,0x44,0x44,0x44,0x7C,0x44,0x44,0x44]
word_I=[0x00,0x38,0x10,0x10,0x10,0x10,0x10,0x38]
word_J=[0x00,0x18,0x14,0x10,0x10,0x10,0x10,0x7C]
word_K=[0x00,0x44,0x24,0x14,0x0C,0x14,0x24,0x44]
word_L=[0x00,0x3C,0x04,0x04,0x04,0x04,0x04,0x04]
word_M=[0x00,0x82,0x82,0x82,0x92,0xAA,0xC6,0x82]
word_N=[0x00,0x82,0xC2,0xA2,0x92,0x8A,0x86,0x82]
word_O=[0x00,0x38,0x44,0x44,0x44,0x44,0x44,0x38]
word_P=[0x00,0x04,0x04,0x04,0x3C,0x44,0x44,0x3C]
word_Q=[0x00,0x5C,0x22,0x32,0x22,0x22,0x22,0x1C]
word_R=[0x00,0x44,0x24,0x14,0x3C,0x44,0x44,0x3C]
word_S=[0x00,0x3C,0x40,0x40,0x38,0x04,0x04,0x78]
word_T=[0x00,0x10,0x10,0x10,0x10,0x10,0x10,0x7C]
word_U=[0x00,0x38,0x44,0x44,0x44,0x44,0x44,0x44]
word_V=[0x00,0x10,0x28,0x44,0x44,0x44,0x44,0x44]
word_W=[0x00,0x82,0xC6,0xAA,0x92,0x82,0x82,0x82]
word_X=[0x00,0x82,0x44,0x28,0x10,0x28,0x44,0x82]
word_Y=[0x00,0x10,0x10,0x10,0x10,0x28,0x44,0x44]
word_Z=[0x00,0xFE,0x04,0x08,0x10,0x20,0x40,0xFE]

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

class lightcube__show():
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

  def show_fall(self,t):
    for j in range(0,8):
      i=0
      while i<t:
        self.c_light(0,7   ,0xff)
        self.c_light(0,15  ,0xf0)
        self.c_light(0,15-j,0x0f)
        i+=1  
    for j in range(0,8):
      i=0  
      while i<t:
        self.c_light(0,15 ,0xf0)
        self.c_light(0,8  ,0x0f)
        self.c_light(0,7  ,0x0f)
        self.c_light(0,7-j,0xf0)
        i+=1
    for j in range(0,8):
      i=0  
      while i<t:
        self.c_light(0,15  ,0xf0)
        self.c_light(0,8   ,0x0f)
        self.c_light(0,7-j ,0x0f)
        self.c_light(0,0   ,0xf0)
        i+=1
    for j in range(0,8):
      i=0
      while i<t:
        self.c_light(0,15-j,0xf0)
        self.c_light(0,8   ,0x0f)
        self.c_light(0,0   ,0xff)
        i+=1

  def show_cube(self,t):
    for j in range(2,9):
      i=0
      S_length=0xff
      S_length>>=8-j
      S_width=(0x1)+(0x1<<(j-1))
      while i<t:
        self.c_light(1,7  ,S_length)
        self.c_light(1,8-j,S_length)
        if j == 2:
          self.c_light(1,15,S_length)
          self.c_light(1,14,S_length)
          i+=4
        if j == 3:
          self.c_light(1,15,S_width )
          self.c_light(1,13,S_width )
          self.c_light(1,6 ,S_width )
          self.c_light(2,6 ,S_width )
          self.c_light(2,7 ,S_length)
          self.c_light(2,5 ,S_length)
          i+=8
        if j == 4:
          self.c_light(1,15,S_width )
          self.c_light(1,12,S_width )
          self.c_light(2,7 ,S_width )
          self.c_light(2,4 ,S_width )
          self.c_light(1,6 ,S_width )
          self.c_light(1,5 ,S_width )
          self.c_light(2,14,S_width )
          self.c_light(2,13,S_width )
          self.c_light(2,15,S_length)
          self.c_light(2,12,S_length)
          i+=12
        if j == 5:
          self.c_light(1,15,S_width )
          self.c_light(1,11,S_width )
          self.c_light(2,7 ,S_width )
          self.c_light(2,3 ,S_width )
          self.c_light(2,15,S_width )
          self.c_light(2,11,S_width )
          self.c_light(1,6 ,S_width )
          self.c_light(1,5 ,S_width )
          self.c_light(1,4 ,S_width )
          self.c_light(4,6 ,S_width )
          self.c_light(4,5 ,S_width )
          self.c_light(4,4 ,S_width )
          self.c_light(4,7 ,S_length)
          self.c_light(4,3 ,S_length)
          i+=16
        if j == 6:
          self.c_light(1,15,S_width )
          self.c_light(1,10,S_width )
          self.c_light(2,7 ,S_width )
          self.c_light(2,2 ,S_width )
          self.c_light(2,15,S_width )
          self.c_light(2,10,S_width )
          self.c_light(4,7 ,S_width )
          self.c_light(4,2 ,S_width )
          self.c_light(1,6 ,S_width )
          self.c_light(1,5 ,S_width )
          self.c_light(1,4 ,S_width )
          self.c_light(1,3 ,S_width )
          self.c_light(4,14,S_width )
          self.c_light(4,13,S_width )
          self.c_light(4,12,S_width )
          self.c_light(4,11,S_width )
          self.c_light(4,15,S_length)
          self.c_light(4,10,S_length)
          i+=20
        if j == 7:
          self.c_light(1,15,S_width )
          self.c_light(1,9 ,S_width )
          self.c_light(2,7 ,S_width )
          self.c_light(2,1 ,S_width )
          self.c_light(2,15,S_width )
          self.c_light(2,9 ,S_width )
          self.c_light(4,7 ,S_width )
          self.c_light(4,1 ,S_width )
          self.c_light(4,15,S_width )
          self.c_light(4,9 ,S_width )
          self.c_light(1,6 ,S_width )
          self.c_light(1,5 ,S_width )
          self.c_light(1,4 ,S_width )
          self.c_light(1,3 ,S_width )
          self.c_light(1,2 ,S_width )
          self.c_light(8,6 ,S_width )
          self.c_light(8,5 ,S_width )
          self.c_light(8,4 ,S_width )
          self.c_light(8,3 ,S_width )
          self.c_light(8,2 ,S_width )
          self.c_light(8,7 ,S_length)
          self.c_light(8,1 ,S_length)
          i+=24
        if j == 8:
          self.c_light(1,15,S_width )
          self.c_light(1,8 ,S_width )
          self.c_light(2,7 ,S_width )
          self.c_light(2,0 ,S_width )
          self.c_light(2,15,S_width )
          self.c_light(2,8 ,S_width )
          self.c_light(4,7 ,S_width )
          self.c_light(4,0 ,S_width )
          self.c_light(4,15,S_width )
          self.c_light(4,8 ,S_width )
          self.c_light(8,7 ,S_width )
          self.c_light(8,0 ,S_width )
          self.c_light(1,6 ,S_width )
          self.c_light(1,5 ,S_width )
          self.c_light(1,4 ,S_width )
          self.c_light(1,3 ,S_width )
          self.c_light(1,2 ,S_width )
          self.c_light(1,1 ,S_width )
          self.c_light(8,14,S_width )
          self.c_light(8,13,S_width )
          self.c_light(8,12,S_width )
          self.c_light(8,11,S_width )
          self.c_light(8,10,S_width )
          self.c_light(8,9 ,S_width )
          self.c_light(8,15,S_length)
          self.c_light(8,8 ,S_length)
          i+=28

  def show_print(self,t,data):
    i=0
    while i<t:
       for j in range(0,8):
        self.c_light(1,j ,data[j])
        i+=1
    i=0 
    while i<t:
       for j in range(8,16):
        self.c_light(1,j ,data[j-8])
        i+=1
    i=0
    while i<t:
       for j in range(0,8):
        self.c_light(2,j ,data[j])
        i+=1
    i=0
    while i<t:
       for j in range(8,16):
        self.c_light(2,j ,data[j-8])
        i+=1
    i=0
    while i<t:
       for j in range(0,8):
        self.c_light(4,j ,data[j])
        i+=1
    i=0
    while i<t:
       for j in range(8,16):
        self.c_light(4,j ,data[j-8])
        i+=1
    i=0
    while i<t:
       for j in range(0,8):
        self.c_light(8,j ,data[j])
        i+=1
    i=0
    while i<t:
       for j in range(8,16):
        self.c_light(8,j ,data[j-8])
        i+=1