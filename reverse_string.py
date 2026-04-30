def reverse_strings(s):
    arr=list(s)
    i=0
    j=len(s)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return "".join(arr)
s=input("Enter string")
a=reverse_strings(s)
print(a)
                       



    

         
     
    
    
    
