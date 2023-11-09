import ctypes
from source.python import helper

libc = ctypes.CDLL("/home/rbuntu/Grath/CLRS/Chapter2/source/CDLL/sorting_algs.so")

insertion_sort_c = libc.insertion_sort_inc
insertion_sort_c.restype = None
insertion_sort_c = helper.sorting_decorator(insertion_sort_c)

recursive_insertion_sort_c = libc.recursive_insertion_sort_c
recursive_insertion_sort_c.restype = None
recursive_insertion_sort_c = helper.sorting_decorator(
    recursive_insertion_sort_c, recursive=True
)

selection_sort_c = libc.selection_sort
selection_sort_c.restype = None
selection_sort_c = helper.sorting_decorator(selection_sort_c)

merge_sort_c = libc.merge_sort_c
merge_sort_c.restype = None
merge_sort_c = helper.sorting_decorator(merge_sort_c, recursive=True, recursive_dac=True)

