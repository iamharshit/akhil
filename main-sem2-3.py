import sys
import numpy as np
import random
from scipy.optimize import minimize

random.seed(10)

ri=[]
xi,yi,zi=[],[],[]

def frange(start,stop, step=1.0):
    while start < stop:
        yield start
        start +=step

def take_input():
    print "============== INPUTS =============="
    global n, di,ci,ri,d,cd,s,cs, xi,yi,zi, xm,ym,zm, rmaxi,bmaxi,zs
    #n, di,ci,ri,d,cd,s,cs, xi,yi,zi, xm,ym,zm, rmaxi,bmaxi,zs = [2]*17
    
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

    rmaxi=input('rmax: ')
    bmaxi=input('bmax: ')
    
    zs =input('zs: ')

def func(l, sign=1.0):
	""" Objective function """
	x,y,z,xs,ys=l
	f1,f2,f3=0,0,0
	for i in range(n):
	 	f1 += (di+ci*ri[i])*(((x-xi[i])**2+(y-yi[i])**2+(z-zi[i])**2 )**0.5)
	for i in range(n):        
	 	f2 += (d +cd*ri[i])*(((x-xs)**2+(y-ys)**2+(z-zs)**2 )**0.5)
	for i in range(n):
	 	f3 += (s +cs*ri[i])*(((xm-xs)**2+(ym-ys)**2+(zm-zs)**2 )**0.5)
	f = f1+f2+f3

	return sign*(f)

def func_deriv(l, sign=1.0):
	""" Derivative of objective function """
	x,y,z,xs,ys=l

	df1dx = 0
	df1dy = 0
	df1dz = 0
	df1dxs = 0
	df1dys = 0
	for i in range(n):
	 	df1dx += (di+ci*ri[i])*(x-xi[i])*(1/ (((x-xi[i])**2+(y-yi[i])**2+(z-zi[i])**2 )**0.5) )
	 	df1dy += (di+ci*ri[i])*(y-yi[i])*(1/ (((x-xi[i])**2+(y-yi[i])**2+(z-zi[i])**2 )**0.5) )
	 	df1dz += (di+ci*ri[i])*(z-zi[i])*(1/ (((x-xi[i])**2+(y-yi[i])**2+(z-zi[i])**2 )**0.5) )

	df2dx = 0
	df2dy = 0
	df2dz = 0
	df2dxs = 0
	df2dys = 0
	for i in range(n):        
	 	df2dx += (d +cd*ri[i])*(x-xs)*(1/ (((x-xs)**2+(y-ys)**2+(z-zs)**2 )**0.5) )
	 	df2dy += (d +cd*ri[i])*(y-ys)*(1/ (((x-xs)**2+(y-ys)**2+(z-zs)**2 )**0.5) )
	 	df2dz += (d +cd*ri[i])*(z-zs)*(1/ (((x-xs)**2+(y-ys)**2+(z-zs)**2 )**0.5) )
		df2dxs += -(d +cd*ri[i])*(x-xs)*(1/ (((x-xs)**2+(y-ys)**2+(z-zs)**2 )**0.5) )
	 	df2dys += -(d +cd*ri[i])*(y-ys)*(1/ (((x-xs)**2+(y-ys)**2+(z-zs)**2 )**0.5) )

	df3dx = 0
	df3dy = 0
	df3dz = 0
	df3dxs = 0
	df3dys = 0
	for i in range(n):
	 	df3dxs += (s +cs*ri[i])*(xm-xs)*(1/ (((xm-xs)**2+(ym-ys)**2+(zm-zs)**2 )**0.5) )
		df3dys += (s +cs*ri[i])*(ym-ys)*(1/ (((xm-xs)**2+(ym-ys)**2+(zm-zs)**2 )**0.5) )

	dfdx = sign*(df1dx + df2dx + df3dx)
	dfdy = sign*(df1dy + df2dy + df3dy)
	dfdz = sign*(df1dz + df2dz + df3dz)
	dfdxs = sign*(df1dxs + df2dxs + df3dxs)
	dfdys = sign*(df1dys + df2dys + df3dys)

	return np.array([ dfdx, dfdy, dfdz, dfdxs, dfdys ])

take_input()

sign = -1.0
temp = ()
for i in range(n):
	temp = temp+({'type': 'ineq',
	         'fun' : lambda x: np.array(
	         	[ sign*abs(x[2]-zi[i])*1.0/(( (x[0]-xi[i])**2+(x[1]-yi[i])**2 )**0.5)-rmaxi]),
	         'jac' : lambda x: np.array([
	         		sign*-abs(x[2]-zi[i])*(x[0]-xi[i])*1.0/(( (x[0]-xi[i])**2+(x[1]-yi[i])**2 )**1.5), 
	          		sign*-abs(x[2]-zi[i])*(x[1]-yi[i])*1.0/(( (x[0]-xi[i])**2+(x[1]-yi[i])**2 )**1.5), 
	          		sign*-(abs(x[2]-zi[i])/(x[2]-zi[i]))*1.0/(( (x[0]-xi[i])**2+(x[1]-yi[i])**2 )**0.5), 
	          		sign*0., 
	          		sign*0.])
	         },)

cons = temp+({
	'type': 'ineq',
    'fun' : lambda x: np.array([sign*abs(x[2]-zs)*1.0/(( (x[0]-x[3])**2+(x[1]-x[4])**2 )**0.5 +1) - rmaxi]),
    'jac' : lambda x: np.array([
     		sign*-abs(x[2]-zs)*(x[0]-x[3])*1.0/(( (x[0]-x[3])**2+(x[1]-x[3])**2 +1)**1.5),
     	 	sign*-abs(x[2]-zs)*(x[1]-x[4])*1.0/(( (x[0]-x[3])**2+(x[1]-x[3])**2 +1)**1.5),
     	 	sign*(abs(x[2]-zs)/(x[2]-zs))*1.0/(( (x[0]-x[3])**2+(x[1]-x[3])**2 +1)**0.5),
     	 	sign*abs(x[2]-zs)*(x[0]-x[3])*1.0/(( (x[0]-x[3])**2+(x[1]-x[3])**2 +1)**1.5),
     	 	sign*abs(x[2]-zs)*(x[1]-x[4])*1.0/(( (x[0]-x[3])**2+(x[1]-x[3])**2 +1)**1.5)
     	 	])
    },
    {'type': 'ineq',
     'fun' : lambda x: np.array([sign*abs(zm-zs)*1.0/(( (xm-x[3])**2+(ym-x[4])**2 )**0.5 ) - bmaxi]),
     'jac' : lambda x: np.array([
     	sign*0.0, 
     	sign*0.0,
     	sign*0.0,
     	sign*abs(zm-zs)*(xm-x[3])*1.0/(( (xm-x[3])**2+(ym-x[3])**2 +1)**1.5),
     	sign*abs(zm-zs)*(ym-x[4])*1.0/(( (xm-x[3])**2+(ym-x[3])**2 +1)**1.5)
     	])
	},
	)

res = minimize(func, x0=[1.,1.,1.,1.,1.], args=(1.0), jac=func_deriv,
               constraints=cons, 
               method='SLSQP',
               options={'disp': True, "maxiter": 1000*10},
			   bounds=[(0,2000),(0,2000),(0,2000),(0,2000),(0,2000)],
			   )

#print res

raw_input()




