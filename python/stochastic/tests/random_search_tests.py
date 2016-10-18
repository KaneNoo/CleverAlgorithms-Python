#! usr/bin/env python3

from ..random_search import objective_function, random_vector

import unittest

class RandomSearchTests(unittest.TestCase):
    """
    Unit tests for functions in random_search.py .
    """
    
    def test_objective_function(self):
        #integer
        self.assertEqual(99**2, objective_function([99]))
        #float
        self.assertEqual(0.1**2.0, objective_function([0.1]))
        #vector
        self.assertEqual((1**2) + (2**2) + (3**2), objective_function([1,2,3]))
    
    def test_random_vector(self):
        bounds, trials, size = [-3, 3], 300, 20
        minmax = [bounds for i in range(size)]
        
        for i in range(trials):
            vector, total = random_vector(minmax), 0.0
            self.assertEqual(size, len(vector))
            
            for v in vector:
                self.assertTrue(v >= bounds[0])
                self.assertTrue(v < bounds[1])
                total += v
            
            #TODO: test with total
