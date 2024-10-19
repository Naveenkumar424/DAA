#matrix multiplication
r1 = 2;c1 = 3;r2 = 3;c2 = 2

#input A
A = []
for i in range(r1):
    r = []
    for j in range(c1):
        print(f"Enter element {i}{j}:")
        r.append(int(input()))
    A.append(r)

#input B
B = []
for i in range(r2):
    r = []
    for j in range(c2):
        print(f"Enter element {i}{j}:")
        r.append(int(input()))
    B.append(r)

#Resultant R
R = []
for i in range(r1):
    r = []
    for j in range(c2):
        r.append(0)
    R.append(r)

#calculation
for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            R[i][j] += A[i][k]*B[k][j]

#Display
print("Resultant array is:")
for i in R:
    print(i)
#end of code