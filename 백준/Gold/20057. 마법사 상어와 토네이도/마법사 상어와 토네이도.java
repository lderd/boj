import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[]args) throws java.io.IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int[][] tornado_d = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}};
        int d = 0;
        int[][] dust = {{1, 1, 1}, {-1, 1, 1}, {1, -1, 10}, {-1, -1, 10},
                {1, 0, 7}, {-1, 0, 7}, {2, 0, 2}, {-2, 0, 2},
                {0, -2, 5}};
/*
0->그대로
1->-dj, di
2->di, -dj
3->dj, -di
rest -> 1 - 45%
*/
        int answer = 0;
        boolean start = false;
        int ci = N/2;
        int cj = N/2;
        boolean[][] check = new boolean[N][N];
        check[ci][cj] = true;
        while (ci != 0 | cj != 0) {
            int nni = ci + tornado_d[(d + 1) % 4][0];
            int nnj = cj + tornado_d[(d + 1) % 4][1];
            if (!check[nni][nnj] & start) {
                d = (d + 1) % 4;
            } else {
                start = true;
                int ni = ci + tornado_d[d][0];
                int nj = cj + tornado_d[d][1];
//                먼지가 있다면
                if (arr[ni][nj] > 0) {
                    int rest = arr[ni][nj];
                    for (int i = 0; i < 9; i++) {
                        int dusti, dustj;
                        int dust_d = arr[ni][nj] * dust[i][2] / 100;
                        rest -= dust_d;
                        if (d == 0) {
                            dusti = ni + dust[i][0];
                            dustj = nj + dust[i][1];
                        } else if (d == 1) {
                            dusti = ni - dust[i][1];
                            dustj = nj + dust[i][0];
                        } else if (d == 2) {
                            dusti = ni + dust[i][0];
                            dustj = nj - dust[i][1];
                        } else {
                            dusti = ni + dust[i][1];
                            dustj = nj - dust[i][0];
                        }
                        if (0 <= dusti & dusti < N & 0 <= dustj & dustj < N) {
                            arr[dusti][dustj] += dust_d;
                        } else {
                            answer += dust_d;
                        }
                    }
                    if (0 <= ni + tornado_d[d][0] & ni + tornado_d[d][0] < N & 0 <= nj + tornado_d[d][1] & nj + tornado_d[d][1] < N) {
                        arr[ni + tornado_d[d][0]][nj + tornado_d[d][1]] += rest;
                    } else {
                        answer += rest;
                    }
                    arr[ni][nj] = 0;
                }
                check[ni][nj] = true;
                ci = ni;
                cj = nj;
            }
        }
        System.out.println(answer);
    }
}