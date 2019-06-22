#!/usr/bin/python3
# def leapyear(year):
# 	if (year % 4) == 0:
# 		if (year % 100) == 0:  
# 			if (year % 400) == 0:  
# 				print( str(year)+ " is a leap year")  
# 			else:  
# 				print(str(year)+" is not a leap year")  
# 		else:
# 			print(str(year)+" is a leap year")
# 	else:  
#    		print(str(year) +" is not a leap year")  


# year = int(input("Enter a year: ")) 
# leapyear(year)

def is_leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:  
            if (year % 400) == 0:  
                return True  
            else:  
                return False 
        else:
            return True
    else:  
           return False  

year = int(input())
print(is_leap(year))