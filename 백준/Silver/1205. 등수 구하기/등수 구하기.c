#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void *b)
{
    return *(int *)b - *(int *)a;
}

int main()
{
    // 리스트에있는점수갯수n, 태수점수score, 랭킹갯수p
    int n, score, p;
    scanf("%d %d %d", &n, &score, &p);
    if (n > 0)
    {
        scanf("\n");
        int rank[p];
        for (int i = 0; i < p; i++)
        {
            rank[i] = -1;
        }
        char tmp[5000];
        scanf("%[^\n]s", tmp);

        rank[0] = atoi(strtok(tmp, " "));
        for (int i = 1; i < n; i++)
        {
            rank[i] = atoi(strtok(NULL, " "));
        }

        qsort(rank, p, sizeof(int), compare);
        int answer = -1;

        for (int i = 0; i < p; i++)
        {
            if (rank[i] <= score)
            {
                answer = i + 1;
                break;
            }
        }
        if (n == p && rank[p - 1] == score)
            answer = -1;
        printf("%d", answer);
    }
    else
    {
        printf("1");
    }
    return 0;
}