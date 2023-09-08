#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// babbling_len은 배열 babbling의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* babbling[], size_t babbling_len) {
    int answer = 0;
    for (int i=0;i<babbling_len;i++)
    {
        int len = strlen(babbling[i]);
        int j = 0;
        bool check[4] = { false, };
        while (j < len) {
            if (babbling[i][j] == 'a' && !check[0] && len - j >= 3 &&babbling[i][j+1] == 'y' && babbling[i][j+2] == 'a') {
                j += 3;
                check[0] = true;
            }
            else if (babbling[i][j] == 'y' && !check[1] && len - j >= 2 && babbling[i][j+1] == 'e') {
                j += 2;
                check[1] = true;
            }
            else if (babbling[i][j] == 'w' && !check[2] && len - j >= 3 && babbling[i][j+1] == 'o' && babbling[i][j+2] == 'o') {
                j += 3;
                check[2] = true;
            }
            else if (babbling[i][j] == 'm' && !check[3] && len - j >= 2 && babbling[i][j+1] == 'a') {
                j += 2;
                check[3] = true;
            }
            else break;
        }
        if (j == len) answer += 1;
    }
    return answer;
}