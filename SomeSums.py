#SomeSums

N,A,B=map(int,input().split())



count=0

for i in range(1,N+1):
    d=[int(i) for i in str(i)]
    if A<=sum(d)<=B:
        count+=i

print(count)