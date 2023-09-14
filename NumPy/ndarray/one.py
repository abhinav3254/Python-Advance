import numpy as np;


'''
# The basic ndarray is created using an array function in NumPy as follows −
# np.array;


# It creates an ndarray from any object exposing array interface, or from any method that returns an array.

# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# breaking the terms 

#object -> Any object exposing the array interface method returns an array, or any (nested) sequence.
# dtype -> Desired data type of array, optional

a = np.array([1,2,3]) 
print(a);

arr = np.array(
    [
    [1,2,3],
    [3,4,5]
    ]
);

# for get the type of the array
print('type of array is -> ',type(arr));
print('dimesions of the array -> ',arr.ndim);
print('shape of the array -> ',arr.shape);
print('size of the array',arr.size);
print('arrays are stored in the data type of ',arr.dtype);
print('printing the array -> ',arr);


print('---------------------')
arr2 = np.array([1,2,3],dtype=complex)
print(arr2);


# little change
print('before shape define')
arr3 = np.array([[1,2,3],[4,5,6]])
print(arr3)
print('after shape define')
arr3.shape = (3,2);
print(arr3);
print('after making it to 6,1')
arr3.shape = (6,1);
print(arr3)

# we can reshape array
arr4 = np.array([[1,2,3,4],[5,6,7,8]])
arr5 = arr4.reshape(4,2);
print('array 5 is now printing after changing it\'s shape')
print(arr5)


# this is one dimesional array
print('\n----------------------\n')
arr7 = np.arange(24) 
print(arr7);
arr6 = np.arange(24);
# making it ndim array
arr6.ndim
# now reshape it
brr6 = arr6.reshape(2,4,3);
# explaination of this thing -> make two array 2 means
# 4 means 4 row
# and 3 means 3 column
print(brr6);


# -----------------numpy.empty--------------------------

# This is the format
# numpy.empty(shape, dtype = float, order = 'C')
# Shape of an empty array in int or tuple of int
# Desired output data type. Optional
# 'C' for C-style row-major array, 'F' for FORTRAN style column-major array

# example :- 
x = np.empty([3,2],dtype=int)
print(x)

# numpy.zeros(shape, dtype = float, order = 'C')
x = np.zeros(5) 
print(x)
# numpy as array

# numpy.asarray(a, dtype = None, order = None)
# a -> datasource that can be list,tuples or anything else

x = [1,2,3,4]
arr = np.asarray(x)
print(arr)
# now reshape it
arr = arr.reshape(2,2)
print(arr)
'''

# to print the ranged value
print(np.array(range(1,11)))