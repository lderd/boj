#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d\n", &n);
    int arr[n];
    char tmp[500005];
    scanf("%[^\n]s", tmp);
    arr[0] = atoi(strtok(tmp, " "));
    for (int i = 1; i < n; i++)
    {
        arr[i] = atoi(strtok(NULL, " "));
    }
    int answer = -2000000000;
    int val = -2000000000;
    for (int i = 0; i < n; i++)
    {
        if (val + arr[i] < arr[i])
        {
            val = arr[i];
        }
        else
            val += arr[i];
        if (val > answer)
            answer = val;
    }
    printf("%d", answer);
    return 0;
}