from Arduino import Arduino
import time
import random
from operator import itemgetter
board = Arduino('9600', port='/dev/ttyACM1')
file = open('portal/gate.txt', 'r')
r = int(file.read())
file.close()


file = open('portal/output2.txt', 'a')
file.write('Round 2 started.\n')
file.write('Gate set: ' + str(r) + "\n")

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

switch = [36, 52, 42, 48, 34, 46, 38, 44, 40, 50]
# gates_led=[11,12,13,14,15,16,17,18,19,20]
gates = [7, 10, 6, 5, 4, 2, 8, 3, 11, 9]
#gates_ir = [35,36,37,38,39,40,41,42,43,44]
board.pinMode(21, "INPUT")  # IR sensor pin1
# board.pinMode(32,"INPUT") # IR sensor pin2
# board.pinMode(33,"INPUT") # IR sensor pin3
board.pinMode(20, "INPUT")  # Infinity stone
board.pinMode(12, "INPUT")
penalty = 5


def servoClose(pin):

    if pin in [7, 8, 9, 10]:
        board.Servos.write(pin, 170)

    else:
        board.Servos.write(pin, 10)


tim = [[0, 1000, 0]] * 10  # ith element will store the time for which the ith gate need to be opened
for x in range(10):
    board.Servos.attach(gates[x])
    board.Servos.write(gates[x], 80)
#r = (int)(file.read())
st = 0
while True:
    q = board.digitalRead(21)
    while (q):
        q = board.digitalRead(21)
        # pass
        # delay
    main_start = time.time()
    while(board.digitalRead(20)):
        print "in"
        for x in range(10):
            i = 0
            while(board.digitalRead(switch[x]) == 1):
                print "Inn"
                if(i == 0):
                    st = time.time()
                    i = 1

                servoClose(gates[ar[r][x] - 1])
                print str(switch[x]) + " " + str(ar[r][x] - 1)
            board.Servos.write(gates[x], 80)
            # board.digitalWrite(gates_led[ar[r][x]-1],"HIGH")
            # board.digitalWrite(gates_led[ar[r][x]-1],"LOW")
            if(i == 1):
                en = time.time()
                tim[ar[r][x] - 1] = [st, en - st, ar[r][x]]  # [time,gate_number]
                file.write(str(int(ar[r][x])) + " " + str(int(en-st)) + "\n")
                break
    file.write('\nInfinty Stone lifted\n')
    print "lifted\n"
    tim = sorted(tim, key=itemgetter(0))
    print tim

    for x in range(10):

        servoClose(gates[x])

    for x in range(10):
        print "innn"
        if(tim[x][1] == 1000):
            continue
        print tim[x][2] - 1

        board.Servos.write(gates[tim[x][2] - 1], 80)

        t1 = 0
        t2 = 0
        s1 = time.time()

        while(int(time.time() - (s1 + t2 - t1)) < int(tim[x][1])):
            pass

            if(board.digitalRead(12) == 1):

                penalty = 2 * penalty
                t1 = time.time()
                while(board.digitalRead(12)):
                    for gate in gates:
                        board.Servos.write(gate, 80)
                t2 = time.time()

                for gate in gates:
                    servoClose(gate)
                board.Servos.write(gates[tim[x][2] - 1], 90)

        print "servo started"
        print tim[x][2]
        # time.sleep(tim[x][1])

        servoClose(gates[tim[x][2] - 1])  # closing of gate
        # if(flag==0):
        # 	board.Servos.write(gates[tim[x][2]-1],90)
        # 	while(board.digitalRead(12)!=1):
        # 		pass

        # 	servoClose(gates[tim[x][2]-1])
        # 	penalty = penalty * 2
    main_end = time.time()
    file.write("Penalty: " + str(int(penalty)) + "\n")
    file.write("score" + str(main_end - main_start + penalty))
    print(main_end - main_start + penalty)
    file_score = open('portal/score.txt', 'w')
    file_score.write(str(int(main_end - main_start + penalty)))
    file_score.close()
    break
file.close()
exit()
