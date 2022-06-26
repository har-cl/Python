print('''Question1
Create a function that takes three parameters where:
 x is the start of the range (inclusive).
 y is the end of the range (inclusive).
 n is the divisor to be checked against.
Return an ordered list with numbers in the range that are divisible by the third parameter n.
Return an empty list if there are no numbers that are divisible by n.''')

def list_operation(x,y,n):
    l=[]
    for i in range(x,y+1,1):
        if i%n==0:
            l.append(i)
    return l

x=int(input('Enter value of x : '))
y=int(input('Enter value of y : '))
n=int(input('Enter value of n : '))
print(list_operation(x,y,n))



print('''\nQuestion2
Create a function that takes in two lists and returns True if the second list follows the first list
by one element, and False otherwise. In other words, determine if the second list is the first
list shifted to the right by 1.''')

def simon_says(l1,l2):
    s=1
    for i in range(0,len(l1)-1):
        if l1[i]!=l2[i+1]:
            s=0
    if s==1:
        return True
    else:
        return False

print(simon_says([1,2,3,4,5],[0,1,2,3,4]))



print('''\nQuestion3
A group of friends have decided to start a secret society. The name will be the first letter of
each of their names, sorted in alphabetical order.
Create a function that takes in a list of names and returns the name of the secret society.''')

def society_name(s1,s2,s3):
    sn=''
    sn+=s1[0]+s2[0]+s3[0]
    return ''.join(sorted(sn.upper()))

print(society_name('harshil','chauhan','kukma'))



print('''\nQuestion4
An isogram is a word that has no duplicate letters. Create a function that takes a string and
returns either True or False depending on whether or not it&#39;s an &quot;isogram&quot;.''')

def is_isogram(s):
    import copy
    iso = 1
    s1 = copy.deepcopy(s.lower())
    for i in s1:
        if s1.count(i) > 1:
            iso = 0
    if iso == 1:
        print("entered word is isogram : ", s)
    else:
        print("entered word is not isogram : ", s)

s=input('enter string : ')
is_isogram(s)



print('''\nQuestion5
Create a function that takes a string and returns True or False, depending on whether the
characters are in order or not.''')

def is_in_order(s):
    import copy
    l1=copy.deepcopy(sorted(s))
    for i in l1:
        s1=''.join(l1)
    if s1==s:
        return True
    else:
        return False

s=input('enter string : ')
print(is_in_order(s))
