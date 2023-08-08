#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int main()
{
    int n;
    scanf("%d", &n);
    int answer = 0;
    for (int i = 1; i <= n; i++)
    {
        char N[5];
        sprintf(N, "%d", i);

        bool hansu = true;

        int l = strlen(N);
        if (l < 3)
        {
            answer += 1;
            continue;
        }

        int gap = N[0] - N[1];
        for (int j = 0; j < l - 1; j++)
        {
            if (N[j] - N[j+1] != gap)
            {
                hansu = false;
                break;
            }
        }

        if (hansu)
            answer += 1;
    }
    printf("%d", answer);
    return 0;
}