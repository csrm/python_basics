#Program to count no. of odd no.s & even no.s in a list
numbers = [12, 45, 4, 362, 765, 98, 101, 227, 78, 2, 59, 63, 0, -23]
#Print the list
print(numbers)
#Loop through the numbers and check for odd even
odd, even = 0,0
for number in numbers:
	if number%2 == 0:
		even = even + 1
	else:
		odd = odd + 1
print(f'No. of even no.s in the list: {even}')
print(f'No. of odd no.s in the list: {odd}')

#If a no. is even & has 2 in its unit place, print the no.
print('Printing the no.s that are even & end with 2:')
for number in numbers:
	if number%2==0 and number%10==2:
		print(number)