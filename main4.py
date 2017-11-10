from platypus import NSGAII, Problem, Real
import sys
import numpy as np
import random

random.seed(10)

ri=[]
xi,yi,zi=[],[],[]

def take_input():
    print "============== INPUTS =============="
    global n, di,ci,ri,d,cd,s,cs, xi,yi,zi, xm,ym,zm, rmax,bmax,zs
    n =input('n: ')
    di=input('di: ')
    ci=input('ci: ')
    for i in range(n):
        ri.append(input('r['+str(i)+']: ') )
    d=input('d: ')
    cd=input('cd: ')
    s=input('s: ')
    cs=input('cs: ')
    for i in range(n):
        xi.append(input('x['+str(i)+']: ') )
        yi.append(input('y['+str(i)+']: ') )
        zi.append(input('z['+str(i)+']: ') )

    xm=input('xm: ')
    ym=input('ym: ')
    zm=input('zm: ')

    rmax=input('rmax: ')
    bmax=input('bmax: ')
    
    zs =input('zs: ')

def belegundu(l):
    x,y,z,xs,ys=l
    f1,f2,f3=0,0,0
    for i in range(n):
        f1 += (di+ci*ri[i])*(((x-xi[i])**2+(y-yi[i])**2+(z-zi[i])**2 )**0.5)
    for i in range(n):        
        f2 += (d +cd*ri[i])*(((x-xs)**2+(y-ys)**2+(z-zs)**2 )**0.5)
    for i in range(n):
        f3 += (s +cs*ri[i])*(((xm-xs)**2+(ym-ys)**2+(zm-zs)**2 )**0.5)
    f = f1+f2+f3

    c1=[]
    for i in range(n):
        c1.append(abs(z-zi[i])*1.0/(( (x-xi[i])**2+(y-yi[i])**2 )**0.5) - rmax)
    c2 = abs(z-zs)*1.0/(( (x-xs)**2+(y-ys)**2 )**0.5) - rmax
    c3 = abs(zm-zs)*1.0/(( (xm-xs)**2+(ym-ys)**2 )**0.5 ) - bmax
    c = c1+[c2]+[c3]
    return [f], c

take_input()
problem = Problem(5, 1, n+2)
problem.types[:] = Real(0, 2000)#[Real(-sys.maxint,sys.maxint),Real(-sys.maxint,sys.maxint),Real(-sys.maxint,sys.maxint),Real(0, 2000), Real(0, 2000), Real(0, 2000)]
problem.constraints[:] = "<=0"
problem.function = belegundu

algorithm = NSGAII(problem)
algorithm.run(100000)

print "============== OUTPUTS =============="
'''
print 'Solution:'
for solution in algorithm.result:
    print(solution.objectives), solution.variables
'''
index= np.argmax(algorithm.result)
print 'Objective functtion value: ',algorithm.result[index].objectives[0]
print 'Parameters: ',algorithm.result[index].variables
