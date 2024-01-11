#!/usr/bin/env python3
""" String concatnate module
"""


def concat(str1: str, str2: str) -> str:
    """ concatenate two strings
        Args:
            str1: string  one
            str2: string two
        Return:
            str1 + str2
    """
    return "{}{}".format(str1, str2)
