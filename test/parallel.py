import numpy as np
from joblib import Parallel, delayed
import matplotlib.pyplot as plt


def collatz_steps(n):
    steps = 0
    while n!=1:
        if n%2==0:
            n = n/2
        else:
            n = 3*n + 1
        steps = steps + 1
    return steps


n_max = int(np.genfromtxt('n_max'))

steps_vals = Parallel(n_jobs=-2)(delayed(collatz_steps)(i) for i in range(1,n_max,1))


plt.hist(steps_vals,bins=1000)
plt.savefig('collatz.pdf')

