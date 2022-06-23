print('Question 1: \nPlease write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.')

def gen():
    a=int(input('enter value of n : '))
    n=0
    while n<a:
        if n%5==0 and n%7==0:
            yield n
        n+=1

x=gen()
print(next(x),end='')

for i in x:
    print(',',i,end='')



print('\n\nQuestion 2: \nPlease write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.')

def gen():
    a=int(input('enter value of n : '))
    n=0
    while n<a:
        if n%2==0:
            yield n
        n+=1

x=gen()
print(next(x),end='')

for i in x:
    print(',',i,end='')



print('\n\nQuestion 3: \nPlease write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.')

l=[0,1]
n=int(input('enter value of n : '))
[l.append(l[i-1]+l[i-2]) for i in range(2,n+1)]
for i in l:
    print(i,end=', ')



print('\n\n Question 4: \nAssuming that we have some email addresses in the &quot;username@companyname.com&quot; format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.')

s=input('enter email address : ')

for i in s:
    if i!='@':
        print(i,end='')
    else:
        break



print('\n\n Question 5: \nDefine a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape&#39;s area is 0 by default.')

class shape:

    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        area=self.l*self.b
        return area

class square(shape):

    def __init__(self,s):
        self.s=s
        self.l=self.s
        self.b=self.s

ll=int(input('enter value of length : '))
x=square(ll)
print(x.area())