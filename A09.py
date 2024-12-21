#A09

H,W,N=map(int,input().split())

A=[None]*N
B=[None]*N
C=[None]*N
D=[None]*N

F=[[0]*(W+1) for _ in range(H+1)]

for i in range(N):
    A[i],B[i],C[i],D[i]=map(int,input().split())
    F[A[i]-1][B[i]-1]+=1
    F[C[i]][D[i]]+=1
    F[C[i]][B[i]-1]-=1
    F[A[i]-1][D[i]]-=1

for i in range(W):
    for j in range(1,H):
        F[i][j]+=F[i-1][j]
for j in range(H):
    for i in range(1,W):
        F[i][j]+=F[i][j-1]




for i in range(H):
    for j in range(W):
        print(F[i][j],end=" " )
    print("")