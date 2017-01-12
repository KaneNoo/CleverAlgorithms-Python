#! usr/bin/env python3

from .common import euc_2d

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

def cost(permutation, cities):
    distance = 0
    limit = len(permutation)
    
    for i in range(limit):
        if i == (limit - 1):
            c2 = permutation[0]
        else:
            c2 = permutation[i + 1]
        
        distance += euc_2d(cities[permutation[i]], cities[c2])
    
    return distance

def random_permutation(cities):
    perm = [i for i in range(len(cities))]
    
    for i in perm:
        r = random.randint(0, len(perm) - 1 - i) + i
        perm[r], perm[i] = perm[i], perm[r]
    
    return perm

def stochastic_two_opt(permutation):
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
        candidate["cost"] = cost(candidate["vector"], cities)
        
        if candidate["cost"] < best["cost"]:
            count = 0
        else:
            count += 1
        
        if candidate["cost"] < best["cost"]:
            best = candidate
    
    return best

def double_bridge_move(perm):    
    pos1 = 1 + random.randint(0, math.floor(len(perm) / 4))
    pos2 = pos1 + 1 + random.randint(0, math.floor(len(perm) / 4))
    pos3 = pos2 + 1 + random.randint(0, math.floor(len(perm) / 4))
    p1 = perm[0:pos1] + perm[pos3:len(perm)]
    p2 = perm[pos2:pos3] + perm[pos1:pos2]
    return p1 + p2

def perturbation(cities, best):
    candidate = {}
    candidate["vector"] = double_bridge_move(best["vector"])
    candidate["cost"] = cost(candidate["vector"], cities)
    return candidate

def search(cities, max_iterations, max_no_improv):
    best = {}
    best["vector"] = random_permutation(cities)
    best["cost"] = cost(best["vector"], cities)
    best = local_search(best, cities, max_no_improv)
    
    for i in range(max_iterations):    
        candidate = perturbation(cities, best)
        candidate = local_search(candidate, cities, max_no_improv)
        
        if candidate["cost"] < best["cost"]:
            best = candidate
        
        print("Iteration #" + str(i) + " best = " + str(best["cost"]))
    
    return best

if __name__ == "__main__":
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
    
    # Algorithm configuration
    max_iterations = 100
    max_no_improv = 50
    
    # Execute the algorithm
    best = search(berlin52, max_iterations, max_no_improv)
    print("Done. Best solution: c = " + str(best["cost"]) +", v = " + str(best["vector"]))
