import java.io.*;
import java.util.*;

public class Main {
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(arr[i], 0);
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a-1][b-1] = 1;
            arr[b-1][a-1] = 1;
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                if (k == i) continue;
                for (int j = 0; j < n; j++) {
                    if (i == j || k == j) continue;
                    if (arr[i][k] != 0 && arr[k][j] != 0) {
                        if (arr[i][j] == 0) {
                            arr[i][j] = arr[i][k] + arr[k][j];
                        } else if (arr[i][j] > arr[i][k] + arr[k][j]) {
                            arr[i][j] = arr[i][k] + arr[k][j];
                        }
                    }
                }
            }
        }
        int answer = 0;
        int number = 10000000;
        for (int i = 0; i < n; i++) {
            int bigNum = 0;
            for (int j = 0; j < n; j++) {
                bigNum += arr[i][j];
            }
            if (number > bigNum) {
                number = bigNum;
                answer = i + 1;
            }
        }
        System.out.println(answer);
    }
}