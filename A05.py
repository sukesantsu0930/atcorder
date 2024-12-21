#A05

N,K=map(int,input().split())
count=0

for i in range(1,N+1):
    for k in range(i,N+1):
        j=K-i-k
        if k<=j<=N:
            if j==k and k==i:
                count+=1
            elif(j==k or k==i or i==j):
                count+=3
            else:
                count+=6

        


print(count)

