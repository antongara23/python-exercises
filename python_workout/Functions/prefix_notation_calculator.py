import operator
from typing import Sequence, Callable


def calc(arg: str) -> int:
    """Perform calculations of a string containing a simple math
    expression in prefix notation in form: 'operator num1 num2'"""
    ab = arg.strip().split()
    a = int(ab[1])
    b = int(ab[2])
    match ab[0]:
        case "*":
            return a * b
        case "/":
            return a / b
        case "+":
            return a + b
        case "-":
            return a - b
        case "%":
            return a % b
        case "**":
            return a ** b
        case _:
            return "Incorrect operator"


def calc_adv(arg: str) -> int:
    """Like calc function, but takes any number of nums."""
    ab = arg.strip().split()
    match ab[0]:
        case "*":
            op = operator.mul
        case "/":
            op = operator.truediv
        case "+":
            op = operator.add
        case "-":
            op = operator.sub
        case "%":
            op = operator.mod
        case "**":
            op = operator.pow
        case _:
            return "Incorrect operator"
    result = int(ab[1])
    for index, num in enumerate(ab[1:-1], 1):
        result = op(result, int(ab[index+1]))
    return result


def apply_to_each(func: Callable[[any], any], seq: Sequence) -> Sequence:
    """Analog of map function."""
    new_seq = []
    for element in seq:
        new_seq.append(func(element))
    return new_seq


def transform_lines(func: Callable[[any], any],
                    input_file: str, output_file: str):
    """Takes three arguments: a function that takes a single argument,
    the name of an input file, and the name of an output file. Calling
    the function will run the function on each line of the input file,
    with the results written to the output file."""
    with open(input_file, "rt") as infile, open(output_file, "wt") as \
            outfile:
        for line in infile:
            outfile.write(func(line))


if __name__ == "__main__":
    print(calc("*f* 2 4"))
    print(calc_adv("** 2 2 2"))
    print(apply_to_each(int, ['1', '2', '3']))
    print(list(map(int, ['1', '2', '3'])))


    def some_func(line):
        return line.upper()


    transform_lines(some_func, "text.txt", "textf.txt")
