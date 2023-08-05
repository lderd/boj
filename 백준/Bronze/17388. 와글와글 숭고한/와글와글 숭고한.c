#include <stdio.h>

int main()
{
    int s, k, h;
    char *ans = "";
    scanf("%d %d %d", &s, &k, &h);
    if (s + k + h >= 100)
        ans = "OK";
    else
    {
        int cnt = 101;
        if (cnt > s)
        {
            ans = "Soongsil";
            cnt = s;
        }
        if (cnt > k)
        {
            ans = "Korea";
            cnt = k;
        }
        if (cnt > h)
        {
            ans = "Hanyang";
            cnt = h;
        }
    }
    printf("%s", ans);
    return 0;
}