a=[]
b=[]
n = int(input("enter number of rows= "))
m = int(input("enter number of columns= "))
for i in range(n):
    c = []
    for j in range(m):
        c.append(int(input("\nenter the number= ")))
    a.append(c)
print("matrix a= ")
for i in range(n):
    print("\n")
    for j in range(m):
        print(a[i][j],end=" ")

for i in range(n):
    d = []
    for j in range(m):
        d.append(int(input("\nenter the number= ")))
    b.append(d)
print("matrix b= ")
for i in range(n):
    print("\n")
    for j in range(m):
        print(b[i][j], end=" ")
print("\n")


def add(a,b):
    sum = [], []
    addition = 0
    print("addition of given matrix is= ")
    for i in range(n):
        for j in range(m):
            addition = a[i][j] + b[i][j]
            sum[i].append(addition)
    print("\n",sum[0][0],sum[0][1],"\n",sum[1][0],sum[1][1])
add(a, b)

def sub(a,b):
    diff= [], []
    subtraction= 0
    print("subtration of given matrix is= ")
    for i in range(n):
        for j in range(m):
            subtraction= a[i][j]-b[i][j]
            diff[i].append(subtraction)
    print("\n",diff[0][0],diff[0][1],"\n",diff[1][0],diff[1][1])
sub(a, b)

def multi(a,b):
    mult= [0,0], [0,0]
    multiplication= 0
    print("multiplication of given matrix is= ")
    for i in range(n):
        for j in range(m):
            for k in range(n):
                mult[i][j]+= a[i][k]*b[k][j]
    print("\n",mult[0][0],mult[0][1],"\n",mult[1][0],mult[1][1])
multi(a, b)

def trans(a,b):
    trans_a= [0,0],[0,0]
    trans_b=[0,0],[0,0]
    print("\nTranspose of given matrix a is= ")
    for i in range(n):
        for j in range(m):
            trans_a[i][j]=a[j][i]
    print("\n",trans_a[0][0],trans_a[0][1],"\n",trans_a[1][0],trans_a[1][1])
    print("\nTranspose of given matrix b is= ")
    for k in range(n):
        for l in range(m):
            trans_b[l][k]=b[k][l]
    print("\n", trans_b[0][0], trans_b[0][1], "\n", trans_b[1][0], trans_b[1][1])

trans(a, b)