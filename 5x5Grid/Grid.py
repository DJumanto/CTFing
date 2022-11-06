import numpy as np
from pyparsing import Char
arr = np.empty([5,5],dtype=int)
c = 65
for i in range(len(arr)):
    for j in range(len(arr)):
        arr[i][j]= c
        if(i==1 and j == 2):
            c+=2
            continue
        c+=1
print(arr)
list = "1-3,4-4,2-1,{,4-4,2-3,4-5,3-2,1-2,4-3,_,4-5,3-5,}"
print(chr(int(arr[0][2]))+chr(int(arr[3][3]))+chr(int(arr[1][0]))+"{"+chr(int(arr[3][3]))+chr(int(arr[1][2]))+chr(int(arr[3][4]))+chr(int(arr[2][1]))+chr(int(arr[0][1]))+chr(int(arr[3][2]))+"_"+chr(int(arr[3][4]))+chr(int(arr[3][4]))+chr(int(arr[2][4]))+"}")