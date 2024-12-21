#KagamiMochi

N=int(input())

d=[int(input()) for _ in range(N)]

sorted_d=sorted(d,reverse=True)

count=1

for i in range(len(sorted_d)-1):
    if sorted_d[i]!=sorted_d[i+1]:
        count+=1
    


print(count)
