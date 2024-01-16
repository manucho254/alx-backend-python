#!/usr/bin/env python3
""" Async Generator module
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """ Async Generator function
        Return:
              a generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
