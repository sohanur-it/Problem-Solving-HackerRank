#!/usr/bin/python3

T = int(input("How many iteration :"))

count_postive = 0
count_negative = 0
for i in range(1,T+1):

	#print("number"+ str(i) +":")
	num=int(input())
	if num > 0:
		count_postive += 1
	if num < 0:
		count_negative += 1
print(count_postive," ",count_negative)