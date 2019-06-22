#!/usr/bin/python3
diction ={}
for i in range(int(input("how many inputs :\n"))):
	line = input().split()[:4]
	diction[line[0]] = list(map(int, line[1:]))
print(diction[input("Enter the name :")])