print('''\n1. In mathematics, the Fibonacci numbers, commonly denoted Fn, form a
sequence, called the Fibonacci sequence, such that each number is the sum
of the two preceding ones, starting from 0 and 1:''')

def fib_fast(n1):
    n=n1-1
    def fib_fast1(n):
        if n==0 or n==1:
            return 1
        else:
            s=fib_fast1(n-1)+fib_fast1(n-2)
            return s
    return fib_fast1(n)

print(fib_fast(5))



print('''\n2. Create a function that takes a strings characters as ASCII and returns each
characters hexadecimal value as a string.''')

def convert_to_hex(s):
    for i in s:
        print(s.encode().hex(),end=' ')

print(convert_to_hex("Big Boi"))



print('''\n3. Someone has attempted to censor my strings by replacing every vowel
with a *, l*k* th*s. Luckily, I&#39;ve been able to find the vowels that were
removed.
Given a censored string and a string of the censored vowels, return the
original uncensored string.''')

def uncensor(s,r):
    s1=''
    for i in str(s):
        if i!='*':
            s1+=i
        else:
            s1+=r[0]
            if len(r)>0:
                r=r[1:]
    return s1

print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))



print('''\n5. Create a function that takes an integer n and returns the factorial of
factorials.''')

def fact_of_fact(n1):
    m = 1
    def fact(n):
        if n == 0 or n == 1:
            return 1
        else:
            s = n * fact(n - 1)
            return s

    for i in range(0,n1+1):
        m = m * fact(i)

    return m


print(fact_of_fact(5))
