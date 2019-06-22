#!/usr/bin/python3
n = int(input())

marksheet = []

for i in range(n):
    marksheet.append([input(),float(input())])
second_highest = sorted(list(set(marks for name, marks in marksheet)))[1]

for a,b in sorted(marksheet):
    if b == second_highest:
        print(a)