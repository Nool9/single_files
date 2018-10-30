
from random import randint


#1 gen 4-diigt num
#2 ask user to guess the number
#3 compare number slots with guesses - if str[0] = correct string 
#4 print how many bulls and cows user got
#5 do inside while loop

def generate_number(numbers_to_generate):

	random_number = ''

	random_number += str(randint(1,9))

	for i in range(numbers_to_generate-1):
		
		random_number += str(randint(0,9))
	
	return random_number




def play(number):

	guess = ''

	print ' Welcome to Cows and Bulls! Game will generate a %s digit number. Your job is to guess what it is. For each guessed digit ( on right position) you will get a COW. For every wrong one you will get a BULL' %(len(number))

	turns = 0
	
	while guess != number:

		turns += 1

		bulls_and_cows = []

		guess = raw_input(' \nTake your guess by entering %s digit number' %(len(number)))

		for i in range(len(number)):

			if guess[i] == number [i]:

				bulls_and_cows.append('Cow')
			else:
				bulls_and_cows.append('Bull')

		print bulls_and_cows

	print ' You guessed the number in %s turns !' %(turns)




# Input- Let user pick difficulty by setting the number of digits

input_digit_lenght = int(raw_input('Enter how many digits game should generate: \n\n'))

# Pass number of digits to generete_number function, get lenght for the promptt

play(generate_number(input_digit_lenght))

