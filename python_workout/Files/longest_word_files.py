from final_line import try_open_file
from os import listdir, path, stat, chdir
from hashlib import md5
from datetime import datetime
import re


@try_open_file
def find_longest_word(filename: str) -> str:
    """Returns the longest word found in the file."""
    with open(filename, "rt") as file:
        longest_word = ""
        for line in file:
            longest_word_in_line = max(line.split(), key=len, default="")
            if len(longest_word_in_line) > len(longest_word):
                longest_word = longest_word_in_line
    return longest_word


@try_open_file
def find_all_longest_words(dir_path: str) -> str:
    files = listdir(dir_path)
    longest_word = []
    chdir(dir_path)
    for filename in files:
        if path.isfile(filename) and not filename.startswith(("_", ".")):
            longest_word.append(find_longest_word(filename))
    return max(longest_word, key=len, default="")


@try_open_file
def file_hash(dir_path: str) -> dict:
    """"""
    files = listdir(dir_path)
    hashes = {}
    chdir(dir_path)
    for filename in files:
        if path.isfile(filename) and not filename.startswith(("_", ".")):
            with open(filename, "rb") as file:
                content = file.read()
                hashes[filename] = md5(content).hexdigest()
    return hashes


@try_open_file
def dir_info(dir_path: str) -> dict:
    """Show all of the files in the directory and how long ago the directory
    was modified."""
    modified = stat(dir_path).st_mtime
    modified = datetime.fromtimestamp(modified)
    print("Directory was modified", datetime.now() - modified, "ago")
    for filename in listdir(dir_path):
        print(filename)


def http_log_codes(filename: str):
    """Return a dictionary of response codes and their occurrences in
    the given file."""
    status_code_pattern = re.compile(r'\s(\d{3})\s')
    codes = {}
    with open(filename, "rt") as file:
        for line in file:
            match = status_code_pattern.search(line)
            if match:
                status_code = match.group(1)
                codes[status_code] = codes.get(status_code, 0) + 1
    return codes


if __name__ == "__main__":
    print(find_longest_word("text.txt"))
    print(find_all_longest_words("."))
    print(file_hash("."))
    dir_info(".")
    print(http_log_codes("log.txt"))
