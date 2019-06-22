#!/usr/bin/python3

n = int(input())
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd = cmd + "("+ ",".join(args) +")" #insert(0,5) 
        eval("l."+cmd)
    else:
        print(l)