

# Generated at 2022-06-14 05:38:46.283484
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # todo: write unit tests
    pass



# Generated at 2022-06-14 05:38:52.763699
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('') == ''
    assert camel_case_to_snake('ThisIsACamelStringTest', '!') == 'this!is!a!camel!string!test'


# Generated at 2022-06-14 05:39:03.832992
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('i_am_a_snake', upper_case_first=False) == 'iAmASnake'
    assert snake_case_to_camel('i_am_a_snake', upper_case_first=True) == 'IAmASnake'
    assert snake_case_to_camel('i_am_a_snake', upper_case_first=True, separator='-') == 'IAmASnake'
    assert snake_case_to_camel('i_am_a_snake_too', upper_case_first=False) == 'iAmASnakeToo'
    assert snake_case_to_camel('i_am_a_snake_too', upper_case_first=True) == 'IAmASnakeToo'
    assert snake

# Generated at 2022-06-14 05:39:05.627536
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert 'test1_test2' == camel_case_to_snake('test1Test2')

# Generated at 2022-06-14 05:39:15.881919
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    import unittest

# Generated at 2022-06-14 05:39:26.000186
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('  a  b   c').format() == 'A B C'
    assert __StringFormatter('a  b  z z z z z z z c').format() == 'A B Z Z Z Z Z Z C'
    assert __StringFormatter('.a  b  z z z z z z z c').format() == '.A B Z Z Z Z Z Z C'
    assert __StringFormatter('a b z z z z z z c').format() == 'A B Z Z Z Z Z Z C'
    assert __StringFormatter('a b z z z z z z .c').format() == 'A B Z Z Z Z Z Z.C'
    assert __StringFormatter('a b z z z z z z.c').format() == 'A B Z Z Z Z Z Z.C'
    assert __StringForm

# Generated at 2022-06-14 05:39:33.687123
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_case_string_test'
    assert camel_case_to_snake('ThisIsACamelStringTest', '-') == 'this-is-a-camel-case-string-test'
    assert camel_case_to_snake('ThisIsACamelStringTest', ' ') == 'this is a camel case string test'



# Generated at 2022-06-14 05:39:40.824376
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('ThisIsACamelStringTest', '-') == 'this-is-a-camel-string-test'
    assert camel_case_to_snake('camelCaseString') == 'camel_case_string'
    assert camel_case_to_snake('CamelCaseString') == 'camel_case_string'
    assert camel_case_to_snake('thisIsACamelStringTest') == 'this_is_a_camel_string_test'



# Generated at 2022-06-14 05:39:52.399442
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('This  is a TEST!').format() == 'This is a test!'
    assert __StringFormatter('An Apple A Day Keeps The Doctor Away').format() == 'An apple a day keeps the doctor away'
    assert __StringFormatter('a_very_tiny_string').format() == 'A very tiny string'
    assert __StringFormatter(' a very tiny string ').format() == 'A very tiny string'
    assert __StringFormatter('a very_tiny string ').format() == 'A very tiny string'
    assert __StringFormatter('make it lower cased').format() == 'Make it lower cased'
    assert __StringFormatter('Make it upper cased').format() == 'Make it upper cased'
    assert __StringFormatter('A very tiny string.').format() == 'A very tiny string'
   

# Generated at 2022-06-14 05:40:04.572092
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake("Test") == "test"
    assert camel_case_to_snake("ThisIsACamelStringTest") == "this_is_a_camel_string_test"
    assert camel_case_to_snake("CamelCase") == "camel_case"
    assert camel_case_to_snake("CamelCaseJava") == "camel_case_java"
    assert camel_case_to_snake("ThisIsACamelStringTest") == "this_is_a_camel_string_test"
    assert camel_case_to_snake("ThisIsACamelStringTest") == "this_is_a_camel_string_test"
    assert camel_case_to_snake("CamelCase") == "camel_case"
    assert camel_case_to

# Generated at 2022-06-14 05:40:18.890402
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('ciao').format() == 'Ciao'
    assert __StringFormatter('abc def   ghi').format() == 'Abc def ghi'
    assert __StringFormatter('abcdefghi').format() == 'Abcdefghi'
    assert __StringFormatter('  abc def   ghi  ').format() == 'Abc def ghi'
    assert __StringFormatter('  abc  def   ghi  ').format() == 'Abc def ghi'
    assert __StringFormatter('  abc  def   ghi').format() == 'Abc def ghi'
    assert __StringFormatter('  abc  def   ghi  ').format() == 'Abc def ghi'

# Generated at 2022-06-14 05:40:31.600151
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    method = __StringFormatter.format
    #
    #     # invalid input
    #     inputs = [
    #         None,
    #         '',
    #         '    ',
    #         1234,
    #         True,
    #         [],
    #         {},
    #         object(),
    #     ]
    #     expected_outputs = itertools.repeat(None)
    #     assert len(list(inputs)) == len(list(expected_outputs))
    #     for o, e in zip(method(inputs), expected_outputs):
    #         assert o == e
    #
    #     # expected outputs
    #     inputs = [
    #         'test',
    #         'test test',
    #         'test test test',
    #         'test test test test

# Generated at 2022-06-14 05:40:44.117471
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter(' A   B   C  ').format() == 'A B C'
    assert __StringFormatter(' A B C ').format() == 'A B C'
    assert __StringFormatter(' A B C ').format() == 'A B C'
    assert __StringFormatter(' A  B  C  ').format() == 'A B C'
    assert __StringFormatter(' A  B C ').format() == 'A B C'
    assert __StringFormatter(' A  B  C  D  ').format() == 'A B C D'
    assert __StringFormatter(' A  B  C  D  ').format() == 'A B C D'
    assert __StringFormatter(' A  B  C  D  ').format() == 'A B C D'
    assert __StringFormatter

# Generated at 2022-06-14 05:40:53.292736
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('a b c').format() == 'A b c'
    assert __StringFormatter('a-b-c').format() == 'A-b-c'
    assert __StringFormatter('a-b-c d-e-f').format() == 'A-b-c d-e-f'
    assert __StringFormatter('a--b-c').format() == 'A-b c'
    assert __StringFormatter('a B c').format() == 'A B c'
    assert __StringFormatter('-a B c-').format() == 'A B c'
    assert __StringFormatter('A B C').format() == 'A B C'
    assert __StringFormatter('A B C D').format() == 'A B C D'

# Generated at 2022-06-14 05:41:03.237390
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert(__StringFormatter('marco  bellucci').format() == 'Marco Bellucci')
    assert(__StringFormatter('marco$bellucci').format() == 'Marco$Bellucci')
    assert(__StringFormatter('marco-bellucci').format() == 'Marco Bellucci')
    assert(__StringFormatter('marco bellucci').format() == 'Marco Bellucci')
    assert(__StringFormatter('Marco Bellucci').format() == 'Marco Bellucci')
    assert(__StringFormatter('MARCO BELLUCCI').format() == 'Marco Bellucci')
    assert(__StringFormatter('Marco-Bellucci').format() == 'Marco Bellucci')
    assert(__StringFormatter('Marco Bellucci').format() == 'Marco Bellucci')

# Generated at 2022-06-14 05:41:12.181744
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter(' a simple text ').format() == 'a simple text'
    assert __StringFormatter('a very very very very long text').format() == 'a very very very very long text'
    assert __StringFormatter('This is a PHP function: str_split()').format() == 'This is a PHP function: str_split()'

# Generated at 2022-06-14 05:41:24.545805
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    input = 'pelle pellepel'
    expected = 'Pelle pellepel'
    assert __StringFormatter(input).format() == expected

    input = 'Pelle pellegrossi'
    expected = 'Pelle pellegrossi'
    assert __StringFormatter(input).format() == expected

    input = 'Pelle   pellegrossi'
    expected = 'Pelle pellegrossi'
    assert __StringFormatter(input).format() == expected

    input = 'Pelle. pellegrossi'
    expected = 'Pelle. pellegrossi'
    assert __StringFormatter(input).format() == expected

    input = 'Pelle pellegrossi?'
    expected = 'Pelle pellegrossi?'
    assert __StringFormatter(input).format() == expected


# Generated at 2022-06-14 05:41:35.771411
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:41:45.405793
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:41:53.401529
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    s = __StringFormatter('  a  b   c   d e-mail@email.it    www.mysite.com  ')
    assert s.format() == 'A B C D e-mail@email.it www.mysite.com'

    s = __StringFormatter('a.   b.     c & d.')
    assert s.format() == 'A. B. C & D.'

    s = __StringFormatter('one  two/three,four;five six/seven')
    assert s.format() == 'One Two/Three,Four;Five Six/Seven'

    s = __StringFormatter('   www.mysite.com ')
    assert s.format() == 'www.mysite.com'

    s = __StringFormatter('https://www.mysite.com')
    assert s.format()

# Generated at 2022-06-14 05:41:58.569696
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    assert __StringFormatter("Test test  test test t") == "Test test test test t"

test___StringFormatter()


# PUBLIC API



# Generated at 2022-06-14 05:41:59.260287
# Unit test for function shuffle
def test_shuffle():
    assert 'l wodheorll' == shuffle('hello world')



# Generated at 2022-06-14 05:42:01.966763
# Unit test for function strip_html
def test_strip_html():
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '



# Generated at 2022-06-14 05:42:04.186540
# Unit test for function roman_decode
def test_roman_decode():
    assert roman_decode('VII') == 7
    assert roman_decode('') == 0

# Generated at 2022-06-14 05:42:17.667725
# Unit test for constructor of class __RomanNumbers
def test___RomanNumbers():
    # Simple test for mapping rules
    assert __RomanNumbers.encode('4') == 'IV'
    assert __RomanNumbers.encode('9') == 'IX'
    assert __RomanNumbers.encode('40') == 'XL'
    assert __RomanNumbers.encode('90') == 'XC'
    assert __RomanNumbers.encode('400') == 'CD'
    assert __RomanNumbers.encode('900') == 'CM'
    assert __RomanNumbers.encode('1954') == 'MCMLIV'
    assert __RomanNumbers.encode('1990') == 'MCMXC'
    assert __RomanNumbers.encode('2014') == 'MMXIV'

    assert __RomanNumbers.decode('IV') == 4
    assert __RomanNumbers.decode('IX') == 9
    assert __RomanNumbers.decode('XL')

# Generated at 2022-06-14 05:42:22.121249
# Unit test for function prettify

# Generated at 2022-06-14 05:42:25.763018
# Unit test for function shuffle
def test_shuffle():
    assert shuffle('hello') == 'olleh'
    assert shuffle('') == ''



# Generated at 2022-06-14 05:42:27.937390
# Unit test for function reverse
def test_reverse():
    assert reverse('hello') == 'olleh'


# Generated at 2022-06-14 05:42:30.055968
# Unit test for function shuffle
def test_shuffle():
    assert is_string(shuffle('hello world'))
    assert not shuffle('hello world') == 'hello world'



# Generated at 2022-06-14 05:42:43.459178
# Unit test for method format of class __StringFormatter