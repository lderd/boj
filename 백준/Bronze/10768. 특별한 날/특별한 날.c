#include <stdio.h>

int main() {
    int month, date;
    scanf("%d", &month);
    scanf("%d", &date);
    if (month == 2 && date == 18)
    {
        printf("Special");
    }
    else if (month < 2)
    {
        printf("Before");
    }
    else if (month == 2 && date < 18)
    {
        printf("Before");
    }
    else 
    {
        printf("After");
    }
    return 0;
}