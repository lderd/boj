import java.io.*;
import java.util.*;

public class Main {
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            int[][] scores = new int[N][2];
            for (int j = 0; j < N; j++) {
                st = new StringTokenizer(br.readLine());
                scores[j][0] = Integer.parseInt(st.nextToken());
                scores[j][1] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(scores, new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    if (o1[0] == o2[0]) return o2[1] - o1[1];
                    return o2[0] - o1[0];
                }
            });
            PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
            for (int j = 0; j < N; j++) {
                int score = scores[j][1];
                q.add(score);
                while (q.peek() != score) {
                    q.poll();
                }
            }
            System.out.println(q.size());
        }
    }
}