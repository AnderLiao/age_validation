country = input('Your country: ')
age = int(input('Your age: '))

if country == 'TW':
	if age >= 18:
		print('You are eligible to get a driver license')
	else:
		print('Sorry, you must be 18 and above as a minimum requirement')
elif country == 'US':
	if age >= 16:
		print('You are eligible to get a driver license')
	else:
		print('Sorry, you must be 18 and above as a minimum requirement')