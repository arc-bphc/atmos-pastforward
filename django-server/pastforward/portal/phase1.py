from Arduino import Arduino
import time
import random
board = Arduino('9600', port="/dev/ttyACM2")
ar = [[1, 4, 3, 2, 5, 8, 7, 6, 9, 10], [2, 5, 6, 9, 1, 4, 3, 8, 10, 7], [7, 9, 2, 5, 1, 8, 6, 3, 10, 4]]
file = open('portal/output1.txt', 'a')
switch = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gates = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

end = 0
start = 0

for x in range(10):
    board.Servos.attach(gates[x])
    board.Servos.write(gates[x], 90)

r = random.choice([0, 1, 2])
while True:
    i = board.digitalRead(21)
    while (i):
        i = board.digitalRead(21)
        # delay
    start = time.time()
    file.write("switch ------ gate\n")
    while(board.digitalRead(21) == 0):
        for x in range(10):
            f = 0
            while(board.digitalRead(switch[x]) == 1):
                board.Servos.write(gates[x], 0)
                f = 1
            if(f == 1):
                board.Servos.write(gates[x], 90)
                file.write(str(x + 1) + "------" + str(ar[r][x]) + "\n")
    end = time.time()
    break
file.write("\n Time taken for phase1 : " + str(int(start - end)))
file.close()
file = open('portal/score.txt', 'w')
file.write(str(int(start - end)))
file.close()
