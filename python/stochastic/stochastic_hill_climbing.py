#! usr/bin/env python3

import random

"""
2.4

Stochastic Hill Climbing iterates the process of randomly
selecting a neighbor for a candidate solution and only accept
it if it results in an improvement. The strategy was proposed to
address the limitations of deterministic hill climbing techniques
that were likely to get stuck in local optima due to their greedy
acceptance of neighboring moves.

This code implements the Random Mutation Hill Climbing algorithm,
a specific instance of Stochastic Hill Climbing. It is applied to
a binary string optimization problem called "One Max": prepare a
string of all '1' bits where the cost function only reports the
number of bits in a given string.

Implementation notes:
The reference implementation uses a list of (one-character) strings.
I opted to use a String object directly.

@author Chad Estioco
"""

def onemax(vector):
	limit = len(vector)
	one_count = 0
	
	for i in range(limit):
		if vector[i] == "1":
			one_count += 1
	
	return one_count

def random_bitstring(num_bits):
	def generator():
		bit = None
		
		if random.random() < 0.5:
			bit = "1"
		else:
			bit = "0"
		
		return bit
	
	return "".join(generator() for i in range(num_bits))

def random_neighbor(bitstring):
	mutant = bitstring
	limit = len(bitstring)
	pos = random.randint(0, limit - 1)
	
	if mutant[pos] == "1":
		mutant = "".join((mutant[0:pos], "0" ,mutant[pos + 1:limit]))
	else:
		mutant = "".join((mutant[0:pos], "1" ,mutant[pos + 1:limit]))
	
	return mutant

def search(max_iterations, num_bits):
	candidate = {}
	candidate["vector"] = random_bitstring(num_bits)
	candidate["cost"] = onemax(candidate["vector"])
	
	for i in range(max_iterations):
		neighbor = {}
		neighbor["vector"] = random_neighbor(candidate["vector"])
		neighbor["cost"] = onemax(neighbor["vector"])
		
		if neighbor["cost"] >= candidate["cost"]:
			candidate = neighbor
		
		print("Iteration " + str(i) + ": best = " + str(candidate["cost"]))
		
		if candidate["cost"] == num_bits:
			break
	
	return candidate

if __name__ == "__main__":
	# problem configuration
	num_bits = 64
	
	# algorithm configuration
	max_iterations = 1000
	
	# execute the algoirthm
	best = search(max_iterations, num_bits)
	print("Done. Best Solution: cost = " + str(best["cost"]) + ", v = " + str(best["vector"]))
