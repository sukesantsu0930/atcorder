#A06

#入力
N,Q=map(int,input().split())
A=list(map(int,input().split()))
LR=[]

for i in range(Q):
    LR.append(list(map(int,input().split())))


Sum=[]
Sum.append(0)
Sum.append(A[0])
for i in range(2,N+1):

    Sum.append(Sum[i-1]+A[i-1])


for i in range(Q):
    print(Sum[LR[i][1]]-Sum[LR[i][0]-1])