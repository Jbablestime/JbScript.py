import argparse
import os
import sys
import time

variables = {}

def send(message):
    print("Sending message:", message)

def wait(duration):
    print("Waiting for", duration, "seconds")
    time.sleep(duration)

def variable(name, value):
    variables[name] = value

def run_code(file_name):
    with open(file_name, 'r') as file:
        code = file.read()
        exec(code, globals(), variables)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="My Custom Coding Language")
    parser.add_argument("file_name", help="Path to the .jb file")
    parser.add_argument("-s", "--silent", action="store_true", help="Run in silent mode (no output)")

    args = parser.parse_args()

    file_name = args.file_name
    if not file_name.endswith(".jb"):
        print("Invalid file extension. The file must have a .jb extension.")
        sys.exit(1)

    if args.silent:
        # Redirect stdout to null for silent mode
        sys.stdout = open(os.devnull, "w")

    run_code(file_name)
