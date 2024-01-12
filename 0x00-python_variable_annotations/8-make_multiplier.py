#!/usr/bin/env python3
""" Return a function from a function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multiply function by float
        Args:
            multiplier: value to multiply
        Return:
              function that multiples a float by
    """
    mult: Callable[[float], float] = lambda value: value * multiplier
    return mult
