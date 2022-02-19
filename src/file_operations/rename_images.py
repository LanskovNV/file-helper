#!/usr/bin/python
import os

from tqdm import tqdm


def rename_images(path: str = "") -> None:
    images = list(os.walk(path))[0][2]

    for i, filename in tqdm(enumerate(images)):
        if filename.split(".")[-1] == "png":
            old = os.path.join(path, filename)
            new = os.path.join(path, f'{i + 1}.png')
            os.replace(old, new)

