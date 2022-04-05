# python code for calculating CG coefficients using the Racah method
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
from math import factorial as fact


#send in double values of all constants (to avoid use of floating point numbers)
#----------------------------------------------------------------------
def cg(j1,j2,j,m1,m2):
    m = m1+m2
    term1 = (j+1)*fact((j1+j2-j)/2)*fact((j+j1-j2)/2)*fact((j+j2-j1)/2)/fact((j+j1+j2+2)/2)
    term2 = fact((j1+m1)/2)*fact((j1-m1)/2)*fact((j2+m2)/2)*fact((j2-m2)/2)*fact((j+m)/2)*fact((j-m)/2)
    [a,b,c,d,e] = np.array([round((j1+j2-j)/2),round((j1-m1)/2),round((j2+m2)/2),round((j-j2+m1)/2),round((j-j1-m2)/2)],int)    
    imin,imax = min(d,e),min(a,b,c)
    if imin<0:
        imin = -imin
    else:
        imin = 0
    term3 = 0
    for i in range(imin,imax+1):
        term3 = term3+((-1)**i/fact(i))/(fact(a-i)*fact(b-i)*fact(c-i)*fact(d+i)*fact(e+i))
    return np.sqrt(term1*term2)*term3



if __name__ == "__main__":

    j1,j2,j,m1,m2 = 3,2,3,1,0       #double values
    print(cg(j1,j2,j,m1,m2))
    print(np.sqrt(1/15))