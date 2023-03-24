import pygame
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
j = pygame.joystick.Joystick(0) #added name to joystick
pygame.init()
clock = pygame.time.Clock()

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
            if j.get_axis(0) >= 0.5: #right
                print("right")
            if j.get_axis(0) <= -0.5: #left
                print("left")

