#BigChungusDriveKeyboardTesting2
#Jean-Sebastien Paul
#2/11/2020
#About:
#Learning about using GPI ZERO motor class to control mercanum wheels. Uses Keyboard over controller to better understand whats going on

# Import required modules
import time
import RPi.GPIO as GPIO
import gpiozero
import keyboard as kb
from time import sleep
from gpiozero import Motor

#define trues and falses to prevent slip ups from R or java
T=True
F=False
true = True
false = False

#pins for motors
A1in1=12
A1in2=16
A2in1=20
A2in2=21

B1in1=26
B1in2=19
B2in1=13
B2in2=6

A1=Motor(12,16)
A2=Motor(20,21)
B1=Motor(26,19)
B2=Motor(13,6)
Amotors=[A1,A2]
Bmotors=[B1,B2]
motors=[A1,A2,B1,B2]

while True:
  if kb.is_pressed('q'):
    for i in range(0,4):
        motors[i].stop()
    break
  if kb.is_pressed('w'):
        for i in range(0,2):
            Amotors[i].forward(speed=1)
            Bmotors[i].backward(speed=1)
  if kb.is_pressed('s'):
        for i in range(0,2):
            Bmotors[i].forward(speed=1)
            Amotors[i].backward(speed=1)
  else:
        for i in range(0,4):
            motors[i].stop()
