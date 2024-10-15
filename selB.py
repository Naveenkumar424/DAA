#recursive selection sort for sorting salaries
def sel(a,i):
    if(i >= len(a)):
        return a
    s = smlIdx(a,i)
    a[s],a[i] = a[i],a[s]
    return sel(a,i+1)
#end of sel
#smlIdx
def smlIdx(a,i):
    return a.index(min(a[i:len(a)]))
#end of smlIdx
#main section
sal = [1000,2300,1800,3400]
sel(sal,0)
print(sal)
#end of code