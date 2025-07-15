import os
import re

SOURCE_DIR = "src/main/java/com/example/"

# Replace any input to exec(...) with this safer wrapper
SAFE_COMMAND = (
    'if (command.matches("^[a-zA-Z0-9_.\\\\\\-/ ]+$")) {\n'
    '            Runtime.getRuntime().exec(command);\n'
    '        } else {\n'
    '            throw new IllegalArgumentException("Invalid command input.");\n'
    '        }'
)

def remediate_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    new_lines = []
    modified = False

    for line in lines:
        match = re.search(r'Runtime\.getRuntime\(\)\.exec\((.*?)\);', line)
        if match:
            command_var = match.group(1).strip()
            print(f"[DEBUG] Found vulnerable exec in {file_path}: {line.strip()}")

            new_lines.append(SAFE_COMMAND + "\n")
            modified = True
        else:
            new_lines.append(line)

    if modified:
        with open(file_path, "w") as file:
            file.writelines(new_lines)
        print(f"[INFO] Remediated: {file_path}")
    else:
        print(f"[SKIPPED] No vulnerable code found in {file_path}")

def run_remediation():
    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith(".java"):
            file_path = os.path.join(SOURCE_DIR, filename)
            remediate_file(file_path)

if __name__ == "__main__":
    run_remediation()
