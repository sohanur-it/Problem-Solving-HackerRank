#!/usr/bin/python3

lists = list(map(int,input().split()))

maxi = max(lists)

cand =0
for i in lists:
	if i == maxi:
		cand += 1
print(cand)