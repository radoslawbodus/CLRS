#include <stdlib.h>

void merge_merge(int *, int, int);

void merge_sort_c(int *arr, int i, int j)
{
    if (j - i <= 1)
        return;

    int m = (i + j) / 2;

    merge_sort_c(arr, i, m);
    merge_sort_c(arr, m, j);
    merge_merge(arr, i, j);
}

void merge_merge(int *arr, int i, int j)
{
    int m = (i + j) / 2;
    int *arr_l = (int *)malloc((m - i) * sizeof(int));
    int *arr_r = (int *)malloc((j - m) * sizeof(int));
    int lp = 0, rp = 0, ap = i;

    while (lp < m - i)
        arr_l[lp++] = arr[ap++];
    lp = 0;

    while (rp < j - m)
        arr_r[rp++] = arr[ap++];
    rp = 0;
    ap = i;

    while (lp < m - i && rp < j - m)
    {
        if (arr_l[lp] <= arr_r[rp])
            arr[ap++] = arr_l[lp++];
        else
            arr[ap++] = arr_r[rp++];
    }

    while (lp < m - i)
        arr[ap++] = arr_l[lp++];
    
    while (rp < j - m)
        arr[ap++] = arr_r[rp++];

    free(arr_l);
    free(arr_r);

    return;
}


