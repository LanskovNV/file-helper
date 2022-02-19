import sys

from loguru import logger

from file_operations.move_all_to_root import move_all_to_root
from file_operations.remove_empty_subdirs import remove_empty_subdirs
from file_operations.jpg2png_in_dir import rename_all_jpg2png
from file_operations.rename_images import rename_images

class ExceptionInMain(Exception):
    pass

def main(path: str = "") -> None:
    try:
        # move_all_to_root(path)
        # remove_empty_subdirs(path)
        # rename_all_jpg2png(path)
        rename_images(path)
    except Exception as ex:
        raise ExceptionInMain("Oops... failed in main") from ex


if __name__ == '__main__':
    try:
        base_path = sys.argv[1]
        main(base_path)
    except ExceptionInMain as ex:
        logger.error(ex)
    except Exception:
        logger.error("You forgot specify base path as script arg")

