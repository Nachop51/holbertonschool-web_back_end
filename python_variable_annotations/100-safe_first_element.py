#!/usr/bin/env python3
""" Anotations - safe_first_element """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Return first element of list """
    if lst:
        return lst[0]
    else:
        return None
