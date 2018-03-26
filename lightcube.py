import time
import light_cube
import lightcube_show
from machine import Pin
  
LC=light_cube.lightcube()
LC_S=lightcube_show.lightcube__show()

while True:

  LC_S.show_print(250,lightcube_show.num_9 )
  LC_S.show_print(250,lightcube_show.num_8 )
  LC_S.show_print(250,lightcube_show.num_7 )
  LC_S.show_print(200,lightcube_show.num_6 )
  LC_S.show_print(200,lightcube_show.num_5 )
  LC_S.show_print(200,lightcube_show.num_4 )
  LC_S.show_print(100,lightcube_show.num_3 )
  LC_S.show_print(100,lightcube_show.num_2 )
  LC_S.show_print(100,lightcube_show.num_1 )
  LC_S.show_print(100,lightcube_show.num_0 )
  LC_S.show_print(200,lightcube_show.word_D)
  LC_S.show_print(200,lightcube_show.word_F)
  LC_S.show_print(200,lightcube_show.word_R)
  LC_S.show_print(200,lightcube_show.word_O)
  LC_S.show_print(200,lightcube_show.word_B)
  LC_S.show_print(200,lightcube_show.word_O)
  LC_S.show_print(200,lightcube_show.word_T)
  
  i=0
  while i<2: 
    for j in range(0,8):
      LC.show_circle(7-j,8)
    for j in range(0,8):
      LC.show_circle(j  ,8)
    i+=1

  i=0  
  while i<1000:
    LC.c_light(0,7 ,0xff)
    LC.c_light(0,15,0xff)
    i+=1
  LC_S.show_fall(30)
  i=0
  while i<10:
    LC.show_cross(50)
    i+=1
 
  i=0
  while i<5:
    LC_S.show_cube(200)
    i+=1
    
  i=0  
  while i<10:
    for j in range (0,16):
      LC.c_light(0,j ,0xff)
    time.sleep(0.1)
    for j in range (0,16):
      LC.c_light(0,j ,0x00)
    i+=1
    
  i=0  
  while i<600:
    for j in range (0,16):
      LC.c_light(0,j ,0xff)
    i+=1  

  i=0
  while i<6:
    LC.show_heart(200)
    i+=1
