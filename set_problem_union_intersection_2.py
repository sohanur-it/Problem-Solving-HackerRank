#!/usr/bin/python3
n=int(input())
lis1 = input().split()
newlis1=list(map(int,lis1))
newlis1=set(newlis1)
#print(newlis1)
m=int(input())
lis2 = input().split()
newlis2=list(map(int,lis2))
newlis2=set(newlis2)
#print(newlis2)
diff1 = newlis1.difference(newlis2)
diff2 = newlis2.difference(newlis1)

#print(diff1)
#print(diff2)

output = diff1.union(diff2)
output = list(output)
length=len(output)
#print(length)
output.sort()
for i in range(length):
	print(output[i])

