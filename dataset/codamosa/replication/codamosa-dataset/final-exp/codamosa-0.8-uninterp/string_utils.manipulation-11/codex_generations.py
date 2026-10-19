

# Generated at 2022-06-14 05:38:53.895562
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert ('this_is_a_camel_case_string_test' == camel_case_to_snake('ThisIsACamelStringTest'))


# Generated at 2022-06-14 05:38:56.099494
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    # assert that a string is converted in a valid way
    assert camel_case_to_snake('thisIsACamelStringTest') == 'this_is_a_camel_string_test'



# Generated at 2022-06-14 05:38:57.398455
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('thisIsACamelStringTest') == 'this_is_a_camel_string_test'



# Generated at 2022-06-14 05:39:02.842442
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert (camel_case_to_snake('DataAccessObject') == 'data_access_object')
    assert (camel_case_to_snake('NoCamelCase') == 'no_camel_case')
    assert (camel_case_to_snake('ModuleName') == 'module_name')
    assert (camel_case_to_snake('DataSet') == 'data_set')

# Generated at 2022-06-14 05:39:09.201252
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    string_formatter = __StringFormatter('Lorem ipsum dolor . sit amet    , consectetur https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjwu_G-6bPWAhUBzIMKHdH6AqUQFggnMAA&url=https%3A%2F%2Fit.wikipedia.org%2Fwiki%2FOctopus_spiralis&usg=AOvVaw2iwmZYF_pKjB0eIN-T7TzT')

# Generated at 2022-06-14 05:39:22.502804
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('hello world').format() == 'Hello world'
    assert __StringFormatter(' hello world').format() == 'Hello world'
    assert __StringFormatter('hello world ').format() == 'Hello world'
    assert __StringFormatter('  hello world  ').format() == 'Hello world'
    assert __StringFormatter('hello  world').format() == 'Hello world'
    assert __StringFormatter('hello   world').format() == 'Hello world'
    assert __StringFormatter('hello.world').format() == 'Hello.World'
    assert __StringFormatter('hello.world.').format() == 'Hello.World.'
    assert __StringFormatter('hello/world').format() == 'Hello/World'
    assert __StringFormatter('hello/world/').format() == 'Hello/World/'

# Generated at 2022-06-14 05:39:31.911418
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:39:33.010162
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('@email.com').format() == '@email.com'



# Generated at 2022-06-14 05:39:34.071578
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    f = __StringFormatter('Hello World!')
    assert f.format() == 'Hello world!'



# Generated at 2022-06-14 05:39:36.211231
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'



# Generated at 2022-06-14 05:39:51.435226
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('').format() == ''
    assert __StringFormatter('    ').format() == ''
    assert __StringFormatter('this is the end').format() == 'this is the end'
    assert __StringFormatter('this is the end . . . . . . . . . . . . . . . . . . . . . . . . . ').format() == 'this is the end.'
    assert __StringFormatter('this is the end...').format() == 'this is the end...'
    assert __StringFormatter('this is the end. ').format() == 'this is the end.'
    assert __StringFormatter('this is the end.                                                                             ').format() == 'this is the end.'

# Generated at 2022-06-14 05:40:03.526968
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # Examples taken from https://en.wikipedia.org/wiki/Title_case
    assert __StringFormatter('this is a sentence that needs to be formatted').format() == 'This Is a Sentence That Needs to Be Formatted'
    assert __StringFormatter('This is another sentence that needs to be formatted').format() == 'This Is Another Sentence That Needs to Be Formatted'
    assert __StringFormatter('a third example').format() == 'A Third Example'
    assert __StringFormatter('a forth example, don\'t miss the comma').format() == 'A Forth Example, Don\'t Miss the Comma'
    assert __StringFormatter('a fifth example with some double spaces between words    here').format() == 'A Fifth Example With Some Double Spaces Between Words Here'

# Generated at 2022-06-14 05:40:11.303868
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('hello world').format() == 'Hello world'
    assert __StringFormatter('hello      world').format() == 'Hello world'
    assert __StringFormatter('hello, world').format() == 'Hello, world'
    assert __StringFormatter('hello,      world').format() == 'Hello, world'
    assert __StringFormatter('hello  world: hello,world').format() == 'Hello world: Hello, world'
    assert __StringFormatter('hello world,   hello , world: hello world').format() == 'Hello world, hello, world: Hello world'
    assert __StringFormatter('hello   world,hello,world:hello world').format() == 'Hello world, hello, world: Hello world'

# Generated at 2022-06-14 05:40:25.160470
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:40:36.517543
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    s = __StringFormatter('ciao,   mamma!')

    # Should be "Ciao, mamma!"
    r = s.format()

    assert r == 'Ciao, mamma!'

    s = __StringFormatter('  ciao,   mamma  mia!  ')

    # Should be "Ciao, mamma mia!"
    r = s.format()

    assert r == 'Ciao, mamma mia!'

    s = __StringFormatter('ciao, mamma mia!')

    # Should be "Ciao, mamma mia!"
    r = s.format()

    assert r == 'Ciao, mamma mia!'

    s = __StringFormatter('ciao,mamma/mia!')

    # Should be "Ciao, m

# Generated at 2022-06-14 05:40:49.656692
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('test').format() == 'Test'
    assert __StringFormatter('test, test.').format() == 'Test, test.'
    assert __StringFormatter('test, test .').format() == 'Test, test.'
    assert __StringFormatter('test, test . test-test').format() == 'Test, test. Test-test.'
    assert __StringFormatter('test, test . test-test.').format() == 'Test, test. Test-test.'
    assert __StringFormatter('test, test . test-test! test?').format() == 'Test, test. Test-test! Test?'
    assert __StringFormatter('test, test . test-test! test? test').format() == 'Test, test. Test-test! Test? Test.'

# Generated at 2022-06-14 05:41:01.966412
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:41:16.831743
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('a a').format() == 'a a'
    assert __StringFormatter(' a ').format() == 'a'
    assert __StringFormatter('a . a . a').format() == 'a. a. a.'
    assert __StringFormatter('a ,  a ,  a').format() == 'a, a, a'
    assert __StringFormatter('aaa @ aaa').format() == 'aaa@aaa'
    assert __StringFormatter('( a a a )').format() == '(a a a)'
    assert __StringFormatter('[ a a a ]').format() == '[a a a]'
    assert __StringFormatter('{ a a a }').format() == '{a a a}'
    assert __StringFormatter('< a a a >').format() == '<a a a>'
   

# Generated at 2022-06-14 05:41:27.772083
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():

    print("#############################")
    print("TESTING __StringFormatter_format")
    print("#############################")

    class __StringFormatter:
        def __init__(self, input_string):
            if not is_string(input_string):
                raise InvalidInputError(input_string)

            self.input_string = input_string

        def __uppercase_first_char(self, regex_match):
            return regex_match.group(0).upper()

        def __remove_duplicates(self, regex_match):
            return regex_match.group(1)[0]

        def __uppercase_first_letter_after_sign(self, regex_match):
            match = regex_match.group(1)
            return match[:-1] + match[2].upper()


# Generated at 2022-06-14 05:41:40.750519
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    formatter = __StringFormatter('Mr.  j. loney')
    assert formatter.format() == 'Mr. J. Loney'
    formatter = __StringFormatter('mr.  j. loney')
    assert formatter.format() == 'Mr. J. Loney'
    formatter = __StringFormatter('Mr.  J.   Loney')
    assert formatter.format() == 'Mr. J. Loney'
    formatter = __StringFormatter('Mr. J. - Loney')
    assert formatter.format() == 'Mr. J. - Loney'
    formatter = __StringFormatter('Mr.  j.   loney')
    assert formatter.format() == 'Mr. J. Loney'
    formatter = __StringFormatter('Mr.  j.   loney')

# Generated at 2022-06-14 05:42:01.360328
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    input_string = '  This    is a    test    '
    expected = 'This is a test'
    assert __StringFormatter(input_string).format() == expected

    input_string = '  This   is   a  test  of   the   method    '
    expected = 'This is a test of the method'
    assert __StringFormatter(input_string).format() == expected

    input_string = '  This   is  a   test   of   the   method  '
    expected = 'This is a test of the method'
    assert __StringFormatter(input_string).format() == expected

    input_string = '  This   is  a   test   of   the   method.  '
    expected = 'This is a test of the method.'
    assert __StringFormatter(input_string).format() == expected



# Generated at 2022-06-14 05:42:11.319939
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('  hello world!  ').format() == 'Hello world!'
    assert __StringFormatter('WhAt! ').format() == 'What!'
    assert __StringFormatter('This is a sentence. This is another one.   ').format() == 'This is a sentence. This is another one.'
    assert __StringFormatter('Don\'t tell me what to do! ').format() == 'Don\'t tell me what to do!'
    assert __StringFormatter('  don\'t tell me what to do! ').format() == 'Don\'t tell me what to do!'
    assert __StringFormatter('  Don\'t tell me what to do! ').format() == 'Don\'t tell me what to do!'

# Generated at 2022-06-14 05:42:24.247547
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    t = __StringFormatter('a pippo b')
    assert t.format() == 'A Pippo B'

    t = __StringFormatter('a   pippo      b')
    assert t.format() == 'A Pippo B'

    t = __StringFormatter('a pippo  b')
    assert t.format() == 'A Pippo B'

    t = __StringFormatter('a  pippo b')
    assert t.format() == 'A Pippo B'

    t = __StringFormatter('a  pippo   b')
    assert t.format() == 'A Pippo B'

    t = __StringFormatter('pippo  b  b bb')
    assert t.format() == 'Pippo B B B BB'

    t = __StringFormatter

# Generated at 2022-06-14 05:42:36.857206
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter("").format() == ""
    assert __StringFormatter("  ").format() == ""
    assert __StringFormatter("abracadabra").format() == "Abracadabra"
    assert __StringFormatter("abracadabra abracadabra").format() == "Abracadabra Abracadabra"
    assert __StringFormatter("abracadabra  abracadabra").format() == "Abracadabra Abracadabra"
    assert __StringFormatter("  abracadabra  abracadabra  ").format() == "Abracadabra Abracadabra"
    assert __StringFormatter("www.google.it").format() == "www.google.it"

# Generated at 2022-06-14 05:42:48.261529
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter(' mr. smith ').format() == 'Mr. Smith'
    assert __StringFormatter('Smith-Jones').format() == 'Smith-Jones'
    assert __StringFormatter('Smith-Jones AND Smith-Jackson').format() == 'Smith-Jones and Smith-Jackson'
    assert __StringFormatter('https://www.google.com').format() == 'https://www.google.com'
    assert __StringFormatter('http://www.google.com').format() == 'http://www.google.com'
    assert __StringFormatter('http://google.com').format() == 'http://google.com'
    assert __StringFormatter('www.google.com').format() == 'www.google.com'
    assert __StringFormatter('google.com').format() == 'google.com'
    assert __String

# Generated at 2022-06-14 05:43:00.868925
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    from .test_utils import assertEquals, assertIsNotNone

    assertIsNotNone(__StringFormatter.format)

    def test_uppercase_first_char(in_, out):
        assertEquals(__StringFormatter(in_).format(), out)

    def test_duplicates(in_, out):
        assertEquals(__StringFormatter(in_).format(), out)

    def test_right_space(in_, out):
        assertEquals(__StringFormatter(in_).format(), out)

    def test_left_space(in_, out):
        assertEquals(__StringFormatter(in_).format(), out)

    def test_spaces_around(in_, out):
        assertEquals(__StringFormatter(in_).format(), out)


# Generated at 2022-06-14 05:43:10.537210
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('toto  tata  ').format() == 'Toto tata'
    assert __StringFormatter('toto, tata').format() == 'Toto, tata'
    assert __StringFormatter('toto, tata,').format() == 'Toto, tata,'
    assert __StringFormatter('toto,   tata,').format() == 'Toto, tata,'
    assert __StringFormatter('toto,  "tata"').format() == 'Toto, "tata"'
    assert __StringFormatter('toto, tata. tata').format() == 'Toto, tata. Tata'
    assert __StringFormatter('toto, tata-tata').format() == 'Toto, tata-tata'

# Generated at 2022-06-14 05:43:17.198852
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    formatter = __StringFormatter(None)

    # creates a dummy formatter class for unit tests with both protected and protected methods
    # exposed as public ones
    class _UnitTestClass:
        def __init__(self, string_formatter):
            self.formatter = string_formatter

        def uppercase_first_char(self, regex_match):
            return self.formatter._StringFormatter__uppercase_first_char(regex_match)

        def remove_duplicates(self, regex_match):
            return self.formatter._StringFormatter__remove_duplicates(regex_match)

        def uppercase_first_letter_after_sign(self, regex_match):
            return self.formatter._StringFormatter__uppercase_first_letter_after_sign(regex_match)

# Generated at 2022-06-14 05:43:26.536134
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    from .string_utils import pretty_print
    from .string_utils import compress
    from .string_utils import decompress
    original_string = 'I\'m a little bee and this is my home-page : http://www.exam.ple/hello?name=marco'
    compressed_string = compress(original_string)
    decompressed_string = decompress(compressed_string)
    assert decompressed_string == original_string
    formatter = __StringFormatter(original_string)
    output = formatter.format()
    assert output == pretty_print(original_string)

# Generated at 2022-06-14 05:43:37.588383
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:44:17.300477
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    from .validation import assert_that
    from .validation import is_in

    assert_that('My home address is 123A, Some street, Any City',
                is_in(__StringFormatter.format('my home address is 123a. some street - any city!')))

    assert_that('Hello World', is_in(__StringFormatter.format('hello world')))
    assert_that('Hello World', is_in(__StringFormatter.format(' hello world ')))
    assert_that('Hello World', is_in(__StringFormatter.format('Hello world')))
    assert_that('Hello - World', is_in(__StringFormatter.format('Hello-World')))
    assert_that('Hello World', is_in(__StringFormatter.format('Hello   world')))

# Generated at 2022-06-14 05:44:19.405252
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    sf = __StringFormatter('   test   ')

    assert 'Test' == sf.format()



# Generated at 2022-06-14 05:44:32.159078
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:44:34.697380
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    from .testing import StringFormatterTestCase

    StringFormatterTestCase.test___StringFormatter_format()



# PUBLIC API



# Generated at 2022-06-14 05:44:42.595042
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('   hello   world,   how   are    you     ?   ').format() == 'Hello world, how are you?'
    assert __StringFormatter('hello world, how are you?').format() == 'Hello world, how are you?'
    assert __StringFormatter('   hello   world,   how   are you     ?   ').format() == 'Hello world, how are you?'
    assert __StringFormatter('hello world, how are you? ').format() == 'Hello world, how are you?'
    assert __StringFormatter('   hello   world,   how  are you     ?   ').format() == 'Hello world, how are you?'
    assert __StringFormatter('hello world, how are you?? ').format() == 'Hello world, how are you?'

# Generated at 2022-06-14 05:44:55.235188
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter(' test  string').format() == 'Test string'
    assert __StringFormatter('test string     ').format() == 'Test string'
    assert __StringFormatter('test :string').format() == 'Test: string'
    assert __StringFormatter('test  ?string').format() == 'Test? string'
    assert __StringFormatter('test.   string').format() == 'Test. string'
    assert __StringFormatter('test  &string').format() == 'Test & string'
    assert __StringFormatter('test  !string').format() == 'Test! string'
    assert __StringFormatter('test  \'string').format() == 'Test\' string'
    assert __StringFormatter('test  "string').format() == 'Test" string'
    assert __StringFormatter('test  %string').format()

# Generated at 2022-06-14 05:45:09.675939
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:45:20.719400
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('bla bla giò').format() == 'Bla bla giò'
    assert __StringFormatter('ciao').format() == 'Ciao'
    assert __StringFormatter('  ciao  ').format() == 'Ciao'
    assert __StringFormatter('  ciao  come  va ? ').format() == 'Ciao come va ?'
    assert __StringFormatter('  ciao  come  va ? bla . . . ').format() == 'Ciao come va ? Bla...'

# Generated at 2022-06-14 05:45:26.698579
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    def assert_format_result(input_string, expected):
        output = __StringFormatter(input_string).format()
        assert output is not None, "Output must not be null"
        assert is_string(output), "Output must be a string"
        assert output == expected, "Output [{}] must be [{}]".format(output, expected)

        # reverse input string to ensure that further formatting is idempotent
        reversed_output = __StringFormatter(reverse(output)).format()
        assert reversed_output == output, "Output [{}] must be [{}]".format(reversed_output, output)

    assert_format_result('hello world', 'Hello world')
    assert_format_result(' hello world ', 'Hello world')
    assert_format_result(' hello world     ', 'Hello world')
   

# Generated at 2022-06-14 05:45:36.144425
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # these tests are rather specific, I would move them to the unit test module
    assert __StringFormatter('test   case').format() == 'test case'
    assert __StringFormatter('SALES  &  MARKETING').format() == 'Sales & Marketing'
    assert __StringFormatter('sales & marketing').format() == 'Sales & Marketing'
    assert __StringFormatter('sales&marketing').format() == 'Sales & Marketing'
    assert __StringFormatter('sales &  MARKETING').format() == 'Sales & Marketing'
    assert __StringFormatter('sales&  marketing').format() == 'Sales & Marketing'
    assert __StringFormatter('sales & MARKETING').format() == 'Sales & Marketing'
    assert __StringFormatter('Sales & marketing').format() == 'Sales & Marketing'
    assert __String