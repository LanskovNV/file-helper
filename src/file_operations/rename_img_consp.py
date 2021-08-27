#!/usr/bin/python
import os
import sys
from tqdm import tqdm


def get_image_names_from_args():
    path = sys.argv[1]
    img_names = list(os.walk(path))[0][2]
    return img_names


def rename_images(images):
    images = sorted(images)
    length = len(images)
    for i, _ in enumerate(tqdm(images)):
        os.rename(_, f"{length - i}.jpg")

if __name__ == "__main__":
    img_names = get_image_names_from_args()
    rename_images(img_names)
