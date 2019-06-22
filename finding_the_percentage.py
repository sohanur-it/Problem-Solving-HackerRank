#!/usr/bin/python3

# n = int(input())

# markseet = []

# for i in range(n):
# 	name = input()
# 	lis =list(map(int, input().strip().split()))[:3]
# 	avg=sum(lis)/3
# 	#print(avg)
# 	avg_2="{:.2f}".format( avg )
# 	#print(avg_2)
# 	#print(name)
# 	#print(lis)
# 	markseet.append([name,avg_2])
# #print(markseet)
# for a,b in markseet:
#  	if a == input():
#  		print(b)

marks = {}
for i in range(int(input())):
    line = input().split()
    #print(line[0])
    #print(list(map(float, line[1:]))
    marks[line[0]] = list(map(float, line[1:]))
name=input()
marks_all = marks[name]
marks_avg = sum(marks_all)/3
print('%.2f' %(marks_avg))

