#include <stdio.h>

int main()
{
    long long n, m;
    scanf("%d %d", &n, &m);
    long long nCnt[2] = { 0, };
    long long mCnt[2] = { 0, };
    long long tmp2 = 2, tmp5 = 5;
    while (tmp2 <= n)
    {
        nCnt[0] += n / tmp2;
        mCnt[0] += m / tmp2;
        mCnt[0] += (n - m) / tmp2;
        tmp2 *= 2;
    }
    while (tmp5 <= n)
    {
        nCnt[1] += n / tmp5;
        mCnt[1] += m / tmp5;
        mCnt[1] += (n - m) / tmp5;
        tmp5 *= 5;
    }
    if (nCnt[0] - mCnt[0] <= nCnt[1] - mCnt[1])
        printf("%d", nCnt[0] - mCnt[0]);
    else
        printf("%d", nCnt[1] - mCnt[1]);
    return 0;
}