#!/usr/bin/env python3
""" Return a function from a function
"""
from typing import Callable


def mult(a: float) -> float:
    """ multiply two float values
        Args:
            a: float value a
            b: float value b
        Return:
            multiple of a and b
    """
    return float(a * a)


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multiply function by float
        Args:
            multiplier: value to multiply
        Return:
              function that multiples a float by
    """
    return mult
