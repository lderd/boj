#include <stdio.h>

int main()
{
    int N;
    scanf("%d", &N);
    int ans1 = 0, ans2 = 0;
    for (int i = 1;i < N + 1;i++)
    {
        ans1 += i;
        ans2 += i * i * i;
    }
    printf("%d\n", ans1);
    printf("%d\n", ans1 * ans1);
    printf("%d\n", ans2);
    return 0;
}