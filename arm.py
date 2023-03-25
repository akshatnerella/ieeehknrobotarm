import pyfirmata #to interface w the arduino
from tkinter import * #gui stuff
import pygame
from math import acos, asin, degrees, pi
from statistics import mean

def rotate_base(angle):
    pin9.write(angle)


def rotate_elbow(angle):
    pin8.write(angle)

def main():
    global pin9
    global pin8
    
    board=pyfirmata.Arduino('COM7')

    iter8 = pyfirmata.util.Iterator(board)
    iter8.start()

    pin9 = board.get_pin('d:9:s')
    pin8 = board.get_pin('d:8:s')
    pin7 = board.get_pin('d:7:p')

    pygame.init()
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    clock = pygame.time.Clock()

    for joystick in joysticks:
        joystick.init()

    history_length = 10
    history = [0]*history_length
    history_position = 0
    weights = [0]*history_length

    base_history_length = 10
    base_history = [0]*base_history_length
    base_history_position = 0
    base_weights = [0]*base_history_length

    while True:
        clock.tick(10)
        for event in pygame.event.get():
            history_position = (history_position + 1) % history_length
            base_history_position = (base_history_position + 1) % base_history_length
            for joystick in joysticks:
                x = joystick.get_axis(0)
                y = joystick.get_axis(1)
                angle = acos(x)
                # if y > 0:
                #     angle += pi
                angle = degrees(angle)
                history[history_position] = angle
                weights[history_position] = x**2 + y**2
                angle = 0
                for point in range(history_length):
                    angle += history[point] * weights[point]
                total_weight = sum(weights)
                if total_weight > 0:
                    angle /= sum(weights)
                    rotate_base(angle)
                    rotate_elbow(180 - angle)


                x = joystick.get_axis(2)
                y = joystick.get_axis(3)
                angle = acos(x)
                # if y > 0:
                #     angle += pi
                angle = degrees(angle)
                base_history[base_history_position] = angle
                base_weights[base_history_position] = x**2 + y**2
                angle = 0
                for point in range(base_history_position):
                    angle += base_history[point] * base_weights[point]
                total_weight = sum(base_weights)
                if total_weight > 0:
                    angle /= sum(base_weights)
                    print(angle)
                    pin7.write(angle / 180)


    pygame.joystick.quit()

main()