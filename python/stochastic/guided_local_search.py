#! usr/bin/env python3

from .common import euc_2d

import math
import random

"""
2.6

Guided Local Search uses penalties to encourage a Local Search
technique to escape local optima and discover the global optima.
A Local Search algorithm is run until it gets stuck in a local
optima. The features from the local optima are evaluated and
penalized, the results of which are used in an augmented cost
function employed by the Local Search procedure. The Local Search
is repeated a number of times using the last local optima discovered
and the augmented cost function that guides exploration away from
solutions with featured present in the discovered local optima.

This implementation applies Guided Local Search to the Berlin52
instance of TSP from TSPLIB.
"""

def random_permutation(cities):
    """
    Same as the one in 2.5
    """
    perm = [i for i in range(len(cities))]
    
    for i in perm:
        r = random.randint(0, len(perm) - 1 - i) + i
        perm[r], perm[i] = perm[i], perm[r]
    
    return perm

def stochastic_two_opt(permutation):
    """
    Same as the one in 2.5
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

def augmented_cost(permutation, penalties, cities, l):
    distance, augmented = 0, 0
    limit = len(permutation)
    
    for i in range(limit):
        c1 = permutation[i]
        
        if i == (limit - 1):
            c2 = permutation[0]
        else:
            c2 = permutation[i + 1]
        
        if c2 < c1:
            c1, c2 = c2, c1
        
        d = euc_2d(cities[c1], cities[c2])
        distance += d
        augmented += d + (l * penalties[c1][c2])
    
    return [distance, augmented]

def cost(cand, penalties, cities, l):
    cost, acost = augmented_cost(cand["vector"], penalties, cities, l)
    cand["cost"], cand["aug_cost"] = cost, acost

def local_search(current, cities, penalties, max_no_improv, l):
    cost(current, penalties, cities, l)
    count  = 0
    
    # begin-until hack
    while True:
        candidate = {}
        candidate["vector"] = stochastic_two_opt(current["vector"])
        cost(candidate, penalties, cities, l)
        
        if candidate["aug_cost"] < current["aug_cost"]:
            count = 0
        else:
            count += 1
        
        if candidate["aug_cost"] < current["aug_cost"]:
            current = candidate
        
        if count >= max_no_improv:
            return current

def calculate_feature_utilities(penalties, cities, permutation):
    """
    For every edge in the path, compute its utility, defined as the cost of the
    edge / (1 + existing penalty for edge).

    Note: The utility is defined per origin node of every edge.
    """
    limit = len(permutation)
    limit_list = range(limit)
    utilities = [0 for i in limit_list]
    
    for i in limit_list:
        c1 = permutation[i]
        
        if i == (limit - 1):
            c2 = permutation[0]
        else:
            c2 = permutation[i + 1]
        
        if c2 < c1:
            c1, c2 = c2, c1
        
        utilities[i] = euc_2d(cities[c1], cities[c2]) / (1 + penalties[c1][c2])
    
    return utilities

def update_penalties(penalties, cities, permutation, utilities):
    """
    Penalize an edge if the utility for its origin is the greatest utility value
    in this round.
    """
    max_util = max(utilities)
    limit = len(permutation)
    
    for i in range(limit):
        c1 = permutation[i]
        
        if i == (limit - 1):
            c2 = permutation[0]
        else:
            c2 = permutation[i + 1]
        
        if c2 < c1:
            c1, c2 = c2, c1
        
        if utilities[i] == max_util:
            penalties[c1][c2] += 1
    
    return penalties

def search(max_iterations, cities, max_no_improv, l):
    current = {}
    current["vector"] = random_permutation(cities)
    best = None
    cities_count_list = range(len(cities))
    penalties = [[0 for i in cities_count_list] for j in cities_count_list]
    
    for i in range(max_iterations):
        current = local_search(current, cities, penalties, max_no_improv, l)
        utilities = calculate_feature_utilities(penalties, cities, current["vector"])
        update_penalties(penalties, cities, current["vector"], utilities)
        
        if best is None or current["cost"] < best["cost"]:
            best = current
        
        print("Iteration #" + str(i + 1) + ", best = " + str(best["cost"]) + ", aug = " + str(best["aug_cost"]))
    
    return best

if __name__ == "__main__":
    from .common import berlin52
    
    max_iterations = 150
    max_no_improv = 20
    alpha = 0.3
    local_search_optima = 12000
    l = alpha * (local_search_optima / len(berlin52))
    
    # Execute the algorithm
    best = search(max_iterations, berlin52, max_no_improv, l)
    print("Done. Best solution: c = " + str(best["cost"]) + ", v = " + str(best["vector"]))
