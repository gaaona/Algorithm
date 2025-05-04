import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        int idx = sc.nextInt();
        System.out.println(word.charAt(idx-1));
    }
}