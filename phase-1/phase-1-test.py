from Arduino import Arduino
import time

board = Arduino('9600') #plugged in via USB, serial com at rate 9600
board.pinMode(9, "OUTPUT")
board.pinMode(3, "INPUT")
while True:
    r=board.digitalRead(3)
    while (r==1):
        r=board.digitalRead(3)
        board.digitalWrite(9,"HIGH")
    board.digitalWrite(9,"LOW")