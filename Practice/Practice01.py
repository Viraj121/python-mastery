# variables

print("Hello,World!")

x=10
y="alice"
pi=3.14
is_actice=True
a_1=10


# type casting 

x=int("10")
print(x)
y=str(124)
print(y)

# # dynammic typing

x=10
print(f"x is of type {type(x)}")

x="Now I am string"
print(f"x is now type {type(x)}")

# # conditionals

x=10

if x>5:
    print("x is great")
elif x==5:
    print("x is 5")
else:
    print("x is less than 5")

# # loops

for i in range(1,11):
    print(i)

fruit = ["apple","banana","cherry"]

for fru in fruit:
    print(fru)

# # even number 

for i in range(2,21,2):
    print(i)

# character

text="Python"
for char in text:
    print(char)


# numbers = [1,2,3,4,5]
# total=0
# for num in numbers:
#     total+=num
# print("Sum:",total)

# fruits = ["app","bana","dev"]

# for fru in fruit:
#     print(fru)

# factorial 

# num = 5
# factorial=1

# for i in range(1,num+1):
#     factorial*=i
# print("Factorial:",factorial)

# reverse a string

# text="Hello"
# reverse_text=""
# for char in text:
#     reverse_text=char+reverse_text
# print("Reverse String:",reverse_text)

# multiplication table

# n=5
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")

# count vowels in string

text="Python Programming"
vowels="aeiouAEIOU"
count=0
for char in vowels:
    if char in vowels:
        count+=1
print("Number of vowels: ",count)

 
# while loop

# i=1
# while i<=10:
#     print(i)
#     i+=1

# sum the numbers

# n=5
# sum=0
# i=1
# while i<= n:
#     sum+=i
#     i+=1
# print("Sum: ",sum)

# reverse a number

# num=12345
# reverse_num=0
# while num>0:
#     digit=num%10
#     reverse_num=reverse_num*10+digit
#     num//=10
# print("Reverse:", reverse_num)

# # print element of a list

# fruit=["apple","banana","cherry"]

# i=0
# while i<len(fruit):
#     print(fruit[i])
#     i+=1

# # infinite loop 

# while True:
#     print("This is a infinite loop")

# guess the number game 

# secret_number = 7

# guess = None
# while guess !=secret_number:
#     guess = int(input("Guess the number: "))

#     if guess < secret_number:
#         print("Too low!")
#     elif guess > secret_number:
#         print("Too high!")
# print("congratlation!")
    

# find the sqaure root of the number

# number=int(input("Enter number to find sqaure root: "))

# sqaure_root=number**0.5
# print("Square root of {} is {}".format(number,sqaure_root))

# swap two variables
# x=10
# y=20

# print("the value of x and y are {}, {} before swapping".format(x,y))

# temp=x
# x=y
# y=temp

# print("value of x and y {},{}".format(x,y))

# without using thrid variable

# x,y=y,x

# generate a random number

# import random 

# num=random.randint(1,10)
# print("print :{}".format(num))

# convert km to m

# km=float(input("Enter distance in kms: "))
# miles=km*0.62171
# print("distance of {} kilometer is {} miles".format(km,miles))

# convert celsius to fahrenheit 

# celsius = float(input("enter the temperature in degree celcius: "))

# fahrenheit = celsius * 1.8 +32
# print("degree celsius = {} converted to degree fahrenheit={}".format(celsius,fahrenheit))

# check if number is positive,negative or zero 

# number = int(input("enter the number: "))
# if(number>0):
#     print("positive number")
# elif(number<0):
#     print("negative number")
# else:
#     print("number is zero")


# even or odd

# num = int(input("enter the number: "))

# if(num % 2==0):
#     print("enter number {} is even".format(num))
# else:
#     print("odd")


# leap year

# year = int(input("enter the year: "))

# if(year % 100 == 0 and year % 400 == 0):
#     print("enter year {} is a leap year".format(year))
# elif(year % 4  == 0 and year % 100 !=0):
#     print("enter year is leap year")
# else:
#     print("enter year {} is not a leap year".format(year))

# largest number among three number

# num1=float(input("enter first number"))
# num2=float(input("enter 2 number"))
# num3=float(input("enter 3 number"))

# if(num1>num2 and num1>num3):
#     print("first number is largest")

# elif(num2>num1 and num2>num3):
#     print("num2 is greatest")

# else:
#     print("third is largest")


# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

# age=26
# day="wednesday"

# price=12 if age>=18 else 8

# if day=="wednesday":
#     price -=2

# print(price)

# grade calculader

# score = 185

# if score >= 101:
#     print("Please verify your grade again")
#     exit()

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print("Grade: ", grade)

# password

# password = "See3P@ss"
# password_length = len(password)

# if len(password) < 6:
#     strength = "Weak"
# elif len(password) <= 10:
#     strength = "Medium"
# else:
#     strength = "Strong"

# print("Password strength is: ", strength)


# LOOPS

# count positive number

num=[1,2,3,4,5,-10,-2]

count=0

for nums in num:
    if num > 0:
        count+=1

print(f"Number of positive numbers: {count}")

# sum of even numbers

nums = [2,3,4,5,6,6]

even_sum=0

for num in nums:
    if num%2==0:
        even_sum +=num

print(f"sum of even numbers: {even_sum}")


# multiplication table 

num=5

for i in range(1,11):
    print(f"{num} x {i} = {num * i}")


# reverse a string

string = "Python"

rev=""

for char in string:
    rev=char+rev

print({rev})


