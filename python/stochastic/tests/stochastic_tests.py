#! /usr/bin/env python3

from ..stochastic import euc_2d

import math
import unittest

"""
Tests for the base class of Chapter 2: Stochastic Algorithms
"""

class StochasticTests(unittest.TestCase):
	
	def test_euc_2d(self):
		self.assertAlmostEqual(0, euc_2d([0, 0], [0, 0]))
		self.assertAlmostEqual(0, euc_2d([1.1, 1.1], [1.1, 1.1]))
		self.assertAlmostEqual(math.sqrt(2), euc_2d([1, 1], [2, 2]))
		self.assertAlmostEqual(2 * math.sqrt(2), euc_2d([-1, -1], [1, 1]))
