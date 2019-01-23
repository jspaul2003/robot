#RUN THIS: sudo python3 chunga1.py

import explorerhat as e #refers to the explorer hat. we ll be calling it e
import keyboard as kb
from time import sleep
#because java is so good:
true = True
false = False

while True:
    if kb.is_pressed('esc'):
        break
    if kb.is_pressed('a'):
        e.motor.one.forwards(100)
        e.motor.two.stop()
    elif kb.is_pressed('d'):
        e.motor.two.forwards(100)
        e.motor.one.stop()
    elif kb.is_pressed('w'):
        e.motor.forwards(100)
    elif kb.is_pressed('s'):
        e.motor.backwards(100)
    else:
        e.motor.one.stop()
        e.motor.two.stop()
    
e.motor.stop()
