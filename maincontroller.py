import pyfirmata #to interface w the arduino
from tkinter import * #gui stuff
import pygame #controller interfacing
import time

###########SETUP################
#Important Variables
COM = 'COM3' #Update each time Arduino is connected

#Declaring all the pins
#Base
global pin_base 
#Arm
global pin_elbowR  
global pin_elbowL
#Hand
global pin_thumbR
global pin_thumbL
global pin_index
global pin_middle
global pin_ring
global pin_pinky

#Boot
board=pyfirmata.Arduino(COM)
iter8 = pyfirmata.util.Iterator(board)
iter8.start()

#pin assignment
#Hand
pin_thumbR  = board.get_pin('d:2:s')
pin_thumbL  = board.get_pin('d:3:s')
pin_index   = board.get_pin('d:4:s')
pin_middle  = board.get_pin('d:5:s')
pin_ring    = board.get_pin('d:6:s')
pin_pinky   = board.get_pin('d:7:s')
#Arm
pin_elbowR = board.get_pin('d:9:s')
pin_elbowL = board.get_pin('d:8:s')
#Base
pin_base_step  = board.get_pin('d:10:o')
pin_base_dir   = board.get_pin('d:11:o')
pin_base_sleep = board.get_pin('d:12:o')


# Move servos to starting position
pin_elbowR.write(90)
pin_elbowL.write(90)

pin_base_sleep.write(1)

#Joystick setup
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
j = pygame.joystick.Joystick(0) #added name to joystick
pygame.init()
clock = pygame.time.Clock()

################ FUNCTIONS ##############
def map_range(value, from_min, from_max, to_min, to_max):
    # Map a value from one range to another
    return (value - from_min) * (to_max - to_min) / (from_max - from_min) + to_min

def rotate_base(angle):
    if angle < 0:
        pin_base_dir.write(0)
        for i in range(5):
            pin_base_step.write(1)
            time.sleep(0.005)
            pin_base_step.write(0)
            time.sleep(0.005)
    if angle > 0:
        pin_base_dir.write(1)
        for i in range(5):
            pin_base_step.write(1)
            time.sleep(0.005)
            pin_base_step.write(0)
            time.sleep(0.005)

def rotate_elbow(angle):
    # Map joystick input to servo angle range
    angleR = int(map_range(angle, -1, 1, 0, 180))
    angleL = int(map_range(angle, 1, -1, 0, 180))
    pin_elbowR.write(angleR)
    pin_elbowL.write(angleL)

def hold():
    var = 180 #fine tune this
    pin_thumbR.write(var)
    pin_thumbL.write(var)
    pin_index.write(var)
    pin_middle.write(var)
    pin_ring.write(var)
    pin_pinky.write(var)

def release():
    var = 0 # fine tune this
    pin_thumbR.write(var)
    pin_thumbL.write(var)
    pin_index.write(var)
    pin_middle.write(var)
    pin_ring.write(var)
    pin_pinky.write(var)

def testfunc():
    print("Success!")

############## MAIN ##################
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit the program if the window is closed
            pygame.quit()
            Sys.exit()
        #Buttons and Functions
        if j.get_button(0): #A
            hold()
        if j.get_button(1): #B
            release()
        
    # Get the current joystick position
    x_axis = j.get_axis(0)
    y_axis = j.get_axis(1)

    # Control the elbow servo with the right joystick
    rotate_elbow(y_axis)

    #Base Stepper
    rotate_base(x_axis)
    # Wait for a short time to avoid overload
    pygame.time.wait(10)

########## MISC ############
#Using Tkinter and PC
    # root = Tk()
    # root.geometry("1000x1000")
    # root.title("IEEE-HKN Robot Arm Controller")

    # base_motor = Scale(root, command = rotate_base, to = 175, 
    #               orient = HORIZONTAL, length = 400, label = 'Base')
    # base_motor.pack(anchor = CENTER)

    # elbow_motor = Scale(root, command = rotate_elbow, to = 175, 
    #               orient = HORIZONTAL, length = 400, label = 'Elbow')
    # elbow_motor.pack(anchor = CENTER)

    # root.mainloop()

