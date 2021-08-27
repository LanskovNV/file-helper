import os


def create_subfolders(path, n):
    for i in range(n):
        subfolder = os.path.join(path, f'{i + 1}')
        os.makedirs(subfolder, exist_ok=True)
    print(f'{n} subfolders created successfully in {path}')


def separate_files(path, n):
    books = list(os.walk(path))[0][2]
    if len(books) < n:
        return

    create_subfolders(path, n)
    for index, book in enumerate(books):
        os.rename(os.path.join(path, book), os.path.join(path, f'{index % n + 1}', book))

    for i in range(n):
        separate_files(os.path.join(path, f'{i + 1}'), n)
