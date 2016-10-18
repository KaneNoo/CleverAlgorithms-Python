#! usr/bin/env python3

import re

import stochastic_hill_climbing as shc

import unittest

class StochasticHillClimbingTests(unittest.TestCase):
	"""
	Unit tests for functions in stochastic_hill_climbing.py .
	Has some additional tests compared to Ruby version.
	
	@author Chad Estioco
	"""
	
	def test_onemax(self):
		self.assertEqual(4, shc.onemax("1111"))
		self.assertEqual(2, shc.onemax("0101"))
		self.assertEqual(0, shc.onemax("0000"))
	
	def test_random_bitstring(self):
		"""
		Tests the string generated as well as it's size.
		"""
		
		bit10 = re.compile("[01]{10}")
		
		for i in range(100):
			self.assertTrue(bit10.match(shc.random_bitstring(10)))
		
		bit8 = re.compile("[01]{8}")
		
		for i in range(100):
			self.assertTrue(bit8.match(shc.random_bitstring(8)))
	
	# TODO: test_random_bitstring_ratio
	
	def test_random_neighbor(self):
		parent = "00000000"
		
		for i in range(100):
			random_neighbor = shc.random_neighbor(parent)
			self.assertEqual(len(random_neighbor), len(parent))
			self.assertNotEqual(random_neighbor, parent)
			self.assertFalse(random_neighbor is parent)
			
			diffs = 0
			
			for i in range(len(random_neighbor)):
				if parent[i] != random_neighbor[i]:
					diffs += 1
			
			self.assertEqual(1, diffs)
	
if __name__ == "__main__":
	tests = unittest.TestLoader().loadTestsFromTestCase(StochasticHillClimbingTests)
	unittest.TextTestRunner(verbosity=2).run(tests)
