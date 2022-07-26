print('1. Given a sentence as txt, return True if any two adjacent words have this property: One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).')

def vowel_links(s):
    l = s.split()
    vowels = ['a', 'e', 'i', 'o',  'u']
    for i in range(1,len(l)):
        if l[i][0] in vowels and l[i-1][-1] in vowels:
            return True
    return False

print(vowel_links("go to edabit"))



print('\n 2. You are given three inputs: a string, one letter, and a second letter. Write a function that returns True if every instance of the first letter occurs before every instance of the second letter.')

def first_before_second(s, s1, s2):
    import re
    flag = 1
    l = re.findall(f'[{s1}|{s2}]', s)
    print(l)
    r = s.count(l[0])
    for i in range(r):
        if l[i] != l[0]:
            flag = 0
    if flag == 1:
        return True
    else:
        return False

print(first_before_second("a rabbit jumps joyfully", "a", "j"))



print('\n 3. Create a function that returns the characters from a list or string r on odd or even positions, depending on the specifier s. The specifier will be "odd" for items on odd positions (1, 3, 5, ...) and "even" for items on even positions (2, 4, 6, ...).')

def char_at_pos(any, s):
    if s == 'odd':
        return any[0::2]
    if s == 'even':
        return any[1::2]

print(char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd"))



print('\n 4. Write a function that returns the greatest common divisor of all list elements. If the greatest common divisor is 1, return 1.')

def GCD(l):
    gcd = 1
    for i in range(2,min(l)+1):
        temp = True
        for j in l:
            if j%i != 0:
                temp = False
        if temp:
            gcd = i
    return gcd

print(GCD([1024, 192, 2048, 512]))



print('\n 5. A number/string is a palindrome if the digits/characters are the same when read both forward and backward. ')

def palindrome_type(n):
    n = str(n)
    flag = 1
    for i in range(0,int(len(n)/2)):
        if n[0+i] != n[-1-i]:
            flag = 0

    n = str(bin(int(n)))[2:]
    bflag = 1
    for i in range(0, int(len(n) / 2)):
        if n[0 + i] != n[-1 - i]:
            bflag = 0

    if flag == 1 and bflag == 0:
        return 'Decimal only'
    elif flag == 0 and bflag == 1:
        return 'Binary only'
    elif flag == 1 and bflag == 1:
        return 'Decimal and binary'
    elif flag == 0 and bflag == 0:
        return 'Neither!'


print(palindrome_type(313))