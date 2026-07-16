import java.io.DataInputStream;

public class c {
    static int[] root;

    public static void main(String[] args) throws Exception {
        DataInputStream sc = new DataInputStream(new java.io.BufferedInputStream(System.in, 1 << 16));
        int tc = readInt(sc);
        StringBuilder out = new StringBuilder();
        while (tc-- > 0) {
            int len = readInt(sc), stepA = readInt(sc), stepB = readInt(sc);
            root = new int[len + 1];
            for (int pos = 1; pos <= len; pos++) root[pos] = pos;
            for (int pos = 1; pos + stepA <= len; pos++) merge(pos, pos + stepA);
            for (int pos = 1; pos + stepB <= len; pos++) merge(pos, pos + stepB);
            boolean sortable = true;
            for (int pos = 1; pos <= len; pos++) {
                int val = readInt(sc);
                if (leader(pos) != leader(val)) sortable = false;
            }
            out.append(sortable ? "YES" : "NO").append('\n');
        }
        System.out.print(out);
    }

    static int leader(int node) {
        while (root[node] != node) { root[node] = root[root[node]]; node = root[node]; }
        return node;
    }

    static void merge(int u, int v) {
        u = leader(u); v = leader(v);
        if (u != v) root[u] = v;
    }

    private static int readInt(DataInputStream sc) throws Exception {
        int num = 0, ch;
        do { ch = sc.read(); } while (ch < '0');
        while (ch >= '0') { num = num * 10 + ch - '0'; ch = sc.read(); }
        return num;
    }
}

