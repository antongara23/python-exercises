from final_line import try_open_file
from os import stat, listdir


@try_open_file
def wordcount(text_file: str):
    """Take a filename as input and print four lines of output:
        1 Number of characters (including whitespace)
        2 Number of words (separated by whitespace)
        3 Number of lines
        4 Number of unique words (case sensitive)"""
    with open(text_file, 'rt') as file:
        results = {"characters": 0,
                   "words": 0,
                   "lines": 0,
                   "unique words": 0}
        words = []
        for line in file:
            results["characters"] += len(line)
            results["words"] += len(line.split())
            results["lines"] += 1
            words.extend(line.split())
        results["unique words"] = len(set(words))
        for line, result in results.items():
            print("Number of " + line + ":", result)


@try_open_file
def specific_wordcount() -> dict:
    """Asks user for a file path, than for words to find and count."""
    filename = input("Enter file path:\n")
    words = input("Enter words separated with spaces:\n").split()
    with open(filename, 'rt') as file:
        result = {}
        for word in words:
            result[word] = 0
        for line in file:
            line_words = line.split()
            for word in words:
                if word in line_words:
                    result[word] = result.get(word, 0) + 1
    return result


@try_open_file
def files_size(*args: str) -> dict:
    """Takes paths of files and returns dict with path: size_in_bytes
    key-value pairs"""
    fsizes = {}
    for filename in args:
        fsizes[filename] = stat(filename).st_size
    return fsizes


@try_open_file
def dir_letters_count(path: str) -> dict:
    """Return a dict with 5 most common letters in directory (path)."""
    files = listdir(path)
    result = {}

    def count_letters(filename: str):
        with open(filename, "rt") as file:
            for line in file:
                for ch in line:
                    if ch.isalpha():
                        result[ch.lower()] = result.get(ch, 0) + 1
    for filename in files:
        if not filename.startswith(("_", ".")):
            count_letters(filename)
    return dict(sorted(result.items(), key=lambda x: x[1], reverse=True)[:5])


if __name__ == "__main__":
    wordcount("text.txt")
    print(specific_wordcount())
    print(files_size("text.txt"))
    print(dir_letters_count("../Files"))
