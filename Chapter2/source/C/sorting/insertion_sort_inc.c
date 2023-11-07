#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void insertion_sort_inc(int * arr, int n)
{
    int i, j;
    int key;

    for (i = 0; i < n; i++)
    {
        key = arr[i];
        j = i - 1;
        while (j >= 0 && key < arr[j])
        {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }

}

void print_arr(int *arr, int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    return;
}

void clean(int *arr)
{
    free(arr);
}
