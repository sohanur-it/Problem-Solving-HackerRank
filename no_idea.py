#!/usr/bin/python3

n,m=map(int,input().split())
l=input().split(' ')[:n]
A=set(input().split(' ')[:m])
B=set(input().split(' ')[:m])

happiness=0

for i in l:
	if i in A:
		#print(i)
		happiness+=1
	if i in B:
		#print(i)
		happiness-=1
print(happiness)