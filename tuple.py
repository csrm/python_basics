#Define tuple
dimensions = (200,30)
#Loop through a tuple
for dimension in dimensions:
	print(dimension)
#Writing over dimensions
dimensions = (400,)
print()
#Loop through a tuple
for dimension in dimensions:
	print(dimension)

dimensions[0] = 30
