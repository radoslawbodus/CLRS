
int linear_search(int *nums, int n, int target)
{
    int i;
    
    for (i = 0; i < n; i++)
    {
        if (target == nums[i])
            return i;
    }

    return -1;
}