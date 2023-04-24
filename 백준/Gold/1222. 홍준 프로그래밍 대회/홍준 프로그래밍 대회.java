import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[2000001];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[Integer.parseInt(st.nextToken())] += 1;
        }
        long answer = N;
        for (int i = 2; i < 2000001; i++) {
            long tmp = 0;
            for (int j = i; j <= 2000000; j+=i) {
                tmp += arr[j];
            }
            if (tmp >= 2 & tmp * i > answer) {
                answer = tmp * i;
            }
        }
        System.out.println(answer);
    }
}