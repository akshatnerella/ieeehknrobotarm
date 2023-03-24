import pyfirmata #to interface w the arduino
from tkinter import * #gui stuff
import pygame

def rotate_base(angle):
    pin9.write(angle)


def rotate_elbow(angle):
    pin8.write(angle)

def main():
    global pin9
    global pin8
    
    # board=pyfirmata.Arduino('COM7')

    # iter8 = pyfirmata.util.Iterator(board)
    # iter8.start()

    # pin9 = board.get_pin('d:9:s')
    # pin8 = board.get_pin('d:8:s')
    
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    clock = pygame.time.Clock()

    for joystick in joysticks:
        joystick.init()

    # print(len(joysticks))
    # exit(0)
    joysticks[0].rumble(1, 1, 2000)

    while True:
        clock.tick(10)
        for joystick in joysticks:
            print('ID:', joystick.get_instance_id(), end='  ')
            print('GUID:', joystick.get_guid(), end='  ')
            print('Power Level:', joystick.get_power_level(), end='  ')
            print('Axis:', joystick.get_numaxes(), end='  ')
            for axis in range(joystick.get_numaxes()):
                print('Axis ', axis, ': ', joystick.get_axis(axis), end='  ', sep='')
            for i in range(joystick.get_numbuttons()):
                print(joystick.get_button(i), end=' ')
            print()

    pygame.joystick.quit()

main()