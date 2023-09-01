import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int[] pList = new int[100001];
        Arrays.fill(pList, 0);
        PriorityQueue<int[]> hard = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0]==o2[0]) return o2[1]-o1[1];
                return o2[0]-o1[0];
            }
        });
        PriorityQueue<int[]> easy = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0]==o2[0]) return o1[1]-o2[1];
                return o1[0]-o2[0];
            }
        });
        int n = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int pNo = Integer.parseInt(st.nextToken());
            int level = Integer.parseInt(st.nextToken());
            pList[pNo] = level;
            hard.add(new int[]{level, pNo});
            easy.add(new int[]{level, pNo});
        }
        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            if (Objects.equals(command, "add")) {
                int pNo = Integer.parseInt(st.nextToken());
                int level = Integer.parseInt(st.nextToken());
                pList[pNo] = level;
                int[] LP = { level, pNo };
                hard.add(LP);
                easy.add(LP);
            } else if (Objects.equals(command, "recommend")) {
                int l = Integer.parseInt(st.nextToken());
                while (true) {
                    int[] LP;
                    if (l == -1) {
                        LP = easy.peek();
                    } else {
                        LP = hard.peek();
                    }
                    assert LP != null;
                    if (LP[0] == pList[LP[1]]) {
                        System.out.println(LP[1]);
                        break;
                    } else {
                        if (l == -1) {
                            easy.poll();
                        } else {
                            hard.poll();
                        }
                    }
                }
            } else {
                int p = Integer.parseInt(st.nextToken());
                pList[p] = 0;
            }
        }
    }
}