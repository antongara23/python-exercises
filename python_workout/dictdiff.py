import sys
from typing import Callable


def dictdiff(dict1: dict, dict2: dict) -> dict:
    """Returns a new dict that expresses the difference between the two
    dicts."""
    output_dict = {}
    dicts_keys = dict1.keys() | dict2.keys()
    for key in dicts_keys:
        if dict1.get(key) != dict2.get(key):
            output_dict[key] = [dict1.get(key), dict2.get(key)]
    return output_dict


def update_dicts(dict1: dict, *args: dict) -> dict:
    """Takes any number of dicts and returns a dict that reflects the
    combination of all of them."""
    for i in args:
        dict1.update(i)
    return dict1


def make_dict(*args: any) -> dict:
    """Takes any even number of arguments and returns a dict based on
    them. The even-indexed arguments become the dict keys, while the
    odd-numbered arguments become the dict values."""
    if len(args)/2 != 0:
        print("Number of arguments should be even!")
        sys.exit()
    result_dict = {}
    for index, element in tuple(enumerate(args))[::2]:
        result_dict[element] = args[index+1]
    return result_dict


def dict_partition(d: dict, f: Callable) -> tuple[dict, dict]:
    """Takes one dict (d) and a function (f) as arguments. Return two
     dicts, each containing key-value pairs from d. f run on each
     key-value pair in d. If True - key-value pair put in the first
     output dict. If False - in the second."""
    dict1 = {}
    dict2 = {}
    for key, value in d.items():
        if f(key, value):
            dict1[key] = value
        else:
            dict2[key] = value
    return dict1, dict2


if __name__ == '__main__':
    a = {'a': 1, 'b': 2, 'c': 3}
    b = {'a': 1, 'b': 2, 'c': 4, 'd': 5}
    c = {'a': 1, 'b': 3, 'c': 5, 'd': 5, 'f': 0}
    print(dictdiff(a, b))
    print(update_dicts(a, b, c))
    a = ('a', 1, 'b', 2)
    print(make_dict('a', 1, 'b', 2))
