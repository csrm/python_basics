#Define an empty dictionary
favourite_book = {}

#Add a few key-value pairs to dictionary
favourite_book['Mrudula'] = 'Dollar Bahu'
favourite_book['Vamsi'] = 'Alchemist'
favourite_book['Amma'] = 'Panchatantra'
favourite_book['xyz'] = 'Maha Shwetha'

#Print the dictionary
print(favourite_book)

#Modify a key value
favourite_book['xyz'] = 'Rich dad-Poor dad'

#Print the dictionary
print(favourite_book)

#Delete a key from the favourite_book dictionary
del favourite_book['xyz']

#Print the dictionary
print(favourite_book)
#Use a get function to read a key-value
print(f'Favourite Book of Mrudula : {favourite_book.get("Mrudula","Key not found")}')
print('Favourite Book of XYZ :',favourite_book.get('xyz','Key "XYZ" not found'))
