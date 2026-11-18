import numpy as np
cuty=np.array([[1,2,3],[4,6,5],[9,8,7]])
print(cuty[0][0])#chained indexing
print(cuty[0,0])# tuple indexing both are same but this is better
print(cuty[:,2])
print(cuty[1:3,1:3])
print(cuty[2,:])