# python functions
# a function is a collection/block of related code/asserrtions that performs a specific task
# e.g mathematical , analytical evaluative operation
# two categories namely Built in and User defined functions
# why pytho functions
# 1. prevent repeating code DRY(Don't repeat yourself)
# 2. functions help divide large programs into smaller, unique,and managemable divisions
# syntax def name():
def name():
    """this function prints the name of a person"""
    print("Maxwell")
# call the function to display the output
name()
# greet
def greet():
    '''function to print greetings'''
    print("Hello World")
greet()

# built-in functions
# sqrt
num=64
from math import sqrt
square_root=sqrt(num)
print(square_root)

# sum
numbers=[20,50,50]
addition=sum(numbers)
print(addition)

def String():
    string='My favourite programming language'
    
    print(len(string))
String()