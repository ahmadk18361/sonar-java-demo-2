import java.io.*;

public class TomcatCVE2019_0232Example {
    public static void main(String[] args) throws IOException {
        // REMEDIATED: Avoid using Runtime exec with untrusted input
System.out.println("Listing directory contents..."); // Vulnerable: Untrusted input could be injected
    }
}
