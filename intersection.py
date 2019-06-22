#!/usr/bin/python3
n = int(input())
inputs1 = list(map(int,input().split()))[:n]
set1 = set(inputs1)
m = int(input())
inputs2 = list(map(int,input().split()))[:m]
set2= set(inputs2)
print(len(set1.intersection(set2)))

