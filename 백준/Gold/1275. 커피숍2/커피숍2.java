import java.io.*;
import java.util.*;

public class Main {
    static long[] arr, tree;
    static int N, Q;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stNQ = new StringTokenizer(br.readLine());
        N = Integer.parseInt(stNQ.nextToken());
        Q = Integer.parseInt(stNQ.nextToken());
        arr = new long[N+1];
        tree = new long[N+1];
        StringTokenizer stArr = new StringTokenizer(br.readLine());
        for (int i = 1; i < N+1; i++) {
            long tmp = Long.parseLong(stArr.nextToken());
            update(i, tmp);
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = 0; i < Q; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            long b = Long.parseLong(st.nextToken());
            if (x > y) {
                int tmp = x;
                x = y;
                y = tmp;
            }
            bw.write(String.valueOf(sum(y) - sum(x-1)));
            bw.newLine();
            update(a, b);
        }
        bw.close();
    }
    static long sum(int index) {
        long val = 0;
        while (index > 0) {
            val += tree[index];
            index -= index & -index;
        }
        return val;
    }
    static void update(int a, long b) {
        long gap = b - arr[a];
        arr[a] = b;
        while (a <= N) {
            tree[a] += gap;
            a += a & -a;
        }
    }
}