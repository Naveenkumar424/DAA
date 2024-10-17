#quick sort 
def quick(a,si,ei):
    if(si > ei):
        return
    pidx = partition(a,si,ei)
    quick(a,si,pidx-1)
    quick(a,pidx+1,ei)
    return a
#end of quick
#partition
def partition(a,si,ei):
    pivot = a[ei]
    i = si-1
    for j in range(si,ei):
        if(a[j]<pivot):
            i += 1
            a[i],a[j] = a[j],a[i]
    i += 1
    a[i],a[ei] = pivot,a[i]
    return i
#end of partition
#main section
a = [100,430,240,860,180]
quick(a,0,len(a)-1)
print(a)
#end of code 