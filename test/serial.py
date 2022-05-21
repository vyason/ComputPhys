import numpy as np
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

n_vals = np.arange(1,n_max,1)

steps_vals = []
for n in n_vals:
    steps_vals.append(collatz_steps(n))


plt.hist(steps_vals,bins=1000)
plt.savefig('chk.pdf')

