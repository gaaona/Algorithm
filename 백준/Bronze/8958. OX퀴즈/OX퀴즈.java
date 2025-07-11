import java.util.Scanner;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < cases; i++){
            String score_board = sc.nextLine();
            
            int ans = 0;
            int current_score = 0;

            for (int j=0; j < score_board.length(); j++){
                if (score_board.substring(j, j+1).equals("O")){
                    current_score += 1;
                    ans += current_score;   
                }
                else {
                    current_score = 0;
                }
            }
            System.out.println(ans);
        }
    }
}