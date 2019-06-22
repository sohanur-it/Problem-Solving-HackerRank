#!/usr/bin/python3

n =int(input())

list2=[]
for i in range(n):
	list1 = list(map(int,input().split()))[:n]
	list2.append(list1)

print(list2)
diagonal1 = 0
for i in range(n):
	for j in range(n):
		print(list2[i][j],end=" ")
		if i == j :
			diagonal1 += list2[i][j]
	print("")

print(diagonal1)

diagonal2 =0 
for i in range(n):
	for j in range(n):
		if i+j == (n-1):
			#print(list2[i][j],end=" ")
			diagonal2 += list2[i][j]

print(diagonal2)
diff = abs(diagonal2- diagonal1)
print(diff)