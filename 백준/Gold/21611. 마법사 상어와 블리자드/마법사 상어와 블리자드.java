import java.io.*;
import java.util.*;

public class Main {
    static int N, answer;
    static int[] ball;
    static int[][] arr;
    static int[][] blizzard_d = {{}, {-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stNM = new StringTokenizer(br.readLine());
        N = Integer.parseInt(stNM.nextToken());
        int M = Integer.parseInt(stNM.nextToken());
        arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer stArr = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(stArr.nextToken());
            }
        }
        ball = new int[N*N - 1];
        int[][] direction = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}};

        boolean[][] checked = new boolean[N][N];
        checked[N/2][N/2] = true;

        ball[0] = arr[N/2][N/2-1];
        arr[N/2][N/2-1] = 0;
        checked[N/2][N/2-1] = true;

        int index = 1;
        int i = N / 2 + 1;
        int j = N / 2 - 1;
        int d = 1;

        while (i > -1 & i < N & j > -1 & j < N) {
            ball[index] = arr[i][j];
            checked[i][j] = true;
            arr[i][j] = index;
            index += 1;
            int ni = i + direction[(d + 1) % 4][0];
            int nj = j + direction[(d + 1) % 4][1];
            if (checked[ni][nj]) {
                ni = i + direction[d][0];
                nj = j + direction[d][1];
            } else {
                d = (d + 1) % 4;
            }
            i = ni;
            j = nj;
        }
        for (int k = 0; k < M; k++) {
            StringTokenizer spell = new StringTokenizer(br.readLine());
            int magicD = Integer.parseInt(spell.nextToken());
            int s = Integer.parseInt(spell.nextToken());
            blizzard(magicD, s);
            move();
            ballSplit();
        }
        System.out.println(answer);
    }
//    마법을 쓰면 리스트에서 마법이 사용된 위치를 0으로
    static void blizzard(int d, int s) {
        int i = N / 2;
        int j = N / 2;
        int index = -1;
        for (int k = 0; k < s; k++) {
            i += blizzard_d[d][0];
            j += blizzard_d[d][1];
            index = arr[i][j];
            ball[index] = 0;
        }
    }
//    빈 칸 없애면서 폭파
    static void move() {
        int boomCnt = 1;
        while (boomCnt >= 1) {
            boomCnt = 0;
            int[] tmp = new int[N*N-1];
            int tmpIndex = 0;
            List<Integer> Q = new LinkedList<>();
            for (int i = 0; i < N*N-1; i++) {
    //            0이 아니면(터진위치 or 블라자드 맞은 위치가 아니면)
                if (ball[i] > 0) {
                    if (Q.isEmpty()) {
                        Q.add(ball[i]);
                    } else {
    //                    Q에 들어있는거랑 같으면 Q에 넣고
                        if (Q.get(0) == ball[i]) {
                            Q.add(ball[i]);
    //                        Q에 들어있는거랑 다를때
                        } else {
    //                        폭파시킨다면 폭파
                            if (Q.size() >= 4) {
                                answer += Q.get(0) * Q.size();
                                boomCnt += 1;
                                Q = new LinkedList<>();
                            } else {
    //                            폭파시키지 않을거면
                                for (int num: Q) {
                                    tmp[tmpIndex] = num;
                                    tmpIndex += 1;
                                }
                                Q = new LinkedList<>();
                            }
                            Q.add(ball[i]);
                        }
                    }
                }
            }
            if (!Q.isEmpty()) {
                if (Q.size() >= 4) {
                    answer += Q.get(0) * Q.size();
                    boomCnt += 1;
                } else {
    //               폭파시키지 않을거면
                    for (int num: Q) {
                        tmp[tmpIndex] = num;
                        tmpIndex += 1;
                    }
                }
            }
            ball = tmp;
        }
    }
    static void ballSplit() {
        int[] tmp = new int[N*N-1];
        int index = 0;
        List<Integer> Q = new LinkedList<>();
        for (int i = 0; i < N*N-1; i++) {
            if (index >= N*N - 1) {
                break;
            }
            if (ball[i] > 0) {
                if (Q.isEmpty()) {
                    Q.add(ball[i]);
                } else {
                    if (Q.get(0) == ball[i]) {
                        Q.add(ball[i]);
                    } else {
                        tmp[index] = Q.size();
                        if (index + 1 < N*N - 1) {
                            tmp[index + 1] = Q.get(0);
                        }
                        index += 2;
                        Q = new LinkedList<>();
                        Q.add(ball[i]);
                    }
                }
            }
        }
        if (!Q.isEmpty()) {
            if (index < N*N - 1) {
                tmp[index] = Q.size();
                if (index + 1 < N*N - 1) {
                    tmp[index + 1] = Q.get(0);
                }
            }
        }
        ball = tmp;
    }
}