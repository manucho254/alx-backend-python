#!/usr/bin/env python3
""" Type Checking the array
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Zoom array of values
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


array: List = [12, 72, 91]
zoom_2x: List = zoom_array(array)
zoom_3x: List = zoom_array(array, 3)
