import cv2
import numpy as np
from matplotlib import pyplot as plt
from auto_a_b import auto_a_b

fname = 'train.jpg'

img0 = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
x, y = auto_a_b(fname)

#linearly expand
img1 =   255 * ( (img0 - x[0]) / (x[1] - x[0]) )
img1 [img1 < 0] = 0
img1 [img1 > 255] = 255
img1 = img1.astype(np.uint8)

#equalization expand
img2 = cv2.equalizeHist(img0)


f, axes = plt.subplots(2, 3) #f is figure and axes is array

axes[0,0].set_alpha(0.5)
axes[0,0].set_title(label='original')
axes[0,0].imshow(img0, 'gray', vmin=0, vmax=255)
axes[0,0].axis('off')
axes[1,0].hist(img0.ravel(),256,[0,256])

axes[0,1].set_title(label='linear_expand')
axes[0,1].imshow(img1, 'gray', vmin=0, vmax=255)
axes[0,1].axis('off')
axes[1,1].hist(img1.ravel(),256,[0,256])

axes[0,2].set_title(label='equalization_expand')
axes[0,2].imshow(img2, 'gray', vmin=0, vmax=255)
axes[0,2].axis('off')
axes[1,2].hist(img2.ravel(),256,[0,256])
save_name = fname[:-4] + 'plot'
# plt.savefig(save_name)
plt.show()




