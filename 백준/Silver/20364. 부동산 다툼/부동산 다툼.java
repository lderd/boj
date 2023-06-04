import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stNQ = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stNQ.nextToken());
        boolean[] tree = new boolean[n + 1];
        int q = Integer.parseInt(stNQ.nextToken());
        for (int i = 0; i < q; i++) {
            int x = Integer.parseInt(br.readLine());
            int index = x;
            int answer = 0;
            while (index > 1) {
                if (tree[index]) {
                    answer = index;
                }
                index /= 2;
            }
            if (answer == 0) {
                tree[x] = true;
            }
            System.out.println(answer);
        }
    }
}