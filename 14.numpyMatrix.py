import numpy as np
matA = list(map(int,input("Enter 6 numbers for matrix A").split()[:6]))
matB = list(map(int,input("Enter 6 numbers for matrix B").split()[:6]))
matA = np.reshape(matA,(2,3))
matB = np.reshape(matB,(2,3))

print("Matrix A: \n",matA)
print("Matrix B: \n",matB)

print("Matrix Addition: \n",matA+matB)
print("Matrix Subtraction: \n",matA-matB)
print("Matrix Multiplication: \n",matA*matB)

print("Max of matA: ",np.max(matA),"Max of matB: ",np.max(matB))
print("Min of matB: ",np.min(matA),"Min of matB: ",np.min(matB))

print("Transpose of matA: ",np.transpose(matA))
print("Transpose of matB: ",np.transpose(matB))
