# python code for finding root of a function using the bisection method
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


#f = function    (a,b) = limits    accy = accuracy
#----------------------------------------------------------------------
def root_bisect(f,a,b,accy,iter_max):
    
    if f(a)*f(b) > 0:
        raise Exception('invalid limits')
    
    for i in range(iter_max):
        
        err = np.abs(b-a)
        if err < accy:
            break

        c = (a+b)/2
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        
    return (a+b)/2,err


#f = function, df = derivative of function    a = initial    accy = accuracy
#----------------------------------------------------------------------
def root_newtraph(f,df,a,accy,iter_max):
    
    for i in range(iter_max):

        b = a - f(a)/df(a)

        err = np.abs(b-a)
        if err < accy:
            break
        else:
            a = b

    return b,err


#f = function,   (a,b) = limits    accy = accuracy
#----------------------------------------------------------------------
def root_secant(f,a,b,accy,iter_max):
    
    if f(a)*f(b) > 0:
        raise Exception('invalid limits')
    
    for i in range(iter_max):

        err = np.abs(b-a)
        if err < accy:
            break

        c = (a*f(b)-b*f(a))/(f(b)-f(a))
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return (a*f(b)-b*f(a))/(f(b)-f(a)),err



#examples
if __name__ == "__main__":
    from math import pi

    #sinx has a root at pi
    def func(x):
        return np.sin(x)
    def dfunc(x):
        return np.cos(x)

    accy = 1e-5

    x0,err = root_bisect(func,pi-0.1,pi+0.2,accy,100)
    print(f'Bisecton: {x0:f}\t{err:e}')

    x0,err = root_newtraph(func,dfunc,pi-0.1,accy,100)
    print(f'Newt-Raph: {x0:f}\t{err:e}')

    x0,err = root_secant(func,pi-0.1,pi+0.2,accy,100)
    print(f'Secant: {x0:f}\t{err:e}')


