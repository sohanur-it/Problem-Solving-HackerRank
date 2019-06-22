#!/usr/bin/python3

lists = list(map(int,input().split()))

x = sum(lists)

print(x-max(lists),x-min(lists))