

# Generated at 2022-06-14 05:39:02.944672
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:39:09.307967
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('a_b_c') == 'ABC'
    assert snake_case_to_camel('a_b_c', upper_case_first=False) == 'aBC'
    assert snake_case_to_camel('a-b-c', separator='-') == 'ABC'
    assert snake_case_to_camel('a_b_c', False, '_') == 'aBC'



# Generated at 2022-06-14 05:39:22.723021
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:39:28.035051
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('hello') == 'Hello'
    assert snake_case_to_camel('hello', upper_case_first=False) == 'hello'
    assert snake_case_to_camel('hello_this_is_a_test', upper_case_first=False) == 'helloThisIsATest'



# Generated at 2022-06-14 05:39:34.392542
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('this.That').format() == 'This. That'
    assert __StringFormatter('this... That').format() == 'This. That'
    assert __StringFormatter('this.that').format() == 'This. That'
    assert __StringFormatter('this (that)').format() == 'This (That)'
    assert __StringFormatter('this-[that]').format() == 'This-[That]'
    assert __StringFormatter('this [that]').format() == 'This [That]'
    assert __StringFormatter('this [ that]').format() == 'This [That]'
    assert __StringFormatter('this [that ]').format() == 'This [That]'
    assert __StringFormatter('this [ that ]').format() == 'This [That]'

# Generated at 2022-06-14 05:39:39.938600
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. nunc enim lacus, iaculis at quam eu, fermentum cursus nulla."
    s = s.replace(" ", "")

    print("Input:")
    print(s)

    # init the formatter
    formatter = __StringFormatter(s)
    output = formatter.format()

    print("Output:")
    print(output)


# PUBLIC API



# Generated at 2022-06-14 05:39:51.434506
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('this_is_a_test', upper_case_first=True) == 'ThisIsATest'
    assert snake_case_to_camel('this_is_a_test', upper_case_first=False) == 'thisIsATest'
    assert snake_case_to_camel('', upper_case_first=True) == ''
    # assert snake_case_to_camel('this_is_a_test', upper_case_first=None) == 'This_is_a_test' # not allowed
    assert snake_case_to_camel('this_is_a_test', separator='-') == 'This_is_a_test'

test_snake_case_to_camel()



# Generated at 2022-06-14 05:39:56.014591
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    #Arrange
    input_string = 'the_black_cat'
    expected_result = 'TheBlackCat'
    #Act
    result = snake_case_to_camel(input_string)
    #Assert
    assertEqual(expected_result,result)


# Generated at 2022-06-14 05:40:06.931210
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter(' a  b c.d-e f  ').format() == 'A b c.d-e f'
    assert __StringFormatter(' a  b c.d-e f  ').format() == 'A b c.d-e f'
    assert __StringFormatter(' a  b c.d-e f  ').format() == 'A b c.d-e f'

    assert __StringFormatter(' a  b c.d-e f  ').format() == 'A b c.d-e f'
    assert __StringFormatter(' a  b c.d-e f  ').format() == 'A b c.d-e f'
    assert __StringFormatter(' a  b c.d-e f  ').format() == 'A b c.d-e f'

   

# Generated at 2022-06-14 05:40:17.506105
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    tests = [
        ('the_snake_is_green', 'TheSnakeIsGreen'),
        ('the_snake_is_green', 'theSnakeIsGreen', False),
        ('the-snake-is-green', 'TheSnakeIsGreen', True, '-'),
        ('the-snake-is-green', 'theSnakeIsGreen', False, '-'),
        ('-the-snake-is-green-', 'TheSnakeIsGreen', True, '-'),
        ('-the-snake-is-green-', 'theSnakeIsGreen', False, '-'),
    ]
    for arg1, expected, *other in tests:
        result = snake_case_to_camel(arg1, *other)

# Generated at 2022-06-14 05:40:28.551335
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:40:42.271197
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    import pytest
    from .randomizer import random_string

    def random_input_string(length: int) -> str:
        s = ''
        for _ in range(length):
            s += random_string(10) + ' '
        return s

    def random_ascii_input_string() -> str:
        return random_input_string(10)

    def random_unicode_input_string() -> str:
        return random_input_string(10)

    def heavy_random_ascii_input_string() -> str:
        return random_input_string(50)

    def heavy_random_unicode_input_string() -> str:
        return random_input_string(50)


# Generated at 2022-06-14 05:40:52.242649
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('hello world').format() == 'Hello world'
    assert __StringFormatter('hello,world').format() == 'Hello world'
    assert __StringFormatter('hello, world').format() == 'Hello world'
    assert __StringFormatter('hello...world').format() == 'Hello world'
    assert __StringFormatter('hello. world').format() == 'Hello world'
    assert __StringFormatter('hello-world').format() == 'Hello world'
    assert __StringFormatter('hello - world').format() == 'Hello world'
    assert __StringFormatter('hello -world').format() == 'Hello world'
    assert __StringFormatter('hello[world').format() == 'Hello world'
    assert __StringFormatter('hello]world').format() == 'Hello world'

# Generated at 2022-06-14 05:41:02.675918
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:41:12.156101
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    string_formatter = __StringFormatter('<a href="https://www.google.com"> click here </a> to visit google')
    assert string_formatter.format() == '<a href="https://www.google.com">click here</a> to visit google'

    string_formatter = __StringFormatter('<a href="https://www.google.com"> click here </a> to visit google')
    assert string_formatter.format() == '<a href="https://www.google.com">click here</a> to visit google'

    string_formatter = __StringFormatter('<a href="https://www.google.com"> click here </a> to visit google')
    assert string_formatter.format() == '<a href="https://www.google.com">click here</a> to visit google'

   

# Generated at 2022-06-14 05:41:22.549149
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    f = __StringFormatter.format

    assert 'the quick brown fox jumps over the lazy dog.' == f('the    quick brown  fox  jumps over the lazy dog.')
    assert 'The quick brown fox jumps over the lazy dog.' == f('the quick brown fox jumps over the lazy dog.')
    assert 'The quick brown fox jumps over the lazy dog.' == f('the quick brown fox jumps over the lazy dog.   ')
    assert 'The Quick Brown Fox Jumps Over The Lazy Dog.' == f('the quick brown fox jumps over the lazy dog.    ')
    assert 'The Quick Brown Fox Jumps Over The Lazy Dog.' == f('The Quick Brown Fox Jumps Over The Lazy Dog.      ')
    assert 'Don\'t do that!' == f('don\'t do that!')

# Generated at 2022-06-14 05:41:34.622038
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('   hello').format() == 'Hello'
    assert __StringFormatter('I am a    test    string').format() == 'I am a test string'
    assert __StringFormatter('   hello   world   ').format() == 'Hello world'
    assert __StringFormatter('   hello   world.').format() == 'Hello world.'
    assert __StringFormatter('   hello   world,   ').format() == 'Hello world,'
    assert __StringFormatter('   hello   world;   ').format() == 'Hello world;'
    assert __StringFormatter('   hello   world:   ').format() == 'Hello world:'
    assert __StringFormatter('   hello   world!   ').format() == 'Hello world!'

# Generated at 2022-06-14 05:41:45.399192
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    f = __StringFormatter
    assert f('Hello,   World!! ').format() == 'Hello, World!'
    assert f('ciao.mamma@gmail.com').format() == 'ciao.mamma@gmail.com'
    assert f('https://www.google.com').format() == 'https://www.google.com'
    assert f('  a  lot  of  spaces  ').format() == 'a lot of spaces'
    assert f(' This  is  a  test  ').format() == 'This is a test'
    assert f('123.456,78').format() == '123.456,78'
    assert f('THIS is a test').format() == 'This is a test'
    assert f('A,B,C').format() == 'A, B, C'

# Generated at 2022-06-14 05:41:50.263394
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('my test:     one two Three,five ///// six seven;eight\nine').format() == \
           'My test: one two three, five // six seven; eight nine'


# PUBLIC API


# Generated at 2022-06-14 05:42:00.562238
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:42:12.114283
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:42:24.958007
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('    vanguard').format() == 'Vanguard'
    assert __StringFormatter(' vanguardk italia').format() == 'Vanguardk Italia'
    assert __StringFormatter('  vanguard').format() == 'Vanguard'
    assert __StringFormatter('vanguard ').format() == 'Vanguard'
    assert __StringFormatter('vanguard italia').format() == 'Vanguard Italia'
    assert __StringFormatter('Vanguard Italia').format() == 'Vanguard Italia'
    assert __StringFormatter('Vanguard Italia ').format() == 'Vanguard Italia'
    assert __StringFormatter('Vanguard Italia  ').format() == 'Vanguard Italia'
    assert __StringFormatter(' Vanguard Italia').format() == 'Vanguard Italia'
    assert __StringFormatter

# Generated at 2022-06-14 05:42:37.900485
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter(' foo bar ').format() == 'foo bar'
    assert __StringFormatter(' foo-bar ').format() == 'foo-bar'
    assert __StringFormatter('foo-bar  ').format() == 'foo-bar'
    assert __StringFormatter(' foo  bar ').format() == 'foo bar'
    assert __StringFormatter(' foo  bar ').format() == 'foo bar'
    assert __StringFormatter('https://www.github.com/motti-ai/').format() == 'https://www.github.com/motti-ai/'
    assert __StringFormatter(' foo,bar ').format() == 'foo, bar'
    assert __StringFormatter(' foo;bar ').format() == 'foo; bar'

# Generated at 2022-06-14 05:42:42.250295
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # given
    formatter = __StringFormatter("this is a test")
    # when
    result = formatter.format()
    # then
    assert result == "This is a test"

# Generated at 2022-06-14 05:42:45.302851
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    out = __StringFormatter('  foo BAr baz').format()
    assert out == 'Foo Bar Baz'


# PUBLIC API METHODS



# Generated at 2022-06-14 05:42:56.640791
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('this is a test').format() == 'This is a test'
    assert __StringFormatter('this is  a  test').format() == 'This is a test'
    assert __StringFormatter(' this is a test ').format() == 'This is a test'
    assert __StringFormatter(' this is a test ').format() == 'This is a test'
    assert __StringFormatter('   this   is   a   test   ').format() == 'This is a test'
    assert __StringFormatter('this is a test .').format() == 'This is a test.'
    assert __StringFormatter(' this is a test ,').format() == 'This is a test,'
    assert __StringFormatter(' this is a test ;').format() == 'This is a test;'

# Generated at 2022-06-14 05:43:05.762655
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:43:10.578717
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # Arrange
    out = __StringFormatter(
        "Hello, i'm  a  string and     i  am  pretty  ugly      and    i    have  some  errors!")
    # Act
    output = out.format()
    # Assert
    assert output == "Hello, I'm a string and I am pretty ugly and I have some errors!"


# Generated at 2022-06-14 05:43:17.226167
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('hello world').format() == 'Hello world'
    assert __StringFormatter('  hello  world   ').format() == 'Hello world'
    assert __StringFormatter('  "hello"  world   ').format() == '"Hello" world'
    assert __StringFormatter('  don\'t "hello"  world   ').format() == 'Don\'t "Hello" world'
    assert __StringFormatter('  "hello "  world   ').format() == '"Hello" world'
    assert __StringFormatter('  " hello "  world   ').format() == '"Hello" world'
    assert __StringFormatter('  hello"  world   ').format() == 'Hello" world'
    assert __StringFormatter('  hello "  world   ').format() == 'Hello "World"'
   

# Generated at 2022-06-14 05:43:22.361828
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    formatter = __StringFormatter('you are a good man, i am trusting you. yours, peter')
    output = formatter.format()
    print(output)
    assert output == 'You are a good man, I am trusting you. Yours, Peter'

    formatter = __StringFormatter('i\'m not a bad person, don\'t worry. i\'m not that bad')
    output = formatter.format()
    print(output)
    assert output == 'I\'m not a bad person, don\'t worry. I\'m not that bad'

    formatter = __StringFormatter('you are  a   good man. i\'m not so bad https://kuujinbo.github.io/i.html')
    output = formatter.format()
    print(output)

# Generated at 2022-06-14 05:43:35.286699
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # test 1
    assert __StringFormatter('says hello to you').format() == 'Says hello to you'

    # test 2
    assert __StringFormatter('Says hello to you').format() == 'Says hello to you'

    # test 3
    assert __StringFormatter('says  hello to you').format() == 'Says hello to you'

    # test 4
    assert __StringFormatter('hello to you says').format() == 'Hello to you says'

    # test 5
    assert __StringFormatter('Hello says hello to you says hello to you says hello to you says hello').format() == 'Hello says hello to you says hello to you says hello to you says hello'

    # test 6

# Generated at 2022-06-14 05:43:39.147623
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    formatter = __StringFormatter(' aBc def : 3 Ghi jKl mno pqr st. Abc def  1.23,45')
    return formatter.format()


# Generated at 2022-06-14 05:43:48.281578
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    formatter = __StringFormatter('hello "world"')
    assert formatter.format() == 'Hello world'

    formatter = __StringFormatter('this is a test "for the method __StringFormatter.format()"')
    assert formatter.format() == 'This is a test for the method __StringFormatter.format()'

    formatter = __StringFormatter('"this is a test" for the method __StringFormatter.format() "even with" duplicates')
    assert formatter.format() == 'This is a test for the method __StringFormatter.format() even with duplicates'

    formatter = __StringFormatter('ă î â ț ș')
    assert formatter.format() == 'ă î â ț ș'



# PUBLIC API



# Generated at 2022-06-14 05:44:01.849156
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('this is a test').format() == 'This is a test'
    assert __StringFormatter('this is a test, woah! a test').format() == 'This is a test, woah! A test'
    assert __StringFormatter('this is a test, woah! a test?').format() == 'This is a test, woah! A test?'
    assert __StringFormatter("this is a-test, woah! a test?").format() == 'This is a-test, woah! A test?'
    assert __StringFormatter("this is a test's").format() == "This is a test's"
    assert __StringFormatter("this is a test's'").format() == "This is a test's"

# Generated at 2022-06-14 05:44:13.161347
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    if PRETTIFY_RE['UPPERCASE_FIRST_LETTER'].search('abc def') is None:
        raise AssertionError('Prettify REGEX ERROR')

    if PRETTIFY_RE['SPACES_AROUND'].search('abc') is None:
        raise AssertionError('Prettify REGEX ERROR')

    assert __StringFormatter('abc             def   ').format() == 'Abc def'
    assert __StringFormatter('Abc             def   ').format() == 'Abc def'
    assert __StringFormatter('abcdef').format() == 'Abcdef'

# Generated at 2022-06-14 05:44:14.047463
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # TODO: implement this test
    pass



# Generated at 2022-06-14 05:44:21.699664
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    input_str = 'camelCase with spaces and duplicates'
    assert __StringFormatter(input_str).format() == 'Camelcase With Spaces And Duplicates'
    input_str = 'the quick   brown fox jumps over the lazy dog'
    assert __StringFormatter(input_str).format() == 'The Quick Brown Fox Jumps Over The Lazy Dog'
    assert __StringFormatter('foo@bar.it').format() == 'Foo@Bar.It'
    assert __StringFormatter('http://www.foo.bar/baz').format() == 'http://www.foo.Bar/Baz'
    assert __StringFormatter('http://www.foo.bar/baz/').format() == 'http://www.foo.Bar/Baz'

# Generated at 2022-06-14 05:44:33.818413
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('Hey World, I\'ve got a news for you!').format() == 'Hey World, I\'ve got a news for you!'
    assert __StringFormatter(
        'Hello my friend  how  are  you     today ?'
    ).format() == 'Hello my friend how are you today?'
    assert __StringFormatter('Umbrella Corp.').format() == 'Umbrella Corp.'
    assert __StringFormatter('Umbrella Corp. is in NY').format() == 'Umbrella Corp. is in NY'
    assert __StringFormatter('we@are.the.99percent').format() == 'we@are.the.99percent'
    assert __StringFormatter('http://www.google.com').format() == 'http://www.google.com'

# Generated at 2022-06-14 05:44:36.832576
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    s = __StringFormatter('MiChAeL  jAcKsOn@LIVE.IT')
    assert s.format() == 'Michael Jackson@live.it'



# Generated at 2022-06-14 05:44:46.591723
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('Hello2_World3_').format() == 'Hello 2 World 3'
    assert __StringFormatter('TEST_UPPER_CASE_SENTENCE').format() == 'Test upper case sentence'
    assert __StringFormatter('TEST1$2_uppercase_with_special_chars').format() == 'Test 1 $ 2 uppercase with special chars'
    assert __StringFormatter('Test_two_addresses_https://www.example.com/more/https://www.example2.com').format() == 'Test two addresses https://www.example.com/more/https://www.example2.com'
    assert __StringFormatter('Test_email_test@test.com_test2@test2.com').format() == 'Test email test@test.com test2@test2.com'



# Generated at 2022-06-14 05:44:55.673246
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'


# Generated at 2022-06-14 05:44:59.761415
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    assert __StringFormatter("this is a string") is not None
    assert __StringFormatter("ciao") is not None


# Generated at 2022-06-14 05:45:11.944539
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

# Generated at 2022-06-14 05:45:18.697970
# Unit test for function reverse
def test_reverse():
    assert reverse('hello') == 'olleh'
    try:
        reverse(None)
        assert False
    except InvalidInputError:
        pass
    try:
        reverse(5)
        assert False
    except InvalidInputError:
        pass



# Generated at 2022-06-14 05:45:30.288103
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('1') == True
    assert booleanize('TRUE') == True
    assert booleanize('yes') == True
    assert booleanize('Y') == True
# Test "prettify" function
from pystripe.string import prettify

assert prettify('a" b"c d e') == 'A "b" c d e'
assert prettify('a.1% b.2% c.3%') == 'A.1% b.2% c.3%'
assert prettify('a.1% b.2%.c\'s d') == 'A.1% b.2%. C\'s d'
assert prettify('a(b)c.d.e\'s f') == 'A (b) c. D. E\'s f'

# Generated at 2022-06-14 05:45:33.707202
# Unit test for function strip_margin
def test_strip_margin():
    m = '''
        |line 1
       |line 2
          |line 3
    '''.replace('|', ' ')

    expected = '''
    line 1
    line 2
    line 3
    '''

    assert strip_margin(m) == expected



# Generated at 2022-06-14 05:45:46.318923
# Unit test for constructor of class __RomanNumbers

# Generated at 2022-06-14 05:45:52.884583
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'
    assert asciify('a') == 'a'
    assert asciify('') == ''
    assert asciify(None) == 'None'

    try:
        asciify(33)
        assert False
    except InvalidInputError:
        pass



# Generated at 2022-06-14 05:45:58.370210
# Unit test for function roman_decode
def test_roman_decode():
    tests = [
        ('VII', 7),
        ('XXIV', 24),
        ('LXXXVII', 87),
        ('MMXX', 2020),
        ('MMXIX', 2019)
    ]
    for (input_string, expected_output) in tests:

        actual_output = roman_decode(input_string)
        print("actual_output: {}".format(actual_output))
        assert expected_output == actual_output, '{} != {}'.format(expected_output, actual_output)


# Generated at 2022-06-14 05:46:03.643037
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true')
    assert not booleanize('False')
    assert booleanize('1')
    assert booleanize('yes')
    assert booleanize('Y')
    assert not booleanize('0')
    assert not booleanize('no')
    assert not booleanize('N')

test_booleanize()
