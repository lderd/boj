import com.sun.source.tree.BreakTree;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int answer = 1;
    static int[][] d = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
    static int[][] arr, checked;
    public static void main(String[]args) throws java.io.IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n][n];
        checked = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int boo = Integer.parseInt(st.nextToken());
                arr[i][j] = boo;
                checked[i][j] = 1;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dfs(i, j);
                if (checked[i][j] > answer) {
                    answer = checked[i][j];
                }
            }
        }
        System.out.println(answer);
    }
    static int dfs(int i, int j) {
        if (checked[i][j] > 1) {
            return checked[i][j];
        }
        for (int k = 0; k < 4; k++) {
            int ni = i + d[k][0];
            int nj = j + d[k][1];
            if (0 <= ni & ni < n & 0 <= nj & nj < n) {
                if (arr[ni][nj] > arr[i][j]) {
                    checked[i][j] = Math.max(checked[i][j], dfs(ni, nj) + 1);
                }
            }
        }
        return checked[i][j];
    }
}