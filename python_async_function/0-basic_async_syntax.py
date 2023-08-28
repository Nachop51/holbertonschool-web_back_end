#!/usr/bin/env python3
""" Async - basic syntax """

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10):
    """ Waits for a random delay between 0 and max_delay """
    value = uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
