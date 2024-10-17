#binary search
a = [8,2,4,1,5]
a.sort()
key = int(input("Enter key:"))
low = 0
high = len(a)-1
f = False
while(low <= high):
    mid = (low+high)//2
    if(a[mid] == key):
        f = True
        break
    elif(a[mid]>key):
        high = mid-1
    else:
        low = mid+1
if(f):
    print(f"{key} found in array")
else:
    print(f"{key} not found in the array")
#end of code