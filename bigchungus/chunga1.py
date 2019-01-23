import explorerhat as e #refers to the explorer hat. we ll be calling it e
import keyboard as kb
from time import sleep
#because java is so good:
true = True
false = False

while True:
    if kb.is_pressed('a'):
        e.motor.one.forwards()
        er.motor.two.stop()
    elif kb.is_pressed('d')
        e.motor.two.forwards()
        e.motor.one.stop()
    else:
        e.motor.one.stop()
        e.motor.two.stop()
    
e.motor.stop()
