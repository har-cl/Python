print('Question1. Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.')

def stutter(s):
    print(((s[0]+s[1]+'. . . ')*2),s+'?')

s=input('enter string : ')
stutter(s)



print('\nQuestion 2.Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.')

import math
def radians_to_degrees(a):
    degree=a*180/math.pi
    return degree

r=float(input('enter string : '))
print(round(radians_to_degrees(r),1))



print('\n Question 3. In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number. Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.')

def is_curzon(a):
    if ((pow(2,a)+1)%((2*a)+1))==0:
        return True
    else:
        return False

cn=int(input('enter number : '))
print(is_curzon(cn))



print('\nQuestion 4.Given the side length x find the area of a hexagon.')

import math
def area_of_hexagon(a):
    area=((3*math.pow(3,0.5)*a*a)/2)
    return round(area,1)

sl=int(input('enter number : '))
print(area_of_hexagon(sl))



print('\nQuestion 5. Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number.')

def binary(n):
    s=''
    n1=n
    while n1>0.4:
        s+=str(n%2)
        n=int(n/2)
        n1=float(n/2)
    return str(s)[::-1]

bn=int(input('enter number : '))
print(binary(bn))