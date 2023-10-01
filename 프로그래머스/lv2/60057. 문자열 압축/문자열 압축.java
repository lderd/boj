import java.util.*;

class Solution {
    public int solution(String s) {
        int l = s.length();
        int answer = l;
        for (int rLen = 1; rLen < l / 2 + 1; rLen++) {
            int idx = rLen;
            int tmp = 0;
            char[] word = new char[rLen];
            for (int i = 0; i < rLen; i++) {
                word[i] = s.charAt(i);
            }
            int cnt = 1;
            while (l - idx >= rLen) {
                boolean flag = true;
                for (int i = 0; i < rLen; i++) {
                    if (!Objects.equals(word[i], s.charAt(idx+i))) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    cnt += 1;
                } else {
                    if (cnt > 1) tmp += Integer.toString(cnt).length() + rLen;
                    else tmp += rLen;
                    for (int i = 0; i < rLen; i++) {
                        word[i] = s.charAt(idx+i);
                    }
                    cnt = 1;
                }
                idx += rLen;
            }
            if (cnt > 1) tmp += Integer.toString(cnt).length() + rLen;
            else tmp += rLen;
            tmp += l - idx;
            if (tmp < answer) answer = tmp;
        }
        return answer;
    }
}