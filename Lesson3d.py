# while loop
# executes a block of code as long as the condition is true
count=0
while count<10:
    print(count, " is  less than 10")
    # increment value of count
    count=count+1
    
number=10
while number <20:
    if number ==15:
        print("Number at 15")
    print(number)
    number+=1
# break and continue
marks =-101
while marks >=0 and marks<=100: 
    if marks<40:
        print("marks = ",marks,"Failed")
        break
    elif marks>=40 and marks <50:
        print("marks = ",marks,"Grade D")
        break
    elif marks >=50 and marks <60:
        print("marks = ",marks,"Grade C")
        break
    elif marks >=60 and marks<70:
        print("marks = ",marks,"Grade B")
        break   
    elif marks >=70 and marks <=100:
        print("marks = ",marks,"GRade A")
        break
else:
    print("Invalid Input")
