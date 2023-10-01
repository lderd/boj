#include <stdio.h>
#include <string.h>

int main() {
    char n[9];
    scanf("%s", n);
    int l = strlen(n);
    int left = 0;
    int right = 0;
    for (size_t i = 0; i < l; i++)
    {
        if (i < l / 2)
            left += n[i] - 48;
        else
            right += n[i] - 48;
    }
    if (left == right)
        printf("LUCKY");
    else
        printf("READY");
    return 0;
}