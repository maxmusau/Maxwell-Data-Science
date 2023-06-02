# 2. iterative statements
# for loop
# range
for number in range(5):
    print(number)
#start and end point
for num in range(2,8):
    print(num)
# range with step
for num in range(10,20,2):
    print(num)
list1=['Wesley','Mudryk','Felix','Thiago']
for name in list1:
    # if 'Wesley' in list1:
    #     print("Wesley is a  chelsea player")
    print(name)
tuple2=(654,36643,4454,6445,46546)
count=1
for number in tuple2: 
    print(number)  
    print("looping",count)
    count+=1
# string
count=1
name='Jumia'
for letter in name:
    print("letter ",count,letter)
    count+=1

