import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        System.out.println(A+B-C);

        int AB = Integer.parseInt(""+A+B);
        System.out.println(AB - C);
    }
}