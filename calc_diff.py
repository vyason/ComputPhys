# subroutines for calculating derivatives with finite-difference approximations
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


#-----------------------------------------------------------------------
# f =  function, h = grid size, J = dimension of grid
#-----------------------------------------------------------------------


import numpy as np

# 1st order derivative (3pt central difference)
#-----------------------------------------------------------------------
def diff_3pt(f,h,J):
    d2f=(np.roll(f,-1)-np.roll(f,+1))/(2*h)
    d2f[0]=d2f[J-1]=0
    return d2f

# 1st order derivative (5pt central difference)
#-----------------------------------------------------------------------
def diff_5pt(f,h,J):
    df=(-(np.roll(f,-2)-np.roll(f,+2))+8*(np.roll(f,-1)-np.roll(f,+1)))/(12*h)
    df[0]=df[1]=df[J-2]=df[J-1]=0
    return df

# 2nd order derivative (3pt central difference)
#-----------------------------------------------------------------------
def diff2_3pt(f,h,J):
    d2f=(np.roll(f,-1)+np.roll(f,+1)-2*f)/h**2
    d2f[0]=d2f[J-1]=0
    return d2f

# 2nd order derivative (5pt central difference)
#-----------------------------------------------------------------------
def diff2_5pt(f,h,J):
    d2f=(-(np.roll(f,-2)+np.roll(f,+2))+16*(np.roll(f,-1)+np.roll(f,+1))-30*f)/(12*h**2)
    d2f[0]=d2f[1]=d2f[J-2]=d2f[J-1]=0
    return d2f