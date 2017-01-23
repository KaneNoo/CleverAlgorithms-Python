#! /usr/bin/env python3

from .common import cost, random_permutation

import random

"""
2.7

Variable Neighborhood Search involves iterative exploration of larger and larger
neighborhoods for a given local optima until an improvement is located after
which time the search across expanding neighborhoods is repeated. The strategy
is motivated by three principles: 1) a local minimum for one neighborhood
structure may not be a local minimum for another neighborhood structure, 2) a
global minimum is local minimum for all possible neighborhood structures, and
3) local minima are relatively close to global minima for many problem classes.
"""

def stochastic_two_opt(perm):
    randlimit = len(perm) - 1
    c1, c2 = random.randint(0, randlimit), random.randint(0, randlimit)
    exclude = [c1]
    exclude.append(randlimit if c1 == 0 else c1 -1)
    exclude.append(0 if c1 == randlimit else c1 + 1)

    while c2 in exclude:
        c2 = random.randint(0, randlimit)

    c1, c2 = c2, c1 if c2 < c1 else None
    perm[c1:c2] = perm[c1:c2][::-1]
    return perm

def local_search(best, cities, max_no_improv, neighborhood_size):
    count = 0

    while count < max_no_improv:
        candidate = {}
        candidate["vector"] = [v for v in best["vector"]]

        for _ in range(neighborhood_size):
            stochastic_two_opt(candidate["vector"])

        candidate["cost"] = cost(candidate["vector"], cities)

        if candidate["cost"] < best["cost"]:
            count, best = 0, candidate
        else:
            count += 1

    return best

def search(cities, neigborhoods, max_no_improv, max_no_improv_ls):
    best = {}
    best["vector"] = random_permutation(cities)
    best["cost"] = cost(best["vector"], cities)
    iter_, count = 0, 0

    while count < max_no_improv:
        for neigh in negihborhoods:
            candidate = {}
            candidate["vector"] = [v for v in best["vector"]]

            for _ in range(neigh):
                stochastic_two_opt(candidate["vector"])

            candidate["cost"] - cost(candidate["vector"], cities)
            candidate = local_search(candidate, cities, max_no_improv_ls, neigh)
            print("> iteration #%s, neigh=%s, best=%s" % (iter_ + 1, neigh, best["cost"]))
            iter_ += 1

            if candidate["cost"] < best["cost"]:
                best, count = candidate, 0
                print("New best, restarting neighborhood search")
