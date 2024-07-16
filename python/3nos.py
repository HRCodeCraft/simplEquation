#find largest of 3 Nos.

a=int(input('enter first number: '))
b=int(input('enter second number: '))
c=int(input('enter third number: '))

largest=0

if a>b and a>c:
  largest=a

elif b>a and b>c: 
  largest=b

else :
  largest=c

print(largest , "is the largest of three numbers.")


