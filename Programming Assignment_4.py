#1. Write a Python Program to Find the Factorial of a Number?
print('1. Write a Python Program to Find the Factorial of a Number?')

try:
    a=int(input('enter whole postive number : '))
    f=1
    for i in range(1,a+1):
        f=f*i
    print(f)
except:
    print('enter properly')

#2. Write a Python Program to Display the multiplication Table?
try:
    print('2. Write a Python Program to Display the multiplication Table?')

    a=int(input('enter whole postive number : '))
    for i in range(1,11):
        print(a,' x ',i,' = ',i*a)
except:
    print('enter proper input')

#3. Write a Python Program to Print the Fibonacci sequence?
print('3. Write a Python Program to Print the Fibonacci sequence?')

try:
    i=int(input('enter value upto which Fibonacci numbers are required : '))
    a=1 #1
    b=1 #2
    c=2 #3
    print(a)
    print(b)
    while c<i:
        print(c)
        c,b=b+c,c

except:
    print('enter input properly')

#4. Write a Python Program to Check Armstrong Number?
print('4. Write a Python Program to Check Armstrong Number?')
try:
    a = int(input('enter number : '))
    power = len(str(a))
    sum = 0
    b = a

    while b > 0:
        sum = sum + pow(int(b % 10), power)
        b = int(b / 10)
    if a == sum:
        print('Entered number is armstrong number')
    else:
        print('Entered number is not armstrong number')

except:
    print('enter number only')

#5. Write a Python Program to Find Armstrong Number in an Interval?
print('5. Write a Python Program to Find Armstrong Number in an Interval?')

try:
    x = int(input('Enter staring point : '))
    y = int(input('Enter end point : '))
    for a in range(x, y + 1):
        power = len(str(a))
        sum = 0
        b = a

        while b > 0:
            sum = sum + pow(int(b % 10), power)
            b = int(b / 10)
        if a == sum:
            print(a,' is armstrong number')
except:
    print('enter range properly')

#6. Write a Python Program to Find the Sum of Natural Numbers?
print('6. Write a Python Program to Find the Sum of Natural Numbers?')
try:
    a=int(input('Enter number upto which sum of natural number is required : '))
    sum=0
    for i in range(0,a+1)
        sum +=i
    print(sum)
except:
    print('Enter +ve numbers only')