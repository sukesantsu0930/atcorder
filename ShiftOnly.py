#ShiftOnly

N=int(input())

A=list(map(int,input().split()))

Flag=False
count=0

while True:
    for i in range(N):
        if(A[i]%2==1):
            Flag=True
        A[i]=A[i]//2
    if Flag:
        break
    count+=1

print(count)

