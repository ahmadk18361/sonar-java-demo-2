import java.io.*;

public class CmdInjectionBufferedReader {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter a directory name: ");
        String userInput = reader.readLine();

        // Vulnerable: Untrusted input could be injected here
        String command = "cmd.exe /c dir " + userInput;
        Runtime.getRuntime().exec(command);
    }
}
