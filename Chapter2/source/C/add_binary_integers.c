
void abi(int *a, int *b, int *c, int n)
{
    int move = 0;
    int v;
    int i;

    for (i = 0; i < n; i++)
    {
        v = a[i] + b[i] + move;
        move = v / 2; // implicit conversion to int makes it a floor division
        c[i] = v % 2;
    }
    c[n] = move;
    
    return;
}