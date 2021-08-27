#!/usr/bin/python
import os
import sys
from tqdm import tqdm

def process_sys_argv(args):
    if len(args) != 2:
        print('Incorrect input params')
        return 1
    return args[1]

def remove_empty_subdirs(args):
    root = process_sys_argv(sys.argv)
    if root == 1:
        return
    subs = list(os.walk(root))
    for subdir in tqdm(subs[1:]):
        if not subdir[1] and not subdir[2]:
            os.rmdir(subdir[0])

if __name__ == '__main__':
    remove_empty_subdirs(sys.argv)

