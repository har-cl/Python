#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
print('1. Write a Python Program to Check if a Number is Positive, Negative or Zero?')
try:
    a=float(input('Enter number : '))
    if a > 0:
        print('entered number is +ve')
    elif a < 0:
        print('entered number is -ve')
    elif a == 0:
        print('entered number is 0')
except:
    print('you have not entered number')

#2. Write a Python Program to Check if a Number is Odd or Even?
print('2. Write a Python Program to Check if a Number is Odd or Even?')
try:
    a = float(input('Enter natural number : '))
    x = float(a / 2) - int(a / 2)
    if a == 0:
        print('entered number is zero')
    elif x == 0:
        print('Entered number is even')
    else:
        print('Entered number is odd')
except:
    print('enter number')

#3. Write a Python Program to Check Leap Year?
print('3. Write a Python Program to Check Leap Year?')
try:
    a = int(input('Enter year in yyyy format : '))
    if a != 0:
       if a%4 == 0:
            print('entered year is leap year')
       else:
            print('entered year is not leap year')
except:
    print('please enter year properly')

#4. Write a Python Program to Check Prime Number?
print('4. Write a Python Program to Check Prime Number?')
try:
    a = int(input('Enter number : '))
    x = 0
    import math
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            x = x + 1
    if x > 0:
        print('entered number is not prime')
    else:
        print('entered number is prime')
except:
    print('enter number only')

#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
print('5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?')
try:
    r = int(input('Enter number : '))
    for j in range(2,r):
        x = 0
        import math
        for i in range(2, int(math.sqrt(j)) + 1):
            if j % i == 0:
                x = x + 1
                # print('a',a,'i=',i,'x=',x)
        if x > 0:
            pass
        else:
            print(j)
except:
    print('enter number only')
