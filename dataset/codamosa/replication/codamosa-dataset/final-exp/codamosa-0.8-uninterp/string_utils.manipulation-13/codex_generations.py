

# Generated at 2022-06-14 05:38:51.039462
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('Is_it_a_snake?', upper_case_first=True, separator='_') == 'IsItASnake?'
    assert snake_case_to_camel('the-snake-is-green', upper_case_first=True, separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', upper_case_first=False, separator='-') == 'theSnakeIsGreen'
    assert snake_case_to_camel

# Generated at 2022-06-14 05:39:02.824801
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('a_low_case_string') == 'ALowCaseString'
    assert snake_case_to_camel('a_low_case_string', False) == 'aLowCaseString'
    assert snake_case_to_camel('_not_a_snake_string_', separator='_') == '_not_a_snake_string_'
    assert snake_case_to_camel('string_without_separator') == 'StringWithoutSeparator'
    assert snake_case_to_camel('_string_without_separator', upper_case_first=False) == '_stringWithoutSeparator'
    assert snake_case_to_camel('only_one_string_token') == 'OnlyOneStringToken'

# Generated at 2022-06-14 05:39:09.175595
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('This string     has     too     many     spaces in  between').format() == 'This string has too many spaces in between'
    assert __StringFormatter('string with url http://www.google.com').format() == 'String with url http://www.google.com'
    assert __StringFormatter('Hello! @user! What do you think about Kevin from @googledevs?').format() == 'Hello @user! What do you think about Kevin from @googledevs?'
    assert __StringFormatter('This is a string with an email. Send an email to admin@google.com, he\'s waiting for you!').format() == 'This is a string with an email. Send an email to admin@google.com, he\'s waiting for you!'

# Generated at 2022-06-14 05:39:15.040983
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
  assert snake_case_to_camel("the_snake_is_here") == "TheSnakeIsHere"
  assert snake_case_to_camel("the_snake_is_here", False) == "theSnakeIsHere"
  assert snake_case_to_camel("the_snake_is_here", upper_case_first=False) == "theSnakeIsHere"
  assert snake_case_to_camel("the-snake-is-here")== "TheSnakeIsHere"
  assert snake_case_to_camel("the-snake-is-here", False) == "theSnakeIsHere"
  assert snake_case_to_camel("the-snake-is-here", upper_case_first=False) == "theSnakeIsHere"

# Generated at 2022-06-14 05:39:24.138390
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('12345') == '12345'
    assert snake_case_to_camel('12345', False) == '12345'
    assert snake_case_to_camel('12345', separator='-') == '12345'
    assert snake_case_to_camel('12345', False, '-') == '12345'



# Generated at 2022-06-14 05:39:32.514888
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    tests = [
        ('the_snake_is_green', True, '_', 'TheSnakeIsGreen'),
        ('the_snake_is_green', False, '_', 'theSnakeIsGreen'),
        ('the-snake-is-green', True, '-', 'TheSnakeIsGreen'),
        ('the-snake-is-green', False, '-', 'theSnakeIsGreen'),
        ('the snake is green', True, ' ', 'TheSnakeIsGreen'),
        ('the snake is green', False, ' ', 'theSnakeIsGreen'),
    ]

    for test in tests:
        t = test_snake_case_to_camel(*test[:3])
        assert t == test[3], f'Snake case to camel failed with test parameters: {test[:3]}'

test_snake_case_

# Generated at 2022-06-14 05:39:41.079322
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('this_is_a_snake') == 'ThisIsASnake'
    assert snake_case_to_camel('this_is_a_snake', upper_case_first=False) == 'thisIsASnake'
    assert snake_case_to_camel('this-is-a-snake', separator='-') == 'ThisIsASnake'
    assert snake_case_to_camel('this_is_a_snake', upper_case_first=False, separator='_') == 'thisIsASnake'



# Generated at 2022-06-14 05:39:47.657367
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'



# Generated at 2022-06-14 05:40:00.985310
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # arrange
    regexes = {
        'UPPERCASE_FIRST_LETTER': PRETTIFY_RE['UPPERCASE_FIRST_LETTER'],
        'DUPLICATES': PRETTIFY_RE['DUPLICATES'],
        'RIGHT_SPACE': PRETTIFY_RE['RIGHT_SPACE'],
        'LEFT_SPACE': PRETTIFY_RE['LEFT_SPACE'],
        'SPACES_AROUND': PRETTIFY_RE['SPACES_AROUND'],
        'SPACES_INSIDE': PRETTIFY_RE['SPACES_INSIDE'],
    }


# Generated at 2022-06-14 05:40:07.018784
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert 'Title' == snake_case_to_camel('title')
    assert 'Title' == snake_case_to_camel('Title')
    assert 'TitleTest' == snake_case_to_camel('title_test')
    assert 'SpecificTitle' == snake_case_to_camel('specific_title')



# Generated at 2022-06-14 05:40:13.539682
# Unit test for function compress
def test_compress():
    n = 0  # <- ignore this, it's a fix for Pycharm (not fixable using ignore comments)
    # "original" will be a string with 169 chars:
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    # "compressed" will be a string of 88 chars
    compressed = compress(original)
    assert original
    assert compressed


# Generated at 2022-06-14 05:40:19.427934
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'


# API for string compression (zlib + base64).

# Generated at 2022-06-14 05:40:23.529587
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('') is False
    assert booleanize('0') is False
    assert booleanize('False') is False
    assert booleanize('true') is True
    assert booleanize('1') is True
    assert booleanize('yes') is True
    assert booleanize('y') is True

# Generated at 2022-06-14 05:40:31.075772
# Unit test for function slugify
def test_slugify():
    # test string conversion
    assert slugify('Mönstér Mägnët') == 'monster-magnet'

    # test ascii conversion
    assert slugify('®') == 'r'

    # test JOIN sign
    assert slugify('a b c', '_') == 'a_b_c'

    # test removal of special characters
    assert slugify('...') == ''

    # test removal of non-ascii chars
    assert slugify('È') == ''

    # test removal of non-printable chars
    assert slugify('\n') == ''

    # test removal of leading and trailing spaces
    assert slugify('a') == 'a'

    # test lower case
    assert slugify('A') == 'a'

    # test removal of extra blank characters

# Generated at 2022-06-14 05:40:43.767493
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    # basic tests
    assert __RomanNumbers.encode(1) == 'I'
    assert __RomanNumbers.encode(5) == 'V'
    assert __RomanNumbers.encode(10) == 'X'
    assert __RomanNumbers.encode(50) == 'L'
    assert __RomanNumbers.encode(100) == 'C'
    assert __RomanNumbers.encode(500) == 'D'
    assert __RomanNumbers.encode(1000) == 'M'

    assert __RomanNumbers.decode('I') == 1
    assert __RomanNumbers.decode('V') == 5
    assert __RomanNumbers.decode('X') == 10
    assert __RomanNumbers.decode('L') == 50
    assert __RomanNumbers.decode('C') == 100

# Generated at 2022-06-14 05:40:52.952593
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.__encode_digit(0, 3) == 'III'
    assert __RomanNumbers.__encode_digit(1, 2) == 'XX'
    assert __RomanNumbers.__encode_digit(1, 5) == 'L'
    assert __RomanNumbers.__encode_digit(2, 1) == 'C'
    assert __RomanNumbers.__encode_digit(3, 1) == 'M'
    assert __RomanNumbers.__encode_digit(3, 2) == 'MM'
    assert __RomanNumbers.__encode_digit(1, 9) == 'XC'
    assert __RomanNumbers.__encode_digit(1, 4) == 'XL'
    assert __RomanNumbers.__encode_digit(1, 8) == 'LXXX'
    assert __RomanNumbers.__en

# Generated at 2022-06-14 05:40:56.606279
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    assert __StringFormatter('a') is not None
    try:
        __StringFormatter(1)
    except InvalidInputError as e:
        assert str(e) == '1 is not a string'


# Generated at 2022-06-14 05:41:08.373412
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
|line 2
|line 3''') == '''
line 1
line 2
line 3'''

    assert strip_margin('''
line 1
        |line 2
line 3
        |line 4''') == '''
line 1
|line 2
line 3
|line 4'''

    assert strip_margin('''
line 1
        |line 2
                |line 3
line 4
        |line 5
                |line 6''') == '''
line 1
|line 2
|line 3
line 4
|line 5
|line 6'''


# Generated at 2022-06-14 05:41:11.396817
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    assert __StringFormatter('test')
    try:
        __StringFormatter(123)
    except InvalidInputError:
        pass
    try:
        __StringFormatter([])
    except InvalidInputError:
        pass


# Generated at 2022-06-14 05:41:13.749783
# Unit test for function slugify
def test_slugify():
    if not (slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'):
        raise ValueError('Error in function slugify.')
    if not (slugify('Mönstér Mägnët') == 'monster-magnet'):
        raise ValueError('Error in function slugify.')
    print('Unit test for function slugify is completed')
######################################################################################################################

# Generated at 2022-06-14 05:41:19.687914
# Unit test for function slugify
def test_slugify():
    assert slugify('Some text here') == 'some-text-here'
    assert slugify('123456789') == '123456789'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs' 

# Generated at 2022-06-14 05:41:24.823178
# Unit test for function strip_margin
def test_strip_margin():
    multi_line_string = '''
    Hello world
    How are you
    '''
    assert strip_margin(multi_line_string) == '''
Hello world
How are you
'''



# Generated at 2022-06-14 05:41:28.475269
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    formatter = __StringFormatter(' en.wikipedia.org  test@test.com ')
    assert formatter.format() == 'En.wikipedia.org test@test.com'


# PUBLIC API



# Generated at 2022-06-14 05:41:35.045281
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    input_string = ' hello world ! '
    assert __StringFormatter(input_string).input_string == input_string
    try:
        __StringFormatter(None)
        assert False, 'Error expected with None input '
    except InvalidInputError:
        pass
    try:
        __StringFormatter(1)
        assert False, 'Error expected with None input '
    except InvalidInputError:
        pass


# Generated at 2022-06-14 05:41:43.572710
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') == True
    assert booleanize('1') == True
    assert booleanize('yes') == True
    assert booleanize('y') == True
    assert booleanize('True') == True
    assert booleanize('False') == False
    assert booleanize('false') == False
    assert booleanize('') == False
    assert booleanize(None) == False
    assert booleanize('uoauo') == False
    try:
        booleanize(1)
    except InvalidInputError:
        pass
    else:
        raise ValueError('stringutils.booleanize() did not raise error for invalid input')
            

# Generated at 2022-06-14 05:41:56.307666
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
    assert roman_encode(20) == 'XX'
    assert roman_encode(30) == 'XXX'
    assert roman_encode(40) == 'XL'
    assert r

# Generated at 2022-06-14 05:42:00.298471
# Unit test for function reverse
def test_reverse():
    assert reverse('lorem ipsum') == 'muspi merol'
    assert reverse('lorem1 ipsum2') == '2muspi 1merol'
    assert reverse('') == ''
    assert reverse(' ') == ' '
    assert reverse('123') == '321'
    assert reverse('hello') == 'olleh'


# Generated at 2022-06-14 05:42:10.656686
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    formatter = __StringFormatter('  s a lut     john   HOW   ARE   YOU ? ')
    assert formatter.format() == 'Salut John How Are You?'

    formatter = __StringFormatter('  s a lut     john   HOW   ARE   YOU ? ')
    assert formatter.format() == 'Salut John How Are You?'

    formatter = __StringFormatter('  s a lut     john   HOW   ARE   YOU ? ')
    assert formatter.format() == 'Salut John How Are You?'

    formatter = __StringFormatter('  s a lut     john   HOW   ARE   YOU ? ')
    assert formatter.format() == 'Salut John How Are You?'

    formatter = __StringFormatter('  s a lut     john   HOW   ARE   YOU ? ')
   

# Generated at 2022-06-14 05:42:11.913087
# Unit test for function decompress
def test_decompress():
    assert decompress(compress('abc')) == 'abc'



# Generated at 2022-06-14 05:42:24.796690
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:42:30.320856
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('VII') == 7

test_roman_decode()

# Generated at 2022-06-14 05:42:33.439490
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('ciao') == 'Ciao'

test_snake_case_to_camel()



# Generated at 2022-06-14 05:42:37.981181
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode(2019) == 'MMXIX'
    assert roman_encode(999) == 'CMXCIX'
    assert roman_encode('543') == 'DXLIII'
    assert roman_encode(13) == 'XIII'
    assert roman_encode('1') == 'I'
    assert roman_encode(3999) == 'MMMCMXCIX'



# Generated at 2022-06-14 05:42:42.297023
# Unit test for function strip_margin
def test_strip_margin():
    csv = strip_margin('''
                        line 1
                        line 2
                        line 3
                        ''')
    assert csv == '\nline 1\nline 2\nline 3'



# Generated at 2022-06-14 05:42:44.691569
# Unit test for function decompress
def test_decompress():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert(original == decompressed)
test_decompress()

# Generated at 2022-06-14 05:42:45.875323
# Unit test for function shuffle
def test_shuffle():
    assert shuffle('hello world') == 'l wodheorll'



# Generated at 2022-06-14 05:42:59.406551
# Unit test for function prettify
def test_prettify():

    # test prettify
    input_string = ' unprettified string ,, like this one,will be"prettified" .it\\'
    expected_string = prettify(input_string) + "'s awesome! "
    assert expected_string == 'Unprettified string, like this one, will be "prettified". It\'s awesome!'

    # test prettify edge case
    input_string = ' . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . '

# Generated at 2022-06-14 05:43:02.833326
# Unit test for function prettify

# Generated at 2022-06-14 05:43:04.237875
# Unit test for function prettify

# Generated at 2022-06-14 05:43:07.661978
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_case_string_test'



# Generated at 2022-06-14 05:43:12.312319
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') is True
    assert booleanize('1') is True
    assert booleanize('yes') is True
    assert booleanize('y') is True
    assert booleanize('True') is True
    assert booleanize('YES') is True
    assert booleanize('nope') is False
    assert booleanize('0') is False
    assert booleanize('not') is False
    assert booleanize('false') is False


# Generated at 2022-06-14 05:43:18.742411
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    rn = __RomanNumbers()
    assert rn.__mappings == [{1: 'I', 5: 'V'}, {1: 'X', 5: 'L'}, {1: 'C', 5: 'D'}, {1: 'M'}]
    assert rn.__reversed_mappings == [{'I': 1, 'V': 5}, {'X': 1, 'L': 5}, {'C': 1, 'D': 5}, {'M': 1}]
    assert rn.__encode_digit(3,4) == 'MMMV'


# PUBLIC API



# Generated at 2022-06-14 05:43:22.499335
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    assert __StringFormatter("").input_string == ""



# Generated at 2022-06-14 05:43:23.919810
# Unit test for function slugify
def test_slugify():
    input_string = 'Top 10 Reasons To Love Dogs!!!'
    result = 'top-10-reasons-to-love-dogs'
    assert (slugify(input_string) == result)
# test_slugify()



# Generated at 2022-06-14 05:43:27.401844
# Unit test for function shuffle
def test_shuffle():
    random.seed(1)
    assert shuffle('hello world') == 'lll lheworod'



# Generated at 2022-06-14 05:43:37.733628
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    test_class = __StringCompressor()

# Generated at 2022-06-14 05:43:43.750546
# Unit test for function prettify
def test_prettify():
    assert(prettify('hello  world ') == 'Hello world')
    assert(prettify('hello! world.') == 'Hello! World.')
    assert(prettify('hello,world') == 'Hello, world')
    assert(prettify('hello. world.') == 'Hello. World.')
    assert(prettify('hello, world') == 'Hello, world')
    assert(prettify('hello?world?') == 'Hello? World?')
    assert(prettify('hello? world?') == 'Hello? World?')
    assert(prettify('hello?  world?') == 'Hello? World?')
    assert(prettify(' hello? world? ') == 'Hello? World?')
    assert(prettify('hello world? ') == 'Hello world?')

# Generated at 2022-06-14 05:43:56.547456
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.encode(10) == 'X'
    assert __RomanNumbers.encode(9) == 'IX'
    assert __RomanNumbers.encode(13) == 'XIII'
    assert __RomanNumbers.encode(42) == 'XLII'
    assert __RomanNumbers.encode(90) == 'XC'
    assert __RomanNumbers.encode(99) == 'XCIX'
    assert __RomanNumbers.encode(14) == 'XIV'
    assert __RomanNumbers.encode(24) == 'XXIV'
    assert __RomanNumbers.encode(84) == 'LXXXIV'
    assert __RomanNumbers.encode(1974) == 'MCMLXXIV'
    assert __RomanNumbers.encode(3999) == 'MMMCMXCIX'


# Generated at 2022-06-14 05:44:07.226196
# Unit test for function roman_decode

# Generated at 2022-06-14 05:44:18.636580
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # init class
    formatter = __StringFormatter('  ')

    # test input data

# Generated at 2022-06-14 05:44:25.778554
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') == True
    assert booleanize('YES') == True
    assert booleanize('nope') == False
    assert booleanize('false') == False
    assert booleanize('False') == False

# Generated at 2022-06-14 05:44:27.295004
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode(37) == 'XXXVIII'


# Generated at 2022-06-14 05:44:31.981157
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
    assert strip_margin('''
                        this is a
                        test for strip_margin
                        function
                        ''') == '''
this is a
test for strip_margin
function
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

# a more complex test to be sure that indentation is removed only from the left margin
# and not from internal lines

# Generated at 2022-06-14 05:44:32.946394
# Unit test for function roman_encode
def test_roman_encode():
    return (roman_encode('37') == 'XXXVIII','roman_encode of 37 is XXXVIII')
    

# Generated at 2022-06-14 05:44:38.420832
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    test = __StringFormatter("  test  ")
    assert test.input_string == '  test  '
    assert test.__placeholder_key() == '$'+uuid4().hex+'$'


# Generated at 2022-06-14 05:44:40.635877
# Unit test for function reverse
def test_reverse():
    assert reverse('hello') == 'olleh'
    assert reverse('hello world') == 'dlrow olleh'



# Generated at 2022-06-14 05:44:54.895253
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    s = 'a' * 1000
    encoded = __StringCompressor.compress(s)
    decoded = __StringCompressor.decompress(encoded)

    assert s == decoded

    # test invalid input
    try:
        __StringCompressor.compress(None)
    except InvalidInputError:
        pass

    # test empty input
    try:
        __StringCompressor.compress('')
    except ValueError:
        pass

    # test invalid encoding
    try:
        __StringCompressor.compress('', encoding='notvalid')
    except ValueError:
        pass

    # test invalid compression level
    try:
        __StringCompressor.compress('', compression_level=9.1)
    except ValueError:
        pass



# PUBLIC API



# Generated at 2022-06-14 05:45:00.197811
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    sc = __StringCompressor()
    assert sc.compress('ab') == 'qLQ'
    assert sc.decompress('qLQ') == 'ab'

# PUBLIC API


# Generated at 2022-06-14 05:45:03.872428
# Unit test for function asciify
def test_asciify():
    assert(asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE')
    assert(asciify('⌘') == '')
    assert(asciify('アリ') == '')
    assert(asciify('@') == '@')
    assert(asciify('hällò') == 'hallo')
    assert(asciify('') == '')
    assert(asciify(None) == '')


# Generated at 2022-06-14 05:45:04.688033
# Unit test for function asciify
def test_asciify():
    assert asciify('aaaaaaaaaa') == 'aaaaaaaaaa'


# Generated at 2022-06-14 05:45:24.250630
# Unit test for function slugify
def test_slugify():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
    assert slugify('Foo$Bar') == 'foo-bar'
    assert slugify('Foo@Bar') == 'foo-bar'
    assert slugify('Foo?Bar') == 'foo-bar'
    assert slugify('ÈèÓóÒòÀàáÁÁÀàÈ') == 'eeoooaaoaaoaoaao'
test_slugify()



# Generated at 2022-06-14 05:45:35.217504
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():

    #
    # Helper
    #

    def try_compression_compatibility(input_string: str, encoding: str = 'utf-8', compression_level: int = 9):
        # compress_and_decompress returns the same string after compressing it then decompressing it.
        def compress_and_decompress(string: str):
            return __StringCompressor.decompress(__StringCompressor.compress(string, encoding, compression_level), encoding)

        # assert that compress-and-decompress returns the same string
        assert compress_and_decompress(input_string) == input_string

    #
    # Test the compress() method
    #

    # test for unicode strings
    try_compression_compatibility('@')

# Generated at 2022-06-14 05:45:38.712899
# Unit test for function strip_html
def test_strip_html():
    assert 'test: click here' == strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True)
    assert 'test: ' == strip_html('test: <a href="foo/bar">click here</a>')



# Generated at 2022-06-14 05:45:43.122273
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    # simple string conversion
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test', \
        'Camel case was not converted correctly'

    #
    assert camel_case_to_snake('ThisIsOtherTest', '|') == 'this|is|other|test', \
        'Camel case was not converted correctly'

    # invalid input strings
    assert camel_case_to_snake('thisIsNotACamelCase') == 'thisIsNotACamelCase', \
        'Invalid input should not be converted'

    assert camel_case_to_snake('this-Is-Not-A-CamelCase') == 'this-Is-Not-A-CamelCase', \
        'Invalid input should not be converted'

    assert camel_case_to_

# Generated at 2022-06-14 05:45:50.592031
# Unit test for function prettify
def test_prettify():
    inputs = [
        ' unprettified string ,, like this one,will be"prettified" .it\\' "s awesome! ",
        '100%',
        '100 %'
    ]
    expected = [
        'Unprettified string, like this one, will be "prettified". It\'s awesome!',
        '100%',
        '100%'
    ]
    for i, e in zip(inputs, expected):
        actual = prettify(i)
        assert actual == e
        print("Test OK")



# Generated at 2022-06-14 05:45:57.260920
# Unit test for function asciify
def test_asciify():
    result = asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË')
    # è -> e
    assert result.find('e') > 0
    # ë -> e
    assert result.find('e') > 0
    # eeuuooaaeynAAACIINOE
    assert result == 'eeuuooaaeynAAACIINOE'
    print('OK')

test_asciify()


# Generated at 2022-06-14 05:46:04.761654
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'
    assert strip_html('test: <a href="<b>foo</b>/<b>bar</b>">click <em>here</em></a>') == 'test: '
    assert strip_html('test: <a href="<b>foo</b>/<b>bar</b>">click <em>here</em></a>', keep_tag_content=True) == 'test: click here'

    assert strip_html('<a href="foo/bar">click here</a>') == ''

# Generated at 2022-06-14 05:46:14.682554
# Unit test for function reverse
def test_reverse():
    # positive tests
    assert reverse('hello') == 'olleh'
    assert reverse('\n') == '\n'
    assert reverse('\n\n') == '\n\n'

    # negative tests
    try:
        reverse('')
        assert False
    except Exception as e:
        assert type(e) is InvalidInputError

    try:
        reverse(1)
        assert False
    except Exception as e:
        assert type(e) is InvalidInputError

    try:
        reverse({})
        assert False
    except Exception as e:
        assert type(e) is InvalidInputError



# Generated at 2022-06-14 05:46:16.557357
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    formatter = __StringFormatter('hello')
    assert formatter is not None


# Generated at 2022-06-14 05:46:18.351885
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('VII') == 7



# Generated at 2022-06-14 05:46:27.283466
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    __StringCompressor.compress('Hello World')


# PUBLIC API



# Generated at 2022-06-14 05:46:30.078501
# Unit test for function decompress
def test_decompress():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    decompressed = decompress(compressed)
    if original == decompressed:
        print("Decompression OK")
    else:
        print("Decompression Failed")

# Generated at 2022-06-14 05:46:33.120539
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    assert __StringCompressor().__class__ == __StringCompressor

test___StringCompressor()


# PUBLIC API



# Generated at 2022-06-14 05:46:35.311083
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    sf = __StringFormatter("hello world")


# Generated at 2022-06-14 05:46:44.775930
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.__encode_digit(0, 1) == 'I'
    assert __RomanNumbers.__encode_digit(0, 2) == 'II'
    assert __RomanNumbers.__encode_digit(0, 3) == 'III'
    assert __RomanNumbers.__encode_digit(0, 4) == 'IV'
    assert __RomanNumbers.__encode_digit(0, 5) == 'V'
    assert __RomanNumbers.__encode_digit(0, 6) == 'VI'
    assert __RomanNumbers.__encode_digit(0, 7) == 'VII'
    assert __RomanNumbers.__encode_digit(0, 8) == 'VIII'
    assert __RomanNumbers.__encode_digit(0, 9) == 'IX'

    assert __RomanNumbers.__encode

# Generated at 2022-06-14 05:46:58.193149
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
    assert __RomanNumbers.encode(14) == 'XIV'
    assert __Roman

# Generated at 2022-06-14 05:46:59.277735
# Unit test for function reverse
def test_reverse():
    assert reverse('hello') == 'olleh'
# Test function end


# Generated at 2022-06-14 05:47:01.438703
# Unit test for function shuffle
def test_shuffle():
    assert shuffle('hello') == 'loleh' or shuffle('hello') == 'ohlel' or shuffle('hello') == 'ohlle'



# Generated at 2022-06-14 05:47:02.284674
# Unit test for function shuffle
def test_shuffle():
    assert shuffle(" ") == " "
    assert shuffle("") == ""


# Generated at 2022-06-14 05:47:03.882845
# Unit test for function shuffle
def test_shuffle():
    tests = [
        ['hello world', 'olleh dlorw'],
        ['6', '6']
    ]

    for t in tests:
        assert shuffle(t[0]) == t[1]



# Generated at 2022-06-14 05:47:23.042612
# Unit test for function roman_encode
def test_roman_encode():
    assert roman_encode(1) == 'I'
    assert roman_encode(5) == 'V'
    assert roman_encode(10) == 'X'
    assert roman_encode(100) == 'C'
    assert roman_encode(500) == 'D'
    assert roman_encode(1000) == 'M'
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode(38) == 'XXXVIII'
    assert roman_encode(39) == 'XXXIX'
    assert roman_encode(40) == 'XL'
    assert roman_encode(58) == 'LVIII'

# Generated at 2022-06-14 05:47:25.208588
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    assert __StringFormatter('hello') is not None



# Generated at 2022-06-14 05:47:28.426963
# Unit test for function decompress
def test_decompress():
    x = 'this is a test of compression'
    y = compress(x)
    z = decompress(y)
    assert z == x



# Generated at 2022-06-14 05:47:31.736878
# Unit test for function decompress
def test_decompress():
    original_str = 'my own test string'
    compressed_str = compress(original_str)
    decompressed_str = decompress(compressed_str)
    assert original_str == decompressed_str, "decompress() failed."



# Generated at 2022-06-14 05:47:34.964846
# Unit test for function strip_margin
def test_strip_margin():
    input_string = '''
        line 1
        line 2
        line 3
    '''
    expected_value = '''
line 1
line 2
line 3
'''
    assert strip_margin(input_string) == expected_value
    return



# Generated at 2022-06-14 05:47:37.624365
# Unit test for function compress
def test_compress():
    assert compress('prova', 'utf-8', 1) == 'eJzlLTsxKjEy0TApBCoA='


# Generated at 2022-06-14 05:47:41.174643
# Unit test for function compress
def test_compress():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    assert True

test_compress()


# Generated at 2022-06-14 05:47:50.341234
# Unit test for function roman_decode
def test_roman_decode():
    """
    Test function roman_decode(input_string)
    
    This function tests the function `roman_decode` on the following conditions:
    - Number is valid roman numeral
    - Number is not valid roman numeral
    - Number is an int
    
    
    If a test fails, an 'AssertionError' is raised and the test fails, otherwise the test passes
    """
    assert roman_decode('VII') == 7
    assert roman_decode('2020') == 0
    assert roman_decode(2020) == 0
test_roman_decode()



# Generated at 2022-06-14 05:47:57.967875
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('ThisIsACamelStringTest', separator='-') == 'this-is-a-camel-string-test'
    assert camel_case_to_snake('ThisIsACamelStringTest', separator='') == 'thisisacamelstringtest'



# Generated at 2022-06-14 05:48:06.896704
# Unit test for function slugify
def test_slugify():
    try:
        slugify(3)
        assert False, 'Invalid input (not a string): exception not raised'
    except Exception as e:
        if not isinstance(e, InvalidInputError):
            assert False, 'Invalid input (not a string): wrong exception ' + str(e)

    assert slugify('') == '', 'Invalid result for empty string'
    assert slugify('TEST') == 'test', 'Invalid result for uppercase string'
    assert slugify('Tes t') == 'tes-t', 'Invalid result for string with uppercase and spaces'
    assert slugify('Te St') == 'te-st', 'Invalid result for string with spaces'
    assert slugify('T10st-e') == 't10st-e', 'Invalid result for string with numbers and separators'