print('Write a Python Program to Find LCM?')
try:
    a=int(input('Enter number 1: '))
    b=int(input('Enter number 2: '))
    for i in range(max(a,b),(a*b)+1):
        if i%a==0 and i%b==0:
            print(i)
            break
except:
    print('you have not entered correct input')

print('Write a Python Program to Find HCF?')
try:
    a=int(input('Enter number 1: '))
    b=int(input('Enter number 2: '))
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            print(i)
            break
except:
    print('you have not entered correct input')

print('Write a Python Program to Find Binary, Octal, Hexadeecimal?')
try:
    a=int(input('Enter number 1: '))
    print(bin(a)," in binary")
    print(oct(a), " in octal")
    print(hex(a), " in hexadecimal")
except:
    print('you have not entered correct input')

print('Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?')
try:
    a = input('Input operation you want to perform (+,-,*,/): ')
    b = int(input('Input 1st number: '))
    c = int(input('Input 2nd number: '))
    if a=='+':
        ans=b+c
    if a=='-':
        ans=b-c
    if a=='*':
        ans=b*c
    if a=='/':
        ans=b/c
    print('Answer is : ',ans)

except:
    print('you have not entered correct input')