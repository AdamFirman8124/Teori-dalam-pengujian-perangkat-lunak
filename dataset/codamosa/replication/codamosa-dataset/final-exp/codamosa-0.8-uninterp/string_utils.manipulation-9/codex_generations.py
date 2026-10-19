

# Generated at 2022-06-14 05:39:05.515041
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:39:15.636388
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    sf = __StringFormatter('giorgio boffa')
    assert sf.format() == 'Giorgio Boffa'

    sf = __StringFormatter('giorgio boffa e figli..')
    assert sf.format() == 'Giorgio Boffa e Figli.'

    sf = __StringFormatter('giorgio boffa  e  figli..')
    assert sf.format() == 'Giorgio Boffa e Figli.'

    sf = __StringFormatter('Giorgio. Boffa')
    assert sf.format() == 'Giorgio. Boffa'

    sf = __StringFormatter('Giorgio. Boffa. (i.e.  codice fiscale BOFFGIO11)')

# Generated at 2022-06-14 05:39:25.888628
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('manage-my-money').format() == 'Manage my Money'
    assert __StringFormatter('').format() == ''
    assert __StringFormatter('        ').format() == ''
    assert __StringFormatter('  hello  ').format() == 'Hello'
    assert __StringFormatter('many     spaces in   some words').format() == 'Many spaces in some words'
    assert __StringFormatter('hello  there').format() == 'Hello there'
    assert __StringFormatter('  hello  there ').format() == 'Hello there'
    assert __StringFormatter('how is it going?').format() == 'How is it going?'
    assert __StringFormatter('a great string with  (many)  internal spaces').format() == 'A great string with (many) internal spaces'
    assert __String

# Generated at 2022-06-14 05:39:29.685490
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    import pytest
    from .test_data import PRETTIFY_TEST_CASES

    for input_string, expected_output in PRETTIFY_TEST_CASES:
        assert __StringFormatter(input_string).format() == expected_output

# Generated at 2022-06-14 05:39:41.475026
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:39:49.959533
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    print('Testing __StringFormatter.format()...')


# Generated at 2022-06-14 05:40:02.627168
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('  hello   world   ').format() == 'Hello world'
    assert __StringFormatter('  hello  ,  world   ').format() == 'Hello, world'
    assert __StringFormatter('  hello   world,   ').format() == 'Hello world,'
    assert __StringFormatter('  hello   world   ,  ').format() == 'Hello world,'
    assert __StringFormatter('  hello   ,world   ').format() == 'Hello, world'
    assert __StringFormatter('  hello  ,world   ').format() == 'Hello, world'
    assert __StringFormatter('  hello  ,  world   ,  ').format() == 'Hello, world,'

# Generated at 2022-06-14 05:40:10.229079
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    s = __StringFormatter("Let's test it! (I'm sure it will work)")
    assert s.format() == "Let's test it! (I'm sure it will work)"
    s = __StringFormatter("Let's test a mistake: 'text with: |multiple| mistakes inside!' (I'm sure it will work)")
    assert s.format() == "Let's test a mistake: 'text with: |multiple| mistakes inside!' (I'm sure it will work)"
    s = __StringFormatter("Let's test a mistake: 'text with: |multiple| mistakes inside!' (I'm sure it will work)")
    assert s.format() == "Let's test a mistake: 'text with: |multiple| mistakes inside!' (I'm sure it will work)"

# Generated at 2022-06-14 05:40:23.902863
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():

    ut = __StringFormatter(' hello world')
    assert ut.format() == 'Hello world'

    ut = __StringFormatter(' hello world ')
    assert ut.format() == 'Hello world'

    ut = __StringFormatter(' hello world ,')
    assert ut.format() == 'Hello world,'

    ut = __StringFormatter(' hello world , ')
    assert ut.format() == 'Hello world,'

    ut = __StringFormatter(' hello world. ')
    assert ut.format() == 'Hello world.'

    ut = __StringFormatter(' hello world. hello world. ')
    assert ut.format() == 'Hello world. Hello world.'

    ut = __StringFormatter(' hello world. hello.world. ')
    assert ut.format() == 'Hello world. Hello.world.'

    ut = __StringFormatter

# Generated at 2022-06-14 05:40:35.257347
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():

    formatter = __StringFormatter("some_string with spaces   and$mixed$case")
    assert formatter.format() == 'Some string with spaces and$mixed$case'

    formatter = __StringFormatter("some_string with spaces   and$mixed$case")
    assert formatter.format() == 'Some string with spaces and$mixed$case'

    formatter = __StringFormatter("some_string with spaces   and$mixed$case")
    assert formatter.format() == 'Some string with spaces and$mixed$case'

    formatter = __StringFormatter("some_string with spaces   and$mixed$case")
    assert formatter.format() == 'Some string with spaces and$mixed$case'

    formatter = __StringFormatter("some_string with spaces   and$mixed$case")


# Generated at 2022-06-14 05:41:00.453868
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('I will do it, ok ?').format() == 'I will do it, ok?'
    assert __StringFormatter('1st place,  just 1').format() == '1st place, just 1'
    assert __StringFormatter('joe@mail.com').format() == 'joe@mail.com'
    assert __StringFormatter('https://www.google.com').format() == 'https://www.google.com'
    assert __StringFormatter('1st place,  just 1 joe@mail.com https://www.google.com').format() == '1st place, just 1 joe@mail.com https://www.google.com'



# Generated at 2022-06-14 05:41:15.075583
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter(' a b c').format() == 'A B C', 'Failed to uppercase first letter'
    assert __StringFormatter('a b b').format() == 'A B', 'Failed to remove duplicate'
    assert __StringFormatter('a b c-d').format() == 'A B C-D', 'Failed to uppercase first letter after signs'
    assert __StringFormatter('a b c').format() == 'A B C', 'Failed to add right space only'
    assert __StringFormatter('a b c ').format() == 'A B C', 'Failed to remove extra right space'
    assert __StringFormatter(' a b c').format() == 'A B C', 'Failed to add left space only'

# Generated at 2022-06-14 05:41:20.523251
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    input_string = '  https://www.google.it/ A_TEST_STRING_FOR_TESTING_PURPOSES  '

    output_string = __StringFormatter(input_string).format()

    assert output_string == 'https://www.google.it/ a test string for testing purposes'



# Generated at 2022-06-14 05:41:27.653565
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:41:31.234250
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    input_string = ' hello - WORLD, this '
    expected_string = 'Hello world, this'

    assert __StringFormatter(input_string).format() == expected_string


# PUBLIC API



# Generated at 2022-06-14 05:41:43.144410
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    input_string = '  This  Is   A   Text  Containing     some     Spaces  '
    assert __StringFormatter(input_string).format() == 'This is a text containing some spaces'
    input_string = '  This  Is   A   Text  Containing     some     Spaces  '
    assert __StringFormatter(input_string).format() == 'This is a text containing some spaces'
    input_string = '  This  Is   A   Text  Containing     some     Spaces  '
    assert __StringFormatter(input_string).format() == 'This is a text containing some spaces'
    input_string = '   This   is  a  test  of  the    function    '
    assert __StringFormatter(input_string).format() == 'This is a test of the function'

# Generated at 2022-06-14 05:41:48.863666
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    sf = __StringFormatter('   Te STsTReam  iTs  LiKe  lIvInG iN  A  TErRor fIlM  ')
    assert sf.format() == 'Te STsTReam iTs LiKe lIvInG iN A TErRor fIlM'


# Generated at 2022-06-14 05:41:59.995661
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('hello world').format() == 'Hello world'
    assert __StringFormatter('hello_world').format() == 'Hello world'
    assert __StringFormatter('hello  world').format() == 'Hello world'
    assert __StringFormatter('hello world,').format() == 'Hello world,'
    assert __StringFormatter('Hello World').format() == 'Hello world'
    assert __StringFormatter(' Hello World ').format() == 'Hello world'
    assert __StringFormatter(' Hello World, ').format() == 'Hello world,'
    assert __StringFormatter(' Hello World,"').format() == 'Hello world,"'
    assert __StringFormatter(' Hello World,"  ').format() == 'Hello world,"'
    assert __StringFormatter('HELLO WORLD').format() == 'Hello world'
    assert __StringForm

# Generated at 2022-06-14 05:42:10.447303
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('this is a  test').format() == 'This is a test'
    assert __StringFormatter('  this is the second  test, pretty cool!').format() == 'This is the second test, pretty cool!'
    assert __StringFormatter('this is a test, pretty cool!').format() == 'This is a test, pretty cool!'
    assert __StringFormatter('this is a <b>test</b>, really <b>cool!</b>').format() == 'This is a test, really cool!'
    assert __StringFormatter('now this is a very long test to see if it works').format() == 'Now this is a very long test to see if it works'

# Generated at 2022-06-14 05:42:23.285583
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    class TestCase:
        input_string: str
        expected_output: str
