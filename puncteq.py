import numpy as np
import random
import matplotlib.pyplot as plt


animals = 4096
time = 100000000
ecosys = np.random.rand(animals)
# empty = np.zeros((time, animals))
# minBar = []
loc = []
for x in range(time):
    print(x)
    minFit = np.argmin(ecosys)
    loc.append(minFit)
    # minBar.append(ecosys[minFit])
    ecosys[minFit] = random.random()
    # empty[(x, minFit)] = 1
    if minFit == 0:
        ecosys[animals-1] = random.random()
        ecosys[minFit+1] = random.random()
        # empty[(x, animals-1)] = 1
        # empty[(x, minFit+1)] = 1
    elif minFit == animals - 1:
        ecosys[minFit-1] = random.random()
        ecosys[0] = random.random()
        # empty[(x, 0)] = 1
        # empty[(x, minFit-1)] = 1
    else:
        ecosys[minFit-1] = random.random()
        ecosys[minFit+1] = random.random()
        # empty[(x, minFit-1)] = 1
        # empty[(x, minFit+1)] = 1
# plt.imshow(empty, cmap='binary', aspect='auto', origin='lower')
# plt.xlabel('X')
# plt.ylabel('Count Time')
# minWeight = np.zeros(time) + 1.0/time
# barrierWeight = np.zeros_like(ecosys) + 1.0/ecosys.size
# plt.hist(minBar, label='Minimum Barriers', histtype='step', bins=100,
#         weights=minWeight)
# plt.hist(ecosys, weights=barrierWeight, label='Barrier distribution',
#         histtype='step', bins=100)
# plt.xlabel('Barrier, B')
# plt.ylabel('Probability, P(B)')
distance = np.ediff1d(loc)
distance = np.absolute(distance)
distance = np.where(distance < animals/2, distance, animals-distance)
distance = distance + 1
logdist = np.log10(distance)
logWeight = np.zeros_like(logdist) + 1.0/logdist.size
plt.hist(logdist, histtype='step', bins=100, weights=logWeight,
         log=True, label='Count Time ='+str(time))
plt.xlabel('Log(X)')
plt.ylabel('Log(C(X))')
plt.legend(loc='upper center')
plt.margins(x=0)
plt.show()
