def describe_pet(pet_name, animal_type='dog'):
	"""Display information about a pet."""
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet(animal_type = 'tiger', pet_name = 'Timoti')