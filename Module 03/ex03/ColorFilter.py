import numpy as np

class ColorFilter:
	def invert(self, array):
		"""
			Inverts the color of the image received as a numpy array.
		Args:
		-----
			array: numpy.ndarray corresponding to the image.
		Return:
		-------
			array: numpy.ndarray corresponding to the transformed image.
			None: otherwise.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		arr_cpy = array.copy()
		print(arr_cpy)
		arr_cpy[:,:,3] = 255 - arr_cpy[:,:,:3]
		return arr_cpy
	def to_blue(self, array):
		"""
		Applies a green filter to the image received as a numpy array.
		Args:
		-----
			array: numpy.ndarray corresponding to the image.
		Return:
		-------
			array: numpy.ndarray corresponding to the transformed image.
			None: otherwise.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		arr_cpy = array.copy()
		arr_cpy[:,:,:2] = 0
		return arr_cpy

	def to_green(self, array):
		"""
		Applies a green filter to the image received as a numpy array.
		Args:
		-----
			array: numpy.ndarray corresponding to the image.
		Return:
		-------
			array: numpy.ndarray corresponding to the transformed image.
			None: otherwise.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		arr_cpy = array.copy()
		arr_cpy[:,:,0] = 0
		arr_cpy[:,:,2] = 0
		return arr_cpy
	def to_red(self, array):
		"""
		Applies a red filter to the image received as a numpy array.
		Args:
		-----
			array: numpy.ndarray corresponding to the image.
		Return:
		-------
			array: numpy.ndarray corresponding to the transformed image.
			None: otherwise.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		arr_cpy = array.copy()
		arr_cpy[:,:,1:3] = 0
		return arr_cpy
	def to_celluloid(self, array):
		"""
		Applies a celluloid filter to the image received as a numpy array.
		Celluloid filter must display at least four thresholds of shades.
		Be careful! You are not asked to apply black contour on the object,
		you only have to work on the shades of your images.
		Remarks:
		celluloid filter is also known as cel-shading or toon-shading.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		ar = array.copy()[:,:,:3]
		arra = array.copy()
		ls = np.linspace(0,255,num=5,endpoint=False)
		tmp = array.copy()[:,:,:3]
		for l in ls:
			ar[tmp>l] = l
		arra[:,:,:3] = ar
		return arra

	def to_grayscale(self, array, filter, **kwargs):
		"""
		Applies a grayscale filter to the image received as a numpy array.
		For filter = 'mean'/'m': performs the mean of RBG channels.
		For filter = 'weight'/'w': performs a weighted mean of RBG channels.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		filter: string with accepted values in ['m','mean','w','weight']
		weights: [kwargs] list of 3 floats where the sum equals to 1,
		corresponding to the weights of each RBG channels.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		arr = None
		if filter in ['m','mean']:
			arr = array.copy()
			ar = np.sum(array[:,:,:3],axis = 2)
			ar = ar/3
			ar = ar.reshape(array.shape[0],array.shape[1],1)
			out = np.broadcast_to(ar,(array.shape[0],array.shape[1],3))
			arr[:,:,:3] = out
		if filter in ['w','weight']:
			if 'weights' in kwargs.keys() and sum(kwargs['weights']) == 1:
				arr = array.copy()
				ar = array[:,:,:3].astype(np.float64)*kwargs['weights']
				arr[:,:,:3] = ar
		# red = self.to_red(array)[:,:,0]
		# blue = self.to_blue(array)[:,:,1]
		# green = self.to_green(array)[:,:,2]
		# arr1 = (red+blue+green / 3).reshape(array.shape[0],array.shape[1],1)
		# an = array.copy()
		# an[:,:,:3] =  np.broadcast_to(arr1,(array.shape[0],array.shape[1],3))
		return arr
