import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String ISBN = br.readLine().trim();
        int ans = 0;
        int starIndex = -1;

        // 1단계: * 위치와 나머지 숫자들의 합 계산
        for (int i = 0; i < 13; i++) {
            char ch = ISBN.charAt(i);
            if (ch == '*') {
                starIndex = i;
                continue;
            }
            int digit = ch - '0';
            if (i % 2 == 0) {   // 가중치 1
                ans += digit;
            } else {            // 가중치 3
                ans += digit * 3;
            }
        }

        // 2단계: * 자리에 숫자 찾기
        for (int num = 0; num <= 9; num++) {
            int total = ans;
            if (starIndex % 2 == 0) {  // 가중치 1
                total += num;
            } else {                   // 가중치 3
                total += num * 3;
            }
            if (total % 10 == 0) {
                System.out.println(num);
                break;
            }
        }
    }
}
