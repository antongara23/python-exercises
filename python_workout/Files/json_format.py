import json
from final_line import try_open_file
import os
from glob import glob
import pathlib


def test_scores(school_class: str):
    """Print the highest, lowest, and average test scores for each subject
    in each class from JSON file like:
    [{"math" : 90, "literature" : 98, "science" : 97},
    {"math" : 65, "literature" : 79, "science" : 85} ... ]."""
    with open(school_class, "rt") as file:
        content = file.read()
        from_json = json.loads(content)
        subjects = {}
        for key in from_json[0].keys():
            subjects[key] = []
            for dictionary in from_json:
                subjects[key].append(dictionary[key])
        output_dict = {}
        for key in subjects:
            output_dict[key] = [{"min": min(subjects[key])},
                                {"max": max(subjects[key])},
                                {"avg": sum(subjects[key])/len(subjects[key])}]
    return output_dict


@try_open_file
def csv_to_json(filename: str):
    """Convert /etc/passwd from a CSV-style file into a JSON-formatted file.
    The JSON file contain the equivalent of a list of Python tuples, with
    each tuple representing one line from the file."""
    with open(filename, "rt", newline="") as file, \
            open("passwd.json", "wt") as jsonfile:
        data_list = [tuple([line.strip()]) for line in file if not line.startswith((
            "#", "\n"))]
        print(data_list)
        json.dump(data_list, jsonfile, indent=2)


@try_open_file
def csv_to_json_dict(filename: str):
    """Convert /etc/passwd from a CSV-style file into a JSON-formatted
    file. The JSON file contain the equivalent of a list of Python
    dictionaries, with each tuple representing one line from the file."""
    with open(filename, "rt", newline="") as file, \
            open("passwd_dicts.json", "wt") as jsonfile:
        field_names = ["Username", "Password", "User ID", "Group ID",
                       "User Info", "Home Directory", "Login Shell"]
        data_list = []
        for line in file:
            if not line.startswith(("#", "\n")):
                line_dict = {}
                for name, field in zip(field_names, line.strip().split(":")):
                    line_dict[name] = field
                data_list.append(line_dict)
        print(data_list)
        json.dump(data_list, jsonfile, indent=2)


@try_open_file
def files_stat(path: str):
    """Take a directory path as an argument. Iterate through each file
    in that directory (ignoring subdirectories), getting (via os.stat)
    the size of the file and when it was last modified. Create a
    JSON-formatted file on disk listing each file-name, size, and
    modification timestamp. Then read the file back in, and identify
    which files were modified most and least recently, and which files
    are largest and smallest, in that directory."""
    a = pathlib.Path(path)
    files_info = []
    for file in a.iterdir():
        if file.is_file():
            file_size = os.stat(file.absolute()).st_size
            time_modified = os.stat(file.absolute()).st_mtime
            files_info.append([file.name, file_size, time_modified])
    with open("files_info.json", "wt") as jsonfile:
        json.dump(files_info, jsonfile, indent=2)
    with open("files_info.json", "rt") as jsonfile:
        files_info = json.load(jsonfile)
    min_size = min(files_info, key=lambda x: x[1])
    max_size = max(files_info, key=lambda x: x[1])
    least_recent_mod = min(files_info, key=lambda x: x[2])
    most_recent_mod = max(files_info, key=lambda x: x[2])
    output_dict = ({"Smallest file": min_size[0], "Size": min_size[1]},
                   {"Largest file": max_size[0], "Size": max_size[1]},
                   {"Least recently modified": least_recent_mod[0],
                    "Timestamp": least_recent_mod[2]},
                   {"Most recently modified": most_recent_mod[0],
                    "Timestamp": most_recent_mod[2]})
    return output_dict


if __name__ == "__main__":
    print(test_scores("9a.json"))
    csv_to_json("/etc/passwd")
    csv_to_json_dict("/etc/passwd")
    for i in files_stat("/etc/"):
        print(i)
