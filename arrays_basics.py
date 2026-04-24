arr=[1,22,55,44,77,88,99,101,3,6,5,4]
largest=arr[0]
smallest=arr[0]
total=0
for i in arr:
    total+=i
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print(f"Sum = {total}")
print(f"Max = {largest}")
print(f"Min = {smallest}")
        
