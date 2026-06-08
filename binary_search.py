arr=[10,20,30,40,50,60,70,80,90,100]
val=50
def check(arr,val):
    l=0
    r= len(arr)-1
    while l<=r:
        
          m=(l+r)//2
          if arr[m]==val:
              return m
          elif arr[m] < val:
              l = m+1
          else:
              r=m-1
    return "Value not found"
        
print(check(arr,val))