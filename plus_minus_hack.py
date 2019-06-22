#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr,n):
    #!/usr/bin/python3
    lists = arr
    lists_pos = []
    lists_neg = []
    lists_zero = []
    for l in lists:
        if l > 0:
            lists_pos.append(l)
        if l < 0:
            lists_neg.append(l)
        if l == 0:
            lists_zero.append(l)
    print("%.6f"%(len(lists_pos)/n))
    print("%.6f"%(len(lists_neg)/n))
    print("%.6f"%(len(lists_zero)/n))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr,n)
