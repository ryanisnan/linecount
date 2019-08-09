import sys
import os
import subprocess
import io
import binascii
import re


def count_pygount_output(output):
    count = 0
    for line in output.splitlines():
        match = re.match("^\d+", line)
        if match:
            count += int(match.group(0))
    return count



def count_dir_py_loc(directory_path):
    # output = io.StringIO()
    results = subprocess.run(f"pygount --suffix=py {directory_path}".split(), capture_output=True, encoding="utf-8")
    if results.stdout:
        count = count_pygount_output(results.stdout)
        print(directory_path.rsplit("/", 1)[-1], "\t", count)


def main():
    for x in os.scandir(sys.argv[1]):
        if x.is_dir():
            count_dir_py_loc(x.path)

if __name__ == "__main__":
    main()