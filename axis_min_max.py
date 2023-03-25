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

    pygame.init()
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    clock = pygame.time.Clock()

    for joystick in joysticks:
        joystick.init()

    # print(len(joysticks))
    # exit(0)
    high = -100
    low = 100

    while True:
        clock.tick(100)
        for event in pygame.event.get():
            for joystick in joysticks:
                axis = joystick.get_axis(0)
                high = max(axis, high)
                low = min(axis, low)
                print(high, low)

    pygame.joystick.quit()

main()