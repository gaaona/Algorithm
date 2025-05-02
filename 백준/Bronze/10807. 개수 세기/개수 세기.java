import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int[] numCounts = new int[201]; // -100 ~ -1, 0, 1 ~ 100

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            numCounts[num + 100] += 1; // 모든 숫자에 +100 적용 (0~100,101,102~201)
        }

        int v = sc.nextInt();
        System.out.println(numCounts[v + 100]); // v도 +100 적용
    }
}
