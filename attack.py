#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    x,y = c_q, r_q
    dl1 = abs((max((x-n+y, 1)), min((y+x-1, n)))[0] - r_q)
    dl2 = abs((max((x-y+1, 1)), max((y-x+1,1)))[0] - r_q)
    dr1 = abs((min((x+n-y, n)), min((y+n-x, n)))[0] - r_q)
    dr2 = abs((min((x+y-1, n)), max(y-n+x, 1))[0] - r_q)
    hr1 = c_q - 1
    hr2 = n - c_q
    vc1 = r_q - 1
    vc2 = n - r_q
    print (hr1,hr2,vc1,vc2,dr1,dr2,dl1,dl2)
    for o in obstacles:

        if(r_q == o[0]):
            tempHori = c_q - o[1]
            hr1 = abs(tempHori)-1 if (tempHori > 0 and abs(tempHori) < hr1) else hr1
            hr2 = abs(tempHori)-1 if (tempHori < 0 and abs(tempHori) < hr2) else hr2

        if(c_q == o[1]):
            tempVer = r_q - o[0]
            vc1 = abs(tempVer)-1 if (tempVer > 0 and abs(tempVer) < vc1) else vc1
            vc2 = abs(tempVer)-1 if (tempVer < 0 and abs(tempVer) < vc2) else vc2

        if (abs(r_q - o[0]) == abs(c_q - o[1])):
            tempDi = abs(r_q - o[0])-1
            if (r_q < o[0] and c_q < o[1]):
                dr1 = tempDi if tempDi < dr1 else dr1

            if (r_q > o[0] and c_q > o[1]):
                dr2 = tempDi if tempDi < dr2 else dr2

            if (r_q > o[0] and c_q < o[1]):
                dl1 = tempDi if tempDi < dl1 else dl1

            if (r_q < o[0] and c_q > o[1]):
                dl2 = tempDi if tempDi < dl2 else dl2
    print (hr1,hr2,vc1,vc2,dr1,dr2,dl1,dl2)
    return hr1+hr2+vc1+vc2+dr1+dr2+dl1+dl2
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
