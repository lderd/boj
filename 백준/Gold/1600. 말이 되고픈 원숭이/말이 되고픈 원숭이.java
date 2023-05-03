import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());
        StringTokenizer stWH = new StringTokenizer(br.readLine());
        int W = Integer.parseInt(stWH.nextToken());
        int H = Integer.parseInt(stWH.nextToken());
        int[][] arr = new int[H][W];
        for (int i = 0; i < H; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < W; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        if (H == 1 & W == 1) {
            System.out.println(0);
        } else {

            boolean[][][] checked = new boolean[H][W][K+1];
            checked[0][0][0] = true;
            int[][] directionHorse = {{-2, -1}, {-2, 1}, {-1, 2}, {1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}};
            int[][] directionMonkey = {{0, -1}, {-1, 0}, {1, 0}, {0, 1}};
            int[] start = {0, 0, 0, 0};
            Queue<int[]> Q = new LinkedList<>();
            Q.add(start);
            int answer = -1;
            while (!Q.isEmpty()) {
                int[] c = Q.poll();
                if (c[2] < K) {
                    for (int d = 0; d < 8; d++) {
                        int[] n = {c[0] + directionHorse[d][0], c[1] + directionHorse[d][1], c[2] + 1, c[3] + 1};
                        if (n[0] >= 0 & n[0] < H & n[1] >= 0 & n[1] < W) {
                            if (n[0] == H-1 & n[1] == W-1) {
                                answer = n[3];
                                break;
                            }
                            if (!checked[n[0]][n[1]][c[2]+1] && arr[n[0]][n[1]] == 0) {
                                checked[n[0]][n[1]][c[2]+1] = true;
                                Q.add(n);
                            }
                        }
                    }
                }
                for (int d = 0; d < 4; d++) {
                    int[] n = {c[0] + directionMonkey[d][0], c[1] + directionMonkey[d][1], c[2], c[3] + 1};
                    if (n[0] >= 0 & n[0] < H & n[1] >= 0 & n[1] < W) {
                        if (n[0] == H-1 & n[1] == W-1) {
                            answer = n[3];
                            break;
                        }
                        if (!checked[n[0]][n[1]][c[2]] && arr[n[0]][n[1]] == 0) {
                            checked[n[0]][n[1]][c[2]] = true;
                            Q.add(n);
                        }
                    }
                }
                if (answer >= 0) {
                    break;
                }
            }
            System.out.println(answer);
        }
    }
}