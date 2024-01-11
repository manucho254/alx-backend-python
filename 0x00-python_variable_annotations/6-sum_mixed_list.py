#!/usr/bin/env python3
""" Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ get sum of mixed list
        Args:
            mxd_lst: a list of integers and floats
        Return:
            sum of mxd_lst as a float
    """
    return sum(mxd_lst)
