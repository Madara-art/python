from ColorFilter import ColorFilter
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open("jackie.webp")
img = np.asarray(img)
cf = ColorFilter()
# img = cf.invert(img)

# img = cf.to_green(img)
print(type(img))
# img = cf.to_grayscale(img,'w',weights = [0.7,0.3,0])
img = cf.to_celluloid(img)
# img = cf.to_blue(img)
# img = cf.to_red(img)
# print(img.shape)
# img=(np.broadcast_to(img[:,:,1].reshape(1080, 1920,1),(1080, 1920,3)))
plt.imshow(img, cmap='brg')
plt.show()