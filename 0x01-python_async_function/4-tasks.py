#!/usr/bin/env python3
""" execute multiple coroutines at the same time
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ execute multiple coroutines at the same time
        Args:
            n: number of times to execute
            max_delay: delay value
        Return:
            a list of floats
    """
    arr: List[float] = []

    for _ in range(n):
        rand_val: float = await task_wait_random(max_delay)
        arr.append(rand_val)

    return sorted(arr)
