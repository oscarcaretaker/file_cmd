# Author : AMAN TIWARI
# MCA - 25112031
# Assigment 2

import os, sys
from pathlib import Path


# this function returns true if file is ASCII Text. (ASCII TEXT, EMPTY FILES)
def is_ascii(path):
    with open(path, "rb") as f:
        data = f.read()
        for i in data:
            if not (32 <= i <= 126 or i in (9, 10, 13)):
                return False
        if len(data) == 0:
            print(f"{path} = Empty File")
        else:
            print(f"{path} = ASCII Text file")
        return True


# HTML FILES
def is_html(file_path):
    with open(file_path, "rb") as f:
        data = f.read(200).lower()
    return b"<html" in data or b"<!doctype html" in data


root = str(Path.cwd())  # getting the current path
if len(sys.argv) != 2:
    print("Enter file name once")
    exit(0)
name = sys.argv[1]  # file name is assigned to argv[1]
file_path = root + "/" + name


# symbolic link files
def is_symlink(path):
    return os.path.islink(path)


try:
    with open(file_path, "rb") as f:
        m4type = f.read(8)  # reading 8 bytes
        #    print(m4type)
        magic_number = {
            "7f454c46": "Executable file / Binary Files",
            "25504446": "pdf file",
            "504b0304": "Zip File",
            "47494638": "Gif file",
            "89504e470d0a1a0a": "PNG file",
            "FFD8FF": "JPEG file",
        }

        if is_symlink(file_path):
            print(f"{file_path} = Symlink File")
            exit(0)

        if m4type.hex()[:8] in magic_number:  # 4 byte types checker
            print(f"{file_path} = {magic_number[m4type.hex()[:8]]}")
            exit(0)
        if m4type.hex()[:6] in magic_number:
            print(f"{file_path} = {magic_number[m4type.hex()[:6]]}")
            exit(0)
        if m4type.hex() in magic_number:
            print(f"{file_path} = {magic_number[m4type.hex()]}")
            exit(0)

        if is_html(file_path):
            print(f"{file_path} = HTML FILE")
            exit(0)
        if is_ascii(file_path):
            exit(0)
        print("Connot Identify Files")

    f.close()

except FileNotFoundError:
    print("File Not exist")

except PermissionError:
    print("Permission Denied to open file")

except IsADirectoryError:
    print(f"{file_path} = Directory")
