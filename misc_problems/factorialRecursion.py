# Factorial using recursion

"""
    Three Laws of Recursion
    ------------------------
    A recursive algorithm must have a base case.
    A recursive algorithm must change its state and move toward the base case.
    A recursive algorithm must call itself, recursively
"""     

import unittest

def factorial(n):
	"""
        Calculate factorial of number. 

        Gamma(n) = (n-1)! for any positive integer n

        It can be also calulated as n! = (n+1)!/n i.e. 0! = 1! / 1 = 1
        
        4! = 4 x 3 x 2 x 1 = 24
        
        Factorial function can be generalized to the Gamma function. 
        The Gamma function can also be extended to complex numbers by replacing the real number x in the definition by a complex number z. 
        Gamma function is undefined for nonpositive integers, so factorial of a nonpositive integer can`t be calculated.
        
        INPUT
        -----------
        n : 3 (positive integer)
        
        RETURN
        -----------
        OUTPUT : 6 (3 * 2 * 1)

	"""

	if n <= 1:
		return 1
	else:
		return n * factorial(n-1)

class FactorialTest(unittest.TestCase):
    def testFactorial(self):
        self.assertEqual(factorial(4),24)
        self.assertEqual(factorial(0),1)
        self.assertEqual(factorial(1),1)

if __name__ == "__main__":
    unittest.main()
