import os
import re

# Path to the folder containing all vulnerable .java files
SOURCE_DIR = "src/main/java/com/example/ ."

# CVE-safe command wrapper
SAFE_COMMAND = '''\
        // REMEDIATED: Validated command input
        if (command.matches("^[a-zA-Z0-9_./\\\\-]+$")) {
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
        if 'Runtime.getRuntime().exec' in line:
            # Extract the variable holding the command (e.g., command)
            match = re.search(r'Runtime\.getRuntime\(\)\.exec\((.*)\);', line)
            if match:
                command_var = match.group(1).strip()
                new_lines.append(f"        String command = {command_var};\n")
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
    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith(".java"):
            filepath = os.path.join(SOURCE_DIR, filename)
            remediate_file(filepath)

if __name__ == "__main__":
    run_remediation()
