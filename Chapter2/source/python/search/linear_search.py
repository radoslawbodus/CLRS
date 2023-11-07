def linear_search(nums: list[int], target: int) -> int:
    """
    Linear search algorithm. When the item is not found -1 is returned.
    Ex 2.1-4 CLRS
    """

    for i, num in enumerate(nums):
        if num == target:
            return i

    return -1
