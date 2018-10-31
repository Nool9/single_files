'''Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.'''


def reverse_string():

	user_string = raw_input(' Enter a sentence: ')
	word_list = user_string.split(' ')[::-1]

	output_string = ''

	for word in word_list:

		output_string += word +' '

	return output_string


print reverse_string()