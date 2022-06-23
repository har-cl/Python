print('Question1 : Create a function that takes a string and returns a string in which each character is repeated once.')

def double_char(s):
    s1=''
    for i in s:
        s1=s1+(i+i)
    return s1

s=input('enter string : ')
print(double_char(s))



print('\nQuestion2 : Create a function that reverses a boolean value and returns the string (boolean expected) if another variable type is given.')

def reverse(a):
    if a==True:
        return True
    elif a==False:
        return False
    else:
        return 'boolean expected'

print(reverse('Truea'))



print('\nQuestion3 : Create a function that returns the thickness (in meters) of a piece of paper after folding it n number of times. The paper starts off with a thickness of 0.5mm.')

def num_layers(n):
    t=0.5
    for i in range(0,n):
        t=t*2
    return t/1000

print(num_layers(21),'m')



print('\nQuestion4 : Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.')

def index_of_caps(s):
    c=0
    l=[]
    for i in s:
        if i.isupper()==True:
            l.append(c)
        c+=1

    return(l)

s=input('enter string : ')
print(index_of_caps(s))



print('\n Question5 : Using list comprehensions, create a function that finds all even numbers from 1 to the given number.')

def find_even_nums(n):
    l=[x for x in range(1,n+1) if x%2==0]
    return l

n=int(input('enter value of n : '))
print(find_even_nums(n))