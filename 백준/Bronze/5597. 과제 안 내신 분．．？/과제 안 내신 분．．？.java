import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] students = new int[31];

        for (int i=0; i<28; i++) {
            int idx = sc.nextInt();
            students[idx] = 1;
        }

        for (int j=1;j<31;j++) {
            if (students[j] == 0) {
                System.out.println(j);
            }
        }
        
    }
}