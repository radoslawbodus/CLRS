#include <stdio.h>

void recursive_insertion_sort_c(int *nums, int n, int end)
{
    // base case
    if (end == 0)
        return;
    
    // Recursive step 
    recursive_insertion_sort_c(nums, n, end-1);

    int j = end - 1;
    int key = nums[end];

    while (j >= 0 && key < nums[j])
    {
        nums[j+1] = nums[j];
        j -= 1;
    }
    nums[j+1] = key;
    
    return;
}

// Testing Recursive function
/*
int main(void)
{
    int nums[10] = {4,6,2,3,7,1,2};
    int n = 10;
    int end = n-1;
    int i;

    recursive_insertion_sort(nums, n, end);

    for (i = 0; i < n; i++)
    {
        printf("arr[%d]=%d\n", i, nums[i]);
    }

    return 0;
}
*/