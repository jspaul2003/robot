#BigChungusDriveKeyboardTesting
#Jean-Sebastien Paul
#2/10/2020
#About:
#Learning about using RPi.GPIO to control mercanum wheels. Uses Keyboard over controller to better understand whats going on

# Import required modules
import time
import RPi.GPIO as GPIO
import keyboard as kb
from time import sleep

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

GPIO.setmode(GPIO.BCM)
GPIO.setup(Ain1,GPIO.OUT)
GPIO.setup(Ain2,GPIO.OUT)
GPIO.setup(Ain3,GPIO.OUT)
GPIO.setup(Ain4,GPIO.OUT)
GPIO.output(Ain1,GPIO.LOW)
GPIO.output(Ain2,GPIO.LOW)
GPIO.output(Ain3,GPIO.LOW)
GPIO.output(Ain4,GPIO.LOW)

GPIO.setup(Bin1,GPIO.OUT)
GPIO.setup(Bin2,GPIO.OUT)
GPIO.setup(Bin3,GPIO.OUT)
GPIO.setup(Bin4,GPIO.OUT)
GPIO.output(Bin1,GPIO.LOW)
GPIO.output(Bin2,GPIO.LOW)
GPIO.output(Bin3,GPIO.LOW)
GPIO.output(Bin4,GPIO.LOW)

while True:
  if kb.is_pressed('esc'):
        break
  if kb.is_pressed('w'):
        GPIO.output(Ain1,GPIO.HIGH)
        GPIO.output(Ain3,GPIO.HIGH)
        GPIO.output(Bin1,GPIO.HIGH)
        GPIO.output(Bin3,GPIO.HIGH)
        GPIO.output(Ain2,GPIO.LOW)
        GPIO.output(Ain4,GPIO.LOW)
        GPIO.output(Bin2,GPIO.LOW)
        GPIO.output(Bin4,GPIO.LOW)
  if kb.is_pressed('s'):
        GPIO.output(Ain1,GPIO.LOW)
        GPIO.output(Ain3,GPIO.LOW)
        GPIO.output(Bin1,GPIO.LOW)
        GPIO.output(Bin3,GPIO.LOW)
        GPIO.output(Ain2,GPIO.HIGH)
        GPIO.output(Ain4,GPIO.HIGH)
        GPIO.output(Bin2,GPIO.HIGH)
        GPIO.output(Bin4,GPIO.HIGH)
  else:
        GPIO.output(Ain1,GPIO.LOW)
        GPIO.output(Ain3,GPIO.LOW)
        GPIO.output(Bin1,GPIO.LOW)
        GPIO.output(Bin3,GPIO.LOW)
        GPIO.output(Ain2,GPIO.LOW)
        GPIO.output(Ain4,GPIO.LOW)
        GPIO.output(Bin2,GPIO.LOW)
        GPIO.output(Bin4,GPIO.LOW)
