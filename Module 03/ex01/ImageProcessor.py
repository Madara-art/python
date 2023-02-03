from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class ImageProcessor:
	@staticmethod
	def load(path):
		try:
			img = Image.open(path)
		except FileNotFoundError:
			return None
		img = np.asarray(img)
		print(f"Loading image of dimensions {img.shape[0]} x {img.shape[1]}")
		return img
	@staticmethod
	def display(array):
		plt.imshow(array, cmap='gray')
		plt.show()
