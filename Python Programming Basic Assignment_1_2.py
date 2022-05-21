"""Program for arithmatic operation"""
op=input('What operation you want to perform addition or division : ')
a=int(input('enter value of a : '))
b=int(input('enter value of b : '))
if op=='addition':
    c=a+b
    print(c)
if op=='division':
    c=a/b
    print(c)