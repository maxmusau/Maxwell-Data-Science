import pandas as pd
# dataset
data =[['Max','Software Developer'],['Sam','Data Scientist'],['Jacob','Teacher']]
DF=pd.DataFrame(data,columns=("Name","Profession"),index=('num1','num2','num3'))
print(DF)
print(data)


# using a dictionary
users={
    "Name":['Kelvin','Mike','Steve','Paul','Kelvin','Mike','Steve','Paul','Kelvin','Mike','Steve','Paul'],
    "Age":[60,30,40,32,60,30,40,32,60,30,40,32]     
}

df=pd.DataFrame(users,dtype=float)
print(df)

# add  a column
school=['Modcom','JKUAT','TUM','TUK','Modcom','JKUAT','TUM','TUK','Modcom','JKUAT','TUM','TUK']
df['School']=school
print(df)

course=['Economics','Finance','Criminology','Medicine','Economics','Finance','Criminology','Medicine','Economics','Finance','Criminology','Medicine']
df['Course']=course
print(df)

# creating a subset
new_df=df[['Name','School','Course']]
print(new_df)

# describe the data
print(df.describe())

# the first five records
print(df.head(8))

# the last eight
print(df.tail(8))

# changing the order
new_format=df[['Name','Course','School','Age']]
print(new_format)
print(df)
print(new_df)