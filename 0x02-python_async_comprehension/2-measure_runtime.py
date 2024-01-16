#!/usr/bin/env python3
"""  Run time for four parallel comprehensions
"""

import asyncio
import time
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run time for four parallel comprehensions
        Return:
             execution time
    """
    tasks: List = []

    for _ in range(4):
        tasks.append(async_comprehension())

    start_time: float = time.perf_counter()
    await asyncio.gather(*tasks)
    end_time: float = time.perf_counter() - start_time

    return end_time
