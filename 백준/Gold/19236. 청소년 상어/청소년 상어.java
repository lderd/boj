import java.io.*;
import java.util.*;

public class Main {
    static int[][] direction = {{-1, 0}, {-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}};
    static int answer = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] space = new int[4][4];
        int[][] fish = new int[17][3];
        for (int i = 0; i < 4; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; j++) {
                int fishNum = Integer.parseInt(st.nextToken());
                int fishD = Integer.parseInt(st.nextToken()) - 1;
                space[i][j] = fishNum;
                fish[fishNum][0] = i;
                fish[fishNum][1] = j;
                fish[fishNum][2] = fishD;
            }
        }
        answer += space[0][0];
        fish[0] = fish[space[0][0]];
        fish[space[0][0]] = new int[3];
        fish[space[0][0]][2] = -1;
        space[0][0] = -1;
        move(space, fish, answer);
        System.out.println(answer);
    }
    static void move(int[][] spaceInfo, int[][] fishInfo, int cnt) {
        if (cnt > answer) {
            answer = cnt;
        }
        int[][] newSpace = new int[4][4];
        for (int i = 0; i < 4; i++) {
            newSpace[i] = Arrays.copyOf(spaceInfo[i], 4);
        }
        int[][] newFish = new int[17][3];
        for (int i = 0; i < 17; i++) {
            newFish[i] = Arrays.copyOf(fishInfo[i], 3);
        }
//        물고기 이동
        for (int i = 1; i < 17; i++) {
            if (newFish[i][2] > -1) {
                for (int j = 0; j < 8; j++) {
                    int d = (newFish[i][2] + j) % 8;
                    int ni = newFish[i][0] + direction[d][0];
                    int nj = newFish[i][1] + direction[d][1];
                    if (0 <= ni && ni < 4 && 0 <= nj && nj < 4 && newSpace[ni][nj] > -1) {
                        if (newSpace[ni][nj] == 0) {
                            newSpace[newFish[i][0]][newFish[i][1]] = 0;
                            newSpace[ni][nj] = i;
                            newFish[i][0] = ni;
                            newFish[i][1] = nj;
                            newFish[i][2] = d;
                        } else {
                            newFish[newSpace[ni][nj]][0] = newFish[i][0];
                            newFish[newSpace[ni][nj]][1] = newFish[i][1];
                            newSpace[newFish[i][0]][newFish[i][1]] = newSpace[ni][nj];
                            newSpace[ni][nj] = i;
                            newFish[i][0] = ni;
                            newFish[i][1] = nj;
                            newFish[i][2] = d;
                        }
                        break;
                    }
                }
            }
        }
//        상어가 1~3칸 이동
        for (int i = 1; i < 4; i++) {
            int ni = newFish[0][0] + direction[newFish[0][2]][0] * i;
            int nj = newFish[0][1] + direction[newFish[0][2]][1] * i;
            if (0 <= ni && ni < 4 && 0 <= nj && nj < 4 && newSpace[ni][nj] > 0) {
                int[][] tmpSpace = new int[4][4];
                for (int j = 0; j < 4; j++) {
                    tmpSpace[j] = Arrays.copyOf(newSpace[j], 4);
                }
                int[][] tmpFish = new int[17][3];
                for (int j = 0; j < 17; j++) {
                    tmpFish[j] = Arrays.copyOf(newFish[j], 3);
                }
                int newCnt = cnt + tmpSpace[ni][nj];
                tmpSpace[tmpFish[0][0]][tmpFish[0][1]] = 0;
                tmpFish[0][0] = ni;
                tmpFish[0][1] = nj;
                tmpFish[0][2] = tmpFish[tmpSpace[ni][nj]][2];
                tmpFish[tmpSpace[ni][nj]] = new int[3];
                tmpFish[tmpSpace[ni][nj]][2] = -1;
                tmpSpace[ni][nj] = -1;
                move(tmpSpace, tmpFish, newCnt);
            }
        }
    }
}