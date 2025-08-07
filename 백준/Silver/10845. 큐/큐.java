import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> que = new LinkedList<>();
        int last = -1;

        int N = sc.nextInt();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            String cmd = sc.next();
            switch (cmd) {
                case "push":
                    int x = sc.nextInt();
                    que.offer(x);
                    last = x;
                    break;
                case "pop":
                    if(que.isEmpty()) {
                        sb.append(-1).append('\n');
                    } else {
                        sb.append(que.poll()).append('\n');
                    }
                    break;
                case "size":
                    sb.append(que.size()).append('\n');
                    break;
                case "empty":
                    sb.append(que.isEmpty() ? 1 : 0).append('\n');
                    break;
                case "front":
                    sb.append(que.isEmpty() ? -1 : que.peek()).append('\n');
                    break;
                case "back":
                    sb.append(que.isEmpty() ? -1 : last).append('\n');
                    break;
            }
        }
        System.out.print(sb);
        sc.close();
    }
}
