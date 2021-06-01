def pet_details(animalType, animalName):
	"""Prints the name of the animal & its type"""
	print(f"I have a {animalType}")
	print(f"My {animalType.lower()}'s name is {animalName}")

animalType = 'Dog'
animalName = 'Jimmy'
pet_details(animalType = animalType, animalName = animalName)


animalType = 'Tiger'
animalName = 'Timoti'

pet_details(animalName = animalName, animalType = animalType)