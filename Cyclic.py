#Cyclic

N=int(input())
number=[]

for i in range(3):
    number.append(N%10)
    N=N//10

A=number[::-1]
B=number[::-1]

A.append(A[0])
del A[0]

B.insert(0,B[-1])
del B[-1]

print("".join(map(str,A)),"".join(map(str,B)))