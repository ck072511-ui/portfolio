import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());
        HashMap<String, String> directory = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String[] input = sc.nextLine().split(" ");
            directory.put(input[0], input[1]);
        }

        while (sc.hasNextLine()) {
            String name = sc.nextLine();

            if (directory.containsKey(name)) {
                System.out.println(name + "=" + directory.get(name));
            } else {
                System.out.println("Contact not found");
            }
        }

        sc.close();
    }
}
