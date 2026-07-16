import java.util.Scanner;

public class c {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int t = sc.nextInt();
        StringBuilder out = new StringBuilder();
        
        while (t-- > 0) {
            int n = sc.nextInt();
            String s = sc.next();
            
            int transitions = 0;
            for (int i = 0; i < n - 1; i++) {
                if (s.charAt(i) != s.charAt(i + 1)) {
                    transitions++;
                }
            }
            
            int minwf = (transitions == 1) ? 2 : 1;
            out.append(minwf).append("\n");
        }
        
        System.out.print(out);
        sc.close();
    }
}