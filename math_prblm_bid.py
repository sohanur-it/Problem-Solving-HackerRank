#!/usr/bin/python3

lists = list(map(int,input().split()))
range = lists[1] - lists[0]

print(lists)



if lists[1] %2 == 0 and lists[0] %2 ==0:
	even = (range//2)+1
	odd = (range//2)

	print(lists[0],lists[1])


	print("Total even nmber : ",even)
	print("Total odd nmber : ",odd)

elif (lists[1] %2 == 0 and lists[0] %2 !=0) or ((lists[1] %2 != 0 and lists[0] %2 ==0)):
	even= (range//2)+1
	odd = (range//2)+1
	print("Total even nmber : ",even)
	print("Total odd nmber : ",odd)

else:
	even= (range//2)
	odd = (range//2)+1
	print("Total even nmber : ",even)
	print("Total odd nmber : ",odd)




#print(range)


#range = lists[1] - list[0]

#print(range) 