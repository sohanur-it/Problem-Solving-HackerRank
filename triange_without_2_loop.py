#!/usr/bin/python3
# def pypart(n): 
#     myList = [] 
#     for i in range(1,n+1): 
#         myList.append(str(i)*i) 
#     print("\n".join(myList)) 
  
# # Driver Code 
# n=int(input())
# pypart(n)


##way--2
# n=int(input())
# myList = []
# for i in range(1,n):
#     myList.append(str(i)*i)
# print("\n".join(myList)) 


##way--3

for i in range(1,int(input())):
    print((10**(i)//9)*i)

