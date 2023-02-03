import numpy as np
from ScrapBooker import ScrapBooker

spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
print(spb.crop(arr1, (3,1),(1,0)))

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
print(spb.thin(arr2,-1,1))

arr3 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(spb.juxtapose(arr3, 2, 1))
