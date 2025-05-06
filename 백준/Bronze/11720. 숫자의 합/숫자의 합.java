import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine(); // 엔터 제거
        String numbers = sc.nextLine();

        int tot = 0;

        for (int i = 0; i<N; i++) {
            char ch = numbers.charAt(i);
            int n = ch - '0';
            tot += n;
        }

        System.out.println(tot);
    }
}
