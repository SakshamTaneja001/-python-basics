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
history=[]
        
while True:
    print("\n---calculator---")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.history")
    print("6.exit")
    choice=int(input("Enter choice:"))
    if choice==6:
        print ("EXITING")
        break
    if choice==5:
        print("history:", history)
        continue
    if choice not in [1,2,3,4,5]:
        print("INVALID CHOCIE")
        continue
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    
    if choice==1:
        result=calc.add(a,b)
        history.append(f"{a}+{b}={result}")
    elif choice==2:
        result=calc.subtract(a,b)
        history.append(f"{a}-{b}={result}")
    elif choice==3:
        result=calc.multiply(a,b)
        history.append(f"{a}*{b}={result}")
    elif choice==4:
        result=calc.divide(a,b)
        history.append(f"{a}/{b}={result}")
    print ("result:", result)
