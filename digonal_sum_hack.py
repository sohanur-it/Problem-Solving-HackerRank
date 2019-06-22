#!/usr/bin/python3

import math
import os
import random
import re
import sys



def diagonalDifference(arr,n):
    # Write your code here
    #!/usr/bin/python3

    list2 = arr

    diagonal1 = 0
    diagonal2 = 0
    for i in range(n):
        for j in range(n):
            if i == j :
                diagonal1 += list2[i][j]
            if i+j == (n-1):
                diagonal2 += list2[i][j]
    dif = abs(diagonal2 - diagonal1)
    
    return dif        
 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    #print(arr)

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
