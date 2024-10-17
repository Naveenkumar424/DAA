#Employee salary analysis by quick sort
def quickSort(a,si,ei):
    if(si < ei):
        pIdx = partition(a,si,ei)
        quickSort(a,si,pIdx-1)
        quickSort(a,pIdx+1,ei)
    return a
#end of quickSort
#Partition
def partition(a,si,ei):
    pivot = a[ei]
    i = si-1
    for j in range(si,ei):
        if(a[j]>pivot):
            i+=1
            a[i],a[j] = a[j],a[i]
    i += 1
    a[i],a[ei] = pivot,a[i]
    return i
#end of partition
#main section
a = [1000,800,1500,970,230,840]
quickSort(a,0,len(a)-1)
print(a)
#end of code