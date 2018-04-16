import math
import numpy as np
 
def create_table(cycles):
    tan = {}
    for i in range(cycles):
        ##print(2**(-i))
        tan[2**(-i)] = math.degrees(math.atan(2**(-i)))
        ##print(tan[2**(-i)])
    return tan
 
 
 
def doCordic(target_angle, steps):
    K = 0.607352
    table = create_table(steps*2)
 
    if target_angle >= 0:
        C,S = K,K
        A = 45
    else:
        C,S = K,-K
        A = -45
     
    print("--INITIAL VALUES--\n C = {} , S = {} , A = {}\n".format(C,S,A))
     
    for i in range(1, steps):
        if A < target_angle:
            newC = C - (S * 2**(-i))
            newS = S + (C * 2**(-i))
            C = newC
            S = newS
            A = A + table[2**(-i)]
            print("--IF LOOP \nIteration No. {} --\nC = {} , S = {} , A = {}\n".format(i,C,S,A))
        else:
            newC = C + (S * 2**(-i))
            newS = S - (C * 2**(-i))
            C = newC
            S = newS
            A = A - table[2**(-i)]
            print("--Iteration No. {} --\nC = {} , S = {} , A = {}\n".format(i,C,S,A))
     
    print("Cos value: " + str(C))
    print("sin value: " + str(S))
    print("A value: " + str(A))
 
 
doCordic(-60, 6)
