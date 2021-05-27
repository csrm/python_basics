list_fizbuz = ['fiz' if number%2==0 else 'buz' for number in range(1,101)]
print(list_fizbuz)

#trying another form of list comprehension
print('printing in another format')
print([['buz','fiz'][number%2==0] for number in range(1,101)])