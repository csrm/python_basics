numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Printing the list: ",numbers)
#Considers the elements from index 0 to 2
print(f'First 3 elements from the list: {numbers[:3]}')
#Considers the elements from index -3 to last
print(f'Last 3 elements from the list: {numbers[-3:]}')
#Considers the elements from index 3 to 6
sliced_list = numbers[3:7]
print(f'Sliced List: {sliced_list}')