import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        List<String> wordList;
        if (line.isEmpty()) {
            wordList = new ArrayList<>();
        } else {
            wordList = Arrays.asList(line.split("\\s+"));
        }
        System.out.println(wordList.size());
    }
}
