import numpy as np
from joblib import Parallel, delayed

def collatz(num):
    n,i_n = num,0
    while n!=1:
        if n%2==0:
            n = n/2
        else:
            n = 3*n + 1
        i_n = i_n + 1
    return num,i_n


n_min,n_max = 1e0,1e6

n_min,n_max = int(n_min),int(n_max)
result = Parallel(n_jobs=-2)(delayed(collatz)(n) for n in range(n_min,n_max+1,1))

n,i_n = zip(*result)
np.savetxt('collatz.dat',np.stack((n,i_n),axis=1),fmt="%i",header='n\tnstep')
