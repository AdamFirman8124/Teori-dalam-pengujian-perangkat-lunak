

# Generated at 2022-06-14 05:38:58.340837
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('Hello') == 'hello'
    assert camel_case_to_snake('hello') == 'hello'
    assert camel_case_to_snake('thisIsACamelCaseString') == 'this_is_a_camel_case_string'
    assert camel_case_to_snake('ThisisACamelCaseString') == 'thisis_a_camel_case_string'
    assert camel_case_to_snake('TisisACamelCaseString') == 'tisis_a_camel_case_string'
    assert camel_case_to_snake('tisisACamelCaseString') == 'tisis_a_camel_case_string'

# Generated at 2022-06-14 05:39:10.400297
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('thisIsACamelStringTest') == 'this_is_a_camel_string_test'
    assert camel_case_to_snake('ThisIsACamelStringTest123') == 'this_is_a_camel_string_test123'
    assert camel_case_to_snake('ThisIsACamelStringTest123') == 'this_is_a_camel_string_test123'
    assert camel_case_to_snake('ThisIsACamelStringTest123', '-') == 'this-is-a-camel-string-test123'

# Generated at 2022-06-14 05:39:18.402125
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test', 'Expected "this_is_a_camel_string_test"'
    assert camel_case_to_snake('this_is_a_camel_string_test') == 'this_is_a_camel_string_test', 'Expected "this_is_a_camel_string_test"'



# Generated at 2022-06-14 05:39:22.660711
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'



# Generated at 2022-06-14 05:39:30.783690
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    out = snake_case_to_camel('the_snake_is_green')
    assert out == 'TheSnakeIsGreen'

    out = snake_case_to_camel('the_snake_is_green', upper_case_first=False)
    assert out == 'theSnakeIsGreen'

    out = snake_case_to_camel('the_snake_is_green', separator='-')
    assert out == 'the-snake-is-green'



# Generated at 2022-06-14 05:39:35.254281
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('a', False) == 'a'
    assert snake_case_to_camel('potato_tomato_pepper') == 'PotatoTomatoPepper'
    assert snake_case_to_camel('is_this_a_snake', False) == 'isThisASnake'
    assert snake_case_to_camel('not_a_snake') == 'NotASnake'



# Generated at 2022-06-14 05:39:49.628257
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    assert snake_case_to_camel('hello_python') == 'HelloPython'
    assert snake_case_to_camel('hello_python', False) == 'helloPython'
    assert snake_case_to_camel('hello_python', True, '-') == 'HelloPython'
    assert snake_case_to_camel('hello_python', False, separator='-') == 'helloPython'
    assert snake_case_to_camel('hello_python', True, separator='-') == 'HelloPython'
    assert snake_case_to_camel('hello_python', False, separator='-') == 'helloPython'
    assert snake_case_to_camel('hello-python', True, '-') == 'HelloPython'

# Generated at 2022-06-14 05:40:02.229073
# Unit test for function snake_case_to_camel
def test_snake_case_to_camel():
    """
    Test for string helper function snake_case_to_camel
    """
    assert snake_case_to_camel('x') == 'X'
    assert snake_case_to_camel('xx') == 'Xx'
    assert snake_case_to_camel('some_text') == 'SomeText'
    assert snake_case_to_camel('some_text', upper_case_first=False) == 'someText'
    assert snake_case_to_camel('some_text', separator='.') == 'Some.Text'
    assert snake_case_to_camel('some_text', separator='.', upper_case_first=False) == 'some.Text'

# Generated at 2022-06-14 05:40:14.951353
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:40:17.819241
# Unit test for function camel_case_to_snake
def test_camel_case_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'


# Generated at 2022-06-14 05:40:27.516702
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    # problems with "i" after "."
    assert __StringFormatter('hello world. i am here.').format() == 'Hello World. I am here.'
    # problems with "i" at the beginning of the sentence
    assert __StringFormatter('hello world.i am here.').format() == 'Hello World. I am here.'
    # spaces before comma
    assert __StringFormatter('hello world,i am here.').format() == 'Hello World, I am here.'
    # remove duplicate spaces
    assert __StringFormatter('Hello World.    I am here.').format() == 'Hello World. I am here.'
    # dashes
    assert __StringFormatter('Hello World. - I am here.').format() == 'Hello World. - I am here.'
    # colons

# Generated at 2022-06-14 05:40:37.572432
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:40:39.396920
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    formatter = __StringFormatter('one two  three  four   five     six       seven')
    assert formatter.format() == 'One two three four five six seven'


# PUBLIC API



# Generated at 2022-06-14 05:40:49.031485
# Unit test for method format of class __StringFormatter

# Generated at 2022-06-14 05:41:01.926114
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('TEST').format() == 'Test'
    assert __StringFormatter('test').format() == 'Test'
    assert __StringFormatter('- test').format() == 'Test'
    assert __StringFormatter(' test ').format() == 'Test'
    assert __StringFormatter('test  ').format() == 'Test'
    assert __StringFormatter('-  test  ').format() == 'Test'
    assert __StringFormatter('test-test').format() == 'Test test'
    assert __StringFormatter(' - test - test -').format() == 'Test test'
    assert __StringFormatter('test , test').format() == 'Test, test'
    assert __StringFormatter('test test').format() == 'Test test'

# Generated at 2022-06-14 05:41:09.589030
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    original_string = '''
    This
    is a
    test...
    '''

    expected_string = 'This is a test.'

    result_string = __StringFormatter(original_string).format()

    assert result_string == expected_string
    
test___StringFormatter_format()
# PUBLIC API



# Generated at 2022-06-14 05:41:21.184662
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert 'I am dumb' == __StringFormatter('i  am     dumb').format()
    assert 'I am dumb' == __StringFormatter('i am dumb').format()
    assert 'I am dumb' == __StringFormatter('i am dumb').format()
    assert 'I am dumb' == __StringFormatter('i  am dumb').format()
    assert 'I am dumb' == __StringFormatter('i  am    dumb').format()
    assert 'I am dumb, 27 years old and very cool' == __StringFormatter('i  am    dumb, 27 years old and very cool').format()
    assert 'I am dumb, 27 years old and very cool' == __StringFormatter('i  am    dumb,  27 years old and very cool').format()

# Generated at 2022-06-14 05:41:25.893756
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    from ._regex import TEST_INPUT_PRETTYFY_RULES

    print(__StringFormatter(' '.join([s[0] for s in TEST_INPUT_PRETTYFY_RULES])).format())



# Generated at 2022-06-14 05:41:36.378701
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    assert __StringFormatter('it is 10:00 p.m., http://www.google.it/test and my e-mail is m.rossi@gmail.com').format() == \
           'It is 10:00 p.m., http://www.google.it/test and my e-mail is m.rossi@gmail.com'
    assert __StringFormatter('  it  is 10:00     ø , http://www.google.it/test and my e-mail is m.rossi@gmail.com and I am "mr. rossi" ').format() == \
           'It is 10:00 ø, http://www.google.it/test and my e-mail is m.rossi@gmail.com and I am "mr. rossi"'
    assert __StringFormatter('it\'s 10:00pm').format

# Generated at 2022-06-14 05:41:45.819516
# Unit test for method format of class __StringFormatter
def test___StringFormatter_format():
    input = r"""
            Hello,     my name is     Stefano...
            I'm 25 years    old and
            I'm a student   at the
             university.
             my email is
            stefano@email.it
            and my website is http://www.stefano.it
            """

    expected = r"""
            Hello, my name is Stefano...
            I'm 25 years old and
            I'm a student at the
            University.
            My email is stefano@email.it
            And my website is http://www.stefano.it
            """

    assert __StringFormatter(input).format() == expected


# Generated at 2022-06-14 05:41:52.025144
# Unit test for function booleanize
def test_booleanize():
    assert booleanize('true') == True
    assert booleanize('True') == True
    assert booleanize('false') == False
    assert booleanize('False') == False
    assert booleanize('123') == False

test_booleanize()


# Generated at 2022-06-14 05:42:01.657338
# Unit test for constructor of class __StringCompressor
def test___StringCompressor():
    # create an instance
    obj = __StringCompressor()

    # using the object, test the class method compress()
    #
    # NOTE:
    # the method is intended to be used in binary mode therefore we deal with bytes instead of strings
    # (as per design, the method compress() is not going to convert strings to bytes)
    original_bytes =  b'deadbeef'
    compressed_bytes = obj.compress(original_bytes)

    # ensure string compression has effectively been applied
    assert len(original_bytes) > len(compressed_bytes)
    assert original_bytes != compressed_bytes

    # using the object, test the class method decompress()
    #
    # NOTE:
    # the method is intended to be used in binary mode therefore we deal with bytes instead of strings
    # (as per design, the method decompress() is

# Generated at 2022-06-14 05:42:03.874715
# Unit test for function decompress
def test_decompress():
    """Test for function decompress()"""
    assert decompress() == 'Decompressed string'




# Generated at 2022-06-14 05:42:07.348540
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

# Generated at 2022-06-14 05:42:20.095432
# Unit test for constructor of class __StringFormatter
def test___StringFormatter():
    # constructor
    try:
        __StringFormatter(None)
        assert False
    except InvalidInputError as e:
        assert True

    try:
        __StringFormatter(123)
        assert False
    except InvalidInputError as e:
        assert True

    try:
        __StringFormatter('test')
        assert True
    except InvalidInputError as e:
        assert False

    # format
    f = __StringFormatter('test')
    assert f.format() == 'Test'

    f = __StringFormatter('test test')
    assert f.format() == 'Test test'

    f = __StringFormatter('  test  test  ')
    assert f.format() == 'Test test'

    f = __StringFormatter('  test test ')
    assert f.format() == 'Test test'

   

# Generated at 2022-06-14 05:42:24.173381
# Unit test for function strip_margin
def test_strip_margin():

    # invalid test
    invalid_test = False
    try:
        strip_margin(None)
    except Exception as e:
        invalid_test = 'InvalidInputError' in str(e)
    assert invalid_test

    # Tests

    # empty string
    assert strip_margin('') == ''

    # string without margins
    assert strip_margin('Hello World!') == 'Hello World!'

    # string with left margins
    assert strip_margin('    Hello \t World!') == 'Hello \t World!'

    # single line string
    assert strip_margin('    Hello World!') == 'Hello World!'

    # multi line string
    assert strip_margin('''
                        Hello World!
                        I\'m a multi line string
                        ''') == '''
Hello World!
I'm a multi line string
'''

    #

# Generated at 2022-06-14 05:42:27.068243
# Unit test for function asciify
def test_asciify():
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'
    assert asciify('ThisIsAscii') == 'ThisIsAscii'
    assert asciify('') == ''



# Generated at 2022-06-14 05:42:31.719772
# Unit test for function prettify
def test_prettify():
    assert prettify(' unprettified string ,, like this one,will be"prettified" .it\\'
                    's awesome! ')\
        == 'Unprettified string, like this one, will be "prettified". It\'s awesome!'

    assert prettify('I love this site: http://foo.bar/baz@qux?gux :)') == 'I love this site: http://foo.bar/baz@qux?gux :)'
    assert prettify('I hate this site: http://foo.bar/baz@qux?gux :)') == 'I hate this site: http://foo.bar/baz@qux?gux :)'
    assert prettify('This is an email: foo@bar.com .') == 'This is an email: foo@bar.com .'

# Generated at 2022-06-14 05:42:36.856989
# Unit test for function strip_margin
def test_strip_margin():
    input_string = '''
                    line 1
                    line 2
                    line 3
                    '''
    output_string = '''
    line 1
    line 2
    line 3
    '''
    assert strip_margin(input_string) == output_string



# Generated at 2022-06-14 05:42:48.134608
# Unit test for function strip_html
def test_strip_html():
    assert strip_html("test: <a href='foo/bar'>click here</a>") == "test: "
    assert strip_html("test: <a href='foo/bar'>click here</a>", keep_tag_content=True) == "test: click here"
    assert strip_html("<a href='foo/bar'>click here</a>") == "click here"
    assert strip_html("<a href='foo/bar'>click here</a>", keep_tag_content=True) == "click here"
    assert strip_html("<body><a href='foo/bar'>click here</a></body>") == "click here"
    assert strip_html("<a href='foo/bar'>click here</a>", keep_tag_content=True) == "click here"