print('''1. Create a function to perform basic arithmetic operations that includes
addition, subtraction, multiplication and division on a string number''')

def arithmetic_operation(s):
    a = int(s[0:2])
    b = int(s[5:7])

    if s[3]=='+':
        return a+b
    if s[3]=='-':
        return a-b
    if s[3]=='*':
        return a*b
    if s[3:5]=='//':
        try:
            b = int(s[6:8])
            return a/b
        except:
            return -1

s=input('enter operation : ')
print(arithmetic_operation(s))



print('''\n2. Write a function that takes the coordinates of three points in the form of a
2d array and returns the perimeter of the triangle. The given points are the
vertices of a triangle on a two-dimensional plane.''')


def perimeter(l):
    a1 = l[0][0]
    a2 = l[0][1]
    b1 = l[1][0]
    b2 = l[1][1]
    c1 = l[2][0]
    c2 = l[2][1]

    ab = pow(pow(a1 - b1, 2) + pow(a2 - b2, 2), 0.5)
    bc = pow(pow(b1 - c1, 2) + pow(b2 - c2, 2), 0.5)
    ac = pow(pow(a1 - c1, 2) + pow(a2 - c2, 2), 0.5)

    return round(ab + bc + ac, 2)


l = [[-10, -10], [10, 10], [-10, 10]]
print(perimeter(l))



print('''\n3. A city skyline can be represented as a 2-D list with 1s representing
buildings. In the example below, the height of the tallest building is 4 (second-
most right column).''')

def tallest_skyscraper(l):
    import copy
    m = 0
    t = 0
    for i in range(0, len(l[0])):
        for j in range(0, len(l[0])):
            if l[j][i] == 1:
                t += 1
        if t > m:
            m = copy.deepcopy(t)
        t = 0
    return m


l = [[0, 0, 0, 1],
     [0, 1, 0, 1],
     [0, 1, 1, 1],
     [1, 1, 1, 1]]
print(tallest_skyscraper(l))



print('''\n4: Write a function to read the billable days of an employee and return the bonus
he/she has obtained in that quarter.''')

def bonus(d):
    b = 0
    if d > 32:
        b += (d-32)*325
    if d > 40:
        b += (d-40)*(550-325)
    if d > 48:
        b += (d-48)*(600-550)
    return b

d=int(input('Enter days : '))
print(bonus(d))



print('''\n5. A number is said to be Disarium if the sum of its digits raised to their
respective positions is the number itself.
Create a function that determines whether a number is a Disarium or not.''')

def is_disarium(n):
    s = 0
    t = 1
    for i in n:
        s += pow(int(i), t)
        t += 1
    if s == int(n):
        return True
    else:
        return False


n = input('Enter number : ')
print(is_disarium(n))