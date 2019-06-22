#!/usr/bin/python3

# n=int(input())

# arr = list(map(int, input().split()))

# print(arr)

# i = int(input())
# lis = list(map(int,input().strip().split()))[:i]
# z = max(lis)
# while max(lis) == z:
#     lis.remove(max(lis))

# print (max(lis))


n = int(input())
lis =list(map(int, input().strip().split()))[:n]
z = max(lis)
while max(lis)== z:
    lis.remove(max(lis))
print(max(lis)) 