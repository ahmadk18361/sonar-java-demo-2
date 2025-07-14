import java.io.*;

public class CmdInjectionArgsExample {
    public static void main(String[] args) throws IOException {
        if (args.length > 0) {
            // Vulnerable: directly using input from args[] without validation
            String command = "cmd.exe /c dir " + args[0];
            Runtime.getRuntime().exec(command);
        } else {
            System.out.println("Please provide a directory name.");
        }
    }
}
