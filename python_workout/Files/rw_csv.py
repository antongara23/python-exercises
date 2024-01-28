import csv
import random
from final_line import try_open_file


@try_open_file
def passwd_to_csv(source_file: str, target_file: str):
    """Read username and ID from the source_file (Unix-style password
    file) and write them to the csv file with TAB as delimiter."""
    with open(source_file, newline="") as sfile, \
            open(target_file, "wt", newline="") as tfile:
        reader = csv.reader(sfile, delimiter=":")
        writer = csv.writer(tfile, delimiter="\t")
        for row in reader:
            if not row[0].startswith(("#", "\n")):
                writer.writerow([row[0], row[2]])


@try_open_file
def csv_maker():
    """Ask for space-separated list of integers, indicating which fields
    Unix password file should be written to the output CSV file. Ask
    for delimiter. Read from /etc/passwd, writing the user’s chosen fields,
    separated by the user’s chosen delimiter."""
    with open("/etc/passwd", newline="") as sfile, \
            open("csv_file.csv", "wt", newline="") as file:
        indexes = input("Enter space separated list of integers:").split()
        delimiter = input("Choose delimiter:")
        reader = csv.reader(sfile, delimiter=":")
        writer = csv.writer(file, delimiter=delimiter)
        for row in reader:
            if not row[0].startswith(("#", "\n")):
                writer.writerow([row[int(index)] for index in indexes])


@try_open_file
def dict_to_csv(dictionary: dict):
    with open("from_dict.csv", "wt", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        for key, value in dictionary.items():
            writer.writerow([key, value, type(value).__name__])


@try_open_file
def sum_from_csv(filename: str) -> list:
    """Read a csv file contains rows of integers. Sum integers from each
    row and return list of sums."""
    with open(filename, "rt", newline="") as file:
        sums = []
        reader = csv.reader(file)
        for row in reader:
            sums.append(sum([int(i) for i in row]))
    return sums


if __name__ == "__main__":
    passwd_to_csv("/etc/passwd", "psw.csv")
    csv_maker()
    dictionary = {"one": 1, "two": "2", "three": [3]}
    dict_to_csv(dictionary)
    with open("integers.csv", "wt", newline="") as file:
        writer = csv.writer(file)
        for i in range(10):
            writer.writerow([random.randint(10, 100) for i in range(10)])
    sum_from_csv("integers.csv")
