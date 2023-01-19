from __future__ import annotations

from copy import copy, deepcopy
from functools import wraps
from typing import Callable


def stabledefaults(deep=False):
    if deep:
        copy_strategy = deepcopy
    else:
        copy_strategy = copy

    def wrapper(f: Callable):
        @wraps(f)
        def wrapped(*args, **kwargs):
            n_args_passed = len(args)

            defaults = f.__defaults__
            total_positional_args = f.__code__.co_argcount

            if total_positional_args - n_args_passed > 0:
                trailing_defaults_copies = [
                    copy_strategy(x)
                    for x in defaults[
                        -(total_positional_args - n_args_passed) :
                    ]
                ]
            else:
                trailing_defaults_copies = []

            new_args = list(args) + trailing_defaults_copies

            default_kwargs = f.__kwdefaults__

            if default_kwargs is not None:
                for arg_name, value in default_kwargs.items():
                    if arg_name not in kwargs:
                        kwargs[arg_name] = copy_strategy(value)

            return f(*new_args, **kwargs)

        return wrapped

    return wrapper