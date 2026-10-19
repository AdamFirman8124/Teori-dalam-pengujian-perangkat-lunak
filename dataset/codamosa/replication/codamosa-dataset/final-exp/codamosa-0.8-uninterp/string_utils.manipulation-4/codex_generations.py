

# Generated at 2022-06-14 05:38:53.645978
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'the-snake-is-green'
    assert snake_case_to_camel('no-way', separator='-') == 'NoWay'
    assert snake_case_to_camel('nope') == 'Nope'



# Generated at 2022-06-14 05:38:57.225934
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('hello_world') == 'HelloWorld'
    assert snake_case_to_camel('hello') == 'Hello'
    assert snake_case_to_camel('a_b_c', False) == 'aBC'



# Generated at 2022-06-14 05:38:59.950369
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    f = __StringFormatter('this-is-a-sample')
    assert f.format() == 'This is a sample'


# PUBLIC API



# Generated at 2022-06-14 05:39:11.784437
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('snake_case_string') == 'SnakeCaseString'
    assert snake_case_to_camel('snake_case_string', upper_case_first=False) == 'snakeCaseString'
    assert snake_case_to_camel('snake-case-string', separator='-') == 'SnakeCaseString'
    assert snake_case_to_camel('snake_case_string', separator='-') == 'snake_case_string'
    assert snake_case_to_camel('snake_case_string', separator='*') == 'snake_case_string'
    assert snake_case_to_camel('snake_case_string', separator='*', upper_case_first=False) == 'snake_case_string'



# Generated at 2022-06-14 05:39:24.136168
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # pylint: disable=locally-disabled,no-member
    formatter = __StringFormatter
    assert formatter('  Hello World    ').format() == 'Hello World'
    assert formatter('hello World').format() == 'Hello World'
    assert formatter('HELLO WORLD').format() == 'Hello World'
    assert formatter('To HELLO WORLD').format() == 'To HELLO WORLD'
    assert formatter('Hello World').format() == 'Hello World'
    assert formatter('Hello, World!!!').format() == 'Hello, World!'
    assert formatter('Hello, world!!!').format() == 'Hello, World!'
    assert formatter('@Hello @World  ').format() == '@Hello @World'
    assert formatter('Hello.  World  ').format() == 'Hello. World'
    assert form

# Generated at 2022-06-14 05:39:27.052377
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('not_valid_string', upper_case_first=False) == 'not_valid_string'
    assert snake_case_to_camel('the snake is green', upper_case_first=False, separator=' ') == 'theSnakeIsGreen'



# Generated at 2022-06-14 05:39:31.479552
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('test_test_test') == 'TestTestTest'
    assert snake_case_to_camel('test_test_test', upper_case_first=False) == 'testTestTest'



# Generated at 2022-06-14 05:39:32.599823
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'



# Generated at 2022-06-14 05:39:43.187966
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    test_data = [
        ('lower_case', 'lowerCase'),
        ('UPPER_CASE', 'upperCase'),
        ('mix_ed_case', 'mixEdCase'),
        ('a_nsb_df', 'aNsbDf'),
        ('_a_b_', '_a_b_'),
        ('__a_b', '__aB'),
        ('a_b__', 'aB__'),
        ('__a_b__', '__a_b__'),
        ('__a_b__', '__aB__', False),
        ('__a_b__', '__a__b__', '__'),
    ]
    for i in range(len(test_data)):
        expected = test_data[i][1]

# Generated at 2022-06-14 05:39:49.621614
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    test_match(snake_case_to_camel('test_test_test'), 'TestTestTest')
    test_match(snake_case_to_camel('test_test_test', False), 'testTestTest')
    test_match(snake_case_to_camel('test_test_test', False, '-'), 'testTestTest')
    test_match(snake_case_to_camel('test-test-test', False, '-'), 'testTestTest')
    test_match(snake_case_to_camel('a_b_c_d', True), 'ABCD')
    test_match(snake_case_to_camel('a_b_c_d', False), 'aBCD')


# Generated at 2022-06-14 05:40:06.283563
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('  hello  world  ').format() == 'Hello world'
    assert __StringFormatter('  HELLO  WORLD  ').format() == 'Hello world'
    assert __StringFormatter('  hello  world and hello  mars  ').format() == 'Hello world and hello mars'
    assert __StringFormatter('  hello  world. and hello  mars  ').format() == 'Hello world. And hello mars'
    assert __StringFormatter('hello world of mars').format() == 'Hello world of mars'
    assert __StringFormatter('HELLO WORLD OF MARS').format() == 'Hello world of mars'
    assert __StringFormatter('Hello World of Mars').format() == 'Hello World of Mars'

# Generated at 2022-06-14 05:40:17.172638
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:40:24.181935
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    input_string = '  !\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~  '
    expected_string = '! "#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    assert __StringFormatter(input_string).format() == expected_string
    print('test___StringFormatter_format passed')



# Generated at 2022-06-14 05:40:31.143039
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # we use a double underscore at the beginning of the function name to ensure that this function will not be
    # listed by the "automagic" documentation generator
    assert __StringFormatter(' ').format() == ''
    assert __StringFormatter('    ').format() == ''
    assert __StringFormatter('').format() == ''
    assert __StringFormatter('   d   ').format() == 'd'
    assert __StringFormatter(' d ').format() == 'd'
    assert __StringFormatter('   d ').format() == 'd'
    assert __StringFormatter(' d   ').format() == 'd'
    assert __StringFormatter(' d  a ').format() == 'd a'
    assert __StringFormatter(' d a ').format() == 'd a'

# Generated at 2022-06-14 05:40:43.813743
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:40:52.989244
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # test all uppercase strings
    assert __StringFormatter('FOO BAR').format() == 'Foo bar'
    assert __StringFormatter('FOO-BAR').format() == 'Foo Bar'
    assert __StringFormatter('FOO_BAR').format() == 'Foo Bar'
    assert __StringFormatter('FOO_BAR_BAZ').format() == 'Foo Bar Baz'
    assert __StringFormatter('FOO_BAR_BAZ-QOO').format() == 'Foo Bar Baz Qoo'
    assert __StringFormatter('FOO.BAR').format() == 'Foo Bar'
    assert __StringFormatter('FOO_BAR_BAZ').format() == 'Foo Bar Baz'

# Generated at 2022-06-14 05:41:03.115630
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('axxBx xxCx xDx').format() == 'Axx Bx Xxcx X Dx'
    assert __StringFormatter('xxxxDx xxCx xBx axx').format() == 'Xxxx Dx Xxcx X Bx Axx'
    assert __StringFormatter('i xxDx xxCx xBx axx').format() == 'I Xxx Dx Xxcx X Bx Axx'
    assert __StringFormatter('xxDx I xxCx xBx axx').format() == 'Xx Dx I Xxcx X Bx Axx'
    assert __StringFormatter('--xxDx I xxCx xBx axx--').format() == '--Xx Dx I Xxcx X Bx Axx--'

# Generated at 2022-06-14 05:41:17.441787
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    from ._regex import PRETTIFY_RE
    from .validation import is_full_string
    import unittest


# Generated at 2022-06-14 05:41:28.159401
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('  hello    world    ').format() == 'hello world'
    assert __StringFormatter('hello    world').format() == 'hello world'
    assert __StringFormatter('hello world   ').format() == 'hello world'
    assert __StringFormatter('Hello    world').format() == 'Hello world'
    assert __StringFormatter('hello,world').format() == 'hello, world'
    assert __StringFormatter('hello,world.').format() == 'hello, world.'
    assert __StringFormatter('hello,  world.').format() == 'hello, world.'
    assert __StringFormatter('hello : world').format() == 'hello: world'
    assert __StringFormatter('http://www.google.com/').format() == 'http://www.google.com/'
    assert __StringFormatter

# Generated at 2022-06-14 05:41:41.259864
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:41:56.767750
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:42:04.001659
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert 'The Quick Brown Fox' == __StringFormatter('the quick brown fox').format()
    assert 'Some Url' == __StringFormatter('some url').format()
    assert 'Some Email' == __StringFormatter('some email').format()
    assert 'Snakes Are Cool' == __StringFormatter('snakes are cool').format()
    assert 'Snakes Are Also Cool' == __StringFormatter('snakes are also cool').format()
    assert 'Do You Love Python' == __StringFormatter('Do you love python?').format()
    assert 'Do You Love Python' == __StringFormatter('Do you love Python?').format()
    assert 'Do You Love Python' == __StringFormatter('Do you love Python').format()
    assert 'Do You Love Python' == __StringFormatter('Do   you   love   Python').format()
   

# Generated at 2022-06-14 05:42:17.666463
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:42:25.471685
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:42:38.457977
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    f = __StringFormatter('this is a simple test case')
    assert f.format() == 'This is a simple test case'
    f = __StringFormatter('this is a simple test case. url: www.google.com')
    assert f.format() == 'This is a simple test case. URL: www.google.com'
    f = __StringFormatter('this is a simple test case. url: www.google.com, email: tophe@gmail.com')
    assert f.format() == 'This is a simple test case. URL: www.google.com, email: tophe@gmail.com'
    f = __StringFormatter('---this is a simple test case---')
    assert f.format() == '---This is a simple test case---'
    f = __StringFormatter('|this is a simple test case|')

# Generated at 2022-06-14 05:42:44.878153
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    out = __StringFormatter('  hello   WORLD!   please   contact me at   e-mail@email.com    and visit my site: http://www.this.it/place   ').format()
    assert out == 'Hello World! Please contact me at e-mail@email.com and visit my site: http://www.this.it/place'


# PUBLIC API

# camel case

# Generated at 2022-06-14 05:42:56.143304
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('hello world').format() == 'Hello world'
    assert __StringFormatter('hello world !').format() == 'Hello world!'
    assert __StringFormatter('hello world !!').format() == 'Hello world!!'
    assert __StringFormatter('hello world !!!').format() == 'Hello world!!!'
    assert __StringFormatter('hello   world').format() == 'Hello world'
    assert __StringFormatter('hello   world   !').format() == 'Hello world!'
    assert __StringFormatter('hello   world   !!').format() == 'Hello world!!'
    assert __StringFormatter('hello   world   !!!').format() == 'Hello world!!!'
    assert __StringFormatter('hello world !!! ').format() == 'Hello world!!!'
    assert __StringFormatter('hello world !! !! !!').format

# Generated at 2022-06-14 05:43:03.458795
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('  test  ').format() == 'Test'
    assert __StringFormatter('  test  test  ').format() == 'Test test'
    assert __StringFormatter('  test  test  test  ').format() == 'Test test test'
    assert __StringFormatter('test  test  test').format() == 'Test test test'
    assert __StringFormatter('test   test    test').format() == 'Test test test'
    assert __StringFormatter('test--test--test').format() == 'Test-test-test'
    assert __StringFormatter('test--test--test--').format() == 'Test-test-test-'
    assert __StringFormatter('--test--test--test').format() == '-test-test-test'

# Generated at 2022-06-14 05:43:12.844142
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:43:17.170654
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # args
    input_string = 'I have an email: fabio@example.com. And a website: http://www.example.com/. ' \
                   'And I like to write like: "This is a test".'

    # execute
    out = __StringFormatter(input_string).format()

    # assert
    assert out == 'I have an email: fabio@example.com. And a website: http://www.example.com/. ' \
                  'And I like to write like: "This is a test".'


# public api


# Generated at 2022-06-14 05:43:25.432803
# Unit test for function strip_margin
def test_strip_margin():
    assert strip_margin('''
                        |line 1
                        |line 2
                        |line 3
                        |''') == """
line 1
line 2
line 3
"""

# Generated at 2022-06-14 05:43:33.542172
# Unit test for function strip_html
def test_strip_html():
    input_string = '<p>Welcome to <a href="http://www.webcodegeeks.com">WebCodeGeeks</a></p>'
    output_string = 'Welcome to WebCodeGeeks'
    output_string_2 = 'Welcome to '
    assert strip_html(input_string) == output_string, 'HtmlTag does not match expected string'
    assert strip_html(input_string, False) == output_string_2, 'HtmlTag does not match expected string'

# Generated at 2022-06-14 05:43:38.228288
# Unit test for function compress
def test_compress():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = __StringCompressor.compress(original)
    assert isinstance(compressed, str)



# Generated at 2022-06-14 05:43:43.354688
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.encode(1) == 'I'
    assert __RomanNumbers.encode(3999) == 'MMMCMXCIX'

    assert __RomanNumbers.decode('I') == 1
    assert __RomanNumbers.decode('MMMCMXCIX') == 3999


# PUBLIC API



# Generated at 2022-06-14 05:43:46.114876
# Unit test for function shuffle
def test_shuffle():
    assert shuffle('') == ''
    assert shuffle('hello') == 'hello'
    assert shuffle('this string can be shuffled') == 'tshhr ngeriigcst sabntlee'



# Generated at 2022-06-14 05:43:56.987393
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    # Test for invalid inputs
    try:
        snake_case_to_camel(None)
        assert False, 'Exception expected'
    except InvalidInputError:
        pass

    input = ''
    assert snake_case_to_camel(input) == input

    # Test conversion with default settings
    input = 'this_is_a_camel_case_string_test'
    expected = 'ThisIsACamelCaseStringTest'
    assert snake_case_to_camel(input) == expected

    input = 'this_is_a_camel_case_string_test'
    expected = 'thisIsACamelCaseStringTest'
    assert snake_case_to_camel(input, upper_case_first=False) == expected

    input = 'this_is_a_camel_case_string_test'
   

# Generated at 2022-06-14 05:43:58.563196
# Unit test for function booleanize
def test_booleanize():
  assert booleanize('true') == True
  assert booleanize('YES') == True
  assert booleanize('nope') == False

# Generated at 2022-06-14 05:44:10.704602
# Unit test for function roman_decode
def test_roman_decode():
    assert __RomanNumbers.decode('X') == 10
    assert __RomanNumbers.decode('L') == 50
    assert __RomanNumbers.decode('C') == 100
    assert __RomanNumbers.decode('D') == 500
    assert __RomanNumbers.decode('M') == 1000
    assert __RomanNumbers.decode('XII') == 12
    assert __RomanNumbers.decode('II') == 2
    assert __RomanNumbers.decode('IV') == 4
    assert __RomanNumbers.decode('IX') == 9
    assert __RomanNumbers.decode('CD') == 400
    assert __RomanNumbers.decode('CM') == 900
    assert __RomanNumbers.decode('CM') == 900
    assert __RomanNumbers.decode('CM') == 900
    assert __RomanNumbers.decode('CM') == 900

# Generated at 2022-06-14 05:44:22.757681
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('test test').format() == 'Test test'
    assert __StringFormatter('test,test').format() == 'Test, test'
    assert __StringFormatter('test-test').format() == 'Test - test'
    assert __StringFormatter('test(test)').format() == 'Test (test)'
    assert __StringFormatter('test -- test').format() == 'Test - test'
    assert __StringFormatter('test test test').format() == 'Test test test'
    assert __StringFormatter('test/test/test').format() == 'Test/test/test'
    assert __StringFormatter('test:test:test').format() == 'Test: test: test'
    assert __StringFormatter('test\ttest\ttest').format() == 'Test test test'

# Generated at 2022-06-14 05:44:30.773891
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    # The string "ciao" is a perfect candidate for compression, therefore
    # we expect that its compressed version will be shorter than its original version
    original_string = "ciao"
    compressed_string = __StringCompressor.compress(original_string)
    assert(len(compressed_string) < len(original_string))

    # decompress the string and check whether it match the original one
    decompressed_string = __StringCompressor.decompress(compressed_string)
    assert(original_string == decompressed_string)


# PUBLIC API



# Generated at 2022-06-14 05:44:34.696944
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert isinstance(__RomanNumbers, type)



# Generated at 2022-06-14 05:44:37.144911
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'

test_asciify()


# Generated at 2022-06-14 05:44:38.636402
# Unit test for function roman_encode
def test_roman_encode():
    assert(roman_encode(37)=='XXXVIII')
test_roman_encode()


# Generated at 2022-06-14 05:44:39.762089
# Unit test for function strip_margin
def test_strip_margin():
    assert strip_margin('''
        line 1
        line 2
        line 3
    ''') == '''
line 1
line 2
line 3
'''



# Generated at 2022-06-14 05:44:44.461192
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    test_input = ' '
    test_output = __StringFormatter(test_input)
    assert isinstance(test_output, __StringFormatter)

# Generated at 2022-06-14 05:44:48.995430
# Unit test for function slugify
def test_slugify():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'

# Generated at 2022-06-14 05:44:50.475499
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode('2020') == 'MMXX'
    assert roman_encode(3999) == 'MMMCMXCIX'



# Generated at 2022-06-14 05:44:59.740887
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:45:04.470490
# Unit test for function decompress
def test_decompress():
    """Unit test for function decompress"""
    print('test_decompress')

    compressed = 'TkMwCkwIaxAjEAlMCMQJxAlMQQQJxAxECYQJxAxECYQJxAxECYQJxAxECYQJxAxECYQJxAxECYQJxAxECYQJxAxECYQJxAxECYQJxAxECYQJxAxECYQMRAmECcQMRAmECcQMRAmECcQJxAxECYQJxAxECYQJxAxECYQJxAxECYQJxAxL'

    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    out = decompress(compressed)


# Generated at 2022-06-14 05:45:08.444434
# Unit test for function compress
def test_compress():
    n = 0
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    assert(original == decompress(compressed))



# Generated at 2022-06-14 05:45:26.768510
# Unit test for constructor of class __StringCompressor

# Generated at 2022-06-14 05:45:31.833908
# Unit test for function reverse
def test_reverse():
    assert reverse('hello') == 'olleh'
    assert reverse('hello world') == 'dlrow olleh'
    assert reverse('123456') == '654321'
    assert reverse('The first letter is the last letter') == 'rettele tsrif si eht tsrif ehT'

CAMEL_CASE_TO_SNAKE_CACHE = {}



# Generated at 2022-06-14 05:45:42.698770
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    # Should not have any exception here
    __StringFormatter('123')

    # Should raise an InvalidInputError because only strings are allowed as input
    try:
        __StringFormatter(123)
        raise AssertionError('test___StringFormatter: no exception thrown')
    except InvalidInputError:
        pass

    # Should raise a ValueError because we are sending an empty string
    try:
        __StringFormatter('')
        raise AssertionError('test___StringFormatter: no exception thrown')
    except ValueError:
        pass


# PUBLIC API


# Generated at 2022-06-14 05:45:53.554436
# Unit test for function prettify
def test_prettify():
    string1 = '  U N P  R E T T I F I E D  S T R I N G  '
    assert prettify(string1) == 'U N P R E T T I F I E D S T R I N G'

    string2 = 'UNPRETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTIIIIIIFIIIIIIIIEEEEDDDD STRIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNNGGGGGGGGGGGG'

# Generated at 2022-06-14 05:45:58.038271
# Unit test for function strip_margin
def test_strip_margin():

    margin_string = '''
        line 1
        line 2
        line 3
    '''

    no_margin_string = '''
line 1
line 2
line 3
'''

    assert strip_margin(margin_string) == no_margin_string



# Generated at 2022-06-14 05:45:58.577810
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('y') == True


# Generated at 2022-06-14 05:46:03.266762
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    input_string = 'hello, my name is giovanni, and i\'m a developer. i work for a "company" and i love it! Are you ' \
                   'the best developer? you\'re the best developer! '

    assert __StringFormatter(input_string).format() == 'Hello, my name is Giovanni, and I\'m a developer. I work for ' \
                                                       'a "company" and I love it! Are you the best developer? ' \
                                                       'You\'re the best developer!'


# Generated at 2022-06-14 05:46:04.149688
# Unit test for function reverse
def test_reverse():
    assert reverse('hello') == 'olleh'
# Test results for function reverse



# Generated at 2022-06-14 05:46:06.502125
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    formatter = __StringFormatter("i am a simple string")
    assert formatter != None


# Generated at 2022-06-14 05:46:09.831209
# Unit test for function reverse
def test_reverse():
    assert reverse('hello world') == 'dlrow olleh'
    assert reverse('@') == '@'
    assert reverse('123') == '321'



# Generated at 2022-06-14 05:46:25.988835
# Unit test for function strip_html
def test_strip_html():
    toTest = strip_html('test: <a href="foo/bar">click here</a>')
    assert toTest == 'test: '
    toTest2 = strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True)
    assert toTest2 == 'test: click here'


# Generated at 2022-06-14 05:46:28.936964
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode('37') == 'XXXVII'
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode('2020') == 'MMXX'
    assert roman_encode(2020) == 'MMXX'



# Generated at 2022-06-14 05:46:34.606481
# Unit test for function decompress
def test_decompress():
    """
    Testing function decompress.
    """

# Generated at 2022-06-14 05:46:40.088377
# Unit test for function decompress
def test_decompress():
    assert decompress('eJwLAA==')=='a'
    assert decompress('eJyBaLz8iA')=='abcde'
    assert decompress('eJwLAAoAAgA==')=='abc'
    
test_decompress()

# Generated at 2022-06-14 05:46:47.785981
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('III') == 3
    assert roman_decode('IV') == 4
    assert roman_decode('XXII') == 22
    assert roman_decode('VIII') == 8
    assert roman_decode('XIX') == 19
    assert roman_decode('XXXIX') == 39
    assert roman_decode('XLIV') == 44
    assert roman_decode('XLIX') == 49
    assert roman_decode('LXXVII') == 77
    assert roman_decode('XCIX') == 99
    assert roman_decode('CCCXCIX') == 399
    assert roman_decode('CMXCIX') == 999
    assert roman_decode('MDCCCXLIX') == 1849

# Generated at 2022-06-14 05:46:52.369126
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('someText') == 'some_text'
    assert camel_case_to_snake('someMixedDelimitersIsGoodLike_this') == 'some_mixed_delimiters_is_good_like_this'
    assert camel_case_to_snake('anotherUUIDExample') == 'another_uuid_example'
    assert camel_case_to_snake('a4') == 'a4'
    assert camel_case_to_snake('a4', '-') == 'a-4'
    assert camel_case_to_snake('invalid') == 'invalid'
    
test_camel_case_

# Generated at 2022-06-14 05:46:54.466368
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert isinstance(__RomanNumbers, object, '__RomanNumbers is not an object')



# Generated at 2022-06-14 05:47:08.446562
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    string = 'TEST'
    assert string.upper() == __StringFormatter(string).format()

    string = 'test'
    assert string.title() == __StringFormatter(string).format()

    string = 'test  '
    assert string.strip() == __StringFormatter(string).format()

    string = '  test'
    assert string.strip() == __StringFormatter(string).format()

    string = '  test  '
    assert string.strip() == __StringFormatter(string).format()

    string = '  test  test  '
    assert 'test test' == __StringFormatter(string).format()

    string = '  test   test   test  '
    assert 'test test test' == __StringFormatter(string).format()

    string = 'te  st'
    assert 'te st'

# Generated at 2022-06-14 05:47:12.233234
# Unit test for function strip_margin
def test_strip_margin():
    expected_string = '''
line 1
line 2
line 3
'''
    test_string = '''
                 line 1
                 line 2
                 line 3
'''
    
    assert strip_margin(test_string) == expected_string

# Generated at 2022-06-14 05:47:15.800186
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'



# Generated at 2022-06-14 05:47:38.994120
# Unit test for function compress
def test_compress():
    assert compress('foo bar') == 'eNpLzs/Pyc3JzE3Jz87PTghJzM7NzE/KjU7NzU\n' \
                                  '7NyU7OyMnPT0vMDc1NDQ2NjQ2OTk5NjY5NjY5PjY5\n' \
                                  'Nzs3Pzs7Kzs3Ozs7Ozs7Ozs7Pzs7Ow==\n'



# Generated at 2022-06-14 05:47:42.572598
# Unit test for function strip_margin
def test_strip_margin():
    margin = '|'
    out = strip_margin('''
        |line 1
        |line 2
        |line 3
    ''', margin)
    assert out == '''
line 1
line 2
line 3
    '''




# Generated at 2022-06-14 05:47:48.525083
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    input_string = 'this is a test'
    assert __StringCompressor.compress(input_string) == 'eNoJDgJADAAYK0a0tMZr9g=='
    assert __StringCompressor.decompress(__StringCompressor.compress(input_string)) == input_string


# START PUBLIC API



# Generated at 2022-06-14 05:48:01.590681
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    assert __StringCompressor.compress('test') == 'eJwLzSktKAst6laoUQA='
    assert __StringCompressor.decompress('eJwLzSktKAst6laoUQA=') == 'test'
    assert __StringCompressor.compress('"test" test "test"') == 'eJwLVUktKi0BQzM9PQspMzM-T1A1TkvOj4_W8sA='
    assert __StringCompressor.decompress('eJwLVUktKi0BQzM9PQspMzM-T1A1TkvOj4_W8sA=') == '"test" test "test"'

# PUBLIC API



# Generated at 2022-06-14 05:48:13.060100
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    for i in range(100):
        input_string = random.choice(['String1', 'String2', 'String3'])
        try:
            formatter = __StringFormatter(input_string)
            assert formatter.input_string == input_string
        except InvalidInputError:
            print('Failed to initialize __StringFormatter with string {}'.format(input_string))
    
    input_string = ' '
    formatter = __StringFormatter(input_string)
    assert formatter.input_string == input_string

    try:
        formatter = __StringFormatter(3)
    except InvalidInputError:
        print('Failed to initialize __StringFormatter with integer {}'.format(3))


# Generated at 2022-06-14 05:48:23.109294
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.encode(1) == 'I'
    assert __RomanNumbers.encode(3) == 'III'
    assert __RomanNumbers.encode(4) == 'IV'
    assert __RomanNumbers.encode(6) == 'VI'
    assert __RomanNumbers.encode(7) == 'VII'
    assert __RomanNumbers.encode(10) == 'X'
    assert __RomanNumbers.encode(33) == 'XXXIII'
    assert __RomanNumbers.encode(41) == 'XLI'
    assert __RomanNumbers.encode(43) == 'XLIII'
    assert __RomanNumbers.encode(55) == 'LV'
    assert __RomanNumbers.encode(71) == 'LXXI'
    assert __RomanNumbers.encode(83) == 'LXXXIII'
