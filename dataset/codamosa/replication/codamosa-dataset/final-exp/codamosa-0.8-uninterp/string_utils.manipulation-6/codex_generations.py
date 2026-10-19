

# Generated at 2022-06-14 05:38:54.769182
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('A2B3C') == 'a2_b3_c'
    assert camel_case_to_snake('A2B3C', '-') == 'a2-b3-c'


# Generated at 2022-06-14 05:38:57.812862
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('Hello') == 'hello'
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('ThisIsACamelStringTest', '*') == 'this*is*a*camel*string*test'



# Generated at 2022-06-14 05:39:00.421520
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('thisIsACamelCaseStringTest') == 'this_is_a_camel_case_string_test'



# Generated at 2022-06-14 05:39:05.541906
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('thisIsACamelStringTest') == 'this_is_a_camel_string_test'



# Generated at 2022-06-14 05:39:11.125438
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'The-Snake-Is-Green'



# Generated at 2022-06-14 05:39:23.540840
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    out = __StringFormatter('Sunrise SunseT').format()
    assert out == 'Sunrise Sunset'

    out = __StringFormatter('Małgorzata     krok         wm').format()
    assert out == 'Małgorzata Krok WM'

    out = __StringFormatter('Hello hi').format()
    assert out == 'Hello Hi'

    out = __StringFormatter('Mr. Mrs.').format()
    assert out == 'Mr. Mrs.'

    out = __StringFormatter('mr mrs').format()
    assert out == 'Mr. Mrs.'

    out = __StringFormatter('mr. mrs.').format()
    assert out == 'Mr. Mrs.'

    out = __StringFormatter('Mr. mrs.').format()
    assert out == 'Mr. Mrs.'

    out = __String

# Generated at 2022-06-14 05:39:29.315299
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    print('Testing function snake_case_to_camel...')
    assert snake_case_to_camel('hello_world') == 'HelloWorld'
    assert snake_case_to_camel('hello_world', upper_case_first=False) == 'helloWorld'
    assert snake_case_to_camel('hello_world', separator='-') == 'HelloWorld'
    print('Passed.')



# Generated at 2022-06-14 05:39:31.572191
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('ThisIsACamelStringTest', '-') == 'this-is-a-camel-string-test'



# Generated at 2022-06-14 05:39:39.097407
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_case_string_test'
    assert camel_case_to_snake('this_is_a_snake_case_string') == 'this_is_a_snake_case_string'
    assert camel_case_to_snake('') == ''
    assert camel_case_to_snake('Test') == 'test'
    assert camel_case_to_snake('test') == 'test'



# Generated at 2022-06-14 05:39:41.283999
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'



# Generated at 2022-06-14 05:39:58.191897
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('one two three').format() == 'One two three'
    assert __StringFormatter('one-two-three').format() == 'One two three'
    assert __StringFormatter('one-two-three').format() == 'One two three'
    assert __StringFormatter('one two three').format() == 'One two three'
    assert __StringFormatter('This   is   just   an  example').format() == 'This is just an example'
    assert __StringFormatter('This  ,  is  ,  just  ,  an example').format() == 'This is just an example'
    assert __StringFormatter('This  ;  is  ;  just  ;  an example').format() == 'This is just an example'

# Generated at 2022-06-14 05:40:01.730951
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('hello_world') == 'HelloWorld'
    assert snake_case_to_camel('hello_world', upper_case_first=False) == 'helloWorld'



# Generated at 2022-06-14 05:40:14.588184
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', True) == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', True, '-') == 'The-Snake-Is-Green'
    assert snake_case_to_camel('the_snake_is_green', False, '-') == 'the-Snake-Is-Green'
    assert snake_case_to_camel('the-snake-is-green', True, '-') == 'The-Snake-Is-Green'
    assert snake

# Generated at 2022-06-14 05:40:21.733019
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # given
    sf = __StringFormatter('i hAvE  a cOuPLe of pRoblEmS   wIth   sPaces, dUplIcatEs, html & email@google.com')

    # when
    actual = sf.format()

    # then
    expected = 'I have a couple of problems with spaces, duplicates, html & email@google.com'
    assert actual == expected


# public API



# Generated at 2022-06-14 05:40:33.101162
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'the-snake-is-green'
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', separator='-', upper_case_first=False) == 'theSnakeIsGreen'



# Generated at 2022-06-14 05:40:36.955554
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('hello_world') == 'HelloWorld'
    assert snake_case_to_camel('hello_world', False) == 'helloWorld'
    assert snake_case_to_camel('hello-world', True, '-') == 'HelloWorld'



# Generated at 2022-06-14 05:40:50.291582
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('this is a text to prettify; as you can see, it has a lot of  duplicate   spaces  '
                             'and it could use a bit of formatting').format() == 'This is a text to prettify; as you ' \
                                                                               'can see, it has a lot of duplicate ' \
                                                                               'spaces and it could use a bit of ' \
                                                                               'formatting'

    assert __StringFormatter('sky is blue, moon is white. rain is cold').format() == 'Sky is blue, moon is white. ' \
                                                                                   'Rain is cold'


# Generated at 2022-06-14 05:41:02.046991
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:41:15.996963
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert 'ThisIsACamelString' == snake_case_to_camel('this_is_a_camel_string')
    assert 'ThisIsACamelString' == snake_case_to_camel('this_is_a_camel_string', True)
    assert 'thisIsACamelString' == snake_case_to_camel('this_is_a_camel_string', False)
    assert 'this::is:a:camel::string' == snake_case_to_camel('this::is:a:camel::string', False, ':')
    assert 'ThisIsACamelString' == snake_case_to_camel('this--is--a-camel--string', True, r'[-_\s]')

# Generated at 2022-06-14 05:41:27.162368
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('this_is_a_snake_string') == 'ThisIsASnakeString'
    assert snake_case_to_camel('this_is_a_snake_string', True, '-') == 'ThisIsASnakeString'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('this_snake_is_not_camel') == 'ThisSnakeIsNotCamel'
    assert snake_case_to_camel('this_snake_is_not_camel', False) == 'thisSnakeIsNotCamel'
    print ('Test function "snake_case_to_camel" passed successfully')
test_snake_case_to_camel()

# Generated at 2022-06-14 05:41:43.460271
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true')
    assert booleanize('True')
    assert booleanize('1')
    assert booleanize('TRUE')
    assert booleanize('yes')
    assert booleanize('YES')
    assert booleanize('y')
    assert booleanize('Y')
    assert not booleanize('false')
    assert not booleanize('False')
    assert not booleanize('0')
    assert not booleanize('FALSE')
    assert not booleanize('nope')
    assert not booleanize('NOPE')
    assert not booleanize('no')
    assert not booleanize('NO')
    assert not booleanize('random')
    assert not booleanize('123')
    assert not booleanize('seven')
    assert not booleanize('')
    assert not booleanize('  ')
    assert not booleanize(' \t')

# Generated at 2022-06-14 05:41:45.686589
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



# Generated at 2022-06-14 05:41:47.931675
# Unit test for function shuffle
def test_shuffle():
    expected_output = 'l wodheorll'
    actual_output = shuffle('hello world')
    assert actual_output == expected_output, 'Error: shuffle() should return "%s" but returned "%s" instead' % (
        expected_output,
        actual_output,
    )



# Generated at 2022-06-14 05:41:53.034998
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'
    assert asciify('abcd') == 'abcd'
    assert asciify('') == ''
    assert asciify('12345') == '12345'


# Generated at 2022-06-14 05:41:56.192274
# Unit test for function shuffle
def test_shuffle():
    # Arrange
    input_string = "hello world"
    expected_length = len(input_string)
    expected_number_of_chars = len(input_string.split(' '))
    # Act
    shuffled_string = shuffle(input_string)
    # # Assert
    assert is_full_string(shuffled_string)
    assert len(shuffled_string) == expected_length
    assert len(shuffled_string.split(' ')) == expected_number_of_chars
    assert shuffled_string != input_string
    test_shuffle()



# Generated at 2022-06-14 05:42:03.750950
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.encode(1) == 'I'
    assert __RomanNumbers.encode(2) == 'II'
    assert __RomanNumbers.encode(3) == 'III'
    assert __RomanNumbers.encode(5) == 'V'
    assert __RomanNumbers.encode(6) == 'VI'
    assert __RomanNumbers.encode(9) == 'IX'
    assert __RomanNumbers.encode(10) == 'X'
    assert __RomanNumbers.encode(20) == 'XX'
    assert __RomanNumbers.encode(40) == 'XL'
    assert __RomanNumbers.encode(50) == 'L'
    assert __RomanNumbers.encode(90) == 'XC'
    assert __RomanNumbers.encode(100) == 'C'

# Generated at 2022-06-14 05:42:17.611842
# Unit test for function prettify
def test_prettify():
    # strip empty strings
    assert prettify('') == ''
    # strip leading whitespace
    assert prettify(' foo') == 'foo'
    # strip trailing whitespace
    assert prettify('foo ') == 'foo'
    # strip leading and trailing whitespace
    assert prettify(' foo ') == 'foo'
    # strip leading newlines
    assert prettify('\nfoo') == 'foo'
    # strip trailing newlines
    assert prettify('foo\n') == 'foo'
    # strip leading and trailing newlines
    assert prettify('\nfoo\n') == 'foo'
    # strip consecutive whitespace
    assert prettify('foo    bar') == 'foo bar'
    # strip consecutive newlines
    assert prettify('foo\n\nbar') == 'foo bar'
    # correctly handle double quotes
   

# Generated at 2022-06-14 05:42:23.573548
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'



# Generated at 2022-06-14 05:42:27.037081
# Unit test for function compress
def test_compress():
    print('%0.20f' % time.time())
    n = 0 # <- ignore this, it's a fix for Pycharm (not fixable using ignore comments)
    # "original" will be a string with 169 chars:
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    print(original)
    # "compressed" will be a string of 88 chars
    compressed = compress(original)
    print(compressed)
    print('%0.20f' % time.time())
    assert len(compressed) < len(original)
    assert decompress(compressed, encoding='utf-8') == original

# Generated at 2022-06-14 05:42:35.279290
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('ThIsIsACamelStringTest') == 'th_is_is_a_camel_string_test'
    assert camel_case_to_snake('ThisIsACamelStringTest', separator='-') == 'this-is-a-camel-string-test'
    assert camel_case_to_snake('Test') == 'test'



# Generated at 2022-06-14 05:42:48.798868
# Unit test for function strip_margin
def test_strip_margin():
    assert strip_margin('''\
    line 1
    line 2
    line 3
    ''') == '''\
line 1
line 2
line 3
'''

    assert strip_margin('''\
    line 1
      line 2
    line 3
    ''') == '''\
line 1
  line 2
line 3
'''



# Generated at 2022-06-14 05:43:01.201784
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('this is just a string'                                                                                     ).format() == 'This Is Just A String'
    assert __StringFormatter('   this is just a string   '                                                                               ).format() == 'This Is Just A String'
    assert __StringFormatter('   this    is    just    a string   '                                                                      ).format() == 'This Is Just A String'
    assert __StringFormatter('this is  a very good email: name.surname@domain.com'                                                        ).format() == 'This Is A Very Good Email: name.surname@domain.com'

# Generated at 2022-06-14 05:43:08.377892
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():

    x = __RomanNumbers()
    assert (x.__mappings == [{1: 'I', 5: 'V'}, {1: 'X', 5: 'L'}, {1: 'C', 5: 'D'}, {1: 'M'}])
    assert(x.__reversed_mappings == [{'I': 1, 'V': 5}, {'X': 1, 'L': 5}, {'C': 1, 'D': 5}, {'M': 1}])
    assert(x.__encode_digit(1,2) == 'XX')
    assert (x.__encode_digit(1, 4) == 'XL')
    assert (x.__encode_digit(1, 9) == 'XC')
    assert(x.__index_for_sign('D') == 2)

# Generated at 2022-06-14 05:43:10.769867
# Unit test for function prettify
def test_prettify():
    input_string = " unprettified string ,, like this one,will be\"prettified\" .it\\' s awesome! "
    result="Unprettified string, like this one, will be \"prettified\". It\'s awesome!"
    assert result==prettify(input_string)

# unit test for function strip_html

# Generated at 2022-06-14 05:43:13.083945
# Unit test for function shuffle
def test_shuffle():
    assert shuffle('hello world') == 'hlleo dlorw'    # Possible output
    assert shuffle('hello world') != 'helo wrld'      # Another possible output
# test_shuffle



# Generated at 2022-06-14 05:43:17.478340
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    # test for encode method
    for number in range(1, 4000):
        assert number == __RomanNumbers.decode(__RomanNumbers.encode(number))

    # test for decode method
    for number in range(1, 4000):
        assert __RomanNumbers.encode(number) == __RomanNumbers.decode(__RomanNumbers.encode(number))


# PUBLIC API



# Generated at 2022-06-14 05:43:26.976285
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('<p>test</p><a href="foo/bar">click here</a>') == ''
    assert strip_html('<p>test</p><a href="foo/bar">click here</a>', True) == 'testclick here'
    assert strip_html('<p>test</p><a href="foo/bar">click here</a>', False) == ''
    assert strip_html('<p>test</p><a href="foo/bar">click here</a>', keep_tag_content=False) == ''



# Generated at 2022-06-14 05:43:31.874419
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    start = __StringCompressor()
    s = 'Hello this is a test string'
    c = start.compress(s)
    d = start.decompress(c)
    assert d == s
    print('The Unittesting with Html Compressor is passed')

# PUBLIC API



# Generated at 2022-06-14 05:43:38.167844
# Unit test for function reverse
def test_reverse():
    assert reverse('Hello') == 'olleH'
    assert reverse('hello') == 'olleh'
    assert reverse('hello world') == 'dlrow olleh'
    assert reverse('H') == 'H'
    assert reverse('H ') == ' H'



# Generated at 2022-06-14 05:43:47.257882
# Unit test for function reverse
def test_reverse():
    assert reverse('It works') == 'skrow tI', "reverse('It works') => 'skrow tI'"
    assert reverse('') == '', "reverse('') => ''"
    assert reverse('a') == 'a', "reverse('a') => 'a'"
    assert reverse('abc') == 'cba', "reverse('abc') => 'cba'"
    assert reverse('abcdefg') == 'gfedcba', "reverse('abcdefg') => 'gfedcba'"
    assert reverse('mO') == 'Om', "reverse('mO') => 'Om'"



# Generated at 2022-06-14 05:44:06.535981
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    input_string = '"lorem ipsum " dolor sit amet!  '

    s = __StringFormatter(input_string)

    assert s
    assert s.input_string == input_string


# Generated at 2022-06-14 05:44:18.015340
# Unit test for function slugify
def test_slugify():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'    
    assert slugify('Monster Magnet', separator=':') == 'monster:magnet'
    assert slugify('') == ''
    assert slugify('   ') == ''
    assert slugify('ABC123') == 'abc123'
    assert slugify('My    cat') == 'my-cat'
    assert slugify('My\tcat') == 'my-cat'
    assert slugify('a a') == 'a-a'

    
test_slugify()


# Generated at 2022-06-14 05:44:23.633973
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the-snake-is-green', True, '-') == 'TheSnakeIsGreen'



# Generated at 2022-06-14 05:44:27.095586
# Unit test for function prettify
def test_prettify():
    assert prettify(' unprettified string ,, like this one,will be"prettified" .'\
        'it\\\' s awesome! ') == 'Unprettified string, like this one, will be "prettified". It\'s awesome!'



# Generated at 2022-06-14 05:44:32.626086
# Unit test for function booleanize
def test_booleanize():
    assert booleanize("true") == True
    assert booleanize("True") == True
    assert booleanize("TRUE") == True
    assert booleanize("1") == True
    assert booleanize("yes") == True
    assert booleanize("Yes") == True
    assert booleanize("YES") == True
    assert booleanize("y") == True
    assert booleanize("Y") == True
    assert booleanize("nope") == False
    assert booleanize("Nope") == False
    assert booleanize("NOPE") == False
    assert booleanize("0") == False
    assert booleanize("NO") == False
    assert booleanize("no") == False
    assert booleanize("") == False
    assert booleanize(" ") == False
    assert booleanize("   ") == False
    assert booleanize("  true") == False
    assert booleanize

# Generated at 2022-06-14 05:44:41.607047
# Unit test for function booleanize

# Generated at 2022-06-14 05:44:55.123741
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    test_string = "Test String with spaces   inside       and    		outside"

    string_formatter = __StringFormatter(test_string)

    # test UPPERCASE_FIRST_LETTER
    assert string_formatter.__uppercase_first_char("test") == "Test"

    # test DUPLICATES
    assert string_formatter.__remove_duplicates("  ") == " "

    # test RIGHT_SPACE
    assert string_formatter.__ensure_right_space_only("   text") == " text "

    # test LEFT_SPACE
    assert string_formatter.__ensure_left_space_only("text   ") == " text "

    # test SPACES_AROUND

# Generated at 2022-06-14 05:45:05.345543
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') == True
    assert booleanize('false') == False
    assert booleanize('True') == True
    assert booleanize('False') == False
    assert booleanize('1') == True
    assert booleanize('0') == False
    assert booleanize('Yes') == True
    assert booleanize('No') == False
    assert booleanize('yes') == True
    assert booleanize('no') == False
    assert booleanize('y') == True
    assert booleanize('n') == False
test_booleanize()



# Generated at 2022-06-14 05:45:09.249049
# Unit test for function prettify

# Generated at 2022-06-14 05:45:13.449485
# Unit test for function shuffle
def test_shuffle():
    # assert that original string and shuffled one have different length
    assert shuffle('hello world') != 'hello world'

    # assert that each char of the original string can be found within the shuffled one
    for char in shuffle('hello world'):
        assert char in 'hello world'



# Generated at 2022-06-14 05:45:47.837605
# Unit test for function strip_margin
def test_strip_margin():
    test_string = '''
    line 1
    line 2
    line 3
    '''
    assert (strip_margin(test_string) == test_string.strip(''))



# Generated at 2022-06-14 05:45:50.175341
# Unit test for function reverse
def test_reverse():
    assert reverse('hello') == 'olleh', 'It should reverse chars.'
    assert reverse('') == '', 'It should reverse empty strings.'



# Generated at 2022-06-14 05:45:51.609168
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    out = __StringFormatter(1)
    assert out


# Generated at 2022-06-14 05:45:55.343016
# Unit test for function strip_margin
def test_strip_margin():
    text = '''
        line 1
        line 2
        line 3
    '''

    stripped = strip_margin(text)
    assert stripped == '''
line 1
line 2
line 3
    '''


# Generated at 2022-06-14 05:46:01.996580
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    assert __RomanNumbers.encode(3999) == 'MMMCMXCIX'
    assert __RomanNumbers.encode(3) == 'III'
    assert __RomanNumbers.encode(29) == 'XXIX'
    assert __RomanNumbers.encode(509) == 'DIX'

    assert __RomanNumbers.decode('MMMCMXCIX') == 3999
    assert __RomanNumbers.decode('III') == 3
    assert __RomanNumbers.decode('XXIX') == 29
    assert __RomanNumbers.decode('DIX') == 509

# public api



# Generated at 2022-06-14 05:46:07.453826
# Unit test for function slugify
def test_slugify():
    assert slugify(None) == ''
    assert slugify(' ') == ''
    assert slugify('!@#;') == ''
    assert slugify('test') == 'test'
    assert slugify('test:') == 'test'
    assert slugify('test: ') == 'test'
    assert slugify(' test: ') == ''
    assert slugify('   test: ') == ''
    assert slugify('test one') == 'test-one'
    assert slugify('test,one') == 'test-one'
    assert slugify('test-one') == 'test-one'
    assert slugify('test  one') == 'test-one'
    assert slugify('test one two') == 'test-one-two'
    assert slugify('test  one  two  ') == 'test-one-two'


# Generated at 2022-06-14 05:46:14.901215
# Unit test for function prettify
def test_prettify():
    test_run = __StringFormatter("unprettified string ,, like this one,will be\"prettified\".it\\' s awesome!")
    assert test_run.format() == "Unprettified string, like this one, will be \"prettified\". It's awesome!"
    print("The prettify method passed all tests!")

# Calling the test_prettify method
test_prettify()




# Generated at 2022-06-14 05:46:17.786931
# Unit test for function shuffle
def test_shuffle():
    assert len(shuffle('hello world')) == 11

if __name__ == '__main__':
    test_shuffle()
    exit()


# Generated at 2022-06-14 05:46:19.779947
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'



# Generated at 2022-06-14 05:46:22.889582
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'
    assert strip_html('<div><span>test</span></div>', keep_tag_content=True) == 'test'
    assert strip_html('<div><span>test</span></div>', keep_tag_content=False) == ''

