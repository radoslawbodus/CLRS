def recursive_insertion_sort(nums: list[int]):
    def rec_is(nums: list[int], end: int) -> None | int:
        """
        Recursive implementation of insertion sort.
        It is done in place as to save the time and memory of creating smaller copies of the nums array for each consecutive recursion call.

        EX 2.3-5
        """
        if end == 0:
            return None

        rec_is(nums, end - 1)

        j = end - 1
        key = nums[end]
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

        return None

    arr = list(nums)
    rec_is(arr, len(arr) - 1)

    return arr


# if __name__ == '__main__':
#     nums = [1,5,3,7,3,2]
#     rec_is(nums=nums, end=len(nums)-1)
#     print(nums)
