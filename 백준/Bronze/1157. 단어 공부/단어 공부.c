#include <stdio.h>
#include <string.h>

int main()
{
    char *alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int count[26] = {0,};
    char word[1000001];
    scanf("%s", word);
    int l = strlen(word);
    for (int i = 0; i < l; i++)
    {
        if (word[i] >= 'a') 
        {
            count[word[i] - 'a'] += 1;
        } else 
        {
            count[word[i] - 'A'] += 1;
        }
    }
    int cnt = -1;
    char ans = '?';
    for (int i = 0; i < 26; i++)
    {
        if (count[i] > cnt)
        {
            cnt = count[i];
            ans = alpha[i];
        }
        else if (count[i] == cnt)
        {
            ans = '?';
        }
    }
    printf("%c", ans);
    
    return 0;
}