a=int(input("Enter number"))
temp=a
rev=0
if a<0:
    print ("not palindrome")
else:
    while a>0:
        digit=a%10
        rev=rev*10+digit
        a=a//10
    if temp==rev:
        print ("palindrome")
    else:
        print ("not palindrome")