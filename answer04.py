N=int(input())
numbers=[]
answer=[]


while True:
    numbers.append(N%2)
    N=N//2
    if(N==0):
        break

for i in range(len(numbers)):
    answer.append(int(numbers[-i-1]))

for i in range(10-len(numbers)):
    answer.insert(0,0)


answer="".join(map(str,answer))

print(answer)

