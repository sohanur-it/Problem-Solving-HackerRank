#!/usr/bin/python3


secret_word = "none"

guess = ""

guess_count = 0 
guess_limit = 3
out_of_guesses = False
while secret_word != guess and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("enter guess :")
		guess_count += 1
	else:
		out_of_guesses = True
if out_of_guesses:
	print('out of guesses,You lose !')
else:
	print('your guess is correct')