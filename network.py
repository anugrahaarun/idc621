import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


nodes = 500
neighbours = 100
p = 0.1
adjMat = np.zeros((nodes, nodes))
for row in range(nodes):
    left = int(row - neighbours/2)
    right = int(row + neighbours/2 + 1)
    if left < 0:
        left = nodes + left
        adjMat[row][0:right] = 1
        adjMat[row][left:] = 1
    elif right > nodes - 1:
        right = right - nodes
        adjMat[row][left:] = 1
        adjMat[row][0:right] = 1
    else:
        adjMat[row][left:right] = 1
    adjMat[row][row] = 0
for row in range(nodes):
    posNewNodes = np.arange(0, nodes)
    for i in range(1, neighbours + 1):
        pre = row - i
        post = row + i
        if pre < 0:
            pre = nodes + pre
        if post >= nodes:
            post = post - nodes
        oldNodes = [pre, post]
        print(oldNodes)
        for oldNode in oldNodes:
            adjMat[row][oldNode] = np.random.choice((1, 0), p=(1-p, p))
            if adjMat[row][oldNode] == 0:
                for x in range(nodes):
                    newNode = np.random.choice(posNewNodes)
                    if adjMat[row][newNode] == 1:
                        continue
                    else:
                        adjMat[row][newNode] = 1
                        adjMat[newNode][row] = 1
                        break
pi = np.pi
ks = np.linspace(0, 10, num=50)
omega = np.random.normal(size=nodes)  # natural frequency
ravgs = []
for k in ks:
    def sumSin(thetas):
        sin = []
        for i in range(nodes):
            theta = thetas[i]
            thetaI = np.full_like(thetas, theta)
            j = np.subtract(thetas, thetaI)
            sinJ = np.sin(j)
            netSinJ = np.multiply(sinJ, adjMat[i])
            sumSinJ = np.sum(netSinJ)
            sin.append(sumSinJ)
        return sin

    def func(t, theta):
        sin = sumSin(theta)
        sin = np.array(sin)
        sin = (k/neighbours)*sin
        thetaDot = np.add(omega, sin)
        return thetaDot
    print('New Program')
    thetaIn = np.random.rand(nodes)
    thetaIn = 2*pi*thetaIn  # initial theta values
    print('theta initial:', thetaIn)
    thetas = solve_ivp(fun=func, t_span=(0, 100), y0=thetaIn, t_eval=
                        np.linspace(0, 100, num=1000))
    print(thetas.y)
    r = []
    for t in range(1000):
        row = thetas.y[:, t]
        rI = np.absolute(sum(np.e**(1j*row)))/nodes
        r.append(rI)
    plt.plot(thetas.t, r, label='K='+str(k))
    plt.title('Rewiring probability, '+str(p))
    plt.savefig('rtp'+str(p)+'n100v1000.png')
    #ravg = np.array(r[899:999])
    #ravg = np.sum(ravg)/100
    #ravgs.append(ravg)
    #print('ravg', ravg)
#plt.plot(ks, ravgs, label='prob'+str(p))
#plt.savefig('rkp'+str(p)+'n60v300.png')
#plt.legend()
