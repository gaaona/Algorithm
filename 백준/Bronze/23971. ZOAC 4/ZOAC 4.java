import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int W = sc.nextInt();
        int N = sc.nextInt();
        int M = sc.nextInt();

        
        int row = (H + N) / (N + 1);
        int col = (W + M) / (M + 1);
        
        System.out.println(row * col);
    }
}