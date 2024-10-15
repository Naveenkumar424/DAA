#gcd middle school
a = 50
b = 40
ad = []
bd = []
for i in range(1,a+1):
    if(a%i == 0):
        ad.append(i)
for j in range(1,b+1):
    if(b%j == 0):
        bd.append(j)
cd = set(ad)&set(bd)
c = max(cd)
print(f"GCD({a},{b}):{c}")
#End of code