print('1. For this challenge, forget how to add two numbers together. The best explanation on what to do for this function is this meme:')

def meme_sum(s1, s2):
    s1 = str(s1)
    s2 = str(s2)
    sum = ''
    max_length = max(len(s1), len(s2))
    if len(s1) != max_length:
        s1 = ((max_length-len(s1)) * '0' ) + s1
    if len(s2) != max_length:
        s2 = ((max_length-len(s2)) * '0' ) + s2
    for i in range(max(len(s1), len(s2))):
        sum += str(int(s1[i]) + int(s2[i]))
    return sum

print(meme_sum(122, 81))



print('\n 2. Given an integer, create a function that returns the next prime. If the number is prime, return the number itself')

def next_prime(n):
    def is_prime(n):
        flag = True
        for i in range(2, n):
            if n % i == 0:
                flag = False
        if flag == False:
            return False
        else:
            return True

    if is_prime(n):
        print(n)
    else:
        n += 1
        next_prime(n)

print(next_prime(12))



print('\n 3. If a person traveled up a hill for 18mins at 20mph and then traveled back down the same path at 60mph then their average speed traveled was 30mph. Write a function that returns the average speed traveled given an uphill time, uphill rate and a downhill rate. Uphill time is given in minutes. Return the rate as an integer (mph). No rounding is necessary.')

def ave_spd(up_time, up_speed, down_speed):
    dist = up_speed * up_time
    down_time = dist / down_speed
    return (dist * 2) / (up_time + down_time)

print(ave_spd(30, 10, 30))



print('\n 4. The Kempner Function, applied to a composite number, permits to find the smallest integer greater than zero whose factorial is exactly divided by the number.')

def kempner(n):

    def fact(n1):
        if n1 == 0:
            return 1
        else:
            return n1 * fact(n1-1)

    for i in range(2,n):
        if fact(i)%n == 0:
            return i

print(kempner(6))



print('\n 5. You work in a factory, and your job is to take items from a conveyor belt and pack them into boxes. Each box can hold a maximum of 10 kgs. Given a list containing the weight (in kg) of each item, how many boxes would you need to pack all of the items?')

def boxes(l):

    box = 0
    temp = 0
    for i in l:
        if temp + i <= 10:
            temp += i
        else:
            box += 1
            temp = i
    if temp > 0:
        return box + 1
    else:
        return box


print(boxes([2, 1, 2, 5, 4, 3, 6, 1, 1, 9, 3, 2]))