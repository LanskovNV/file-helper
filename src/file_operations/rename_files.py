#!/usr/bin/env python3.9

import os
import re


# Globals
pathToFiles = "/Users/leins275/Data/Storage/Книги/Books"

def get_filenames(path):
    fileSearcher = os.walk(path) 
    return list(fileSearcher)[0][2] 

def get_fullpath(path, fname):
    return os.path.join(path, fname)

def rename_all_files(old_names, new_names): 
    num_files = len(old_names) 
    for i in range(num_files): 
        old_name = get_fullpath(pathToFiles, old_names[i])
        new_name = get_fullpath(pathToFiles, new_names[i])
        os.rename(old_name, new_name)

def print_files_arr(arr): 
    for _ in arr:
        print(_)

def process_filename(filename):
    name, extension = filename.rsplit('.', 1)
    new_name = re.sub("[\W_]+", "", name) 
    return f'{new_name}.{extension}'


if __name__ == "__main__":
    names = get_filenames(pathToFiles)
    new_names = map(process_filename, names)
    rename_all_files(names, list(new_names))
