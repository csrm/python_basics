#Define 3 dictionaries for Student info, Favourite Books of Students & Book Authors
favourite_books = {
	'Mrudula':'Dollar Bahu',
	'Vamsi' : 'Alchemist',
	'Amma' : 'Panchatantra',
	'Aishwarya': 'Dollar Bahu'
}
students = {
	'Student1':'Mrudula',
	'Student2':'Amma',
	'Student3':'Vamsi',
	'Student4':'Aishwar'
}
book_author = {
	'Dollar Bahu':'Sudha Murthy',
	'Alchemist' : 'Paul O Coehlo',
	'Mahabharata':'Vyasa',
	'Ramayana':'Valmiki',
	'Panchatantra':'Vishnu Sharma'
}

#Print Student Name, Favourite Book & Book Author
print('S.No.\t\tStudent Name\tFavourite Book\tBook Author')
for key,value in students.items():
	print(f'{key}\t{value}\t\t{favourite_books.get(value)}\t{book_author.get(favourite_books.get(value))}')
print()

#Print Only the Student Names
print('Printing only student names:')
for value in students.values():
	print(value)
print()

#Print on the Book Names
print('Printing only the Book Names:')
for book in book_author.keys():                   #Or for book in book_author
    print(book)
print()

#Print only the unique Favourite Books
print('Printing on the Unique favourite books:')
for fav_book in set(favourite_books.values()):
	print(fav_book)

