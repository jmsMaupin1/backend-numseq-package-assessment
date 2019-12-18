#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing three geometric functions:

Square(n): returns n squared
triangle(n): returns n*(n+1) / 2
cube(n): returns n cubed
"""
__author__ = "jmsMaupin1"


def square(n):
    """returns n squared"""
    return n * n


def triangle(n):
    """returns n triangled"""
    return n * (n + 1) / 2


def cube(n):
    """returns n cubed"""
    return n * n * n