#!/usr/bin/python3

def translate(phrase):
	translation=""
	for letter in phrase:
		if letter.lower() in "aeiou":
			translation = translation + "g"
		else:
			translation = translation + letter
	return translation



name=input("enter a phrase : ")
print(translate(name))
