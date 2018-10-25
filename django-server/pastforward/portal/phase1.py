from Arduino import Arduino
import time

board = Arduino('9600',port="/dev/ttyACM1") #plugged in via USB, serial com at rate 9600
board.pinMode(9, "OUTPUT")
board.pinMode(3, "INPUT")

f=0
c = 0
while c < 3:
    r=board.digitalRead(3)

    while (r==1):
    	
    	if(f==0):
    		c += 1
    		file = open("portal/output1.txt", 'a')
    		file.write("Switch is ON\n")
    		file.close()
    		f=1
        r=board.digitalRead(3)
        board.digitalWrite(9,"HIGH")
        print(board.analogRead(3))
        #file.write("this is line" + str(r))
    board.digitalWrite(9,"LOW")
    if(f==1):

    	file = open("portal/output1.txt", 'a')
    	file.write("Switch is OFF\n")
    	file.close()
    	f=0
    

