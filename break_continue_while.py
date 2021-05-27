while True:
	print('Enter a no. from 1 to 9 to get square of the no. or "-1" to Quit')
	num = int(input())
	if num < 0:
		break
	elif num < 1 or num > 9:
		print('Invalid Choice!')
		continue
	
	print(f'{num} square is : {num**2}')