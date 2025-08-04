import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        int[] A = new int[N];
        
        String[] aInput = sc.nextLine().split(" ");
        for (int i = 0; i < N; i++){
            A[i] = Integer.parseInt(aInput[i]);
        };
        Arrays.sort(A);
            
        int M = Integer.parseInt(sc.nextLine());
        String[] bInput = sc.nextLine().split(" ");
        
        for (int i = 0; i < M; i++){
            int target = Integer.parseInt(bInput[i]);

            if (binarySearch(A, target)){
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
    }

    private static boolean binarySearch(int[] arr, int target){
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (arr[mid] == target){
                return true;
            } else if (arr[mid] < target){
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
}