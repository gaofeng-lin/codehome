package LT76;

import java.util.HashMap;

public class Demo {

    public static void main(String[] args) {
        String s = "ADOBECODEBANC";
        String t = "ABC";

        String res = minWindow(s, t);
        System.out.println(res);

    }

    public static String minWindow(String s, String t) {
        HashMap<Character, Integer> need = new HashMap<>();
        HashMap<Character, Integer> window = new HashMap<>();
        int left = 0, right = 0;
        int valid = 0;
        // for (char c : t) {
        //     need.put()
        // }
        for (int i = 0; i < t.length(); i++) {
            need.put(t.charAt(i), need.getOrDefault(t.charAt(i), 0) + 1);
        }

        int start = 0, len = Integer.MAX_VALUE;

        while (right < s.length()) {
            char c = s.charAt(right);
            right++;
            if (need.containsKey(c)) {
                window.put(c, need.getOrDefault(c, 0) + 1);
                if (window.get(c) == need.get(c)) {
                    valid++;
                }
            }

            while (valid == t.length()) {
                if (right - left < len) {
                    start = left;
                    len = right - left;
                }

                char d = s.charAt(left);
                left++;
                if (need.containsKey(d)) {
                    if (window.get(d) == need.get(d)) {
                        valid--;
                    }
                    window.put(c, need.getOrDefault(c, 0) - 1);
                }
            }
        }

        return len == Integer.MAX_VALUE ? "" : s.substring(left, right + 1);
    }
}

