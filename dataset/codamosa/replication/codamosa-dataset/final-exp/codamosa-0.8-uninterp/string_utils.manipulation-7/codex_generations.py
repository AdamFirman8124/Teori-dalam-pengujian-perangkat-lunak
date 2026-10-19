

# Generated at 2022-06-14 05:39:02.592480
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert 'ThisIsTheString' == snake_case_to_camel('this_is_the_string')
    assert 'thisIsTheString' == snake_case_to_camel('this_is_the_string', upper_case_first=False)
    assert 'ThisIsTheString' == snake_case_to_camel('this.is.the.string', separator='.')
    assert 'ThisIsTheString' == snake_case_to_camel('this-is-the-string', separator='-')
    assert 'ThisIsTheString' == snake_case_to_camel('this is the string', separator=' ')
    assert 'ThisIsTheString' == snake_case_to_camel('this is the string', separator='  ')
    assert 'This is the string' == snake_case_to

# Generated at 2022-06-14 05:39:12.075017
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('hello_world') == 'HelloWorld'
    assert snake_case_to_camel('_hello_world', False) == '_helloWorld'
    assert snake_case_to_camel('hello_world_', upper_case_first=False) == 'helloWorld_'
    assert snake_case_to_camel('hello_   world_', upper_case_first=False) == 'helloWorld_'
    assert snake_case_to_camel('h_e_l_l_o___w_o_r_l_d', upper_case_first=False) == 'hELlOwORlD'

# Generated at 2022-06-14 05:39:24.136638
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:39:30.176850
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # single input
    input_string = 'SoMe% RaNdoM      StrinG with   Extra SPACES,\tduplicated \nletters  (aAaBbB) and @email'
    expected_output = 'Some Random String With Extra Spaces, Duplicated Letters (AaBb) And Email'
    assert __StringFormatter(input_string).format() == expected_output

    # multiple inputs

# Generated at 2022-06-14 05:39:33.378796
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('snake_case', upper_case_first=False, separator='-') == 'snakeCase'



# Generated at 2022-06-14 05:39:34.404246
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert 'TheSnakeIsGreen' == snake_case_to_camel('the_snake_is_green')



# Generated at 2022-06-14 05:39:44.240896
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():

    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the snake is green', True, ' ') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', upper_case_first=False, separator='-') == 'theSnakeIsGreen'

    assert snake_case_to_camel('this is not a snake string', True, ' ') == 'this is not a snake string'
    assert snake_case_to_camel('this is not a snake string') == 'This is not a snake string'



# Generated at 2022-06-14 05:39:51.061300
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:40:02.428665
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    # noinspection PyShadowingNames
    def assert_result(expected_result: str, input_string: str, upper_case_first: bool, separator: str):
        assert expected_result == snake_case_to_camel(input_string, upper_case_first, separator)

    assert_result('TheSnakeIsGreen', 'the_snake_is_green', True, '_')
    assert_result('theSnakeIsGreen', 'the_snake_is_green', False, '_')
    assert_result('TheSnakeIsGreen', 'the-snake-is-green', True, '-')
    assert_result('theSnakeIsGreen', 'the-snake-is-green', False, '-')



# Generated at 2022-06-14 05:40:15.074495
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('the-silliest_BAND in the world').format() == 'The Silliest Band In The World'
    assert __StringFormatter('the silliest band in the world').format() == 'The Silliest Band In The World'
    assert __StringFormatter('advice: something to consider').format() == 'Advice: Something To Consider'
    assert __StringFormatter('test@test.com').format() == 'test@test.com'
    assert __StringFormatter('http://www.test.com').format() == 'http://www.test.com'
    assert __StringFormatter('http://test.com').format() == 'http://test.com'
    assert __StringFormatter('https://test.com').format() == 'https://test.com'

# Generated at 2022-06-14 05:40:24.123029
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    input_string = 'prova di stringa di test'
    encoded = __StringCompressor.compress(input_string)
    decoded_bytes = __StringCompressor.decompress(encoded)

    assert decoded_bytes == input_string

# PUBLIC API



# Generated at 2022-06-14 05:40:25.865763
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('X') == 10

# Generated at 2022-06-14 05:40:31.373804
# Unit test for function slugify
def test_slugify():
    """
    Unit test for slugify function
    """
    slugs = [
        ('ThIs text will be slugified', 'this-text-will-be-slugified'),
        ('    spaces   ere     removed     too     ', 'spaces-ere-removed-too'),
        ('éèàöï', 'e-e-a-o-i'),
        ('', ''),
        ('this_is_a_custom_SEPARATOR', 'this-is-a-custom-separator'),
    ]

    for s, expected in slugs:
        actual = slugify(s)
        assert expected == actual, '\nExpected: "%s"\nActual: "%s"' % (expected, actual)



# Generated at 2022-06-14 05:40:41.557974
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_case_string_test'
    assert camel_case_to_snake('thisIsACamelStringTest') == 'this_is_a_camel_case_string_test'
    assert camel_case_to_snake('thisIsACamelStringTest', '-') == 'this-is-a-camel-case-string-test'
    assert camel_case_to_snake('isNotACamelString') == 'is_not_a_camel_string'

# Generated at 2022-06-14 05:40:46.692703
# Unit test for function shuffle
def test_shuffle():
    for i in range(1000):
        assert shuffle('abcdefghi') != 'abcdefghi'
        assert len(shuffle('abcdefghi')) == 9
# set test pass when test_shuffle return true
unittest.TestCase().assertTrue(test_shuffle())



# Generated at 2022-06-14 05:40:52.943082
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') == True
    assert booleanize('1') == True
    assert booleanize('yes') == True
    assert booleanize('y') == True
    assert booleanize('false') == False
    assert booleanize('0') == False
    assert booleanize('no') == False
    assert booleanize('n') == False
    assert booleanize('foobar') == False
    
    
# Main function

# Generated at 2022-06-14 05:40:53.627856
# Unit test for function shuffle
def test_shuffle():
    assert shuffle('hello world') != 'hello world'



# Generated at 2022-06-14 05:40:54.874525
# Unit test for function strip_margin
def test_strip_margin():
    example_str = '''
hello
world
'''
    expected_str = '''
hello
world
'''
    assert(expected_str == strip_margin(example_str))



# Generated at 2022-06-14 05:41:00.238827
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true')
    assert booleanize('1')
    assert booleanize('yes')
    assert booleanize('y')
    assert booleanize('True')
    assert booleanize('Y')
    assert not booleanize('nope')
    assert not booleanize('0')
    assert not booleanize('test')
    assert not booleanize('')
test_booleanize()



# Generated at 2022-06-14 05:41:03.206461
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'
    assert asciify('a') == 'a'



# Generated at 2022-06-14 05:41:19.923135
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    out = __StringFormatter('hello world').format()
    assert out == 'Hello world'

    out = __StringFormatter('hello world!!:)').format()
    assert out == 'Hello world!!:)'

    out = __StringFormatter('hello    world').format()
    assert out == 'Hello world'

    out = __StringFormatter('hello world--').format()
    assert out == 'Hello world--'

    out = __StringFormatter('hello--world').format()
    assert out == 'Hello world'

    out = __StringFormatter('HELLO WORLD').format()
    assert out == 'Hello world'

    out = __StringFormatter('helloWorld').format()
    assert out == 'Hello world'

    out = __StringFormatter(' helloWorld  ').format()
    assert out == 'Hello world'

    out

# Generated at 2022-06-14 05:41:29.325577
# Unit test for function slugify
def test_slugify():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
    assert slugify('òóü') == 'oo' # wrong translation
    assert slugify('òòóóüü') == 'ooo' # wrong translation
    assert slugify('òòóóüü', '_') == 'ooo' # wrong translation



# Generated at 2022-06-14 05:41:35.838280
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'
    assert asciify('hello world') == 'hello world'



# Generated at 2022-06-14 05:41:45.496211
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('snake') == 'Snake'
    assert snake_case_to_camel('snake', True) == 'Snake'
    assert snake_case_to_camel('_snake_') == 'Snake'
    assert snake_case_to_camel('snake_case_to_camel', True) == 'SnakeCaseToCamel'
    assert snake_case_to_camel('snake_case_to_camel', False) == 'snakeCaseToCamel'
    assert snake_case_to_camel('snake-case-to-camel') == 'SnakeCaseToCamel'
    assert snake_case_to_camel('snake_case_to_camel', separator='_') == 'SnakeCaseToCamel'
    assert snake_case_to_

# Generated at 2022-06-14 05:41:47.130213
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

# Generated at 2022-06-14 05:41:58.403604
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('this_is_not_a_snake_case') == 'This_is_not_a_snake_case'
    assert snake_case_to_camel('this-is-not-a-snake-case', separator='-') == 'This-is-not-a-snake-case'



# Generated at 2022-06-14 05:42:01.920962
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    import pytest
    with pytest.raises(InvalidInputError):
        __StringCompressor(5)
    assert __StringCompressor("5").input_string == "5"


# Generated at 2022-06-14 05:42:02.599123
# Unit test for function shuffle
def test_shuffle():
    assert shuffle('hello world') != 'hello world'



# Generated at 2022-06-14 05:42:05.833372
# Unit test for function decompress
def test_decompress():
    original = 'Some string'
    compressed = compress(original)
    assert decompress(compressed) == original, 'Compression/decompression failed'

# Unit tests for function compress

# Generated at 2022-06-14 05:42:18.843357
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    out = __StringFormatter('   mr.    Anthony   E.   Zuiker    ').format()
    assert 'Mr. Anthony E. Zuiker' == out

    out = __StringFormatter('  ``hello``    ').format()
    assert "``hello``" == out

    out = __StringFormatter('  I''m   a   $   ').format()
    assert "I'm a $" == out

    out = __StringFormatter('mrs.    Claire    L.  zuiker-foo').format()
    assert 'Mrs. Claire L. Zuiker-Foo' == out

    out = __StringFormatter('  http://www.hello.com  ').format()
    assert 'http://www.hello.com' == out


# Generated at 2022-06-14 05:42:30.832188
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    try:
        __StringCompressor()
        raise AssertionError(
            'Class must not allow direct instantiation'
        )
    except (TypeError, NameError):
        pass



# Generated at 2022-06-14 05:42:34.864978
# Unit test for function decompress
def test_decompress():
    """
    Unit test for function "decompress".
    """
    test_string = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(test_string)
    assert(decompress(compressed) == test_string)



# Generated at 2022-06-14 05:42:37.350604
# Unit test for function compress
def test_compress():
    # "original" will be a string with 169 chars:
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    # "compressed" will be a string of 88 chars
    compressed = compress(original)

    assert compressed is not None
    assert is_string(compressed)
    assert len(compressed) < len(original)
    assert __StringCompressor.decompress(compressed) == original



# Generated at 2022-06-14 05:42:40.778485
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'
test_strip_html()




# Generated at 2022-06-14 05:42:54.090348
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
    assert __RomanNumbers.encode(12) == 'XII'
    assert __Roman

# Generated at 2022-06-14 05:42:59.987768
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') == True
    assert booleanize('TRUE') == True
    assert booleanize('1') == True
    assert booleanize('yes') == True
    assert booleanize('y') == True
    assert booleanize('nope') == False
    assert booleanize('0') == False
    assert booleanize('false') == False

# Generated at 2022-06-14 05:43:01.698334
# Unit test for function decompress
def test_decompress():
    assert decompress('eJyLztP08zLzM3J1MLCpKLElw1BItTTJLEoDQ0MtPzQvyEJW8hvA0Mt/rckwJwE', encoding = 'utf-8') == 'atalavera'


# Generated at 2022-06-14 05:43:03.834650
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    assert __StringCompressor().compress('abc') == 'eJwFwQEBAAAAwL9PRDNPRDNPRDNPRDNPRDJ0MgAAAAB'
    

# Generated at 2022-06-14 05:43:08.745758
# Unit test for function shuffle
def test_shuffle():
    # we cannot predict the output, therefore we are going to try to predict the
    # outcome of the function based on its first char by assuming that the function is
    # correctly implemented
    s = 'hello'
    assert shuffle(s)[0] == random.choice(list(s))



# Generated at 2022-06-14 05:43:16.095845
# Unit test for function roman_decode
def test_roman_decode():
    assert(roman_decode('LXIV')==64)
    assert(roman_decode('CCCLXXXVII')==387)
    assert(roman_decode('VI')=='6')
    assert(roman_decode('MCCXXXVII')==1237)
    assert(roman_decode('M')==1000)

# Generated at 2022-06-14 05:43:33.540251
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'



# Generated at 2022-06-14 05:43:46.739314
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode(1) == "I"
    assert roman_encode(2) == "II"
    assert roman_encode(3) == "III"
    assert roman_encode(4) == "IV"
    assert roman_encode(5) == "V"
    assert roman_encode(12) == "XII"
    assert roman_encode(13) == "XIII"
    assert roman_encode(19) == "XIX"
    assert roman_encode(20) == "XX"
    assert roman_encode(22) == "XXII"
    assert roman_encode(39) == "XXXIX"
    assert roman_encode(40) == "XL"

# Generated at 2022-06-14 05:43:57.399351
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:44:06.014146
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') == True
    assert booleanize('false') == False
    assert booleanize('1') == True
    assert booleanize('2') == False
    assert booleanize('yes') == True
    assert booleanize('no') == False
    assert booleanize('y') == True
    assert booleanize('n') == False
    assert booleanize('string') == False
    assert booleanize('') == False
    assert booleanize('Tru') == False
    assert booleanize('1.0') == False
    assert booleanize('1.1') == False

# Generated at 2022-06-14 05:44:12.863630
# Unit test for function prettify
def test_prettify():
    s = ' unprettified string ,, like this one,will be"prettified" .it\\\' s awesome! '
    expected = 'Unprettified string, like this one, will be "prettified". It\'s awesome!'
    result = prettify(s)
    assert expected == result

test_prettify()



# Generated at 2022-06-14 05:44:15.848735
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'



# Generated at 2022-06-14 05:44:24.405794
# Unit test for function strip_html
def test_strip_html():
    input_str = '<p>Test</p>'
    output_str = strip_html(input_str)
    assert output_str == 'Test'
    input_str = '<p>Test</p><p><a href="foo/bar">click here</a></p>'
    output_str = strip_html(input_str)
    assert output_str == 'Testclick here'
    output_str = strip_html(input_str, keep_tag_content=True)
    assert output_str == 'Testclick here'
    input_str = 'Test<p>Test</p>Test'
    output_str = strip_html(input_str)
    assert output_str == 'TestTestTest'
    output_str = strip_html(input_str, keep_tag_content=True)
    assert output_

# Generated at 2022-06-14 05:44:28.677602
# Unit test for function decompress
def test_decompress():
    for i in range(1,503):
        y = compress(x)
        assert x == decompress(y)
        if i%50 == 0:
            print("done with {}".format(i))
            
if __name__ == '__main__':
    x = ''.join(str(i) for i in range(501))
    test_decompress()
    print("all tests successful")


# Generated at 2022-06-14 05:44:37.251052
# Unit test for function prettify
def test_prettify():
    print(prettify(' hello i\'m a (unprettified) string to be prettified. my  favourit color  is  blue 100 % '))
    print(prettify('Yes? Well, I am a mean, green mother from outer space'))
    print(prettify('hello world'))
    print(prettify('1 + 1'))
    print(prettify('a+ b'))
    print(prettify('a+b'))
    print(prettify('a +b'))
    print(prettify('a  +  b'))
    print(prettify('hello world'))
    print(prettify('hello world'))
    print(prettify('hello world'))
    print(prettify('hello world'))

# Generated at 2022-06-14 05:44:40.665590
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('ThisStringContainsNoCamel') == 'this_string_contains_no_camel'
    assert camel_case_to_snake('') == ''



# Generated at 2022-06-14 05:45:02.158680
# Unit test for function decompress
def test_decompress():
    assert decompress('ewogICAgImFhMiI6ICI3ZDQ2NDAwZWRjN2QiLAogICAgImFhMSI6ICI5ZjRiZWI1YmIwZjAxIgp9')=='{"aa2": "7d46400edc7d", "aa1": "9f4beb5bb0f0"}'

test_decompress()



# Generated at 2022-06-14 05:45:04.815860
# Unit test for function compress
def test_compress():
    n = 0 # <- ignore this, it's a fix for Pycharm (not fixable using ignore comments)
    # "original" will be a string with 169 chars:
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    # "compressed" will be a string of 88 chars
    compressed = compress(original)
    print(compressed)
    return



# Generated at 2022-06-14 05:45:14.509922
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    print('Test function "snake_case_to_camel"')

    # single test
    test_input = 'this_is_a_snake_case_test'
    expected_output = 'ThisIsASnakeCaseTest'
    output = snake_case_to_camel(test_input)

    assert output == expected_output, 'Invalid output for "{}": "{}" vs "{}"'.format(
        test_input, output, expected_output)

    # test with custom separator
    test_input = 'this-is-a-snake-case-test'
    expected_output = 'ThisIsASnakeCaseTest'
    output = snake_case_to_camel(test_input, separator='-')

# Generated at 2022-06-14 05:45:18.277275
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    result = camel_case_to_snake('ThisIsACamelStringTest')
    assert result == 'this_is_a_camel_string_test'



# Generated at 2022-06-14 05:45:25.201022
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('test_test_test') == 'TestTestTest'
    assert snake_case_to_camel('test_test_test', upper_case_first=False) == 'testTestTest'
    assert snake_case_to_camel('test_test_test', separator='-') == 'TestTestTest'
    assert snake_case_to_camel('test_test_test', separator='-', upper_case_first=False) == 'testTestTest'
    assert snake_case_to_camel('TestTestTest') == 'TestTestTest'
    assert snake_case_to_camel('TestTestTest', separator='-') == 'TestTestTest'

# Generated at 2022-06-14 05:45:28.905586
# Unit test for function strip_margin
def test_strip_margin():
    expected = r'line 1\nline 2'
    actual = strip_margin(r'    line 1\n    \tline 2')
    assert actual == expected


# Generated at 2022-06-14 05:45:42.429871
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'
    assert asciify('èùóáïñ') == 'euoain'
    assert asciify('ìåÜÞþÃã') == 'iUYTtAa'
    assert asciify('ÝÑÓÒÚÙÝÜØöõ') == 'YNOOUUYUo'
    assert asciify('ØþÞðÐÕÔ') == 'OtThdDO'
    assert asciify('ÓÒÖØÕÚÛÜÙÝÚ')

# Generated at 2022-06-14 05:45:46.644049
# Unit test for function prettify
def test_prettify():
    test = "  on"
    test2 = 'prefered'
    #test3 = "prettified."
    #test4 = "prettified? it's awesome!"
    #test5 = "prettified!it's awesome!"
    #test6 = "prettified:it's awesome!"
    test7 = "$ 5"
    test8 = "$ 5 %"
    test9 = "increase of 10%"
    test10 = "increase of 5 percent"
    test11 = "increase50%"
    test12 = "increase of: 50%"
    test13 = "increase of: 50 %"
    test14 = "increase (5%)"
    test15 = "increase (5 percent)"
    test16 = "increase (5 percent)"
    test17 = "increase (5 %)"
    test

# Generated at 2022-06-14 05:45:47.663069
# Unit test for function prettify
def test_prettify():
    # TODO: create unit tests
    pass



# Generated at 2022-06-14 05:45:52.152802
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('yes') == True, 'booleanize failed to convert "yes" to True'
    assert booleanize('y') == True, 'booleanize failed to convert "y" to True'
    assert booleanize('YES') == True, 'booleanize failed to convert "YES" to True'
    assert booleanize('True') == True, 'booleanize failed to convert "True" to True'
    assert booleanize('1') == True, 'booleanize failed to convert "1" to True'
    assert booleanize('no') == False, 'booleanize converted a non boolean value to True'
    assert booleanize('0') == False, 'booleanize converted a non boolean value to True'
    assert booleanize('false') == False, 'booleanize converted a non boolean value to True'


# Generated at 2022-06-14 05:46:07.385562
# Unit test for function compress
def test_compress():
    input_string = " ".join(["word n{}".format(n) for n in range(20)])
    assert len(input_string) == 169
    compressed = compress(input_string)
    assert len(compressed) == 88
    recovered = decompress(compressed)
    assert recovered == input_string


# Generated at 2022-06-14 05:46:15.228396
# Unit test for function strip_margin
def test_strip_margin():
    input_string = '''
    line 1 (with some leading spaces and tabs)
    line 2
    line 3
'''
    expected = '''
line 1 (with some leading spaces and tabs)
line 2
line 3
'''
    obtained = strip_margin(input_string)
    if expected != obtained:
        raise AssertionError('Expected: \n' + expected + ' but obtained: \n' + obtained)
test_strip_margin()

# Generated at 2022-06-14 05:46:17.787232
# Unit test for function shuffle
def test_shuffle():
    result = shuffle("hello world")
    assert shuffle("hello world")
    assert shuffles("hello world")
    return result
test_shuffle()


# Generated at 2022-06-14 05:46:26.495586
# Unit test for function decompress

# Generated at 2022-06-14 05:46:31.082679
# Unit test for function strip_html
def test_strip_html():
    s = 'test: <a href="foo/bar">click here</a>'
    assert strip_html(s) == 'test: '
    assert strip_html(s, keep_tag_content=True) == 'test: click here'



# Generated at 2022-06-14 05:46:33.511590
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    assert __StringCompressor.__name__ == '__StringCompressor'


# PUBLIC API



# Generated at 2022-06-14 05:46:40.530992
# Unit test for function compress
def test_compress():
    original = '''
    A quote by Aristotle:
    "It is the mark of an educated mind to be able to entertain a thought without accepting it."
    '''
    assert(len(original) == 177)
    compressed = compress(original)
    assert(len(compressed) == 25)
    assert(original == decompress(compressed))




# Generated at 2022-06-14 05:46:54.903469
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('I') == 1
    assert roman_decode('V') == 5
    assert roman_decode('X') == 10
    assert roman_decode('L') == 50
    assert roman_decode('C') == 100
    assert roman_decode('D') == 500
    assert roman_decode('M') == 1000
    assert roman_decode('VII') == 7
    assert roman_decode('VIII') == 8
    assert roman_decode('XV') == 15
    assert roman_decode('IV') == 4
    assert roman_decode('IX') == 9
    assert roman_decode('XL') == 40
    assert roman_decode('XC') == 90
    assert roman_decode('CD') == 400
   

# Generated at 2022-06-14 05:47:08.816960
# Unit test for function prettify
def test_prettify():
    input_string = ' unprettified string ,, like this one,will be"prettified" .it\\'
    assert prettify(input_string) == 'Unprettified string, like this one, will be "prettified". It\'s'
    input_string = 'unprettified string ,, like this one,will be"prettified" .it\\'
    assert prettify(input_string) == 'Unprettified string, like this one, will be "prettified". It\'s'
    input_string = 'unprettified string ,, like this one,will be"prettified" .it\\'
    assert prettify(input_string) == 'Unprettified string, like this one, will be "prettified". It\'s'

# Generated at 2022-06-14 05:47:10.558408
# Unit test for function decompress