import java.io.*;
import java.util.*;

public class Main {
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        ArrayList<int[]>[] arr = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            arr[i] = new ArrayList<>();
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken());
            arr[a].add(new int[]{b, c});
            arr[b].add(new int[]{a, c});
        }
        st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken()) - 1;
        int e = Integer.parseInt(st.nextToken()) - 1;
        PriorityQueue<int[]> q = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] == o2[0]) {
                    return o1[1] - o2[1];
                }
                return o2[0] - o1[0];
            }
        });
        int[] limit = new int[N];
        Arrays.fill(limit, 0);
        for (int i = 0; i < arr[s].size(); i++) {
            int[] road = arr[s].get(i);
            if (limit[road[0]] < road[1]) {
                limit[road[0]] = road[1];
                q.add(new int[]{road[1], road[0]});
            }
        }
        while (!q.isEmpty()) {
            int[] info = q.poll();
            if (info[0] < limit[info[1]]) continue;
            for (int i = 0; i < arr[info[1]].size(); i++) {
                int[] hubo = arr[info[1]].get(i);
                int newLimit = Math.min(info[0], hubo[1]);
                if (newLimit > limit[hubo[0]]) {
                    limit[hubo[0]] = newLimit;
                    q.add(new int[]{newLimit, hubo[0]});
                }
            }
        }
        System.out.println(limit[e]);
    }
}