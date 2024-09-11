import math
import time

A = 40
Offset = 40

for y in range(100):
    for x in range(0,359,15):
        radians = 2*math.pi*x/360
        index1 = int(A*math.sin(radians) + Offset)
        index2 = int(A*math.sin(radians + math.pi) + Offset)
        line = ""
        for j in range(A*2+1):
            if j == index1 or j == index2:
                line += "*"
            else:
                line += " "
        print(line)
        time.sleep(0.1)