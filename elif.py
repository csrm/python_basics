numbers = [1, -23, 34, -3, 5, 0, 67, -2, 10, -11]
for number in numbers:
	if number > 0:
		print(f'{number} : Positive no.')
	elif number < 0:
		print(f'{number} : Negative no.')
	else:
		print(f'{number} : Neither positive nor Negative')