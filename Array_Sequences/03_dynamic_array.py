"""
    Lists vs Arrays
    1) The main difference between a list and an array is the functions that you can perform to them.
        For example, you can divide an array by 3, and each number in the array will be divided by 3 and the result will be printed if you request it.
        If you try to divide a list by 3, Python will tell you that it can't be done, and an error will be thrown.
    2) It does take an extra step to use arrays because they have to be declared while lists don't because they are part of Python's syntax,
        so lists are generally used more often between the two, which works fine most of the time.

"""

# below is the dynamic array implementation.
# it will let the array grow automatically when the new elements are added


import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0                              #actual count or number of elements in an array
        self.capacity = 1                       #by default it is 1 starting with first element
        self.A = self.make_array(self.capacity) #this is to create an array A(using python ctypes py_object)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        #if not 0 <= k < self.n:                    # same condition but a better way of coding
        if k < 0 or k > self.n:
            return IndexError('k is out of bound')
        return self.A[k]

    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity)           #increase the capacity to two times if it is not enough
        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()           # to make a raw array object using py_object

import sys
arr = DynamicArray()
arr.append(10)
a = arr[0]
b = len(arr)
c = sys.getsizeof(arr)
print 'value: {0:2d}, length: {1:3d}, size_in_bytes: {2:3d}'.format(a,b,c)

for k in xrange(1000):
    arr.append(k)
a = arr[1]
b = len(arr)
c = sys.getsizeof(arr)
print 'value: {0:2d}, length: {1:3d}, size_in_bytes: {2:3d}'.format(a,b,c)



#arr.append(2)
#arr.__len__()


