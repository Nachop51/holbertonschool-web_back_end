#!/usr/bin/env python3
""" Anotations - make_multiplier """
from typing import Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return a function that multiplies a float by multiplier """
    def multiply(n: float) -> float:
        """ Multiply a float by multiplier """
        return n * multiplier
    return multiply
