from Arduino import Arduino
import time
import random

file = open('portal/gate.txt', 'r')
r = int(file.read())
file.close()
file = open('portal/output1.txt', 'a')
print "Round1 Started"
file.write("Gate set: " + str(r) + "\n")
file.write('Round 1 started.\n')

board = Arduino('9600', port='/dev/ttyACM1')
board.pinMode(21,"INPUT_PULLUP")

ar = [[10,3,7,5,8,2,1,9,4,6],
      [4,9,6,10,8,1,2,3,5,7],
      [10,3,7,2,9,4,1,5,6,8],
      [10,5,1,8,2,9,7,4,3,6],
      [4,10,8,1,2,3,9,6,7,5],
      [9,6,10,8,2,4,5,7,1,3],
      [10,4,5,7,1,2,9,3,6,8],
      [9,3,6,8,2,1,4,10,7,5],
      [8,6,9,1,10,4,5,7,3,2],
      [6,8,9,3,4,10,7,5,2,1]]

switch=[36,52,42,48,34,46,38,44,40,50]
gates=[7,10,6,5,4,2,8,3,11,9]


def servoClose(pin):

    if pin in [7,8,9,10]:
        board.Servos.write(pin, 170)

    else:
        board.Servos.write(pin, 10)

def closeAllGates():

    for gate in gates:
        servoClose(gate)


for x in range(10):
    board.Servos.attach(gates[x])
    board.Servos.write(gates[x],80)



while True:
    i = board.digitalRead(21)
    while (i==1):
        i=board.digitalRead(21)
        #delay
    start = time.time()
    file.write("switch ------ gate\n")
    #ir = board.digitalRead(21)
    while(i==0):
        for x in range(10):
            f=0
            while(board.digitalRead(switch[x])==1):
                print str(x)+" "+str(gates[ar[r][x]-1])
                servoClose(gates[ar[r][x]-1])
                f=1
            if(f == 1):
                board.Servos.write(gates[ar[r][x]-1],80)
                file.write(str(x+1)+"------"+str(ar[r][x])+"\n")
        i = board.digitalRead(21)
    end = time.time()
    print end-start
    file.write("\n Time taken for phase1 : " + str(int(end - start)) + " seconds")
    score_file = open('portal/score.txt', 'w')
    score_file.write(str(int(end-start)))
    score_file.close()
    break
file.close()
exit()
