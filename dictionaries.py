personal_details = { 1 : {'Name':'Mrudula', 'Age': 25, 'Qualification':'B.Tech', 'Marital Status':'Married'},
                     2 : {'Name':'Satya', 'Age': 52, 'Qualification':'B.Ed', 'Marital Status':'Married'},
                     3 : {'Name':'Vamsi', 'Age': 31, 'Qualification':'B.Tech', 'Marital Status':'Married'}
                   }
for i in range(1,len(personal_details)+1):
	print(personal_details[i]['Name'])