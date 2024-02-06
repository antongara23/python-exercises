from typing import Sequence


def sum_numbers(seq: Sequence) -> int:
    """
    Take a sequence of strings, turn them into numbers, return sum.
    Filter out strings that can’t be turned into integers.
    """
    return sum(int(num.strip()) for num in seq if num.strip().isdigit())


def lines_filter(file_name: str) -> tuple[str]:
    """
    Return list of lines of a text file that contain at least one vowel
    and contain more than 20 characters.
    """
    def check_condition(line: str) -> bool:
        if len(line.strip()) > 20:
            for ch in "aeiou":
                if line.find(ch) != -1:
                    return True
        return False

    with open(file_name, "rt") as file:
        return tuple(line.strip() for line in file if check_condition(line))


def new_phone_number(seq: list[str]) -> list[str]:
    """
    Takes a list of strings containing phone numbers in format:
    XXX-YYY-ZZZZ. Return a new list of strings, in which any phone
    number whose YYY begins with the digits 0–5 will have its area code
    changed to XXX+1.
    """
    def change_code(num: str) -> str:
        num = num.split("-")
        if num[1][0] in "012345":
            num[0] = str(int(num[0]) + 1)
        return "-".join(num)

    return [change_code(num) for num in seq]


def age_in_months(persons: list[dict[str, int]]) -> list[dict[str, int]]:
    """
    Take a list of dicts each having two key-value pairs, name and
    age(in years). Return a list of dicts in which each dict contains
    three key-value pairs: the originals and a third age_in_months key,
    containing the person’s age in months.
    """
    return [{**person, "age_in_month": person["age"] * 12} for person in
            persons]


if __name__ == "__main__":
    print(sum_numbers([' 10', 'asvb', '90', 'asf9r']))
    print(lines_filter("text.txt"))
    print(new_phone_number(['123-456-7890', '123-333-4444', '123-777-8888']))

    dictionaries = [{"name": "anton", "age": 25},
                    {"name": "alice", "age": 21},
                    {"name": "boris", "age": 52},
                    {"name": "andrew", "age": 43},
                    {"name": "john", "age": 32}
                    ]
    print(age_in_months(dictionaries))
