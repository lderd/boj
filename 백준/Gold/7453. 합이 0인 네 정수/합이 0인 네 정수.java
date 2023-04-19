import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] A = new int[n];
        int[] B = new int[n];
        int[] C = new int[n];
        int[] D = new int[n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; j++) {
                if (j == 0) {
                    A[i] = Integer.parseInt(st.nextToken());
                } else if (j == 1) {
                    B[i] = Integer.parseInt(st.nextToken());
                } else if (j == 2) {
                    C[i] = Integer.parseInt(st.nextToken());
                } else {
                    D[i] = Integer.parseInt(st.nextToken());
                }
            }
        }
        long[] sumAB = new long[n * n];
        long[] sumCD = new long[n * n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sumAB[i * n + j] = A[i] + B[j];
                sumCD[i * n + j] = (C[i] + D[j]) * (-1);
            }
        }
        Arrays.sort(sumAB);
        Arrays.sort(sumCD);
        long answer = 0;
        int i = 0;
        int j = 0;
        while (i < n * n & j < n * n) {
            if (sumAB[i] > sumCD[j]) {
                j += 1;
            } else if (sumAB[i] < sumCD[j]) {
                i += 1;
            } else {
                int tmpI = 1;
                int tmpJ = 1;
                while (i + tmpI < n * n) {
                    if (sumAB[i] == sumAB[i + tmpI]) {
                        tmpI += 1;
                    } else {
                        break;
                    }
                }
                while (j + tmpJ < n * n) {
                    if (sumCD[j] == sumCD[j + tmpJ]) {
                        tmpJ += 1;
                    } else {
                        break;
                    }
                }
                answer += (long) tmpI * tmpJ;
                i += tmpI;
                j += tmpJ;
            }
        }
        System.out.println(answer);
    }
}