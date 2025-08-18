import java.util.*;

class Point {
    int x,y;
    Point(int x, int y) { this.x = x; this.y = y;}
}

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        ArrayList<Point> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            arr.add(new Point(x,y));
        }
        arr.sort((a,b) -> { // 오름차순 정렬
            if (a.y != b.y) return a.y - b.y;
            return a.x - b.x;
        });
        for (Point p : arr) {
            System.out.println(p.x + " " + p.y);
        }
    }
}