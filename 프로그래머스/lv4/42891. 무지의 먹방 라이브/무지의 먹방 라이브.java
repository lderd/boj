import java.util.*;

class Solution {
    public int solution(int[] food_times, long k) {
        int answer = -1;
        int l = food_times.length;
        int[][] inTable = new int[l][2];
        HashSet<Integer> checked = new HashSet<>();
        for (int i = 0; i < l; i++) {
            inTable[i][0] = food_times[i];
            inTable[i][1] = i + 1;
            checked.add(i + 1);
        }
        Arrays.sort(inTable, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] == o2[0]) return o1[1] - o2[1];
                return o1[0] - o2[0];
            }
        });
        int beforeFood = 0;
        for (int i = 0; i < l; i++) {
            long remain = (long) (inTable[i][0] - beforeFood) * (l - i);
            if (k < remain) {
                Object[] checkedArray = checked.toArray();
                Arrays.sort(checkedArray);
                answer = (int) checkedArray[(int) (k % (l - i))];
                break;
            } else {
                k -= remain;
                checked.remove(inTable[i][1]);
                beforeFood = inTable[i][0];
            }
        }
        return answer;
    }
}