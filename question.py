#!/usr/bin/python3

question_promt=[
"what is color of apple?\na)red\nblue\nc)green\nAns:",
"what is color of sky?\na)red\nblue\nc)green\nAns:",
"what is color of leaves?\na)red\nblue\nc)green\nAns:",
]

class Question:
	def __init__(self, promt, answer):
		self.promt = promt
		self.answer = answer

questions= [
Question(question_promt[0],'a'),
Question(question_promt[1],'b'),
Question(question_promt[2],'c')
]

def run_test(questions):
	score = 0 
	for question in questions:
		#print(question.promt)
		answer = input(question.promt)
		if answer == question.answer:
			score += 1
	print("you got "+str(score) + " out of " + str(len(questions)) + " correct ")

run_test(questions)