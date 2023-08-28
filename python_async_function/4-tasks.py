#!/usr/bin/env python3
""" Async - tasks """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int):
    """ spawn wait_random n times with the specified max_delay """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]