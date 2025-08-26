import java.util.Scanner;
import java.io.IOException;
import java.util.Stack;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        Stack<Integer> st = new Stack<>();

        int N = sc.nextInt();

        for (int i = 0; i < N; i ++) {
            int num = sc.nextInt();
            if (num == 0) {
                st.pop();
            } else {
                st.push(num);
            }
        }
        int ans = 0;
        for (int j = 0; j < st.size(); j ++) {
            ans += st.get(j);
        }

        System.out.println(ans);
    }
}