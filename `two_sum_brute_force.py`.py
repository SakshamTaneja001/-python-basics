arr=[10,20,30,40,50,60,70,80,90,100]
val=50
def check(arr,val):
    for i in range(len(arr)):
        for j in range(i+1, (len(arr))):
            a=arr[i]
            b=arr[j]
            if a+b==val:
                print(f"{val} found by adding index {i} and index {j}")
                return i,j
    return False
c=check(arr,val)
print(c)