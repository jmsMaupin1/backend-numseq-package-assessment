#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module that contains a funntion to return the nth fibonacci number
"""
__author__ = "jmsMaupin1"

def nth_fib(n):
    """Returns the nth Fibonacci number"""
    if n < 2:
        return n
    return nth_fib(n - 1) + nth_fib(n - 2)