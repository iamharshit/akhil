
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
	
	n = input('Number of Ore Bodies: ')
	if(n<1 or n>4):
		print('----------VALUE OUT OF RANGE-------------')
		input()
		sys.exit(0)		

	print("-----------Range for Productivity of Various Ore Bodies---------")
	mini,maxi = [],[]
	for i in range(n):
		mini.append( input('Minimum '+str(i+1)+': ') )
		maxi.append( input('Maximum '+str(i+1)+': ') )
		print('')
	
	print("-----------Range for Grades of Various Ore Bodies---------")
	xmini,xmaxi = [],[]
	for i in range(n):
		xmini.append( input('Minimum '+str(i+1)+': ') )
		xmaxi.append( input('Maximum '+str(i+1)+': ') )
		print('')

	sum_of_all_n = input("Total amount of Output to be produced per year: ")
	cutt_off_grade = input('Cutt Off Grade: ')
	
	temp = 0
	for i in range(n):
		temp += maxi[i]
	if(temp<sum_of_all_n):
		print('---------EVEN SUM OF MAXIMUM VALUE IS NOT EQUAL TO '+sum_of_all_n+'----------')
		input()
		sys.exit(0)

	if(n==1):
		R.append( maxi[0] )


	elif(n==2):
		def belegundu(l):
			x, y, a, b = l
			f = -x*a -y*b

			c1 = x + y - sum_of_all_n
			c2 = (x*a + y*b)/2 - cutt_off_grade
			return [f], [c1 , c2]		
		from platypus import NSGAII, Problem, Real		

		problem = Problem(4, 1, 2)
		problem.types[:] = [ Real(mini[0], maxi[0]), Real(mini[1], maxi[1]), Real(xmini[0], xmaxi[0]), Real(xmini[1], xmaxi[1]) ]
		problem.constraints[:] = "==0"
		problem.function = belegundu

		algorithm = NSGAII(problem)
		algorithm.run(1000)

		dictt = {}
		for solution in algorithm.result:
	 		dictt[solution.objectives[0]] = solution.variables
	 	
	 	R = dictt[ min(dictt.keys()) ] [:2]

	elif(n==3):	
		def belegundu(l):
			x, y, z, p, q, r = l
			f = -x*p -y*q -z*r

			c1 = x + y +z - sum_of_all_n
			c2 = (x*p + y*q + z*r)/3 - cutt_off_grade
			return [f], [c1,c2]			
		from platypus import NSGAII, Problem, Real		


		problem = Problem(6, 1, 2)
		problem.types[:] = [ Real(mini[0], maxi[0]), Real(mini[1], maxi[1]), Real(mini[2], maxi[2]),     Real(xmini[0], xmaxi[0]), Real(xmini[1], xmaxi[1]), Real(xmini[2], xmaxi[2])]
		problem.constraints[:] = "==0"
		problem.function = belegundu

		algorithm = NSGAII(problem)
		algorithm.run(1000)

		dictt = {}
		for solution in algorithm.result:
	 		dictt[solution.objectives[0]] = solution.variables

	 	R = dictt[ min(dictt.keys())] [:3]


	elif(n==4):
		def belegundu(l):
			x,y,z,q, e,f,g,h = l
			f = -x*e -y*f -z*g -q*h

			c1 = x + y + z + q - sum_of_all_n
			c2 = (x*e + y*f + z*g + q*h)/4 - cutt_off_grade

			return [f], [c1,c2]		
		from platypus import NSGAII, Problem, Real		

		problem = Problem(8, 1, 2)
		problem.types[:] = [ Real(mini[0], maxi[0]), Real(mini[1], maxi[1]), Real(mini[2], maxi[2]), Real(mini[3], maxi[3]),        Real(xmini[0],xmaxi[0]), Real(xmini[1],xmaxi[1]), Real(xmini[2],xmaxi[2]), Real(xmini[3],xmaxi[3])]
		problem.constraints[:] = "==0"
		problem.function = belegundu

		algorithm = NSGAII(problem)
		algorithm.run(1000)

		dictt = {}
		for solution in algorithm.result:
	 		dictt[solution.objectives[0]] = solution.variables

	 	R = dictt[ min(dictt.keys())] [:4]




def take_input():
    print "============== INPUTS =============="
    global n, di,ci,ri,d,cd,s,cs, xi,yi,zi, xm,ym,zm, gi, rmaxi,bmaxi,zs, R
    #n =input('Number of Ore Bodies,n: ')
    di=input('Unit Cost of Decline Development from UMCP to Ore body [USD/m],di: ')
    ci=input('Unit Ore haulage cost from ore body to UMCP [USD/tm],ci: ')

    for i in range(n):
    	ri.append(R[i])

    d=input('Unit cost of Decline Development from UMCP to SBP[USD/m],d: ')
    cd=input('Unit core haulage cost from UMCP to SBP[USD/tm],cd: ')
    s=input('Unit cost of surface route development from SBP to MPF[USD/m],s: ')
    cs=input('Unit ore transportation cost from SBP to MPF[USD/tm],cs: ')
    for i in range(n):
        xi.append(input('x['+str(i)+']: ') )
        yi.append(input('y['+str(i)+']: ') )
        zi.append(input('z['+str(i)+']: ') )

    xm=input('Mineral Processing Facility,xm: ')
    ym=input('Mineral Processing Facility,ym: ')
    zm=input('Mineral Processing Facility,zm: ')

    rmaxi=input('Maximum absolute value of decline slope, rmax: ')
    bmaxi=input('Maximum absolute value of the slope of surface transportation section, bmax: ')
    
    zs =input('Z coordinate of suface breakout point,zs: ')


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


