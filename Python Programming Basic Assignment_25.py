print('''Question1
Create a function that takes three integer arguments (a, b, c) and returns the amount of
integers which are of equal value.''')

def equal(a, b, c):
    flag = 0
    if a == b:
        if a == c:
            flag = 3
        else:
            flag = 2
    elif a == c:
        flag = 2
    elif b == c:
        flag = 2
    return flag


a = int(input('enter value of a : '))
b = int(input('enter value of b : '))
c = int(input('enter value of c : '))
print(equal(a, b, c))



print('''\nQuestion2
Write a function that converts a dictionary into a list of keys-values tuples.''')

def dict_to_list(d):
    l=[]
    l1=[]
    for i in d:
        l1.append(i)
    l1.sort()
    for i in l1:
        temp=(i,d[i])
        l.append(temp)
    return l

d={'likes':2,
   'dislikes':3,
   'followers':10
   }
print(dict_to_list(d))



print('''\nQuestion3
Write a function that creates a dictionary with each (key, value) pair being the (lower case,
upper case) versions of a letter, respectively.''')

def mapping(l):
    d=dict()
    for i in l:
        d[i]=i.upper()
    return d

print(mapping(['a','b','c']))



print('''\nQuestion4
Write a function, that replaces all vowels in a string with a specified vowel.''')

def vow_replace(str,r):
    v='AaEeIiOoUu'
    s1=''
    for i in str:
        if i in v:
            s1+=r
        else:
            s1+=i
    return s1

print(vow_replace('i am harshil','o'))



print('''\nQuestion5
Create a function that takes a string as input and capitalizes a letter if its ASCII code is even
and returns its lower case version if its ASCII code is odd.''')

def ascii_capitalize(s):
    s1=''
    for i in s:
        if ord(i)%2==0:
            s1+=i.upper()
        else:
            s1+=i.lower()
    return s1

s=input('enter string : ')
print(ascii_capitalize(s))
