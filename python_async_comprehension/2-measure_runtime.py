#!/usr/bin/env python3
""" Async comprehension - measure runtime """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measures the execution time for async_comprehension four times """
    start = asyncio.get_event_loop().time()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)
    end = asyncio.get_event_loop().time()
    return end - start
