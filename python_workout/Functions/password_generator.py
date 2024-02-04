import random
import string
from typing import Callable


def create_password_generator(from_str: str) -> Callable[[int], str]:
    """Takes a string as argument to generate passwords from. Returns a
    password generator function that takes an integer argument (length)
    and returns a password composed of characters from the provided
    string."""
    def return_fun(length: int):
        password = ""
        for i in range(length):
            password = password + random.choice(from_str)
        return password
    return return_fun


def create_password_checker(min_uppercase: int,
                            min_lowercase: int,
                            min_punctuation: int,
                            min_digits: int) -> Callable[[str], bool]:
    """Creates a password checker function. Takes integers as criteria
    for number of uppercase, lowercase, punctuation, digits characters.
    Returns a function that takes a password as input and returns True
    if it meets the specified criteria, False otherwise."""
    def return_fun(password: str):
        is_applicable = False
        lc = uc = punc = dig = 0
        for ch in password:
            if ch in string.ascii_lowercase:
                lc += 1
            elif ch in string.ascii_uppercase:
                uc += 1
            elif ch in string.punctuation:
                punc += 1
            elif ch in string.digits:
                dig += 1
            else:
                return False
        if lc >= min_lowercase and uc >= min_uppercase and punc >= \
                min_punctuation and dig >= min_digits:
            is_applicable = True
        return is_applicable
    return return_fun


def getitem(element: any) -> Callable[[dict], any]:
    """Analog of operator.itemgetter."""
    def getter(dictionary: dict):
        return dictionary[element]
    return getter


def doboth(func1: Callable[[any], any],
           func2: Callable[[any], any]) -> Callable[[any], any]:
    """Takes two functions as arguments (func1 and func2) and returns a
    single function, g. Invoking g(x) should return the same result as
    invoking func2(func1(x))."""
    def g(arg: any):
        return func2(func1(arg))
    return g


if __name__ == "__main__":
    alphanum = string.ascii_letters + string.digits
    password_generator = create_password_generator(alphanum)
    print(password_generator(8))
    password_checker = create_password_checker(1,1,1,1)
    print(password_checker("1a,C"))
    print(password_checker("aa,C"))
    a = getitem('a')
    print(a({'a': 1, 'b': 2}))
    both = doboth(all, int)
    print(both([1, 2, 3]))
    print(both([1, 0, 3]))
