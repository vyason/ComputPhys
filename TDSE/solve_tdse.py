# python code for solving the TDSE using Cayley's operator
# Copyright (C) 2022  Ankit Kumar
# Email: akvyas1995@gmail.com
#-----------------------------------------------------------------------

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

#-----------------------------------------------------------------------


import numpy as np
from math import pi
import matplotlib.pyplot as plt
from scipy.integrate import simps
from scipy.sparse import spdiags
from scipy.sparse.linalg import splu


# 2nd order derivative (3pt central difference)
#-----------------------------------------------------------------------
def diff2(f,h,J):
    d2f=(np.roll(f,-1)+np.roll(f,+1)-2*f)/h**2
    d2f[0]=d2f[J-1]=0
    return d2f

# LU matrix on the left: tridiagonal case
#-----------------------------------------------------------------------
def lhs_lumatrix(J,dx,dt,V,hb,hb2m):
    a = 1 + 1j*dt*(2*hb2m/dx**2 + V)/(2*hb)
    b = (-1j*hb2m*dt/(2*hb*dx**2))*np.ones((J),float)
    return splu(spdiags(np.array([b,a,b]),np.array([-1,0,+1]),J,J).tocsc())

# zeta vector on the right: tridiagonal case
#-----------------------------------------------------------------------
def zeta(J,psi,dx,dt,V,hb,hb2m):
    return psi - 1j*(dt/hb)*(-hb2m*diff2(psi,dx,J)+V*psi)/2



hb = 1                                  #Planck's constant, hbar
m =	1                                   #mass of particle, m


# defining the system for harmonic oscillator
#-----------------------------------------------------------------------

xmin,xmax,dx = -20,+20,0.01              #x-limits of simulation box
x = np.arange(xmin,xmax+dx,dx)          #defining the position grid
J = len(x)                              #dimension of position grid

w = 0.1                                 #freq of harmonic oscillator
V = 1/2*m*w**2*x**2                     #harmonic oscillator potential

x0,p0,sig = -10,0,1                     #initial position,momentum, position spread

psi = np.exp( -((x-x0)/(2*sig))**2 + 1j*p0*(x-x0) )/np.sqrt( sig*np.sqrt(2*pi) )

tmax,dt,plot_steps =  2*(2*pi/w),0.01,10        #time limit, time step, and interval b/w 2 successive plots



# solving the TDSE
#-----------------------------------------------------------------------

hb2m = hb**2/(2*m)                                          #value of hbar^2/2m
lhs_lu = lhs_lumatrix(J,dx,dt,V,hb,hb2m)	                #LU decomposition for the LHS matrix

t = 0
ymax = 1.01*np.max(np.abs(psi)**2)
while t < tmax:

    for j in range(plot_steps):                             #evolve plot_steps times
        psi = lhs_lu.solve(zeta(J,psi,dx,dt,V,hb,hb2m))   
    t = t + plot_steps*dt

    plt.cla()
    plt.xlim(xmin,xmax);                    plt.ylim(0,ymax)
    plt.xlabel(r'$x$',fontsize=14);         plt.ylabel(r'$|\psi|^2$',fontsize=14)
    plt.title(f'$t$ = {t:.1f}');            plt.grid()
    plt.plot(x,np.abs(psi)**2,c='red');      plt.pause(0.001)
