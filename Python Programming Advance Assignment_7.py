print('1. Write a function that counts how many concentric layers a rug.')


def count_layers(l):
    m = len(l) // 2
    word = l[m]
    layer = 0
    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            layer += 1
    layer = (layer // 2) + 1
    return layer


l = [
    "AAAAAAAAAAA",
    "AABBBBBBBAA",
    "AABCCCCCBAA",
    "AABCAAACBAA",
    "AABCADACBAA",
    "AABCAAACBAA",
    "AABCCCCCBAA",
    "AABBBBBBBAA",
    "AAAAAAAAAAA"
]
print(count_layers(l))

print(
    '\n 2. There are many different styles of music and many albums exhibit multiple styles. Create a function that takes a list of musical styles from albums and returns how many styles are unique.')


def unique_styles(l):
    l1 = []
    for i in l:
        l1.extend(i.split(','))
    s1 = set(l1)
    return len(s1)


l = [
    "Soul",
    "House,Folk",
    "Trance,Downtempo,Big Beat,House",
    "Deep House",
    "Soul"
]
print(unique_styles(l))

print(
    '\n 3. Create a function that finds a target number in a list of prime numbers. Implement a binary search algorithm in your function. The target number will be from 2 through 97. If the target is prime then return "yes" else return "no".')

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


# primes = [1,2,3,4,5,6,7,8,9]

def is_prime(primes, s):
    lb = 0
    ub = len(primes) - 1
    n = int(s)
    mi = (lb + ub) / 2
    while ub > lb:
        if n == primes[int(mi)]:
            return 'Yes'
        elif n > primes[int(mi)]:
            lb = mi
        elif n < primes[int(mi)]:
            ub = mi
        mi = (lb + ub) / 2
    return 'No'


print(is_prime(primes, 19))

print(
    '\n 4. Create a function that takes in n, a, b and returns the number of positive values raised to the nth power that lie in the range [a, b], inclusive.')


def power_ranger(n, a, b):
    result = 0
    for i in range(a, b + 1):
        num = pow(i, 1 / n)
        if num == int(num):
            result += 1
    return result


print(power_ranger(4, 250, 1300))

print(
    '\n 5. Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged')


def rearranged_difference(s):
    import re, copy
    s = str(s)
    l = re.findall('[0-9]', s)
    min_number = max_number = ''
    l.sort()
    for i in l:
        min_number += i
    l.reverse()
    for i in l:
        max_number += i
    return int(max_number) - int(min_number)


print(rearranged_difference(3320707))
