#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// id_list_len은 배열 id_list의 길이입니다.
// report_len은 배열 report의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int* solution(const char* id_list[], size_t id_list_len, const char* report[], size_t report_len, int k) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = malloc(sizeof(int) * id_list_len);
    int* cnt = malloc(sizeof(int) * id_list_len);
    bool* checked = malloc(sizeof(bool) * id_list_len * id_list_len);
    for (size_t i = 0;i < id_list_len;i++)
    {
        answer[i] = 0;
        cnt[i] = 0;
        for (size_t j = 0;j < id_list_len;j++)
        {
            checked[i * id_list_len + j] = false;
        }
    }

    for (size_t i = 0;i < report_len;i++)
    {
        char report_info[22];
        strcpy(report_info, report[i]);
        char *report_name = strtok(report_info, " ");
        char *reported_name = strtok(NULL, " ");
        int report_idx = idx(id_list, id_list_len, report_name);
        int reported_idx = idx(id_list, id_list_len, reported_name);
        if (!checked[report_idx + id_list_len * reported_idx]) {
            checked[report_idx + id_list_len * reported_idx] = true;
            cnt[reported_idx] += 1;
        }
    }
    for (size_t i = 0;i < id_list_len;i++)
    {
        if (cnt[i] >= k) {
            for (size_t j = 0;j < id_list_len;j++) {
                if (checked[i * id_list_len + j]) {
                    answer[j] += 1;
                }
            }
        }
    }
    return answer;
}

int idx(const char* id_list[], size_t id_list_len, char* name) {
    for (size_t i=0;i<id_list_len;i++)
    {
        if (strcmp(id_list[i], name) == 0)
            return i;
    }
}
/*
["abc", "acd", "add", "abd"], ["abc abd", "abc add", "acd abd", "abc abd", "add abd"], 2
[1, 1, 1, 0]
*/