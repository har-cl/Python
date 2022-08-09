print('1. Create a function that takes the width, height and character and returns a picture frame as a 2D list.')

def get_frame(n2, n1, s):
    if n1>2:
        for i in range(n1):
            for j in range(n2):
                if i==0 or i==n1-1:
                    print(s, end='')
                else:
                    if j==0 or j==n2-1:
                        print(s, end='')
                    else:
                        print(' ', end='')
            print('')
    else:
        print('Frame\'s width is not more than 2')

print(get_frame(10, 3, "#"))



print('\n 2. These functions should evaluate a list of True and False values, starting from the leftmost element and evaluating pairwise.')

def boolean_and(l):
    import functools
    return functools.reduce(lambda a, b: bool(a & b), l)

def boolean_or(l):
    import functools
    return functools.reduce(lambda a, b: bool(a | b), l)

def boolean_xor(l):
    import functools
    return functools.reduce(lambda a, b: bool(a ^ b), l)

l = ([True, True, False, True])
print(boolean_and(l))

l = ([True, True, False, False])
print(boolean_or(l))

l = ([True, True, False, False])
print(boolean_xor(l))



print('\n 3. Create a function that creates a box based on dimension n.')

def make_box(n):
    s = '#'
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1:
                print(s, end='')
            else:
                if j==0 or j==n-1:
                    print(s, end='')
                else:
                    print(' ', end='')
        print('')

make_box(5)



print('\n 4. Given a common phrase, return False if any individual word in the phrase contains duplicate letters. Return True otherwise')

def no_duplicate_letters(s):
    import re
    ptn = re.compile('[A-Z][a-z]*|[a-z][a-z]*')
    l = re.findall(ptn,s)
    for i in l:
        for j in i:
            if i.count(j)>1:
                return False
    return True

s = "You can lead a horse to water, but you can't make him drink."
print(no_duplicate_letters(s))



print('\n 5. Write a regular expression that will match the states that voted yes to President Trump\'s impeachment. You must use RegEx positive lookahead')

def voted_states(s):
    import re
    l1 = []
    l = re.findall('[A-Z][a-z]*|yes|no',s)
    for i in range(len(l)):
        if l[i]=='yes':
            l1.append(l[i-1])
    return l1

txt = "Texas = no, California = yes, Florida = yes, Michigan = no"
print(voted_states(txt))
