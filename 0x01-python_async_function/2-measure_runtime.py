#!/usr/bin/env python3
""" Measure the runtime of code
"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime of code
        Args:
             n: integer
             max_dalay: maximum delay number
        Return:
             total execution time devide by n
    """
    cur_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.perf_counter() - cur_time

    return total_time / n
