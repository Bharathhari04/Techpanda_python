#NUMPY:

#1.CREATE 1D ARRAY AND RESHAPE TO 4 CROSS 5 MATRIX:
import numpy as np
arr = np.arange(1, 21)
matrix=arr.reshape(4,5)
print(matrix)

#2.SUM OF EACH ROW AND COLUMN:
arr=np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
row_sum=np.sum(arr,1)
column_sum=np.sum(arr,0)
print("sum of rows:",row_sum)
print("sum of columns:",column_sum)

#3.ADD,SUB,MULTIPLY,DIVISION:
a=np.array([10,20,30])
b=np.array([2,4,5])
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)

#4.5 CROSS 5 MATRIX AND FIND MAX,MIN,MEAN AND STANDARD DEVIATION:
arr = np.random.randint(10, 101, size=(5, 5))
print("array:")
print(arr)
print("maximum:",np.max(arr))
print("minimum:",np.min(arr))
print("mean:",np.mean(arr))
print("standard deviation:",np.std(arr))

#5.BOOLEAN INDEXING:
arr=np.array([15,8,23,4,42,16])
result=arr[arr>15]
print(result)

#6.REPLACE NaN VALUES WITH MEAN:
arr=np.array([10,20,np.nan,40,50,np.nan])
print(arr)
mean=np.nanmean(arr)
arr[np.isnan(arr)]=mean
print("after replacing NaN:",arr)

#7.BROADCASTING:
arr1=np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
arr2=np.array([10,20,30])
result=arr1+arr2
print(result)

#8.USE np.where() TO LABEL HIGH/LOW:
arr=np.array([45,67,89,14])
result=np.where(arr>50,"high","low")
print(result)

#9.STACK ARRAY VERTICALLY AND HORIZONTALLY:
a=np.array([1,2,3])
b=np.array([4,5,6])
vertical=np.vstack((a,b))
horizontal=np.hstack((a,b))
print("vertical:",vertical)
print("horizontal:",horizontal)

#10.IDENTIFY MATRIX 4 CROSS 4 AND TRANSPOSE:
import numpy as np
matrix=np.eye(4)
print("Identity matrix:")
print(matrix)
transpose = matrix.T
print("Transpose:")
print(transpose)