#! /usr/bin/env python3

from .common import euc_2d

"""
2.7

Variable Local Search involves iterative exploration of larger and larger
neighborhoods for a given local optima until an improvement is located after
which time the search across expanding neighborhoods is repeated. The strategy
is motivated by three principles: 1) a local minimum for one neighborhood
structure may not be a local minimum for another neighborhood structure, 2) a
global minimum is local minimum for all possible neighborhood structures, and
3) local minima are relatively close to global minima for many problem classes.
"""
