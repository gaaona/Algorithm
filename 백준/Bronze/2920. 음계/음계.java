import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] nums = new int[8];
        for (int i = 0; i < 8; i++) {
            nums[i] = sc.nextInt();
        }
        
        boolean ascending = true;
        boolean descending = true;
        
        for (int i = 0; i < 7; i++) {
            if (nums[i] < nums[i+1]) {
                descending = false;
            } else if (nums[i] > nums[i+1]) {
                ascending = false;
            }
        }
        
        if (ascending) {
            System.out.println("ascending");
        } else if (descending) {
            System.out.println("descending");
        } else { // 둘 다 false면 mixed
            System.out.println("mixed");
        }
    }
}
