import matplotlib.pyplot as plt 
import numpy as np 
from cvxpy import * 

import subprocess 
import shlex
#parabola parameters
V = np.array([[1,0],[0,0]])
u = np.array([0,-0.5]).reshape(2,1)
f = 0
# parameters of Tr(AX) expression
A = np.block([[V,u],[u.T,f]])

X = Variable((3,3), symmetric=True)
#generating points in the range(0,5) 
num_pts = 50
gen_pts = np.linspace(0, 5, num_pts)
min_dist = np.zeros((num_pts,))
#parameters of Tr(CX) expression
for i in range(0, num_pts):
    P = np.array([0, gen_pts[i]]).reshape(2,1)
    C = np.hstack((np.vstack((np.eye(2), -P.T)), np.vstack((-P, np.linalg.norm(P)**2))))
#defining objective and constraints
    objective = Minimize(trace(C @ X))
    constraints = [X >> 0]
    constraints += [
        trace(A @ X) == 0,
        X[2,2] == 1
    ]
# solving the expresssion 
    prob = Problem(objective, constraints)
    prob.solve()
    min_dist[i] = np.sqrt(np.abs(prob.value))
    print(gen_pts[i], min_dist[i])
#plotting shortest distance from the points in the range(0,5) to the parabola
plt.plot(gen_pts, min_dist)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
plt.show()
#plt.savefig('/sdcard/reshma/opt/fig1.pdf')
#subprocess.run(shlex.split("termux-open /sdcard/reshma/opt/fig1.pdf"))
