from platypus import NSGAII, Problem, Real
import sys
import numpy as np

def take_input():
    print "============== INPUTS =============="
    global di,ci,ri,d,cd,s,cs, xi,yi,zi, x,y,z, rmax,bmax 
    di=input('di: ')
    ci=input('ci: ')
    ri=input('ri: ')
    d=input('d: ')
    cd=input('cd: ')
    s=input('s: ')
    cs=input('cs: ')
    
    xi=input('xi: ')
    yi=input('yi: ')
    zi=input('zi: ')

    x=input('x: ')
    y=input('y: ')
    z=input('z: ')

    rmax=input('rmax: ')
    bmax=input('bmax: ')

def belegundu(l):
    print "============== OUTPUTS =============="
    x,y,z,xs,ys,zs=l
    f1 = (di+ci*ri)*(((x-xi)**2+(y-yi)**2+(z-zi)**2 )**0.5)
    f2 = (d +cd*ri)*(((x-xs)**2+(y-ys)**2+(z-zs)**2 )**0.5)
    f3 = (s +cs*ri)*(((x-xs)**2+(y-ys)**2+(z-zs)**2 )**0.5)
    f = f1+f2+f3

    c1 = abs(z-zi)*1.0/(( (x-xi)**2+(y-yi)**2 )**0.5) - rmax
    c2 = abs(z-zs)*1.0/(( (x-xs)**2+(y-ys)**2 )**0.5) - rmax
    c3 = abs(zi-zs)*1.0/(( (xi-xs)**2+(yi-ys)**2 )**0.5 ) - bmax
    return [f], [c1,c2,c3]

take_input()
problem = Problem(6, 1, 3)
problem.types[:] = Real(0, 2000)#[Real(-sys.maxint,sys.maxint),Real(-sys.maxint,sys.maxint),Real(-sys.maxint,sys.maxint),Real(0, 2000), Real(0, 2000), Real(0, 2000)]
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
