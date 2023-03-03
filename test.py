from calculate_words_frequency import calculate_word_frequency

def test_word_frequency():
    # test case 1
    sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
    n = 3
    expected_output = [("zblah", 3), ("bar", 2), ("baz", 2)]
    assert calculate_word_frequency(sentence, n) == expected_output

    # test case 2
    sentence = "a a a b b c d d d d d e e e e e e f f f f f f f g g g g g g g g"
    n = 3
    expected_output = [('g', 8), ('f', 7), ('e', 6)]
    assert calculate_word_frequency(sentence, n) == expected_output

    # test case 3
    sentence = "a a a b b c d d d d d e e e e e e f f f f f f f g g g g g g g g"
    n = "4"
    expected_output = [('g', 8), ('f', 7), ('e', 6), ('d', 5)]
    assert calculate_word_frequency(sentence, n) == expected_output

    # test case 4
    sentence = "hello world"
    n = 2
    expected_output = [("hello", 1), ("world", 1)]
    assert calculate_word_frequency(sentence, n) == expected_output

    # test case 5
    sentence = ""
    n = 5
    expected_output = []
    assert calculate_word_frequency(sentence, n) == expected_output

    # test case 6
    sentence = ["baz bar foo foo zblah zblah zblah baz toto bar", 1, {"tes":"he"}, "ubibuib", "eee"]
    n = 7
    expected_output = "the sentence's type is not a string... Please try again"
    assert calculate_word_frequency(sentence, n) == expected_output

    # test case 7
    sentence = "hello world"
    n = "d"
    expected_output = "the n's type is not a int... Please try again"
    assert calculate_word_frequency(sentence, n) == expected_output
