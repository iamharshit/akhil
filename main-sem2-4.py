
import sys
import numpy as np
import random

random.seed(10)

ri=[]
xi,yi,zi=[],[],[]
R = []

def frange(start,stop, step=1.0):
    while start < stop:
        yield start
        start +=step

def optimise_production():
	global n, R, sum_of_all_n
	
	n = input('n(between 1 to 4 only): ')
	if(n<1 or n>4):
		print('----------VALUE OUT OF RANGE-------------')
		input()
		sys.exit(0)		

	mini,maxi = [],[]
	for i in range(n):
		mini.append( input('min '+str(i+1)+': ') )
		maxi.append( input('max '+str(i+1)+': ') )
		print('')
	
	sum_of_all_n = input("Enter sum of all n's:")
	
	temp = 0
	for i in range(n):
		temp += maxi[i]
	if(temp<sum_of_all_n):
		print('---------EVEN SUM OF MAXIMUM VALUE ISNOT EQUAL TO '+sum_of_all_n+'----------')
		input()
		sys.exit(0)

	if(n==1):
		R.append( maxi[0] )


	elif(n==2):
		def belegundu(l):
			x, y = l
			f = -x*random.uniform(0.1, 6) -y*random.uniform(0.1, 6)

			c = x + y - sum_of_all_n
			 
			return [f], [c]		
		from platypus import NSGAII, Problem, Real		

		problem = Problem(2, 1, 1)
		problem.types[:] = [ Real(mini[0], maxi[0]), Real(mini[1], maxi[1]) ]
		problem.constraints[:] = "==0"
		problem.function = belegundu

		algorithm = NSGAII(problem)
		algorithm.run(1000)

		dictt = {}
		for solution in algorithm.result:
	 		dictt[solution.objectives[0]] = solution.variables

	 	R = dictt[ min(dictt.keys())][0]

	elif(n==3):	
		def belegundu(l):
			x, y, z = l
			f = -x*random.uniform(0.1, 6) -y*random.uniform(0.1, 6) -z*random.uniform(0.1, 6)

			c = x + y +z - sum_of_all_n
			 
			return [f], [c]		
		from platypus import NSGAII, Problem, Real		


		problem = Problem(3, 1, 1)
		problem.types[:] = [ Real(mini[0], maxi[0]), Real(mini[1], maxi[1]), Real(mini[2], maxi[2])]
		problem.constraints[:] = "==0"
		problem.function = belegundu

		algorithm = NSGAII(problem)
		algorithm.run(1000)

		dictt = {}
		for solution in algorithm.result:
	 		dictt[solution.objectives[0]] = solution.variables

	 	R = dictt[ min(dictt.keys())][0]


	elif(n==4):
		def belegundu(l):
			x, y, z, q = l
			f = -x*random.uniform(0.1, 6) -y*random.uniform(0.1, 6) -z*random.uniform(0.1, 6) -q*random.uniform(0.1,6)

			c = x + y + z + q - sum_of_all_n
			 
			return [f], [c]		
		from platypus import NSGAII, Problem, Real		

		problem = Problem(4, 1, 1)
		problem.types[:] = [ Real(mini[0], maxi[0]), Real(mini[1], maxi[1]), Real(mini[2], maxi[2]), Real(mini[3], maxi[3])]
		problem.constraints[:] = "==0"
		problem.function = belegundu

		algorithm = NSGAII(problem)
		algorithm.run(1000)

		dictt = {}
		for solution in algorithm.result:
	 		dictt[solution.objectives[0]] = solution.variables

	 	R = dictt[ min(dictt.keys())][0]




def take_input():
    print "============== INPUTS =============="
    global n, di,ci,ri,d,cd,s,cs, xi,yi,zi, xm,ym,zm, gi, rmaxi,bmaxi,zs
    #n =input('n: ')
    di=input('di: ')
    ci=input('ci: ')

    for i in range(n):
    	ri.append(R[i] * input('G['+str(i)+']: ') )
    
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

optimise_production()
take_input()
dic = {}
for rmax__ in frange(0,rmaxi,0.01):
	for bmax__ in frange(0,bmaxi,0.01):
		from platypus import NSGAII, Problem, Real		
		global rmax, bmax
		rmax,bmax = rmax__,bmax__

		problem = Problem(5, 1, n+2)
		problem.types[:] = Real(0, 2000)
		problem.constraints[:] = "<=0"
		problem.function = belegundu

		algorithm = NSGAII(problem)
		algorithm.run(100*100)

		index= np.argmax(algorithm.result)
		
		dic[algorithm.result[index].objectives[0]] = algorithm.result[index].variables

print "============== OUTPUTS =============="
'''
print 'Solution:'
for solution in algorithm.result:
	 print(solution.objectives), solution.variables
'''
print 'Objective functtion value: ',min(dic.keys())
print 'Parameters: ',dic[ min(dic.keys()) ]
print ''

raw_input()


