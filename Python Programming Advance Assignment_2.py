print('''1. Write a function that takes a positive integer num and calculates how many
dots exist in a pentagonal shape around the center dot on the Nth iteration.''')


def pentagonal(n):
    sum = 1
    if n == 1:
        return 1
    elif n > 1:
        for i in range(1, n):
            sum += 5 * i
        return sum


n = int(input('Enter value of n : '))
print(pentagonal(n))

print('''\n2. Make a function that encrypts a given input with these steps: ''')


def encrypt(s):
    s = s[::-1]
    s1 = ''
    for i in s:
        if i == 'a':
            s1 += '0'
        elif i == 'e':
            s1 += '1'
        elif i == 'i':
            s1 += '2'
        elif i == 'o':
            s1 += '2'
        elif i == 'u':
            s1 += '3'
        else:
            s1 += i
    s1 += 'aca'
    return s1


n = input('Enter word : ')
print(encrypt(n))

print('''\n3. Given the month and year as numbers, return whether that month contains
a Friday 13th.(i.e You can check Python&#39;s datetime module)''')


def has_friday_13(m, y):
    import datetime
    x = datetime.date(y, m, 13)
    if x.weekday() == 4:
        return True
    else:
        return False


m = int(input('enter month in \'m\' format : '))
y = int(input('enter month in \'yyyy\' format : '))
print(has_friday_13(m, y))

print('''\n4. Write a regular expression that will help us count how many bad cookies
are produced every day. You must use RegEx negative lookbehind.''')

import re


def cal(l):
    str = ''
    for i in l:
        str += i
    return len(re.findall('bad cookie', str))


lst = ['bad cookie', 'good cookie', 'bad cookie', 'good cookie', 'good cookie', 'bad cookie']
print(cal(lst))

print('''\n5. Given a list of words in the singular form, return a set of those words in the
plural form if they appear more than once in the list.''')


def pluralize(l):
    s = ''
    l1 = []
    for i in l:
        if l.count(i) > 1 and i + 's' not in l1:
            l1.append(i + 's')
        elif i + 's' not in l1:
            l1.append(i)
    return l1


l = ['cow', 'pig', 'cow', 'cow', 'cow', 'pig']
print(pluralize(l))
