#!/usr/bin/python3

string = input()

lists = list(string)

pos,let = input().split()

#print(m)

lists[int(pos)] = let

print("".join(lists))