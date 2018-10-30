


def check_prime(number):

	prime = False
	dividors = 0

	for x in range(1,1000000):
		
		if number % x == 0:
			
			dividors += 1
	
	
	if dividors > 2:
		
		prime = False
	
	else:
		
		prime = True

	return prime

number = int(raw_input(' Enter your number : '))

print check_prime(number)