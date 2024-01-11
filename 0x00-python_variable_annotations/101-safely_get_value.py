#!/usr/bin/env python3
""" More involved type annotations
"""

from typing import Union, TypeVar, Mapping, Any

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ find value in dictionary
        Args:
            dct: dictionary
        Return:
             a dict value or default
    """
    if key in dct:
        return dct[key]
    else:
        return default
