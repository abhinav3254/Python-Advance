import numpy as np;

# The basic ndarray is created using an array function in NumPy as follows −
# np.array;


# It creates an ndarray from any object exposing array interface, or from any method that returns an array.

# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# breaking the terms 

#object -> Any object exposing the array interface method returns an array, or any (nested) sequence.
# dtype -> Desired data type of array, optional

a = np.array([1,2,3]) 
print(a);