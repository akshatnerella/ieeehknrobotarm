import pyfirmata #to interface w the arduino
from tkinter import * #gui stuff

def rotate_base(angle):
    pin9.write(angle)


def rotate_elbow(angle):
    pin8.write(angle)

def main():
    #declaring all the pins
    global pin9 #pin_elbow 
    global pin8 #pin_base
    
    board=pyfirmata.Arduino('COM7') #update each time connected to pc
    iter8 = pyfirmata.util.Iterator(board)
    iter8.start()

    #pin assignment
    pin9 = board.get_pin('d:9:s')
    pin8 = board.get_pin('d:8:s')

    root = Tk()
    root.geometry("1000x1000")
    root.title("IEEE-HKN Robot Arm Controller")

    base_motor = Scale(root, command = rotate_base, to = 175, 
                  orient = HORIZONTAL, length = 400, label = 'Base')
    base_motor.pack(anchor = CENTER)

    elbow_motor = Scale(root, command = rotate_elbow, to = 175, 
                  orient = HORIZONTAL, length = 400, label = 'Elbow')
    elbow_motor.pack(anchor = CENTER)

    root.mainloop()

main()