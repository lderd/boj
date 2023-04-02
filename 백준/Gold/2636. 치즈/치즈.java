import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[]args) throws java.io.IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        final int N = Integer.parseInt(st.nextToken());
        final int M = Integer.parseInt(st.nextToken());
        int[][] arr = new int[N][M];
        int cheese = 0;
        for (int i = 0; i < N; i++) {
            StringTokenizer st1 = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int tmp = Integer.parseInt(st1.nextToken());
                if (tmp == 1) {
                    cheese += 1;
                    arr[i][j] = 1;
                }
            }
        }
        int cnt = 0;
        int[][] d = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while (cheese > 0) {
            cnt += 1;
            Queue<int[]> q = new LinkedList<>();
            boolean[][] checked = new boolean[N][M];
            checked[0][0] = true;
            int melt = 0;
            int[] start = {0, 0};
            q.add(start);
            while (!q.isEmpty()) {
                int[] popq = q.poll();
                for (int i = 0; i < 4; i++) {
                    int ni = popq[0] + d[i][0];
                    int nj = popq[1] + d[i][1];
                    if (0 <= ni & ni < N & 0 <= nj & nj < M) {
                         if (!checked[ni][nj]) {
                            checked[ni][nj] = true;
                            if (arr[ni][nj] == 1){
                                arr[ni][nj] = 0;
                                melt += 1;
                            } else {
                                int[] next = {ni, nj};
                                q.add(next);
                            }
                         }
                    }
                }
            }
            if (cheese == melt) {
                System.out.println(cnt);
                System.out.println(melt);
            }
            cheese -= melt;
        }
    }
}