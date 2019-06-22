#!/usr/bin/python3

n = int(input())

std1_mark = []

for i in range(n):
	std1_mark.append(int(input()))

final_mark = []
for mark in std1_mark:
	near_50 = ((mark//5)+1)*5
	if (near_50 -mark) > 3:
		final_mark.append(mark)
	else:
		mark = near_50
		final_mark.append(mark)
print(final_mark)

for mark in final_mark:
	print(mark)