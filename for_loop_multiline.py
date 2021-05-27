#Define a list
names = ['Mrudula','Satya','Vamsi']
#Print all the names in the list
for name in names:
	print(f'Shop Owner : Hi {name}! How may I help you?')
	print(f'{name} : Can you show me a nice dress?')
	print(f'Shop Owner : Sure {name}')
	print(f'{name} : Wow! I like the dress. How much is it?')
	print(f'Shop Owner : It costs Rs.{len(name)*100}/- only {name}')
	print(f'{name} : Here you go')
	print(f'Shop Owner : Anything else you need {name}')
	print(f'{name} : No, Thank you! I will make a move now\n')
print('Thank you for visiting my store')