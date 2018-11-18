from arduino import Arduino
import time

board = Arduino('9600', port="/dev/ttyACM1") #plugged in via USB, serial com at rate 9600
board.pinMode(9, "OUTPUT")
board.pinMode(3, "INPUT")
print("switch1")
while True:
    print("switch2")
    r=board.digitalRead(3)

    while (r==1):
        print("switch3")
        r=board.digitalRead(3)
        board.digitalWrite(9,"HIGH")
    board.digitalWrite(9,"LOW")