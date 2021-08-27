#!/usr/bin/python
import codecs
import os
import sys
from tqdm import tqdm
from zipfile import ZipFile


sys.getdefaultencoding()

def process_sys_argv(args):
    if len(args) != 2:
        print('Incorrect input params')
        return 1
    return args[1]

def extract_archives(args):
    root = process_sys_argv(sys.argv)
    if root == 1:
        return
    subs = list(os.walk(root))
    for f in tqdm(subs[0][2]):
        print(f.encode('cp1251', errors='replace'))
#        if 'zip' in f.split('.'):
#            os.remove(os.path.join(subs[0][0], f))
#            with ZipFile(os.path.join(subs[0][0], f), 'r') as zip_ref:
#                zip_ref.extractall(os.path.join(subs[0][0], 'unzipped'))

if __name__ == '__main__':
    extract_archives(sys.argv)

