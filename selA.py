#selection sort movie theatre
a = [100,400,200,420,180]
for turn in range(len(a)-1):
    minPos = turn
    for inner in range(turn,len(a)):
        if(a[minPos]>a[inner]):
            minPos = inner
    a[turn],a[minPos] = a[minPos],a[turn]
print(a)
#end of code