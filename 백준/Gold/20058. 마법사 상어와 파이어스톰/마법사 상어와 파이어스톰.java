import java.io.*;
import java.util.*;

public class Main {
    static int[][] ice;
    static int N, iceSum, bigIce;
    static int[][] direction = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stNQ = new StringTokenizer(br.readLine());
        N = (int) Math.pow(2, Integer.parseInt(stNQ.nextToken()));
        int Q = Integer.parseInt(stNQ.nextToken());
        ice = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                ice[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        StringTokenizer cast = new StringTokenizer(br.readLine());
        for (int i = 0; i < Q; i++) {
            magic(Integer.parseInt(cast.nextToken()));
            melt();
        }
        solve();
        System.out.println(iceSum);
        System.out.println(bigIce);
    }

    static void magic(int L) {
        int[][] tmp = new int[N][N];
        int n = (int) Math.pow(2, L);
        int cntR = 0;
        while (cntR <= N - n) {
            int cntC = 0;
            while (cntC <= N - n) {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        tmp[cntR + i][cntC + j] = ice[cntR + n - 1 - j][cntC + i];
                    }
                }
                cntC += n;
            }
            cntR += n;
        }
        ice = tmp;
    }

    static void melt() {
        int[][] tmp = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (ice[i][j] > 0) {
                    int around = 0;
                    for (int d = 0; d < 4; d++) {
                        int ni = i + direction[d][0];
                        int nj = j + direction[d][1];
                        if (0 <= ni & ni < N & 0 <= nj & nj < N) {
                            if (ice[ni][nj] > 0) {
                                around += 1;
                            }
                        }
                    }
                    if (around < 3) {
                        tmp[i][j] = ice[i][j] - 1;
                    } else {
                        tmp[i][j] = ice[i][j];
                    }
                }
            }
        }
        ice = tmp;
    }

    static void solve() {
        iceSum = 0;
        bigIce = 0;
        boolean[][] checked = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (ice[i][j] > 0) {
//                    값이 있다면 전체에 더해주고
                    iceSum += ice[i][j];
//                    가장 큰 녀석인지 확인하지 않았다면 확인한다
                    if (!checked[i][j]) {
//                        초기값
                        int tmp = 1;
                        checked[i][j] = true;

                        Queue<int[]> q = new LinkedList<>();
                        int[] start = {i, j};
                        q.add(start);

                        while (!q.isEmpty()) {
                            int[] c = q.poll();
                            for (int d = 0; d < 4; d++) {
                                int ni = c[0] + direction[d][0];
                                int nj = c[1] + direction[d][1];
                                if (0 <= ni & ni < N & 0 <= nj & nj < N) {
                                    if (ice[ni][nj] > 0 & !checked[ni][nj]) {
                                        int[] next = {ni, nj};
                                        tmp += 1;
                                        checked[ni][nj] = true;
                                        q.add(next);
                                    }
                                }
                            }
                        }

                        if (tmp > bigIce) {
                            bigIce = tmp;
                        }
                    }
                }
            }
        }
    }
}