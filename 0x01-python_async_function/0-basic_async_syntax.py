#!/usr/bin/env python3
""" asynchronous coroutine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ asynchronous coroutine that takes an integer argument
        Args:
            max_delay: delay number
        Return:
            random.uniform(0, max_delay) value
    """
    rand_val: float = random.uniform(0, max_delay)
    await asyncio.sleep(rand_val)

    return rand_val
