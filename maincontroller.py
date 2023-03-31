import pyfirmata #to interface w the arduino
from tkinter import * #gui stuff
import pygame #controller interfacing

###########SETUP################
#Important Variables
COM = 'COM5' #Update each time Arduino is connected

#Declaring all the pins
global pin9 #pin_elbow1 
global pin8 #pin_base

board=pyfirmata.Arduino(COM)
iter8 = pyfirmata.util.Iterator(board)
iter8.start()

#pin assignment
pin9 = board.get_pin('d:9:s')
pin8 = board.get_pin('d:8:s')

#Joystick part
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
j = pygame.joystick.Joystick(0) #added name to joystick
pygame.init()
clock = pygame.time.Clock()

################FUNCTIONS##############
def map_range(value, from_min, from_max, to_min, to_max):
    # Map a value from one range to another
    return (value - from_min) * (to_max - to_min) / (from_max - from_min) + to_min

def rotate_base(angle):
    # Map joystick input to servo angle range
    mapped_angle = int(map_range(angle, -1, 1, 0, 180))
    pin9.write(mapped_angle)

def rotate_elbow(angle):
    # Map joystick input to servo angle range
    mapped_angle = int(map_range(angle, -1, 1, 0, 180))
    pin8.write(mapped_angle)

##############MAIN##################
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit the program if the window is closed
            pygame.quit()
            sys.exit()

    # Get the current joystick position
    x_axis = j.get_axis(0)
    y_axis = j.get_axis(1)

    # Control the base servo with the left joystick
    rotate_base(x_axis)

    # Control the elbow servo with the right joystick
    rotate_elbow(y_axis)

    # Wait for a short time to avoid overwhelming the Arduino board
    pygame.time.wait(10)

##########SCRATCH############
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

