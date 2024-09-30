import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int[][] arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int[] dp = new int[1<<N];
        Set<Integer> q = new HashSet<>();
        for (int i = 0; i < N; i++) {
            dp[1<<i] = arr[0][i];
            q.add(1<<i);
        }
        for (int i = 1; i < N; i++) {
            Set<Integer> tmp_q = new HashSet<>();
            for (int j = 0; j < N; j++) {
                for (int before_bit:q) {
                    if ((before_bit & (1<<j)) == 0) {
                        int new_bit = before_bit + (1<<j);
                        if ((dp[new_bit] == 0) || (dp[before_bit] + arr[i][j] < dp[new_bit])) {
                            dp[new_bit] = dp[before_bit] + arr[i][j];
                            tmp_q.add(new_bit);
                        }
                    }
                }
            }
            q = tmp_q;
        }
        System.out.println(dp[(1<<N) - 1]);
    }
}