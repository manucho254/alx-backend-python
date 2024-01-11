#!/usr/bin/env python3
""" duck typing  an iterable object
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element length
        Args:
            lst: a list of values
        Return:
            a list of tuples
    """
    return [(i, len(i)) for i in lst]
