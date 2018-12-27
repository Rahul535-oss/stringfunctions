import fnmatch


def to_string(value):
    return str(value)


def to_list(value):
    if is_list(value):
        return value
    return [value]


def is_string(value):
    return isinstance(value, str)


def is_list(value):
    return isinstance(value, list)


def trim(string):
    """
    Removes leading, trailing, and redundant spaces/whitespace from a text string, or from each element of a text list.
    :param str string: text or text list
    :return: Text or text list. The string, with extra spaces removed.

    Remove all redundant whitespace from string
    >>> trim('A  B C   ')
    'A B C'

    Trim all entries in list and remove empty entries
    >>> trim(['Hello   ','','   World'])
    ['Hello', 'World']


    """
    if is_list(string):
        trimmed = list(map(trim, string))  # trim all entries in list
        return list(filter(lambda entry: entry != '', trimmed))  # remove empty entries
    return " ".join(string.split())  # trim string


def unique(source_list, ignore_case=False):
    """
    removes duplicate values from a text list.
    :param list:
    :return: text list whith unique members


    >>> unique( ['A','B','C','B','A'])
    ['A', 'B', 'C']

    >>> unique( ['red','green','Red','green'])
    ['red', 'green', 'Red']

    >>> unique( ['red','green','Red','green'], True)
    ['red', 'green']

    """
    if ignore_case:
        unique_list = []
        for entry in source_list:
            if not is_member(entry, unique_list, ignore_case=True):
                unique_list.append(entry)
        return unique_list
    return list(dict.fromkeys(source_list))


def is_empty(string):
    """
    Return true is string is empty or only contains whitespace

    >>> is_empty( "   " )
    True

    >>> is_empty( None )
    True

    """
    if string is None:
        return True
    return string.strip() == ''


def contains(string, substring, ignore_case=False):
    """
    Determine if a string contains any of the substrings

    :param string: (str or list) The string you want to search in
    :param substring: (str or list) The string(s) you want to search for in string.
    :param bool ignore_case: Optional, default False. Specify True to perform a case-insensitive search

    >>> contains( "Hello World", "Wo")
    True

    >>> contains( "Hello World", "world", True)
    True

    >>> contains( "Red Blue Yellow Green", ['Black', 'Red'])
    True

    >>> contains( "Red Blue Yellow Green", ['Blue', 'red'], True)
    True

    >>> contains( "Red Blue Yellow Green", ['Rubbish', ''])
    True

    >>> contains( ['ABC', 'DEF'], ['B'])
    True

    """
    if is_list(string):
        return any([contains(entry, substring, ignore_case) for entry in string])

    substrings = to_list(substring)
    if ignore_case:
        return any([entry.casefold() in string.casefold() for entry in substrings])
    return any([entry in string for entry in substrings])


def contains_all(string, substring, ignore_case=False):
    """
    Determine if a string contains all of the substring substrings

    :param string: (str or list) The string you want to search in
    :param substring: (str or list) The string(s) you want to search for in string.
    :param bool ignore_case: Optional, default False. Specify True to perform a case-insensitive search

    >>> contains_all( "Hello World", "Wo")
    True

    >>> contains_all( "Hello World", "world", True)
    True

    >>> contains_all( "Red Blue Yellow Green", ['Black', 'Red'])
    False

    >>> contains_all( "Red Blue Yellow Green", ['Blue', 'red'], True)
    True

    """
    if is_list(string):
        return any([contains_all(entry, substring, ignore_case) for entry in string])

    substrings = to_list(substring)
    if ignore_case:
        return all([entry.casefold() in string.casefold() for entry in substrings])
    return all([entry in string for entry in substrings])


def index_of(string, substring, ignore_case=False, reverse=False):
    """
    First character in the string has position = 1

    :param string:
    :param substring:
    :return:

    >>> index_of( 'Jakob','a')
    2

    >>> index_of( 'Jakob','K')
    0

    >>> index_of( 'Jakob','K', ignore_case=True)
    3

    >>> index_of( ['Red', 'Green','Blue'], 'e')
    [2, 3, 4]

    >>> index_of( "This is key: FIS", "is", reverse=True)
    6
    >>> index_of( "This is key: FIS", "is")
    3

    >>> index_of( "This is key: FIS", "is", reverse=True, ignore_case=True)
    15


    """
    if is_list(string):
        return [index_of(entry, substring, ignore_case) for entry in string]
    if ignore_case:
        string = string.casefold()
        substring = substring.casefold()
    if reverse:
        return string.rfind(substring) + 1
    return string.find(substring) + 1


def implode(strings, separator=''):
    """
    Concatenate all member of a list into a single string by a separating delimiter.
    """
    return separator.join(strings)


def propercase(string):
    """
    Converts the words in a string to proper­name capitalization: the first letter of each word becomes uppercase,
    the rest become lowercase.

    >>> propercase('hELLO wORLD')
    'Hello World'

    """
    return implode([entry.capitalize() for entry in string.split()], ' ')


def left(string, find, ignore_case=False):
    """

    :param str string: The string where you want to find the leftmost characters.
    :param str find: a substring to search for. Left return all character to the left of *find*
    :param int find: number of chars to return
    :return: the leftmost characters of string
    :rtype: str

    >>> left( "Hello World", 2 )
    'He'

    >>> left( "Hello", 10 )
    'Hello'

    >>> left( "Hello World", -3 )
    'Hello Wo'


    >>> left( "Happy Birthday", "XYZ")
    ''

    >>> left( "Hello World", "l")
    'He'

    >>> left( ["Jakob","Majkilde"], 2)
    ['Ja', 'Ma']

    """
    if is_list(string):
        return [left(entry, find) for entry in string]

    if isinstance(find, int):
        if find > 0:
            return string[:find]
        return string[:find]

    pos = index_of(string, find, ignore_case)
    if pos > 0:
        return left(string, pos - 1)
    return ""


def left_back(string, find, ignore_case=False):
    """
    As :func: left: but counts/searches from the back

    :param str string: The string where you want to find the leftmost characters.
    :param str find: a substring to search for. Left return all character to the left of *find*
    :param int find: number of chars to return
    :return: the leftmost characters of string
    :rtype: str

    >>> left_back( "Hello World", 3 )
    'Hello Wo'

    >>> left_back( "Hello", 10 )
    'Hello'

    >>> left_back( "Hello World", -2 )
    'Hello World'


    >>> left_back( "Happy Birthday", "XYZ")
    ''

    >>> left_back( "Hello World", "l")
    'Hello Wor'

    >>> left_back( ["Jakob","Majkilde"], 2)
    ['Jak', 'Majkil']

    """
    if is_list(string):
        return [left_back(entry, find) for entry in string]

    if isinstance(find, int):
        if find > 0:
            if find > len(string):
                return string
            return string[:len(string) - find]
        return string
    pos = index_of(string, find, ignore_case, reverse=True)
    if pos > 0:
        return left(string, pos - 1)
    return ""


def is_member(value, list, ignore_case=False):
    """

    :param value:
    :param list:
    :param ignore_case:
    :return:


    >>> is_member('Admin', ['Owner', 'Admin', 'Reader'])
    True

    >>> is_member('admin', ['Owner', 'Admin', 'Reader'])
    False

    >>> is_member( ['Jakob','Maiken'], ['Maiken','Amalie','Jakob','Ida'])
    True

    >>> is_member('admin', ['Owner', 'Admin', 'Reader'], ignore_case=True)
    True

    """
    if is_list(value):
        return all([is_member(entry, list, ignore_case) for entry in value])
    if ignore_case:
        return is_member(lowercase(value), lowercase(list))
    return value in list


def lowercase(value):
    """

    :param value:
    :return:

    >>> lowercase("Der Fluß")
    'der fluss'

    >>> lowercase( ['Green','RED','bluE'])
    ['green', 'red', 'blue']

    """
    if is_list(value):
        return [entry.casefold() for entry in value]
    return value.casefold()


def right(string, find, ignore_case=False):
    """

    :param str string: The string where you want to find the rightmost characters.
    :param str find: a substring to search for. Left return all characters to the right of *find*
    :param int find: skip first 'find' characters and return the rest
    :return: the rightmost characters of string
    :rtype: str

    >>> right( "Hello World", 3 )
    'lo World'

    >>> right( "Hello", 10 )
    'Hello'

    >>> right( "Hello World", -2 )
    'ld'


    >>> right( "Happy Birthday", "XYZ")
    ''

    >>> right( "Hello World", "l")
    'lo World'

    >>> right( ["Jakob","Majkilde"], 2)
    ['kob', 'jkilde']

    >>> right( ["Jakob","Majkilde"], 'j')
    ['', 'kilde']

    """
    if is_list(string):
        return [right(entry, find) for entry in string]

    if isinstance(find, int):
        if find > len(string):
            return string
        if find > 0:
            return string[find:]
        return string[find:]
    pos = index_of(string, find, ignore_case)
    if pos > 0:
        return right(string, pos + len(find) - 1)
    return ""


def right_back(string, find, ignore_case=False):
    """

    :param str string: The string where you want to find the rightmost characters.
    :param str find: a substring to search for. Left return all characters to the right of *find*
    :param int find: skip first 'find' characters and return the rest
    :return: the rightmost characters of string
    :rtype: str

    >>> right_back( "Hello World", 3 )
    'rld'

    >>> right_back( "Hello", 10 )
    'Hello'

    >>> right_back( "Hello World", -2 )
    'Hello World'


    >>> right_back( "Happy Birthday", "XYZ")
    ''

    >>> right_back( "Hello World", "l")
    'd'

    >>> right_back( ["Jakob","Majkilde"], 2)
    ['ob', 'de']


    """
    if is_list(string):
        return [right_back(entry, find) for entry in string]

    if isinstance(find, int):
        if find > len(string):
            return string
        if find > 0:
            return string[-find:]
        return string
    pos = index_of(string, find, ignore_case, reverse=True)
    if pos > 0:
        return right(string, pos + len(find) - 1)
    return ""


def word(string, number, separator=None):
    """

    :param string:
    :param separator:
    :param number:
    :return:

    >>> word( "Some text here", 2)
    'text'

    >>> word( "Some text here", 5)
    ''

    >>> word( "Some text here", -1)
    'here'

    >>> word( "North, West, East", 2, ", ")
    'West'

    >>> word( ["North, West, East", 'Scandinavia, UK, China'], 2, ", ")
    ['West', 'UK']



    """
    if is_list(string):
        return [word(entry, number, separator) for entry in string]
    list = string.split(separator)
    index = number - 1 if number > 0 else number
    if index > len(list):
        return ''
    return list[index]


def compare(string1, string2, ignore_case=False):
    """
    Compares two strings
    :param string1:
    :param string2:
    :param ignore_case:
    :return:

    string1 is less than string2: return	  -1
    string1 equals string2: return	   0
    string1 is greater than string2: return	   1

    >>> compare( "Jakob", "jakob")
    -1

    >>> compare( "Jakob", "jakob", ignore_case=True)
    0

    """
    if ignore_case:
        string1 = lowercase(string1)
        string2 = lowercase(string2)
    if string1 < string2:
        return -1
    if string2 > string1:
        return 1
    return 0


# TODO
def replace(sourceList, fromList, toList, ignore_case=False):
    """
    Performs a find-and-replace operation on a text list.
Syntax
@Replace( sourcelist ; fromlist ; tolist )
Parameters
sourcelist
Text list. The list whose values you want to scan.
fromlist
Text list. A list containing the values that you want to replace.
tolist
Text list. A list containing the replacement values.
    :param string:
    :return:
    """
    pass


# TODO
def replace_substring(sourceList, fromList, toList, ignore_case=False):
    """

    :return:


    Replaces specific words or phrases in a string with new words or phrases that you specify. Case sensitive.
Syntax
@ReplaceSubstring( sourceList ; fromList ; toList )
Parameters
sourceList
Text or text list. The string whose contents you want to modify.
fromList
Text or text list. A list containing the words or phrases that you want to replace.
toList
Text or text list. A list containing the replacement words or phrases.
Return value
newSourceList
Text or text list. The sourceList, with any values from fromList replaced by the corresponding value in toList.  If none of the values in fromList matched the values in sourceList, then sourceList is returned unaltered.
    """
    pass


def diff(list1, list2, ignore_case=False):
    """
    Remove elements on list2 from list1

    :param list1:
    :param list2:
    :return:

    >>> diff( ['A','B','C'], ['A','D', 'c'])
    ['B', 'C']

    >>> diff( ['A','B','C'], ['A','D', 'c'], ignore_case=True)
    ['B']

    """
    return [entry for entry in list1 if not is_member(entry, list2, ignore_case)]


def union(list1, list2, ignore_case=False):
    """
    Adds to list

    :param list1:
    :param list2:
    :return:

    >>> union( ['A','B','C'], ['A','D','c'])
    ['A', 'B', 'C', 'D', 'c']

    >>> union( ['A','B','C'], ['A','D','c'], ignore_case=True)
    ['A', 'B', 'C', 'D']

    """
    final_list = unique(list1 + list2, ignore_case)
    return final_list


def intersection(list1, list2, ignore_case=False):
    """

    :param list1:
    :param list2:
    :param ignore_case:
    :return:

    >>> intersection( ['A','B','C'], ['A','D', 'c'])
    ['A']

    >>> intersection( ['A','B','C'], ['A','D', 'c'], ignore_case=True)
    ['A', 'C']
    """
    return [entry for entry in list1 if is_member(entry, list2, ignore_case)]


# https://docs.python.org/3/library/fnmatch.html
def like(string, pattern, ignore_case=False):
    """

    :param string:
    :param pattern:
    :param ignore_case:
    :return:

    >>> like( 'Jakob', 'jakob')
    False

    >>> like( 'Jakob', 'ja?ob', ignore_case=True)
    True

    >>> like( ['Petersen','Pedersen','Peter', 'Olsen'],"Pe?er*" )
    [True, True, True, False]

    """
    if is_list(string):
        return [like(entry, pattern, ignore_case) for entry in string]
    if ignore_case:
        return fnmatch.fnmatch(string, pattern)
    return fnmatch.fnmatchcase(string, pattern)


def sort(source_list, ignore_case=False):
    """

    :param list source_list:
    :return:

    >>> sort( ['Bad','bored','abe','After'])
    ['After', 'Bad', 'abe', 'bored']

    >>> sort( ['Bad','bored','abe','After'], ignore_case=True)
    ['abe', 'After', 'Bad', 'bored']


    """
    if ignore_case:
        source_list.sort(key=lambda s: s.casefold())
    else:
        source_list.sort()

    return source_list
