#include <stdio.h>
#include <string.h>

int main()
{
    char *alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int count[26] = {0,};
    char word[1000001];
    scanf("%s", word);
    int cnt = -1;
    char ans = '?';
    int l = strlen(word);
    for (int i = 0; i < l; i++)
    {
        int idx;
        if (word[i] >= 'a') 
        {
            idx = word[i] - 'a';
        } else 
        {
            idx = word[i] - 'A';
        }
        count[idx] += 1;

        if (count[idx] > cnt)
        {
            cnt = count[idx];
            ans = alpha[idx];
        }
        else if (count[idx] == cnt)
        {
            ans = '?';
        }
    }
    printf("%c", ans);
    
    return 0;
}