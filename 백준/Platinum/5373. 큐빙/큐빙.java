import java.io.*;
import java.util.*;

public class Main {
//          위U0w 아래D1y 앞F2r 뒤B3o 왼L4g 오R5b
    static String[][][] cube;
    static String faceIndex = "UDFBLR";
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());
        for (int i = 0; i < TC; i++) {
            cube = new String[][][]{{{"w", "w", "w"}, {"w", "w", "w"}, {"w", "w", "w"}}, {{"y", "y", "y"}, {"y", "y", "y"}, {"y", "y", "y"}}, {{"r", "r", "r"}, {"r", "r", "r"}, {"r", "r", "r"}}, {{"o", "o", "o"}, {"o", "o", "o"}, {"o", "o", "o"}}, {{"g", "g", "g"}, {"g", "g", "g"}, {"g", "g", "g"}}, {{"b", "b", "b"}, {"b", "b", "b"}, {"b", "b", "b"}}};
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                String[] order = st.nextToken().split("");
                rotate(order[0], order[1]);
            }
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    System.out.print(cube[0][j][k]);
                }
                System.out.println();
            }
        }
    }
    static void rotate(String face, String clockwise) {
        String[][] newFace = new String[3][3];
        int s = faceIndex.indexOf(face);
        if (clockwise.equals("+")) {
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    newFace[j][2 - i] = cube[s][i][j];
                }
            }
        } else {
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    newFace[2 - j][i] = cube[s][i][j];
                }
            }
        }
        cube[s] = newFace;
        int[] f = new int[4];
        String[][] row = new String[4][3];
        int[][][] index = new int[4][3][2];
//          위U0w 아래D1y 앞F2r 뒤B3o 왼L4g 오R5b
        if (s == 0) {
            f = new int[]{3, 5, 2, 4};
            index = new int[][][]{{{0, 0}, {0, 1}, {0, 2}},
                                  {{0, 0}, {0, 1}, {0, 2}},
                                  {{0, 0}, {0, 1}, {0, 2}},
                                  {{0, 0}, {0, 1}, {0, 2}}};
        } else if (s == 1) {
            f = new int[]{2, 5, 3, 4};
            index = new int[][][]{{{2, 0}, {2, 1}, {2, 2}},
                                  {{2, 0}, {2, 1}, {2, 2}},
                                  {{2, 0}, {2, 1}, {2, 2}},
                                  {{2, 0}, {2, 1}, {2, 2}}};
        } else if (s == 2) {
            f = new int[]{0, 5, 1, 4};
            index = new int[][][]{{{2, 0}, {2, 1}, {2, 2}},
                                  {{0, 0}, {1, 0}, {2, 0}},
                                  {{0, 2}, {0, 1}, {0, 0}},
                                  {{2, 2}, {1, 2}, {0, 2}}};
        } else if (s == 3) {
            f = new int[]{0, 4, 1, 5};
            index = new int[][][]{{{0, 0}, {0, 1}, {0, 2}},
                                  {{2, 0}, {1, 0}, {0, 0}},
                                  {{2, 2}, {2, 1}, {2, 0}},
                                  {{0, 2}, {1, 2}, {2, 2}}};
        } else if (s == 4) {
            f = new int[]{0, 2, 1, 3};
            index = new int[][][]{{{0, 0}, {1, 0}, {2, 0}},
                                  {{0, 0}, {1, 0}, {2, 0}},
                                  {{0, 0}, {1, 0}, {2, 0}},
                                  {{2, 2}, {1, 2}, {0, 2}}};
        } else if (s == 5) {
            f = new int[]{0, 3, 1, 2};
            index = new int[][][]{{{0, 2}, {1, 2}, {2, 2}},
                                  {{2, 0}, {1, 0}, {0, 0}},
                                  {{0, 2}, {1, 2}, {2, 2}},
                                  {{0, 2}, {1, 2}, {2, 2}}};
        }
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 3; j++) {
                row[i][j] = cube[f[i]][index[i][j][0]][index[i][j][1]];
            }
        }
        if (clockwise.equals("+")) {
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 3; j++) {
                    cube[f[(i+1)%4]][index[(i+1)%4][j][0]][index[(i+1)%4][j][1]] = row[i][j];
                }
            }
        } else {
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 3; j++) {
                    cube[f[(i+3)%4]][index[(i+3)%4][j][0]][index[(i+3)%4][j][1]] = row[i][j];
                }
            }
        }
    }
}