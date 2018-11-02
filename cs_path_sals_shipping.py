# Given the package weight, output the best type of delivery and total price.

def customer_service():
	
	price = None

	print ' Welcome to Sals Shipping!\n'

	weight = float(raw_input(' Enter weight of your package: \n\n'))


	if weight <= 3:
		print ' \nDrone delivery is your best option.'
		print ' Total cost : %s$'%(drone(weight))

		
	elif weight >= 4 and weight <= 22:
		print ' \nGround delivery is your best option.'
		print ' Total cost : %s$'%(ground(weight))
	else:
		print ' \nPremium delivery is your best option.'
		print ' Total cost : %s$'%(premium(weight))


def drone(weight):

	if weight <= 2:
		price = weight * 4.50
		return price
	elif weight > 2 and weight <= 6:
		price = weight * 9
		return price
	elif weight >6 and weight <= 10:
		price = weight * 12
		return price
	else:
		price = weight * 14.25
		return price 


def ground(weight):
	
	flat_charge = 20.0

	if weight <= 2:
		price = weight * 1.50
		return price + flat_charge
	elif weight > 2 and weight <= 6:
		price = weight * 3
		return price + flat_charge
	elif weight >6 and weight <= 10:
		price = weight * 4
		return price + flat_charge
	else:
		price = weight * 4.75 
		return price + flat_charge

def premium(weight):
	
	flat_charge = 125.0

	return flat_charge


customer_service()
