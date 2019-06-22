#!/usr/bin/python3

# array=list(map(int,input().split()))
# print(array)

mylist1=[]
n=int(input())
 
for i in range(n):
    list1=int(input())
    mylist1.append(list1)
mylist1=set(mylist1)
print(mylist1)


mylist2=[]
m=int(input())
 
for j in range(m):
    list2=int(input())
    mylist2.append(list2)
mylist2=set(mylist2) 
print(mylist2)

print(mylist1.union(mylist2))