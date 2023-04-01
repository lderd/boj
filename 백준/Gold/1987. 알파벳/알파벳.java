import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[]args) throws java.io.IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        final int R = Integer.parseInt(st.nextToken());
        final int C = Integer.parseInt(st.nextToken());
        String[] arr = new String[R];
        for (int i = 0; i < R; i++) {
            arr[i] = br.readLine();
        }
        String alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
//             r, c, bit, cnt
        Queue<int[]> q = new LinkedList<>();
        int[] start = {0, 0, 1 << alphas.indexOf(String.valueOf(arr[0].charAt(0))), 1};
        q.add(start);
        final int[][] d = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int answer = 0;
        Set<Integer>[][] checked = new HashSet[R][C];
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                checked[i][j] = new HashSet<>();
            }
        }
        checked[0][0].add(1 << alphas.indexOf(String.valueOf(arr[0].charAt(0))));
        while (!q.isEmpty()) {
            int[] rcbit = q.poll();
            if (rcbit[3] > answer) {
                answer = rcbit[3];
            }
            for (int i = 0; i < 4; i++) {
                int nr = rcbit[0] + d[i][0];
                int nc = rcbit[1] + d[i][1];
                if (0 <= nr & nr < R & 0 <= nc & nc < C) {
                    if ((rcbit[2] & (1 << alphas.indexOf(String.valueOf(arr[nr].charAt(nc))))) == 0 & !checked[nr][nc].contains(rcbit[2])) {
                        int[] nrcbit = {nr, nc, rcbit[2] + (1 << alphas.indexOf(String.valueOf(arr[nr].charAt(nc)))), rcbit[3] + 1};
                        checked[nr][nc].add(rcbit[2]);
                        q.add(nrcbit);
                    }
                }
            }
        }
        System.out.println(answer);
    }
}