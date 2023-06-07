import java.io.*;
import java.util.*;

public class Main {
    static class inq {
        int[] r, b;
        String cnt;
        inq(int[] r, int[] b, String cnt){
            this.r = r;
            this.b = b;
            this.cnt = cnt;
        }
    }
    static String[][] board;
    static int[][] direction = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
    static boolean[][][][] checked;
    static Queue<inq> q = new LinkedList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stNM = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stNM.nextToken());
        int m = Integer.parseInt(stNM.nextToken());
        board = new String[n][m];
        checked = new boolean[n][m][n][m];
        int[][] balls = new int[2][2];
        for (int i = 0; i < n; i++) {
            String st = br.readLine();
            for (int j = 0; j < m; j++) {
                String tmp = Character.toString(st.charAt(j));
                if (tmp.equals("B")) {
                    balls[1] = new int[]{i, j};
                    board[i][j] = ".";
                } else if (tmp.equals("R")) {
                    balls[0] = new int[]{i, j};
                    board[i][j] = ".";
                } else {
                    board[i][j] = tmp;
                }
            }
        }
        checked[balls[0][0]][balls[0][1]][balls[1][0]][balls[1][1]] = true;
        q.add(new inq(balls[0], balls[1], ""));
        boolean flag = false;
        while (!q.isEmpty()) {
            inq now = q.poll();
            int[] cr = now.r;
            int[] cb = now.b;
            String ccnt = now.cnt;
            for (int d = 0; d < 4; d++) {
                boolean[] goal = new boolean[2];
                int[] nnr, nnb;
                String ncnt;
                if (d == 0) {
                    if (cr[1] < cb[1]) {
//                        레드 먼저 움직
                        int tmp = 1;
                        while (true) {
                            int[] nr = {cr[0] + direction[d][0] * tmp, cr[1] + direction[d][1] * tmp};
                            if (0 <= nr[0] && nr[0] < n && 0 <= nr[1] && nr[1] < m) {
                                if (board[nr[0]][nr[1]].equals("#")) {
                                    tmp -= 1;
                                    break;
                                } else if (board[nr[0]][nr[1]].equals("O")) {
                                    goal[0] = true;
                                    break;
                                }
                                tmp += 1;
                            }
                        }
                        nnr = new int[]{cr[0] + direction[d][0] * tmp, cr[1] + direction[d][1] * tmp};
                        tmp = 1;
                        while (true) {
                            int[] nb = {cb[0] + direction[d][0] * tmp, cb[1] + direction[d][1] * tmp};
                            if (0 <= nb[0] && nb[0] < n && 0 <= nb[1] && nb[1] < m) {
                                if (board[nb[0]][nb[1]].equals("#")) {
                                    tmp -= 1;
                                    break;
                                } else if (board[nb[0]][nb[1]].equals("O")) {
                                    goal[1] = true;
                                    break;
                                } else if (Arrays.equals(nb, nnr)) {
                                    tmp -= 1;
                                    break;
                                }
                                tmp += 1;
                            }
                        }
                        nnb = new int[]{cb[0] + direction[d][0] * tmp, cb[1] + direction[d][1] * tmp};
                    } else {
//                        블루 먼저 움직
                        int tmp = 1;
                        while (true) {
                            int[] nb = {cb[0] + direction[d][0] * tmp, cb[1] + direction[d][1] * tmp};
                            if (0 <= nb[0] && nb[0] < n && 0 <= nb[1] && nb[1] < m) {
                                if (board[nb[0]][nb[1]].equals("#")) {
                                    tmp -= 1;
                                    break;
                                } else if (board[nb[0]][nb[1]].equals("O")) {
                                    goal[1] = true;
                                    break;
                                }
                                tmp += 1;
                            }
                        }
                        nnb = new int[]{cb[0] + direction[d][0] * tmp, cb[1] + direction[d][1] * tmp};
                        tmp = 1;
                        while (true) {
                            int[] nr = {cr[0] + direction[d][0] * tmp, cr[1] + direction[d][1] * tmp};
                            if (0 <= nr[0] && nr[0] < n && 0 <= nr[1] && nr[1] < m) {
                                if (board[nr[0]][nr[1]].equals("#")) {
                                    tmp -= 1;
                                    break;
                                } else if (board[nr[0]][nr[1]].equals("O")) {
                                    goal[0] = true;
                                    break;
                                } else if (Arrays.equals(nnb, nr)) {
                                    tmp -= 1;
                                    break;
                                }
                                tmp += 1;
                            }
                        }
                        nnr = new int[]{cr[0] + direction[d][0] * tmp, cr[1] + direction[d][1] * tmp};
                    }
                    ncnt = ccnt + "L";
                } else if (d == 1) {
                    if (cr[1] > cb[1]) {
//                        레드 먼저 움직
                        int tmp = 1;
                        while (true) {
                            int[] nr = {cr[0] + direction[d][0] * tmp, cr[1] + direction[d][1] * tmp};
                            if (0 <= nr[0] && nr[0] < n && 0 <= nr[1] && nr[1] < m) {
                                if (board[nr[0]][nr[1]].equals("#")) {
                                    tmp -= 1;
                                    break;
                                } else if (board[nr[0]][nr[1]].equals("O")) {
                                    goal[0] = true;
                                    break;
                                }
                                tmp += 1;
                            }
                        }
                        nnr = new int[]{cr[0] + direction[d][0] * tmp, cr[1] + direction[d][1] * tmp};
                        tmp = 1;
                        while (true) {
                            int[] nb = {cb[0] + direction[d][0] * tmp, cb[1] + direction[d][1] * tmp};
                            if (0 <= nb[0] && nb[0] < n && 0 <= nb[1] && nb[1] < m) {
                                if (board[nb[0]][nb[1]].equals("#")) {
                                    tmp -= 1;
                                    break;
                                } else if (board[nb[0]][nb[1]].equals("O")) {
                                    goal[1] = true;
                                    break;
                                } else if (Arrays.equals(nb, nnr)) {
                                    tmp -= 1;
                                    break;
                                }
                                tmp += 1;
                            }
                        }
                        nnb = new int[]{cb[0] + direction[d][0] * tmp, cb[1] + direction[d][1] * tmp};
                    } else {
//                        블루 먼저 움직
                        int tmp = 1;
                        while (true) {
                            int[] nb = {cb[0] + direction[d][0] * tmp, cb[1] + direction[d][1] * tmp};
                            if (0 <= nb[0] && nb[0] < n && 0 <= nb[1] && nb[1] < m) {
                                if (board[nb[0]][nb[1]].equals("#")) {
                                    tmp -= 1;
                                    break;
                                } else if (board[nb[0]][nb[1]].equals("O")) {
                                    goal[1] = true;
                                    break;
                                }
                                tmp += 1;
                            }
                        }
                        nnb = new int[]{cb[0] + direction[d][0] * tmp, cb[1] + direction[d][1] * tmp};
                        tmp = 1;
                        while (true) {
                            int[] nr = {cr[0] + direction[d][0] * tmp, cr[1] + direction[d][1] * tmp};
                            if (0 <= nr[0] && nr[0] < n && 0 <= nr[1] && nr[1] < m) {
                                if (board[nr[0]][nr[1]].equals("#")) {
                                    tmp -= 1;
                                    break;
                                } else if (board[nr[0]][nr[1]].equals("O")) {
                                    goal[0] = true;
                                    break;
                                } else if (Arrays.equals(nnb, nr)) {
                                    tmp -= 1;
                                    break;
                                }
                                tmp += 1;
                            }
                        }
                        nnr = new int[]{cr[0] + direction[d][0] * tmp, cr[1] + direction[d][1] * tmp};
                    }
                    ncnt = ccnt + "R";
                } else if (d == 2) {
                    if (cr[0] < cb[0]) {
//                        레드 먼저 움직
                        int tmp = 1;
                        while (true) {
                            int[] nr = {cr[0] + direction[d][0] * tmp, cr[1] + direction[d][1] * tmp};
                            if (0 <= nr[0] && nr[0] < n && 0 <= nr[1] && nr[1] < m) {
                                if (board[nr[0]][nr[1]].equals("#")) {
                                    tmp -= 1;
                                    break;
                                } else if (board[nr[0]][nr[1]].equals("O")) {
                                    goal[0] = true;
                                    break;
                                }
                                tmp += 1;
                            }
                        }
                        nnr = new int[]{cr[0] + direction[d][0] * tmp, cr[1] + direction[d][1] * tmp};
                        tmp = 1;
                        while (true) {
                            int[] nb = {cb[0] + direction[d][0] * tmp, cb[1] + direction[d][1] * tmp};
                            if (0 <= nb[0] && nb[0] < n && 0 <= nb[1] && nb[1] < m) {
                                if (board[nb[0]][nb[1]].equals("#")) {
                                    tmp -= 1;
                                    break;
                                } else if (board[nb[0]][nb[1]].equals("O")) {
                                    goal[1] = true;
                                    break;
                                } else if (Arrays.equals(nb, nnr)) {
                                    tmp -= 1;
                                    break;
                                }
                                tmp += 1;
                            }
                        }
                        nnb = new int[]{cb[0] + direction[d][0] * tmp, cb[1] + direction[d][1] * tmp};
                    } else {
//                        블루 먼저 움직
                        int tmp = 1;
                        while (true) {
                            int[] nb = {cb[0] + direction[d][0] * tmp, cb[1] + direction[d][1] * tmp};
                            if (0 <= nb[0] && nb[0] < n && 0 <= nb[1] && nb[1] < m) {
                                if (board[nb[0]][nb[1]].equals("#")) {
                                    tmp -= 1;
                                    break;
                                } else if (board[nb[0]][nb[1]].equals("O")) {
                                    goal[1] = true;
                                    break;
                                }
                                tmp += 1;
                            }
                        }
                        nnb = new int[]{cb[0] + direction[d][0] * tmp, cb[1] + direction[d][1] * tmp};
                        tmp = 1;
                        while (true) {
                            int[] nr = {cr[0] + direction[d][0] * tmp, cr[1] + direction[d][1] * tmp};
                            if (0 <= nr[0] && nr[0] < n && 0 <= nr[1] && nr[1] < m) {
                                if (board[nr[0]][nr[1]].equals("#")) {
                                    tmp -= 1;
                                    break;
                                } else if (board[nr[0]][nr[1]].equals("O")) {
                                    goal[0] = true;
                                    break;
                                } else if (Arrays.equals(nnb, nr)) {
                                    tmp -= 1;
                                    break;
                                }
                                tmp += 1;
                            }
                        }
                        nnr = new int[]{cr[0] + direction[d][0] * tmp, cr[1] + direction[d][1] * tmp};
                    }
                    ncnt = ccnt + "U";
                } else {
                    if (cr[0] > cb[0]) {
//                        레드 먼저 움직
                        int tmp = 1;
                        while (true) {
                            int[] nr = {cr[0] + direction[d][0] * tmp, cr[1] + direction[d][1] * tmp};
                            if (0 <= nr[0] && nr[0] < n && 0 <= nr[1] && nr[1] < m) {
                                if (board[nr[0]][nr[1]].equals("#")) {
                                    tmp -= 1;
                                    break;
                                } else if (board[nr[0]][nr[1]].equals("O")) {
                                    goal[0] = true;
                                    break;
                                }
                                tmp += 1;
                            }
                        }
                        nnr = new int[]{cr[0] + direction[d][0] * tmp, cr[1] + direction[d][1] * tmp};
                        tmp = 1;
                        while (true) {
                            int[] nb = {cb[0] + direction[d][0] * tmp, cb[1] + direction[d][1] * tmp};
                            if (0 <= nb[0] && nb[0] < n && 0 <= nb[1] && nb[1] < m) {
                                if (board[nb[0]][nb[1]].equals("#")) {
                                    tmp -= 1;
                                    break;
                                } else if (board[nb[0]][nb[1]].equals("O")) {
                                    goal[1] = true;
                                    break;
                                } else if (Arrays.equals(nb, nnr)) {
                                    tmp -= 1;
                                    break;
                                }
                                tmp += 1;
                            }
                        }
                        nnb = new int[]{cb[0] + direction[d][0] * tmp, cb[1] + direction[d][1] * tmp};
                    } else {
//                        블루 먼저 움직
                        int tmp = 1;
                        while (true) {
                            int[] nb = {cb[0] + direction[d][0] * tmp, cb[1] + direction[d][1] * tmp};
                            if (0 <= nb[0] && nb[0] < n && 0 <= nb[1] && nb[1] < m) {
                                if (board[nb[0]][nb[1]].equals("#")) {
                                    tmp -= 1;
                                    break;
                                } else if (board[nb[0]][nb[1]].equals("O")) {
                                    goal[1] = true;
                                    break;
                                }
                                tmp += 1;
                            }
                        }
                        nnb = new int[]{cb[0] + direction[d][0] * tmp, cb[1] + direction[d][1] * tmp};
                        tmp = 1;
                        while (true) {
                            int[] nr = {cr[0] + direction[d][0] * tmp, cr[1] + direction[d][1] * tmp};
                            if (0 <= nr[0] && nr[0] < n && 0 <= nr[1] && nr[1] < m) {
                                if (board[nr[0]][nr[1]].equals("#")) {
                                    tmp -= 1;
                                    break;
                                } else if (board[nr[0]][nr[1]].equals("O")) {
                                    goal[0] = true;
                                    break;
                                } else if (Arrays.equals(nnb, nr)) {
                                    tmp -= 1;
                                    break;
                                }
                                tmp += 1;
                            }
                        }
                        nnr = new int[]{cr[0] + direction[d][0] * tmp, cr[1] + direction[d][1] * tmp};
                    }
                    ncnt = ccnt + "D";
                }
                if (!checked[nnr[0]][nnr[1]][nnb[0]][nnb[1]] && !goal[1]) {
                    checked[nnr[0]][nnr[1]][nnb[0]][nnb[1]] = true;
                    if (goal[0]) {
                        flag = true;
                        System.out.println(ncnt.length());
                        System.out.println(ncnt);
                        break;
                    }
                    if (ncnt.length() < 10) {
                        q.add(new inq(nnr, nnb, ncnt));
                    }
                }
            }
            if (flag) {
                break;
            }
        }
        if (!flag) {
            System.out.println(-1);
        }
    }
}