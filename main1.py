from platypus import NSGAII, Problem, Real
import sys
import numpy as np

def belegundu(l):
    x,y,z,xs,ys,zs=l
    f =5000+14524.642*( (x-1160)**2+(y-1229)**2+(z-200)**2 )**0.5 + 14524.642*( (x-xs)**2+(y-ys)**2+(z-zs)**2 )**0.5 + 6602.11*( (1300-xs)**2+(1900-ys)**2+(300-zs)**2 )**0.5 
    c1 = abs(z-200)*1.0/(( (x-1160)**2+(y-1229)**2 )**0.5) - 0.14
    c2 = abs(z-zs)*1.0/( ( (x-xs)**2+(y-ys)**2 )**0.5) - 0.14
    c3 = abs(300-zs)*1.0/(( (1300-xs)**2+(1900-ys)**2 )**0.5 ) - 0.05
    return [f], [c1,c2,c3]

problem = Problem(6, 1, 3)
problem.types[:] = [Real(-sys.maxint,sys.maxint),Real(-sys.maxint,sys.maxint),Real(-sys.maxint,sys.maxint),Real(0, 2000), Real(0, 2000), Real(0, 2000)]
problem.constraints[:] = "<=0"
problem.function = belegundu

algorithm = NSGAII(problem)
algorithm.run(10000)

'''
print 'Solution:'
for solution in algorithm.result:
    print(solution.objectives), solution.variables
'''
index= np.argmax(algorithm.result)
print 'Objective functtion value: ',algorithm.result[index].objectives[0]
print 'Parameters: ',algorithm.result[index].variables