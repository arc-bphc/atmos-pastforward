from Arduino import Arduino
import time

board = Arduino('9600')
r = 9
board.Servos.attach(r)
while True:
    board.Servos.write(r, 15)
    time.sleep(2)  # wait for 2 seconds at 15 degree
    board.Servos.write(r, 120)
    time.sleep(2)  # wait for 2 seconds at 120 degree
board.Servos.detach(r)
