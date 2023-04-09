import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[]args) throws java.io.IOException{
        int N, M;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stNM = new StringTokenizer(br.readLine());
        N = Integer.parseInt(stNM.nextToken());
        M = Integer.parseInt(stNM.nextToken());
        int[][] arr = new int[N][2];
        StringTokenizer stMemory = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i][0] = Integer.parseInt(stMemory.nextToken());
        }
        int maxCost = 0;
        StringTokenizer stCost = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int tmp = Integer.parseInt(stCost.nextToken());
            arr[i][1] = tmp;
            maxCost += tmp;
        }
        int[][] memo = new int[N + 1][maxCost + 2];
        int answer = 10000001;
        for (int i = 0; i < N; i++) {
            for (int j = 1; j < maxCost + 2; j++) {
                if (j - 1 >= arr[i][1]) {
                    memo[i+1][j] = Math.max(memo[i][j], Math.max(memo[i+1][j-1], memo[i][j-arr[i][1]] + arr[i][0]));
                    if (memo[i+1][j] >= M & j - 1 < answer) {
                        answer = j - 1;
                    }
                } else {
                    memo[i+1][j] = Math.max(memo[i][j], memo[i+1][j-1]);
                }
            }
        }
        System.out.println(answer);
    }
}