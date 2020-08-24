
A = [[0,1,0,1],
     [-1,0,0,2]]

B = [[1,0,0],
     [0,0,1],
     [0,-1,0],
     [1,1,1]]

def mult(X,Y):
    Z = []
    for i in range(len(X)):
        Z.insert(i,[])
        for k in range(len(Y[0])):
            Z[i].insert(k,0)
            for j in range(len(X[0])):
                Z[i][k] += X[i][j]*Y[j][k]
    return Z

for i in range(len(A)):
    print(mult(A,B)[i])