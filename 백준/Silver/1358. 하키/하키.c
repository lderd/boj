#include <stdio.h>


int main()
{
    int w, h, x, y, p;
    scanf("%d %d %d %d %d\n", &w, &h, &x, &y, &p);
    int answer = 0;
    for (size_t i = 0; i < p; i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        if (a >= x && a <= x + w && b >= y && b <= y + h)
            answer += 1;
        else
        {
            if (a < x && b >= y && b <= y + h)
            {
                if ((x - a) * (x - a) + (y - b + h / 2) * (y - b + h / 2) <= (h / 2) * (h / 2))
                    answer += 1;
            }
            else if (a > x + w && b >= y && b <= y + h)
            {
                if ((x + w - a) * (x + w - a) + (y - b + h / 2) * (y - b + h / 2) <= (h / 2) * (h / 2))
                    answer += 1;
            }
            
        }
    }
    printf("%d", answer);
    return 0;
}