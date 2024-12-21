#CardGame

N=int(input())

a=list(map(int,input().split()))

alice=0
bob=0

for i in range(len(a)):
    alice+=max(a)
    a.remove(max(a))
    if not a:
        break
    bob+=max(a)
    a.remove(max(a))
    if not a:
        break

print(alice-bob)