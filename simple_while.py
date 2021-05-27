choice = True
while choice:
	print('Enter your age:')
	age = int(input())
	if age < 18:
		print(f'Sorry, you have to wait for {18-age} {"years" if 18-age>1 else "year"}')
	else:
		print('Please cast your vote & protect democracy')
	print('Would you like to continue: Y/N')
	user_choice = input()
	if user_choice.upper() == 'Y' or user_choice.upper() == 'YES':
		choice = True
	else:
		choice = False
		print('Exiting the program as per your choice!!')