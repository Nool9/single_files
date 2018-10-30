# Simple password generator.

import random



words = ['cream','water','joke','jester','coin','pope','totem','apple','tree','smoke']
numbers = ['12','51','341','25','2','90','99','121','43','13']
symbols = ['#','%','*','@']



def pick_random_item(work_list):

	picked_item = ''
	
	roll_item = random.randint(0,len(work_list)-1)
	return work_list[roll_item]
	


def generate():

	password = []
	password_string =''


	word = pick_random_item(words)

	
	word_to_list = []

	for l in word:
		word_to_list.append(l)
	
	roll_letter = random.randint(0,len(word_to_list)-1)
	word_to_list[roll_letter] = word_to_list[roll_letter].upper()
	
	word = ''
	
	for l in word_to_list:
		word += l



	number = pick_random_item(numbers)
	
	symbol= pick_random_item(symbols)

	password.append(word)
	password.append(number)
	password.append(symbol)

	
	random.shuffle(password)
	
	
	
	for l in password:

		password_string += l

	return password_string

	


print generate()