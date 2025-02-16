# control flow statements :

# even or odd 

num = int(input("enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# greatest of three numbers

a=int(input("Enter first Number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))

if a>=b and b>=c:
    print("Bigger is a",a)
elif b>=a and b>=c:
    print("Bigger is b",b)
else:
    print("c",c)


# leap year 

year = int(input("enter a year: "))

if(year % 4 == 0 and year % 100 != 0) and (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")

# grade based on marks

marks = int(input("enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks>= 75:
    print("Grade B")
elif marks>=50:
    print("Grade: C")
else:
    print("Grade: Fail")

# short-hand if

num=int(input("Enter a number: "))
result="Even" if num%2==0 else "Odd"
print(result)

# Vowel or consonant

char = input("Enter a character: ").lower()

if char in "aeiou":
    print("Vowel")
else:
    print("consonant")

# positive, nagative or zero

num=int(input("enter a number: "))
if num > 0:
    print("positive")
elif num<0:
    print("nagative")
else:
    print("zero")

# wheather number is divisible by 5 and 11

num=int(input("enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("divisible by both")
else:
    print("not divisible by both")

# check if a triangle is valid 

a=int(input("enter first side"))
b=int(input("enter second side"))
c=int(input("enter third side"))

if a+b>c and a+c>b and b+c>a:
    print("valid triangle")
else:
    print("invalid triangle")

# determine character

char = input("enter a character: ")

if 'A'<=char <= 'Z':
    print("Uppercase Letter")
elif 'a'<=char<='z':
    print("LowerCase Letter")
elif '0'<=char<='9':
    print("digit")
else:
    print("special character")

# ternary operator

a=int(input("first: "))
b=int(input("second number: "))

smallest = a if a<b else b
print(smallest)

# rock,paper, scissors game

player1=input("player 1, enter rock,paper or scissors: ").lower()
player2=input("player 2, enter rock,paper, or scissors: ").lower()

if player1==player2:
    print("it's a tie")
elif (player1 == "rock" and player2=="scissors") or \
     (player1=="scissors" and player2=="paper") or \
     (player1=="paper" and player2=="rock"):
    print("player 1 wins!!")
else:
    print("Player 2 wins!")

# check if three numbers can form arithmetic sequence 

a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))

if (b-a) == (c-b):
    print("forms arithmetic sequence")
else:
    print("not forms arithmetic sequence")

# ATM withdrawal

balance = 5000
amount =int(input("enter withdrawal amount: "))

if amount <= balance:
    print("transaction successful!remaining bal: ",balance-amount)
else:
    print("insufficient bal")

# BMI Calculator

weight = float(input("enter weight (kg): "))
height = float(input("enter height (m): "))

bmi = weight/(height ** 2)

if bmi < 18.5:  
    print("Underweight")  
elif bmi < 24.9:  
    print("Normal weight")  
elif bmi < 29.9:  
    print("Overweight")  
else:  
    print("Obese")  
