import pyfirmata #to interface w the arduino
from tkinter import * #gui stuff
import pygame

def rotate_base(angle):
    pin9.write(angle)


def rotate_elbow(angle):
    pin8.write(angle)

#declaring all the pins
global pin9 #pin_elbow 
global pin8 #pin_base
    
board=pyfirmata.Arduino('COM7') #update each time connected to pc
iter8 = pyfirmata.util.Iterator(board)
iter8.start()

#pin assignment
pin9 = board.get_pin('d:9:s')
pin8 = board.get_pin('d:8:s')

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


#Joystick part
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
j = pygame.joystick.Joystick(0) #added name to joystick
pygame.init()
clock = pygame.time.Clock()

#control loop
while True:
    a = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.JOYBUTTONDOWN: #A0 B1 X2 Y3
            if pygame.joystick.Joystick(0).get_button(0):
                #code here
                print(event)
        if event.type == pygame.JOYAXISMOTION:
        #get_axis(0) is LR, get_axis(1) is UD
            if j.get_axis(0) >= 0.5: #right
                print(event)
                if a < 256:
                    a +=1
                rotate_base(a)
            if j.get_axis(0) <= -0.5: #left
                print(event)
                if a > 0:
                    a -= 1
                rotate_base(a)