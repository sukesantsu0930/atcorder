#Otoshidama

N,Y=map(int,input().split())

Exi=False

for i in range(N+1):
    y=Y-10000*i
    for j in range(N+1-i):
        y_last=y-5000*j
        if y_last==(N-i-j)*1000:
            print(i)
            print(j)
            print(N-i-j)
            Exi=True
        if Exi:
            break
    if Exi:
        break

if not Exi:
    print(-1,-1,-1)