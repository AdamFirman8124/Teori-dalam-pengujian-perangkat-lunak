

# Generated at 2022-06-14 05:38:59.038974
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('Hello World!!').format() == 'Hello World', 'FAILED - test_prettify - Expected: Hello World'
    assert __StringFormatter('   Hello    World!!!     ').format() == 'Hello World', 'FAILED - test_prettify - Expected: Hello World'
    assert __StringFormatter('Hello  World!!!').format() == 'Hello World', 'FAILED - test_prettify - Expected: Hello World'
    assert __StringFormatter('Hello   World!!!').format() == 'Hello World', 'FAILED - test_prettify - Expected: Hello World'

# Generated at 2022-06-14 05:39:06.115910
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('THE_SNAKE_IS_GREEN') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False, separator='-') == 'theSnakeIsGreen'

# Generated at 2022-06-14 05:39:10.481217
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    sf = __StringFormatter('Hi ALLa, my name  is... Stefano!! with $x$ and https://www.dapgs.it/example/string and info@dapgs.it')
    assert sf.format() == 'Hi Alla, my name is Stefano! With $x$ and https://www.dapgs.it/example/string and info@dapgs.it'


# Generated at 2022-06-14 05:39:18.964888
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('this_is_a_snake_string') == 'ThisIsASnakeString'
    assert snake_case_to_camel('this_is_a_snake_string', upper_case_first=False) == 'thisIsASnakeString'
    assert snake_case_to_camel('THIS_IS_A_SNAKE_STRING', upper_case_first=False) == 'thisIsASnakeString'



# Generated at 2022-06-14 05:39:24.134312
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'The-Snake-Is-Green'



# Generated at 2022-06-14 05:39:29.501391
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'



# Generated at 2022-06-14 05:39:37.268833
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', True, '-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('not-a-valid-snake-case-string', True, '-') == 'not-a-valid-snake-case-string'



# Generated at 2022-06-14 05:39:50.317419
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('  asd  ASD@GMAIL.COM  ASD  ').format() == 'Asd asd@gmail.com Asd'
    assert __StringFormatter('a1-b-c d 2 - e').format() == 'A1 b c d 2 e'
    assert __StringFormatter('a 1-b-c d 2 - e').format() == 'A 1 b c d 2 e'
    assert __StringFormatter('a 1-b- c d 2 - e').format() == 'A 1 b c d 2 e'
    assert __StringFormatter('a 1-b -c d 2 - e').format() == 'A 1 b c d 2 e'
    assert __StringFormatter('a 1 -b - c d 2 - e').format() == 'A 1 b c d 2 e'
    assert __StringForm

# Generated at 2022-06-14 05:40:02.863807
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:40:04.241556
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    pass


# PUBLIC API



# Generated at 2022-06-14 05:40:10.962631
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'



# Generated at 2022-06-14 05:40:25.045233
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert 'HelloOneTest' == snake_case_to_camel('hello_one_test')
    assert 'HelloOneTest' == snake_case_to_camel('hello_one_test', True, '_')
    assert 'helloOneTest' == snake_case_to_camel('hello_one_test', False, '_')

    assert 'HelloOneTest' == snake_case_to_camel('hello-one-test', True, '-')
    assert 'helloOneTest' == snake_case_to_camel('hello-one-test', False, '-')

    assert 'HelloOneTest' == snake_case_to_camel('hello--one--test', True, '--')
    assert 'helloOneTest' == snake_case_to_camel('hello--one--test', False, '--')

   

# Generated at 2022-06-14 05:40:36.449263
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('') == ''
    assert snake_case_to_camel(' ') == ' '
    assert snake_case_to_camel(None) == None
    assert snake_case_to_camel('aBc') == 'aBc'
    assert snake_case_to_camel('a b c') == 'a b c'
    assert snake_case_to_camel(' a  b c ') == ' a  b c '
    assert snake_case_to_camel('abc', False) == 'abc'
    assert snake_case_to_camel('a_b_c') == 'ABc'
    assert snake_case_to_camel('a_b_c', False) == 'aBc'

# Generated at 2022-06-14 05:40:49.523975
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('') == ''
    assert snake_case_to_camel('a') == 'A'
    assert snake_case_to_camel('d') == 'D'
    assert snake_case_to_camel('a', upper_case_first=False) == 'a'
    assert snake_case_to_camel('a_b_c') == 'ABC'
    assert snake_case_to_camel('a_b_c', upper_case_first=False) == 'aBC'
    assert snake_case_to_camel('a__b', upper_case_first=False) == 'aB'
    assert snake_case_to_camel('a__b') == 'AB'

# Generated at 2022-06-14 05:41:01.967030
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('this_is_a_string_test', separator='_') == 'ThisIsAStringTest'
    assert snake_case_to_camel('thisIsAStringTest', separator='_', upper_case_first=False) == 'thisIsAStringTest'

# Generated at 2022-06-14 05:41:16.831232
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('') == ''
    assert snake_case_to_camel('123') == '123'
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('TheSnakeIsGreen') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('TheSnakeIsGreen', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the:snake:is:green', separator=':') == 'TheSnakeIsGreen'

# Generated at 2022-06-14 05:41:19.647342
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('a_simple_test') == 'ASimpleTest'



# Generated at 2022-06-14 05:41:31.993547
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('test_snake') == 'TestSnake'
    assert snake_case_to_camel('test_snake', upper_case_first=False) == 'testSnake'
    assert snake_case_to_camel('test_snake_to_camel', upper_case_first=False) == 'testSnakeToCamel'
    assert snake_case_to_camel('test_snake_to_camel', upper_case_first=False, separator='-') == 'test_snake_to_camel'
    assert snake_case_to_camel('test_string_with_number_1') == 'TestStringWithNumber1'



# Generated at 2022-06-14 05:41:38.921498
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert 'TheSnakeIsGreen' == snake_case_to_camel('the_snake_is_green')
    assert 'TheSnakeIsGreen' == snake_case_to_camel('the_snake_is_green', True)
    assert 'theSnakeIsGreen' == snake_case_to_camel('the_snake_is_green', False)
    # --- Invalid input ----
    assert 'TheSnakeIsGreen' == snake_case_to_camel('TheSnakeIsGreen')
    assert 'TheSnakeIsGreen' == snake_case_to_camel('TheSnakeIsGreen', False)



# Generated at 2022-06-14 05:41:45.880783
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('theSnakeIsGreen') == 'TheSnakeIsGreen'



# Generated at 2022-06-14 05:41:54.108932
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') == True
    assert booleanize('YES') == True
    assert booleanize('nope') == False
    assert booleanize('1') == True
    assert booleanize('0') == False
    
test_booleanize()



# Generated at 2022-06-14 05:42:00.020998
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

    assert strip_margin(' \t\tline 1\n \t\tline 2\n \t\tline 3') == 'line 1\nline 2\nline 3'



# Generated at 2022-06-14 05:42:03.374559
# Unit test for function decompress
def test_decompress():
    original = "This is a test"
    compressed = compress(original)
    assert original == decompress(compressed)

if __name__ == '__main__':
    test_decompress()


# Generated at 2022-06-14 05:42:07.430314
# Unit test for function camel_case_to_snake

# Generated at 2022-06-14 05:42:11.394890
# Unit test for function compress
def test_compress():
    """
    This function tests the result of function compress()
    """
    n = 0  # <- ignore this, it's a fix for Pycharm (not fixable using ignore comments)
    # "original" will be a string with 169 chars:
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    # "compressed" will be a string of 88 chars
    compressed = compress(original)
    assert compressed == 'eJwIykEKwjAMBdA79UY8EZTNX9n0P6o0l6AEe1aQ2LmbUfI2gOgrCW0cN/R56sfcAK9lg=', 'Failed to compress string'



# Generated at 2022-06-14 05:42:18.796594
# Unit test for function roman_encode
def test_roman_encode():
    try:
        print(roman_encode(37)) # returns 'XXXVIII'
        print(roman_encode('2020')) # returns 'MMXX'
        print(roman_encode(4000)) 
    except ValueError:
        print("ValueError")
    except Exception:
        print("InvalidInputError")
test_roman_encode()


# Generated at 2022-06-14 05:42:23.947891
# Unit test for function roman_encode

# Generated at 2022-06-14 05:42:34.389820
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.encode(20) == 'XX'
    assert __RomanNumbers.encode(2) == 'II'
    assert __RomanNumbers.encode(39) == 'XXXIX'
    assert __RomanNumbers.encode(3999) == 'MMMCMXCIX'
    assert __RomanNumbers.encode(35) == 'XXXV'

    assert __RomanNumbers.decode('XX') == 20
    assert __RomanNumbers.decode('II') == 2
    assert __RomanNumbers.decode('XXXIX') == 39
    assert __RomanNumbers.decode('MMMCMXCIX') == 3999
    assert __RomanNumbers.decode('XXXV') == 35


# PUBLIC API



# Generated at 2022-06-14 05:42:43.671381
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    # Compressed and decompressed versions of string should match
    original_string = "hello world! python rocks!"
    compressed_string = __StringCompressor.compress(original_string)
    assert __StringCompressor.decompress(compressed_string) == original_string

    # Test compression level to be raised by ValueError
    compression_level_out_of_range = 10
    test_failed = False
    try:
        __StringCompressor.compress(original_string, compression_level=compression_level_out_of_range)
    except ValueError:
        test_failed = True
    assert test_failed

    # Test encoding argument to be raised by ValueError
    encoding_not_string = 123
    test_failed = False

# Generated at 2022-06-14 05:42:49.239380
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
    assert roman_decode('X') == 10
    assert roman_decode('XI') == 11
    assert roman_decode('XIV') == 14
    assert roman_decode('XV') == 15
    assert roman_decode('XIX') == 19
    assert roman_decode('XX') == 20

# Generated at 2022-06-14 05:42:54.614887
# Unit test for function decompress
def test_decompress():
    for i in range(1, 1000):
        s = ' '.join(['word n{}'.format(n) for n in range(i)])
        compressed = compress(s)
        restored = decompress(compressed)
        if s != restored:
            raise Exception('Error testing decompress. Expected "{}" but got "{}"'.format(s, restored))


test_decompress()



# Generated at 2022-06-14 05:42:57.000802
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'
    assert asciify('Строка тест') == '---'
    assert asciify('My favoríte chars are ñÑáà') == 'My favor-te chars are naA'


# Generated at 2022-06-14 05:43:03.879845
# Unit test for function shuffle
def test_shuffle():

    # test normal execution with a string
    out = shuffle('ello world')
    assert is_string(out)
    assert out != 'ello world'
    assert len(out) == len('ello world')
    assert all([c in out for c in 'ello world'])

    # test that the function accepts an empty string
    out = shuffle('')
    assert is_string(out)
    assert out == ''

    # test that the function accepts a string with only spaces
    out = shuffle('    ')
    assert is_string(out)
    assert out == '    '



# Generated at 2022-06-14 05:43:06.913958
# Unit test for function strip_margin
def test_strip_margin():
    test_content='''
    line 1
    line 2
    line 3
    '''
    print(strip_margin(test_content))



# Generated at 2022-06-14 05:43:09.302779
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    result = __StringFormatter(input_string='input_string')
    assert(result.input_string == 'input_string')


# Generated at 2022-06-14 05:43:13.825021
# Unit test for function prettify

# Generated at 2022-06-14 05:43:27.419377
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('  a  ').format() == 'a'
    assert __StringFormatter('a b').format() == 'a b'
    assert __StringFormatter('a  b').format() == 'a b'
    assert __StringFormatter('a\nb').format() == 'a b'
    assert __StringFormatter('a\r\nb').format() == 'a b'
    assert __StringFormatter('a\r\n\r\nb').format() == 'a b'
    assert __StringFormatter('a\n\nb').format() == 'a b'
    assert __StringFormatter('a\n\n\nb').format() == 'a b'
    assert __StringFormatter('a\nb\nc').format() == 'a b c'

# Generated at 2022-06-14 05:43:35.286290
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('VII') == 7
    assert roman_decode('IX') == 9
    assert roman_decode('XV') == 15
    assert roman_decode('XX') == 20
    assert roman_decode('L') == 50
    assert roman_decode('C') == 100
    assert roman_decode('D') == 500
    assert roman_decode('M') == 1000
    assert roman_decode('MDCLXVIII') == 1668
    assert roman_decode('MMXIX') == 2019
    assert roman_decode('MMM') == 3000
    assert roman_decode('MMMCMXCIX') == 3999
    assert roman_decode('MMMM') == 0
    assert roman_decode('XIX') == 19



# Generated at 2022-06-14 05:43:39.312964
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode('') == None, "' ' should not be encoded"
    assert roman_encode('0') == None, "'0' should not be encoded"
    assert roman_encode('4000') == None, "'4000' should not be encoded"
    assert roman_encode('1') == 'I', "'1' should be encoded as 'I'"
    assert roman_encode('2') == 'II', "'2' should be encoded as 'II'"
    assert roman_encode('3') == 'III', "'3' should be encoded as 'III'"
    assert roman_encode('4') == 'IV', "'4' should be encoded as 'IV'"
    assert roman_encode('5') == 'V', "'5' should be encoded as 'V'"

# Generated at 2022-06-14 05:43:49.967904
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    test_cases = [
        ('', True, '_', ''),
        ('i_am_a_string', True, '_', 'IAmAString'),
        ('i_am_a_string', False, '_', 'iAmAString'),
        ('#i_am_a_string', False, '_', '#IAmAString'),
        ('#i_am_a_string', False, '#', 'iAmAString'),
    ]

    for test_case in test_cases:
        expected = test_case[3]
        actual = snake_case_to_camel(test_case[0], test_case[1], test_case[2])
        assert actual == expected



# Generated at 2022-06-14 05:43:58.752777
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test', 'should return the proper string'



# Generated at 2022-06-14 05:44:03.708536
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('') == ''
    assert strip_html('<p>Simple</p>') == ''
    assert strip_html('<p>Simple</p>', keep_tag_content=True) == 'Simple'



# Generated at 2022-06-14 05:44:06.641504
# Unit test for function shuffle
def test_shuffle():
    # loop test (it will be repeated 1000 times)
    for _ in range(1000):
        # we are going to use a random string (a random string will be generated every time)
        random_string = generate_random_string()

        # and we will check that every char in it is still present in the shuffled string
        for c in random_string:
            shuffled_string = shuffle(random_string)

            assert c in shuffled_string, "char {} not found in shuffled string {} (original: {})".format(c, shuffled_string, random_string)



# Generated at 2022-06-14 05:44:10.852512
# Unit test for function compress
def test_compress():
    assert compress(' '.join(['word n{}'.format(n) for n in range(20)])) == 'eJyNzRMKAzEMAN/FmfCSRhJmvPQyQNEbwQmYaAqbLJqPZ+XJZTpNhjJH8pN1SxSxw=='



# Generated at 2022-06-14 05:44:14.852689
# Unit test for function decompress
def test_decompress():
    n = 0 # <- ignore this, it's a fix for Pycharm (not fixable using ignore comments)
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert original == decompressed



# Generated at 2022-06-14 05:44:16.679564
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    assert __StringCompressor.__StringCompressor == __StringCompressor.__StringCompressor
    pass


# PUBLIC API



# Generated at 2022-06-14 05:44:25.778206
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode(0) == 'I'
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
    assert roman_encode(12) == 'XII'
   

# Generated at 2022-06-14 05:44:27.155347
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('VII') is 7
    return True

# Generated at 2022-06-14 05:44:31.015351
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true')
    assert booleanize('1')
    assert booleanize('yes')
    assert booleanize('y')
    assert not booleanize('false')
    assert not booleanize('0')
    assert not booleanize('no')
    assert not booleanize('n')
    assert not booleanize('')
    assert not booleanize(' ')
    assert not booleanize(None)
    assert not booleanize(1)
    assert not booleanize([])


# Generated at 2022-06-14 05:44:34.989711
# Unit test for function decompress
def test_decompress():
    expected = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(expected)
    decompressed = decompress(compressed)
    assert expected == decompressed

# Generated at 2022-06-14 05:44:55.944511
# Unit test for function compress
def test_compress():
    """
    This function implements the unit test for function compress.
    """

    # No value check (input_string = None):
    # Function must raise a ValueError
    try:
        compress(None)
    except ValueError:
        pass
    else:
        raise AssertionError('function should raise a ValueError if input_string is None')

    # No value check (input_string = int):
    # Function must raise a ValueError
    try:
        compress(1)
    except ValueError:
        pass
    else:
        raise AssertionError('function should raise a ValueError if input_string is an int')

    # No value check (input_string = float):
    # Function must raise a ValueError
    try:
        compress(1.0)
    except ValueError:
        pass

# Generated at 2022-06-14 05:45:00.783592
# Unit test for function prettify

# Generated at 2022-06-14 05:45:11.686181
# Unit test for function roman_encode
def test_roman_encode():
    print(roman_encode(9))
    print(roman_encode(12))
    print(roman_encode("1"))
    print(roman_encode("3"))
    print(roman_encode("5"))
    print(roman_encode("7"))
    print(roman_encode("8"))
    print(roman_encode("9"))
    print(roman_encode("10"))
    print(roman_encode("11"))
    print(roman_encode("14"))
    print(roman_encode("43"))
    print(roman_encode("99"))
    print(roman_encode("100"))
    print(roman_encode("123"))
    print(roman_encode("999"))
    print(roman_encode("1234"))
    print(roman_encode("3999"))

# Generated at 2022-06-14 05:45:14.876857
# Unit test for function slugify
def test_slugify():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
    return('test passed')



# Generated at 2022-06-14 05:45:22.710185
# Unit test for function strip_margin
def test_strip_margin():
    str = '''\
    |hello
    |
    |world/
    '''

    assert (strip_margin(str) == '''hello

world/\n''')

    str = '''\
    |hello world
    '''

    assert (strip_margin(str) == 'hello world')

    str = '''
    hello world
    '''

    assert (strip_margin(str) == 'hello world')



# Generated at 2022-06-14 05:45:29.725449
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    assert __StringCompressor.compress("shubham bhardwaj") == 'xLHMs5R5M5R5MOwB5c5R5M5R5M5R5M5ROwA=='
    assert __StringCompressor.decompress("xLHMs5R5M5R5MOwB5c5R5M5R5M5R5M5ROwA==") == 'shubham bhardwaj'


# PUBLIC API


# Generated at 2022-06-14 05:45:37.709659
# Unit test for function slugify
def test_slugify():

    input_string_1= 'Top 10 Reasons To Love Dogs!!!'
    out = slugify(input_string_1)
    assert out == 'top-10-reasons-to-love-dogs'

    input_string_2 = 'Mönstér Mägnët'
    out = slugify(input_string_2)
    assert out == 'monster-magnet'



# Generated at 2022-06-14 05:45:39.880896
# Unit test for function decompress
def test_decompress():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed_str = compress(original)
    decompressed_str = decompress(compressed_str)
    if original != decompressed_str:
        print("Test Failed")
    else:
        print("Test Passed")
test_decompress()


# Generated at 2022-06-14 05:45:42.689741
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('ThisIsACamelStringTest', '-') == 'this-is-a-camel-string-test'
    assert camel_case_to_snake('HelloWorld') == 'hello_world'
    assert camel_case_to_snake('HelloWorld', '-') == 'hello-world'



# Generated at 2022-06-14 05:45:52.609678
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('hello_world') == 'HelloWorld'
    assert snake_case_to_camel('hello_world', False) == 'helloWorld'
    assert snake_case_to_camel('hello_world', False, '-') == 'hello-world'
    assert snake_case_to_camel('the-snake-is-green', False, '-') == 'theSnakeIsGreen'

if __name__ == '__main__':
    test_snake_case_to_camel()
test_snake_case_to_camel()


# Generated at 2022-06-14 05:46:19.109761
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    # Initialize a string
    input_string = 'hello world'

    # Run compress method
    compressed_string = __StringCompressor.compress(input_string)

    # Run decompress method
    decompressed_string = __StringCompressor.decompress(compressed_string)

    # Check input string is same as decompressed_string
    assert(input_string == decompressed_string)

    print('Test of __StringCompressor class: Passed')


# PUBLIC API



# Generated at 2022-06-14 05:46:25.988355
# Unit test for function shuffle
def test_shuffle():
    chars_list = list(string.ascii_letters)
    random.shuffle(chars_list)
    random_string = "".join(chars_list)
    shuffle_string = shuffle(random_string)
    assert is_string(shuffle_string)
    assert shuffle_string != random_string



# Generated at 2022-06-14 05:46:33.391897
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    source = 'This is a test'
    compression_level = 5
    expected = 'This is a test'

    try:
        encoded = __StringCompressor.compress(source, compression_level=compression_level)
        decoded = __StringCompressor.decompress(encoded)
        assert decoded == expected
    except Exception as e:
        print(e)
        assert False

# PUBLIC API



# Generated at 2022-06-14 05:46:37.465122
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode(2020) == 'MMXX'
test_roman_encode()



# Generated at 2022-06-14 05:46:40.045452
# Unit test for function shuffle
def test_shuffle():
    assert shuffle('hello world') != 'hello world'
    assert shuffle('hello world') != 'world hello'



# Generated at 2022-06-14 05:46:47.753957
# Unit test for function prettify
def test_prettify():
    # Test 1
    input_string = ' unprettified string ,, like this one,will be"prettified" .it\\'
    correct_output = 'Unprettified string, like this one, will be "prettified". It\'s'
    assert prettify(input_string) == correct_output

    # Test 2
    input_string = 'this is "a small" test, to test prettify func: all(characters) are"prettified": OK!?'
    correct_output = 'This is "a small" test, to test prettify func: all(characters) are "prettified": OK?!'
    assert prettify(input_string) == correct_output

    # Test 3

# Generated at 2022-06-14 05:46:58.961619
# Unit test for function slugify
def test_slugify():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
    assert slugify('ÅØÆ') == 'aoe'
    assert slugify('Đầu nước, đầu đường, đầu tư, đầu tư') == 'dau-nuoc-dau-duong-dau-tu-dau-tu'

# Generated at 2022-06-14 05:47:00.845004
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode('37') == 'XXXVII'

# Generated at 2022-06-14 05:47:12.278143
# Unit test for function compress
def test_compress():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])

# Generated at 2022-06-14 05:47:14.017029
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    assert __StringFormatter('test')


# TESTING HELPERS


# Generated at 2022-06-14 05:48:02.876576
# Unit test for function compress
def test_compress():
    original = ''.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)

# Generated at 2022-06-14 05:48:09.734560
# Unit test for function compress
def test_compress():
    assert compress("ciao") == "eJxLc3M."
    assert compress("ciao ciao") == "eJxLc3M.OAw"
    assert compress("ciao\nciao") == "eJxLc3M.OAw"
    assert compress("ciao\nciao\nciao") == "eJxLc3M.OAw0AQ"

#----------------------------------------------------------------------

# Generated at 2022-06-14 05:48:11.781567
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'
    assert asciify('大丰') == ''


# Generated at 2022-06-14 05:48:15.667696
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

# Generated at 2022-06-14 05:48:20.806757
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    original_string = 'the quick brown fox jumps over the lazy dog'

    # compress original string
    compressed_string = __StringCompressor.compress(original_string)

    # decompress the compressed string to get back the original one
    decompressed_string = __StringCompressor.decompress(compressed_string)

    # assert that the decompressed string is equal to the original one
    assert decompressed_string == original_string


# PUBLIC API


# Generated at 2022-06-14 05:48:25.494286
# Unit test for function compress
def test_compress():
    # "original" will be a string with 169 chars:
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    # "compressed" will be a string of 88 chars
    compressed = compress(original)



# Generated at 2022-06-14 05:48:29.074926
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode(1) == 'I'
    assert roman_encode(3999) == 'MMMCMXCIX'
    assert roman_encode('3999') == 'MMMCMXCIX'
