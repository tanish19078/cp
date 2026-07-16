import java.util.*;
import java.io.*;

public class b {
    static List<Long> goodNumbers;
    
    // Precompute good numbers once globally
    static void precompute() {
        Set<Long> goodSet = new HashSet<>();
        for (int d1 = 0; d1 < 10; d1++) {
            for (int d2 = d1; d2 < 10; d2++) {
                dfs(0, 0, d1, d2, goodSet);
            }
        }
        goodNumbers = new ArrayList<>(goodSet);
        Collections.sort(goodNumbers);
    }
    
    static void dfs(long val, int len, int d1, int d2, Set<Long> goodSet) {
        if (val >= 2 && val <= 1000000000L) {
            goodSet.add(val);
        }
        if (len == 10) return;
        
        if (val > 0 || d1 > 0) dfs(val * 10 + d1, len + 1, d1, d2, goodSet);
        if (val > 0 || d2 > 0) dfs(val * 10 + d2, len + 1, d1, d2, goodSet);
    }
    
    public static void main(String[] args) {
        precompute();
        
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) return;
        
        int t = scanner.nextInt();
        StringBuilder out = new StringBuilder();
        
        for (int i = 0; i < t; i++) {
            long x = scanner.nextLong();
            
            for (long y : goodNumbers) {
                long prod = x * y;
                
                int mask = 0;
                int count = 0;
                long temp = prod;
                boolean isGood = true;
                
                // Fast digit validation
                while (temp > 0) {
                    int d = (int)(temp % 10);
                    if ((mask & (1 << d)) == 0) {
                        mask |= (1 << d);
                        count++;
                        if (count > 2) {
                            isGood = false;
                            break;
                        }
                    }
                    temp /= 10;
                }
                
                if (isGood) {
                    out.append(y).append("\n");
                    break;
                }
            }
        }
        System.out.print(out.toString());
        scanner.close();
    }
}