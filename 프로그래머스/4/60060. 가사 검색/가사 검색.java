import java.util.*;

class Solution {
    public int[] solution(String[] words, String[] queries) {
        int[] answer = new int[queries.length];
        Trie trie = new Trie();
        Trie Rtrie = new Trie();
        for (String word: words) {
            trie.insert(word);
            StringBuffer sb = new StringBuffer(word);
            String Rword = sb.reverse().toString();
            Rtrie.insert(Rword);
        }
        for (int i = 0; i < queries.length; i++) {
            String word = queries[i];
            if (word.charAt(word.length() - 1) == '?') answer[i] = trie.find(word);
            else {
                StringBuffer sb = new StringBuffer(word);
                String Rword = sb.reverse().toString();
                answer[i] = Rtrie.find(Rword);
            }
        }
        return answer;
    }
}
class Node {
    HashMap<Character, Node> child;
    HashMap<Integer, Integer> cnt;
    Node() {
        this.child = new HashMap<>();
        this.cnt = new HashMap<>();
    }
}

class Trie {
    Node head;
    Trie() {
        this.head = new Node();
    }
    public void insert(String word) {
        Node now = this.head;
        int l = word.length();
        if (now.cnt.containsKey(l)) {
            now.cnt.replace(l, now.cnt.get(l) + 1);
        } else {
            now.cnt.put(l, 1);
        }
        for (int i = 0; i < l; i++) {
            char c = word.charAt(i);
            if (!now.child.containsKey(c)) {
                now.child.put(c, new Node());
            }
            now = now.child.get(c);
            if (now.cnt.containsKey(l - i - 1)) {
                now.cnt.replace(l - i - 1, now.cnt.get(l - i - 1) + 1);
            } else {
                now.cnt.put(l - i - 1, 1);
            }
        }
    }
    public int find(String word) {
        Node now = this.head;
        int l = word.length();
        for (int i = 0; i < l; i++) {
            char c = word.charAt(i);
            if (c == '?') {
                return now.cnt.getOrDefault(l - i, 0);
            } else if (now.child.containsKey(c)) {
                now = now.child.get(c);
            } else return 0;
        }
        return now.cnt.getOrDefault(0, 0);
    }
}