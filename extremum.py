# python code for finding extremum of a function
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


import numpy as np


#golden ratio search algoritm
#f = function    (a,b) = limits    accy = accuracy    ext_type = min/max
#----------------------------------------------------------------------
def extremum_grs(f,a,b,accy,ext_type):
    gr = (1+np.sqrt(5))/2                   #golden ratio
    c,d = b-(b-a)/gr,a+(b-a)/gr
    
    if ext_type=='min':
        while np.abs(b-a) > accy:
            if f(c) < f(d):
                b = d
            else:
                a = c
            c,d = b-(b-a)/gr,a+(b-a)/gr
        return (b+a)/2,f((b+a)/2)

    elif ext_type=='max':
        while np.abs(b-a) > accy:
            if f(c) > f(d):
                b = d
            else:
                a = c
            c,d = b-(b-a)/gr,a+(b-a)/gr
        return (b+a)/2,f((b+a)/2)

    else:
        raise Exception('ERROR: specify extrema as min/max')



#examples
if __name__ == "__main__":

    from math import pi

    def func(x):
        return np.sin(x)

    #sinx has a maxima at pi/2
    x0,f0 = extremum_grs(func,0,pi,1e-5,ext_type='max')
    print(x0/pi,f0)

    #sinx has a minima at 3*pi/2
    x0,f0 = extremum_grs(func,pi,2*pi,1e-5,ext_type='min')
    print(x0/pi,f0)

