#!/usr/bin/python3

n = int(input())
lis =list(map(int, input().strip().split()))[:n]
#print(lis)
sets = set(lis)
avg = sum(sets)/len(sets)
#avg = sum(lis)/n
print("%.3f"%(avg))
#avg = sum(sets)/n
#print("%.2f"%(avg))