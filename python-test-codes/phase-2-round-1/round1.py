import random

ar = [[1,4,3,2,5,8,7,6,9,10],[2,5,6,9,1,4,3,8,10,7],[7,9,2,5,1,8,6,3,10,4]]

switch=[1,2,3,4,5,6,7,8,9,10]
gates=[11,12,13,14,15,16,17,18,19,20]

time =[None]*10   #ith element will store the time for which the ith gate need to be opened
#this should be replaced by a pair
r=random.choice([0,1,2])
while True:
	i=board.digitalRead(21)
	while (i):
		i=board.digitalRead(21)
		#delay
	start = time.time()
	while(board.digitalRead(21)==0):
		for x in range(10):
			i=0
			while(board.digitalRead(switch[x])==1):
				if(i==0):
					st=time.time()
					i=1
				board.digitalWrite(gates[ar[r][x]-1],"HIGH")
			board.digitalWrite(gates[ar[r][x]-1],"LOW")
			if(i==1):
				en=time.time()
				#time[ar[r][x]-1]=en-st
				time[ar[r][x]-1] = [en-st,ar[r][x]-1]

	end = time.time()
	print end-start
	exit()
