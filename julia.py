import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


pixels = 1000
minz, maxz = -1.5, 1.5
size = maxz - minz

c = complex(-0.55, 0.55)
bound = 10
maxIter = 1000
juliaImage = np.zeros((pixels, pixels))
for x in range(pixels):
    for y in range(pixels):
        xScaled = (x*size)/pixels - maxz
        yScaled = (y*size)/pixels - maxz
        z = complex(xScaled, yScaled)
        it = 0
        while abs(z) <= bound and it < maxIter:
            z = z ** 2 + c
            it += 1
        colour = it/maxIter
        juliaImage[x, y] = colour
plt.imshow(juliaImage, interpolation='nearest', cmap=cm.Spectral)
plt.axis('off')
plt.show()
