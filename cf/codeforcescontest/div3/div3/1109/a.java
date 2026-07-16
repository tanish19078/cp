import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class a {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine().trim());
            String s = br.readLine().trim();
            int best = 0, cur = 0;
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '#') {
                    cur++;
                    if (cur > best) best = cur;
                } else {
                    cur = 0;
                }
            }
            sb.append((best + 1) / 2).append('\n');
        }
        System.out.print(sb);
    }
}