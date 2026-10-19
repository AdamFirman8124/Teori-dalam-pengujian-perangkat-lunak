

# Generated at 2022-06-14 05:38:47.291363
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    instance = __StringFormatter('Hello $ World!!!')
    assert instance.format() == 'Hello world!'


# PUBLIC API



# Generated at 2022-06-14 05:38:57.921233
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    f = __StringFormatter('this is a sample sentence, including some special cases: | https://www.library|.edu | '
                          '|http://www.library.edu| |http://library.edu| |my.email@domain.com| | '
                          'my.email@domain.com|').format()
    expected = 'This is a sample sentence, including some special cases: https://www.library.edu | http://www.library.edu ' \
               '| http://library.edu | my.email@domain.com'
    assert f == expected, f"Failed; expected '{expected}' but got '{f}'"



# Generated at 2022-06-14 05:39:05.554022
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:39:11.609197
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # input data
    s = 'test     string to format. ciao_cometesta. how.are. you? mike@test.com. it,is@test.it  and i love ' \
        'http://www.test.com'
    e = 'Test string to format. Ciao_cometesta. How.Are. You? Mike@test.com. It,is@test.it and i love ' \
        'http://www.test.com'

    # method tested
    formatter = __StringFormatter(s)
    assert formatter.format() == e



# Generated at 2022-06-14 05:39:21.577151
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False, '-') == 'the-snake-is-green'
    assert snake_case_to_camel('the-snake-is-green', False, '-') == 'the-snake-is-green'

# Generated at 2022-06-14 05:39:31.767834
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('   Hello   World  Foo  bar  ').format() == 'Hello World Foo Bar'
    assert __StringFormatter('hello,world.Foo?Bar').format() == 'Hello, World. Foo? Bar'
    assert __StringFormatter('hello-world--foo-bar').format() == 'Hello-World Foo-Bar'
    assert __StringFormatter('hello_world__foo_bar').format() == 'Hello_World Foo_Bar'
    assert __StringFormatter('hello^world__foo_bar').format() == 'Hello^World Foo_Bar'
    assert __StringFormatter('hello^world--foo-bar').format() == 'Hello^World Foo-Bar'
    assert __StringFormatter('hello^world__foo-bar').format() == 'Hello^World Foo-Bar'

# Generated at 2022-06-14 05:39:42.558803
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    # Check that the result of snake_case_to_camel is a string
    assert is_string(snake_case_to_camel('the_snake_is_green')) == True
    assert is_string(snake_case_to_camel('the_snake_is_green', False)) == True
    assert is_string(snake_case_to_camel('the_snake_is_green', True, '-')) == True
    assert is_string(snake_case_to_camel('the_snake_is_green', False, '-')) == True  

    # Check that the result of snake_case_to_camel is the same as expected
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case

# Generated at 2022-06-14 05:39:48.696247
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False, separator='-') == 'theSnakeIsGreen'
    assert snake_case_to_camel('the snake is green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('this is a sentence', upper_case_first=False) == 'thisIsASentence'

# Generated at 2022-06-14 05:40:01.132229
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:40:10.604534
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    #first case
    upper_case_first = False
    separator = '_'
    input_string = 'the_snake_is_green'
    assert snake_case_to_camel(input_string) == 'TheSnakeIsGreen'
    # second case
    upper_case_first = True
    separator = '_'
    input_string = 'The_Snake_Is_Green'
    assert snake_case_to_camel(input_string) == 'TheSnakeIsGreen'



# Generated at 2022-06-14 05:40:21.440667
# Unit test for function prettify

# Generated at 2022-06-14 05:40:25.819275
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'
    assert asciify('short string') == 'short string'
    assert asciify('---') == '---'
    assert asciify('') == ''
    assert asciify(None) == ''



# Generated at 2022-06-14 05:40:30.171919
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true')
    assert booleanize('True') == booleanize('true')
    assert booleanize('TRUE') == booleanize('true')
    assert booleanize('1') == booleanize('true')
    assert booleanize('Yes') == booleanize('true')
    assert booleanize('YES') == booleanize('true')
    assert booleanize('y') == booleanize('true')
    assert booleanize('Y') == booleanize('true')
    assert not booleanize('no')
    assert not booleanize('nope')
    assert not booleanize('0')
    assert not booleanize('false')
    assert not booleanize('0')
test_booleanize()

# Generated at 2022-06-14 05:40:35.449922
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    input_string = '   lorem   ipsum  dolor    sit    amet    '
    formatter = __StringFormatter(input_string)
    assert formatter.input_string == input_string


# Generated at 2022-06-14 05:40:37.014007
# Unit test for function roman_encode
def test_roman_encode():
    return roman_encode(37)
    
    

# Generated at 2022-06-14 05:40:37.921486
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('CamelCaseString') == 'camel_case_string'


# Generated at 2022-06-14 05:40:45.432588
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    from .unit_testing import assert_object

    assert_object(__StringCompressor)
    print('"__StringCompressor" class has no public methods, therefore this test does not assert anything')


# PUBLIC API


# Converting to and from camelCase


# Generated at 2022-06-14 05:40:46.241106
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('MMXIV') == 2014
    assert roman_decode('V') == 5


# Generated at 2022-06-14 05:40:55.189306
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('THE_SNAKE_IS_GREEN', False) == 'tHE_SNAKE_IS_GREEN'
    assert snake_case_to_camel('THE_SNAKE_IS_green', False) == 'tHE_SNAKE_IS_Green'
    assert snake_case_to_camel('THIS_is_a_test', False) == 'tHIS_Is_A_Test'
    assert snake_case_to_camel('this_is_a_test', False) == 'thisIsATest'
    assert snake_

# Generated at 2022-06-14 05:40:59.446246
# Unit test for function prettify
def test_prettify():
    assert prettify(' unprettified string ,, like this one,will be"prettified" .it\\'
                    ' s awesome! ') == 'Unprettified string, like this one, will be ' \
                                       '"prettified". It\'s awesome!'



# Generated at 2022-06-14 05:41:11.116208
# Unit test for constructor of class __StringFormatter

# Generated at 2022-06-14 05:41:20.530323
# Unit test for function prettify
def test_prettify():
    out = prettify('''This is a test for string prettify !!! It's very cool.
                        It will correct spacing, letters, punctuation, even brackets and quotes.
                        For example 100 % of the words in this sentence
                        will be "prettified" and it's awesome.
                        Dave's dog is also ok.''')
    assert out == '''This is a test for string prettify! It's very cool. It will correct spacing, letters, punctuation,
                     even brackets and quotes. For example 100% of the words in this sentence will be "prettified" and
                     it's awesome. Dave's dog is also ok.'''



# Generated at 2022-06-14 05:41:22.691330
# Unit test for function decompress
def test_decompress():
    original = "lorem ipsum"
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed == original


# Generated at 2022-06-14 05:41:28.306889
# Unit test for function prettify
def test_prettify():
    import re

    input = """Unprettified string! Like    this one,will be"prettified" .it\'s awesome! it\\'s awesome! \
("foo(bar )baz")"""

    expected = """Unprettified string! Like this one, will be "prettified". It's awesome! it's awesome! \
("foo (bar) baz")"""

    result = prettify(input)
    assert result == expected



# Generated at 2022-06-14 05:41:41.443631
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.encode(1) == 'I'
    assert __RomanNumbers.encode(5) == 'V'
    assert __RomanNumbers.encode(10) == 'X'
    assert __RomanNumbers.encode(15) == 'XV'
    assert __RomanNumbers.encode(20) == 'XX'
    assert __RomanNumbers.encode(25) == 'XXV'
    assert __RomanNumbers.encode(30) == 'XXX'
    assert __RomanNumbers.encode(35) == 'XXXV'
    assert __RomanNumbers.encode(40) == 'XL'
    assert __RomanNumbers.encode(45) == 'XLV'
    assert __RomanNumbers.encode(50) == 'L'
    assert __RomanNumbers.encode(55) == 'LV'
    assert __

# Generated at 2022-06-14 05:41:44.587856
# Unit test for function asciify
def test_asciify():
    input_string = 'èéùúòóäåëýñÅÀÁÇÌÍÑÓË'
    assert asciify(input_string) == 'eeuuooaaeynAAACIINOE'

# Testing function

# Generated at 2022-06-14 05:41:48.727609
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') == True
    assert booleanize('false') == False
    assert booleanize('TRUE') == True
    assert booleanize('y') == True
    assert booleanize('YES') == True
    assert booleanize('yes') == True
    assert booleanize('1') == True
    assert booleanize('0') == False
    assert booleanize('nope') == False
    assert booleanize('') == False
    assert booleanize(' ') == False

# Unit tests for function slugify

# Generated at 2022-06-14 05:42:00.159425
# Unit test for function asciify
def test_asciify():
    # Test 1
    input_string = 'èéùúòóäåëýñÅÀÁÇÌÍÑÓË'
    output = asciify(input_string)
    assert output == 'eeuuooaaeynAAACIINOE'

    # Test 2
    input_string = 'ÈÈÈÈÈÈÈÈÈÈ'
    output = asciify(input_string)
    assert output == 'EEEEEEEEEEE'

    # Test 3
    input_string = 'aèéùúòóäåëýñÅÀÁÇÌÍÑÓËb'
    output = asciify(input_string)

# Generated at 2022-06-14 05:42:10.555348
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('a_snake_case_string') == "ASnakeCaseString"
    assert snake_case_to_camel('a_snake_case_string', False) == "aSnakeCaseString"
    assert snake_case_to_camel('a_snake_case_string', True, '-') == "ASnakeCaseString"
    assert snake_case_to_camel('a_snake_case_string', False, '-') == "aSnakeCaseString"
    assert snake_case_to_camel('a_snake_case_string', True, '-') == "ASnakeCaseString"
    assert snake_case_to_camel('a_snake-case_string', False, '-') == "aSnake-CaseString"
    assert snake_case

# Generated at 2022-06-14 05:42:14.635807
# Unit test for function slugify
def test_slugify():
    cases = {
        "this is a test": "this-is-a-test",
        "Foo Bar": "foo-bar",
        "is.this?a.test": "istasatest",
        "1123581321345589144": "1123581321345589144",
        "¥µ€ƒ£¢―—¬®¯¥µ€ƒ£¢―¬": '¥µ-ƒ£-¢-®-¯¥µ-ƒ£-¢-¬',
        'Mönstér Mägnët': 'monster-magnet'
    }

    for case, expected in cases.items():
        assert slugify(case) == expected

    # same tests with a custom separator

# Generated at 2022-06-14 05:42:33.198399
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('testString') == 'test_string' 
    assert camel_case_to_snake('test string') == 'test string' 
camel_case_to_snake('testString')
camel_case_to_snake('test string')


# Generated at 2022-06-14 05:42:42.736596
# Unit test for function roman_decode
def test_roman_decode():
    # Test roman_decode (should be 0/1 => False/True)
    print("\nTest roman_decode (should be 0/1 => False/True)")
    print(roman_decode('II') == 3)
    print(roman_decode('MCMXLIV') == 1944)
    print(roman_decode('XX') == 20)
    print(roman_decode('XLII') == 42)
    print(roman_decode('') == 0)
    print(roman_decode("garbage") == 0)
    print(roman_decode("IIII") == 0)
    print(roman_decode("XIIV") == 0)
    print(roman_decode("IC") == 0)
    print(roman_decode("XIX") == 19)

# Generated at 2022-06-14 05:42:55.836881
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.__encode_digit(0, 1) == 'I'
    assert __RomanNumbers.__encode_digit(0, 5) == 'V'
    assert __RomanNumbers.__encode_digit(0, 4) == 'IV'
    assert __RomanNumbers.__encode_digit(1, 9) == 'XC'
    assert __RomanNumbers.__encode_digit(1, 5) == 'L'
    assert __RomanNumbers.__encode_digit(1, 8) == 'LXXX'
    assert __RomanNumbers.__encode_digit(2, 9) == 'CM'
    assert __RomanNumbers.__encode_digit(2, 5) == 'D'
    assert __RomanNumbers.__encode_digit(3, 1) == 'M'
    assert __RomanNumbers.__en

# Generated at 2022-06-14 05:43:01.574400
# Unit test for function roman_decode
def test_roman_decode():
    # Assert that roman_decode returns as expected
    assert roman_decode('VII') == 7
    assert roman_decode('MVXII') == 1008
    assert roman_decode('LXXIX') == 79
    assert roman_decode('CXLVIII') == 148
    assert roman_decode('CLV') == 155

# Generated at 2022-06-14 05:43:08.617049
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('c', False) == 'c'
    assert snake_case_to_camel('c', True) == 'C'
    assert snake_case_to_camel('a_b_c') == 'ABC'
    assert snake_case_to_camel('c', False, '.') == 'c'
    assert snake_case_to_camel('') == ''
    assert snake_case_to_camel('a.b..') == 'A.b..'
    assert snake_case_to_camel('a.B..', upper_case_first=False) == 'a.B..'

    assert snake_case_to_camel('ac', upper_case_first=False) == 'ac'

    print('test snake_case_to_camel done.')


# Generated at 2022-06-14 05:43:17.954825
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('test') == 'test'
    assert snake_case_to_camel('test_string') == 'testString'
    assert snake_case_to_camel('test_string', False) == 'testString'
    assert snake_case_to_camel('test_string', True) == 'TestString'
    assert snake_case_to_camel('test', False) == 'test'
    assert snake_case_to_camel('some string') == 'SomeString'



# Generated at 2022-06-14 05:43:29.778114
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.encode(1) == 'I'
    assert __RomanNumbers.encode(5) == 'V'
    assert __RomanNumbers.encode(10) == 'X'
    assert __RomanNumbers.encode(14) == 'XIV'
    assert __RomanNumbers.encode(15) == 'XV'
    assert __RomanNumbers.encode(39) == 'XXXIX'
    assert __RomanNumbers.encode(40) == 'XL'
    assert __RomanNumbers.encode(41) == 'XLI'
    assert __RomanNumbers.encode(44) == 'XLIV'
    assert __RomanNumbers.encode(50) == 'L'
    assert __RomanNumbers.encode(90) == 'XC'
    assert __RomanNumbers.encode(100) == 'C'
   

# Generated at 2022-06-14 05:43:39.915556
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    formatter = __StringFormatter(' ')
    assert formatter.format() == ''

    formatter = __StringFormatter(
        'Lorem Ipsum è un testo segnaposto utilizzato nel '
        'composizione e impaginazione, http://www.google.com '
        'al fine di agevolare la impaginazione del testo che '
        'verrà distribuite@libero.it. '
    )
    assert formatter.format() == 'Lorem Ipsum è un testo segnaposto utilizzato nel composizione e impaginazione, ' \
                                 'http://www.google.com al fine di agevolare la impaginazione del testo che verrà ' \
                                 'distribuite@libero.it.'

# Generated at 2022-06-14 05:43:49.580834
# Unit test for function prettify
def test_prettify():
    #test empty string
    s = prettify('')
    assert(s=='')
    #test normal

# Generated at 2022-06-14 05:44:00.773608
# Unit test for function prettify
def test_prettify():
    assert 'This is a test' == prettify('  This       is a   test    ')
    assert 'This is a test' == prettify('This is a test')
    assert 'This is a test.' == prettify('This is a test.')
    assert 'This is a test...' == prettify('This is a test...')
    assert 'This is a test. This is a test.' == prettify('This is a test.   This is a test.')
    assert 'This is a test? This is a test!' == prettify('This is a test ? This is a test !')
    assert 'This is a test. This is a test.' == prettify('This is a test. This is a test.')
    assert 'This is a test. This is a test.' == prettify('This is a test.  This is a test.')
   

# Generated at 2022-06-14 05:44:29.562903
# Unit test for function reverse
def test_reverse():
    assert reverse('hello') == 'olleh'



# Generated at 2022-06-14 05:44:35.048668
# Unit test for function slugify
def test_slugify():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
    assert slugify('This is a long sentence that will generate a slug. Yea!!.') == 'this-is-a-long-sentence-that-will-generate-a-slug-yea'

# Generated at 2022-06-14 05:44:42.732673
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    def __do_test(text, expected_result):
        prettified = __StringFormatter(text).format()
        assert prettified == expected_result, 'Test failed: text = {}, result = {}, expected = {}'.format(text, prettified, expected_result)

    __do_test(
        'abc  abc  abc',
        'Abc abc abc')
    __do_test(
        'Abc abc abc',
        'Abc abc abc')
    __do_test(
        'ABC Abc Abc',
        'Abc abc abc')
    __do_test(
        'aBc abC abc',
        'Abc abc abc')

# Generated at 2022-06-14 05:44:55.307887
# Unit test for function slugify
def test_slugify():
    import unittest

    class TestSlugify(unittest.TestCase):
        def test_with_spaces(self):
            self.assertEqual(slugify('This is a sentence'), 'this-is-a-sentence')

        def test_with_punctuation(self):
            self.assertEqual(slugify('.;,:!?*'), '')

        def test_spaces_and_punctuation(self):
            self.assertEqual(slugify(' Test for spaces and punctuation. '), 'test-for-spaces-and-punctuation')

        def test_with_non_ascii(self):
            self.assertEqual(slugify('Test for German Umlauts ä,ö,ü'), 'test-for-german-umlauts-aou')

# Generated at 2022-06-14 05:45:01.166542
# Unit test for function strip_margin
def test_strip_margin():
    multiline_string = '''
  | line 1
  | line 2
  | line 3
'''
    assert strip_margin(multiline_string) == '''
  line 1
  line 2
  line 3
'''



# Generated at 2022-06-14 05:45:03.404455
# Unit test for function strip_html
def test_strip_html():
	print(strip_html('test: <a href="foo/bar">click here</a>')) # returns 'test: '
	print(strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True)) # returns 'test: click here'
#test_strip_html()


# Generated at 2022-06-14 05:45:12.029279
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    assert __StringFormatter('hello').input_string == 'hello'
    assert __StringFormatter(42).input_string == '42'
    assert __StringFormatter(42.942).input_string == '42.942'
    assert __StringFormatter(True).input_string == 'True'
    assert __StringFormatter(False).input_string == 'False'
    assert __StringFormatter(None).input_string == 'None'

    try:
        __StringFormatter(42)
    except InvalidInputError:
        pass


# Generated at 2022-06-14 05:45:17.686055
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

    

# Generated at 2022-06-14 05:45:19.971056
# Unit test for function reverse
def test_reverse():
    assert reverse('hello') == 'olleh'
    assert callable(reverse)



# Generated at 2022-06-14 05:45:23.660273
# Unit test for function compress
def test_compress():
    n = 0 # <- ignore this, it's a fix for Pycharm (not fixable using ignore comments)
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    assert isinstance(original, str)
    assert isinstance(compressed, str)
    assert (len(original) > len(compressed))



# Generated at 2022-06-14 05:46:22.652991
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    result = snake_case_to_camel('the_snake_is_green') # returns 'TheSnakeIsGreen'
    print(result)
    assert result == 'TheSnakeIsGreen', " failed"
    
    
    
    
    

# Generated at 2022-06-14 05:46:24.153763
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'



# Generated at 2022-06-14 05:46:27.283591
# Unit test for function decompress
def test_decompress():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert original == decompressed
test_decompress()


# Generated at 2022-06-14 05:46:37.634810
# Unit test for function prettify
def test_prettify():
    print("------------------")
    print("Test function prettify")
    print("------------------")
    print()
    print("Uppercase first letter:", prettify("hello world"))

    print("Remove duplicated space:", prettify("hello  world"))

    print("Remove trailing space:", prettify("hello world "))

    print("Remove leading space:", prettify("   hello world"))

    print("Remove trailing empty lines:", prettify("Hello world!\n\n\n\n\n"))

    print("Remove leading empty lines:", prettify("\n\n\n\n\nHello world!"))

    print("Remove trailing punctuation:", prettify("Hello world! ?? ! ,,,..,."))

    print("Remove leading punctuation:", prettify("?? ! ,,,..,. Hello world!"))


# Generated at 2022-06-14 05:46:39.177342
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('VII') == 7

# Generated at 2022-06-14 05:46:49.366268
# Unit test for function strip_html
def test_strip_html():
    if strip_html('test: <a href="foo/bar">click here</a>') != 'test: ' and strip_html('<a href="foo/bar">click here</a>') != '':
        raise ValueError()
    if strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) != 'test: click here' and strip_html('<a href="foo/bar">click here</a>', keep_tag_content=True) != 'click here':
        raise ValueError()



# Generated at 2022-06-14 05:46:50.478460
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    assert __StringCompressor != None

test___StringCompressor()


# Generated at 2022-06-14 05:47:00.057968
# Unit test for function compress
def test_compress():
    n = 0 # fix for Pycharm highlighting
    # "original" will be a string with 169 chars:
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    # "compressed" will be a string of 88 chars
    compressed = compress(original)
    assert compressed == 'eNpSyVbKwkAQvfeue7pXKoVB0RNDktpE4H4lWZh8g2BpuKy3YFcSvlSbyA9XmQo' \
                          'w/tW/ZnMgRcGlYiWErFzHjnT8lNhcPdNlk/XXzhBx/Zi+/IGY/YzPQ='



# Generated at 2022-06-14 05:47:11.901373
# Unit test for constructor of class __StringCompressor

# Generated at 2022-06-14 05:47:15.285044
# Unit test for function compress
def test_compress():
    original = "test"
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert original == decompressed