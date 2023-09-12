#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// terms_len은 배열 terms의 길이입니다.
// privacies_len은 배열 privacies의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int* solution(const char* today, const char* terms[], size_t terms_len, const char* privacies[], size_t privacies_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = malloc(sizeof(int) * privacies_len);
    int idx = 0;
    char *term = malloc(sizeof(char) * terms_len);
    int *period = malloc(sizeof(int) * terms_len);
    int ty = atoi(strtok(today, "."));
    int tm = atoi(strtok(NULL, "."));
    int td = atoi(strtok(NULL, "."));
    for (size_t i=0;i<terms_len;i++)
    {
        char tterms[5];
        strcpy(tterms, terms[i]);
        term[i] = tterms[0];
        strtok(tterms, " ");
        period[i] = atoi(strtok(NULL, " "));
    }

    for (size_t i=0;i<privacies_len;i++)
    {
        char privacy[13];
        strcpy(privacy, privacies[i]);
        char pterm = privacy[11];
        char *p = strtok(privacy, " ");
        int py = atoi(strtok(p, "."));
        int pm = atoi(strtok(NULL, "."));
        int pd = atoi(strtok(NULL, "."));
        int pperiod;
        for (size_t j=0;j<terms_len;j++)
        {
            if (term[j] == pterm)
            {
                pperiod = period[j];
                break;
            }
        }
        if (pd == 1)
        {
            pd = 28;
            if (pm == 1)
            {
                py -= 1;
                pm = 12;
            }
            else
                pm -= 1;
        }
        else
            pd -= 1;
        pm += pperiod;
        while (pm > 12)
        {
            py += 1;
            pm -= 12;
        }
        if (ty < py) continue;
        else if (ty == py)
        {
            if (tm < pm) continue;
            else if (tm == pm)
            {
                if (td <= pd) continue;
            }
        }
        answer[idx] = i + 1;
        idx += 1;
    }

    return answer;
}
/*
입력값 〉 "2010.06.17", ["A 16"], ["2009.01.19 A", "2000.01.05 A"]
기댓값 〉 [1, 2]
*/