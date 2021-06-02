def print_params(*args, **kwargs): 
	print('Length of args:', len(args))
	print("[", end = ' ')
	for arg in args:
		print(arg, end = ' ')
	print("]")
	print(f'Length of kwargs: {len(kwargs)}')
	print('{', end = '\n  ')
	for key, value in kwargs.items():
		print(f'"{key}" : "{value}"', end = '\n  ')
	print('\r}')


print_params('Apple', 'Banana', 'Orange', 'PineApple', firstName= 'Sree Mrudula', lastName = 'Chivukula', age = '25')