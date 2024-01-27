import sys


def try_open_file(func):
    """Check if file exists. Exit with error message if no."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OSError as e:
            sys.exit(e.strerror)
    return wrapper


@try_open_file
def get_final_line(text_file: str) -> str:
    """Return last line of a file."""
    with open(text_file, 'rt') as file:
        for line in file:
            last_line = line
        return last_line


@try_open_file
def files_int_sum(text_file: str) -> int:
    """Find words that contain only integers return sum."""
    with open(text_file, 'rt') as file:
        nums_sum = 0
        for line in file:
            for word in line.split():
                if word.isdecimal():
                    nums_sum += int(word)
        return nums_sum


@try_open_file
def multiply_num_columns(text_file: str) -> int:
    """Find two tab-separated columns, with each column containing a number.
    Return sum of multiplication products of each row."""
    with open(text_file, 'rt') as file:
        nums_sum = 0
        for line in file:
            line = line.split()
            if len(line) == 2 and line[0].isdecimal() and line[1].isdecimal():
                nums_sum += int(line[0]) * int(line[1])
        return nums_sum


@try_open_file
def vowel_amount(text_file: str) -> dict:
    """Check how many times each vowel (a, e, i, o, and u) appears in the
    file."""
    with open(text_file, 'rt') as file:
        vowels = {}
        for line in file:
            for ch in line:
                if ch.lower() in "aeiou":
                    vowels[ch] = vowels.get(ch, 0) + 1
        return vowels


if __name__ == "__main__":
    print(get_final_line('text.txt'))
    print(files_int_sum('text.txt'))
    print(multiply_num_columns('text.txt'))
    print(vowel_amount('text.txt'))
