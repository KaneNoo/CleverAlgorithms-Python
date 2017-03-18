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
        c2 = permutation[(i + 1) % limit]
        distance += euc_2d(cities[permutation[i]], cities[c2])

    return distance

# Problem configuration
berlin52 = [[565,575],[25,185],[345,750],[945,685],[845,655],
[880,660],[25,230],[525,1000],[580,1175],[650,1130],[1605,620],
[1220,580],[1465,200],[1530,5],[845,680],[725,370],[145,665],
[415,635],[510,875],[560,365],[300,465],[520,585],[480,415],
[835,625],[975,580],[1215,245],[1320,315],[1250,400],[660,180],
[410,250],[420,555],[575,665],[1150,1160],[700,580],[685,595],
[685,610],[770,610],[795,645],[720,635],[760,650],[475,960],
[95,260],[875,920],[700,500],[555,815],[830,485],[1170,65],
[830,610],[605,625],[595,360],[1340,725],[1740,245]]
