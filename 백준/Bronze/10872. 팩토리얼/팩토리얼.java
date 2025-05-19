import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int ans = 1;
        for (int i=num; i>1; i--) {
            ans *= i;
        }
        System.out.println(ans);
    }
}