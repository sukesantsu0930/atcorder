#PlacingMarbles

s=str(input())

digit=[int(d) for d in s]
count=0
for i in s:
    if int(i)==1:
        count+=1

print(count)