
sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
n = "3"

def calculate_word_frequency(string, number):
    """
    Calculates the frequency of words in a given string and returns a list of tuples sorted by decreasing frequency.

    Args:
        string (str): A string containing words separated by whitespace characters.
        number (int): An integer specifying the number of most frequent words to include in the returned list.

    Returns:
        A list of tuples containing the most frequent words in the input string, sorted by decreasing frequency. Each tuple
        contains a word as its first element and its frequency as its second element.

    Raises:
        ValueError: If the input of the number is not an integer.

    Example:
        >>> sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
        >>> n = 3
        >>> calculate_word_frequency(sentence, n)
        [('zblah', 3), ('bar', 2), ('baz', 2)]
    """

    # Verify the string and number's type are effectivly string and number "
    if not isinstance(string, str):
        return "the sentence's type is not a string... Please try again"
    try:
        number = int(number)
    except ValueError:
        return "the n's type is not a int... Please try again"

    # Convert the sentence into a string and split it into a list of words
    words = str(string).split()
    # words = ['baz', 'bar', 'foo', 'foo', 'zblah', 'zblah', 'zblah', 'baz', 'toto', 'bar']

    # sort by alphabetical order
    words.sort()
    # words = ['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'toto', 'zblah', 'zblah', 'zblah']

    # create dictionary to store word frequency
    word_freq = {}

    # Count frequency of each word
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    # word_freq = {'bar': 2, 'baz': 2, 'foo': 2, 'toto': 1, 'zblah': 3}

    # Sort and transform the dict into a list of tuble ordered by decreasing frequency
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    # sorted_word_freq = [('zblah', 3), ('bar', 2), ('baz', 2), ('foo', 2), ('toto', 1)]

    # calculate how many tuple to remove, based on the number's value
    tuples_to_remove = len(sorted_word_freq) - number
    # tuples_to_remove = 2

    # if less the 0, keept the same value, if more remove some tuples to get the final result. 
    if tuples_to_remove <= 0:
        pass
    else:
        sorted_word_freq = sorted_word_freq[:-tuples_to_remove]
    # sorted_word_freq = [('zblah', 3), ('bar', 2), ('baz', 2)]

    return sorted_word_freq


print(calculate_word_frequency(sentence, n))




