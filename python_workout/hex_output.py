def hex_output(num: str):
    """Take a hex number and return the decimal equivalent."""
    decnum = 0
    for power, digit in enumerate(reversed(num)):
        decnum += int(digit, 16) * (16 ** power)
    return decnum


def name_triangle(name: str):
    """Take a name and produce a name triangle"""
    for index, ch in enumerate(name, start=1):
        print(name[:index])


if __name__ == '__main__':
    assert hex_output('A4F') == 0xA4F
    name_triangle('Anton')


