from Arduino import Arduino
import time
import random

ar = [[1,4,3,2,5,8,7,6,9,10],[2,5,6,9,1,4,3,8,10,7],[7,9,2,5,1,8,6,3,10,4]]
switch=[1,2,3,4,5,6,7,8,9,10]
gates_led=[11,12,13,14,15,16,17,18,19,20]
gates = [21,22,23,24,25,26,27,28,29,30]
gates_ir = [35,36,37,38,39,40,41,42,43,44]
board.pinMode(31,"INPUT") # IR sensor pin1
board.pinMode(32,"INPUT") # IR sensor pin2
board.pinMode(33,"INPUT") # IR sensor pin3
board.pinMode(34,"INPUT") # Infinity stone
penalty=5
time =[None]*10   #ith element will store the time for which the ith gate need to be opened
for x in range(10):
	board.Servos.attach(gates[x])
r=random.choice([0,1,2])
while True:
	while (board.digitalRead(31)):
		pass
		#delay
	main_start = time.time()
	while(board.digitalRead(34)):
		for x in range(10):
			i=0
			while(board.digitalRead(switch[x])==1):
				if(i==0):
					st=time.time()
					i=1
				board.digitalWrite(gates_led[ar[r][x]-1],"HIGH")
			board.digitalWrite(gates_led[ar[r][x]-1],"LOW")
			if(i==1):
				en=time.time()
				time[ar[r][x]-1] = [en-st,ar[r][x]] # [time,gate_number]
				break
	sort(time)
	for x in range(10):
		if(time[x][0]==1000):
			break
		board.Servos.write(gates[time[x][1]-1],100)
		flag=0
		s1 = time.time();
        while((time.time()-s1)<(time[x][0]+0.1)):
        	if(board.digitalRead(gates_ir[time[x][1]-1])==1):
        		flag=1
        board.Servos.write(gates[time[x][1]-1],0)
        if(flag==0):
        	board.Servos.write(gates[time[x][1]-1],100)
        	while(board.digitalRead(gates_ir[time[x][1]-1])!=1):
        		pass
        	board.Servos.write(gates[time[x][1]-1],0)
        	penalty = penalty * 2
	while(board.digitalRead(31)==0 & board.digitalRead(32)==0 & board.digitalRead(33)==0):
		pass    
	main_end = time.time()
	print (main_end - main_start)+penalty
	exit()