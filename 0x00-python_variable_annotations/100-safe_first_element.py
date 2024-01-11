#!/usr/bin/env python3
""" Duck typing - first element of a sequence
"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ get first item in list
        Args:
            lst: a list of different items
        Return:
             if list is not empty return first item else none
    """
    if lst:
        return lst[0]
    else:
        return None
