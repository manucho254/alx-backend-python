#!/usr/bin/env python3
""" Loop through values and return a list
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Loop through values and return a list
       Args:
           lst: a tuple of values
           factor: an integer
        Return: a list of integers
    """
    zoomed_in: List = [
            item for item in lst
            for i in range(factor)
            ]
    return zoomed_in


array = [12, 72, 91]
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
