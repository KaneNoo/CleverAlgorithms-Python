#! /usr/bin/env python3

import stochastic
import unittest

"""
Tests for the base class of Chapter 2: Stochastic Algorithms
"""

class StochasticTests(unittest.TestCase):
	
	def test_euc_2d(self):
		self.assertEqual(0, stochastic.euc_2d([0, 0], [0, 0]))
		self.assertEqual(0, stochastic.euc_2d([1.1, 1.1], [1.1, 1.1]))
		self.assertEqual(1, stochastic.euc_2d([1, 1], [2, 2]))
		self.assertEqual(3, stochastic.euc_2d([-1, -1], [1, 1]))

if __name__ == "__main__":
	unittest.main()
