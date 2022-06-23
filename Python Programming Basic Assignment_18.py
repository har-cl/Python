print('Question 1 Create a function that takes a list of non-negative integers and strings and return a new list without the strings.')

def filter_list(l):
    nl=[]
    for i in l:
        if type(i)==int:
            nl.append(i)
    return nl

print(filter_list([1,2,'afsa','1','123',123]))



print('\nQuestion 2. The (Reverser) takes a string as input and returns that string in reverse order, with the opposite case.')

def reverse(s):
    ans=''
    for i in s:
        if i.isupper()==True:
            ans+=i.lower()
        if i.islower()==True:
            ans+=i.upper()
        if i==' ':
            ans+=' '

    return (ans[::-1])

s=input('enter string : ')
print(reverse(s))



print('\nQuestion 3. Create variables first, middle and last from the given list using destructuring assignment (check the Resources tab for some examples),')

def writeyourcodehere(writeyourcodehere):
    start,*middle,end=writeyourcodehere
    print('start : ',start)
    print('middle : ',middle)
    print('end : ',end)

l=[1,2,3,4,5,6,7]
x=writeyourcodehere(l)



print('\nQuestion 4 : Write a function that calculates the factorial of a number recursively.')

def fact(i):
    if i==0:
        return 1

    elif i==1:
        return 1

    else:
        ans=i*fact(i-1)

    return ans

f=int(input('Enter value of n : '))
print(fact(f))



print('Write a function that moves all elements of one type to the end of the list.')

def move_to_end(sa,a):
    sa.append(a)
    from copy import deepcopy
    sn=deepcopy(sa)
    l=[]
    l1=[]
    for i in sa:
        if sn.count(i)>1 and i not in l1:
            while sn.count(i)!=0:
                l1.append(i)
                sn.pop(sn.index(i))

        elif i not in l1:
            l.append(i)
    return l+l1

li=[7,8,9,1,2,3,4]
print(move_to_end(li,9))