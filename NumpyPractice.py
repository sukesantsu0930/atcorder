import numpy as np

A=np.array([[3,2],[4,1]])
b=np.array([5,6])

solution=np.linalg.solve(A,b)

print(solution)