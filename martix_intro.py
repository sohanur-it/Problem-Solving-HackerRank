#!/usr/bin/python3


row = int(input("Enter the row:"))

col =int(input("Enter the column :"))

matrix = []
for i in range(row):
	a=[]
	for j in range(col):
		a.append(int(input('[{0}] [{1}]:'.format(i,j))))
	matrix.append(a)
	#print(matrix)




diagonal = 0
for i in range(row):
	for j in range(col):
		print(matrix[i][j],end=" ")
		if i == j:
			diagonal = diagonal+ matrix[i][j]
	print("")

print(diagonal)