import java.io.*;
import java.util.*;

public class Main {
    static int[][] memo;
    static int[] fileSum;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int k = Integer.parseInt(br.readLine());
            memo = new int[k][k];
            fileSum = new int[k + 1];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < k; j++) {
                int oneFile = Integer.parseInt(st.nextToken());
                int index = j + 1;
                while (index <= k) {
                    fileSum[index] += oneFile;
                    index += index & -index;
                }
            }
            for (int j = 0; j < k; j++) {
                dp(0, j);
            }
            System.out.println(memo[0][k-1]);
        }
    }
    public static int dp(int s, int e) {
        if (memo[s][e] > 0) {
            return memo[s][e];
        }
        if (s == e) {
            return 0;
        }
        if (s + 1 == e) {
            memo[s][e] = getFileSum(e) - getFileSum(s - 1);
            return memo[s][e];
        }
        int result = 987654321;
        for (int i = s; i < e; i++) {
            int tmp = dp(s, i) + dp(i+1, e) + getFileSum(e) - getFileSum(s - 1);
            if (tmp < result) {
                result = tmp;
            }
        }
        memo[s][e] = result;
        return memo[s][e];
    }
    public static int getFileSum(int e) {
        int result = 0;
        int index = e + 1;
        while (index > 0) {
            result += fileSum[index];
            index -= index & -index;
        }
        return result;
    }
}