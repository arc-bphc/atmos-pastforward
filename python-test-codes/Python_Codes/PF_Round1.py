from Arduino import Arduino
import time

board = Arduino('9600', port="/dev/ttyACM0") #plugged in via USB, serial com at rate 9600
board.pinMode(5, "INPUT")#entry gate sensor
board.pinMode(7, "INPUT")
time_r1 = 0

while True:

    #time start
    start = time.time()

    val = board.digitalRead(5)

    #main working loop
    while(val == 0):
            
            val = board.digitalRead(5)
            #s1 = board.digitalRead(7)
            

    #time stop
    end = time.time()
               
        
    #print(val, '\n')
    time_r1 = end - start
    print(end - start)           
    exit()
