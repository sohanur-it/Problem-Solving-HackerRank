#!/usr/bin/python3


#for i in range(0,int(input()),2):
#	print(i,end=" ")

lists = list(map(int,input("Enter two numbers: ").split()))

print(lists)
if lists[0] %2 ==0:
	lists_f_even = [i for i in range(lists[0],lists[1]+1,2)]
	print(lists_f_even)
	print("even:",len(lists_f_even))

	lists_f_odd = [i for i in range(lists[0]+1,lists[1]+1,2)]
	print(lists_f_odd)
	print("odd :",len(lists_f_odd))

if lists[0] %2 !=0:
	lists_f_even = [i for i in range(lists[0]+1,lists[1]+1,2)]
	print(lists_f_even)
	print("even:",len(lists_f_even))

	lists_f_odd = [i for i in range(lists[0],lists[1]+1,2)]
	print(lists_f_odd)
	print("odd :",len(lists_f_odd))
