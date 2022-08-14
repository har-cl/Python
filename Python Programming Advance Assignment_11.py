print('1. Create a function that takes a list and returns a new list containing only prime numbers.')

def filter_primes(l):
    import math
    l1 = []
    temp = 0
    for i in l:
        for j in range(2,math.ceil(math.sqrt(i)+1)):
            if i%j==0:
                temp = 1
        if temp == 0:
            l1.append(i)
        temp = 0
    return l1

print(filter_primes([7, 9, 3, 9, 10, 11, 27]))



print('\n Create a function that takes a list which takes the pre-pop state and returns the state after the balloon is popped. The pre-pop state will contain at most a single balloon, whose size is represented by the only non-zero element.')

def pop(l):
    s = 0
    l1 = []
    for i in l:
        if i>0:
            s = i
    return [i for i in range(s+1)]+[i for i in range(s-1,-1,-1)]

print(pop([0, 0, 0, 0, 4, 0, 0, 0, 0]))



print('\n 3. Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases')

def loves_me(n):
    import re
    s = ''
    s1 = 'Loves me, '
    s2 = 'Loves me not, '
    for i in range(1,n+1):
        if i==n:
            if i%2!=0:
                s += s1[:-2:].upper()
            elif i%2==0:
                s += s2[:-2].upper()
        elif i%2!=0 and i!=n:
            s += s1
        elif i%2==0 and i!=n:
            s += s2
    return s

print(loves_me(3))



print('\n 4. Write a function that sorts each string in a list by the letter in alphabetic ascending order (a-z).')

def sort_by_letter(l):
    import re
    d = {}
    for i in l:
        alpha = re.findall('[a-z]', i)[0]
        d[alpha] = i
    keys_list = list(d.keys())
    keys_list.sort()
    l1 = []
    for i in keys_list:
        l1.append(d[i])
    return l1

print(sort_by_letter((["99a", "78e", "c2345", "11d"])))



print('5. Create a function that returns the letter position that the ball is at, once I finish swapping the cups. The swaps will be given to you as a list.')

def cup_swapping(l):
    import re
    ball = 'B'
    for i in l:
        if ball in i:
            ball = re.findall(f'[^{ball}]', i)[0]
    return ball

l = ["AB", "CA", "CB", "AC", "BA"]
print(cup_swapping(l))