"""
>>> 5*5
25

"""


def to_string(value):
    return str(value)


def to_list(value):
    return list(value)


def is_string(value):
    return isinstance(value, str)


def is_list(value):
    return isinstance(value, list)


def trim(string):
    """
    Removes leading, trailing, and redundant spaces/whitespace from a text string, or from each element of a text list.
    :param string: text or text list
    :return: Text or text list. The string, with extra spaces removed.

    >>> trim(['A  B C   '])
    ['A B C']
    """
    if is_list(string):
        trimmed = list(map(trim, string))  # trim all entries in list
        return list(filter(lambda entry: entry != '', trimmed))  # remove empty entries
    return " ".join(string.split())  # trim string


def unique(list):
    """
    removes duplicate values from a text list.
    :param list:
    :return: text list whith unique members
    """
    return list(dict.fromkeys(list))


def is_empty(string):
    """
    Return true is string is empty or only contains whitespace
    """
    if string is None:
        return True
    return string.strip() == ''


def contains(string, matches):
    """
    Determine if a string contains any of the given values. *matches* may be a
    single string, or a list of strings.
    """
    return any([m in string for m in ([matches] if isinstance(matches, str) else matches)])


def contains_all(string, matches):
    """
    Determine if a string contains all of the given values.
    """
    return all([m in string for m in matches])


def join(strings, sep=''):
    """
    Concatenate a list of strings into a single string by a separating
    delimiter.
    """
    return sep.join(strings)


def propercase(string):
    """
    Converts the words in a string to proper­name capitalization: the first letter of each word becomes uppercase,
    the rest become lowercase.
    """
    # return join(map(ucfirst, split(string)), ' ')
    pass


def replace(string):
    pass


def unique(string):
    pass


def sort(string):
    pass


def left(string):
    pass


def right(string):
    pass


def word(string):
    pass


def begins(string):
    pass


def ends(string):
    pass


def contains(string):
    pass


def getInitials(string):
    pass

# if __name__ == '__main__':
# import doctest
# doctest.testmod()
