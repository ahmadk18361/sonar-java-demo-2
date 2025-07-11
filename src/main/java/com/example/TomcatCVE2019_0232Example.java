import java.io.*;

public class TomcatCVE2019_0232Example {
    public static void main(String[] args) throws IOException {
        String command = "cmd.exe /c dir";
        Runtime.getRuntime().exec(command); // Vulnerable: Untrusted input could be injected
    }
}
