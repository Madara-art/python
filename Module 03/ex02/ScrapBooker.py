import numpy as np

class ScrapBooker:
	def crop(self, array, dim, position=(0,0)):
		"""
		Crops the image as a rectangle via dim arguments (being the new height
		and width of the image) from the coordinates given by position arguments.
		Args:
		-----
		array: numpy.ndarray
		dim: tuple of 2 integers.
		position: tuple of 2 integers.
		Return:
		-------
		new_arr: the cropped numpy.ndarray.
		None (if combinaison of parameters not compatible).
		Raise:
		------
		This function should not raise any Exception.
		"""
		if not isinstance(array,np.ndarray):
			return None
		if len(dim) != 2 or len(position) != 2:
			return None
		if dim < (0,0) or position < (0,0):
			return None
		if array.shape < dim or dim < position:
			return None
		return array[position[0]:dim[0]+position[0],position[1]:dim[1]+position[1]]


	def thin(self, array, n, axis):
		"""
		Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
		Args:
		-----
		array: numpy.ndarray.
		n: non null positive integer lower than the number of row/column of the array
		(depending of axis value).
		axis: positive non null integer.
		Return:
		-------
		new_arr: thined numpy.ndarray.
		None (if combinaison of parameters not compatible).
		Raise:
		------
		This function should not raise any Exception.
		"""
		if not isinstance(array,np.ndarray) or n < 0 or not isinstance(axis,int):
			return None
		if n == 0:
			return array
		lst = []
		if not axis:
			for row in array:
				lst.append([(x) for i, x in enumerate(row,1) if i % n])
			return np.array(lst)
		lst = [x for i,x in enumerate(array, 1) if i % n]
		return np.array(lst)

	def juxtapose(self, array, n, axis):
		"""
		Juxtaposes n copies of the image along the specified axis.
		Args:
		-----
		array: numpy.ndarray.
		n: positive non null integer.
		axis: integer of value 0 or 1.
		Return:
		-------
		new_arr: juxtaposed numpy.ndarray.
		None (combinaison of parameters not compatible).
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not isinstance(array,np.ndarray) or n < 0 or not isinstance(axis,int):
			return None
		lst = []
		if axis:
			for row in array:
				tmp = []
				for _ in range(n):
					tmp = tmp + list(row)
				lst.append(tmp)
			return np.array(lst)
		for _ in range(n):
			for row in array:
				lst.append(row)
		return np.array(lst)

	def mosaic(self, array, dim):
		"""
		Makes a grid with multiple copies of the array. The dim argument specifies
		the number of repetition along each dimensions.
		Args:
		-----
		array: numpy.ndarray.
		dim: tuple of 2 integers.
		Return:
		-------
		new_arr: mosaic numpy.ndarray.
		None (combinaison of parameters not compatible).
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not isinstance(array,np.ndarray) or dim < (0,0):
			return None
		return np.tile(array, dim)