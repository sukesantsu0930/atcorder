a=[1,2,3,4,5]
b=[]
c=[]
for i in range(len(a)):
    b.append(a[i]*2)

for i in a:
    if i%2==0:
        c.append(i)

print(b,c)