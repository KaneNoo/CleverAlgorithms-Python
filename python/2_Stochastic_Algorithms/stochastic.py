#! /usr/bin/env python3

import math

"""
Not in the original code listing. This factors out the common functions
used in Chapter 2.
"""

def euc_2d(p1, p2):
	dx = p1[0] - p2[0]
	dy = p1[1] - p2[1]
	return math.sqrt((dx ** 2) + (dy ** 2))
