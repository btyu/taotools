import os


def ensure_dirs(path: str) -> None:
    """
    Check whether the directory exists. Create if not.
    :param path: directory
    :return: None
    """
    if not (os.path.exists(path) and os.path.isdir(path)):
        os.makedirs(path)
