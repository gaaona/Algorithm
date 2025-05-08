import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int max_v = -1000000;
        int min_v = 1000000;
        
        for (int i = 0; i<N; i++) {
            int tmp = sc.nextInt();
            
            if (min_v>tmp) {
                min_v = tmp;
            } 

            if (max_v < tmp) {
                max_v = tmp;
            }
        }
        
        System.out.print(min_v);
        System.out.print(' ');
        System.out.print(max_v);
    }
}