#Strawberries

N,K=map(int,input().split())

S=str(input())

answer="o"*K
print(answer)

print(S.count(answer))
S_sprit=S.split("X")

print(S_sprit)

count=0

for i in S_sprit:
    if len(i) >= K:
        count+=1


print(S_sprit)
print(count)