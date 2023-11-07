def selection_sort(arr: list[int]) -> list[int]:
    """
    Selection sort algorithm that has O(n^2) time complexity both for worst and best case scenario
    """
    arr = list(arr)  # Create a copy of the data

    for i in range(len(arr) - 1):
        min_id = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_id]:
                min_id = j
        temp = arr[i]
        arr[i] = arr[min_id]
        arr[min_id] = temp

    return arr
