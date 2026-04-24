a=int(input("Enter number"))
sign = -1 if a<0 else 1
a=abs(a)
rev=0
while a>0:
    digit=a%10
    rev=rev*10+digit
    a=a//10
rev=rev*sign
print (rev)
