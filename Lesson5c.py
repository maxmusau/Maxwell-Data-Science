# Python Exceptions
# try and except
try:
    numerator=10
    denominator=0
    
    result=numerator / denominator
    print(result)
except:
    print(f"Error occured. {numerator} cannot be divided by {denominator}")
    
try:
    number1=50
    number2=60
    result=number1 * number2
    print(result)
except:
    print("An Exeption Error occured")
# type error
name="Modcom "
age="50"
result=name+age
print(result)

# example with exception
name="Modcom "
age=50
try:  
    result=name+age
    print(result)
except:
    print("Error:  you cannot Concatenate")
# syntax error
a=40
b=60
if  a >b:
    print("A is greater than B")