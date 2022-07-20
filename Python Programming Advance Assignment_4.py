print('''1. Create a function that takes a number n (integer greater than zero) as an
argument, and returns 2 if n is odd and 8 if n is even.
You can only use the following arithmetic operators: addition of numbers +,
subtraction of numbers -, multiplication of number *, division of number /, and
exponentiation **.
You are not allowed to use any other methods in this challenge (i.e. no if
statements, comparison operators, etc).''')

def f(n):
    try:
        1 / (n % 2)
        return 2
    except:
        return 8


print(f(6))



print('''\n2. Create a function that returns the majority vote in a list. A majority vote is
an element that occurs &gt; N/2 times in a list (where N is the length of the list).''')

def majority_vote(l):
    maj = ''
    for i in l:
        v = l.count(i)
        if v > l.count(maj) and v > int(len(l) / 2):
            maj = i
    if len(maj) > 0:
        return maj
    else:
        return 'None'

l=['A','A','A','B','C','A']
print(majority_vote(l))



print('''\n3. Create a function that takes a string txt and censors any word from a given
list lst. The text removed must be replaced by the given character char.''')

def censor_string(s1, l, s2):
    s1_list=s1.split(' ')
    l_new=''
    for i in s1_list:
        if i in l:
            l_new += s2+' '
        else:
            l_new += i+' '
    return l_new

print(censor_string('The cow jumped over the moon.',['cow','over'],'*'))



print('''\nCreate a function which takes an integer n and returns True if the given
number is a Polydivisible Number and False otherwise.''')

def is_polydivisible(n):
    Flag = 1
    for i in range(1, len(str(n))):
        if int(str(n)[0:i + 1]) % (i+1) != 0:
            Flag = 0
    if Flag == 1 and int(str(n)[0]) != 0:
        return True
    else:
        return False


print(is_polydivisible(123220))



print('''\n5. Create a function that takes a list of numbers and returns the sum of all
prime numbers in the list.''')

def sum_primes(l):
    sum=0
    for i in l:
        flag=1
        for j in range(2,int(pow(i,0.5))+1):
            if i%j==0:
                flag = 0
        if flag == 1 and i!=1:
            sum+=i
            print(i)
    return sum

l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_primes(l))




