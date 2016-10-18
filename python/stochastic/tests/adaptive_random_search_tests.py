#! usr/bin/env python3

from ..adaptive_random_search import (
    objective_function, rand_in_bounds, random_vector, take_step,
    large_step_size, take_steps
)

import unittest

class AdaptiveRandomSearchTests(unittest.TestCase):
	
	def test_objective_function(self):
		#integer
		self.assertEqual(99**2, objective_function([99]))
		#float
		self.assertEqual(0.1**2.0, objective_function([0.1]))
		#vector
		self.assertEqual((1**2) + (2**2) + (3**2), objective_function([1,2,3]))
	
	def test_rand_in_bounds(self):
		x = rand_in_bounds(0, 20)
		self.assertTrue(x >= 0)
		self.assertTrue(x < 20)
		
		x = rand_in_bounds(-20, -1)
		self.assertTrue(x >= -20)
		self.assertTrue(x < -1)
		
		x = rand_in_bounds(-10, 20)
		self.assertTrue(x >= -10)
		self.assertTrue(x < 20)
	
	def test_random_vector(self):
		bounds, trials, size = [-3, 3], 300, 20
		minmax = [bounds for i in range(size)]
		
		for i in range(trials):
			vector, total = random_vector(minmax), 0.0
			self.assertEqual(size, len(vector))
			
			for v in vector:
				self.assertTrue(v >= bounds[0])
				self.assertTrue(v < bounds[1])
				total += v
			
			#TODO: test with total
	
	def test_take_step(self):
		p = take_step([[0, 100]], [50], 3.3)
		self.assertTrue(p[0] >= 50 - 3.3)
		self.assertTrue(p[0] <= 50 + 3.3)
		
		p = take_step([[0, 1]], [0], 3.3)
		self.assertTrue(p[0] >= 0)
		self.assertTrue(p[0] < 1)
	
	def test_large_step_size(self):
		# Test using small factor
		s = large_step_size(0, 1, 2, 3, 100)
		self.assertEqual(1*2, s)
		
		# Test using large factor
		s = large_step_size(100, 1, 2, 3, 100)
		self.assertEqual(1*3, s)
	
	def test_take_steps(self):
		vector_content = 5
		for i in range(20):
			step1, step2 = take_steps([[0,10]], {"vector":[vector_content]}, 1, 3)
			self.assertTrue(step1["vector"] is not None)
			self.assertTrue(step1["cost"] is not None)
			self.assertTrue(step1["vector"][0] >= vector_content - 1)
			self.assertTrue(step1["vector"][0] < vector_content + 1)
			
			self.assertTrue(step2["vector"] is not None)
			self.assertTrue(step2["cost"] is not None)
			self.assertTrue(step2["vector"][0] >= vector_content - 3)
			self.assertTrue(step2["vector"][0] < vector_content + 3)
	
	#TODO : Test search
