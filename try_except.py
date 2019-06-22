#!/usr/bin/python3
try:

	number = int(input("enter a number :"))
	number=number/0
	print(number)
except ZeroDivisionError:
	print('divided by zero ')

except ValueError:
	print('invalid value')