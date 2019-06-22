#!/usr/bin/python3

n=int(input())

for row in range(1,n):
	for col in range(1,row+1):
		print(row,end="")
	print("")


# # # if we print(row)
# 1
# 2 2
# 3 3 3
# 4 4 4 4

### If we print(col)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
