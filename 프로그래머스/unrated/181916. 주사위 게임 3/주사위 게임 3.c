#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return *(int*) a - *(int*) b;
}

int solution(int a, int b, int c, int d) {
    int answer = 0;
    int cnt = 0;
    if (a == b)
        cnt += 1;
    if (a == c)
        cnt += 1;
    if (a == d)
        cnt += 1;
    if (b == c)
        cnt += 1;
    if (b == d)
        cnt += 1;
    if (c == d)
        cnt += 1;

    if (cnt == 6)
        answer = 1111 * a;
    else {
        int nums[] = {a, b, c, d};
        qsort(nums, 4, sizeof(int), compare);
        if (cnt == 0)
            answer = nums[0];
        else if (cnt == 2) {
            answer = (nums[0] + nums[3]) * abs(nums[0] - nums[3]);
        }
        else if (cnt == 1) {
            if (nums[0] == nums[1])
                answer = nums[2] * nums[3];
            else if (nums[1] == nums[2])
                answer = nums[0] * nums[3];
            else
                answer = nums[0] * nums[1];
        }
        else {
            if (nums[0] == nums[1])
                answer = (10 * nums[0] + nums[3]) * (10 * nums[0] + nums[3]);
            else
                answer = (10 * nums[3] + nums[0]) * (10 * nums[3] + nums[0]);
        }
    }
    return answer;
}