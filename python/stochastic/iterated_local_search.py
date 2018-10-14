#! usr/bin/env python3

from .common import path_cost, random_permutation
from ..switch import decide

import math
import random

"""
2.5

Iterated Local Search improves upon Multi-Restart Search by
sampling in the broader neighborhood of candidate solutions
and using a Local Search technique to refine solutions to
their local optima. Iterated Local Search explores a sequence
of solutions created as perturbations of the current best
solution, the result of which is refined using an embedded
heuristic.

The code listing applies the algorithm to the Berlin52 instance
of the Traveling Salesman Problem, taken from TSPLIB. The problem seeks a
permutation of the order to visit cities (called a tour) that minimizes the
total distance traveled. The optimal tour distance for the Berlin52 instance is
7542 units.
"""

def stochastic_two_opt(permutation):
    """
    Looks for a random subsequence in the permutation and reverses them.

    See also: https://en.wikipedia.org/wiki/2-opt
    """
    perm = [permutation[i] for i in range(len(permutation))]
    upper_bound = len(perm) - 1
    c1, c2 = random.randint(0, upper_bound), random.randint(0, upper_bound)
    exclude = [c1]
    
    if c1 == 0:
        exclude.append(upper_bound)
    else:
        exclude.append(c1 - 1)
    
    if c1 == upper_bound:
        exclude.append(0)
    else:
        exclude.append(c1 + 1)
    
    while c2 in exclude:
        c2 = random.randint(0, upper_bound)
    
    if c2 < c1:
        c1, c2 = c2, c1
    
    perm_range = perm[c1:c2]
    perm_range.reverse()
    perm[c1:c2] = perm_range
    
    return perm

#FIXME modifying and returning an argument?
def local_search(best, cities, max_no_improv):
    count = 0
    
    while count < max_no_improv:
        candidate = {}
        candidate["vector"] = stochastic_two_opt(best["vector"])
        candidate["cost"] = path_cost(candidate["vector"], cities)
        
        if candidate["cost"] < best["cost"]:
            count = 0
        else:
            count += 1
        
        if candidate["cost"] < best["cost"]:
            best = candidate
    
    return best

def double_bridge_move(perm):
    """
    Partitions the permutation into 4 subsequences and then shuffles those
    subsequences to create a new permutation.
    """
    pos1 = 1 + random.randint(0, math.floor(len(perm) / 4))
    pos2 = pos1 + 1 + random.randint(0, math.floor(len(perm) / 4))
    pos3 = pos2 + 1 + random.randint(0, math.floor(len(perm) / 4))
    p1 = perm[0:pos1] + perm[pos3:len(perm)]
    p2 = perm[pos2:pos3] + perm[pos1:pos2]
    return p1 + p2

def perturbation(cities, best):
    candidate = {}
    candidate["vector"] = double_bridge_move(best["vector"])
    candidate["cost"] = path_cost(candidate["vector"], cities)
    return candidate

def search(cities, max_iterations, max_no_improv, output_format="human"):
    best = {}
    best["vector"] = random_permutation(cities)
    best["cost"] = path_cost(best["vector"], cities)
    best = local_search(best, cities, max_no_improv)
    
    for i in range(max_iterations):    
        candidate = perturbation(cities, best)
        candidate = local_search(candidate, cities, max_no_improv)
        
        if candidate["cost"] < best["cost"]:
            best = candidate
        
        if output_format == "csv":
            print("%s,%s" % (i, best["cost"]))
        else:
            print("Iteration #" + str(i) + " best = " + str(best["cost"]))
    
    return best

if __name__ == "__main__":
    from .common import berlin52
    
    # Algorithm configuration
    max_iterations = 100
    max_no_improv = 50
    output_format = decide()
    
    # Execute the algorithm
    best = search(berlin52, max_iterations, max_no_improv, output_format)

    if output_format == "csv":
        print("%s,%s" % (best["cost"], ",".join([str(i) for i in best["vector"]])))
    else:
        print("Done. Best solution: c = " + str(best["cost"]) +", v = " + str(best["vector"]))
