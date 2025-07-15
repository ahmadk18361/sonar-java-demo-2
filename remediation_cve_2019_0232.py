import os
import re

# path to the folder containing all vulnerable .java files
SOURCE_DIR = "src/main/java/com/example/"

# DEBUG: Show working directory and target source folder
print("Current working directory:", os.getcwd())
print("Target source folder (relative):", SOURCE_DIR)
print("Absolute path:", os.path.abspath(SOURCE_DIR))

# CVE-safe command wrapper
SAFE_COMMAND = '''
// REMEDIATED: Validated command input
if (command.matches("^[a-zA-Z0-9._/-]+$")) {
    Runtime.getRuntime().exec(command);
} else {
    throw new IllegalArgumentException("Invalid command input.");
}
'''

def remediate_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified = False
    new_lines = []

    for line in lines:
        # match the variable holding the command (e.g., command)
        match = re.search(r'Runtime\.getRuntime\(\)\.exec\((.*)\)', line)
        if match:
            command_var = match.group(1).strip()
            new_lines.append(f"    String command = {command_var};\n")
            new_lines.append(SAFE_COMMAND)
            modified = True
        else:
            new_lines.append(line)

    if modified:
        with open(file_path, 'w') as file:
            file.writelines(new_lines)
        print(f"[+] Remediated: {file_path}")
    else:
        print(f"[-] No changes made: {file_path}")

def run_remediation():
    print("Running remediation...")
    if not os.path.exists(SOURCE_DIR):
        print("ERROR: SOURCE_DIR does not exist.")
        return

    for filename in os.listdir(SOURCE_DIR):
        print("Checking file:", filename)  # DEBUG: See what's being processed
        if filename.endswith(".java"):
            file_path = os.path.join(SOURCE_DIR, filename)
            remediate_file(file_path)

if __name__ == "__main__":
    run_remediation()
