from Arduino import Arduino
import time

board = Arduino('9600')

#the values represent the pin number for the switch for the gate at that index
switches = [5,9,8,1,3,4,6,7,2,10]

#list for storing the times when the switches are pressed and released
times = [[]*10]

#noting down the time when the round starts
round_start = time.time()

while True:

    for (i, switch) in enumerate(switches):
        if(board.digitalRead(switch) == HIGH):
            start = time.time()
            while(board.digitalRead(switch)==HIGH):
                pass
            stop = time.time()
            both = [start, stop]
            times[i] = both 