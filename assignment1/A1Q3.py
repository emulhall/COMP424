import math
import numpy as np
import random
#function: Y=sin(X^2/2)/log(X+4), in the range X=[0,10]

def evaluate(x):
	return math.sin(((math.pow(x, 2))/2))/math.log(x + 4)

def hill_climbing(initial_x, initial_value, step_size, steps):
	neighbors=[(initial_x-step_size, evaluate(initial_x-step_size)) , (initial_x+step_size, evaluate(initial_x+step_size))]
	emax=initial_value
	index=initial_x
	for element in neighbors:
		if element[1]>emax:
			emax=element[1]
			index=element[0]
		else:
			continue
	if emax<=initial_value:
		return str((initial_x, initial_value)) + ' & ' + str(steps)
	else:
		return hill_climbing(index, emax, step_size, steps+1)

def test_hillclimbing(starting_points, step_sizes):
	results=[]
	for n in starting_points:
		for s in step_sizes:
			results.append(str(n) + ' & ' +  str(s) + '&' + hill_climbing(n, evaluate(n), s, 1) + '\\' + '\\' + '\hline')
	return results

def simulated_annealing(x, e, imax, emax, step_size, steps, temperature, annealing):
	neighbors=[(x-step_size, evaluate(x-step_size)) , (x+step_size, evaluate(x+step_size))]
	#choose a random neighbor
	chosen=random.randint(0, 1)
	xi=neighbors[chosen][0]
	ei=neighbors[chosen][1]
	if temperature<0.0001:
		return str((imax, emax)) + ' & ' + str(steps)
	else:
		if ei>emax:
			imax=xi
			emax=ei
		if ei>e:
			e=ei
			x=xi
		else:
			p=math.pow(math.e, -(e-ei)/temperature)
			if p>random.uniform(0, 1):
				e=ei
				x=xi
		return simulated_annealing(x, e, emax, imax, step_size, steps+1, temperature*annealing, annealing)

def test_simulated_annealing(starting_points, step_sizes, temperatures, annealing_constants):
	results=[]
	for point in starting_points:
		for size in step_sizes:
			for temp in temperatures:
				for constant in annealing_constants:
					results.append(str(point) + ' & ' + str(size) + ' & ' + str(temp) + ' & ' + str(constant) + ' & ' + simulated_annealing(point, evaluate(point), point, evaluate(point), size, 1, temp, constant) + '\\' + '\\' + '\hline')
	return results

#uncomment below to test
'''results=test_simulated_annealing(range(0, 11), [0.01, 0.02, 0.03], [1e5, 1e10, 1e15, 1e20], [0.01, 0.05, 0.1, 0.5, 0.9])
for element in results:
	print element'''
'''results=test_hillclimbing(range(0, 11), np.arange(0.01, 0.11, 0.01))
for item in results:
	print item'''