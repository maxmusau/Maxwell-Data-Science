# conditional statements
marks=int(input("Enter Marks: "))
if marks>=0 and marks<40:
    print("marks = ",marks,"Failed")
elif marks>=40 and marks <50:
    print("marks = ",marks,"Grade D")
elif marks >=50 and marks <60:
    print("marks = ",marks,"Grade C")
elif marks >=60 and marks<70:
    print("marks = ",marks,"Grade B")
elif marks >=70 and marks <=100:
    print("marks = ",marks,"GRade A")
else:
    print("Invalid Input")   
