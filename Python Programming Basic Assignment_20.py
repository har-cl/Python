print('Question1 : Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.')

def filter_list(s):
    l=[]
    for i in s:
        if type(i)==int:
            l.append(i)

    return l

s=[1,2,3,'a','b',4,'d']
print(filter_list(s))



print('\nQuestion2 :Given a list of numbers, create a function which returns the list but with each element index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...')

def add_indexes(l):
    index=0
    l1=[]
    for i in l:
        l1.append(i+index)
        index+=1
    return l1

s=[1,2,3,4,5]
print(add_indexes(s))



print('\nQuestion3 :Create a function that takes the height and radius of a cone as arguments and returns the volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.')

def cone_volume(r,h):
    import math
    v=math.pi*pow(r,2)*h/3
    return round(v,2)

r=int(input('enter value of r : '))
h=int(input('enter value of h : '))
print(cone_volume(r,h))



print('\nQuestion4 :Write a function that gives the number of dots with its corresponding triangle number of the sequence.')

def triangle(n):
    l=[1]
    for i in range(2,n+1):
        l.append(l[i-2]+i)
    return l[i-2]+i

n=int(input('enter vale of n : '))
print(triangle(n))



print('\nQuestion5 : Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.')

def missing_num(l):
    for i in range(1,11):
        if i not in l:
            print('missing number is : ',end='')
            return i

l=[1,2,3,4,6,7,8,9,10]
print(missing_num(l))