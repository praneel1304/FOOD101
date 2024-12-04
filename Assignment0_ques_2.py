import numpy as np 

def det(a):
  a = np.array(a)

  if( a.shape== (1,1)):
    return a[0][0]
  if(a.shape == (2,2)):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]
  determinant = 0 
  for i in range(a.shape[0]):
    m = np.delete(np.delete(a,0,axis = 0),i,axis =1)
    determinant += (-1**i)*det(m)
    return determinant


def matmul(a,b):
  a = np.array(a)
  b = np.array(b)
  c = np.zeros((a.shape[0], b.shape[1]))
  for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            for k in range(a.shape[1]):
                c[i, j] += a[i, k] * b[k, j]
  return c

def matrix_operation(array1,array2,operation):
 if(operation == "dot"):
  if(array1.shape[0]==array2.shape[0] and array2.shape[1]==array1.shape[1]):
   array3 =   array1*array2
   return array3
  else: return"The dot array1.array2 is not possible"
 elif(operation == "matrix"):
     if(array1.shape[1] == array2.shape[0]):
      array3 = matmul(array1,array2)
      return array3

     else:
         return "matrix multiplication array1xarray2 is not possible "
 elif(operation == "determinant"):
     if(array1.shape[0]!=array1.shape[1]):
      return "Array 1 cannot have a determinant"
     elif(array2.shape[0]!=array2.shape[1]):
      return "Array 2 cannot have a determinant"   
     else:
         ar  =(det(array1),det(array2))
         return ar

