# Data types
# Modcom1986
# list
# we define a list using square brackets list=[]
# list can contain multiple items
# allows duplicate entries
# is ordered
# changeable -edit, 
# accepst items of other data types
courses=['Economics','Computer Science','Information Tech', 'Economics','Business Admin']
print(courses)
print(type(courses))
# access items in a list using index
first_item=courses[4]
# print(courses[0])
print(first_item)
# change
courses[0]='Information Science'
print(courses)
# add items to the list
courses.append('Criminology')
print(courses)
count=len(courses)
# print(count)
print(len(courses))
list_2=['First_month',76473,90.87,5654j+7,True]
print(list_2)
print(type(list_2))

# list constructor
fruits=list(('Mango','Berries','Pineapple'))
print(fruits)
print(type(fruits))

# add items to a specific index
fruits.insert(1, 'Apple')
print(fruits)

# add more than one item into a list
fruits2=['Goose berries','water Melon']
fruits.extend(fruits2)
print(fruits)

# remove 
fruits.remove('water Melon')
print(fruits)
# pop
fruits.pop()
print(fruits)

# delete
del fruits[0]
print(fruits)
# del fruits
fruits.clear()
print(fruits)