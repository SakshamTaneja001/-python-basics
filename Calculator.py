class calculator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b==0:
            print ("cannot divide by zero")
        else:
            return a/b
calc=calculator()
while True:
    print("\n--- Calculator ---")
    print("1. Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.exit")
    choice=int(input('Enter Choice:'))
    if choice==5:
        print ("Exiting")
        break
    if choice not in [1,2,3,4]:
        print ("Invalid Choice")
        continue
    a=int(input("Enter first number:"))
    b=int(input("Enter second number"))
    if choice==1:
        print ("Result:", calc.add(a,b))
    elif choice==2:
        print ("Result:",calc.subtract(a,b))
    elif choice==3:
        print ("Result:",calc.multiply(a,b))
    elif choice==4:
        print ("Result:",calc.divide(a,b))


