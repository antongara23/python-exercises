from typing import Sequence


def myxml(tag: str, text="", **kwargs) -> str:
    kwargs = [f" {key}=\"{value}\"" for key, value in kwargs.items()]
    return f"<{tag}" + "".join(kwargs) + ">" + text + f"</{tag}>"


def copyfile(input_file: str, *args: str):
    """Takes one mandatory argument—the name of an input file—and any
    number of additional arguments: the names of files to which the
    input should be copied."""
    def make_copy(copy, source):
        with open(copy, "wt") as copy_file:
            for line in source:
                copy_file.write(line)

    with open(input_file, "rt") as source_file:
        source_file_content = source_file.read()
        for copy_name in args:
            make_copy(copy_name, source_file_content)


def factorial(*args):  # Is not a real factorial function.
    """Takes any number of numeric arguments and returns the result of
    multiplying them all by one another."""
    result = 1
    for number in args:
        result *= number
    return result


def anyjoin(sequence: Sequence, sep: str = " ") -> str:
    """Works similarly to str.join, except that the first argument is a
    sequence of any types (not just of strings), and the second argument
    is the “glue” that we put between elements, defaulting to " "
    (a space)."""
    result = ""
    for element in sequence:
        result += str(element) + sep
    return result


if __name__ == "__main__":
    print(myxml("foo"))
    print(myxml("foo", a=1, b=2, c=3))
    print(myxml("foo", "bar", a=1, b=2, c=3))
    copyfile("../Files/text.txt", "copy1.txt", "copy2.txt", "copy3.txt")
    print(factorial(1, 2, 3, 4, 5))
    print(anyjoin([1, 2, 3]))
    print(anyjoin(["A", "N", "t"], "&"))
