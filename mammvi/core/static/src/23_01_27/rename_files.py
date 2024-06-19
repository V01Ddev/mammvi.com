#!/bin/python

import os

def rename_files():
    # Get the current working directory
    cwd = os.getcwd()
    # Get the name of this script
    script_name = os.path.basename(__file__)
    
    # List all files in the current working directory
    files = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]
    
    # Filter out the script itself
    files = [f for f in files if f != script_name]
    
    # Rename each file
    for i, filename in enumerate(files, start=1):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]
        # Construct the new filename
        new_filename = f"{i}{file_extension}"
        # Rename the file
        os.rename(os.path.join(cwd, filename), os.path.join(cwd, new_filename))
        print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    rename_files()
