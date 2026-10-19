

# Generated at 2022-06-14 05:38:45.575482
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    test_input = """
    "Hello There"
    "Hello , there!!!"
    "Hello ,there"
    "This is a test's test"
    "This is an email test <test@test.test> but it's not an email"
    "This is a URL test http://www.test.test but it's not a URL"
    "This is a test a very long test f     g     h     i     j     k     l "
    "This is a test a very long test f     g     h     i     j     k     l"
    """

# Generated at 2022-06-14 05:38:46.243976
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    pass



# Generated at 2022-06-14 05:38:51.755467
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    # Test with default arguments
    assert 'TheSnakeIsGreen' == snake_case_to_camel('the_snake_is_green')

    # Test with upper_case_first = False and separator = "-"
    assert 'theSnakeIsGreen' == snake_case_to_camel('the-snake-is-green', False, '-')



# Generated at 2022-06-14 05:38:56.289184
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('snake_case', False, '-') == 'snake-case'



# Generated at 2022-06-14 05:39:05.466656
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False, separator='-') == 'the-snake-is-green'
    assert snake_case_to_camel('the-snake-is-green', upper_case_first=True, separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'

# Generated at 2022-06-14 05:39:12.045920
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('ThisIsAStringWithAnAcronymLikeHTTP') == 'this_is_a_string_with_an_acronym_like_http'
    assert camel_case_to_snake(' ThisIsAStringWithAnAcronymLikeHTTP ') == 'this_is_a_string_with_an_acronym_like_http'



# Generated at 2022-06-14 05:39:15.285300
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'


# Generated at 2022-06-14 05:39:18.519698
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake("ThisIsACamelStringTest") == "this_is_a_camel_string_test"



# Generated at 2022-06-14 05:39:32.948610
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('this is a test. 1234. test@test.com').format() == 'This is a test. 1234. test@test.com'
    assert __StringFormatter('test      here').format() == 'Test here'
    assert __StringFormatter('https://google.it').format() == 'https://google.it'
    assert __StringFormatter('(test) http://something here').format() == '(test) http://something here'
    assert __StringFormatter('(test) http://something here').format() == '(test) http://something here'
    assert __StringFormatter('hello\tworld').format() == 'Hello world'
    assert __StringFormatter('hello\tworld\n').format() == 'Hello world'

# Generated at 2022-06-14 05:39:43.391188
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    str_formatter = __StringFormatter("tHis is a      test txt")
    assert str_formatter.format() == "This is a test txt"

    str_formatter = __StringFormatter("tHis is a      test txt.....")
    assert str_formatter.format() == "This is a test txt."

    str_formatter = __StringFormatter("tHis is a  test txt   .....")
    assert str_formatter.format() == "This is a test txt."

    str_formatter = __StringFormatter("tHis is a  test txt   .....")
    assert str_formatter.format() == "This is a test txt."

    str_formatter = __StringFormatter("url: http://google.com acta")

# Generated at 2022-06-14 05:40:00.985521
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('The-Snake-Is-Green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('TheSnakeIsGreenToTest', upper_case_first=False) == 'theSnakeIsGreenToTest'
    assert snake

# Generated at 2022-06-14 05:40:10.485780
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('this_is_my_snake', separator='-') == 'ThisIsMySnake'
    assert snake_case_to_camel('this.is.my.snake', separator='.') == 'ThisIsMySnake'



# Generated at 2022-06-14 05:40:18.460531
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('this_is_a_full_string') == 'ThisIsAFullString'
    assert snake_case_to_camel('a_full_string') == 'AFullString'
    assert snake_case_to_camel('a_full_string', False) == 'aFullString'
    assert snake_case_to_camel('a_full_string', separator='-') == 'AFullString'
    assert snake_case_to_camel('this_is_a_camel_string_test') == 'ThisIsACamelStringTest'
    assert snake_case_to_camel('this_is_a_camel_string_test', False) == 'thisIsACamelStringTest'



# Generated at 2022-06-14 05:40:27.154437
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('THE_SNAKE_IS_GREEN', upper_case_first=False) == 'tHE_SNAKE_IS_GREEN'
    assert snake_case_to_camel('THE__SNAKE__IS__GREEN') == 'THESnakeIsGreen'
    assert snake_case_to_camel('camel_case', separator='-') == 'camelCase'



# Generated at 2022-06-14 05:40:28.495185
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('this_is_a_snake_case_test_string') == 'ThisIsASnakeCaseTestString'



# Generated at 2022-06-14 05:40:35.195268
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    actual = snake_case_to_camel('the_snake_is_green')
    expected = 'TheSnakeIsGreen'
    assert actual == expected, "Expected {0}, but got {1}".format(expected, actual)

test_snake_case_to_camel()



# Generated at 2022-06-14 05:40:41.906801
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    print(snake_case_to_camel(""))
    print(snake_case_to_camel(" "))
    print(snake_case_to_camel("_a_"))
    print(snake_case_to_camel("a"))
    print(snake_case_to_camel("a_"))
    print(snake_case_to_camel("a_ ", separator=' ', upper_case_first=False))
    print(snake_case_to_camel("a_ ", separator=' ', upper_case_first=True))
    print(snake_case_to_camel("a_b", separator='_', upper_case_first=False))

# Generated at 2022-06-14 05:40:52.073323
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('') == ''
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', upper_case_first=False, separator='-') == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'The_snake_is_green'
    assert snake_case_to_

# Generated at 2022-06-14 05:40:58.020983
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', True, '-') == 'TheSnakeIsGreen'



# Generated at 2022-06-14 05:41:08.696666
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('this_is_a_snake_case_string_test') == 'ThisIsASnakeCaseStringTest'
    assert snake_case_to_camel('this_is_a_snake_case_string_test', True, '_') == 'ThisIsASnakeCaseStringTest'
    assert snake_case_to_camel('this-is-a-snake-case-string-test', True, '-') == 'ThisIsASnakeCaseStringTest'
    assert snake_case_to_camel('this_is_a_snake_case_string_test', False) == 'thisIsASnakeCaseStringTest'

# Generated at 2022-06-14 05:41:17.831718
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('test_test') == 'TestTest'
    assert snake_case_to_camel('test_test', upper_case_first=False) == 'testTest'
    assert snake_case_to_camel('test__test') == 'TestTest'
    assert snake_case_to_camel('test_  _test') == 'TestTest'



# Generated at 2022-06-14 05:41:21.749011
# Unit test for function strip_margin
def test_strip_margin():
    s = '''
    line 1
    line 2
    line 3
    '''

    out = strip_margin(s)

    assert out == '''
line 1
line 2
line 3
'''



# Generated at 2022-06-14 05:41:23.913163
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    class_roman = __RomanNumbers()


# PUBLIC API



# Generated at 2022-06-14 05:41:35.952736
# Unit test for function prettify
def test_prettify():
    print('Testing "prettify" function...')

    # Test that function works well with empty strings
    assert prettify('') == ''

    # Test that function works well with random strings
    assert prettify('a b c de f') == 'A b c de f'

    # Test that a string with empty lines keeps its empty lines
    assert prettify('\n\n') == '\n\n'

    # Test that function works well with a string that
    # - starts with spaces
    # - ends with spaces
    # - contains empty lines
    # - contains 2 or more spaces in sequence
    # - contains spaces before or after punctuation
    # - contains multispaces
    # - contains text inside quotes
    # - contains text inside brackets
    # - contains saxon genitive

# Generated at 2022-06-14 05:41:37.536371
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    assert isinstance(__StringCompressor(), __StringCompressor)


# Generated at 2022-06-14 05:41:42.044304
# Unit test for function roman_encode
def test_roman_encode():
    '''
    This function test the function roman_encode.
    :return: None.
    '''
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode(2020) == 'MMXX'

# Generated at 2022-06-14 05:41:44.728733
# Unit test for function strip_margin
def test_strip_margin():
    expected = '''
line 1
line 2
line 3
'''
    actual = strip_margin('''
                line 1
                line 2
                line 3
            ''')
    assert_equals(expected, actual)

# Generated at 2022-06-14 05:41:52.662695
# Unit test for function prettify
def test_prettify():
    input_string = ' unprettified string ,, like this one,will be"prettified" .it\\\' s awesome! '
    formatted = 'Unprettified string, like this one, will be "prettified". It\'s awesome!'
    assert prettify(input_string) == formatted
    input_string = 'Unprettified string, like this one, will be "prettified". It\\\'s awesome!'
    assert prettify(input_string) == formatted
    input_string = '<p lang="en">Unprettified string, like this one, <b>will be</b> "prettified". It\\\'s awesome!</p>'
    formatted = 'Unprettified string, like this one, will be "prettified". It\'s awesome!'
    assert prettify(input_string) == formatted
   

# Generated at 2022-06-14 05:41:56.726623
# Unit test for function slugify
def test_slugify():
    assert 'top-10-reasons-to-love-dogs' == slugify('Top 10 Reasons To Love Dogs!!!')
    assert 'monster-magnet' == slugify('Mönstér Mägnët')
    assert 'casa-mariano' == slugify('Casa°Mariano°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
    assert 'pixar-in-a-box-lesson-1' == slugify('Pixar in a Box : Lesson 1 - Introduction to Computer Graphics')

# Generated at 2022-06-14 05:42:02.400695
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'
test_strip_html()



# Generated at 2022-06-14 05:42:11.883711
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    original_string = 'I could go for a solid meal right now, some chicken soup and a....' + str(uuid4())
    assert original_string == __StringCompressor.decompress(__StringCompressor.compress(original_string))


# Generated at 2022-06-14 05:42:16.380913
# Unit test for function strip_margin
def test_strip_margin():

    assert strip_margin('''
        |line 1
        |line 2
        |line 3''') == '''
        line 1
        line 2
        line 3'''

    assert strip_margin('''
        |line 1
        |
        |line 3''') == '''
        line 1
        
        line 3'''

    assert strip_margin('''
        |line 1
        |   line 2
        |   line 3''') == '''
        line 1
        line 2
        line 3'''

    assert strip_margin('''
        |line 1
        |line 2
        |    line 3''') == '''
        line 1
        line 2
        line 3'''


# Generated at 2022-06-14 05:42:18.787743
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('a  b').format() == 'a b'


# PUBLIC API



# Generated at 2022-06-14 05:42:24.483614
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    original_string = 'Hello World!'
    compressed_string = __StringCompressor.compress(original_string)
    decompressed_string = __StringCompressor.decompress(compressed_string)
    assert original_string == decompressed_string


__is_initialized = False
__available_marks = None
__unicode_upper_mapping = None
__unicode_lower_mapping = None



# Generated at 2022-06-14 05:42:34.608957
# Unit test for function roman_decode
def test_roman_decode():
    test_cases = [
        {'input': 'XII', 'expected': 12},
        {'input': '', 'expected': None},
        {'input': 'blah', 'expected': None},
        {'input': '-2', 'expected': None},
        {'input': 3, 'expected': None},
        {'input': 'VII', 'expected': 7}
    ]

    for case in test_cases:
        input_string = case['input']
        expected = case['expected']
        actual = roman_decode(input_string)
        assert actual == expected, "roman_decode failed for input: {}".format(input_string)



# Generated at 2022-06-14 05:42:36.777337
# Unit test for function asciify
def test_asciify():
    input_string='èéùúòóäåëýñÅÀÁÇÌÍÑÓË'
    result=asciify(input_string)
    print('Result of test_asciify: ',result)

if __name__ == '__main__':
    test_asciify()



# Generated at 2022-06-14 05:42:43.844901
# Unit test for function decompress
def test_decompress():
    assert is_string(decompress(''))
    assert is_string(decompress('', ''))
    assert is_string(decompress('', ''))

    assert decompress(None) == ''
    assert decompress(None, '') == ''
    assert decompress(None, None) == ''

    assert decompress('Tm9uZXN0') == 'Monest'
    assert decompress('Tm9uZXN0', '') == 'Monest'
    assert decompress('Tm9uZXN0', None) == 'Monest'



# Generated at 2022-06-14 05:42:49.348009
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('A') == 'a'
    assert camel_case_to_snake('a') == 'a'
    assert camel_case_to_snake('aa') == 'aa'
    assert camel_case_to_snake('Aa') == 'aa'
    assert camel_case_to_snake('AA') == 'aa'
    assert camel_case_to_snake('AAa') == 'aa_a'
    assert camel_case_to_snake('AaA') == 'aa_a'
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'

# Generated at 2022-06-14 05:42:51.231385
# Unit test for function shuffle
def test_shuffle():
    assert shuffle('banana') != shuffle('banana')



# Generated at 2022-06-14 05:43:00.079696
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.encode(1999) == 'MCMXCIX'
    assert __RomanNumbers.encode(2005) == 'MMV'
    assert __RomanNumbers.encode(2020) == 'MMXX'
    assert __RomanNumbers.encode(3999) == 'MMMCMXCIX'

    assert __RomanNumbers.decode('MCMLXXXIX') == 1989
    assert __RomanNumbers.decode('MMVIII') == 2008
    assert __RomanNumbers.decode('MCMXC') == 1990


# public api



# Generated at 2022-06-14 05:43:26.402795
# Unit test for function decompress
def test_decompress():
    # Test for invalid input
    for input_string in (None, 1, 2.3, '', True, False, b'foo'):
        try:
            decompress(input_string)
            assert("when not a string, string must be raise")
        except InvalidInputError:
            pass
    # Test for invalid encoding
    for encoding in (None, 1, 2.3, '', True, False, b'foo'):
        try:
            decompress('foo', encoding)
            assert("when not a string, encoding must be raise")
        except InvalidInputError:
            pass
    # TODO : Test cases
    assert(decompress(compress('foo')) == "foo")
    assert(decompress(compress('foo'*100)) == 'foo'*100)


# Generated at 2022-06-14 05:43:32.837030
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel("lorem_ipsum") == "LoremIpsum"
    assert snake_case_to_camel("lorem_ipsum", upper_case_first=False) == "loremIpsum"
    assert snake_case_to_camel(
        "lorem_ipsum", separator="-") == "LoremIpsum"
    

# Generated at 2022-06-14 05:43:37.532010
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('VII') == 7
    assert roman_decode('xix') == 19
    assert roman_decode('XIV') == 14



# Generated at 2022-06-14 05:43:43.518470
# Unit test for function booleanize
def test_booleanize():
    assert(booleanize("true") == True)
    assert(booleanize("True") == True)
    assert(booleanize("1") == True)
    assert(booleanize("YES") == True)
    assert(booleanize("y") == True)
    assert(booleanize("true ") == False)
    assert(booleanize("False") == False)
    assert(booleanize("false ") == False)
    assert(booleanize("false") == False)
    assert(booleanize("0") == False)
    assert(booleanize("No") == False)
    assert(booleanize("n") == False)
    assert(booleanize("") == False)
    assert(booleanize(0) == False)
test_booleanize()


# Generated at 2022-06-14 05:43:46.424836
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    assert __StringCompressor.decompress(__StringCompressor.compress('a' * 10000)) == 'a' * 10000

test___StringCompressor()



# Generated at 2022-06-14 05:43:57.193868
# Unit test for function asciify
def test_asciify():
    assert asciify(None) == ''
    assert asciify('Test') == 'Test'
    assert asciify('Ã©') == 'e'
    assert asciify('Ã¨') == 'e'
    assert asciify('Ã¨') == 'e'
    assert asciify('Ã¹') == 'u'
    assert asciify('Ã¹Ã¨') == 'ue'
    assert asciify('uÃ¨') == 'ue'
    assert asciify('Ã®') == 'i'
    assert asciify('Ã‘') == 'N'
    assert asciify('Ã­Ã®') == 'ii'
    assert asciify('ã©') == 'e'
    assert asciify('ã¨') == 'e'
    assert asciify('ã¨') == 'e'

# Generated at 2022-06-14 05:43:58.687260
# Unit test for function reverse
def test_reverse():
    assert reverse('hello') == 'olleh'
# Test
test_reverse()



# Generated at 2022-06-14 05:44:08.359872
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.__mappings[0] == {1: 'I', 5: 'V'}
    assert __RomanNumbers.__mappings[1] == {1: 'X', 5: 'L'}
    assert __RomanNumbers.__mappings[2] == {1: 'C', 5: 'D'}
    assert __RomanNumbers.__mappings[3] == {1: 'M'}

    assert __RomanNumbers.__reversed_mappings[0] == {'I': 1, 'V': 5}
    assert __RomanNumbers.__reversed_mappings[1] == {'X': 1, 'L': 5}
    assert __RomanNumbers.__reversed_mappings[2] == {'C': 1, 'D': 5}
    assert __RomanNumbers.__reversed_mappings

# Generated at 2022-06-14 05:44:10.858430
# Unit test for function slugify
def test_slugify():
    print('Testing slugify...')

    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs', \
        "Slugify is not working properly"
    assert slugify(' Mönstér Mägnët ', '_') == 'monster_magnet', \
        "Slugify is not working properly"

    print('All test OK')

# Let's test it!
test_slugify()


# Generated at 2022-06-14 05:44:15.589269
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    assert __StringFormatter('aaa bbb ccc').input_string == 'aaa bbb ccc'
    exception_thrown = False
    try:
        __StringFormatter(123)
    except InvalidInputError:
        exception_thrown = True
    assert exception_thrown



# Generated at 2022-06-14 05:44:40.042187
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    input_roman = ['I', 'IV', 'X', 'XIV', 'XIX', 'CCLXXVII', 'CDXCIX', 'MCMLXXXVII', 'MMXVIII', 'MMMCMXCIX', 'MMMM']
    output_int = [1, 4, 10, 14, 19, 277, 499, 1987, 2018, 3999, 4000]
    for i in range(0, len(input_roman)):
        assert __RomanNumbers.encode(output_int[i]) == input_roman[i]
        assert __RomanNumbers.decode(input_roman[i]) == output_int[i]
test___RomanNumbers()


# PUBLIC API



# Generated at 2022-06-14 05:44:54.444652
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    # Simple test: The original string is returned if is not a valid snake case string
    assert snake_case_to_camel('hello') == 'hello'

    # Simple test: The original string is returned if is not a valid snake case string
    assert snake_case_to_camel('hello world') == 'hello world'

    # Simple test: The original string is returned if is not a valid snake case string
    assert snake_case_to_camel('hello_world-to-the_moon') == 'hello_world-to-the_moon'

    # Simple test: The original string is returned if is not a valid snake case string
    assert snake_case_to_camel('hello_world_to_the_moon', upper_case_first=False) == 'hello_world_to_the_moon'

    # Simple test: The original string is

# Generated at 2022-06-14 05:45:00.647766
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('this_is_a_string') == 'this_is_a_string'


# Generated at 2022-06-14 05:45:11.884213
# Unit test for function decompress
def test_decompress():
    # positive tests
    assert decompress('fNV4hA8Aso') == 'hello'
    assert decompress('fNV4hA8Aso-world') == 'hello-world'
    assert decompress('fNV4hA8Aso-world', encoding='ascii') == 'hello-world'

    # negative tests
    try:
        decompress('fNV4hA8Aso-world', encoding='foobar')
        assert False
    except ValueError as _:
        pass

    try:
        decompress(1)
        assert False
    except InvalidInputError as _:
        pass

    try:
        decompress(None)
        assert False
    except InvalidInputError as _:
        pass



# Generated at 2022-06-14 05:45:24.077569
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    # encoding
    assert type(__StringCompressor.__require_valid_input_and_encoding('test', 'utf-8')) == ValueError
    assert type(__StringCompressor.__require_valid_input_and_encoding('test', '')) == ValueError

    # compression level
    assert type(__StringCompressor.compress('test', 'utf-8', 5)) != ValueError
    assert type(__StringCompressor.compress('test', 'utf-8', 10)) == ValueError
    assert type(__StringCompressor.compress('test', 'utf-8', -1)) == ValueError


# Generated at 2022-06-14 05:45:28.188549
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelCaseStringTest_CaseB') == 'this_is_a_camel_case_string_test_case_b'
    assert is_snake_case(camel_case_to_snake('ThisIsACAmeL_CaseB'))

    assert camel_case_to_snake('This-IsA-CAMEL_CaseB') == 'this-is_a-c_a_m_e_l__case_b'
    assert is_snake_case(camel_case_to_snake('This-IsA-CAMEL_CaseB'))



# Generated at 2022-06-14 05:45:29.246680
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'



# Generated at 2022-06-14 05:45:31.794413
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true')
    assert booleanize('True')
    assert booleanize('1')
    assert booleanize('YES')
    assert booleanize('y')
    assert not booleanize('false')
    assert not booleanize('0')
    assert not booleanize('NO')
    assert not booleanize('n')


# Generated at 2022-06-14 05:45:43.983285
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
    assert strip_html('<html><div/>test: <a href="foo/bar">click<p>here</p></a></html>') == 'test: '
    assert strip_html('<html><div/>test: <a href="foo/bar">click<p>here</p></a></html>', keep_tag_content=True) == 'test: clickhere'



# Generated at 2022-06-14 05:45:45.009907
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') == True
    assert booleanize('y') == True
    assert booleanize('d') == False

# Generated at 2022-06-14 05:46:21.232570
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    print("test_snake_case_to_camel")

    assert snake_case_to_camel('test_test') == 'TestTest'
    assert snake_case_to_camel('test_test', upper_case_first=False) == 'testTest'
    assert snake_case_to_camel('test test string', upper_case_first=False) == 'test Test String'
    assert snake_case_to_camel('', upper_case_first=False) == ''
    assert snake_case_to_camel('string', upper_case_first=False) == 'string'



# Generated at 2022-06-14 05:46:25.205571
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    original_string = str(uuid4())

    compressed_string = __StringCompressor.compress(original_string)
    decompressed_string = __StringCompressor.decompress(compressed_string)

    # check generated ID are equal
    assert original_string == decompressed_string


test___StringCompressor()


# PUBLIC API



# Generated at 2022-06-14 05:46:32.543004
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('VII') == 7
    assert roman_decode('IV') == 4
    assert roman_decode('MCMXCIX') == 1999
    assert roman_decode('MMMCDXCIII') == 3493
    assert roman_decode('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMC') == 49999
    assert roman_decode('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM') == 50000
    assert roman_decode('III') == 3
    assert roman_decode('I') == 1
    assert roman_decode('XX') == 20
   

# Generated at 2022-06-14 05:46:42.893964
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('my_snake_test') == 'MySnakeTest'
    assert snake_case_to_camel('my_snake_test', upper_case_first=False) == 'mySnakeTest'
    assert snake_case_to_camel('my_snake_test', separator='-') == 'MySnakeTest'
    assert snake_case_to_camel('my-snake-test', separator='-') == 'MySnakeTest'
    assert snake_case_to_camel('mySnakes') == 'MySnakes'
    assert snake_case_to_camel('thisIsNotASnake') == 'ThisIsNotASnake'



# Generated at 2022-06-14 05:46:45.090179
# Unit test for function booleanize
def test_booleanize():
  assert booleanize("tRuE") == True
  assert booleanize("1") == True
  assert booleanize("YES") == True
  assert booleanize("Y") == True
  assert booleanize("nope") == False
test_booleanize()


# Generated at 2022-06-14 05:46:47.326175
# Unit test for function decompress
def test_decompress():
    assert __StringCompressor.decompress('eJxNj01PTc0yjSCAIBnAxJSU=', encoding='utf-8') == 'test string'



# Generated at 2022-06-14 05:46:58.737901
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert 'camel_case_to_snake' == camel_case_to_snake('camelCaseToSnake')
    assert 'camel_case_to_snake' == camel_case_to_snake('camel_case_to_snake')
    assert 'camel_case_to_snake' == camel_case_to_snake('CamelCaseToSnake')
    assert 'camel_case_to_snake' == camel_case_to_snake('CAMEL_CASE_TO_SNAKE')
    assert 'camel_case_to_snake' == camel_case_to_snake('camelCase to snake')
    assert 'camel_case_to_snake' == camel_case_to_snake('camel_case to snake')

# Generated at 2022-06-14 05:47:05.732562
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('this_is_a_snake_case_string_test') == 'ThisIsASnakeCaseStringTest'



# Generated at 2022-06-14 05:47:11.063239
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('thisIsACamelStringTest', '-') == 'this-is-a-camel-string-test'
    assert camel_case_to_snake('ThisIsACamelStringTest', '-') == 'this-is-a-camel-string-test'
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('thisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('ThisIsACamelStringTest', '-') == 'this-is-a-camel-string-test'

# Generated at 2022-06-14 05:47:18.409345
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    assert __StringFormatter('hello').input_string == "hello"
    assert __StringFormatter(' hello ').input_string == " hello "
    assert __StringFormatter('').input_string == ""
    assert __StringFormatter(' ').input_string == " "
    try:
        __StringFormatter(123)
        assert False
    except InvalidInputError:
        assert True
    try:
        __StringFormatter([])
        assert False
    except InvalidInputError:
        assert True
    try:
        __StringFormatter(None)
        assert False
    except InvalidInputError:
        assert True
