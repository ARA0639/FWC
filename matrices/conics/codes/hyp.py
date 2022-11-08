from sympy import *
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys
sys.path.insert(0,'/sdcard/reshma/matrices/conics/codes/CoordGeo')

#local imports
from line.funcs import*
from triangle.funcs import*
from conics.funcs import*

import subprocess
import shlex
# normal parameters
x = Symbol('x')
c =np.array([7*sqrt(3)])
# m is the vector perpendicular to normal chord ie m^tx = c
m = np.array([1,x])
omat = np.array(([0, -1], [1, 0]))
# n is the vector along the normal chord ie h + kn = x 
n = omat*m
# Conic parameters
V = np.array(([Rational(1,24), 0],[0, Rational(-1,18)]))
# Inverse of V
v = V.inv()
u = np.array([0, 0])
f = np.array([-1])
# Equation solving for x
eq1 = (n.T*v*m)**2
eq2 = (m.T*v*m)
eq3 = (c + n.T*v*u)**2
eq = -f[0,0]*eq1[0,0]/eq2[0,0] - eq3[0,0]
print(expand(eq))
print(solveset(eq, x))
x =list(solveset(eq,x))
# n1 is the vector along the normal 1
n1 = np.array(([x[0],1]))
# n2 is the  vector along the normal 2
n2 = np.array(([x[1],1]))
# direction vectors of  normals(1,2)
m2 =omat@n2
m1 = omat@n1
# point through  normal
q = np.array(([0,7*np.sqrt(3)]))
#generating normals
k1=-40
k2=40
line1 = line_dir_pt(m1,q,k1,k2)
line2 = line_dir_pt(m2,q,k1,k2)
#generating hyperbola
a=24
b=18
y = np.linspace(-60,60,120)
hyp = hyper_gen(y,a,b)
hyp2 = -hyp
#plotiing normals and hyperbola
plt.plot(line2[0,:],line1[1,:],'-r',label ='normal')
plt.plot(line2[0,:],line2[1,:],'-r',label ='normal')
plt.plot(hyp,y,'-g',label='hyperbola')
plt.plot(hyp2,y,'-g')
#labelling
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.savefig('/sdcard/reshma/matrices/conics/fig/hyp.pdf')
subprocess.run(shlex.split("termux-open /sdcard/reshma/matrices/conics/fig/hyp.pdf"))
