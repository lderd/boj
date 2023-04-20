import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stNM = new StringTokenizer(br.readLine());
        final int n = Integer.parseInt(stNM.nextToken());
        final int m = Integer.parseInt(stNM.nextToken());
        int[] arr = new int[n + 1];
        long[] tree = new long[n + 1];
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int mm = 0; mm < m; mm++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int operator = Integer.parseInt(st.nextToken());
            if (operator == 0) {
                int i = Integer.parseInt(st.nextToken());
                int j = Integer.parseInt(st.nextToken());
                long answer = 0;
                if (i > j) {
                    while (i > 0) {
                        answer += tree[i];
                        i -= i & -i;
                    }
                    j -= 1;
                    while (j > 0) {
                        answer -= tree[j];
                        j -= j & -j;
                    }
                } else {
                    while (j > 0) {
                        answer += tree[j];
                        j -= j & -j;
                    }
                    i -= 1;
                    while (i > 0) {
                        answer -= tree[i];
                        i -= i & -i;
                    }
                }
                bw.write(String.valueOf(answer));
                bw.newLine();
            } else {
                int i = Integer.parseInt(st.nextToken());
                int k = Integer.parseInt(st.nextToken());
                int gap = k - arr[i];
                arr[i] = k;
                while (i <= n) {
                    tree[i] += gap;
                    i += i & -i;
                }
            }
        }
        bw.close();
    }
}