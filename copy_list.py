#Define a list of food items
regular_food = ['Annam', 'Pappu', 'Kura', 'Pacchadi', 'Charu', 'Curd']
#Assign the list regular_food to my_fav_food
my_fav_food = regular_food
#Copy list regular food to mom_fav_food
mom_fav_food = regular_food[:]

print(f'Regular Food : {regular_food}\nMy Favourite Food: {my_fav_food}\nMom Favourite Food {mom_fav_food}')
print()
#Append ice-cream to mom_fav_food
mom_fav_food.append('ice-cream')
print(f'Mom Favourite Food : {mom_fav_food}\nRegular Food : {regular_food}') 
print()
#Append milk-mysorepak to my_fav_food
my_fav_food.append('Milk MysorePak')
print(f'My Favourite Food : {my_fav_food}"\nRegular Food : {regular_food}')