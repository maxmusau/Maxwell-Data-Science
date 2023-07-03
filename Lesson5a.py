# Functions
# modules
from math import sqrt
from Lesson4c import *
from Lesson4b import *


# calculate the simple interest
SI=Simple_Interest(70000, 6, 2)
print("The Simple interest value is",SI)


print(BMI)

#program to check if someone qualifies for blood donation
def Verify_Donation():
    age=int(input("Enter Age in years: "))
    weight=int(input("Enter your Weight in Kgs: "))
    if age >=18:
        if weight >=50:
            response="Qualifies to donate blood"
            return response
        else:
            response="Underweight:  Does not qualify to donate blood"
            return response
    else:
        response="Underage: You do not Qualify"
        return response
# Verify_Donation()
        