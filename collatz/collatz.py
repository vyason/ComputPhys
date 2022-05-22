# python code for calculating CG coefficients using the Racah method
# Copyright (C) 2022  Ankit Kumar
# Email: akvyas1995@gmail.com
#-----------------------------------------------------------------------
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#-----------------------------------------------------------------------


#collatz function: returns the collatzsteps i_n for a given number n
#-----------------------------------------------------------------------
def collatz(n):
    i_n = 0
    while n!=1:
        if n%2==0:
            n = n/2
        else:
            n = 3*n + 1
        i_n = i_n + 1
    return i_n


#example using parallel programming
#-----------------------------------------------------------------------
if __name__ == "__main__":
    import numpy as np
    from joblib import Parallel, delayed

    #minnimum and maximum n vals
    n_min,n_max = 1e0,1e3

    n_vals = range(int(n_min),int(n_max+1))
    
    #calling collatz functions parallely (n_jobs = -2 means ncores = ncores_max - 1)
    i_n = Parallel(n_jobs=-2)(delayed(collatz)(n) for n in n_vals)

    #saving the data in collatz.dat
    np.savetxt('collatz.dat',np.stack((n_vals,i_n),axis=1),fmt="%d")
