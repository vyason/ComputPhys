# python code for calculating factorials
# Copyright (C) 2022  Ankit Kumar
# Email: akvyas1995@gmail.com
#-----------------------------------------------------------------------
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#-----------------------------------------------------------------------


import numpy as np


#calculates factorials using the normal method
#----------------------------------------------------------------------
def calc_fact(nmax):
    fact = np.zeros(nmax+1,float)
    fact[0],fact[1] = 1,1
    for i in range(2,nmax+1):
        fact[i] = i*fact[i-1]
    return fact

#calculates factorials using log scale (accurate for large numbers)
#----------------------------------------------------------------------
def calc_lfact(nmax):
    lfact = np.zeros(nmax+1,float)
    lfact[0],lfact[1] = 0,0
    for i in range(2,nmax+1):
        lfact[i] = np.log(i) + lfact[i-1]
    return np.exp(lfact)



if __name__ == "__main__":

    nmax = 10
    fact = calc_fact(nmax)
    lfact = calc_lfact(nmax)

    print('n \t fact[n] \t lfact[n]')
    print('-----------------------------------------')
    for n in range(0,nmax+1):
        print(f'{n} \t {fact[n]:E} \t {lfact[n]:E}')