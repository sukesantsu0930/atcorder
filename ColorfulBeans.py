#ColorfulBeans

N=int(input())

min_taste={}

for _ in range(N):
    a,c=map(int,input().split())

    if c in min_taste:
        min_taste[c]=min(min_taste[c],a)
    else:
        min_taste[c]=a

print(max(min_taste.values()))