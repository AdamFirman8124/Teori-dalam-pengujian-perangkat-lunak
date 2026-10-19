

# Generated at 2022-06-14 05:38:47.378881
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'the_snake_is_green'
    assert snake_case_to_camel('the_snake_is_green', False, '-') == 'the_snake_is_green'
    assert snake_case_to_camel('TheSnakeIsGreen') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('TheSnakeIsGreen', False) == 'TheSnakeIsGreen'

# Generated at 2022-06-14 05:38:58.409600
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    formatter = __StringFormatter('this is a  test')
    assert formatter.format() == 'This is a test'

    formatter = __StringFormatter('  this is a  test  ')
    assert formatter.format() == 'This is a test'

    formatter = __StringFormatter('this-is-a-test')
    assert formatter.format() == 'This is a test'

    formatter = __StringFormatter('this_is_a_test')
    assert formatter.format() == 'This is a test'

    formatter = __StringFormatter('thIs-is_a-test')
    assert formatter.format() == 'This is a test'

    formatter = __StringFormatter('this-is-a-test-yup')

# Generated at 2022-06-14 05:39:02.736875
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('theSnakeIsGreen') == 'TheSnakeIsGreen'



# Generated at 2022-06-14 05:39:09.146632
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('a string with many     spaces     inside').format() == 'A string with many spaces inside'
    assert __StringFormatter('string without spaces').format() == 'String without spaces'
    assert __StringFormatter('a string with an email address: email@example.com').format() == \
           'A string with an email address: email@example.com'
    assert __StringFormatter('a string with a url: https://www.example.com').format() == \
           'A string with a url: https://example.com'
    assert __StringFormatter('saXon\'s genitive').format() == 'Saxon genitive'
    assert __StringFormatter('a string with   bad spaces').format() == 'A string with bad spaces'
    assert __StringFormatter('string with extra  spaces   (more spaces)').format

# Generated at 2022-06-14 05:39:15.758082
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # Initialize the class
    sf = __StringFormatter('this is my text')

    # Call the method
    result = sf.format()

    # Check the result
    assert 'This is my text' == result
    assert 'This is my text' != sf.input_string

test___StringFormatter_format()


# Generated at 2022-06-14 05:39:25.947854
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():

    def test_it():
        formatter = __StringFormatter('This is a test      string')
        assert formatter.format() == 'This is a test string'

    def test_it_with_url():
        formatter = __StringFormatter('This is a test string http://www.google.com')
        assert formatter.format() == 'This is a test string http://www.google.com'

    def test_it_with_email():
        formatter = __StringFormatter('This is a test string test@gmail.com')
        assert formatter.format() == 'This is a test string test@gmail.com'

    def test_it_with_lowercase_first_char():
        formatter = __StringFormatter('this is a test string')
        assert formatter.format() == 'This is a test string'

   

# Generated at 2022-06-14 05:39:36.733669
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='_') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='') == 'the_snake_is_green'



# Generated at 2022-06-14 05:39:49.849367
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    actual = __StringFormatter('test, this method is AWESOME!')
    expected = 'Test, this method is awesome!'
    assert actual.format() == expected

    actual = __StringFormatter('Let\'s  test  multiple  spaces  inside  a sentence.')
    expected = 'Let\'s test multiple spaces inside a sentence.'
    assert actual.format() == expected

    actual = __StringFormatter('Let\'s  test  multiple  spaces  inside  a sentence.   ')
    expected = 'Let\'s test multiple spaces inside a sentence.'
    assert actual.format() == expected

    actual = __StringFormatter(' Let\'s  test  multiple  spaces  inside  a sentence.   ')
    expected = 'Let\'s test multiple spaces inside a sentence.'
    assert actual.format() == expected


# Generated at 2022-06-14 05:40:02.529628
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('Foo bar   foo bar ').format() == 'Foo Bar Foo Bar'
    assert __StringFormatter('foo bar foo bar').format() == 'Foo Bar Foo Bar'
    assert __StringFormatter('FOO BAR FOO BAR').format() == 'Foo Bar Foo Bar'
    assert __StringFormatter('foo-bar foo-bar').format() == 'Foo-Bar Foo-Bar'
    assert __StringFormatter('foo.bar foo.bar').format() == 'Foo.Bar Foo.Bar'
    assert __StringFormatter('foo:bar foo:bar').format() == 'Foo:Bar Foo:Bar'
    assert __StringFormatter('foo\'s bar foo\'s bar').format() == 'Foo\'s Bar Foo\'s Bar'

# Generated at 2022-06-14 05:40:10.179000
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # Basic tests
    assert __StringFormatter('this is a test').format() == 'This is a test'
    assert __StringFormatter('  this is a test  ').format() == 'This is a test'
    assert __StringFormatter('This is a test').format() == 'This is a test'
    assert __StringFormatter('this is a test.This is a test').format() == 'This is a test. This is a test'
    assert __StringFormatter('this is a test:This is a test').format() == 'This is a test: This is a test'
    assert __StringFormatter('this is a test->This is a test').format() == 'This is a test -> This is a test'

# Generated at 2022-06-14 05:40:20.178010
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('tHE_sNAKE_iS_gREEN') == 'THeSnakeIsGreen'
    assert snake_case_to_camel('tHE_sNAKE_iS_gREEN', upper_case_first=False) == 'tHeSnakeIsGreen'



# Generated at 2022-06-14 05:40:28.869429
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    # when
    snake_case = "this_is_a_snake"
    # and
    camel_case = snake_case_to_camel(snake_case)
    # then
    assert camel_case == "ThisIsASnake"

    # when
    snake_case = "a_long_snake_for_testing"
    # and
    camel_case = snake_case_to_camel(snake_case)
    # then
    assert camel_case == "ALongSnakeForTesting"



# Generated at 2022-06-14 05:40:32.643120
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('a_camel_string_test') == 'ACamelStringTest'



# Generated at 2022-06-14 05:40:44.469290
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    # create input string with a valid snake case and convert it to camel case
    input_string = 'I_have_a_pencil'
    output = snake_case_to_camel(input_string)
    assert output == 'IHaveAPencil'

    # create input string with a valid snake case and convert it to camel case
    input_string = 'i_have_a_pencil'
    output = snake_case_to_camel(input_string, upper_case_first=False)
    assert output == 'iHaveAPencil'

    # create input string with a valid snake case and convert it to camel case
    input_string = 'i_have_a_pencil'
    output = snake_case_to_camel(input_string, separator='-')
    assert output == 'IHaveAPencil'



# Generated at 2022-06-14 05:40:50.584005
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('this_is_a_snake_case_string') == 'ThisIsASnakeCaseString'
    assert snake_case_to_camel('this_is_a_snake_case_string', False) == 'thisIsASnakeCaseString'
    assert snake_case_to_camel('this_is_a_snake_case_string', separator='-') == 'ThisIsASnakeCaseString'



# Generated at 2022-06-14 05:40:59.332178
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    test_cases = {
        'this_is_a_test': 'ThisIsATest',
        '': '',
        'the_snake_is_longer': 'TheSnakeIsLonger',
        'the_snake_is_green': 'TheSnakeIsGreen',
        'the_snake_is_green_': 'TheSnakeIsGreen'
    }

    for k in test_cases:
        assert snake_case_to_camel(k) == test_cases[k]



# Generated at 2022-06-14 05:41:08.624433
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert(snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen')
    assert(snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen')
    assert(snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen')
    assert(snake_case_to_camel('the snake is green') == 'TheSnakeIsGreen')
    assert(snake_case_to_camel('ThisIsACamelStringTest') == 'ThisIsACamelStringTest')

test_snake_case_to_camel()



# Generated at 2022-06-14 05:41:19.126704
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel("snake_case") == "SnakeCase"
    assert snake_case_to_camel("snake_case",False) == "snakeCase"
    assert snake_case_to_camel('snake_case_is_the_best_case') == 'SnakeCaseIsTheBestCase'
    assert snake_case_to_camel('snake_case_is_the_best_case',False) == 'snakeCaseIsTheBestCase'

test_snake_case_to_camel()
print("Testing snake_case_to_camel: passed")

# Utility function to test a string

# Generated at 2022-06-14 05:41:33.220478
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('hello') == 'Hello'
    assert snake_case_to_camel('this_is_a_snake') == 'ThisIsASnake'
    assert snake_case_to_camel('this_is_a_snake', upper_case_first=False) == 'thisIsASnake'
    assert snake_case_to_camel('thisIsACamelCaseString') == 'ThisIsACamelCaseString'
    assert snake_case_to_camel('this_is_a_kebab-case-string', separator='-') == 'ThisIsAKebabCaseString'
    assert snake_case_to_camel('this_is_a_pascal_case_string') == 'ThisIsAPascalCaseString'

# Generated at 2022-06-14 05:41:37.535524
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green', True) is 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False) is 'theSnakeIsGreen'



# Generated at 2022-06-14 05:41:44.013967
# Unit test for function strip_margin
def test_strip_margin():
    assert strip_margin('''
     I am a poet;
     But my poetry is in my heart,
     Not in my pen.''') == '''
I am a poet;
But my poetry is in my heart,
Not in my pen.'''




# ROT13 implementation
# https://en.wikipedia.org/wiki/ROT13


# Generated at 2022-06-14 05:41:45.191054
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    _ = __RomanNumbers()



# Generated at 2022-06-14 05:41:53.240512
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'
    assert strip_html('<input type="text" style="font:14px Arial;border:0" value="Hi">') == ''
    assert strip_html('<input type="text" style="font:14px Arial;border:0" value="Hi">', True) == 'Hi'
    assert strip_html('<p>Here is a paragraph in <strong>bold</strong></p>') == 'Here is a paragraph in '

# Generated at 2022-06-14 05:42:05.247244
# Unit test for function strip_margin
def test_strip_margin():
    assert strip_margin('''
        | line 1
        | line 2
        | line 3
''') == '''
line 1
line 2
line 3
'''
    assert strip_margin('''
line 1
line 2
line 3
''') == '''
line 1
line 2
line 3
'''
    assert strip_margin('''
        line 1
        line 2
        line 3
''') == '''
line 1
line 2
line 3
'''
    assert strip_margin('''
        |line 1
        |line 2
        |line 3
''') == '''
line 1
line 2
line 3
'''

# Generated at 2022-06-14 05:42:18.503751
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('theSnakeIsGreen', separator='-') == 'TheSnakeIsGreen'

    assert snake_case_to_camel('the_snake_is_green', separator='/') == 'the_snake_is_green'
    assert snake_case_to_camel('the_snake_is_green', separator='/') == 'the_snake_is_green'
    assert snake_case_to_camel('this_is_a_test', separator='-') == 'ThisIsATest'


# Generated at 2022-06-14 05:42:22.948606
# Unit test for function slugify
def test_slugify():
    assert slugify('A B C') == 'a-b-c'
    assert slugify('ciao alice!!!!') == 'ciao-alice'
    assert slugify('https://www.youtube.com') == 'https:www.youtube.com'
    assert slugify('https://www.youtube.com/') == 'https:www.youtube.com:slug'
    assert slugify('<b>Hola</b> Alice!!!! <script>xss()</script>') == 'b:hola-b-alice:script:xss()script'
    assert slugify('HI! Alice') == 'hi-alice'



# Generated at 2022-06-14 05:42:24.590577
# Unit test for function asciify
def test_asciify():
    print(asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË'))



# Generated at 2022-06-14 05:42:26.237513
# Unit test for function reverse
def test_reverse():
    assert 'olleh' == reverse('hello')



# Generated at 2022-06-14 05:42:39.303883
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    import pytest
    from .validation import is_full_string
    sf = __StringFormatter('some    string to  format')
    assert is_full_string(sf.format())
    sf = __StringFormatter('Format   some   string   and   check   it!')
    assert sf.format() == 'Format some string and check it!'
    sf = __StringFormatter('format   a   string    with    spaces    inside')
    assert sf.format() == 'format a string with spaces inside'
    sf = __StringFormatter('An XML example: http://some.url/some/path/xml*example.xml')
    assert sf.format() == 'An XML example: http://some.url/some/path/xml*example.xml'

# Generated at 2022-06-14 05:42:42.512399
# Unit test for function strip_margin
def test_strip_margin():
    # test strip_margin
    print(strip_margin('''
                        line 1
                        line 2
                        line 3
    '''
    ))

# Generated at 2022-06-14 05:42:45.795838
# Unit test for function reverse
def test_reverse():
    assert reverse('hello') == 'olleh'

# Generated at 2022-06-14 05:42:53.684903
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('false') == False
    assert booleanize('FALSE') == False
    assert booleanize('true') == True
    assert booleanize('TRUE') == True
    assert booleanize('1') == True
    assert booleanize('2') == False
    assert booleanize('yes') == True
    assert booleanize('no') == False
    assert booleanize('y') == True
    assert booleanize('n') == False



# Generated at 2022-06-14 05:42:56.112556
# Unit test for function decompress
def test_decompress():
    assert decompress('H4sIAAAAAAAEAC1WO23MDQAy0QAgAJTtyTQNQAAAA=') == 'Hello, world!'

# Generated at 2022-06-14 05:42:58.257272
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



# Generated at 2022-06-14 05:43:11.473960
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():

    for i in range(-4,15):
        try:
            __StringCompressor.compress('abc', 'abc', i)
            assert False
        except ValueError:
            assert True

    try:
        __StringCompressor.compress('abc', 'efg')
        assert False
    except ValueError:
        assert True

    try:
        __StringCompressor.compress(None)
        assert False
    except InvalidInputError:
        assert True

    assert __StringCompressor.compress('') == ''

    try:
        __StringCompressor.decompress('')
        assert False
    except ValueError:
        assert True

    try:
        __StringCompressor.decompress(None)
        assert False
    except InvalidInputError:
        assert True


# Generated at 2022-06-14 05:43:13.250068
# Unit test for function decompress
def test_decompress():
    from uuid import uuid4
    from com.gio.common.utils import compress
    original = str(uuid4())
    c_original = compress(original)
    d_original = decompress(c_original)
    assert original == d_original



# Generated at 2022-06-14 05:43:21.254095
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('test').format() == 'Test'
    assert __StringFormatter('test test').format() == 'Test test'
    assert __StringFormatter('test     test').format() == 'Test test'
    assert __StringFormatter('  test test').format() == 'Test test'
    assert __StringFormatter('test test     ').format() == 'Test test'
    assert __StringFormatter('  test test  ').format() == 'Test test'
    assert __StringFormatter('test  test  test').format() == 'Test test test'
    assert __StringFormatter('test test test ').format() == 'Test test test'
    assert __StringFormatter(' test test test').format() == 'Test test test'
    assert __StringFormatter(' test test test ').format() == 'Test test test'

# Generated at 2022-06-14 05:43:31.138623
# Unit test for function prettify

# Generated at 2022-06-14 05:43:45.132774
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('test_string') == 'TestString'
    assert snake_case_to_camel('test_string', upper_case_first=False) == 'testString'
    assert snake_case_to_camel('test string') == 'TestString'
    assert snake_case_to_camel('test string', upper_case_first=False) == 'testString'
    assert snake_case_to_camel('test-string') == 'TestString'
    assert snake_case_to_camel('test-string', upper_case_first=False) == 'testString'
    assert snake_case_to_camel('test string', separator='-') == 'TestString'

# Generated at 2022-06-14 05:43:50.016715
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    expected0 = 'IV'
    actual0 = __RomanNumbers.encode(4)
    assert expected0 == actual0

    expected1 = 4
    actual1 = __RomanNumbers.decode('IV')
    assert expected1 == actual1

# Public API

# Generated at 2022-06-14 05:43:55.844862
# Unit test for function shuffle
def test_shuffle():
    in_str = 'hello world!'
    out_str = shuffle(in_str)
    assert len(in_str) == len(out_str)
    assert set(in_str) == set(out_str)
    assert in_str != out_str



# Generated at 2022-06-14 05:44:04.903716
# Unit test for function booleanize
def test_booleanize():
    assert booleanize("true") == True
    assert booleanize("True") == True
    assert booleanize("TRUE") == True
    assert booleanize("1") == True
    assert booleanize("yes") == True
    assert booleanize("y") == True
    assert booleanize("false") == False
    assert booleanize("False") == False
    assert booleanize("FALSE") == False
    assert booleanize("0") == False
    assert booleanize("no") == False
    assert booleanize("N") == False
test_booleanize()



# Generated at 2022-06-14 05:44:10.254285
# Unit test for function shuffle
def test_shuffle():
    assert shuffle('hello') != 'hello'
    assert len(shuffle('hello')) == 5
    assert shuffle('hello') != shuffle('hello')



# Generated at 2022-06-14 05:44:22.384917
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.decode('I') == 1
    assert __RomanNumbers.decode('II') == 2
    assert __RomanNumbers.decode('III') == 3
    assert __RomanNumbers.decode('IV') == 4
    assert __RomanNumbers.decode('V') == 5
    assert __RomanNumbers.decode('VI') == 6
    assert __RomanNumbers.decode('VII') == 7
    assert __RomanNumbers.decode('VIII') == 8
    assert __RomanNumbers.decode('IX') == 9
    assert __RomanNumbers.decode('X') == 10
    assert __RomanNumbers.decode('XI') == 11
    assert __RomanNumbers.decode('XII') == 12
    assert __RomanNumbers.decode('XIII') == 13

# Generated at 2022-06-14 05:44:26.016547
# Unit test for function shuffle
def test_shuffle():
    assert shuffle('hello world') != 'hello world'
    assert is_full_string(shuffle('hello world'))
    assert len(shuffle('hello world')) == len('hello world')



# Generated at 2022-06-14 05:44:35.462837
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    f = __StringFormatter('  HELLo!      This   is   a     test. https://www.google.com/  '
                          'https://anotherlink.com/ page? pippo=pluto&max=10.456&min=8.96'
                          'mailto:name@domain.com mailto:name@anotherdomain.com')
    assert f.format() == 'Hello! This is a test. https://www.google.com/ ' \
                         'https://anotherlink.com/ page? pippo=pluto&max=10.456&min=8.96 ' \
                         'mailto:name@domain.com mailto:name@anotherdomain.com'


# PUBLIC API



# Generated at 2022-06-14 05:44:44.802654
# Unit test for function decompress
def test_decompress():
    #pylint: disable=C0103
    input_string = 'word n0 word n1 word n2 word n3 word n4 word n5 word n6 word n7 word n8 word n9 word n10 word n11 word n12 word n13 word n14 word n15 word n16 word n17 word n18 word n19'
    expected_result = compress(input_string, encoding='utf-8', compression_level=9)
    result = decompress(expected_result, encoding='utf-8')

    assert result == input_string
    
test_decompress()


# Generated at 2022-06-14 05:44:56.324389
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:45:10.062344
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.encode(1) == 'I'
    assert __RomanNumbers.encode(2) == 'II'
    assert __RomanNumbers.encode(3) == 'III'
    assert __RomanNumbers.encode(4) == 'IV'
    assert __RomanNumbers.encode(5) == 'V'
    assert __RomanNumbers.encode(6) == 'VI'
    assert __RomanNumbers.encode(7) == 'VII'
    assert __RomanNumbers.encode(8) == 'VIII'
    assert __RomanNumbers.encode(9) == 'IX'
    assert __RomanNumbers.encode(10) == 'X'
    assert __RomanNumbers.encode(11) == 'XI'
    assert __RomanNumbers.encode(20) == 'XX'
    assert __RomanNumbers

# Generated at 2022-06-14 05:45:19.468218
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', upper_case_first=False, separator='-') == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False, separator='-') == 'the_snake_is_green'



# Generated at 2022-06-14 05:45:26.689555
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode("VII")==7


# Generated at 2022-06-14 05:45:29.376490
# Unit test for function asciify
def test_asciify():
    my_cases = [
        'èéùúòóäåëýñÅÀÁÇÌÍÑÓË', 'ciao', '', None, 0, 1.4, True, False, object(), {}
    ]

    for case in my_cases:
        if case is not None:
            assert asciify(case) is not None
            assert is_string(asciify(case))



# Generated at 2022-06-14 05:45:33.228509
# Unit test for function compress
def test_compress():
    n = 0
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    if len(compressed) > 100:
        assert False, "compress failed"
    else:
        assert True, "passed"



# Generated at 2022-06-14 05:45:37.893851
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'



# Generated at 2022-06-14 05:45:39.692428
# Unit test for function shuffle
def test_shuffle():
    assert shuffle('hello world') == 'l wodheorll'



# Generated at 2022-06-14 05:45:47.610518
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False, '-') == 'the-snake-is-green'
    assert snake_case_to_camel('the_snake_is_green', True, '-') == 'The-Snake-Is-Green'



# Generated at 2022-06-14 05:45:49.133041
# Unit test for function reverse
def test_reverse():
    assert reverse('hello') == 'olleh'


# Generated at 2022-06-14 05:45:51.393708
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode(1) == 'I'
    assert roman_encode(2) == 'II'
    assert roman_encode(3) == 'III'
    assert roman_encode(4) == 'IV'
    assert roman_encode(20) == 'XX'
    assert roman_encode(2020) == 'MMXX'


# Generated at 2022-06-14 05:45:55.628824
# Unit test for function roman_encode
def test_roman_encode():
    # valid numbers
    assert roman_encode(1) == 'I'
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode(45) == 'XLV'
    assert roman_encode(2) == 'II'
    assert roman_encode(3) == 'III'
    assert roman_encode('3') == 'III'
    assert roman_encode(4) == 'IV'
    assert roman_encode('4') == 'IV'
    assert roman_encode(5) == 'V'
    assert roman_encode('5') == 'V'
    assert roman_encode(6) == 'VI'
    assert roman_encode('6') == 'VI'

# Generated at 2022-06-14 05:45:56.932931
# Unit test for function shuffle
def test_shuffle():
    assert shuffle('hello world') != 'hello world'
test_shuffle()



# Generated at 2022-06-14 05:46:18.910326
# Unit test for function compress
def test_compress():
    assert compress(
        'esto es una frase') == 'eJzT04rQ0NKwUiL0rEJTU32oKHAwELy1TEc1Q0NBQ0NIS0tLS0gNzEzMzI0NjAxM1gA'
    assert compress(
        'esto es una frase esto es una frase esto es una frase esto es una frase esto es una frase esto es una frase') == 'eJzT04rQ0NKwUiL0rEJTU32oKHAwELy1TEc1Q0NBQ0NIS0tLS0gNzEzMzI0NjAxM1gA'

# Generated at 2022-06-14 05:46:28.425081
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('') == 0
    assert roman_decode('I') == 1
    assert roman_decode('V') == 5
    assert roman_decode('X') == 10
    assert roman_decode('L') == 50
    assert roman_decode('C') == 100
    assert roman_decode('D') == 500
    assert roman_decode('M') == 1000
    assert roman_decode('MMMCMXCIX') == 3999



# Generated at 2022-06-14 05:46:41.457740
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('') == ''
    assert snake_case_to_camel('another_test') == 'AnotherTest'
    assert snake_case_to_camel('another_test', upper_case_first=False) == 'anotherTest'
    assert snake_case_to_camel('another_test', upper_case_first=False, separator='-') == 'another-test'
    assert snake_case_to_camel('another_test', upper_case_first=False, separator='-') == 'another-test'
    assert snake_case_to_camel('another_test', upper_case_first=False, separator='_') == 'anotherTest'

# Generated at 2022-06-14 05:46:48.929759
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'
    assert asciify('Stringa per test') == 'Stringa per test'

test_asciify()



# Generated at 2022-06-14 05:46:51.422075
# Unit test for function strip_margin
def test_strip_margin():
    assert strip_margin('''
                          line 1
                          line 2
                          line 3
                          '''.strip()) == '''
                          line 1
                          line 2
                          line 3
                          '''.strip()



# Generated at 2022-06-14 05:47:01.574158
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('  a  b  c  ').format() == 'A b c'
    assert __StringFormatter('  a  BC  c  ').format() == 'A BC c'
    assert __StringFormatter('  AA  BC  cc  ').format() == 'Aa bC cc'
    assert __StringFormatter('a b c').format() == 'A b c'
    assert __StringFormatter('A b c').format() == 'A b c'
    assert __StringFormatter('a B c').format() == 'A B c'
    assert __StringFormatter('A B c').format() == 'A B c'
    assert __StringFormatter('a b C').format() == 'A b C'
    assert __StringFormatter('A b C').format() == 'A b C'

# Generated at 2022-06-14 05:47:09.290924
# Unit test for function decompress
def test_decompress():
    assert decompress('eJxLTElQyE8tKc1PSyFVQUKMBSDFKTCxV1EiQjK5VLBGoGdlyUS8nIyEjIBiCVIpKjUzIB0kKbMfo1Bf') == "Welcome to the world of tomorrow"
    assert decompress('eJxLTU4sL8hKzs9OClVQQqwSsxS0wqVSRSITcqVSzGowZ2XEUtLydDQSAzJlU6KjUwIB8kKbMfo1Bf') == "The world of tomorrow"

# Generated at 2022-06-14 05:47:10.484711
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'


# Generated at 2022-06-14 05:47:16.095136
# Unit test for function shuffle
def test_shuffle():
    # we expect list(s) to contain the same number of chars of input string 's'
    def test_shuffle_invariant(s):
        assert len(s) == len(list(s))

    test_shuffle_invariant('1')
    test_shuffle_invariant('12')
    test_shuffle_invariant('123')
    test_shuffle_invariant('abcdefghilmnopqrstuvz')
    test_shuffle_invariant('abcdefghilmnopqrstuvz1234567890')
    test_shuffle_invariant('AAAAA')
    test_shuffle_invariant('BBBBBBBB')
    test_shuffle_invariant('CCCCCCCCCC')

# Generated at 2022-06-14 05:47:21.055845
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'



# Generated at 2022-06-14 05:47:34.364421
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'



# Generated at 2022-06-14 05:47:37.038165
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    string_compressor = __StringCompressor()
    assert string_compressor is not None

test___StringCompressor()


# PUBLIC API



# Generated at 2022-06-14 05:47:49.441282
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode(1) == 'I'
    assert roman_encode(4) == 'IV'
    assert roman_encode(5) == 'V'
    assert roman_encode(9) == 'IX'
    assert roman_encode(10) == 'X'
    assert roman_encode(40) == 'XL'
    assert roman_encode(50) == 'L'
    assert roman_encode(90) == 'XC'
    assert roman_encode(100) == 'C'
    assert roman_encode(400) == 'CD'
    assert roman_encode(500) == 'D'
    assert roman_encode(900) == 'CM'
    assert roman_encode(1000) == 'M'
    assert r

# Generated at 2022-06-14 05:47:52.741182
# Unit test for function reverse
def test_reverse():
    assert reverse('hello') == 'olleh'
    assert reverse('  hello') == 'olleh  '
    assert reverse(' hello ') == ' olleh '



# Generated at 2022-06-14 05:48:04.901685
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('thisisacamelstringtest') == 'thisisacamelstringtest'
    assert camel_case_to_snake('ThisIsACamelStringTest', '-') == 'this-is-a-camel-string-test'
    assert camel_case_to_snake('ThisIsACamelStringTest', '') == 'thisisacamelstringtest'
    assert camel_case_to_snake('ThisIsACamelStringTest', '+') == 'this+is+a+camel+string+test'



# Generated at 2022-06-14 05:48:08.394928
# Unit test for function booleanize
def test_booleanize():
    return (booleanize('true') == True and
    booleanize('YES') == True and
    booleanize('nope') == False)



# Generated at 2022-06-14 05:48:15.397125
# Unit test for function booleanize
def test_booleanize():
    import json
    try:
        with open('test.json', 'r') as json_file:
            json_dict = json.load(json_file)
        for k, v in json_dict.items():
           assert v == booleanize(k), 'For {}, expected {} but got {}'.format(k, v, booleanize(k))
    except AssertionError as e:
        print(e)
    else:
        print('All tests passed')

test_booleanize()

# Generated at 2022-06-14 05:48:20.555787
# Unit test for function slugify
def test_slugify():
    tests = [
        ['Top 10 Reasons To Love Dogs!!!', 'top-10-reasons-to-love-dogs'],
        ['Mönstér Mägnët', 'monster-magnet'],
        "!!A* ¿?¡!b_c.", 'a-b-c'
    ]

    for test in tests:
        assert slugify(test[0]) == test[1]