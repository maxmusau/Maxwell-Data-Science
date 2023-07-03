def Area_circle(pi=3.142):
    radius=21
    Area=pi*radius**2
    print("The area of the circle is ",Area)
# Area_circle()
def Division(num1,num2):
    division=num1 /num2
    print(f" The division of {num1} and {num2} is {division}")
# Division(num2=10, num1=50)
def Simple_Interest(p,r,t):
    SI=p*t*r /100
    
    # print(SI)
    return SI
# Simple_Interest(30000, 4, 2)
# create a program to grade students based on their performance, use marks,name as parameter
def performance(marks,name):
    if marks>=0 and marks<40:
        print("Student name= ",name)
        print("Student Makrs= ",marks)
        print("Performance  Failed")
    elif marks>=40 and marks <50:
        print("Student name= ",name)
        print("Student Makrs= ",marks)
        print("Performance = Grade D")
    elif marks >=50 and marks <60:
        print("Student name= ",name)
        print("Student Makrs= ",marks)
        print("Performance = Grade C")
    elif marks >=60 and marks<70:
        print("Student name= ",name)
        print("Student Makrs= ",marks)
        print("Performance = Grade B")
    elif marks >=70 and marks <=100:
        print("Student name= ",name)
        print("Student Makrs= ",marks)
        print("Performance = GRade A")
        
    else:
        print("Invalid input")
performance(80, "Kasyoki")