#! usr/bin/env python3

import random

"""
2.3

Adaptive Random Search was designed to address the limitations
of the fixed step size in the Localized Random Search algorithm.
The strategy for Adaptive Random Search is to continually approximate
the optimal step size required to reach the global optimum in the search
space. This is achieved by trialling and adopting smaller or larger step sizes
only if they result in an improvement in the search performance.

The strategy of Adaptive Random Search is to trial a larger step in each
iteration and adopt the larger step if it results in an improved result. Very
large step sizes are trialled in the same manner although with a much lower
frequency. This strategy of preferring large moves is intended to allow the
technique to escape local optima. Smaller step sizes are adopted if no
improvement is made for an extended period.

The example problem below is similar to the one solved by Random Search [2.2].

@author Chad Estioco
"""

def objective_function(vector):
	"""
	Similar to the one in [2.2]
	"""
	sum = 0
	
	for val in vector:
		sum += val ** 2
	
	return sum

def rand_in_bounds(minimum, maximum):
	return minimum + ((maximum - minimum) * random.random())

def random_vector(minmax):
	"""
	_Essentially_ similar to the one in [2.2]
	"""
	i = 0
	limit = len(minmax)
	random_vector = [0 for i in range(limit)]
	
	for i in range(limit):
		random_vector[i] = rand_in_bounds(minmax[i][0], minmax[i][1])
	
	return random_vector

def take_step(minmax, current, step_size):
	limit = len(current)
	position = [0 for i in range(limit)]
	
	for i in range(limit):
		minimum = max(minmax[i][0], current[i] - step_size)
		maximum = min(minmax[i][1], current[i] + step_size)
		position[i] = rand_in_bounds(minimum, maximum)
	
	return position

def large_step_size(iter_count, step_size, s_factor, l_factor, iter_mult):
	if iter_count > 0 and iter_count % iter_mult == 0:
		return step_size * l_factor
	else:
		return step_size * s_factor

def take_steps(bounds, current, step_size, big_stepsize):
	step, big_step = {}, {}
	step["vector"] = take_step(bounds, current["vector"], step_size)
	step["cost"] = objective_function(step["vector"])
	big_step["vector"] = take_step(bounds, current["vector"], big_stepsize)
	big_step["cost"] = objective_function(big_step["vector"])
	return step, big_step

def search(max_iter, bounds, init_factor, s_factor, l_factor, iter_mult, max_no_impr):
	step_size = (bounds[0][1] - bounds[0][0]) * init_factor
	current, count = {}, 0
	current["vector"] = random_vector(bounds)
	current["cost"] = objective_function(current["vector"])
	
	for i in range(max_iter):
		big_stepsize = large_step_size(i, step_size, s_factor, l_factor, iter_mult)
		step, big_step = take_steps(bounds, current, step_size, big_stepsize)
		
		if step["cost"] <= current["cost"] or big_step["cost"] <= current["cost"]:
			if big_step["cost"] <= step["cost"]:
				step_size, current = big_stepsize, big_step
			else:
				current = step
			
			count = 0
		else:
			count += 1
			
			if count >= max_no_impr:
				count, stepSize = 0, (step_size/s_factor)
		
		print("Iteration " + str(i) + ": best = " + str(current["cost"]))
	
	return current

if __name__ == "__main__":
	# problem configuration
	problem_size = 2
	bounds = [[-5, 5] for i in range(problem_size)]
	
	# algorithm configuration
	max_iter = 1000
	init_factor = 0.05
	s_factor = 1.3
	l_factor = 3.0
	iter_mult = 10
	max_no_impr = 30
	
	# execute the algorithm
	best = search(max_iter, bounds, init_factor, s_factor, l_factor, iter_mult, max_no_impr)
	print("Done. Best Solution: cost = " + str(best["cost"]) + ", v = " + str(best["vector"]))
