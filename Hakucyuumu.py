#Hakucyuumu

S=str(input())

words = ["dreamer", "eraser", "dream", "erase"]


while S:
    exi=False
    for word in words:
        if S.endswith(word):
            S=S[:-len(word)]
            exi=True
            break
    if not exi:
        print("NO")
        break
    
if exi:
    print("YES")
