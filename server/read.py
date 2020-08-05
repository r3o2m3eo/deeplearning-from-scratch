import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('./out/img.png')
fig = plt.figure()
plt.imshow(img)
fig.savefig('./out/read.png')

