import sys
from typing import Callable
import random
import pytest

sys.path.append("/home/rbuntu/Grath/CLRS/Chapter2")
from source.python.sorting import (
    insertion_sort,
    recursive_insertion_sort,
    selection_sort,
    merge_sort,
    merge_sort_ins_2
)
from source.python.sorting_c.sorting_algs import (
    insertion_sort_c,
    recursive_insertion_sort_c,
    selection_sort_c,
    merge_sort_c
)


def sort_test(sorting_alg: Callable[[list[int]], list[int]], sample_size: int) -> None:
    random.seed(42)
    arr = [random.randint(0, 1000) for _ in range(sample_size)]
    assert sorting_alg(arr) == sorted(arr), f"{sorting_alg.__name__} failed"


sort_algs = [
    insertion_sort,
    recursive_insertion_sort,
    selection_sort,
    merge_sort,
    merge_sort_ins_2,
    insertion_sort_c,
    recursive_insertion_sort_c,
    selection_sort_c,
    merge_sort_c,
]

random.seed(42)
arr = [random.randint(0, 100) for _ in range(100)]
sorted_arr = sorted(arr)


@pytest.mark.parametrize(
    "sorting_alg, arr, sorted_arr",
    [(sort_alg, arr, sorted_arr) for sort_alg in sort_algs],
)
def test_sorts(sorting_alg, arr, sorted_arr):
    assert sorting_alg(arr) == sorted_arr
