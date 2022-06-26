print('''Question1
Create a function that takes an integer and returns a list from 1 to the given number, where:
1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the
number).
2. If the number cannot be divided evenly by 4, simply return the number.''')

def amplify(n):
    return [(x*10) if x%4==0 else x for x in range(1,n+1)]

n=int(input('enter number : '))
print(amplify(n))



print('''\nQuestion2
Create a function that takes a list of numbers and return the number that is unique.''')

def unique(l):
    for i in l:
        if l.count(i)==1:
            return i

l=[3, 3, 3, 7, 3, 3]
print(unique(l))



print('''\nQuestion3
Your task is to create a Circle constructor that creates a circle with a radius provided by an
argument. The circles constructed must have two getters getArea() (PIr^2) and
getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).

For help with this class, I have provided you with a Rectangle constructor which you can use
as a base example.''')

import math

class circy:
    import math
    def __init__(self, r):
        self.r = r

    def getArea(self):
        a = (math.pi) * self.r * self.r
        return int(a)

    def getPerimeter(self):
        a = 2 * (math.pi) * self.r
        return int(a)


c = circy(11)
print(c.getArea())
print(c.getPerimeter())



print('''\nQuestion4
Create a function that takes a list of strings and return a list, sorted from shortest to longest.''')

def sort_by_length(l):
    l1 = sorted(l, key=len)
    return l1


l = ['google', 'apple', 'microsoft']
print(sort_by_length(l))



print('''\nQuestion5
Create a function that validates whether three given integers form a Pythagorean triplet. The
sum of the squares of the two smallest integers must equal the square of the largest number to
be validated.''')

import math

def is_triplet(a,b,c):
    flag=1
    if pow(max(a,b,c),2)!=(pow(a,2)+pow(b,2)+pow(c,2)-pow(max(a,b,c),2)):
        flag=0
    if flag==1:
        return True
    else:
        return False

a=int(input('enter value of a : '))
b=int(input('enter value of b : '))
c=int(input('enter value of c : '))
print(is_triplet(a,b,c))