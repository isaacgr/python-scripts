"""Returns all strings from a list that are as long or longer than a given lenth"""


def longer_than(strings, minimum=0):
    """Return all strings from list longer than minimum length"""
    string_list = []

    if not isinstance(minimum, int) or minimum < 0:
        raise ValueError('Length must be >= 0')

    for string in strings:
        if not isinstance(string, str):
            continue
        if len(string) >= minimum:
            string_list.append(string)
    return string_list
