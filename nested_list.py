#!/usr/bin/python3

##way--1

# n = int(input())
# marksheet = [[input(), float(input())] for i in range(n)]
# print(marksheet)

##way--2

n = int(input())
marksheet = []

for i in range(n):
    marksheet.append([input(), float(input())])
print(marksheet)
#print([marks for name, marks in marksheet])
lists=([marks for name, marks in marksheet])

#print(lists)
sets=set(lists)
#print(sets)

lists=sorted(sets)

second_highest=lists[1]

#print(lists)
#print(lists[1])




#sets = set([marks for name, marks in marksheet])
#print(sets)
#second_highest = sorted(list(sets))
#print(second_highest[1])
#print(sorted(marksheet))

for a,b in sorted(marksheet):
	if b == second_highest:
		print(a)
































##way --3

# marksheet=[]
# scorelist=[]
# if __name__ == '__main__':
#         for _ in range(int(input())):
#                 name = input()
#                 score = float(input())
#                 marksheet+=[[name,score]]
#                 scorelist+=[score]
#         b=sorted(list(set(scorelist)))[1] 

#         for a,c in sorted(marksheet):
#              if c==b:
#                     print(a)