print('\n 1. YouTube offers different playback speed options for users. This allows users to increase or decrease the speed of the video content. Given the actual duration and playback speed of the video, calculate the playback duration of the video.')

def playback_duration(s, t):
    l = s.split(':')

    time = int(l[0])*3600 + int(l[1])*60 + int(l[2])
    new_time = time / t
    #print('time : ', time, '\n new time',new_time)
    A = int(new_time / 3600)
    B = int((new_time-A*3600) / 60)
    C = int(new_time-(A*3600)-(B*60))
    if A<10:
        A = '0' + f'{A}'
    if B<10:
        B = '0' + f'{B}'
    if C <10:
        C = '0' + f'{C}'
    return f'{A}:{B}:{C}'

print(playback_duration("51:20:09", 0.5)   )



print('\n 2. Given the total volume m of the building, can you find the number of cubes n required for the building?')

def pile_of_cubes(n):
    ub = pow(n,1/3)
    sum = 0
    for j in range(1,int(ub)+1):
        sum = 0
        for i in range(1,j):
            sum += pow(i,3)
        if sum == n:
            return j-1
        #print(sum)

print(pile_of_cubes(4183059834009))



print('\n 3. A fulcrum of a list is an integer such that all elements to the left of it and all elements to the right of it sum to the same value. Write a function that finds the fulcrum of a list.')

def find_fulcrum(l):
    for i in range(0,len(l)):
        if sum(l[0:i:1]) == sum(l[i+1:len(l):1]):
            print(sum(l[0:i:1]))
            return l[i]
    flag = 1
    for i in l:
        if l[0] != i:
            flag = 0
    if flag == 1:
        return -1

print(find_fulcrum([8, 8, 8, 8]))



print('\n 4. Given a list of integers representing the color of each sock, determine how many pairs of socks with matching colors there are. For example, there are 7 socks with colors [1, 2, 1, 2, 1, 3, 2]. There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.')

def sock_merchant(l):
    l1 = []
    pair = 0
    for i in l:
        if i not in l1:
            if l.count(i) > 1:
                pair += l.count(i)//2
                l1.append(i)
    return pair

l = [50, 20, 30, 90, 30, 20, 50, 20, 90]
print(sock_merchant(l))



print('\n 5. Create a function that takes a string containing integers as well as other characters and return the sum of the negative integers only.')

def negative_sum(s):
    import re
    p = re.compile('-[0-9]*')
    l = re.findall(p, s)
    sum = 0
    for i in l:
        sum += int(i)
    return sum

s = '22 13%14&-11-22 13 12'
print(negative_sum(s))