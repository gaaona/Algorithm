import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            String text = sc.nextLine();
            String[] nums = text.split(" ");
            
            // 문자열을 정수로 변환해서 비교
            if (Integer.parseInt(nums[0]) == 0 && Integer.parseInt(nums[1]) == 0) {
                break;
            }
            
            if (Integer.parseInt(nums[0]) > Integer.parseInt(nums[1])) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }
        sc.close(); // Scanner 닫기 (좋은 습관)
    }
}
