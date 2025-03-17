import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from mpl_toolkits.axes_grid1 import make_axes_locatable
import random


ca = np.zeros((50, 50), dtype=int)
tau0 = 20
ca[(1, 1)] = 1
ca[(48, 48)] = 1
tauI = 10
time = 200
colormap = colors.ListedColormap(['white', 'red', 'lightblue'])
norm = colors.BoundaryNorm([0, 1, tauI, tau0], 3)
S = []
Inf = []
R = []
T = []
fig, ax = plt.subplots(1, 2)
ax[1].legend()
cax = make_axes_locatable(ax[0]).append_axes('right', size='5%', pad=0.1)
for t in range(time):
    T.append(t)
    s = 50*50 - np.count_nonzero(ca)
    S.append(s)
    inf = 0
    for day in range(1, tauI + 1):
        inf += np.count_nonzero(ca == day)
    Inf.append(inf)
    r = 50*50 - inf - s
    R.append(r)
    ax[0].cla()
    im = ax[0].imshow(ca, cmap=colormap, norm=norm)
    plt.colorbar(im, spacing='proportional', cax=cax)
    ax[1].cla()
    ax[1].plot(T, S, color='green', label='Sus')
    ax[1].plot(T, Inf, color='red', label='Inf')
    ax[1].plot(T, R, color='lightblue', label='Ref')
    ax[1].legend()
    plt.pause(0.0000001)
    trans = ca.copy()
    for i in range(1, 49):
        for j in range(1, 49):
            migi = random.choice(range(1, tauI + 1))
            migr = random.choice(range(tauI + 1, tau0 + 1))
            mig = random.choices([0, migi, migr],
                                 cum_weights=[s, s+inf, 2500])[0]
            trans[(i, j)] = random.choices([trans[(i, j)], mig],
                                           cum_weights=[0.99, 1])[0]
            if trans[(i, j)] == tau0:
                ca[(i, j)] = 0
            elif trans[(i, j)] == 0:
                inei = 0
                for o in range(i-1, i+2):
                    for m in range(j-1, j+2):
                        if trans[(o, m)] > 0 and trans[(o, m)] <= tauI:
                            inei += 1
                ca[(i, j)] = random.choices([1, 0], cum_weights=[inei, 8])[0]
            else:
                ca[(i, j)] = trans[(i, j)] + 1
plt.show()
plt.close()
