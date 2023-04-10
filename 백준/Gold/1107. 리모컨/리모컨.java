import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] channelArray;
    static boolean[] crashed = new boolean[10];
    static int channel;
    static int bigMin = 50000000;
    static int bigMinIndex = 8;
    static int smallMax = -1;
    static int smallMaxIndex = 0;
    public static void main(String[]args) throws java.io.IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String N = br.readLine();
        channel = Integer.parseInt(N);
        channelArray = new int[N.length()];
        for (int i = 0; i < N.length(); i++) {
            channelArray[i] = Integer.parseInt(String.valueOf(N.charAt(i)));
        }
        int M = Integer.parseInt(br.readLine());
        if (M > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < M; i++) {
                crashed[Integer.parseInt(st.nextToken())] = true;
            }
        }
        if (M < 10) {
//            목표채널보다 큰 최소 채널
            int[] tmp = new int[N.length()];
            makeBigMin(tmp, 0, -1);
//            자릿수가 더 많아야 할 때
            if (bigMin == 50000000) {
                tmp = new int[N.length() + 1];
                for (int i = 0; i < N.length() + 1; i++) {
                    for (int j = i == 0 ? 1 : 0; j < 10; j++) {
                        if (!crashed[j]) {
                            tmp[i] = j;
                            break;
                        }
                    }
                }
                int now = 0;
                for (int i = 0; i < N.length() + 1; i++) {
                    now += tmp[i] * Math.pow(10, N.length() - i);
                }
                if (now < bigMin & now >= channel) {
                    bigMin = now;
                    bigMinIndex = N.length() + 1;
                }
            }
//            목표채널보다 큰 최소 채널
//            목표채널보다 작은 최대 채널
            tmp = new int[N.length()];
            makeSmallMax(tmp, 0, -1);
//            자릿수가 더 적어야 할 때
            if (smallMax == -1 & N.length() > 1) {
                tmp = new int[N.length() - 1];
                for (int i = 0; i < N.length() - 1; i++) {
                    for (int j = 9; j > (i == 0 ? 0 : -1); j--) {
                        if (!crashed[j]) {
                            tmp[i] = j;
                            break;
                        }
                    }
                }
                int now = 0;
                for (int i = 0; i < N.length() - 1; i++) {
                    now += tmp[i] * Math.pow(10, N.length() - 2 - i);
                }
                if (now > smallMax & now <= channel) {
                    smallMax = now;
                    smallMaxIndex = N.length() - 1;
                }
            }
            if (smallMax > -1) {
                int ttmp = smallMax;
                if (ttmp == 0) {
                    smallMaxIndex = 1;
                } else {
                    smallMaxIndex = 0;
                    while (ttmp > 0) {
                        ttmp /= 10;
                        smallMaxIndex += 1;
                    }
                }
            }
//            목표채널보다 작은 최대 채널
            int answer = 500000;
            if (smallMax > -1 & smallMaxIndex + Math.abs(smallMax - channel) < answer) {
                answer = smallMaxIndex + Math.abs(smallMax - channel);
            }
            if (bigMin < 50000000 & bigMinIndex + Math.abs(bigMin - channel) < answer) {
                answer = bigMinIndex + Math.abs(bigMin - channel);
            }
            if (Math.abs(channel - 100) < answer) {
                answer = Math.abs(channel - 100);
            }
            System.out.println(answer);
        } else {
            System.out.println(Math.abs(channel - 100));
        }
    }
    static void makeBigMin(int[] num, int len, int index) {
        if (index < len) {
            for (int j = 0; j < 10; j++) {
                if (!crashed[j]) {
                    num[len] = j;
                    if (len < num.length - 1) {
                        makeBigMin(num, len + 1, index);
                    } else {
                        int now = 0;
                        for (int i = 0; i < len + 1; i++) {
                            now += num[i] * Math.pow(10, len - i);
                        }
                        if (now < bigMin & now >= channel) {
                            bigMin = now;
                            bigMinIndex = len + 1;
                        }
                    }
                }
            }
        } else {
            for (int j = 0; j < 10; j++) {
                if (channelArray[len] == j & !crashed[j]) {
                    num[len] = j;
                    if (len < num.length - 1) {
                        makeBigMin(num, len + 1, len + 1);
                    } else {
                        int now = 0;
                        for (int i = 0; i < len + 1; i++) {
                            now += num[i] * Math.pow(10, len - i);
                        }
                        if (now < bigMin & now >= channel) {
                            bigMin = now;
                            bigMinIndex = len + 1;
                        }
                    }
                } else if (channelArray[len] < j & !crashed[j]) {
                    num[len] = j;
                    if (len < num.length - 1) {
                        makeBigMin(num, len + 1, len);
                    } else {
                        int now = 0;
                        for (int i = 0; i < len + 1; i++) {
                            now += num[i] * Math.pow(10, len - i);
                        }
                        if (now < bigMin & now >= channel) {
                            bigMin = now;
                            bigMinIndex = len + 1;
                        }
                    }
                }
            }
        }
    }
    static void makeSmallMax(int[] num, int len, int index) {
        if (index < len) {
            for (int j = 9; j > -1; j--) {
                if (!crashed[j]) {
                    num[len] = j;
                    if (len < num.length - 1) {
                        makeSmallMax(num, len + 1, index);
                    } else {
                        int now = 0;
                        for (int i = 0; i < len + 1; i++) {
                            now += num[i] * Math.pow(10, len - i);
                        }
                        if (now > smallMax & now <= channel) {
                            smallMax = now;
                        }
                    }
                }
            }
        } else {
            for (int j = 9; j > -1; j--) {
                if (channelArray[len] == j & !crashed[j]) {
                    num[len] = j;
                    if (len < num.length - 1) {
                        makeSmallMax(num, len + 1, len + 1);
                    } else {
                        int now = 0;
                        for (int i = 0; i < len + 1; i++) {
                            now += num[i] * Math.pow(10, len - i);
                        }
                        if (now > smallMax & now <= channel) {
                            smallMax = now;
                        }
                    }
                } else if (channelArray[len] > j & !crashed[j]) {
                    num[len] = j;
                    if (len < num.length - 1) {
                        makeSmallMax(num, len + 1, index);
                    } else {
                        int now = 0;
                        for (int i = 0; i < len + 1; i++) {
                            now += num[i] * Math.pow(10, len - i);
                        }
                        if (now > smallMax & now <= channel) {
                            smallMax = now;
                        }
                    }
                }
            }
        }
    }
}