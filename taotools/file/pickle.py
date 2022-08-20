import pickle
import os
from .file_operations import ensure_dirs


def pickle_save(obj: object, path: str) -> None:
    """
    Dump an object as a file with pickle. The folder will be created if not existed.
    :param path: path where the file should be saved.
    :param obj: the object to save.
    :return: None.
    """
    dir_name = os.path.dirname(path)
    ensure_dirs(dir_name)
    with open(path, 'wb') as f:
        pickle.dump(obj, f)


def pickle_load(path: str) -> object:
    """
    Load an object from file with pickle.
    :param path: the file path to load.
    :return: the loaded_object.
    """
    with open(path, 'rb') as f:
        obj = pickle.load(f)

    return obj
