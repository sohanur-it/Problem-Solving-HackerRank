#!/usr/bin/python3


# x,y,z,n = [int(input()) for i in range(4)]
# print([ [a,b] for a in range(x+1) for b in range(y+1) if a+b != n ] )


# x,y,z,n = [int(input()) for i in range(4)]
# for a in range(x+1):
# 	for b in range(y+1):
# 		for c in range(z+1):
# 			if (a+b+c != n):
# 				print([a,b,c], end=",")


# n=int(input())
# inputs = []
# for i in range(n):  # loop 3 times
# 	inputs.append(input().split())

# print(inputs)

# n=int(input())
# inputs = [int(input()) for i in range(n)]
# print(inputs)


x = list(map(int, input("Enter a multiple value: ").split())) 
print("List of students: ", x)