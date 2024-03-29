"""
If n is the numerator and d the denominator of a fraction, that fraction is defined a (reduced) proper fraction if and only if GCD(n,d)==1.

For example 5/16 is a proper fraction, while 6/16 is not, as both 6 and 16 are divisible by 2, thus the fraction can be reduced to 3/8.

Now, if you consider a given number d, how many proper fractions can be built using d as a denominator?

For example, let's assume that d is 15: you can build a total of 8 different proper fractions between 0 and 1 with it: 1/15, 2/15, 4/15, 7/15, 8/15, 11/15, 13/15 and 14/15.

You are to build a function that computes how many proper fractions you can build with a given denominator:

proper_fractions(1)==0
proper_fractions(2)==1
proper_fractions(5)==4
proper_fractions(15)==8
proper_fractions(25)==20

Be ready to handle big numbers.
"""

from nose.tools import assert_equals

# from fractions import Fraction

# def proper_fractions(n):
#     def gcd(a, b):  
#         if a == 0: 
#             return b  
        
#         return gcd(b%a, a) 
 
#     count = 0

#     for i in range(1,n):
#         if gcd(i,n) == 1: 
#             count += 1
    
#     return count

import math
import fractions

def proper_fractions(n):

    def isprime(n):
        if n & 1 == 0:
            return 2
        d= 3
        while d * d <= n:
            if n % d == 0:
                return d
            d= d + 2
        return 0

    if n == 1:
        return 0

    if n == 2:
        return 1

    if isprime(n):
        return n-1

    amount = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1
    return amount

proper_fractions(15)

def test_1():
    assert_equals(proper_fractions(1), 0)

def test_2():
    assert_equals(proper_fractions(2), 1)

def test_3():
    assert_equals(proper_fractions(3), 2)

def test_5():
    assert_equals(proper_fractions(5), 4)

def test_15():
    assert_equals(proper_fractions(15), 8)

def test_25():
    assert_equals(proper_fractions(25), 20)

