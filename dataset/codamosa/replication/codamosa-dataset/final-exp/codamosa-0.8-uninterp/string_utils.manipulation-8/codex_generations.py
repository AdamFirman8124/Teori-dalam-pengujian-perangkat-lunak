

# Generated at 2022-06-14 05:38:57.078441
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:39:05.352902
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('').format() == ''
    assert __StringFormatter('A').format() == 'A'
    assert __StringFormatter('Abc').format() == 'Abc'
    assert __StringFormatter('Abc def').format() == 'Abc def'
    assert __StringFormatter('Abc def\nghi').format() == 'Abc def ghi'
    assert __StringFormatter('Abc def ghi').format() == 'Abc def ghi'
    assert __StringFormatter('Abc def\nghi jkl').format() == 'Abc def ghi jkl'
    assert __StringFormatter('Abc def\nghi jkl').format() == 'Abc def ghi jkl'

# Generated at 2022-06-14 05:39:15.409894
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    formatter = __StringFormatter('my test str')
    assert formatter.format() == 'My test str'

    formatter = __StringFormatter('This is   my 2nd     test')
    assert formatter.format() == 'This is my 2nd test'

    formatter = __StringFormatter('preceded by sign, follow by sign.')
    assert formatter.format() == 'Preceded by sign, follow by sign.'

    formatter = __StringFormatter('thiS   is   a test')
    assert formatter.format() == 'This is a test'

    formatter = __StringFormatter('this is.a @mail@to.be@sent.com')
    assert formatter.format() == 'This is a mail@to.be@sent.com'


# Generated at 2022-06-14 05:39:25.766661
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:39:33.353020
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:39:43.680281
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('test').format() == 'Test'
    assert __StringFormatter('test test').format() == 'Test test'
    assert __StringFormatter('test test ').format() == 'Test test'
    assert __StringFormatter(' test test').format() == 'Test test'
    assert __StringFormatter(' test test ').format() == 'Test test'
    assert __StringFormatter('test,test').format() == 'Test, test'
    assert __StringFormatter('test,test ').format() == 'Test, test'
    assert __StringFormatter(' test,test').format() == 'Test, test'
    assert __StringFormatter(' test,test ').format() == 'Test, test'
    assert __StringFormatter('test,test test').format() == 'Test, test test'
    assert __StringForm

# Generated at 2022-06-14 05:39:50.777149
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('This is a test string').format() == 'This is a test string'
    assert __StringFormatter('This is a test string ').format() == 'This is a test string'
    assert __StringFormatter(' This is a test string').format() == 'This is a test string'
    assert __StringFormatter('THIS IS A test string').format() == 'This is a test string'
    assert __StringFormatter('This IS A test string').format() == 'This is a test string'
    assert __StringFormatter('This    is    a    test    string').format() == 'This is a test string'
    assert __StringFormatter('This-is-a-test-string').format() == 'This is a test string'
    assert __StringFormatter('This -is - a -  test  -  string').format()

# Generated at 2022-06-14 05:40:03.165176
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('a b c').format() == 'a b c'  # no change
    assert __StringFormatter(' a b c ').format() == 'a b c'  # trim
    assert __StringFormatter('a b c d e').format() == 'a b c d e'  # no change
    assert __StringFormatter('a B c d e').format() == 'a B c d e'  # no change
    assert __StringFormatter('a B c d e f').format() == 'a B c d e f'  # no change
    assert __StringFormatter('a B C d E f').format() == 'a B C d E f'  # no change
    assert __StringFormatter('a  b c d e f').format() == 'a b c d e f'  # trim duplicates
    assert __

# Generated at 2022-06-14 05:40:15.516816
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('a b    c      d').format() == 'A b c d'
    assert __StringFormatter('a b Cd').format() == 'A b Cd'
    assert __StringFormatter('a b.').format() == 'A b.'
    assert __StringFormatter('a b... c').format() == 'A b... C'
    assert __StringFormatter('a - b').format() == 'A - b'
    assert __StringFormatter('a -B.').format() == 'A - B.'
    assert __StringFormatter('Ba- c').format() == 'Ba - c'
    assert __StringFormatter('Ba- c').format() == 'Ba - c'
    assert __StringFormatter('Ba- c').format() == 'Ba - c'

# Generated at 2022-06-14 05:40:21.773720
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    class __FakeStringFormatter(__StringFormatter):
        input_string = ''
        def __uppercase_first_char(self, regex_match): return '__Fake_first_char'
        def __remove_duplicates(self, regex_match): return '__Fake_duplicates'
        def __uppercase_first_letter_after_sign(self, regex_match): return '__Fake_uppercase_after_sign'
        def __ensure_right_space_only(self, regex_match): return '__Fake_right_space'
        def __ensure_left_space_only(self, regex_match): return '__Fake_left_space'
        def __ensure_spaces_around(self, regex_match): return '__Fake_spaces_around'

# Generated at 2022-06-14 05:40:31.756840
# Unit test for function asciify
def test_asciify():
    assert asciify("ÈèéùúòóäåëýñÅÀÁÇÌÍÑÓË")==("Ee'e'u'u'o'o'a'a'e'y'n'A'A'A'C'I'I'N'O'E")
    assert asciify("阿里巴巴")==("A'l'i'b'a'b'a")
    assert asciify("Alpha")==("Alpha")
    assert asciify("アルファ")==("A'r'u'f'a")
    assert asciify("中文")==("Z'h'o'n'g' 'w'e'n")

# Generated at 2022-06-14 05:40:36.117849
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    assert __StringFormatter('string')
    assert __StringFormatter('string string')
    assert __StringFormatter('a string')
    assert __StringFormatter('string a')
    assert __StringFormatter(' a string ')
    assert __StringFormatter('string a string')
    assert __StringFormatter('a string a')
    assert __StringFormatter('a string a string')
    assert __StringFormatter('a string a string a')
    assert __StringFormatter('a  string  a  string  a')
    assert __StringFormatter('a string a string a.')
    assert __StringFormatter('a string a string a!')
    assert __StringFormatter('a string a string a?')
    assert __StringFormatter('a string a string a:')
    assert __StringFormatter('a string a string a,')


# Generated at 2022-06-14 05:40:37.569708
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'



# Generated at 2022-06-14 05:40:45.340616
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'



# Generated at 2022-06-14 05:40:48.091346
# Unit test for function strip_margin
def test_strip_margin():
    code_snippet = '''
        def foo(a) {
            a + 1
        }
    '''


# Generated at 2022-06-14 05:40:58.855635
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('') == ''
    assert strip_html('<p><b>test</b></p>') == ''
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
    assert strip_html('<p><b>test</b></p>', keep_tag_content=True) == 'test'
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'



# Generated at 2022-06-14 05:41:05.246075
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', upper_case_first=False, separator='-') == 'theSnakeIsGreen'



# Generated at 2022-06-14 05:41:09.544400
# Unit test for function booleanize
def test_booleanize():
    test_booleanize_true('true')
    test_booleanize_true('TRUE')
    test_booleanize_true('True')
    test_booleanize_true('1')
    test_booleanize_true('y')
    test_booleanize_true('yes')
    test_booleanize_true('Yes')
    test_booleanize_true('YEs')
    test_booleanize_false('false')
    test_booleanize_false('FALSE')
    test_booleanize_false('False')
    test_booleanize_false('2')
    test_booleanize_false('n')
    test_booleanize_false('no')
    test_booleanize_false('NO')


# Generated at 2022-06-14 05:41:13.204847
# Unit test for function decompress
def test_decompress():
    assert decompress("eJxNUcFo0zAM/RW4o4d4upStrIiZG1mYBJVMXWwiIyH1qbOqgQTQWjrrLkvfVAANnIgJpClzWUj8cw6wADU2nCQ==") == "It's a compressed string"


# Generated at 2022-06-14 05:41:26.128402
# Unit test for function prettify
def test_prettify():
    failed = False

# Generated at 2022-06-14 05:41:31.583346
# Unit test for function compress
def test_compress():

    # no compression at all (level 0)
    assert compress('Hello World!', compression_level=0) == 'Hello World!'

    # no compression at all (default level)
    assert compress('Hello World!') == 'Hello World!'

    # best compression (level 9)
    assert compress('Hello World!', compression_level=9) == 'eNrzSM3JyVcIfCkpLCzJU8lMz1YvV1AvJLM/ILckvy8gvyE='



# Generated at 2022-06-14 05:41:37.750206
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('X') == 10 # now equal
    assert roman_decode('VII') == 7 # now equal
    assert roman_decode('XIV') == 14 # now equal
    assert roman_decode('31') == 31  # now equal

"""
Helper classes (private)
"""



# Generated at 2022-06-14 05:41:46.534214
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.encode(1) == 'I'
    assert __RomanNumbers.encode(4) == 'IV'
    assert __RomanNumbers.encode(5) == 'V'
    assert __RomanNumbers.encode(16) == 'XVI'
    assert __RomanNumbers.encode(1954) == 'MCMLIV'
    assert __RomanNumbers.encode(1990) == 'MCMXC'
    assert __RomanNumbers.encode(2014) == 'MMXIV'

    assert __RomanNumbers.decode('I') == 1
    assert __RomanNumbers.decode('IV') == 4
    assert __RomanNumbers.decode('V') == 5
    assert __RomanNumbers.decode('XVI') == 16
    assert __RomanNumbers.decode('MCMLIV') == 1954

# Generated at 2022-06-14 05:41:50.152501
# Unit test for function slugify
def test_slugify():
    assert slugify('The quick brown fox jumps over the lazy dog') == 'the-quick-brown-fox-jumps-over-the-lazy-dog'
    assert slugify('The quick brown fox jumps over the lazy dog.') == 'the-quick-brown-fox-jumps-over-the-lazy-dog'
    assert slugify('   The quick brown fox jumps over the lazy dog   ') == 'the-quick-brown-fox-jumps-over-the-lazy-dog'
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'


# Generated at 2022-06-14 05:41:52.272615
# Unit test for function reverse
def test_reverse():
    assert reverse('hello') == 'olleh'
# Test
test_reverse()



# Generated at 2022-06-14 05:42:01.796235
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.__mappings == [
        {1: 'I', 5: 'V'},
        {1: 'X', 5: 'L'},
        {1: 'C', 5: 'D'},
        {1: 'M'},
    ]
    assert __RomanNumbers.__reversed_mappings == [
        {'I': 1, 'V': 5},
        {'X': 1, 'L': 5},
        {'C': 1, 'D': 5},
        {'M': 1},
    ]
    assert __RomanNumbers.__encode_digit(0, 1) == 'I'
    assert __RomanNumbers.__encode_digit(0, 5) == 'V'
    assert __RomanNumbers.__encode_digit(1, 3) == 'XXX'
    assert __Roman

# Generated at 2022-06-14 05:42:05.441097
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode(1) == 'I'
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode(2020) == 'MMXX'
    assert roman_encode('1') == 'I'
    assert roman_encode('37') == 'XXXVII'
    assert roman_encode('2020') == 'MMXX'
    with pytest.raises(InvalidInputError):
        roman_encode(0)
    with pytest.raises(InvalidInputError):
        roman_encode(4000)



# Generated at 2022-06-14 05:42:09.788273
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert('camel_case_test' == camel_case_to_snake('CamelCaseTest'))
    assert('test' == camel_case_to_snake('test'))
    assert('test_test' == camel_case_to_snake('TestTest'))
    assert('test_test_test' == camel_case_to_snake('TestTestTest'))
    assert('test_test_test_test' == camel_case_to_snake('TestTestTestTest'))
    assert('this_is_a_camel_case_string_test' == camel_case_to_snake('ThisIsACamelStringTest'))
    assert('camel_case_string_test' == camel_case_to_snake('camelCaseStringTest'))



# Generated at 2022-06-14 05:42:15.258555
# Unit test for function shuffle
def test_shuffle():
    """
    Test the function Shuffle
    :return:
    """
    assert shuffle('Hello world') == 'lodHl eworl'
    assert shuffle('Hello world') == 'lelHw orlod'
    assert shuffle('Hello world') == 'lloHe wlrod'



# Generated at 2022-06-14 05:42:23.383363
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('V') == 5
    assert roman_decode('IX') == 9
    assert roman_decode('XIII') == 13
    assert roman_decode('LXIX') == 69
    assert roman_decode('CXXX') == 130
    assert roman_decode('MDCCCLXXXIX') == 1889
    assert roman_decode('MMXX') == 2020
    assert roman_decode('MMMCD') == 3400


# Generated at 2022-06-14 05:42:42.387813
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.encode(2112) == 'MMCXII'
    assert __RomanNumbers.encode(2020) == 'MMXX'
    assert __RomanNumbers.encode(1847) == 'MDCCCXLVII'
    assert __RomanNumbers.encode(15) == 'XV'
    assert __RomanNumbers.encode(15) == 'XV'
    assert __RomanNumbers.encode(3) == 'III'
    assert __RomanNumbers.encode(2) == 'II'
    assert __RomanNumbers.encode(1) == 'I'
    assert __RomanNumbers.encode(4) == 'IV'
    assert __RomanNumbers.encode(5) == 'V'
    assert __RomanNumbers.encode(6) == 'VI'
    assert __RomanNumbers.encode(7)

# Generated at 2022-06-14 05:42:48.019613
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    # given
    a_string = 'doe, john'
    the_string_formatter = __StringFormatter(a_string)

    # when
    actual_string_formatter = the_string_formatter

    # then
    assert(isinstance(actual_string_formatter, __StringFormatter))


# Generated at 2022-06-14 05:42:54.628543
# Unit test for function strip_margin
def test_strip_margin():
    test_string = '''
                                line 1
                                line 2
                                line 3
                                '''
    stripped = strip_margin(test_string)
    assert '\nline 1\nline 2\nline 3\n' == stripped
    print('\ntest_strip_margin() PASSED !')


# Generated at 2022-06-14 05:43:01.985376
# Unit test for function strip_margin
def test_strip_margin():
    assert strip_margin ('''
        this is my first line
        this is my second line
        ''') == '''
this is my first line
this is my second line
'''
    assert strip_margin('''
        | this is my first line
        | this is my second line
        ''') == '''
this is my first line
this is my second line
'''
    assert strip_margin('''
        | this is my first line
        | this is my second line
        ''') == '''this is my first line
this is my second line'''
    assert strip_margin('''
        | this is my first line
        | this is my second line
        ''') == '''this is my first line
this is my second line'''

test_strip_margin()

# Generated at 2022-06-14 05:43:07.570080
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers(): 
    # encode some numbers
    roman = __RomanNumbers()
    assert roman.encode(1) == 'I'
    assert roman.encode(12) == 'XII'
    assert roman.encode(2999) == 'MMCMXCIX'

    # decode some strings
    assert roman.decode('I') == 1
    assert roman.decode('XII') == 12
    assert roman.decode('MMCMXCIX') == 2999
    assert roman.decode('MMMMCMXCIV') == 4994
    
    


# Generated at 2022-06-14 05:43:08.034255
# Unit test for function compress
def test_compress():
    pass # test done inside class


# Generated at 2022-06-14 05:43:10.409146
# Unit test for function shuffle
def test_shuffle():
    assert shuffle('hello world') != 'hello world'
    assert shuffle('hello world') != 'hello world'
    assert shuffle('hello world') != 'hello world'
    assert shuffle('hello world') != 'hello world'



# Generated at 2022-06-14 05:43:12.103331
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert 'this_is_a_camel_string_test' == camel_case_to_snake('ThisIsACamelStringTest')



# Generated at 2022-06-14 05:43:15.780319
# Unit test for function booleanize
def test_booleanize():
    assert booleanize("") is False
    assert booleanize("yEs") is True
    assert booleanize("no") is False
    assert booleanize("1") is True
    assert booleanize("true") is True
    assert booleanize("false") is False
    assert booleanize("foo bar") is False
    assert booleanize("yep") is False
    assert booleanize("") is False
    assert booleanize("0") is False



# Generated at 2022-06-14 05:43:21.272605
# Unit test for constructor of class __StringCompressor

# Generated at 2022-06-14 05:43:34.659818
# Unit test for function decompress

# Generated at 2022-06-14 05:43:40.885257
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'
    assert strip_html('<a href="http://www.google.com">Google</a>') == 'Google'



# Generated at 2022-06-14 05:43:53.660078
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    class FakeRE:
        def __init__(self, value):
            self.value = value

        def search(self, __) -> bool:
            return self.value

        def sub(self, __, ___) -> str:
            return self.value

    def check(input_string, expected_output):
        assert isinstance(expected_output, str)
        assert isinstance(input_string, str)

        fake_regex = FakeRE(expected_output)


# Generated at 2022-06-14 05:43:58.209415
# Unit test for function asciify
def test_asciify():
    input_string = "èéùúòóäåëýñÅÀÁÇÌÍÑÓË"
    output_string = "eeuuooaaeynAAACIINOE"
    assert(asciify(input_string) == output_string)

test_asciify()

# Generated at 2022-06-14 05:44:03.095108
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('ThisIsACamelStringTest', '-') == 'this-is-a-camel-string-test'



# Generated at 2022-06-14 05:44:11.163929
# Unit test for function decompress
def test_decompress():
    assert 'word n0 word n1 word n2 word n3 word n4 word n5 word n6 word n7 word n8 word n9 word n10 word n11 word \
    n12 word n13 word n14 word n15 word n16 word n17 word n18 word n19' == decompress(compress('word n0 word n1 word n2 \
    word n3 word n4 word n5 word n6 word n7 word n8 word n9 word n10 word n11 word n12 word n13 word n14 word n15 \
    word n16 word n17 word n18 word n19'))



# Generated at 2022-06-14 05:44:23.071862
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    # Valid input string
    input_string = 'some text'

    # Valid input string
    invalid_input_string = ''

    # Valid encoding
    encoding = 'utf-8'

    # Valid compression level
    compression_level = 9

    # Invalid compression level
    invalid_compression_level = 10

    # Valid compressed string
    compressed_string = __StringCompressor.compress(input_string, encoding, compression_level)

    # Valid decompressed string
    decompressed_string = __StringCompressor.decompress(compressed_string, encoding)

    # Abnormal behavior
    try:
        # Empty input string
        __StringCompressor.compress(invalid_input_string, encoding, compression_level)
    except ValueError:
        pass
    else:
        raise ValueError('Empty string should not be accepted')



# Generated at 2022-06-14 05:44:34.771842
# Unit test for function prettify

# Generated at 2022-06-14 05:44:42.620177
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.__encode_digit(0, 1) == 'I'
    assert __RomanNumbers.__encode_digit(0, 5) == 'V'
    assert __RomanNumbers.__encode_digit(0, 9) == 'IX'
    assert __RomanNumbers.__encode_digit(1, 1) == 'X'
    assert __RomanNumbers.__encode_digit(1, 8) == 'VIII'
    assert __RomanNumbers.__encode_digit(1, 9) == 'XC'
    assert __RomanNumbers.__encode_digit(2, 1) == 'C'
    assert __RomanNumbers.__encode_digit(2, 8) == 'DCCC'
    assert __RomanNumbers.__encode_digit(2, 9) == 'CM'
    assert __RomanNumbers.__

# Generated at 2022-06-14 05:44:44.081255
# Unit test for function decompress
def test_decompress():
    logging.info("test_decompress")
    msg = 'foo bar'
    assert decompress(compress(msg)) == msg

# Generated at 2022-06-14 05:44:51.199499
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode(37) == 'XXXVII'
    


# Generated at 2022-06-14 05:44:56.464804
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') == True, "booleanize('true') should return True"
    assert booleanize('YES') == True, "booleanize('YES') should return True"
    assert booleanize('nope') == False, "booleanize('nope') should return False"
    assert booleanize('') == False, "booleanize('') should return False"



# Generated at 2022-06-14 05:45:06.531920
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('thisIsACamelCaseString') == 'this_is_a_camel_case_string'
    assert camel_case_to_snake('thisIsACamelCaseString', separator='-') == 'this-is-a-camel-case-string'
    assert camel_case_to_snake('thisIsACamelCaseString', separator='') == 'thisisacamelcasestring'
    assert camel_case_to_snake('thisIsNotACamelCaseString') == 'thisIsNotACamelCaseString'



# Generated at 2022-06-14 05:45:11.854270
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('IV') == 4
    assert roman_decode('XIX') == 19
    assert roman_decode('CM') == 900
    assert roman_decode('XL') == 40
    assert roman_decode('XC') == 90
    assert roman_decode('MMMM') == 4000

# Generated at 2022-06-14 05:45:17.623331
# Unit test for function shuffle
def test_shuffle():
    input_string = 'hello world'
    tmp = shuffle(input_string)
    if tmp == 'hello world':
        assert False
    else:
        assert True
# test
test_shuffle()



# Generated at 2022-06-14 05:45:23.370279
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('This is a <div>test with <span>html</span> tags.</div>') == 'This is a test with html tags.'
    assert strip_html('This is a <div>test with <span>html</span> tags.</div>', keep_tag_content=True) == 'This is a test with html tags.'



# Generated at 2022-06-14 05:45:28.950282
# Unit test for function compress
def test_compress():
    original = ' '.join('word n{}'.format(n) for n in range(20))
    compressed = compress(original)
    assert len(compressed) < len(original)
test_compress()



# Generated at 2022-06-14 05:45:34.999131
# Unit test for function strip_margin
def test_strip_margin():
    s = '''
        |line 1
        |line 2
        |line 3
        |'''
    out = '''
        line 1
        line 2
        line 3
        '''
    assert out == strip_margin(s)
    assert out == strip_margin(s[1:])
    assert out == strip_margin(s[2:])
    assert out == strip_margin(s[3:])
    assert out == strip_margin(s[4:])
    assert out == strip_margin(s[5:])



# Generated at 2022-06-14 05:45:41.567162
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # test format on a simple input
    assert __StringFormatter('hello world').format() == 'Hello world'

    # test format with multiple spaces
    assert __StringFormatter('hello  world').format() == 'Hello world'

    # test invalid input
    try:
        __StringFormatter(None).format()
    except InvalidInputError:
        pass

    # test format with punctuation
    assert __StringFormatter('hello#world!').format() == 'Hello world'

    # test format with digits
    assert __StringFormatter('hello 123 world').format() == 'Hello 123 world'

    # test format with upper case letters
    assert __StringFormatter('HELLO WORLD').format() == 'Hello world'

    # test format with lower case letters
    assert __StringFormatter('hello WORLD').format() == 'Hello world'

    # test

# Generated at 2022-06-14 05:45:43.215378
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'



# Generated at 2022-06-14 05:46:05.864382
# Unit test for function compress
def test_compress():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    assert len(original) == 169
    assert len(compressed) == 96
    assert original == decompress(compressed)

test_compress()



# Generated at 2022-06-14 05:46:11.577661
# Unit test for function slugify
def test_slugify():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('This is a test') == 'this-is-a-test'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
test_slugify()



# Generated at 2022-06-14 05:46:14.177009
# Unit test for function compress
def test_compress():
    assert compress('test') == 'eJxLTE2tLS1BycoCFgkcXAA='


# Generated at 2022-06-14 05:46:18.530319
# Unit test for function slugify
def test_slugify():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
    assert slugify('Mönstér Mägnët', '*') == 'monster*magnet'


# Generated at 2022-06-14 05:46:33.513332
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:46:44.418300
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('VII') == 7
    assert roman_decode('MMMDCCLXXXVII') == 3787
    assert roman_decode('MMDCCLXXXVII') == 2787
    assert roman_decode('DCCLXXXVII') == 787
    assert roman_decode('MCDLII') == 1452
    assert roman_decode('MDLXXVII') == 1577
    assert roman_decode('MMDCCVII') == 2707
    assert roman_decode('MCCLXXVII') == 1277
    assert roman_decode('MCCVII') == 1207
    assert roman_decode('MDCCXCIX') == 1799
    assert roman_decode('MCDLXXVII') == 1477

# Generated at 2022-06-14 05:46:50.018512
# Unit test for function strip_margin
def test_strip_margin():
    out = strip_margin('''
                        line 1
                        line 2
                        line 3
                        ''')
    assert (out == '''
line 1
line 2
line 3''')



# Generated at 2022-06-14 05:46:53.118958
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_case_string_test'


# Generated at 2022-06-14 05:46:57.739057
# Unit test for function reverse
def test_reverse():
    assert reverse('') == '', 'Empty string is reverted properly'
    assert reverse('  ') == '  ', 'Spaces are reverted properly'
    assert reverse('hello') == 'olleh', 'Words are reverted properly'
    assert reverse('   hello   ') == '   olleh   ', 'Words with spaces are reverted properly'



# Generated at 2022-06-14 05:47:00.782600
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('VII') == 7
    assert roman_decode('MMXX') == 2020


# Generated at 2022-06-14 05:47:29.199182
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('I') == 1
    assert roman_decode('II') == 2
    assert roman_decode('III') == 3
    assert roman_decode('IV') == 4
    assert roman_decode('V') == 5
    assert roman_decode('VI') == 6
    assert roman_decode('VII') == 7
    assert roman_decode('VIII') == 8
    assert roman_decode('IX') == 9
    assert roman_decode('X') == 10
    assert roman_decode('XI') == 11
    assert roman_decode('XII') == 12
    assert roman_decode('XIII') == 13
    assert roman_decode('XIV') == 14

# Generated at 2022-06-14 05:47:35.434599
# Unit test for function asciify
def test_asciify():
    input_string = 'èéùúòóäåëýñÅÀÁÇÌÍÑÓË'
    assert asciify(input_string) == 'eeuuooaaeynAAACIINOE'



# Generated at 2022-06-14 05:47:39.551749
# Unit test for function decompress
def test_decompress():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert original==decompressed


# Generated at 2022-06-14 05:47:51.088470
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    #formatter = __StringFormatter('S.o.S  a ,  B.  C  D.  E. F.   G  H  I  J  K  L.  M  N  O  P .Q  R.  S  T  U  V  W X  Y  Z')
    formatter = __StringFormatter('  s.o.s  a ,  b.  c  d.  e. f.   g  h  i  j  k  l.  m  n  o  p .q  r.  s  t  u  v  w x  y  z')
    assert formatter.format() == 'S.O.S. A, B. C D. E. F. G H I J K L. M N O P. Q R. S T U V W X Y Z'



# Generated at 2022-06-14 05:47:52.866547
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    assert __StringFormatter('this is a   stupid test#') is not None



# Generated at 2022-06-14 05:48:06.295912
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    # Tests to check that the function correctly converts a snake case string in a camel case one
    assert snake_case_to_camel('foo') == 'Foo'
    assert snake_case_to_camel('foo_bar') == 'FooBar'
    assert snake_case_to_camel('foo_bar_harry') == 'FooBarHarry'
    assert snake_case_to_camel('foo_bar', False) == 'fooBar'
    assert snake_case_to_camel('foo_bar_harry', False) == 'fooBarHarry'

    # Tests to check that the function correctly converts a snake case string (with custom separator) in a camel case one
    assert snake_case_to_camel('foo-bar', True, '-') == 'FooBar'
    assert snake_case_to_c

# Generated at 2022-06-14 05:48:09.436717
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.encode(7) == 'VII'
    assert __RomanNumbers.encode(555) == 'DLV'
    assert __RomanNumbers.decode('MCMLXXII') == 1972
    assert __RomanNumbers.decode('IX') == 9


# PUBLIC API



# Generated at 2022-06-14 05:48:20.244426
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode(0) == ''
    assert roman_encode(1) == 'I'
    assert roman_encode(4) == 'IV'
    assert roman_encode(5) == 'V'
    assert roman_encode(7) == 'VII'
    assert roman_encode(8) == 'VIII'
    assert roman_encode(9) == 'IX'
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode(80) == 'LXXX'
    assert roman_encode(89) == 'LXXXIX'
    assert roman_encode(90) == 'XC'
    assert roman_encode(234) == 'CCXXXIV'

# Generated at 2022-06-14 05:48:23.897834
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    assert __StringCompressor.compress('foo') == 'eJwLzs8M'
    assert __StringCompressor.decompress('eJwLzs8M') == 'foo'


# PUBLIC API



# Generated at 2022-06-14 05:48:32.876461
# Unit test for function roman_encode
def test_roman_encode():
    assert is_equal(roman_encode(1), 'I')
    assert is_equal(roman_encode(23), 'XXIII')
    assert is_equal(roman_encode(37), 'XXXVII')
    assert is_equal(roman_encode(58), 'LVIII')
    assert is_equal(roman_encode(94), 'XCIV')
    assert is_equal(roman_encode(100), 'C')
    assert is_equal(roman_encode(2018), 'MMXVIII')
    assert is_equal(roman_encode(3999), 'MMMCMXCIX')

test_roman_encode()

