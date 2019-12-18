#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contains a module that handles prime numbers
"""
__author__ = "jmsMaupin1"


def is_prime(n):
    """Returns true if n is a prime otherwise return false"""
    if n <= 1:
        return False
    if n < 3:
        return True

    for i in range(2, n // 2 + 1):
        if not n % i:
            return False
    
    return True

def primes(n):
    """Returns a list of all primes less than n"""
    return [i for i in range(n) if is_prime(i)]