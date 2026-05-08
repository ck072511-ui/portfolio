import java.util.*;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Number of contacts
        int n = Integer.parseInt(sc.nextLine());

        // HashMap to store contacts
        HashMap<String, String> directory = new HashMap<>();

        // Reading contact details
        for (int i = 0; i < n; i++) {
            String input = sc.nextLine();   // full line
            String[] data = input.split(" ");

            String name = data[0];
            String phone = data[1];

            directory.put(name, phone);
        }

        // Search queries (supports multiple searches)
        while (sc.hasNextLine()) {
            String searchName = sc.nextLine();

            if (directory.containsKey(searchName)) {
                System.out.println(searchName + "=" + directory.get(searchName));
            } else {
                System.out.println("Contact not found");
            }
        }

        sc.close();
    }
}