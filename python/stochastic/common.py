#! /usr/bin/env python3

import math
import random

"""
Not in the original code listing. This factors out the common functions
used in Chapter 2.
"""

def euc_2d(p1, p2):
	dx = p1[0] - p2[0]
	dy = p1[1] - p2[1]
	return math.sqrt((dx ** 2) + (dy ** 2))

def random_permutation(cities):
    """
    Given a list of cities, return a random permutation _of the indices_.
    """
    indices = [idx for idx, val in enumerate(cities)]
    for i in indices:
        # Guaranteed not to choose i as well
        r = random.randint(0, len(cities) - 1 - i) + i
        indices[r], indices[i] = indices[i], indices[r]

    return indices

def path_cost(permutation, cities):
    """
    Given a permutation of indices and the actual location of the cities,
    the total cost (assessed as Euclidean distance) of traversing the path
    described by the permutation.
    """
    distance = 0
    limit = len(permutation)

    for i in range(limit):
        if i == (limit - 1):
            c2 = 0
        else:
            c2 = i + 1
        distance += euc_2d(cities[permutation[i]], cities[c2])

    return distance
