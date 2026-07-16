import java.io.DataInputStream;

public class b {
    public static void main(String[] args) throws Exception {
        DataInputStream in = new DataInputStream(new java.io.BufferedInputStream(System.in, 1 << 16));
        int t = nextInt(in);
        StringBuilder sb = new StringBuilder();
        while (t-- > 0) {
            int n = nextInt(in);
            long prev = 0, carry = 0;
            boolean ok = true;
            for (int i = 0; i < n; i++) {
                long a = nextInt(in);
                long total = a + carry;
                long need = prev + 1;
                if (i == n - 1) {
                    if (total < need) ok = false;
                } else {
                    if (total < need) { ok = false; carry = 0; prev = need; }
                    else { carry = total - need; prev = need; }
                }
            }
            sb.append(ok ? "YES" : "NO").append('\n');
        }
        System.out.print(sb);
    }

    private static int nextInt(DataInputStream in) throws Exception {
        int ret = 0, b;
        do { b = in.read(); } while (b < '0');
        while (b >= '0') { ret = ret * 10 + b - '0'; b = in.read(); }
        return ret;
    }
} 
