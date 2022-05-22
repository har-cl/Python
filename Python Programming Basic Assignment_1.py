#1
"""This will simple print program"""
print('Hello Python')

#2
"""Program for arithmatic operation"""
op=input('What operation you want to perform addition or division : ')
a=int(input('enter value of a : '))
b=int(input('enter value of b : '))
if op=='addition':
    c=a+b
    print(c)
if op=='division':
    c=a/b
    print(c)

#3
def area():
    """to find area of triangle"""
    base=float(input('Enter value of base : '))
    height=float(input('Enter value of height : '))
    area=0.5*base*height
    print(area)
    return area

area()

#4
a=input("Enter first variable : ")
b=input('Enter second variable : ')
x=a
y=b
a=y
b=x
print('value of a is ',a)
print('value of b is ',b)

#5
import random
a=int(random.random()*100)
print('Generated random number upto 99 is ',a)
