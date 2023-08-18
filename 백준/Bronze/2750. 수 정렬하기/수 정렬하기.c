#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}

int main()
{
    int n;
    scanf("%d", &n);
    int arr[n];
    for (size_t i = 0; i < n; i++)
    {
        int tmp;
        scanf("%d", &tmp);
        arr[i] = tmp;
    }
    qsort(arr, n, sizeof(int), compare);
    for (size_t i = 0; i < n; i++)
    {
        printf("%d\n", arr[i]);
    }
    
    return 0;
}