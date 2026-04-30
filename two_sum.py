def two_sum(arr,target):
    i=0
    j=len(arr)-1
    while i<j:
        s=arr[i]+arr[j]
        if s==target:
            return True
        if s<target:
            i+=1
        if s>target:
            j-=1
    return False
arr=list(map(int,input('Enter arrays:').split()))
target=int(input("Enter target:"))
a=two_sum(arr,target)
print(a)


    

         
     
    
    
    
