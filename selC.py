#decrement score board
rank = [100,23,987,18,32]
for turn in range(len(rank)-1):
    maxPos = turn
    for inner in range(turn,len(rank)):
        if(rank[maxPos]<rank[inner]):
            maxPos = inner
    rank[turn],rank[maxPos] = rank[maxPos],rank[turn]
print(rank)
#end of code