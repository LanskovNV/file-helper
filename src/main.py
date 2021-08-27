from file_operations.move_all_to_root import move_all_to_root
from file_operations.remove_empty_subdirs import remove_empty_subdirs

if __name__ == '__main__':
    base_path = '/Users/leins275/Data/Storage/Книги/Books'
    remove_empty_subdirs(base_path)
    # move_all_to_root(base_path)
