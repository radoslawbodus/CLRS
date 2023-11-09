def insertion_sort_inplace(arr: list[int]) -> None:
    """
    Algorithm for insertion sort that sorts values in the increasing monotonic order in-place.
    """
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key



def insertion_sort_inc(arr: list[int]) -> list[int]:
    """
    Algorithm for insertion sort that sorts values in the increasing monotonic order that returns the sorted array and leaves the passed array untouched
    """
    arr = list(arr)
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def insertion_sort_dec(arr: list[int]) -> list[int]:
    """
    An insertion sort function that returns the sorted array in the monotonic decreasing order.
    Ex: 2.1-3
    """

    arr = list(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr
