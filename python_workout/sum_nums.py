from collections.abc import Iterable


def my_sum(*sequence: Iterable[int]) -> int:
    """Recursively computes the sum of a sequence of numbers.

    Params:
        *sequence (Iterable[int]): A sequence of numbers. Can include
        nested sequences.

    Returns:
        int: The sum of the numbers in the sequence.
    """
    result = 0
    for i in sequence:
        if isinstance(i, Iterable):
            # "*" to unpack an iterable.
            result += my_sum(*i)
        else:
            result += i
    return result


def str_analysis(word_list: list[str]) -> tuple[int, int, int]:
    """Take a list of words (strings). Return a tuple containing three
    integers, representing the length of the shortest word, the length of
    the longest word, and the average word length.s.

    Params:
        word_list (list[str]): list of words(strings)

    Returns:
        tuple[int, int, int]: length of the shortest word, the length of the
        longest word, and the average word length.
    """
    lengths = [len(word) for word in word_list]
    return min(lengths), max(lengths), sum(lengths)//len(lengths)


if __name__ == '__main__':
    print(my_sum([1, [2, 3, [4, 5]]]))
    print(str_analysis(['some', 'list', 'of', 'words']))
