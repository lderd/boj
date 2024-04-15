import java.io.*;
import java.util.*;

public class Main {
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[] arr = new int[n+1];
        for (int i = 1; i < n+1; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = Integer.parseInt(st.nextToken());
        }
        HashSet<Integer> answerSet = new HashSet<>();
        for (int i = 1; i < n+1; i++) {
            if (answerSet.contains(i)) continue;
            HashSet<Integer> tmp = new HashSet<>();
            int start = i;
            int now = i;
            while (!tmp.contains(now)) {
                tmp.add(now);
                now = arr[now];
            }
            if (now == start) {
                answerSet.addAll(tmp);
            }
        }
        Integer[] answer = answerSet.toArray(new Integer[0]);
        Arrays.sort(answer);
        System.out.println(answer.length);
        for (int ans: answer) {
            System.out.println(ans);
        }
    }
}