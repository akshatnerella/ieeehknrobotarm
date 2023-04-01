import pyfirmata
import time

# set up the board
board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()

# set up the pins
step_pin = board.get_pin('d:10:o')
dir_pin = board.get_pin('d:11:o')
sleep_pin = board.get_pin('d:12:o')

# set the microstepping mode
board.digital[8].write(0)
board.digital[9].write(0)
board.digital[10].write(0)

# enable the driver
sleep_pin.write(1)
# rotate one full revolution in one direction
dir_pin.write(1)
for i in range(200):
    step_pin.write(1)
    time.sleep(0.005)
    step_pin.write(0)
    time.sleep(0.005)

# rotate one full revolution in the other direction
dir_pin.write(0)
for i in range(200):
    step_pin.write(1)
    time.sleep(0.005)
    step_pin.write(0)
    time.sleep(0.005)
    
sleep_pin.write(1)
# close the connection to the board
board.exit()