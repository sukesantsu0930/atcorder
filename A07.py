#A07

D=int(input())
N=int(input())
LR=[]
for i in range(N):
    LR.append(list(map(int,input().split())))


ComeDay=[0]*D
AwayDay=[0]*D
ComeDay.append(0)
AwayDay.append(0)



for i in range(N):
    ComeDay[LR[i][0]]+=1
    AwayDay[LR[i][1]]+=1

for i in range(1,D+1):
    ComeDay[i]=ComeDay[i-1]+ComeDay[i]
    AwayDay[i]=AwayDay[i-1]+AwayDay[i]
    sum=ComeDay[i]-AwayDay[i-1]
    print(sum)
