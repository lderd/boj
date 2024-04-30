import java.io.*;
import java.util.*;

public class Main {
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int fuel = Integer.parseInt(st.nextToken());
        int[][] city = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                city[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int[] texi = new int[2];
        int[][][] info = new int[N][N][3];
        st = new StringTokenizer(br.readLine());
        texi[0] = Integer.parseInt(st.nextToken()) - 1;
        texi[1] = Integer.parseInt(st.nextToken()) - 1;
        int[] di = {-1, 0, 0, 1};
        int[] dj = {0, -1, 1, 0};
        for (int i = 2; i < M+2; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;
            int d = Integer.parseInt(st.nextToken()) - 1;
            city[a][b] = i;
            info[a][b][0] = c;
            info[a][b][1] = d;
            Queue<int[]> q = new LinkedList<>();
            q.add(new int[]{a, b, 0});
            boolean[][] checked = new boolean[N][N];
            for (int j = 0; j < N; j++) {
                Arrays.fill(checked[j], true);
            }
            checked[a][b] = false;
            while (!q.isEmpty() && info[a][b][2] == 0) {
                int[] now = q.poll();
                for (int j = 0; j < 4; j++) {
                    int ni = now[0] + di[j];
                    int nj = now[1] + dj[j];
                    if (0 <= ni && ni < N && 0 <= nj && nj < N && city[ni][nj] != 1 && checked[ni][nj]) {
                        if (ni == c && nj == d) {
                            info[a][b][2] = now[2] + 1;
                            break;
                        }
                        q.add(new int[]{ni, nj, now[2]+1});
                        checked[ni][nj] = false;
                    }
                }
            }
            if (info[a][b][2] == 0) info[a][b][2] = 1000000000;
        }
        for (int i = 0; i < M; i++) {
            Queue<int[]> q = new LinkedList<>();
            q.add(new int[]{texi[0], texi[1], 0});
            boolean[][] checked = new boolean[N][N];
            for (int j = 0; j < N; j++) {
                Arrays.fill(checked[j], true);
            }
            checked[texi[0]][texi[1]] = false;
            int[] passenger = {21, 21, 1000000000};
            if (city[texi[0]][texi[1]] > 1) {
                passenger = new int[]{texi[0], texi[1], 0};
            }
            while (!q.isEmpty()) {
                int[] now = q.poll();
                if (now[2] >= passenger[2]) break;
                for (int j = 0; j < 4; j++) {
                    int ni = now[0] + di[j];
                    int nj = now[1] + dj[j];
                    if (0 <= ni && ni < N && 0 <= nj && nj < N && checked[ni][nj] && city[ni][nj] != 1) {
                        checked[ni][nj] = false;
                        if (city[ni][nj] == 0) {
                            q.add(new int[]{ni, nj, now[2]+1});
                        } else {
                            if (ni < passenger[0] || (ni == passenger[0] && nj < passenger[1])) {
                                passenger = new int[]{ni, nj, now[2] + 1};
                            }
                        }
                    }
                }
            }
            if (passenger[0] > N || passenger[1] > N || fuel < passenger[2] + info[passenger[0]][passenger[1]][2]) {
                fuel = -1;
                break;
            } else {
                fuel -= passenger[2] - info[passenger[0]][passenger[1]][2];
                city[passenger[0]][passenger[1]] = 0;
                passenger[2] = 0;
                texi[0] = info[passenger[0]][passenger[1]][0];
                texi[1] = info[passenger[0]][passenger[1]][1];
            }
        }
        System.out.println(fuel);
    }
}