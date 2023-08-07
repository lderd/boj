#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n[10001] = { 0, };
    int tmp;
    char s[6];

    for (int i = 1; i < 10000; i++)
    {
        tmp = i;
        while (tmp < 10001)
        {
            sprintf(s, "%d", tmp);

            int l = strlen(s);
            for (int j = 0; j < l; j++)
            {
                tmp += s[j] - 48;
            }
            if (tmp < 10001)
                n[tmp] += 1;
        }
        
    }
    for (int i = 1; i < 10001; i++)
    {
        if (n[i] == 0)
            printf("%d\n", i);
    }
    
    return 0;
}