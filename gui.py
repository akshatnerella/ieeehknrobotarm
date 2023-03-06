from tkinter import *
#All functions here
def rotate_base(angle):
    return
def rotate_elbow(angle):
    return




#GUI Part
root = Tk()
root.geometry("1000x1000")
root.title("HKN Robot Arm")
base_motor = Scale(root, command = rotate_base, to = 175, 
                  orient = HORIZONTAL, length = 400, label = 'Base Servo')
base_motor.pack(anchor = CENTER)
elbow_motor = Scale(root, command = rotate_elbow, to = 175, 
                  orient = HORIZONTAL, length = 400, label = 'Elbow Servo')
elbow_motor.pack(anchor = CENTER)
root.mainloop() #Default statement