import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        
        for (int i = 0; i < N; i ++){
            boolean isNo = false;
            
            String ln = sc.nextLine();
            Stack<Integer> stack = new Stack<>();
            
            int M = ln.length();
            
            for (int j=0; j < M; j ++) {
                if (ln.charAt(j) == '('){
                    stack.push(j);
                } else if (!stack.isEmpty() && ln.charAt(j) == ')') {
                    stack.pop();
                } else {
                    isNo = true;
                    break;
                }
            }
            
            if (!isNo && stack.isEmpty()){
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}