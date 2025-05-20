import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int number = 1;
        int i = 1; // i를 1부터 시작 (첫 번째 방은 1이므로)

        int N = sc.nextInt();

        while (number < N) {
            number += 6 * i;
            i++;
        }
        System.out.println(i);
    }
}
