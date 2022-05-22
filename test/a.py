import numpy as np
from joblib import Parallel, delayed

def sum(par):
    (a,b) = par
    res = a+b
    return par,res

#genereate tuples
list_par = []
for i in range(5):
    par = [i,i]
    list_par.append(par)

list_out = Parallel(n_jobs=-2)(delayed(sum)(par) for par in list_par)

*trash,list_res = zip(*list_out)

arr_res = np.array(list_res)

print(arr_res)
print(arr_res**2)


