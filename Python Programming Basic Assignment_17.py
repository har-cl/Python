print('Question1. Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.')

def evenly_divisible(a,b,c):
    s=0
    for i in range(a,b+1):
        if i%c==0:
            s+=i
    return s

a=int(input('enter value of a : '))
b=int(input('enter value of b : '))
c=int(input('enter value of c : '))
x=evenly_divisible(a,b,c)
print(x)



print('\nQuestion2. Create a function that returns True if a given inequality expression is correct and False otherwise.')

def correct_signs(a):
    if eval(a):
        return True
    else:
        return False

a=input()
print(correct_signs(a))



print('\nQuestion3. Create a function that replaces all the vowels in a string with a specified character.')

def replace_vowels(word,symbol):
    vowels='AaEeIiOoUu'
    nw=''
    for i in word:
        if i in vowels:
            nw+=symbol
        else:
            nw+=i
    return nw

word=input('enter sentence : ')
symbol=input('enter symbol : ')
print(replace_vowels(word,symbol))



print('\nQuestion4. Write a function that calculates the factorial of a number recursively.')

def fact(i):
    if i==0:
        return 1

    elif i==1:
        return 1

    else:
        ans=i*fact(i-1)

    return ans

f=int(input('Enter value of n : '))
print(fact(f))



print('\nCreate a function that computes the hamming distance between two strings.')

x=input('Enter string 1 : ')
y=input('Enter string 2 : ')

def hamming_distance(s1,s2):
    if len(s1)==len(s2):
        pass
    else:
        print('Enter same length strings')

    hd=0
    for i in range(0,len(s1)):
        if s1[i]==s2[i]:
            pass
        else:
            hd+=1
    return hd

print('Hamming distance is : ',hamming_distance(x,y))
