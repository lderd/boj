import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[]args) throws java.io.IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int X, Y, D, T;
        X = Integer.parseInt(st.nextToken());
        Y = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        double dist = Math.sqrt(X*X + Y*Y);
        double maxB = dist / D;
        int b = 0;
        double answer = 10000000;
        while (b <= maxB + 1) {
            double a = dist - D * b;
            if (a < 0) {
                a = -a;
            }
            double tmp = a + T * b;
            if (0 < tmp & tmp < answer) {
                answer = tmp;
            }
            if (Math.abs(dist - D * b) < D) {
                if ((b + 2) * T < answer) {
                    answer = (b + 2) * T;
                }
            }
            if (Math.abs(dist - D * b) < D * 2) {
                if ((b + 2) * T < answer) {
                    answer = (b + 2) * T;
                }
            }
            b += 1;
        }
        System.out.println(answer);
    }
}