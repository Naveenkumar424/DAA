#consecutive initeger counting
def gcd(m,n,t):
    if(m%t == 0):
        if(n%t == 0):
            return t
    return gcd(m,n,t-1)
#end of fun
#main section
a = 50
b = 40
print(f"GCD({a},{b}):{gcd(a,b,max(a,b))}")
#end of code