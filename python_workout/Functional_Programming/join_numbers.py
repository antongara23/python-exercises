from typing import Iterable


def join_numbers(nums: Iterable) -> str:
    """
    Take a range of integers. Return integers as a string, with
    commas between the numbers.
    """
    return ','.join(str(i) for i in nums)


def join_numbers_one_to_ten(nums: Iterable) -> str:
    """
    Take a range of integers. Return integers in range from 0 to 10 as a
    string, with commas between the numbers.
    """
    return ','.join(str(i) for i in nums if i in range(0, 11))


def hex_sum(hex_nums: list) -> int:
    """
    Take a list of strings containing hexadecimal numbers. Return sum
    of those numbers.
    """
    return sum(int(i, 16) for i in hex_nums)


def revers_words_order(file_name: str) -> list:
    """
    Read file and return list of strings containing words from each line
    in reverse order.
    """
    with open(file_name, "rt") as file:
        return [' '.join(line.split()[::-1]) for line in file]


if __name__ == "__main__":
    print(join_numbers(range(15)))
    print(join_numbers_one_to_ten(range(15)))
    print(hex_sum(['f', 'f', '2', 'a']))
    print(revers_words_order("text.txt"))
