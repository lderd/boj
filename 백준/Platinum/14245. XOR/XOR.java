import java.io.*;
import java.util.*;

public class Main {
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int[] tree = new int[n+1];
        Arrays.fill(tree, 0);
        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int q = Integer.parseInt(st.nextToken());
            if (q == 1) {
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                a += 1;
                b += 2;
                while (a <= n) {
                    tree[a] ^= c;
                    a += a & (-a);
                }
                while (b <= n) {
                    tree[b] ^= c;
                    b += b & (-b);
                }
            } else {
                int c = Integer.parseInt(st.nextToken());
                int answer = arr[c];
                c += 1;
                while (c > 0) {
                    answer ^= tree[c];
                    c -= c & (-c);
                }
                System.out.println(answer);
            }
        }
    }
}