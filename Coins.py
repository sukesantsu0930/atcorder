#Coins

A=int(input())
B=int(input())
C=int(input())
X=int(input())

count=0

for i in range(A+1):
    for j in range(B+1):
        c=X-500*i-100*j
        if C>=c//50>=0 and c%50==0:
            count+=1


print(count)