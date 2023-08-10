#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int dmg[6][3] = {{9, 3, 1}, {9, 1, 3}, {3, 9, 1}, {3, 1, 9}, {1, 9, 3}, {1, 3, 9}};

bool checked[61][61][61] = { false, };

int compare(const void *a, const void *b)
{
    return *(int *)b - *(int *)a;
}

void down(int scv[], int n, int cnt, int *answer)
{
    if (cnt >= *answer)
    {
        return;
    }

    int tmp[3] = { 0, };

    for (int i = 0; i < n; i++)
    {
        tmp[i] = scv[i];
    }
    
    for (int i = 0; i < 3; i++)
    {
        if (tmp[i] < 0)
            tmp[i] = 0;
    }

    if (!(tmp[0] == 0 && tmp[1] == 0 && tmp[2] == 0) && checked[tmp[0]][tmp[1]][tmp[2]])
        return;
    checked[tmp[0]][tmp[1]][tmp[2]] = true;


    qsort(tmp, n, sizeof(int), compare);

    if (tmp[0] > 0)
    {
        for (int i = 0; i < 6; i++)
        {
            for (int j = 0; j < n; j++)
            {
                tmp[j] -= dmg[i][j];
            }
            down(tmp, n, cnt + 1, answer);
            for (int j = 0; j < n; j++)
            {
                tmp[j] += dmg[i][j];
            }
        }
    }
    else
    {
        *answer = cnt;
        return;
    }
}

int main()
{
    int answer = 99;
    int n;
    scanf("%d\n", &n);
    int scv[3] = { 0, };
    char tmp[10];
    scanf("%[^\n]s", tmp);
    scv[0] = atoi(strtok(tmp, " "));
    for (int i = 1; i < n; i++)
    {
        scv[i] = atoi(strtok(NULL, " "));
    }

    down(scv, n, 0, &answer);

    printf("%d", answer);
    return 0;
}