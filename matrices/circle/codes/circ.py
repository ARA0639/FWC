import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                                                #for path to external scripts
sys.path.insert(0,'/home/reshma/downloads/fwc-assignment-1/matrices/circle/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
#from conics.funcs import circ_gen
from conics.funcs import *
import subprocess
import shlex

o = np.array(([0,0]))
I =  np.eye(2)
e1 =  I[:,0]
e2 =  I[:,1]
#Input parameters

#line parameters
n1 =  np.array(([1,-2])) #normal vector
m1 =  omat@n1 #direction vector
c1 = -3
x1 = c1/(n1@e1)*e1 #x-intercept
y1 = c1/(n1@e2)*e2 # y-intercept
y2 = np.array(([0,1]))
A= np.linalg.norm(x1-o)
B= np.linalg.norm(y1-o)
C= np.linalg.norm(y2-o)
k = (A)/(B*C)
print('k=',k)
x2 =np.array(([-0.5,0]))
n2 = np.array(([2,-1]))
m2 = omat@n2
c2=-1
q2 = x2
q1=x1
n3= np.array(([1,0]))
m3= omat@n3
n4 = np.array(([0,1]))
m4=omat@n4

#Points of intersection
#of line with circle

A = line_intersect(n1,x1,n3,o)
B= line_intersect(n2,y2,n3,o) 
C= line_intersect(n1,x1,n4,o) 
D= line_intersect(n2,y2,n4,o)
O =line_intersect(n3,o,n4,o)
print('Intersection Points:')
print(A,B,C,D,O)


#circle parameters
#centre
c1 =(x1+x2)/2
c2 =(y1+y2)/2

P= np.array(([c1[0],c2[1]]))
print('center=',P)
r = np.linalg.norm(P-x1)
print('radius=',r)



#genarating  lines
k1=-2
k2= 2
v1=-4
v2= 4
line1 = line_dir_pt(m1,q1,k1,k2)
line2 = line_dir_pt(m2,q2,k1,k2)
line3 = line_dir_pt(m3,o,v1,v2)
line4 = line_dir_pt(m4,o,v1,v2)


#Generating the circle
x_circ= circ_gen(P,r)



#Plotting all lines
plt.plot(line1[0,:],line1[1,:],'-r',label='$x-2y+3=0$')
plt.plot(line2[0,:],line2[1,:],'-r',label='$2x-y+1=0$')
plt.plot(line3[0,:],line3[1,:],'-g',label='$x=0$')
plt.plot(line4[0,:],line4[1,:],'-g',label='$y=0$')

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')

#Labeling the coordinates
tri_coords = np.vstack((A,B,C,D,O,P)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','O','P']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-3,3), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()

plt.savefig('/sdcard/reshma/matrices/circle/fig/circle.pdf')
subprocess.run(shlex.split("termux-open /sdcard/reshma/matrices/circle/fig/circle.pdf"))






