
void selection_sort(int *arr, int n)
{
    int i, j;
    int min_id;
    int temp;

    for (i = 0; i < n-1; i++)
    {
        min_id = i;
        for (j = i; j < n; j++)
        {
            if (arr[j] < arr[min_id])
            {
                min_id = j;
            }
        }
        temp = arr[i];
        arr[i] = arr[min_id];
        arr[min_id] = temp;
    }

    return;
}