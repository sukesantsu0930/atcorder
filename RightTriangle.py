#RightTriangle
import numpy as np

points=np.array([list(map(int,input().split())) for _ in range(3)])


dis=np.array(abs(points[0]-points[1]))
dis=np.append(dis,abs((points[1]-points[2])))
dis=np.append(dis,abs((points[2]-points[0])))
dis=dis.reshape(3,2)
abs_dis=[]
for i in range(3):
    abs_dis.append(np.linalg.norm(dis[i],ord=2))

abs_dis.sort()
a,b,c=abs_dis
if abs(c**2-b**2-a**2)<1e-3:
    print("Yes")
else:
    print("No")