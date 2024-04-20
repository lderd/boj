import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int answer = 0;
        int[] arr = new int[N];
        Arrays.fill(arr, 0);
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken()) * -1;
            int idx = Arrays.binarySearch(arr, num);
            if (idx < 0) {
                idx = (idx + 1) * -1;
            }
            arr[idx] = num;
            if (idx >= answer) answer += 1;
        }
        System.out.println(answer);
    }
}