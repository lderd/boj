#include <stdio.h>
#include <stdbool.h>

int main()
{
    char cnt[26] = { 0, };
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        char tmp[31];
        scanf("%s", tmp);
        cnt[tmp[0] - 97] += 1;
    }
    
    bool idx = true;
    for (size_t i = 0; i < 26; i++)
    {
        if (cnt[i] >= 5)
        {
            printf("%c", i + 97);
            idx = false;
        }
    }
    if (idx)
        printf("PREDAJA");
    return 0;
}