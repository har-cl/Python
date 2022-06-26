print('''Question1
Write a function that takes a list and a number as arguments. Add the number to the end of
the list, then remove the first element of the list. The function should then return the updated
list.''')

def next_in_line(l,s):
    try:
        a=l[0]
        l.append(int(s))
        l.pop(0)
        return l
    except:
        return 'No list has been selected'

l=[1,2,3,4]
s=5

print(next_in_line(l,s))



print('''\nQuestion2
Create the function that takes a list of dictionaries and returns the sum of people budgets sum''')

def get_budgets(*d):
    s=0
    for i in d:
        s+=i['budget']
    return s

print(get_budgets(
    { 'name': 'John', 'age': 21, 'budget': 23000 },
    { 'name': 'Steve', 'age': 32, 'budget': 40000 },
    { 'name': 'Martin', 'age': 16, 'budget': 2700 }
))



print('''\nQuestion3
Create a function that takes a string and returns a string with its letters in alphabetical order.''')

def alphabet_soup(s):
    l1=sorted(s)
    s1=''
    for i in l1:
        s1+=i
    return s1

s=input('Enter string : ')
print(alphabet_soup(s))



print('''\nQuestion4
Create a function that accepts the principal p, the term in years t, the interest rate r, and the
number of compounding periods per year n. The function returns the value at the end of term
rounded to the nearest cent.''')

def compound_interest(p,t,r,n):
    ans=p*pow((1+(r/n)),t*n)
    return round(ans,2)

print(compound_interest(10000, 10, 0.06, 12))



print('''\nQuestion5
Write a function that takes a list of elements and returns only the integers.''')

def return_only_integer(l):
    l1=[]
    for i in l:
        if type(i)==int:
            l1.append(i)
    return l1

l=[1,2,3,'a','b','c',4]
print(return_only_integer(l))

