from final_line import try_open_file


@try_open_file
def passwd_to_dict(text_file: str) -> dict:
    """Returns a dict from a Unix-style password file, contains
    username: ID key-value pairs."""
    with open(text_file, 'rt') as file:
        users = {}
        for line in file:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2])
    return users


@try_open_file
def login_shell(text_file: str) -> dict:
    """Returns a dict from a Unix-style password file, contains
    shell: [usernames] key-value pairs."""
    with open(text_file, 'rt') as file:
        users = {}
        for line in file:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                shell = user_info[-1].rstrip()
                users[shell] = users.get(shell, [])
                users[shell].append(user_info[0])
    return users


def nums_factors() -> dict:
    """Returns a dict contains factors for numbers from user input."""
    numbers = input("Enter number separated by spaces:\n")
    numbers = list(map(int, numbers.split()))
    factors = {}
    for num in numbers:
        factors[num] = []
        for i in range(num, 0, -1):
            if num % i == 0:
                factors[num].append(i)
    return factors


@try_open_file
def user_info(text_file: str) -> dict:
    """Return a dict from Unix-style password file, where keys are
    usernames and values are dicts with user ID, home directory, shell.
    """
    with open(text_file, 'rt') as file:
        users = {}
        for line in file:
            if not line.startswith(('#', '\n')):
                user_attr = line.split(':')
                # Creates a dict contains 'username: [attributes]'
                users[user_attr[0]] = {'User ID': user_attr[2],
                                       'Home directory': user_attr[-2],
                                       'Shell': user_attr[-1]}
        return users


if __name__ == "__main__":
    print(passwd_to_dict("/etc/passwd"))
    for item in login_shell("/etc/passwd").items():
        print(item)
    print(nums_factors())
    print(user_info("/etc/passwd"))

