#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    bool checked[6][6] = { false, };
    char *answer = "Valid";
    int cnt = 0;

    char before[3] = "e";
    char start[3] = "st";
    for (int i = 0; i < 36; i++)
    {
        char after[3];
        scanf("%s", after);
        if (checked[after[0] - 65][after[1] - 49])
        {
            answer = "Invalid";
        }
        checked[after[0] - 65][after[1] - 49] = true;
        cnt += 1;

        if (strlen(before) == 1)
        {
            start[0] = after[0];
            start[1] = after[1];
        }
        else
        {
            int aGap = abs(before[0] - after[0]);
            int bGap = abs(before[1] - after[1]);

            if (!(aGap == 1 && bGap == 2) && !(aGap == 2 && bGap == 1))
            {
                answer = "Invalid";
            }
        }

        before[0] = after[0];
        before[1] = after[1];
    }
    int aGap = abs(before[0] - start[0]);
    int bGap = abs(before[1] - start[1]);

    if (!(aGap == 1 && bGap == 2) && !(aGap == 2 && bGap == 1))
    {
        answer = "Invalid";
    }

    if (cnt != 36)
        answer = "Invalid";

    printf("%s", answer);
    return 0;
}