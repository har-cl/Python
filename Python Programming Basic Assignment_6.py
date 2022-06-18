print('Write a Python Program to Display Fibonacci Sequence Using Recursion?')
try:
    def fibo(n):
        if n<=1:
            return n
        else:
            return fibo(n-1)+fibo(n-2)
    a=int(input('enter nth digit : '))
    print(fibo(a-1))

except:
    print('you have not entered correct input')

print('Write a Python Program to Find Factorial of Number Using Recursion?')
try:
    def fact(n):
        if n==0:
            return 1
        if n==1:
            return 1
        else:
            ans=1
            return n*fact(n-1)
    print(fact(int(input('enter number  : '))))

except:
    print('you have not entered correct input')

print('Write a Python Program to calculate your Body Mass Index?')
try:
    weight=int(input('enter mass in kgs: '))
    height=(int(input('enter height in cms: '))/100)
    bmi=round(weight/(height*height),2)
    print(bmi)

except:
    print('you have not entered correct input')

print('Write a Python Program to calculate the natural logarithm of any number?')
try:
    import math
    a=float(input('enter number: '))
    ans=math.log(a)
    print('natural log of is:',ans)

except:
    print('you have not entered correct input')

print('Write a Python Program for cube sum of first n natural numbers')
try:
    import math
    a=int(input('enter number: '))
    def cube_sum(n):
        if n==1:
            return 1
        else:
            return (n*n*n)+cube_sum(n-1)
    print('cube sum of first n natural numbers is: ',cube_sum(a))

except:
    print('you have not entered correct input')