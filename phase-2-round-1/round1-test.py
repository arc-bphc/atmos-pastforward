from Arduino import Arduino
import time

board = Arduino('9600') #plugged in via USB, serial com at rate 9600
board.pinMode(9, "OUTPUT")
board.pinMode(3, "INPUT")
while True:
    i=0
    while (board.digitalRead(3)):
    	if(i==0):
    		st=time.time()
    		i=1
        board.digitalWrite(9,"HIGH")
    board.digitalWrite(9,"LOW")
    if(i==1):
    	end=time.time()
    	print(end-st)
    