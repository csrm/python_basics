#Ask the user to Enter his name
name = input("Enter you name:")
print(f'Hello, {name}!')

#Ask the user for age
age = int(input("Enter your age:"))

if age >=18:
	print('You are eligible to vote')
else:
	print(f'Wait for {18-age} {"year" if 18-age == 1 else "years"} to vote')
