#include <stdio.h>
#include <string.h>

int main()
{
    char s[51];
    scanf("%s", s);
    int ls = strlen(s);
    char t[51];
    scanf("%s", t);
    int lt = strlen(t);
    int answer = 1;
    int i = 1;
    while (i % ls != 0 || i % lt != 0 || (i < 2 * ls || i < 2 * lt))
    {
        if (s[(i - 1) % ls] != t[(i - 1) % lt])
        {
            answer = 0;
            break;
        }
        i += 1;
    }
    printf("%d", answer);
    return 0;
}