#!/usr/bin/python3

# n = int(input())

# for i in range(1,n+1):
# 	print(i,bin(i),oct,(i),hex(i))

n = int(input())
length = len("{0:b}".format(n))

#  for i in range(1,n+1):
#  	print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

# n = int(input())
# print("Headings: \n")
# for i in range(1,n+1):
# 	print('{0:<5} {0:>10} {0:>13}'.format(i))


for i in range(1,n+1):
	print('{0:{length}d} {0:{length}b} {0:{length}X} {0:{length}o}'.format(i,length=length))

