import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Queue<Integer> queue = new LinkedList<>();

        for (int i = 1; i <= N; i++) {
            queue.offer(i);
        }

        while (queue.size() > 1) {
            queue.poll();           // 앞 카드 버림
            queue.offer(queue.poll()); // 다음 카드를 맨 뒤로 보냄
        }

        System.out.println(queue.peek()); // 마지막 카드 출력
    }
}
