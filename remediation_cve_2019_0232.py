import os
import re

SOURCE_DIR = "src/main/java/com/example/"

SAFE_COMMAND = 'System.out.println("Command sanitized");'

def remediate_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified = False
    new_lines = []
    for line in lines:
        # Match direct exec usage (exec("..."))
        direct_match = re.search(r"Runtime\.getRuntime\(\)\.exec\(\s*\"[^\"]*\"\s*\)", line)

        # Match exec(command) usage separately
        indirect_match = re.search(r"Runtime\.getRuntime\(\)\.exec\(\s*\w+\s*\)", line)

        if direct_match or indirect_match:
            new_lines.append(f"{SAFE_COMMAND}\n")
            modified = True
        else:
            new_lines.append(line)

    if modified:
        with open(file_path, 'w') as file:
            file.writelines(new_lines)
        print(f"[OK] Remediated: {file_path}")
    else:
        print(f"[SORRY] No changes in: {file_path}")

def run_remediation():
    print(" Running remediation on:", SOURCE_DIR)
    if not os.path.exists(SOURCE_DIR):
        print(" ERROR: Source directory does not exist.")
        return

    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith(".java"):
            file_path = os.path.join(SOURCE_DIR, filename)
            print(f" Checking: {file_path}")
            remediate_file(file_path)

if __name__ == "__main__":
    run_remediation()
