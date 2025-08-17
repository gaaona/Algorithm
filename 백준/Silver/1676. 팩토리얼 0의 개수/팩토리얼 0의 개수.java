import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int count = 0;
        
        for (int i = 5; i <= N; i *= 5) { // 5보다 크면 2보다도 큼(%10 가능)
            count += N / i;
        }
        System.out.println(count);
    }
}
