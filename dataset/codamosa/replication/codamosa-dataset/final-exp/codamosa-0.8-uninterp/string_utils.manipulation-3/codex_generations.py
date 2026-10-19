

# Generated at 2022-06-14 05:38:58.937924
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    formatter = __StringFormatter('one two three')
    assert formatter.format() == 'One two three'

    formatter = __StringFormatter('this is a test')
    assert formatter.format() == 'This is a test'

    formatter = __StringFormatter('  this  is  a test  ')
    assert formatter.format() == 'This is a test'

    formatter = __StringFormatter('  This   is   a test  ')
    assert formatter.format() == 'This is a test'

    formatter = __StringFormatter('  This  is  a  test  ')
    assert formatter.format() == 'This is a test'

    formatter = __StringFormatter('one two three four five')
    assert formatter.format() == 'One two three four five'

    formatter

# Generated at 2022-06-14 05:39:02.372514
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    s = __StringFormatter('Lorem ipsum Dolor sit Amet, consectetur adipisicing elit.')
    assert s.format() == 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'



# Generated at 2022-06-14 05:39:09.825303
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('hello_world') == 'HelloWorld'
    assert snake_case_to_camel('hello_world', True, '_') == 'HelloWorld'
    assert snake_case_to_camel('hello_world', False, '_') == 'helloWorld'
    assert snake_case_to_camel('hello_world', True, '-') == 'HelloWorld'
    assert snake_case_to_camel('hello-world', True, '-') == 'HelloWorld'



# Generated at 2022-06-14 05:39:22.766279
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    f = __StringFormatter('foo bar')
    assert f.format() == 'Foo bar'

    f = __StringFormatter(' foo bar ')
    assert f.format() == 'Foo bar'

    f = __StringFormatter('foo bar  ')
    assert f.format() == 'Foo bar'

    f = __StringFormatter('   foo bar')
    assert f.format() == 'Foo bar'

    f = __StringFormatter('Foo Bar')
    assert f.format() == 'Foo bar'

    f = __StringFormatter('Foo Bar ')
    assert f.format() == 'Foo bar'

    f = __StringFormatter('foo Bar')
    assert f.format() == 'Foo bar'

    f = __StringFormatter('FooBar  ')

# Generated at 2022-06-14 05:39:32.083876
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('hello world').format() == 'Hello World'
    assert __StringFormatter('hello  world  ').format() == 'Hello World'
    assert __StringFormatter('Hello world').format() == 'Hello World'
    assert __StringFormatter('  Hello world  ').format() == 'Hello World'
    assert __StringFormatter('helloWorld').format() == 'Hello World'
    assert __StringFormatter('helloWorld.com').format() == 'Hello World.com'
    assert __StringFormatter('hello_world').format() == 'Hello World'
    assert __StringFormatter('https://www.helloWorld.com').format() == 'https://www.helloWorld.com'
    assert __StringFormatter('hello\'s world').format() == 'Hello\'s World'

# Generated at 2022-06-14 05:39:36.655726
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:39:49.852266
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert (__StringFormatter('abcde').format() == 'abcde')
    assert (__StringFormatter('abcde fg').format() == 'abcde fg')
    assert (__StringFormatter('Abcde fg').format() == 'Abcde fg')
    assert (__StringFormatter('A a').format() == 'A a')
    assert (__StringFormatter('A a.').format() == 'A a.')
    assert (__StringFormatter('A a      g').format() == 'A a g')
    assert (__StringFormatter('A a. g').format() == 'A a. g')
    assert (__StringFormatter('A a.   g').format() == 'A a. g')

# Generated at 2022-06-14 05:40:02.525362
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    sf = __StringFormatter('a b c d e f')
    assert sf.format() == 'A b c d e f'

    sf.input_string = 'a b c d e f a'
    assert sf.format() == 'A b c d e f a'

    sf.input_string = 'a b c d   e f'
    assert sf.format() == 'A b c d e f'

    sf.input_string = 'a b c d e f https://www.google.it/mail@mail.it'
    assert sf.format() == 'A b c d e f https://www.google.it/mail@mail.it'

    sf.input_string = 'dopo il punto prova'

# Generated at 2022-06-14 05:40:15.146376
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    test_string = "  hello, world...  This is a text  with a lot of   spaces    and strange   characters! \t\n\t"
    # check if the result string is the expected one
    assert __StringFormatter(test_string).format() == "Hello, world... This is a text with a lot of spaces and strange characters!"


# PUBLIC API

# Transforms a camelCase string into a snake_case string.
camel_case_to_snake = lambda s: SNAKE_RE.sub(r'\1_\2', s).lower()
if __name__ == '__main__':
    # Unit test for function camel_case_to_snake
    assert camel_case_to_snake("thisIsAString") == "this_is_a_string"

# Transforms a snake_case string

# Generated at 2022-06-14 05:40:18.912000
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    print('Test for function snake_case_to_camel passed successfully')
    return True



# Generated at 2022-06-14 05:40:26.058377
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    input_str = 'hello,    world!   ùàòèéì...-.,;è_*^ç^àòè_ààà'

    expected_output = 'Hello, world! ùàòèéì... -.,;è_*^ç^àòè_ààà'
    instance = __StringFormatter(input_str)
    assert instance.format() == expected_output



# Generated at 2022-06-14 05:40:37.015685
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=True) == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'

    assert snake_case_to_camel('THE_SNAKE_IS_GREEN', upper_case_first=True) == 'THESnakeIsGreen'
    assert snake_case_to_camel('THE_SNAKE_IS_GREEN', upper_case_first=False) == 'thESnakeIsGreen'

    assert snake_case_to_camel('theSnakeIsGreen', upper_case_first=True) == 'theSnakeIsGreen'

# Generated at 2022-06-14 05:40:50.376135
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False, '#') == 'theSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', False, '-') == 'theSnakeIsGreen'
    assert snake_case_to_camel('the#snake#is#green', False, '#') == 'theSnakeIsGreen'
    assert snake_case_to_camel('this string is not a snake case string') == 'ThisStringIsNotASnakeCaseString'



# Generated at 2022-06-14 05:41:02.043519
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    expected_string = 'TheSnakeIsGreen'
    actual_string = snake_case_to_camel('the_snake_is_green')
    assert expected_string == actual_string
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('this_is_a_snake_case_string') == 'ThisIsASnakeCaseString'
    assert snake_case_to_camel('this_is_a_snake_case_string', upper_case_first=False) == 'thisIsASnakeCaseString'
    assert snake_case_to_camel('this-is-a-snake-case-string', separator='-') == 'ThisIsASnakeCaseString'
    assert snake_case_to

# Generated at 2022-06-14 05:41:16.947217
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('one two three   four-five  -six-seven-eight-nine').format() == 'one two three four-five -six-seven-eight-nine'
    assert __StringFormatter('one TWO three  FOUR-five  -six-seven-eight-nine').format() == 'One two three four-five -six-seven-eight-nine'
    assert __StringFormatter('one two Three  FOUR-five  -six-seven-eight-nine').format() == 'One two three four-five -six-seven-eight-nine'
    assert __StringFormatter('one two three  FOUR-five  -six-seven-eight-nine').format() == 'One two three four-five -six-seven-eight-nine'

# Generated at 2022-06-14 05:41:27.843093
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('this_is_not_a_snake_string') == 'thisIsNotASnakeString'
    assert snake_case_to_camel('IsNotASnakeString') == 'isNotASnakeString'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('this_is_not_a_snake_string', False) == 'thisIsNotASnakeString'
    assert snake_case_to_camel('IsNotASnakeString', False) == 'isNotASnakeString'

# Generated at 2022-06-14 05:41:40.840279
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('test') == 'test'
    assert snake_case_to_camel('test_invalid') == 'test_invalid'
    assert snake_case_to_camel('test_invalid', True) == 'test_invalid'
    assert snake_case_to_camel('test-invalid') == 'test-invalid'
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', False) == 'theSnakeIsGreen'

# Generated at 2022-06-14 05:41:53.973889
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert 'theSnakeIsGreen' == snake_case_to_camel('the_snake_is_green', upper_case_first=False)
    assert 'TheSnakeIsGreen' == snake_case_to_camel('the_snake_is_green', upper_case_first=True)
    assert 'ThisSnakeIsGreen' == snake_case_to_camel('_this_snake_is_green', upper_case_first=True)
    assert 'thisSnakeIsGreen' == snake_case_to_camel('_this_snake_is_green', upper_case_first=False)
    assert 'thisSnakeIsGreen' == snake_case_to_camel('this snake is green', upper_case_first=False, separator=' ')
    assert 'thisSnakeIsGreen' == snake_case_to_c

# Generated at 2022-06-14 05:42:00.683585
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'The-Snake-Is-Green'



# Generated at 2022-06-14 05:42:10.884387
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='.') == 'The.Snake.Is.Green'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False, separator='.') == 'the.Snake.Is.Green'
    assert snake_case_to_camel('this_is_a_snake_case_string_test') == 'ThisIsASnakeCaseStringTest'

# Generated at 2022-06-14 05:42:23.407003
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:42:36.437132
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    from .validation import assert_equals

    sf = __StringFormatter('a bbb c  dddd    eee f  gggg  hhhh')
    output = sf.format()
    assert_equals(output, 'A Bbb C Dddd Eee F Gggg Hhhh')

    sf = __StringFormatter('A Bbb C  Dddd    Eee F  Gggg  Hhhh')
    output = sf.format()
    assert_equals(output, 'A Bbb C Dddd Eee F Gggg Hhhh')

    sf = __StringFormatter('')
    output = sf.format()
    assert_equals(output, '')

    sf = __StringFormatter('a')
    output = sf.format()
    assert_equals

# Generated at 2022-06-14 05:42:48.027138
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    def assert_format(input_string, expected_output):
        instance = __StringFormatter(input_string)
        assert expected_output == instance.format()

    # --- test cases ---
    assert_format("hello world", "Hello world")
    assert_format("hello-world", "Hello world")
    assert_format("helloWorld", "Hello world")
    assert_format('hello_world', 'Hello world')
    assert_format("hello world!", "Hello world!")
    assert_format("hello world?", "Hello world?")
    assert_format("hello world!!", "Hello world!!")
    assert_format("hello world?", "Hello world?")
    assert_format("hello world...", "Hello world...")
    assert_format("hello world?!", "Hello world?!")

# Generated at 2022-06-14 05:43:00.653159
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():

    # test that formatter does not perform any operation on invalid inputs
    try:
        __StringFormatter(None).format()
        raise AssertionError()
    except InvalidInputError:
        pass

    try:
        __StringFormatter('').format()
        raise AssertionError()
    except InvalidInputError:
        pass

    try:
        __StringFormatter('   ').format()
        raise AssertionError()
    except InvalidInputError:
        pass

    try:
        __StringFormatter(1).format()
        raise AssertionError()
    except InvalidInputError:
        pass

    # test that urls and emails are not modified while other string gets prettified
    assert __StringFormatter('test@test.it').format() == 'test@test.it'

# Generated at 2022-06-14 05:43:06.385115
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('a very long string').format() == 'A very long string'
    assert __StringFormatter('a very very long string').format() == 'A very long string'
    assert __StringFormatter('a very long string.').format() == 'A very long string'
    assert __StringFormatter('a very long string   ').format() == 'A very long string'
    assert __StringFormatter(' a very long string   ').format() == 'A very long string'
    assert __StringFormatter('a very long string  ,').format() == 'A very long string'



# Generated at 2022-06-14 05:43:09.074724
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    formatter = __StringFormatter('   hello world \r\n')
    assert formatter.format() == 'Hello World'

# Generated at 2022-06-14 05:43:19.918924
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:43:30.960855
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('sEcOnds').format() == 'Seconds'
    assert __StringFormatter('pErMiTs').format() == 'Permits'
    assert __StringFormatter('mOnEy').format() == 'Money'
    assert __StringFormatter('mUlTIPLe').format() == 'Multiple'
    assert __StringFormatter('cRItIcal').format() == 'Critical'
    assert __StringFormatter('tRaNsActiOn').format() == 'Transaction'
    assert __StringFormatter('vARiablEs').format() == 'Variables'

    assert __StringFormatter('pErMiTs pErMiTs').format() == 'Permits Permits'
    assert __StringFormatter('mOnEy mOnEy').format() == 'Money Money'

# Generated at 2022-06-14 05:43:44.966664
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('I Wanna  BE  YOUR            dog ').format() == 'I wanna be your dog'
    assert __StringFormatter('   BABY    (     I WANT TO BE YOUR  dog)  ').format() == 'Baby (I want to be your dog)'
    assert __StringFormatter('  "     ( I  want  to  be your  DOG)  ').format() == '"(I want to be your dog)'
    assert __StringFormatter('  --   I wanna  -  be  your  dog;  ').format() == '-- I wanna - be your dog;'
    assert __StringFormatter('  --   I wanna  -  be  your  dog\'s  ').format() == '-- I wanna - be your dog\'s'

# Generated at 2022-06-14 05:43:56.869205
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:44:13.391168
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    formatter = __StringFormatter('  hello world      world  !')
    assert formatter.format() == 'Hello world world!'
    formatter = __StringFormatter('  hello world!   hello wOrld!')
    assert formatter.format() == 'Hello world! Hello world!'
    formatter = __StringFormatter('   hello@world.com   ')
    assert formatter.format() == 'hello@world.com'
    formatter = __StringFormatter('  https://docs.djangoproject.com/en/3.1/ref/templates/builtins/  ')
    assert formatter.format() == 'https://docs.djangoproject.com/en/3.1/ref/templates/builtins/'
    formatter = __StringFormatter('  hello-world-   ')


# Generated at 2022-06-14 05:44:25.626083
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:44:35.999419
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    sf = __StringFormatter('  welcome   dude   ')
    assert sf.format() == 'Welcome dude'

    sf = __StringFormatter('welcome   dude')
    assert sf.format() == 'Welcome dude'

    sf = __StringFormatter('welcome_dude')
    assert sf.format() == 'Welcome dude'

    sf = __StringFormatter('welcome dude')
    assert sf.format() == 'Welcome dude'

    sf = __StringFormatter('welcome:dude')
    assert sf.format() == 'Welcome: dude'

    sf = __StringFormatter('welcome.dude')
    assert sf.format() == 'Welcome. Dude'

    sf = __StringFormatter('welcome...dude')

# Generated at 2022-06-14 05:44:39.831870
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    for d in PRETTIFY_TESTS:
        assert __StringFormatter(d['input']).format() == d['output']

# PUBLIC API



# Generated at 2022-06-14 05:44:54.230107
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    formatter = __StringFormatter('  the   quick brown  fox jumps over the  lazy dog  ')
    assert formatter.format() == 'The quick brown fox jumps over the lazy dog'

    formatter = __StringFormatter('  THE   QUICK BROWN  FOX JUMPS OVER THE  LAZY DOG  ')
    assert formatter.format() == 'The quick brown fox jumps over the lazy dog'

    formatter = __StringFormatter('  the   quick brown  fox jumps over: the  lazy dog  ')
    assert formatter.format() == 'The quick brown fox jumps over: the lazy dog'

    formatter = __StringFormatter('  the   quick brown  fox jumps over, the  lazy dog  ')
    assert formatter.format() == 'The quick brown fox jumps over, the lazy dog'


# Generated at 2022-06-14 05:45:01.248877
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:45:11.915928
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    import unittest
    import random


# Generated at 2022-06-14 05:45:19.668590
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('  test  ').format() == 'Test'
    assert __StringFormatter('  test1 test2   test3   test4 test5    test6    test7 test8 ').format() == 'Test1 Test2 Test3 Test4 Test5 Test6 Test7 Test8'
test___StringFormatter_format()


# Generated at 2022-06-14 05:45:30.770033
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('  foo-Bar  ').format() == 'Foo Bar'
    assert __StringFormatter('helloWorld').format() == 'Hello world'
    assert __StringFormatter('http://www.example.com/foo/bar').format() == 'http://www.example.com/foo/bar'
    assert __StringFormatter('  <p>Text</p>  ').format() == 'Text'
    assert __StringFormatter('<p><br />Text</p>').format() == 'Text'
    assert __StringFormatter('<p>Text<br /></p>').format() == 'Text'
    assert __StringFormatter('  <p>  Text  </p>  ').format() == 'Text'
    assert __StringFormatter('<h2>This Is A Title</h2>').format

# Generated at 2022-06-14 05:45:39.505027
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert PRETTIFY_TESTS_DATA['INPUT'] == __StringFormatter(PRETTIFY_TESTS_DATA['INPUT']).format()
    assert PRETTIFY_TESTS_DATA['WITH_PLACEHOLDERS'] == __StringFormatter(PRETTIFY_TESTS_DATA['WITH_PLACEHOLDERS']).format()

# Generated at 2022-06-14 05:45:51.844294
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False, '-') == 'the_snake_is_green'
    # Unit test for function camel_case_to_snake

# Generated at 2022-06-14 05:45:52.735226
# Unit test for function booleanize
def test_booleanize():
    assert(booleanize('true') == True)
    assert(booleanize('False') == False)

# Generated at 2022-06-14 05:45:56.895839
# Unit test for function shuffle
def test_shuffle():
    # fully random result, we have to check multiple times to grant we have at least
    # one random result
    out = shuffle('hello world')

    assert out == 'hlleo oldwr', 'String was not properly shuffled'



# Generated at 2022-06-14 05:46:06.502481
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode(1) == 'I'
    assert roman_encode(2) == 'II'
    assert roman_encode(3) == 'III'
    assert roman_encode(4) == 'IV'
    assert roman_encode(5) == 'V'
    assert roman_encode(6) == 'VI'
    assert roman_encode(7) == 'VII'
    assert roman_encode(8) == 'VIII'
    assert roman_encode(9) == 'IX'
    assert roman_encode(10) == 'X'
    assert roman_encode(11) == 'XI'
    assert roman_encode(14) == 'XIV'
    assert roman_encode(15) == 'XV'


# Generated at 2022-06-14 05:46:18.303621
# Unit test for function strip_html
def test_strip_html():
    assert isinstance(strip_html(''), str)
    assert isinstance(strip_html('foo'), str)
    assert isinstance(strip_html('foo <bar baz="foobar">'), str)
    assert isinstance(strip_html('foo <bar baz="foobar">', keep_tag_content=True), str)
    assert isinstance(strip_html('<a href="foo/bar">click here</a>'), str)
    assert isinstance(strip_html('<a href="foo/bar">click here</a>', keep_tag_content=True), str)
    assert strip_html('') == ''
    assert strip_html('foo') == 'foo'
    assert strip_html('foo <bar baz="foobar">') == 'foo '

# Generated at 2022-06-14 05:46:22.510825
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') == True
    assert booleanize('1') == True
    assert booleanize('yes') == True
    assert booleanize('y') == True
    assert booleanize('nope') == False
    assert booleanize('0') == False
    assert booleanize('no') == False

test_booleanize()


# Generated at 2022-06-14 05:46:23.964539
# Unit test for function slugify
def test_slugify():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'

test_slugify()


# Generated at 2022-06-14 05:46:27.643959
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    input_string = 'hello'

    # compress
    output = __StringCompressor.compress(input_string)
    print('Output: ' + output)

    # decompress
    output2 = __StringCompressor.decompress(output)
    print('Output: ' + output2)


# PUBLIC API


# Generated at 2022-06-14 05:46:40.749460
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('') == ''
    assert strip_html('<a href="/foo/bar">Click here</a>') == ''
    assert strip_html('<a href="/foo/bar">Click here</a>', keep_tag_content=True) == 'Click here'
    assert strip_html('<p>Ciao</p>') == ''
    assert strip_html('<p>Ciao</p>', keep_tag_content=True) == 'Ciao'
    assert strip_html('<p class="test">Ciao</p>') == ''
    assert strip_html('<p class="test">Ciao</p>', keep_tag_content=True) == 'Ciao'

# Generated at 2022-06-14 05:46:44.539331
# Unit test for function decompress
def test_decompress():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    assert original == decompress(compressed)



# ######################################################################################################################
# ###   PRIVATE   ######################################################################################################
# ######################################################################################################################


# Generated at 2022-06-14 05:47:04.702460
# Unit test for function prettify
def test_prettify():
    test_string = '''
    un prettified string ,, like this one,will be"prettified" .it\\' s awesome!
    '''
    expected = '''
    Unprettified string, like this one, will be "prettified".
    It\'s awesome!
    '''
    assert prettify(test_string) == expected



# Generated at 2022-06-14 05:47:09.031873
# Unit test for function booleanize
def test_booleanize():
    x = booleanize('true')
    assert x, "booleanize('true') is not true."



# Generated at 2022-06-14 05:47:18.309840
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    s = __StringFormatter('  string  with   duplicate    spaces  ')
    assert s.format() == 'string with duplicate spaces'

    s = __StringFormatter('string-with-no-space-on-the-left')
    assert s.format() == 'string-with-no-space-on-the-left'

    s = __StringFormatter('string-with-no-space-on-the-right')
    assert s.format() == 'string-with-no-space-on-the-right'

    s = __StringFormatter('string with no space on the left')
    assert s.format() == 'string with no space on the left'

    s = __StringFormatter('string with no space on the right')
    assert s.format() == 'string with no space on the right'

    s = __String

# Generated at 2022-06-14 05:47:30.524968
# Unit test for function strip_margin
def test_strip_margin():
    print(strip_margin('''
        |line 1
        |line 2
        |line 3
    '''))

test_strip_margin()

#print(strip_margin('''
#line 1
#line 2
#line 3
#'''))

#print(strip_margin('''
#    line 1
#    line 2
#    line 3
#'''))

#print(strip_margin('''
#    |line 1
#    |line 2
#    |line 3
#'''))


#print(strip_margin('''
#|line 1
#|line 2
#|line 3
#'''))


#print(strip_margin('''
#    |line 1
#    |line 2
#    |line 3
#'''))


#print

# Generated at 2022-06-14 05:47:32.030888
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') == True


# Generated at 2022-06-14 05:47:34.891450
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'


# Generated at 2022-06-14 05:47:37.096902
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
        assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
# test_camel_case_to_snake()



# Generated at 2022-06-14 05:47:47.002954
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('VII') == 7
    assert roman_decode('vii') == 7
    assert roman_decode('XVI') == 16
    assert roman_decode('xvi') == 16
    assert roman_decode('MMXX') == 2020
    assert roman_decode('mmxx') == 2020


if __name__ == '__main__':
    test_roman_decode()
    # test_fuzzy_search()
    # test_roman_encode()
    # test_roman_decode()
    # test_string_randomizer()

# Generated at 2022-06-14 05:47:55.037588
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') is True, "booleanize('true') should return True"
    assert booleanize('True') is True, "booleanize('True') should return True"
    assert booleanize('1') is True, "booleanize('1') should return True"
    assert booleanize('yes') is True, "booleanize('yes') should return True"
    assert booleanize('Yes') is True, "booleanize('Yes') should return True"
    assert booleanize('Y') is True, "booleanize('Y') should return True"
    assert booleanize('nope') is False, "booleanize('nope') should return False"
    # assert booleanize(1) is False, "booleanize(1) should return False"
    # assert booleanize('') is False, "booleanize('') should return

# Generated at 2022-06-14 05:48:01.710369
# Unit test for function booleanize
def test_booleanize():
    stringa="true"
    stringb="YES"
    stringc="nope"
    n=booleanize(stringa)
    m=booleanize(stringb)
    o=booleanize(stringc)
    assert n == True
    assert m == True
    assert o == False


if __name__ == '__main__':
    test_booleanize()