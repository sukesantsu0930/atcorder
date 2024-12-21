#Sum0
import numpy as np

N=int(input())

LR=[list(map(int,input().split())) for _ in range(N)]

M=0
m=0

for i in range(N):
    M+=LR[i][1]
    m+=LR[i][0]



if M*m<=0:
    print("Yes")



else:
    print("No")
