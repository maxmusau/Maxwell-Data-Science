# dictionary
# use curly brackets
# has keys and values
# changeable
# does not allow duplicate entries
# takes values of any data type


car={
    'brand':'Ford',
    'model':'Mustang',
    'year':1989,
    'year':1967,
    'colors':['Red','Blue','Green'],
    
    'Manual':True
    
}
print(car)
print(type(car))
print(len(car))
# access the different values
print(car['brand'])
print(car.values())
# access the keys
print(car.keys())
# use constructor to create a dictionary
personX=dict(name='Mike',DOB='12/6/2000',Nationality='Kenyan')
print(personX)
print(type(personX))

# change
personX['name']='Maurine'
personX.update({'Nationality':'American'})
print(personX)
print(personX.items())
# add item
personX['Profession']='Footballer'
print(personX)

# create an item in PersonX dict whose is a list of different data types
personX.update({'Hobbies':"['reading','travelling','hiking'],('eating','sleeping','football'),'Dancing',897"})
print(personX)

# countries
country={
    'Kenya':[['Nairobi','Makueni','Kajiado'],['Maasai mara','Lake Naivasha','Nairobi national park']],
    'Uganda':'Kasese',
    'Tanzania':'Katanga'
}
print(country['Kenya'])
# print first item in the key
print(country['Kenya'][0])
# access items in the first value
print(country['Kenya'][0][0])
country['Kenya'][0][0]='Kericho'
print(country['Kenya'][0][0])
