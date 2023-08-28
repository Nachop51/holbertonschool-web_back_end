#!/usr/bin/env python3
""" Anotations - element_length """
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return list of tuples, each containing an element and its length """
    return [(i, len(i)) for i in lst]
