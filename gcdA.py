#gcd euclidian
def gcd(m,n):
    if(n == 0):
        return m
    if(m<n):
        return gcd(n,m)
    return gcd(n,m%n)
#end of gcd
#main
print(f"GCD(50,40):{gcd(50,40)}")
#end of code