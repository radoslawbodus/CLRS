int binary_search_it_c(int *nums, int n, int target)
{
    int l, r, m;
    l = 0;
    r = n-1;
    
    while (l <= r)
    {
        m = (l + r) / 2; // l and r are type int the operation is in fact a floor division as the result is casted downwards to the nearest integer

        if (nums[m] > target)
            r = m - 1;
        else if (nums[m] < target)
            l = m + 1;
        else
            return m;
    }

    return -1;
}