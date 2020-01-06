import sys
import random

def getNumber(start, end):
	number = int(input(f'Type a number between {start} to {end}: '))
	num = validateNumber(number, start, end)
	return num

def validateNumber(num, start, end):
	validateNumber = False
	while validateNumber == False:
		if num < start:
			print(f'Number must be greater or equal to {start}')
			num = int(input(f'Type a number between {start} to {end}: '))
		elif num > end:
			print(f'Number must be less or equal to {end}')
			num = int(input(f'Type a number between {start} to {end}: '))
		else: 
			validateNumber = True
	return num


if sys.argv[1]:
	start = int(sys.argv[1])
	end = int(sys.argv[2])
	numberList = list(range(start, end+1))
	winnerNumber = random.choice(numberList)
	guessNumber = getNumber(start, end)
	mistakes = 1
	while guessNumber != winnerNumber:
		print('Wrong!!! Try again!')
		guessNumber = getNumber(start, end)
		mistakes += 1
	print(f'Alright! It took you {mistakes} tries to get the Winner Number!')
else:
	print("Type in 2 numbers for the range.")

