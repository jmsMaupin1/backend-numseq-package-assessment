import unittest
from numseq.fib import nth_fib
from numseq.geo import square, triangle, cube
from numseq.prime import primes, is_prime

class TestNumseq(unittest.TestCase):


    def test_fib(self):
        """Should return the correct nth fibonacci number"""
        actual = {}
        expected = {
            0: 0,
            1: 1,
            2: 1,
            3: 2,
            4: 3,
            5: 5,
            6: 8,
            7: 13,
            8: 21,
            9: 34
        }

        for i in range(10):
            actual[i] = nth_fib(i)

        self.assertEquals(expected, actual)


    def test_geo(self):
        """Should return the correct geometic numbers"""
        actual = {}
        expected = {
            0: [0, 0, 0],
            1: [1, 1, 1],
            2: [4, 3, 8],
            3: [9, 6, 27],
            4: [16, 10, 64],
            5: [25, 15, 125],
            6: [36, 21, 216],
            7: [49, 28, 343],
            8: [64, 36, 512],
            9: [81, 45, 729],
        }

        for i in range(10):
            actual[i] = [square(i), triangle(i), cube(i)]

        self.assertEquals(expected, actual)


    def test_is_prime(self):
        """Should return true when passed a prime, otherwise false"""
        expected = [False, False, True, True, False, True, False, True, False, False, False]
        actual = [is_prime(i) for i in range(11)]

        self.assertEquals(expected, actual)


    def test_primes(self):
        """Should return all primes less than 100"""
        expected = [
             2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
             43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        ]

        self.assertEquals(expected, primes(100))
