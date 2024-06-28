#!/bin/python

import os

def rename_files():
    cwd = os.getcwd()
    script_name = os.path.basename(__file__)
    
    files = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]
    
    files = [f for f in files if f != script_name]
    
    for i, filename in enumerate(files, start=1):
        file_extension = os.path.splitext(filename)[1]
        new_filename = f"{i}{file_extension}"
        os.rename(os.path.join(cwd, filename), os.path.join(cwd, new_filename))
        print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    rename_files()
