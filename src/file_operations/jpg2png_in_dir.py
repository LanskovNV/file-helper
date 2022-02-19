import os
import subprocess

from loguru import logger
from tqdm import tqdm

rename_command = "convert \"{}\".jpg \"{}\".png"

def rename_all_jpg2png(path: str = "") -> None:
    cnt = 0
    files = list(os.walk(path))
    files = files[0][2]
    try:
        for file in tqdm(files):
            filename, *rest = file.split(".")
            filename = os.path.join(path, filename)
            extension = rest[-1]
            if extension == "jpg":
                cnt += 1
                subprocess.call([
                    "convert",
                    f"{filename}.jpg",
                    f"{filename}.png"])
                subprocess.call([
                    "rm",
                    f"{filename}.jpg"
                    ])
        logger.info(f"total: {cnt}")
    except Exception as ex:
        logger.info(ex)
