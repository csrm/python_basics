numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Print the elements in the below format
# [1 2 3]
# [2 3]
# [3]
print('Printing the elements')
for i in range(len(numbers)):
#Use end = "" to specify a delimeter for the print function
#Else, the default delimiter is \n
	print(f'[ {numbers[i]}', end = " ")
	for j in range(i+1,len(numbers)):
		print(f' {numbers[j]}', end = " ")
	print(']\n')

