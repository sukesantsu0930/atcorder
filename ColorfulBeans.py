N=int(input())

dict={}

for i in range(N):
    a,b=map(int,input().split())
    if b in dict:
        if dict[b] > a:
            dict[b]=a
    else:
        dict[b]=a


    


print(max(dict.values()))