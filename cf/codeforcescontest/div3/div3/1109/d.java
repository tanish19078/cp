import java.io.DataInputStream;

public class d {
    public static void main(String[] args) throws Exception {
        DataInputStream sc = new DataInputStream(new java.io.BufferedInputStream(System.in, 1 << 16));
        int tc = readInt(sc);
        StringBuilder out = new StringBuilder();
        while (tc-- > 0) {
            int len = readInt(sc), posts = readInt(sc);
            long[] arr = new long[len + 1];
            for (int pos = 1; pos <= len; pos++) arr[pos] = readInt(sc);
            boolean[] flipAt = new boolean[len + 1];
            for (int j = 0; j < posts; j++) flipAt[readInt(sc)] = true;

            long even = 0, odd = Long.MIN_VALUE / 4;
            for (int pos = len; pos >= 1; pos--) {
                if (flipAt[pos]) {
                    long best = Math.max(even, odd);
                    even = best; odd = best;
                }
                even += arr[pos];
                odd  -= arr[pos];
            }
            out.append(Math.max(even, odd)).append('\n');
        }
        System.out.print(out);
    }

    private static int readInt(DataInputStream sc) throws Exception {
        int num = 0, ch, sgn = 1;
        do { ch = sc.read(); } while (ch != '-' && (ch < '0' || ch > '9'));
        if (ch == '-') { sgn = -1; ch = sc.read(); }
        while (ch >= '0' && ch <= '9') { num = num * 10 + ch - '0'; ch = sc.read(); }
        return num * sgn;
    }
}

