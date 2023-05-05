//https://www.acmicpc.net/problem/1079
import java.io.*;
import java.util.*;

public class Main {
    static int[][] R;
    static boolean[] dead;
    static int[] guiltyScore;
    static int answer, N, me;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer stG = new StringTokenizer(br.readLine());
        answer = 0;
        guiltyScore = new int[N];
        for (int i = 0; i < N; i++) {
            guiltyScore[i] = Integer.parseInt(stG.nextToken());
        }
        R = new int[N][N];
        dead = new boolean[N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                R[i][j]= Integer.parseInt(st.nextToken());
            }
        }
        me = Integer.parseInt(br.readLine());
        if (N > 1) {
            dfs(N, 0);
        }
        System.out.println(answer);
    }
    static void dfs(int restGamer,int night) {
        if (restGamer % 2 ==  1) {
            int guilty = 0;
            int bigScore = 0;
            for (int i = 0; i < N; i++) {
                if (!dead[i] & bigScore < guiltyScore[i]) {
                    bigScore = guiltyScore[i];
                    guilty = i;
                }
            }
            if (guilty != me) {
                dead[guilty] = true;
                dfs(restGamer - 1, night);
                dead[guilty] = false;
            }
        } else {
            if (night + 1 > answer) {
                answer = night + 1;
            }
            if (restGamer <= 2) {
                return;
            }
            for (int i = 0; i < N; i++) {
                if (!dead[i] & i != me) {
                    dead[i] = true;
                    for (int j = 0; j < N; j++) {
                        guiltyScore[j] += R[i][j];
                    }
                    dfs(restGamer - 1, night + 1);
                    dead[i] = false;
                    for (int j = 0; j < N; j++) {
                        guiltyScore[j] -= R[i][j];
                    }
                }
            }
        }
    }
}