students = {
	'name' : 'Mrudula',
	'id' : '518',
	'age' : '25',
	'location' : 'Bengaluru'
}
counter = 0
while counter < len(list(students.keys())):
	keys = list(students.keys())
	print(students[keys[counter]])
	counter +=1
