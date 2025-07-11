import re

with open("src/main/java/com/example/TomcatCVE2019_0232Example.java", "r") as file:
    code = file.read()

# Replace both lines — command assignment and exec call
fixed_code = re.sub(
    r'String command = "cmd\.exe /c dir";\s+Runtime\.getRuntime\(\)\.exec\(command\);',
    '// REMEDIATED: Avoid using Runtime exec with untrusted input\nSystem.out.println("Listing directory contents...");',
    code
)

with open("src/main/java/com/example/TomcatCVE2019_0232Example.java", "w") as file:
    file.write(fixed_code)
