#!/usr/bin/env python3
""" Complex types - string and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ values to tuple
        Args:
            k: string value
            v: int or float value
        Return:
            a tuple containing k and v
    """
    square_v: float = v ** 2

    return (k, square_v)
