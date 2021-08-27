import os
from tqdm import tqdm


def move_all_to_root(root):
    cnt = 0
    subs = list(os.walk(root))
    for subdir in tqdm(subs[1:]):
        cnt += 1

        for f in subdir[2]:
            old_path = os.path.join(root, subdir[0], f)
            new_path = os.path.join(root, f)
            os.replace(old_path, new_path)
