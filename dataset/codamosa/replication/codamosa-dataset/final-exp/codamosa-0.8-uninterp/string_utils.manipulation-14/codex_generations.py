

# Generated at 2022-06-14 05:39:00.132047
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:39:07.044023
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False, separator='-') == 'theSnakeIsGreen'

# Generated at 2022-06-14 05:39:18.965576
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter("test").format() == 'Test'
    assert __StringFormatter("testTest").format() == 'Testtest'
    assert __StringFormatter("test@test").format() == 'Test@test'
    assert __StringFormatter("test1.test2").format() == 'Test1.test2'
    assert __StringFormatter("test@test.com").format() == 'Test@test.com'
    assert __StringFormatter("test+test@test.test").format() == 'Test+test@test.test'
    assert __StringFormatter("test+test@test.test.test.test").format() == 'Test+test@test.test.test.test'
    assert __StringFormatter("test.test").format() == 'Test.test'

# Generated at 2022-06-14 05:39:22.958108
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('tHiS Text IS Always writteN iN lower case').format() == 'This text is always written in lower case'
    assert __StringFormatter('tHiS Text IS Always writteN iN lower case, and with some duplicates charaters').format() == 'This text is always written in lower case, and with some duplicates characters'
    assert __StringFormatter('This text.Is very good,And has no internal spaces').format() == 'This text. Is very good, And has no internal spaces'
    assert __StringFormatter('This text has missing spaces around symbols').format() == 'This text has missing spaces around symbols'
    assert __StringFormatter('This text.has.too many.spaces').format() == 'This text. Has. Too many. Spaces'

# Generated at 2022-06-14 05:39:29.398658
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # 1. PRETTIFY_RE['UPPERCASE_FIRST_LETTER']
    assert __StringFormatter('this is a test').format() == 'This is a test'
    assert __StringFormatter('This is a test').format() == 'This is a test'
    # 2. PRETTIFY_RE['DUPLICATES']
    assert __StringFormatter('this is a --- test').format() == 'This is a - test'
    assert __StringFormatter('this is a - test').format() == 'This is a - test'
    # 3. PRETTIFY_RE['RIGHT_SPACE']
    assert __StringFormatter('this is a   test').format() == 'This is a test'
    assert __StringFormatter('this is a test').format() == 'This is a test'
    # 4.

# Generated at 2022-06-14 05:39:34.943366
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('hello') == 'hello'
    assert snake_case_to_camel('Hello') == 'Hello'
    assert snake_case_to_camel('HELLO') == 'HELLO'
    assert snake_case_to_camel(' h  e  l  l  o  ') == ' h  e  l  l  o  '
    assert snake_case_to_camel(' h  e  l  l  o') == ' h  e  l  l  o'
    assert snake_case_to_camel(' h  e  l  l  o  ') == ' h  e  l  l  o  '
    assert snake_case_to_camel('Hello  ,  world') == 'Hello  ,  world'
    assert snake_case_to

# Generated at 2022-06-14 05:39:49.524319
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    out = __StringFormatter('  Ciao   come   stai  ? ').format()
    assert out == 'Ciao come stai?'

    out = __StringFormatter('Hello  I\'m   Andrea  ').format()
    assert out == "Hello I'm Andrea"

    out = __StringFormatter('Hello  I\'m   Andrea  ,  I  am  27    years   old    ,   I  am    an  italian     guy  ').format()
    assert out == 'Hello I\'m Andrea, I am 27 years old, I am an italian guy'

    out = __StringFormatter('Hello   !!!  ').format()
    assert out == 'Hello !!!'

    out = __StringFormatter('  Hello   !!!  ').format()
    assert out == 'Hello !!!'

    out = __

# Generated at 2022-06-14 05:40:00.409684
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('camel_to_snake_case_string', upper_case_first=True) == 'CamelToSnakeCaseString'
    assert snake_case_to_camel('camel_to_snake_case_string', upper_case_first=False) == 'camelToSnakeCaseString'
    assert snake_case_to_camel('camel_to_snake_case_string', upper_case_first=False, separator='-') == \
           'camelToSnakeCaseString'
    assert snake_case_to_camel('camelToSnakeCaseString') == 'CamelToSnakeCaseString'



# Generated at 2022-06-14 05:40:13.504438
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    def _test(input_string, expected):
        actual = __StringFormatter(input_string).format()
        assert actual == expected, 'Failed for %s, expected "%s" got "%s"' % (input_string, expected, actual)

    # input string must not be empty
    with pytest.raises(ValueError):
        _test('', '')

    _test(
        '\t hello, world!  ',
        'Hello, world!'
    )
    _test(
        '\t hello, world!  .  ',
        'Hello, world!'
    )
    _test(
        '\t hello, world!  .\n\t how are you?  ',
        'Hello, world! How are you?'
    )

# Generated at 2022-06-14 05:40:18.741718
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    print(__StringFormatter('This  is  a test!').format())
    print(__StringFormatter('‘It’s already a success,’ says former student').format())
    print(__StringFormatter('Let us pretend we aren’t sons of bitches').format())
    print(__StringFormatter('...And so,').format())
    print(__StringFormatter('The U.S. is a big place.').format())


# GLOBAL API

# strings


# Generated at 2022-06-14 05:40:25.630884
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('test_test_test') == 'testTestTest'
    assert snake_case_to_camel('test_test_test', upper_case_first = False) == 'testTestTest'
    assert snake_case_to_camel('test_test_test', separator = '-') == 'testTestTest'



# Generated at 2022-06-14 05:40:36.787494
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', True, '-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False, '-') == 'theSnakeIsGreen'
    assert snake_case_to_camel('the snake is green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the snake is green', True, '-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the snake is green', False, '-') == 'theSnakeIsGreen'
    assert snake_case_to_camel('TheSnakeIsGreen') == 'TheSnakeIsGreen'

# Generated at 2022-06-14 05:40:42.563020
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel(): #TODO da fare
    snake_cases = [
        'this_is_a_snake_case_string',
        'this_is_a_snake_case_string_with_numbers123',
        '_this_is_another_snake_case_string_with_numbers123_',
        '_this_is_another_snake_case_string_with_numbers123_',
        'this_is_another_snake_case_string_with_numbers123_'
    ]
    for snakecase in snake_cases:
        camelcase = snake_case_to_camel(snakecase)
        print('Snake case: ' + snakecase)
        print('Camel case: ' + camelcase)
        assert is_camel_case(camelcase)

# Generated at 2022-06-14 05:40:52.339764
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    formatter = __StringFormatter('-foo bar-')
    assert formatter.format() == 'Foo bar'

    formatter = __StringFormatter('-foo bar')
    assert formatter.format() == 'Foo bar'

    formatter = __StringFormatter('foo bar-')
    assert formatter.format() == 'Foo bar'

    formatter = __StringFormatter('foo bar')
    assert formatter.format() == 'Foo bar'

    formatter = __StringFormatter('Foo bar')
    assert formatter.format() == 'Foo bar'

    formatter = __StringFormatter('foo bar baz')
    assert formatter.format() == 'Foo bar baz'

    formatter = __StringFormatter('foo- bar- baz-')

# Generated at 2022-06-14 05:40:58.675756
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'



# Generated at 2022-06-14 05:41:08.974518
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    input_string = 'Company  Name'
    expected = 'Company Name'
    actual = __StringFormatter(input_string).format()
    assert actual == expected

    input_string = 'Company Name, Inc.'
    expected = 'Company Name, Inc.'
    actual = __StringFormatter(input_string).format()
    assert actual == expected

    input_string = 'Company Name, Inc. / Example.org'
    expected = 'Company Name, Inc. / Example.org'
    actual = __StringFormatter(input_string).format()
    assert actual == expected

    input_string = 'Company Name, Inc. / Example.org'
    expected = 'Company Name, Inc. / Example.org'
    actual = __StringFormatter(input_string).format()
    assert actual == expected


# Generated at 2022-06-14 05:41:20.574413
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert 'HelloWorld' == snake_case_to_camel('hello_world')
    assert 'HelloWorld' == snake_case_to_camel('hello_world', separator='-')
    assert 'helloWorld' == snake_case_to_camel('hello_world', upper_case_first=False)
    assert 'helloWorld' == snake_case_to_camel('hello_world', upper_case_first=False, separator='-')
    assert 'helloWorld' == snake_case_to_camel('hello_world', separator='_', upper_case_first=False)
    assert 'snakeHelloIsGreen' == snake_case_to_camel('snake_hello_is_green', separator='_', upper_case_first=False)
    assert 'snakeHelloIsGreen' == snake_case

# Generated at 2022-06-14 05:41:28.062051
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'



# Generated at 2022-06-14 05:41:34.255973
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'the-snake-is-green'



# Generated at 2022-06-14 05:41:44.804026
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    sf = __StringFormatter('this is a test to check if it works')
    assert sf.format() == 'This is a test to check if it works'

    sf = __StringFormatter('this is a test to check if it works   ')
    assert sf.format() == 'This is a test to check if it works'

    sf = __StringFormatter('  this is a test to check if it works')
    assert sf.format() == 'This is a test to check if it works'

    sf = __StringFormatter('  this is a test to check if it works   ')
    assert sf.format() == 'This is a test to check if it works'

    sf = __StringFormatter('  this is a test    to check if it works   ')

# Generated at 2022-06-14 05:41:53.762479
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('hello') == 'Hello'
    assert snake_case_to_camel('hello_world') == 'HelloWorld'
    
# Function snake_case_to_camel for review

# Generated at 2022-06-14 05:42:02.219592
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('this_is_a_test') == 'ThisIsATest'
    assert snake_case_to_camel('this_is_a_test', True, '-') == 'ThisIsATest'
    assert snake_case_to_camel('this-is-a-test', True, '-') == 'ThisIsATest'
    assert snake_case_to_camel('this_is_a_test', False) == 'thisIsATest'
    assert snake_case_to_camel('this_is_a_test', False, '-') == 'thisIsATest'
    assert snake_case_to_camel('this-is-a-test', False, '-') == 'thisIsATest'


# Generated at 2022-06-14 05:42:11.729619
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', separator='-', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake', upper_case_first=False) == 'theSnake'
    assert snake_case_to_camel('a') == 'A'

# Generated at 2022-06-14 05:42:19.104551
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('snake_case') == 'SnakeCase'
    assert snake_case_to_camel('snake_case', upper_case_first=False) == 'snakeCase'
    assert snake_case_to_camel('snake_case', separator='-') == 'SnakeCase'
    assert snake_case_to_camel('snake_case', separator='-', upper_case_first=False) == 'snakeCase'



# Generated at 2022-06-14 05:42:22.384301
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    val_test = snake_case_to_camel('the_snake_is_green')
    assert val_test == 'TheSnakeIsGreen'
    print(val_test)



# Generated at 2022-06-14 05:42:26.756816
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    in_s = "the_snake_is_green"
    assert snake_case_to_camel(in_s) == "TheSnakeIsGreen"


# Generated at 2022-06-14 05:42:36.557107
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'The-Snake-Is-Green'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False, separator='-') == 'the-Snake-Is-Green'



# Generated at 2022-06-14 05:42:48.107135
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('theSnakeIsGreen') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('theSnakeIsGreen', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the:snake:is:green', separator=':') == 'TheSnakeIsGreen'

# Generated at 2022-06-14 05:42:58.265655
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('thi_is_not_a_snake_case_string') == 'Thi_is_not_a_snake_case_string'



# Generated at 2022-06-14 05:43:07.869329
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    input_string="this_is_a_camel_case_string_test"
    assert snake_case_to_camel(input_string)=="ThisIsACamelCaseStringTest"
    input_string="this_is_a_camel_case_string_test_with_lower_case_first_letter"
    assert snake_case_to_camel(input_string,upper_case_first=False)=="thisIsACamelCaseStringTestWithLowerCaseFirstLetter"


# Generated at 2022-06-14 05:43:12.889857
# Unit test for function shuffle
def test_shuffle():
    string = 'abcdefgh'
    out = shuffle(string)
    print('In: "{}" Out:"{}"'.format(string, out))



# Generated at 2022-06-14 05:43:15.730145
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '



# Generated at 2022-06-14 05:43:28.375111
# Unit test for function asciify

# Generated at 2022-06-14 05:43:35.615567
# Unit test for function prettify

# Generated at 2022-06-14 05:43:47.626132
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    assert __StringFormatter
    assert __StringFormatter('test')
    assert __StringFormatter('test').input_string == 'test'
    assert __StringFormatter('test').__uppercase_first_char
    assert __StringFormatter('test').__remove_duplicates
    assert __StringFormatter('test').__uppercase_first_letter_after_sign
    assert __StringFormatter('test').__ensure_right_space_only
    assert __StringFormatter('test').__ensure_left_space_only
    assert __StringFormatter('test').__ensure_spaces_around
    assert __StringFormatter('test').__remove_internal_spaces
    assert __StringFormatter('test').__fix_saxon_genitive

test___StringFormatter()


# PUBLIC API



# Generated at 2022-06-14 05:43:56.763961
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    class TestObject:
        def __init__(self):
            pass

    # invalid input: not a string
    try:
        __StringFormatter(TestObject())
        assert False, 'Expected InvalidInputError'
    except InvalidInputError:
        pass

    # valid input
    try:
        __StringFormatter('Some text to be formattet')
        assert True
    except InvalidInputError:
        assert False, 'Expected valid input string'


# Generated at 2022-06-14 05:44:03.426430
# Unit test for function decompress
def test_decompress():
    test1 = "test1"
    test2 = "тест2"
    test3 = "テスト3"

    # case1
    assert test1 == decompress(compress(test1))

    # case2
    assert test2 == decompress(compress(test2))

    # case3
    assert test3 == decompress(compress(test3))


# Generated at 2022-06-14 05:44:14.370420
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    test_input = """
    Hello,
    my name is Michele.
    I live in New York    (  U.S.A.  )
    and I am a developer.

    I am interesting in many things about   computers, such as
    - php
    - python
    - java
    - c#

    I have a blog @ http://www.michele.orlando.it
    and an email account: michele@protomail.com

    If you want to contact me my phone number is 555-123456.

    Thanks a lot
    """


# Generated at 2022-06-14 05:44:19.347809
# Unit test for function shuffle
def test_shuffle():
    assert shuffle('abc') == 'abc'
    assert shuffle('abc') != 'abc'
    assert shuffle('') == ''
    assert shuffle('hello world') != 'hello world'
    assert shuffle('hello world') == 'hello world'
    print('Test for function shuffle passed!')

test_shuffle()


# Generated at 2022-06-14 05:44:22.439855
# Unit test for function asciify
def test_asciify():
    a = asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË')
    assert a == 'eeuuooaaeynAAACIINOE'
    print("Test passed")
test_asciify()


# Generated at 2022-06-14 05:44:28.967786
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode(1) == 'I'
    assert roman_encode(2) == 'II'
    assert roman_encode(3) == 'III'
    assert roman_encode(4) == 'IV'
    assert roman_encode(5) == 'V'
    assert roman_encode(7) == 'VII'
    assert roman_encode(9) == 'IX'
    assert roman_encode(10) == 'X'
    assert roman_encode(11) == 'XI'
    assert roman_encode(13) == 'XIII'
    assert roman_encode(14) == 'XIV'
    assert roman_encode(15) == 'XV'
    assert roman_encode(16) == 'XVI'

# Generated at 2022-06-14 05:44:32.419540
# Unit test for function shuffle
def test_shuffle():
    assert shuffle('hello world') != 'hello world'
    assert ''.join(sorted(shuffle('hello world'))) == ' ' + ''.join(sorted('hello world'))



# Generated at 2022-06-14 05:44:34.835854
# Unit test for function slugify
def test_slugify():
    assert slugify('Top 10 Reasons to Love Dogs') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'



# Generated at 2022-06-14 05:44:39.916400
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') == True
    assert booleanize('1') == True
    assert booleanize('yes') == True
    assert booleanize('y') == True

# Run unit test
test_booleanize()

# Generated at 2022-06-14 05:44:43.021663
# Unit test for function reverse
def test_reverse():
    assert reverse('hello') == 'olleh'



# Generated at 2022-06-14 05:44:54.548766
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'
    assert strip_html('<a href="foo/bar">click here</a>', keep_tag_content=True) == 'click here'
    assert strip_html('<a href="foo/bar">click here</a>', keep_tag_content=False) == ''
    assert strip_html('<a href="foo/bar">click\'here</a>', keep_tag_content=False) == ''
    assert strip_html('<a href=\'foo/bar\'>click here</a>', keep_tag_content=False) == ''
    assert strip

# Generated at 2022-06-14 05:45:05.162823
# Unit test for function compress
def test_compress():
    """
    Unit test for StringUtils.compress

    :return: void
    """
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    assert(compressed == 'eNqzc8JwFDDgAOJ/DMMDFxvx8XAjBcwsRgYGCIwGBwYB4yMHM0sDAqCqAJ5FbSXn5YawABgQQtCg==')



# Generated at 2022-06-14 05:45:10.809425
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('camel_case') == 'CamelCase'
    assert snake_case_to_camel('camel_case', upper_case_first=False) == 'camelCase'
    assert snake_case_to_camel('camelCase') == 'CamelCase'
    assert snake_case_to_camel('camelCase', upper_case_first=False) == 'camelCase'



# Generated at 2022-06-14 05:45:15.080688
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('ThisIsACamelStringTest', '-') == 'this-is-a-camel-string-test'



# Generated at 2022-06-14 05:45:23.427522
# Unit test for function strip_margin
def test_strip_margin():
  assert strip_margin("""    line 1
                          line 2
                          line 3""") == """line 1
line 2
line 3"""
  assert strip_margin("""      line 1
                            line 2
                            line 3""") == """  line 1
  line 2
  line 3"""
  assert strip_margin("""line 1
                         line 2
                         line 3""") == """line 1
line 2
line 3"""

test_strip_margin()


# Generated at 2022-06-14 05:45:37.297120
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:45:39.046189
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    s = __StringFormatter('Hello world !')


# Generated at 2022-06-14 05:45:43.700445
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'



# Generated at 2022-06-14 05:45:46.920356
# Unit test for function asciify
def test_asciify():
    return asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË')
test_asciify()


# Generated at 2022-06-14 05:45:49.612718
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') == True
    assert booleanize('true') == True
    assert booleanize('false') == False
    assert booleanize('False') == False
    assert booleanize('TRUE') == True
    assert booleanize('FALSE') == False
    try:
        print(booleanize(10))
        assert False
    except InvalidInputError:
        assert True
    except:
        assert False

test_booleanize()


# Generated at 2022-06-14 05:45:53.841159
# Unit test for function slugify
def test_slugify():
    assert 'top-10-reasons-to-love-dogs' == slugify('Top 10 Reasons To Love Dogs!!!')
    assert 'monster-magnet' == slugify('Mönstér Mägnët')

test_slugify()



# Generated at 2022-06-14 05:45:54.862695
# Unit test for function roman_encode
def test_roman_encode():
    assert is_string(roman_encode('2019'))
    assert roman_encode(2019) == 'MMXIX'
    return True


# Generated at 2022-06-14 05:46:03.471246
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    from unittest import TestCase

    class __Test___StringCompressor(TestCase):

        def test_constructor_raises_exception_when_input_string_is_invalid(self):
            self.assertRaises(InvalidInputError, lambda: __StringCompressor(dict(), 'utf-8'))

        def test_constructor_raises_exception_when_input_string_is_empty(self):
            self.assertRaises(ValueError, lambda: __StringCompressor('', 'utf-8'))

        def test_constructor_raises_exception_when_encoding_is_invalid(self):
            self.assertRaises(ValueError, lambda: __StringCompressor('abc', 1024))


# Generated at 2022-06-14 05:46:16.698579
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Vehicula ipsum a arcu cursus vitae congue mauris. Facilisis gravida neque convallis a cras. Sit amet facilisis magna etiam tempor orci eu lobortis. Ut morbi tincidunt augue interdum. Ce eu nisl nunc mi. Id porta nibh venenatis'
    compressedString = __StringCompressor.compress(string, "utf-8", 9)

    assert compressedString is not None
    assert len(compressedString) > 0

    decompressedString = __StringCompressor.decompress(compressedString, "utf-8")



# Generated at 2022-06-14 05:46:20.462059
# Unit test for function asciify
def test_asciify():
    assert asciify("èéùúòóäåëýñÅÀÁÇÌÍÑÓË") == "eeuuooaaeynAAACIINOE"


# Generated at 2022-06-14 05:46:37.388065
# Unit test for function roman_decode
def test_roman_decode():
    assert(roman_decode("VII")==7)
    assert(roman_decode("VI")==6)
    assert(roman_decode("V")==5)
    assert(roman_decode("IV")==4)
    assert(roman_decode("III")==3)
    assert(roman_decode("II")==2)
    assert(roman_decode("I")==1)
test_roman_decode()



# Generated at 2022-06-14 05:46:51.121749
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.encode(1) == 'I'
    assert __RomanNumbers.encode(5) == 'V'
    assert __RomanNumbers.encode(10) == 'X'
    assert __RomanNumbers.encode(50) == 'L'
    assert __RomanNumbers.encode(100) == 'C'
    assert __RomanNumbers.encode(500) == 'D'
    assert __RomanNumbers.encode(1000) == 'M'
    assert __RomanNumbers.encode(3) == 'III'
    assert __RomanNumbers.encode(4) == 'IV'
    assert __RomanNumbers.encode(6) == 'VI'
    assert __RomanNumbers.encode(7) == 'VII'
    assert __RomanNumbers.encode(8) == 'VIII'

# Generated at 2022-06-14 05:46:56.309294
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_case_string_test'
    assert camel_case_to_snake('ThisIsACamelStringTest', '-') == 'this-is-a-camel-case-string-test'



# Generated at 2022-06-14 05:47:03.709217
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
    assert __RomanNumbers.encode(50) == 'L'
    assert __RomanNumbers.encode(100) == 'C'

# Generated at 2022-06-14 05:47:05.960820
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('VII') == 7
    assert roman_decode('Iv') == 4


# Generated at 2022-06-14 05:47:11.800677
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode(0) == '0'
    assert roman_encode('2020') == 'MMXX'
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode(-37) == '-XXXVII'
    assert roman_encode(4000) == 'MMMMCMXCIX'

test_roman_encode()


# Generated at 2022-06-14 05:47:25.653848
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.encode(1) == 'I'
    assert __RomanNumbers.encode(2) == 'II'
    assert __RomanNumbers.encode(3) == 'III'
    assert __RomanNumbers.encode(4) == 'IV'
    assert __RomanNumbers.encode(5) == 'V'
    assert __RomanNumbers.encode(9) == 'IX'
    assert __RomanNumbers.encode(10) == 'X'
    assert __RomanNumbers.encode(40) == 'XL'
    assert __RomanNumbers.encode(50) == 'L'
    assert __RomanNumbers.encode(90) == 'XC'
    assert __RomanNumbers.encode(100) == 'C'
    assert __RomanNumbers.encode(400) == 'CD'

# Generated at 2022-06-14 05:47:26.750185
# Unit test for function compress
def test_compress():
    compress('test_string')

# Generated at 2022-06-14 05:47:31.969844
# Unit test for function compress
def test_compress():
    # string to compress
    s = ' '.join(['word {}'.format(n) for n in range(20)])
    # compressed string
    cs = compress(s)
    # the compressed string must be shorter than the original one
    assert len(s) > len(cs)
    # the original string must be restored by using the original string
    assert decompress(cs) == s

# Generated at 2022-06-14 05:47:36.921976
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    assert __StringFormatter('test')
    assert not __StringFormatter('')
    assert not __StringFormatter(1)
    try:
        __StringFormatter(None)
        assert False
    except InvalidInputError:
        assert True

test___StringFormatter()



# Generated at 2022-06-14 05:48:03.223296
# Unit test for function roman_decode
def test_roman_decode():
    assert(roman_decode('VII') == 7)
    assert(roman_decode('VIII') == 8)
    assert(roman_decode('IX') == 9)
    assert(roman_decode('X') == 10)
    assert(roman_decode('XI') == 11)
    assert(roman_decode('XII') == 12)
    assert(roman_decode('XIII') == 13)
    assert(roman_decode('XIV') == 14)
    assert(roman_decode('XV') == 15)
    assert(roman_decode('XVI') == 16)
    assert(roman_decode('XVII') == 17)
    assert(roman_decode('XVIII') == 18)
    assert(roman_decode('XIX') == 19)

# Generated at 2022-06-14 05:48:14.592687
# Unit test for function prettify
def test_prettify():
    assert prettify('hello world') == 'Hello world'
    assert prettify('hello     world') == 'Hello world'
    assert prettify('hello world ') == 'Hello world'
    assert prettify(' hello world ') == 'Hello world'
    assert prettify('hello, world!') == 'Hello, world!'
    assert prettify('hello,world!') == 'Hello, world!'
    assert prettify('hello,world !') == 'Hello, world!'
    assert prettify('foo + bar - baz / qux * qux = test') == 'foo + bar - baz / qux * qux = test'
    assert prettify('foo+ bar- baz/ qux* qux= test') == 'Foo + bar - baz / qux * qux = test'

# Generated at 2022-06-14 05:48:24.155032
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('') == ''
    assert snake_case_to_camel('snake') == 'Snake'
    assert snake_case_to_camel('snake_case') == 'SnakeCase'
    assert snake_case_to_camel('snake_case', upper_case_first=False) == 'snakeCase'
    assert snake_case_to_camel('this_is_a_complex_snake_case') == 'ThisIsAComplexSnakeCase'
    assert snake_case_to_camel('this_is_a_complex_snake_case', upper_case_first=False) == 'thisIsAComplexSnakeCase'

# Generated at 2022-06-14 05:48:28.777650
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode("II") == 2
    assert roman_decode("XX") == 20
    assert roman_decode("XIX") == 19
    assert roman_decode("iv") == 4
    assert roman_decode("xix") == 19

