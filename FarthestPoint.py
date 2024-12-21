#FarthestPoint

import numpy as np

N=int(input())
XY=np.empty((0,2),int)

for i in range(N):
    x,y=map(int,input().split())
    XY=np.append(XY,[[x,y]],axis=0)




for i in range(N):
    max=0
    index1=-1
    index2=-1
    for j in range(N):
        if max < np.linalg.norm(XY[i]-XY[j]):
            #print(f"更新  (点1) {i} (点2) {j}  距離 {np.linalg.norm(XY[i]-XY[j])}")
            max=np.linalg.norm(XY[i]-XY[j])
            index1=i
            index2=j
        #print(f"max {max}  point1) {index1}  point2) {index2}")
    #print("--------------------------")
    print(index2+1)

