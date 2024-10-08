"""
@author: F. B. Pérez Maurera
"""
from __future__ import annotations

import time

from typing import cast, Any, Callable, TypeVar, Tuple, Dict
from recsys_framework.Utils.conf_logging import get_logger

logger = get_logger(__name__)

T_F = TypeVar('T_F', bound=Callable[..., Any])
T_ARGS = TypeVar('T_ARGS', bound=Tuple[Any])
T_KWARGS = TypeVar('T_KWARGS', bound=Dict[str, Any])


def timeit(func: T_F) -> T_F:
    """
    Decorator that measures execution time of a method. This is a modified version from the one published at:
    https://medium.com/pythonhive/python-decorator-to-measure-the-execution-time-of-methods-fa04cb6bb36d
    """

    def wrapper(*args: T_ARGS, **kwargs: T_KWARGS) -> Any:
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        logger.info(
            f"{func.__name__}|Execution time: {te - ts:.2f}s"
        )
        return result

    return cast(T_F, wrapper)


def log_calling_args(func: T_F) -> T_F:
    def wrapper(*args: T_ARGS, **kwargs: T_KWARGS) -> Any:
        logger.debug(
            f"Calling method '{func.__name__}' with args={args} and kwargs={kwargs}"
        )
        return func(*args, **kwargs)

    return cast(T_F, wrapper)
