# # Loops 

# # counting positive numbers

import time


count = 0

while True:
    num = int(input("enter a number: "))
    if num < 0:
        break
    count += 1

print("total positive number entered: ",count)

# # sum of even numbers

n = int(input("enter a number: "))
sum_even = 0

for i in range(1,n+1):
    if i%2 == 0:
        sum_even += i

print("sum of even numbers: ",sum_even )

# # multiplication table

num = int(input("enter a number: "))

for i in range(1,11):
    print(f"{num} x {i} = {num * i}")


# # reverse a String 

text = input("enter a string: ")
reverse_text = ""

for char in text:
    reverse_text= char+reverse_text

print("reverse string: ",reverse_text)


# # first non-repeated character

text = input("enter a string: ")
char_count={}

for char in text:
    char_count[char] = char_count.get(char,0)+1

for char in text:
    if char_count[char] == 1:
        print("First non-repeated character: ",char)
        break

# # factorial 

num = int(input("enter a number: "))
fact = 1

for i in range(1,num+1):
    fact *= i

print("Factorial: ",fact)

# validate input

while True:
    num=int(input("enter a number between 1 and 100: "))
    if 1 <= num <= 100:
        print("Valid input", num)
        break
    else:
        print("Invalid input.Try again")

# # Prime number checker 

num = int(input("enter a number: "))
is_prime=True

for i in range(2,int(num**0.5)+1):
    if num % i == 0:
        is_prime=False
        break

print("Prime number" if is_prime and num>1 else "Not prime")

# # list uniqueness checker

items = ["apple","banana","ornage","apple"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ",item)
        break
    unique_item.add(item)

# # Exponential Backoff

wait_time=1
max_retries=5
attempts =0

while attempts < max_retries:
    print("Attempt",attempts+1,"- wait time",wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1
    
# range function in loop

for i in range(1,6):
    print(i,end=" ")

# sqaure in range 

for i in range(1,6):
    print(i**2,end=" ")

# print even numbers 
for i in range(1,11):
    if i % 2 ==0:
        print(i,end=" ")

# sum of numbers

total=0
for i in range(1,11):
    total += i

print(f"sum is {total}")

# reverse a string using range function

word = "python"
for i in range(len(word)-1,-1,-1):
    print(word[i],end=" ")

# count vowels in a string 

vowels = "aeiou"
string ="python"
count=0

for char in string:
   if char in vowels:
       count+=1

print(f"total vowels {count}")

# fibonacci series 
a=0
b=1
print(a,b,end=" ")

for _ in range(8):
    next_term = a+b
    print(next_term,end=" ")
    a,b = b,next_term

