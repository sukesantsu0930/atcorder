#Traveling

N = int(input())

txy=[list(map(int,input().split())) for _ in range(N)]


Clear=True

a=0
b=0
k=0

for i in range(N):
    c=txy[i][1]
    d=txy[i][2]
    j=txy[i][0]
    x=(j-k)
    y=(abs(c-a)+abs(d-b))
    if x<y or (x-y)%2!=0:
        print("No")
        Clear=False
        break
    a=c
    b=d
    k=j

if Clear:
    print("Yes")