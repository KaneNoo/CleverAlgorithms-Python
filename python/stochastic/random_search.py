#! usr/bin/env python3

import random

"""
2.2

Random Search samples solutions from across the entire search space
using a uniform probability distribution. Each future sample is
independent of the samples that come before it.

The example problem (solved by the code below) is an instance of a
continuous function optimization that seeks min f(x) where
f = \sum_{i=1}^{n} x_i^2, -5 <= x_i <= 5 and n = 2.

@author Chad Estioco
"""

def objective_function(vector):
	sum = 0
	
	for val in vector:
		sum += val ** 2
	
	return sum

def random_vector(minmax):
	i = 0
	limit = len(minmax)
	random_vector = [0 for i in range(limit)]
	
	for i in range(limit):
		spam = minmax[i][0]
		random_vector[i] = spam + ((minmax[i][1] - spam) * random.random())
	
	return random_vector

def search(search_space, max_iter):
	best = None
	
	for i in range(max_iter):
		candidate = {}
		candidate['vector'] = random_vector(search_space)
		candidate['cost'] = objective_function(candidate['vector'])
		
		if best is None or candidate['cost'] < best['cost']:
			best = candidate
		
		print("Iteration " + str(i) + ": best = " + str(best['cost']))
	
	return best

if __name__ == "__main__":
	# problem configuration
	problem_size = 2
	search_space = [[-5, 5] for i in range(problem_size)]
	
	# algorithm configuration
	max_iter = 100
	
	# execute the algorithm
	best = search(search_space ,max_iter)
	print("Done. Best Solution: cost = " + str(best['cost']) + ", v = " + str(best['vector']))
