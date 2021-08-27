import os
from tqdm import tqdm


def remove_empty_subdirs(root):
    subs = list(os.walk(root))
    for subdir in tqdm(subs[1:]):
        if not subdir[1] and not subdir[2]:
            os.rmdir(subdir[0])
