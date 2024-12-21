N=int(input())

s=[]

for i in range(N):
    if i%3==2:
        s.append("x")
    else:
        s.append("o")


s=''.join(s)
print(s)