print('''1. Write a function that takes a list of lists and returns the value of all of the
symbols in it, where each symbol adds or takes something from the total
score. Symbol values:
# = 5
O = 3
X = 1
! = -1
!! = -3
!!! = -5
A list of lists containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.
If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and a X would be
(0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return 0.''')


def check_score(l):
    sum = 0

    def cs(i):
        # sum = globals(sum)
        sum = 0
        if i == '#':
            sum += 5
        if i == 'O':
            sum += 3
        if i == 'X':
            sum += 1
        if i == '!':
            sum += -1
        if i == '!!':
            sum += -3
        if i == '!!!':
            sum += -5
        return sum

    for i in l:
        if type(i) == str:
            sum += cs(i)
        if type(i) == list:
            for j in i:
                sum += cs(j)

    if sum < 0:
        return 0
    else:
        return sum


print(check_score([['#', '!'], ['!!', 'X']]))

print('''2. Create a function that takes a variable number of arguments, each
argument representing the number of items in a group, and returns the
number of permutations (combinations) of items that you could get by taking
one item from each group.''')


def combinations(*args):
    ans = 1
    for i in args:
        ans *= i
    return ans


print(combinations(2, 3, 4, 5))

print('''3. Create a function that takes a string as an argument and returns the Morse
code equivalent.''')


def encode_morse(s):
    s1 = ''
    char_to_dots = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '&': '.-...', '\'': '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
        ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
        '-': '-....-', '+': '.-.-.', '\'': '.-..-.', '?': '..--..', '/': '-..-.'
    }

    for i in s:
        s1 += char_to_dots[i] + ' '
        # print(s1)
    return s1


print(encode_morse('HELP ME !'))

print('''4. Write a function that takes a number and returns True if it&#39;s a prime; False
otherwise. The number can be 2^64-1 (2 to the power of 63, not XOR). With
the standard technique it would be O(2^64-1), which is much too large for the
10 second time limit.''')


def prime(n):
    import math
    n1 = math.pow(n, 0.5)
    p = 1
    for i in range(2, int(n1 + 2)):
        if n % i == 0:
            p = 0
    if p == 0:
        return False
    else:
        return True


print(prime(5151512515524))

print('''5. Create a function that converts a word to a bitstring and then to a boolean
list based on the following criteria:
1. Locate the position of the letter in the English alphabet (from 1 to 26).
2. Odd positions will be represented as 1 and 0 otherwise.
3. Convert the represented positions to boolean values, 1 for True and 0
for False.
4. Store the conversions into an array.''')


def to_boolean_list(s):
    s1 = ''
    l = []
    for i in s:
        if (ord(i) - 96) % 2 == 0:
            s1 += '0'
        else:
            s1 += '1'
    print('binary conversion is : ', s1)
    for i in s1:
        if i == '0':
            l.append(False)
        else:
            l.append(True)
    return l


print(to_boolean_list('deep'))
