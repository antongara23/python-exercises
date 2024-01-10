def mysum(*args: [int, float, str, list, tuple]):
    """Return the sum of a sequence of arguments of the same type"""
    if not args:
        return args
    result = args[0]
    for i in args[1:]:
        result += i
    return result


def mysum_bigger_than(threshold: [int, float, str, list, tuple],
                      *args: [int, float, str, list, tuple]):
    """Return the sum of elements of the same type which are bigger then
    the threshold."""
    if not args:
        return args
    bigger = [i for i in args if i > threshold]
    result = bigger[0]
    for i in bigger[1:]:
        result += i
    return result


def sum_numeric(*args: any) -> int:
    """Return the sum of the integers. If the argument is or can be
    turned into an integer, it is added to the total. Arguments that
    can’t be handled as integers are ignored. """
    result = 0
    for i in args:
        try:
            int(i)
            to_int = True
        except (ValueError, TypeError):
            to_int = False
        if to_int:
            result += int(i)
    return result


def dict_sum(list_of_dicts: list[dict]) -> dict:
    """Take a list of dicts and return a single dict that combines all
    the keys and values. If a key appears in more than one argument, the
     value is a list containing all the values from the arguments."""
    result = {}
    for d in list_of_dicts:
        for key, value in d.items():
            if key in result:
                if isinstance(result[key], list):
                    result[key].append(value)
                else:
                    result[key] = [result[key], value]
            else:
                result[key] = value
    return result


if __name__ == '__main__':
    print(mysum())
    print(mysum('abc', 'def'))
    print(mysum([1,2,3], [4,5,6]))
    print(mysum(1,2,3))
    print(mysum_bigger_than(10, 5, 20, 30, 6))
    print(mysum_bigger_than('b', 'a', 'c', 'd', 'e'))
    print(sum_numeric('a', 'b', 1, '2', 3, 'f'))
    print(dict_sum([{'A': 1, 'B': 1}, {'A': 2}, {'B': 2},{'A': 3}, {'B': 3}]))
