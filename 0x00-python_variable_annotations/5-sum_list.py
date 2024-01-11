#!/usr/bin/env python3
""" sum of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ get sum of floats in a list
        Args:
            input_list: a list of floats
        Return:
             sum of floats in input_list
    """
    return sum(input_list)
