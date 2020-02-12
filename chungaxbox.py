#ChungaXbox
#Jean-Sebastien Paul
#2/11/2020
#About:
#Learning about using GPI ZERO motor class to control mercanum wheels. Uses controller s goin

# Import required modules
import time
import keyboard as kb
import RPi.GPIO as GPIO
import gpiozero
import pygame
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

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10


pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
    
# Get ready to print
textPrint = TextPrint()

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
            
 
    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count) )
    textPrint.indent()
    
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        textPrint.print(screen, "Joystick {}".format(i) )
        textPrint.indent()
    
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        textPrint.print(screen, "Joystick name: {}".format(name) )
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.print(screen, "Number of axes: {}".format(axes) )
        textPrint.indent()
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
        textPrint.unindent()
        
        ax = joystick.get_axis(1)
        ax1 = joystick.get_axis(0)
        if(ax<0):
            A1.forward(abs(ax))
            A2.forward(abs(ax))
            B1.backward(abs(ax))
            B2.backward(abs(ax))
        elif(ax>0):
            B1.forward(abs(ax))
            B2.forward(abs(ax))
            A1.backward(abs(ax))
            A2.backward(abs(ax))
        else:
            for i in range(0,4):
                motors[i].stop()
        if(ax==0 and ax1<0):
            A1.forward(abs(ax1))
            A2.stop()
            B1.stop()
            B2.backward(abs(ax1))
        elif(ax==0 and ax1>0):
            A2.forward(abs(ax1))
            A1.stop()
            B2.stop()
            B1.backward(abs(ax1))
        elif(ax<0 and ax1<0 and abs(ax1)>=0.01):
            print('f')
            A1.forward(abs(ax))
            A2.forward((abs(ax)/(abs(ax1)))/100)
            B2.backward(abs(ax))
            B1.backward((abs(ax)/(abs(ax1)))/100)
        elif(ax<0 and ax1>0 and abs(ax1)>=0.01):
            print('f')
            A2.forward(abs(ax))
            A1.forward((abs(ax)/(abs(ax1)))/100)
            B1.backward(abs(ax))
            B2.backward((abs(ax)/(abs(ax1)))/100)
        elif(ax>0 and ax1<0 and abs(ax1)>=0.01):
            print('back')
            A1.backward(abs(ax))
            A2.backward((abs(ax)/(abs(ax1)))/100)
            B2.forward(abs(ax))
            B1.forward((abs(ax)/(abs(ax1)))/100)
        elif(ax>0 and ax1>0 and abs(ax1)>=0.01):
            print('back')
            print((abs(ax)/(abs(ax1)))/100)
            A2.backward(abs(ax))
            A1.backward((abs(ax)/(abs(ax1)))/100)
            B1.forward(abs(ax))
            B2.forward((abs(ax)/(abs(ax1)))/100)
            
            
        
        buttons = joystick.get_numbuttons()
        textPrint.print(screen, "Number of buttons: {}".format(buttons) )
        textPrint.indent()

        for i in range( buttons ):
            button = joystick.get_button( i )
            textPrint.print(screen, "Button {:>2} value: {}".format(i,button) )
        textPrint.unindent()
            
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        textPrint.print(screen, "Number of hats: {}".format(hats) )
        textPrint.indent()

        for i in range( hats ):
            hat = joystick.get_hat( i )
            textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)) )
        textPrint.unindent()
        
        textPrint.unindent()

    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(20)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()


