## One function that will merge the two arrays
## the other function that will split the two arrays

def merge_sort_factory(type_merge: int, k: int = 0):

    def merge_sort(arr: list[int]):

        ## As the below two functions are not really needed anywhere else we can embed them into this runner function
        def insertion_sort_inplace(arr: list[int], start, end) -> None:
            """
            Algorithm for insertion sort that sorts values in the increasing monotonic order in-place.
            """
            for i in range(start, end):
                key = arr[i]
                j = i - 1
                while j >= start and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1

                arr[j + 1] = key

        def merge_sort_r(arr: list[int], i: int, j: int):
            # print(arr, i, j)
            if j-i <= 1:
                return
            m = (i + j) // 2
            
            merge_sort_r(arr, i, m)
            merge_sort_r(arr, m, j)
            if j - i <= k and type_merge == 1:
                insertion_sort_inplace(arr, i, j)
                return
            merge_merge(arr, i, j)
            # print(arr, i, j)

        def merge_merge(arr, i, j):
            m = (i + j) // 2
            
            arr_l = arr[i:m]
            arr_r = arr[m:j]

            lp, rp, ap = 0, 0, i
            
            while lp < len(arr_l) and rp < len(arr_r):
                if arr_l[lp] <= arr_r[rp]:
                    arr[ap] = arr_l[lp]
                    lp += 1
                else:
                    arr[ap] = arr_r[rp]
                    rp += 1
                ap += 1
            
            while lp < len(arr_l):
                arr[ap] = arr_l[lp]
                lp += 1
                ap += 1
            
            while rp < len(arr_r):
                arr[ap] = arr_r[rp]
                rp += 1
                ap += 1
            
            return 

        arr = list(arr)
        merge_sort_r(arr, 0, len(arr))

        return arr
    
    return merge_sort

merge_sort = merge_sort_factory(0)
merge_sort_ins_2 = merge_sort_factory(1, 2)
merge_sort_ins_4 = merge_sort_factory(1, 4)
merge_sort_ins_8 = merge_sort_factory(1, 8)