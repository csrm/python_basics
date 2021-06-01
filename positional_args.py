def pet_details(animalType, animalName):
	"""Prints the name of the animal & its type"""
	print(f"I have a {animalType}")
	print(f"My {animalType.lower()}'s name is {animalName}")

pet_details('Dog', 'Jimmy')