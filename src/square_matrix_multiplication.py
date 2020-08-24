
A = [[0,1,0],
     [-1,0,0],
     [0,0,1]]

B = [[1,0,0],
     [0,0,1],
     [0,-1,0]]

def mult(X,Y):
    Z = []
    for i in range(len(X)):
        Z.insert(i,[])
        for j in range(len(X)):
            Z[i].insert(j,0)
            for k in range(len(X)):
                Z[i][j] += X[i][k]*Y[k][j]
    return Z

for i in range(len(A)):
    print(mult(A,B)[i])