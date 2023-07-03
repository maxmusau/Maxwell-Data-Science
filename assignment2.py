# paliandrone- 
string="maam"

# half of the string should be similar to the other half
half=int(len(string) /2)

first_str=string[:half]
second_str=string[half:]
# symetric
if first_str == second_str:
    print(f"{string} String is symetrical")
else:
    print(f"{string} String is not  symetrical")

# paliandrone
if first_str ==second_str[::-1]:
    print(f"{string} String is paliandrone")
else:
    print(f"{string} String is not paliandrone")
print(second_str[::-1])


# print the maximum number in a lidt
numbers=[7,53,6,6,7,7,5,37,53,2]
# sort the items in the list
numbers.sort()
print(numbers) 
# last item in a list
last_num=numbers[-1]
maximum=last_num
print(maximum)

max_nubmber=max(30, 37)
print(max_nubmber)

if 37 in numbers:
    print("37 is available")
else:
    print("37 not available")