import pyfirmata #to interface w the arduino
from tkinter import * #gui stuff
import pygame #controller interfacing

#Important Variables
COM = 'COM7' #Update each time Arduino is connected

#Functions to control each servo
def rotate_base(angle):
    pin9.write(angle)


def rotate_elbow(angle):
    pin8.write(angle)


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

#Control loop
a = 0
#fine tune these:
joy_offset = 0.1
joy_increment = 10
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.JOYBUTTONDOWN: #A0 B1 X2 Y3
            if pygame.joystick.Joystick(0).get_button(0):
                #code here
                print(event)
        if event.type == pygame.JOYAXISMOTION:
        #get_axis(0) is LR, get_axis(1) is UD
            if j.get_axis(0) >= joy_offset: #right
                print(event)
                print(a)
                if a < 256:
                    a +=joy_increment
                rotate_base(a)
            if j.get_axis(0) <= -joy_offset: #left
                print(event)
                print(a)
                if a > 0:
                    a -= joy_increment
                rotate_base(a)


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

