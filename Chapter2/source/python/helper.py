import ctypes
from typing import Callable
from functools import wraps


# decorator for C sorting functions
def sorting_decorator(
    func: Callable, recursive: bool = False, recursive_dac: bool = False, 
) -> Callable[[list[int]], list[int]]:
    @wraps(func)
    def run_sort_alg(arr: list[int]) -> list[int]:
        arr_type = ctypes.c_int * len(arr)
        n = ctypes.c_int(len(arr))
        arr_c = arr_type(*arr)
        if recursive:
            if recursive_dac:
                func(ctypes.pointer(arr_c), ctypes.c_int(0), ctypes.c_int(len(arr)))
            else:
                func(ctypes.pointer(arr_c), n, ctypes.c_int(len(arr) - 1))
        else:
            func(ctypes.pointer(arr_c), n)

        return list(arr_c)

    return run_sort_alg


# decorator for C searching functions
def search_decorator(func: Callable) -> Callable[[list[int], int], int]:
    @wraps(func)
    def run_search_alg(arr: list[int], target: int) -> int:
        arr_type = ctypes.c_int * len(arr)
        n = ctypes.c_int(len(arr))
        target = ctypes.c_int(target)
        arr_c = arr_type(*arr)
        return func(ctypes.pointer(arr_c), n, target)

    return run_search_alg
