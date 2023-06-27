import java.io.*;
import java.util.*;

public class Main {
    static int R, C;
    static String[][] board;
    static Stack[] checked;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stRC = new StringTokenizer(br.readLine());
        R = Integer.parseInt(stRC.nextToken());
        C = Integer.parseInt(stRC.nextToken());
        board = new String[R][C];
        checked = new Stack[C];
        for (int i = 0; i < R; i++) {
            String row = br.readLine();
            for (int j = 0; j < C; j++) {
                board[i][j] = Character.toString(row.charAt(j));
            }
        }
        for (int i = 0; i < C; i++) {
            checked[i] = new Stack<Integer[]>();
        }
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            int col = Integer.parseInt(br.readLine());
            col -= 1;
            int[] start = {0, col};
            if (!checked[col].isEmpty()) {
                start = rootCheck(col);
            }
            down(col, start[0], start[1]);
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = 0; i < R; i++) {
            String answer = String.join("", board[i]);
            bw.write(answer);
            bw.newLine();
        }
        bw.close();
    }
    static int[] rootCheck(int start) {
        while (true) {
            int[] now = (int[]) checked[start].pop();
            if (Objects.equals(board[now[0]][now[1]], ".")) {
                return now;
            }
        }
    }
    static void down(int start, int row, int col) {
        for (int i = row; i < R; i++) {
            if (Objects.equals(board[i][col], ".")) {
                checked[start].add(new int[]{i, col});
            }else {
                if (Objects.equals(board[i][col], "X")) {
                    board[i-1][col] = "O";
                    return;
                } else {
                    if (col > 0 && Objects.equals(board[i][col-1], ".") && Objects.equals(board[i-1][col-1], ".")) {
                        down(start, i, col-1);
                        return;
                    } else if (col < C - 1 && Objects.equals(board[i][col+1], ".") && Objects.equals(board[i-1][col+1], ".")) {
                        down(start, i, col + 1);
                        return;
                    } else {
                        board[i-1][col] = "O";
                        return;
                    }
                }
            }
        }
        board[R-1][col] = "O";
    }
}