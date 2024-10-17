#linear search 
a = [8,2,4,1,5]
key = int(input("Enter key:"))
f = False
for i in a:
    if(i == key):
        f = True
if(f):
    print(f"{key} found in array")
else:
    print(f"{key} not found in the array")
#end of code