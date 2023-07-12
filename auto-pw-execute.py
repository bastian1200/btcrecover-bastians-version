import subprocess
import time

# Function to read commands from a file
def read_commands(file_name):
    with open(file_name, 'r') as file:
        commands = file.readlines()
    return commands

commands = read_commands('commands.txt')

for command in commands:
    command = command.strip()  # remove newline characters
    print(f"Running command: {command}")
    process = subprocess.Popen(command, shell=True)

    # Loop while the process is running
    while process.poll() is None:
        time.sleep(1)  # Wait for 1 second

    # Now that the process has finished, read its output
    output, _ = process.communicate()
    output = output.decode() if output else "No output"
    print(f"Command output: {output}")  # decode the output from bytes to string

    if "Password found" in output:  # replace this with the actual success message
        print("Password found, stopping execution.")
        break