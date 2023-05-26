import java.io.*;
import java.util.*;

public class Main {
    static int N, M, ssum, rest;
    static int[][] circles;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stNMK = new StringTokenizer(br.readLine());
        N = Integer.parseInt(stNMK.nextToken());
        M = Integer.parseInt(stNMK.nextToken());
        int K = Integer.parseInt(stNMK.nextToken());
        rest = N * M;
        circles = new int[N][M];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int tmp = Integer.parseInt(st.nextToken());
                ssum += tmp;
                circles[i][j] = tmp;
            }
        }
        for (int i = 0; i < K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            rotate(x, d, k);
            boolean duplication = deleteDuplication();
            if (!duplication) {
                float average = (float) ssum / rest;
                for (int j = 0; j < N; j++) {
                    for (int l = 0; l < M; l++) {
                        if (circles[j][l] > 0) {
                            if (circles[j][l] > average) {
                                circles[j][l] -= 1;
                                ssum -= 1;
                                if (circles[j][l] == 0) {
                                    rest -= 1;
                                }
                            } else if (circles[j][l] < average) {
                                circles[j][l] += 1;
                                ssum += 1;
                            }
                        }
                    }
                }
            }
        }
        System.out.println(ssum);
    }
    private static void rotate(int x, int d, int k) {
        int index = x - 1;
        while (index < N){
            int[] tmp = new int[M];
            if (d == 0) {
                for (int i = 0; i < M; i++) {
                    tmp[(i + k) % M] = circles[index][i];
                }
            }
            if (d == 1) {
                for (int i = 0; i < M; i++) {
                    tmp[(i + M - k) % M] = circles[index][i];
                }
            }
            circles[index] = tmp;
            index += x;
        }
    }
    private static boolean deleteDuplication() {
        boolean val = false;
        int[][] direction = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
        boolean[][] checked = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (!checked[i][j] && circles[i][j] > 0) {
                    int cnt = 1;
                    int tmp = circles[i][j];
                    checked[i][j] = true;
                    Queue<int[]> q = new LinkedList<>();
                    q.add(new int[]{i, j});
                    while (!q.isEmpty()) {
                        int[] c = q.poll();
                        for (int d = 0; d < 4; d++) {
                            int ni = c[0] + direction[d][0];
                            int nj = (c[1] + direction[d][1] + M) % M;
                            if (0 <= ni && ni < N && !checked[ni][nj] && circles[ni][nj] == tmp) {
                                q.add(new int[]{ni, nj});
                                checked[ni][nj] = true;
                                cnt += 1;
                                circles[ni][nj] = 0;
                                ssum -= tmp;
                            }
                        }
                    }
                    if (cnt > 1) {
                        circles[i][j] = 0;
                        ssum -= tmp;
                        rest -= cnt;
                        val = true;
                    }
                }
            }
        }
        return val;
    }
}