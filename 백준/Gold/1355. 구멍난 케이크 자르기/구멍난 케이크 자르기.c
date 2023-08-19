#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void * b)
{
    return *(int *)a - *(int *)b;
}

int main()
{
    // 케이크 한 변의 절반LC, 구멍 절반LH
    int LC, LH;
    scanf("%d %d\n", &LC, &LH);
    // 가로줄 수
    int H;
    scanf("%d\n", &H);
    int horizons[H + 2];

    char tmp[1000];
    if (H)
        scanf("%[^\n]s\n", tmp);
    else
        scanf(" ");
    if (H > 0)
    {
        int ttmp = atoi(strtok(tmp, " "));
        horizons[0] = ttmp;
    }
    for (size_t i = 1; i < H; i++)
    {
        int ttmp = atoi(strtok(NULL, " "));
        horizons[i] = ttmp;
    }
    horizons[H] = -LC;
    horizons[H + 1] = LC;
    qsort(horizons, H + 2, sizeof(int), compare);

    // 세로줄 수
    int V;
    scanf("%d\n", &V);
    int verticals[V + 2];

    char ttmp[1000];
    if (V)
        scanf("%[^\n]s\n", ttmp);
    else
        scanf(" ");
    if (V > 0)
    {
        int tmp = atoi(strtok(ttmp, " "));
        verticals[0] = tmp;
    }
    for (size_t i = 1; i < V; i++)
    {
        int tmp = atoi(strtok(NULL, " "));
        verticals[i] = tmp;
    }
    verticals[V] = -LC;
    verticals[V + 1] = LC;
    qsort(verticals, V + 2, sizeof(int), compare);

    int v = 0, h = 0;
    int in_v = 0, in_h = 0;
    for (size_t i = 1; i < V + 2; i++)
    {
        if (verticals[i-1] < verticals[i])
        {
            v += 1;
            if (verticals[i] >= -LH && verticals[i] <= LH)
                in_v += 1;
        }
    }
    for (size_t i = 1; i < H + 2; i++)
    {
        if (horizons[i-1] < horizons[i])
        {
            h += 1;
            if (horizons[i] >= -LH && horizons[i] <= LH)
                in_h += 1;
        }
    }
    if (in_v && in_h)
    {
        in_v -= 1;
        in_h -= 1;
        printf("%d", v * h - in_v * in_h);
    }
    else if (in_v == 0 && in_h > 0)
        printf("%d", v * h + in_h - 1);
    else if (in_h == 0 && in_v > 0)
        printf("%d", v * h + in_v - 1);
    else
        printf("%d", v * h);

    return 0;
}