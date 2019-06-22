#!/usr/bin/python3

# arr1 = list(map(int,input().split()))

# arr2 = list(map(int,input().split()))

# l = len(arr1)

# a=0
# b=0

# for i in range(l):
# 	if arr1[i]>arr2[i]:
# 		a +=1
# 	else:
#  		b+=1
# print(a,b)



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    l = len(a)
    p=0
    q=0
    for i in range(l):
        if a[i]>b[i]:
            p+=1
        elif a[i] == b[i]:
        	p = p
        	q = q

        else:
            q+=1
    return p,q
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
