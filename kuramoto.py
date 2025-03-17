from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

ks = np.linspace(0, 10, num=50)
ravgs = []
osc = 1000
pi = np.pi
stdevs = [1, 2, 3]


for stdev in stdevs:
    omega = np.random.normal(loc=0, scale=stdev, size=osc)  # natural frequency
    for k in ks:
        def sumSin(thetas):
            sin = []
            for theta in thetas:
                thetaI = np.full_like(thetas, theta)
                j = np.subtract(thetas, thetaI)
                sinJ = np.sin(j)
                sumSinJ = np.sum(sinJ)
                sin.append(sumSinJ)
            return sin


        def func(t, theta):
            sin = sumSin(theta)
            sin = np.array(sin)
            sin = (k/osc)*sin
            thetaDot = np.add(omega, sin)
            return thetaDot


        print('New Program')
        thetaIn = np.random.rand(osc)
        thetaIn = 2*pi*thetaIn  # initial theta values
        print('theta initial:', thetaIn)
        thetas = solve_ivp(fun=func, t_span=(0, 100), y0=thetaIn, t_eval=
                        np.linspace(0, 100, num=1000))
        print(thetas.y)
        r = []
        for t in range(1000):
            row = thetas.y[:, t]
            print('row:', row)
            rI = np.absolute(sum(np.e**(1j*row)))/osc
            r.append(rI)
        # plt.plot(thetas.t, r)
        ravg = np.array(r[899:999])
        ravg = np.sum(ravg)/100
        ravgs.append(ravg)
        print('ravg', ravg)
    plt.plot(ks, ravgs, label='N:0,'+str(stdev))
plt.legend()
plt.show()
