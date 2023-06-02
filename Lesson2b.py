# tuple
# dfeined using round brackets tuple=()
# can store multiple items
# ordered
# unchangeable
# accept any data type
# allows duplicate entries
languages=('Python','Kotlin','HTML',9898,89.76,'PHP','PHP','Java Script')
print(languages)
print(languages[1])
# languages[0]='HTML' #unchangeable
# print(languages)
print(len(languages))
print(type(languages))
# tuple constructor
tuple2=tuple((90,56,75,3,3.34,454))
print(tuple2)
print(type(tuple2))
# tuple with a single item
name=('Modcom',)
print(type(name))
# unpacking a tuple
tuple3=('apple','cherry','banana')
(yellow,red,blue)=tuple3
print(yellow)
# convert tuple
new_tuple=list(tuple3)
print(type(new_tuple))
new_tuple.append('Orange')
# convert back to tuple
tuple3=tuple(new_tuple)
print(tuple3)

