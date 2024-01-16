#!/usr/bin/env python3
""" Async Comprehensions module
"""

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """  Async Comprehensions function
         Return:
              a list of random numbers
    """
    return [i async for i in async_generator()]
