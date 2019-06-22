#!/usr/bin/python3

# string1 = input()
# string2 = input()

# count = 0

# if string2 in string1:
# 	count +=1

# print(count)

def count_substring(string, sub_string):
	return sum(1 for i in range(len(string)) if sub_string in string[i:i+len(sub_string)])



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
