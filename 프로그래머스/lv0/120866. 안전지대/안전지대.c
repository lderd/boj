#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// board_rows는 2차원 배열 board의 행 길이, board_cols는 2차원 배열 board의 열 길이입니다.
int solution(int** board, size_t board_rows, size_t board_cols) {
    int answer = 0;
    int di[] = {0, 0, 1, -1, 1, 1, -1, -1};
    int dj[] = {1, -1, 0, 0, 1, -1, 1, -1};
    for (size_t i = 0; i < board_rows; i++)
    {
        for (size_t j = 0; j < board_cols; j++)
        {
            if (board[i][j] == 1) continue;
            answer += 1;
            for (size_t d = 0; d < 8; d++)
            {
                int ni = i + di[d];
                int nj = j + dj[d];
                if (0 <= ni && ni < board_rows && 0 <= nj && nj < board_cols && board[ni][nj] == 1)
                {
                    answer -= 1;
                    break;
                }
            }
        }
    }
    return answer;
}