#A08

#入力
H,W = map(int,input().split())
X=[list(map(int,input().split())) for _ in range(H)]



Q=int(input())
A=[None]*Q
B=[None]*Q
C=[None]*Q
D=[None]*Q

for i in range(Q):
    A[i],B[i],C[i],D[i]=map(int,input().split())



#Do


Sum=[[0]*(W+1) for _ in range(H+1)]


for i in range(1,W+1):
    for j in range(1,H+1):
        Sum[i][j]=Sum[i-1][j]+Sum[i][j-1]-Sum[i-1][j-1]+X[i-1][j-1]



for i in range(Q):
    S=Sum[C[i]][D[i]]+Sum[A[i]-1][B[i]-1]
    S-=Sum[C[i]][B[i]-1]+Sum[A[i]-1][D[i]]
    print(S)