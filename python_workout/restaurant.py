from datetime import date


MENU = {'sandwich': 10, 'tea': 7, 'coffee': 9}


def restaurant():
    """Ask the name of a dish on the menu. Print the price and the
    running total. If enter empty string, print the total and exist."""
    total = 0
    while True:
        item = input("Order: ")
        if not item:
            break
        if item in MENU:
            total += MENU[item]
            print(f"{item} costs {MENU[item]}, total is {total}.")
        else:
            print(f"Sorry, but {item} is not in menu today.")
    print("Total is {}".format(total))


PASSWORDS = {'Anton': '1234', 'John': 'abcd', 'Alice': '12ab'}


def simple_logging():
    while True:
        login = input("Enter your name: ")
        password = input("Enter a password: ")
        if login in PASSWORDS and PASSWORDS[login] == password:
            print("Successfully logged in.")
        else:
            print("Name or password is not correct. Try again.")


BIRTHDAYS = {'Anton': '1997-05-06',
             'Alice': '2000-03-05',
             'Misha': '1994-04-23'}  # date in ISO formats


def how_old() -> int:
    """Ask for name and return how old person is in days."""
    while True:
        name = input('Enter a name: ')
        if name in BIRTHDAYS:
            break
        else:
            print("Try again.")
    return (date.today() - date.fromisoformat(BIRTHDAYS[name])).days


if __name__ == '__main__':
    restaurant()
    simple_logging()
    print(how_old())
