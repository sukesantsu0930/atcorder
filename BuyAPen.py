#BuyAPen
import numpy as np
color=list(map(int,input().split()))
C=input()

if C=="Blue":
    color[2]=float(np.inf)
elif C=="Green":
    color[1]=float(np.inf)
else:
    color[0]=float(np.inf)


print(min(color))