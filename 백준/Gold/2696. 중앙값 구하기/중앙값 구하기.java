import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        for (int i = 0; i < T; i++) {
            solve();
        }
    }
    static void solve() throws IOException {
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        System.out.println(N/2 + 1);
        PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder());
        int smallLen = 0;
        PriorityQueue<Integer> big = new PriorityQueue<>();
        int bigLen = 0;
        int idx = 0;
        int mid;
        st = new StringTokenizer(br.readLine());
        mid = Integer.parseInt(st.nextToken());
        System.out.print(mid + " ");
        for (int i = 0; i <= N/10; i++) {
            while (st.hasMoreTokens()) {
                int now = Integer.parseInt(st.nextToken());
                if (now <= mid) {
                    small.add(now);
                    smallLen += 1;
                } else {
                    big.add(now);
                    bigLen += 1;
                }
                int gap = smallLen - bigLen;
                if (gap < -1) {
                    small.add(mid);
                    mid = big.poll();
                    bigLen -= 1;
                    smallLen += 1;
                } else if (gap > 1) {
                    big.add(mid);
                    mid = small.poll();
                    bigLen += 1;
                    smallLen -= 1;
                }
                if (idx % 2 == 1) {
                    System.out.print(mid + " ");
                }
                idx += 1;
            }
            if (idx < N - 1) {
                st = new StringTokenizer(br.readLine());
            }
        }
        System.out.println();
    }
}