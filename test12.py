##NumPy Getting Started:
#-----------------------------------------
# import numpy
# a = numpy.array([1,2,3,4,5])
# print(a)

# import numpy as np 
# a = np.array([1,2,3,4,5])
# print(a)

# import numpy as np 
# a = np.__version__
# print(a)

##Create a NumPy ndarray Object:
#----------------------------------------
# import numpy as np 
# a = np.array([1,2,3,4,5])
# print(a)
# print(type(a))

# import numpy as np 
# a = np.array([1,2,3,4,5])
# print(a)
# print(type(a))

# import numpy as np 
# b = np.array((1,2,3,4,5))
# print(b)
# print(type(b))

#>>0D Array
# import numpy as np 
# a = np.array(124)
# print(a)
# print(type(a))

#>>1D Array 
# import numpy as np 
# a = np.array([1,2,3,4,5])
# print(a)
# print(type(a))

#>>2D Array 
# import numpy as np 
# a = np.array([[1,2,3],[4,5,6]])
# print(a)
# print(type(a))

#>>3D Array 
# import numpy as np 
# a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(a)
# print(type(a))


# import numpy as np
# a = np.array(124)
# b = np.array([1,2,3,4])
# c = np.array([[1,2,3,4],[5,6,7,8]])
# d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# import numpy as np 
# arr = np.array([1,2,3,4], ndmin=5)
# print(arr)
# print('your value is:',arr.ndim)

##NumPy Array Indexing:
#-----------------------------------
#>>Get the first element from the following array:
# import numpy as np 
# a = np.array([1,2,3,4])
# print(a[0])
# print(type(a))
#>>Get the second element from the following array.
# import numpy as np 
# b = np.array([1,2,3,4,5])
# print(b[1])
# print(type(b))
#>>Get third and fourth elements from the following array and add them.
# import numpy as np 
# c = np.array([1,2,3,4])
# print(c[2]+c[3])
#>>Access 2-D Arrays
# import numpy as np 
# a = np.array([[1,2,3,4,5],[6,7,8,9,1]])
# print(a[0,1])                                                                      0 or 1
#>>Access the 5th element on 2nd dim:                                                0 or 1
# import numpy as np 
# a = np.array([[1,2,3,4,5],[5,6,7,8,9]])
# print(a[1,4])
#>>Access 3-D Arrays
# import numpy as np 
# a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(a[0,1,2])
#>>Print the last element from the 2nd dim:
# import numpy as np 
# a = np.array([[1,2,3],[4,5,6]])
# print('Enter Last value:',a[1,-1])


##NumPy Array Slicing:
#-------------------------------------
#>>Slice elements from index 1 to index 5 from the following array:
# import numpy as np 
# a = np.array([1,2,3,4,5,6,7])
# print(a[1:5])

#>>Slice elements from index 4 to the end of the array:
# import numpy as np 
# a = np.array([101,102,103,104,105,106,107])
# print(a[4:])

#>>Slice elements from the beginning to index 4 (not included):
# import numpy as np 
# a = np.array([1,2,3,4,5,6,7])
# print(a[:4])

#>>Slice from the index 3 from the end to index 1 from the end:
# import numpy as np 
# a = np.array([1,2,3,4,5,6,4,5,6,4,5,87,14])
# print(a[-3:-1])

#>>Return every other element from index 1 to index 5:
# import numpy as np 
# a = np.array([1,2,3,4,5,6,7])
# print(a[1:5:2])

#>>Return every other element from the entire array:
# import numpy as np 
# a = np.array([1,2,3,4,5,6,7,8,9])
# print(a[::2])

#>>Slicing 2-D Arrays
# import numpy as np 
# a = np.array([[1,2,3,4,5],[5,6,7,8,9]])
# print(a[1,1:4])

#>>From both elements, return index 2:
# import numpy as np 
# a = np.array([[1,2,3,4],[5,6,7,8]])
# print(a[0:2,2])

#>>From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
# import numpy as np
# a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(a[0:2, 1:4])

##NumPy Data Types
#--------------------------------------

#>>Get the data type of an array object:
# import numpy as np 
# a = np.array([1,2,3,4,5])
# print(a.dtype)

#>>Get the data type of an array containing strings:
# import numpy as np 
# a = np.array(["Apple,Mango,Banana"])
# print(a.dtype)

# import numpy as np 
# b = np.array(["Apple","Mango","Banana"])
# print(b.dtype)

# import numpy as np 
# c = np.array(['apple','mango','banana'])
# print(c.dtype)

#>>Create an array with data type string:
# import numpy as np 
# a = np.array([1,2,3,4], dtype='S')
# print(a)
# print(a.dtype)

#>>Create an array with data type 4 bytes integer:
# import numpy as np 
# a = np.array([1,2,3,4,5,6,7,8],dtype='i1')
# print(a)
# print(a.dtype)

# import numpy as np 
# b = np.array([1,2,3,4,5,6,7,8],dtype='i2')
# print(b)
# print(b.dtype)

# import numpy as np                           #Error Asbe
# c = np.array([1,2,3,4,5,6,7,8],dtype='i3')
# print(c)
# print(c.dtype)

# import numpy as np 
# d = np.array([1,2,3,4,5,6,7,8],dtype='i4')
# print(d)
# print(d.dtype)

# import numpy as np 
# e = np.array([1,2,3,4,5,6,7,8],dtype='i5')
# print(e)
# print(e.dtype)

# import numpy as np 
# f = np.array([1,2,3,4,5,6,7,8],dtype='i6')
# print(f)
# print(f.dtype)

# import numpy as np 
# g = np.array([1,2,3,4,5,6,7,8],dtype='i7')
# print(g)
# print(g.dtype)


# import numpy as np 
# h = np.array([1,2,3,4,5,6,7,8],dtype='i8')
# print(h)
# print(h.dtype)

#>>A non integer string like 'a' can not be converted to integer (will raise an error):
# import numpy as np
# a = np.array(['1','2','a','4','5','6'],dtype='i')
# print(a)
# print(a.dtype)

# import numpy as np 
# a = np.array(['1,2,3,4,5,6,7'],dtype='i')
# print(a)
# print(a.dtype)

#>>Change data type from float to integer by using 'i' as parameter value:
# import numpy as e
# a = e.array([1.1,1,2.1,3])
# e = a.astype('i')
# print(e)
# print(e.dtype)

#>>Change data type from float to integer by using int as parameter value:
# import numpy as np 
# a = np.array([1,2,3,4])
# b = a.astype('int')
# print(b)
# print(b.dtype)

# import numpy as np 
# a = np.array([1.1,2.2,3.3])
# b = a.astype('int')
# print(b)
# print(b.dtype)

# import numpy as np 
# a = np.array([1,0,7])
# b = a.astype('bool')
# print(b)
# print(b.dtype)

## NumPy Array Copy vs View:
#--------------------------------------------

#>>Make a copy, change the original array, and display both arrays:
# import numpy as np  
# a = np.array([1,2,3,4,5,6,7,8])
# b = a.copy()
# a[1] = 356
# print(a)
# print(b)

#>>Make a view, change the original array, and display both arrays:
# import numpy as np 
# a = np.array([1,2,3,4])
# b = a.view()
# a[1] = 50
# print(a)
# print(b)

#>>Make a view, change the view, and display both arrays:
# import numpy as np 
# a = np.array([1,2,3,4])
# b = a.view()
# b[2] = 24
# print(a)
# print(b)

#>>Print the value of the base attribute to check if an array owns it's data or not:
# import numpy as np 
# a = np.array([1,2,3,4])
# b = a.copy()
# c = a.view()
# print(b.base)
# print(c.base)
