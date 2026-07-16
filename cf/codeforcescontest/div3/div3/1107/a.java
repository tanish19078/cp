import java.util.Scanner;

public class a {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
      
        if (!scanner.hasNextInt()) {
            return;
        }
        
        int t = scanner.nextInt();
        StringBuilder output = new StringBuilder();
        
        for (int i = 0; i < t; i++) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            
            if (x % y == 0) {
                output.append("YES\n");
            } else {
                output.append("NO\n");
            }
        }

        System.out.print(output.toString());
        scanner.close();
    }
}