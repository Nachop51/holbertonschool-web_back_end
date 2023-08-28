#!/usr/bin/env python3
""" Anotations - to_kv """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Sum of list of ints and floats """
    return (k, v * v)
