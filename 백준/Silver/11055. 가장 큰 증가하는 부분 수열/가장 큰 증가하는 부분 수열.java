import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int answer = 0;
        int[] arr = new int[N];
        int[] ssum = new int[N];
        Arrays.fill(ssum, 0);
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            arr[i] = num;
            ssum[i] = num;
            for (int j = 0; j < i; j++) {
                if (arr[j] < arr[i] && ssum[j] + num > ssum[i]) ssum[i] = ssum[j] + num;
            }
            if (ssum[i] > answer) answer = ssum[i];
        }
        System.out.println(answer);
    }
}