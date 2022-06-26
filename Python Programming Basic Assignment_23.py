print('''Question 1
Create a function that takes a number as an argument and returns True or False depending
on whether the number is symmetrical or not. A number is symmetrical when it is the same as
its reverse.''')


def is_symmetrical(n):
    flag = 1
    for i in range(0, int((len(str(n)) + 1) / 2)):
        if n[i] != n[-1 - i]:
            flag = 0
    if flag == 1:
        return 'symmatrical'
    else:
        return ' not symmatrical'


n = input('enter string : ')
print(is_symmetrical(n))



print('''\nQuestion 2
Given a string of numbers separated by a comma and space, return the product of the
numbers.''')

def multiply_nums(n):
    x, y = n.split(',')
    return int(x) * int(y)


n = input('enter numbers separated by comma : ')
print(multiply_nums(n))



print('''\nQuestion 3
Create a function that squares every digit of a number.''')

def square_digits(s):
    s1 = ''
    for i in s:
        s1 += str(int(i) * int(i))
    return int(s1)


n = input('enter number : ')
print(square_digits(n))



print('''\nQuestion 4
Create a function that sorts a list and removes all duplicate items from it.''')

def setify(l):
    return sorted(list(set(l)))

l=[1,2,6,4,7,5,5,6,3,1]
print(setify(l))



print('''\nQuestion 5
Create a function that returns the mean of all digits.''')

def mean(n):
    s=0
    c=0
    for i in n:
        s+=int(i)
        c+=1
    return int(s/c)

n = input('enter number : ')
print(mean(n))