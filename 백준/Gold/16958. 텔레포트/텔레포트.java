import java.io.*;
import java.util.*;

public class Main {
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());
        HashMap<Integer, int[]> arr = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int s, x, y;
            st = new StringTokenizer(br.readLine());
            s = Integer.parseInt(st.nextToken());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            arr.put(i, new int[]{s, x, y});
        }

        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], 10000000);
        }

        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                if (i == j) continue;
                int[] iCity = arr.get(i);
                int[] jCity = arr.get(j);
                dist[i][j] = Math.abs(iCity[1] - jCity[1]) + Math.abs(iCity[2] - jCity[2]);
                if (iCity[0] == 1 && jCity[0] == 1 && t < dist[i][j]) {
                    dist[i][j] = t;
                }
                dist[j][i] = dist[i][j];
            }
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                if (i == k) continue;
                for (int j = 0; j < n; j++) {
                    if (i == j || j == k) continue;
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }

        int m = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            System.out.println(dist[a-1][b-1]);
        }
    }
}