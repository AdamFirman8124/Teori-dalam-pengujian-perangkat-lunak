

# Generated at 2022-06-13 19:41:36.807770
# Unit test for function parse
def test_parse():
    ds = """This is a summary.

    This is a long description. There may be lines separated by
    blank lines.

    Args:
        arg1 (str): First argument.
        arg2 (str): Second argument.

    Returns:
        str: Some `cool` stuff.

    Raises:
        Exception: If something bad happens.
    """
    doc = parse(ds)
    assert doc.short_description == "This is a summary."
    assert len(doc.long_description.split("\n")) == 5
    assert doc.meta[0].args == "arg1 (str)"
    assert doc.meta[0].description[0] == "First argument."
    assert doc.meta[-1].args == "Exception"
    assert doc.meta[-1].description[0] == "If something bad happens."
   

# Generated at 2022-06-13 19:41:43.264158
# Unit test for function parse
def test_parse():
    text = '''\
    Replaces null bytes in the input file with a given replacement byte.

    :param input: path to the file where null bytes will be replaced
    :param output: path to the output file
    :param replacement_byte: byte used as a replacement
    :returns: number of replaced bytes
    '''
    res = parse(text)
    assert len(res.returns) == 1
    assert len(res.params) == 3
    assert res.short_description == 'Replaces null bytes in the input file with a given replacement byte.'
    
# print(parse(text).params)
# print(len(parse(text).params))
# print(parse(text).short_description)
# print(parse(text).long_description)
# print(parse(text).params[0].param_name)
# print(

# Generated at 2022-06-13 19:41:51.857253
# Unit test for function parse
def test_parse():
    from docstring_parser import parse

    text = """List of colors to label for either 'lines' or 'points'.

This parameter is a dictionary, where the keys are the plotted data, and
the values are colors to be used for the respective keys.  If the
dictionary has only one key, then all lines will be colored the same.

Parameters
----------
d : dict
    Coloring scheme, where keys are plotted data, and values
    are colors.

Returns
-------
int
    The number of colors applied"""

    print("Parse text: ")
    print(text)
    print("")
    print("Parse result: ")
    print(parse(text))


# Generated at 2022-06-13 19:42:01.954987
# Unit test for function parse
def test_parse():

    doc = """A short description.

    Extended description.

    Args:
    arg1: The first arg.
    arg2: The second arg.
    Returns:
        Some return value.
    """

    parsed = parse(doc)
    assert parsed.short_description == "A short description."
    assert parsed.long_description == "Extended description."
    assert len(parsed.params) == 2
    assert len(parsed.returns) == 1
    assert parsed.returns[0].description == "Some return value."

    doc = """A short description.

    Args:
    arg1: The first arg.
    arg2: The second arg.
    Returns:
        Some return value.
    """

    parsed = parse(doc)
    assert parsed.short_description == "A short description."

# Generated at 2022-06-13 19:42:11.028647
# Unit test for function parse
def test_parse():
    """Test for function parse"""
    assert parse("") == Docstring("", [], "")
    assert parse("hello") == Docstring("", [], "hello")
    assert parse("The quick brown fox jumps over the lazy dog") == Docstring("", [], "The quick brown fox jumps over the lazy dog")
    assert parse("hello world") == Docstring("", [], "hello world")
    assert parse("hello\nworld") == Docstring("", [], "hello\nworld")
    assert parse("hello\nworld\n") == Docstring("", [], "hello\nworld")
    assert parse("hello\n\nworld") == Docstring("", [], "hello\nworld")
    assert parse("\nhello\n\nworld\n") == Docstring("", [], "hello\nworld")

# Generated at 2022-06-13 19:42:18.844711
# Unit test for function parse
def test_parse():

    docstring = 'This is a test for the docstring parsing'
    # parse the docstring
    try:
        parse(docstring)
    except ParseError:
        raise
    else:
        # parse the docstring with a style
        try:
            parse(docstring, style='napoleon')
        except ParseError:
            raise
        else:
            pass


# Generated at 2022-06-13 19:42:27.868942
# Unit test for function parse
def test_parse():

    #Doctest 1
    def doctest_1():
        """
            Single line summary.

            Single line description.

            Args:
                param1 (str): The first parameter.
                param2 (Optional[str]): The second parameter. Defaults to None.
                *args: Variable length argument list.
                **kwargs: Arbitrary keyword arguments.

            Returns:
                bool: The return value
                int: The number of things returned.

            Raises:
                AttributeError: The ``Raises`` section is a list of all exceptions
                                that are relevant to the interface.
                ValueError: If `param2` is equal to `param1`.

        """

    #Doctest 2

# Generated at 2022-06-13 19:42:31.641200
# Unit test for function parse
def test_parse():
    text = """Called before every request, get_current_user is expected to return
    None if the user is not logged in, otherwise it should return the user
    object that was set by :meth:`LoginHandler.get_current_user`.
    """
    pd = parse(text)
    assert pd.short_description == 'Called before every request, get_current_user is expected to return'

# Generated at 2022-06-13 19:42:35.985247
# Unit test for function parse
def test_parse():
    docstring = parse('Test docstring')
    assert docstring.short_description == 'Test docstring'
    assert docstring.long_description == ''
    assert len(docstring.meta) == 0
    assert docstring.returns == None
    assert docstring.returns_description == ''
    assert len(docstring.params) == 0
    assert len(docstring.raises) == 0


# Generated at 2022-06-13 19:42:45.322601
# Unit test for function parse

# Generated at 2022-06-13 19:42:59.870128
# Unit test for function parse
def test_parse():
    docstring1 = """
    This is a Google style docstring.

    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.

    Returns:
        bool: The return value. True for success, False otherwise.

    """
    docstring2 = """
    This is a Numpy style docstring.

    Parameters
    ----------
    arg1 : int
        The first argument.
    arg2 : str
        The second argument.

    Returns
    -------
    bool
        The return value. True for success, False otherwise.

    """

# Generated at 2022-06-13 19:43:11.945042
# Unit test for function parse
def test_parse():
    from docstring_parser.styles.sphinx import parse as parse_sphinx
    from docstring_parser.styles.numpy import parse as parse_numpy
    from docstring_parser.styles.google import parse as parse_google
    from docstring_parser.common import Field

    # Test that passing a style works
    assert parse(':param foo: bar\n', style='sphinx') == parse_sphinx(':param foo: bar\n')
    assert parse(':param foo: bar\n', style='numpy') == parse_numpy(':param foo: bar\n')
    assert parse(':param foo: bar\n', style='google') == parse_google(':param foo: bar\n')

    # Test the auto selection
    field = Field(name='foo', type_='int', desc='bar')


# Generated at 2022-06-13 19:43:12.529705
# Unit test for function parse
def test_parse():
    pass



# Generated at 2022-06-13 19:43:22.236547
# Unit test for function parse
def test_parse():
    docstring = parse("""A module for parsing docstrings.

What does this function do?

:param arg1: The first argument.
:param arg2: The second argument.
:returns: None
:raises keyError: raises an exception
""")
    assert docstring.short_description == "A module for parsing docstrings."
    assert docstring.long_description == "What does this function do?"
    assert docstring.returns == "None"
    assert docstring.raises == "keyError: raises an exception"
    assert docstring.params[0].arg_name == "arg1"
    assert docstring.params[0].description == "The first argument."
    print("test_parse() passed")

# Generated at 2022-06-13 19:43:32.321241
# Unit test for function parse

# Generated at 2022-06-13 19:43:43.863570
# Unit test for function parse
def test_parse():
    ds = """\
    This is a simple example of a docstring.

    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.
    Returns:
        bool: The return value. True for success, False otherwise.
    """

    docstring = parse(ds)
    assert docstring.short_description == 'This is a simple example of a docstring.'
    assert docstring.long_description == ''

# Generated at 2022-06-13 19:43:54.717676
# Unit test for function parse
def test_parse():
    doc = parse(
        '''\
    :param name: description
    :param email: description
    :raises: :py:class:`ValueError`, TypeError
    '''
    )
    assert doc.meta == [('name', 'description'), ('email', 'description')]
    assert doc.raises == ['ValueError', 'TypeError']

    doc = parse(
        '''\
    :param name: description
    :type name: str
    :param email: description
    :type email: str
    '''
    )
    assert len(doc.meta) == 2
    assert doc.meta[0][0] == 'name'
    assert doc.meta[0][1] == 'description'
    assert doc.meta[0][2] == str

# Generated at 2022-06-13 19:43:57.425182
# Unit test for function parse
def test_parse():
    assert parse("""
        Summary line.

        Extended description.
        """).summary == 'Summary line.'
    assert parse("""
        Summary line.
        """).summary == 'Summary line.'

# Generated at 2022-06-13 19:44:01.435721
# Unit test for function parse
def test_parse():
    docstring = """This is a test.

    This is a second line.
    """

    parsed_docstring = parse(docstring)
    assert parsed_docstring.short_description == "This is a test."

# Generated at 2022-06-13 19:44:10.225155
# Unit test for function parse
def test_parse():
    class TestClass:
        """This is a test class.

        :param param1: this is a first param
        :param param2: this is a second param
        :returns: None
        :raises keyError: raises an exception
        """
        def __init__(self, param1, param2):
            self.param1 = param1
            self.param2 = param2

        def test_method(self):
            """This is a test method.

            :param param1: this is a first param
            :param param2: this is a second param
            :returns: None
            :raises keyError: raises an exception
            """
            return self.param1 + self.param2


# Generated at 2022-06-13 19:44:17.819580
# Unit test for function parse
def test_parse():
    text = """
    Test parse function
    :arg1: value1
    :arg2: value2
    """

    docstring = parse(text)

    assert docstring.full_d

# Generated at 2022-06-13 19:44:25.262540
# Unit test for function parse
def test_parse():
    text = '''
    Function to display a message
    :param str message: the message to display
    :returns: None
    '''
    assert parse(text).summary == 'Function to display a message'
    assert str(parse(text).params[0]) == 'message: the message to display'
    assert str(parse(text).returns) == 'None'

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:44:34.789398
# Unit test for function parse
def test_parse():
    """Test the docstring_parser.parse function."""

    from docstring_parser.common import ParseError

    def _parse(s, style):
        try:
            return parse(s, style=STYLES[style])
        except ParseError as e:
            print(e)


# Generated at 2022-06-13 19:44:45.145552
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import epytext, numpy, google, default, rest_reST
    assert parse('', style=default) == Docstring(summary='', body='', meta={})
    assert parse('hi\n==\n\nbody', style=epytext) == Docstring(summary='hi', body='body', meta={})
    assert parse('hi\n==\n\nbody', style=numpy) == Docstring(summary='hi', body='body', meta={})
    assert parse('hi\n==\n\nbody', style=google) == Docstring(summary='hi', body='body', meta={})
    assert parse('hi\n==\n\nbody', style=default) == Docstring(summary='hi', body='body', meta={})

# Generated at 2022-06-13 19:44:52.316577
# Unit test for function parse
def test_parse():
    docstr = """
            Shuffle an array (Fisher-Yates).

            :param arr: An array to shuffle
            :param seed: Random seed
            :return: Shuffled array
            """

    d = parse(docstr)
    assert d.brief == "Shuffle an array (Fisher-Yates)."
    assert len(d.params) == 2
    assert d.params[0].name == "arr"
    assert d.params[0].desc == "An array to shuffle"
    assert d.returns.type == "None"
    assert d.returns.desc == "Shuffled array"

# Generated at 2022-06-13 19:44:57.056470
# Unit test for function parse
def test_parse():
    text = '''Simple function

    :param x: does y
    :returns: z
    '''
    assert parse(text)

    text = '''Simple function

    :param x: does y
    :returns: z

    More text.
    '''
    assert parse(text)

    text = '''Simple function

    :param x: does y
    :returns: z

    More text.

    And even more.
    '''
    assert parse(text)

# Generated at 2022-06-13 19:45:03.709938
# Unit test for function parse
def test_parse():
    """Test case to check parse function"""
    assert parse('') == Docstring(description='')
    assert parse(
        'module') == Docstring(description='module')
    assert parse(
        'module'
    ) == Docstring(description='module')
    assert parse(
        'module\n') == Docstring(description='module')
    assert parse(
        'module\n\n') == Docstring(description='module')
    assert parse(
        'module\n\nA second paragraph') == Docstring(description='module\n\nA second paragraph')
    assert parse(
        'module\n\nA second paragraph\n') == Docstring(description='module\n\nA second paragraph')

# Generated at 2022-06-13 19:45:07.628797
# Unit test for function parse
def test_parse():
    docstr = """This is a test docstring
    :param arg1: the first argument
    :param arg2: the second argument
    :returns: None
    """
    parse(docstr)

# Generated at 2022-06-13 19:45:09.501233
# Unit test for function parse
def test_parse():
    assert True

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 19:45:10.996340
# Unit test for function parse
def test_parse():
    # TODO: Implement
    return True

# Generated at 2022-06-13 19:45:17.456514
# Unit test for function parse
def test_parse():
    with open('docstring_parser/__init__.py', 'r') as f:
        text = f.read()
        result = parse(text)
        assert result.short_description == 'Main interface for parsing docstrings.'

# Generated at 2022-06-13 19:45:23.874670
# Unit test for function parse
def test_parse():
    from docstring_parser.parse import parse
    from docstring_parser.docstring import Docstring
    docstring = """Example docstring.
        Another line of the docstring.
        """
    # Test String 
    assert isinstance(parse(docstring), Docstring)
     
    # Test Style
    assert parse(docstring, style=None)
    
    # Test Docstring, Style
    assert isinstance(parse(docstring, style=None), Docstring)

# Generated at 2022-06-13 19:45:32.642113
# Unit test for function parse
def test_parse():
    docstring = parse("""Hello
                        : meta1: value1
                        : meta2: value2
                        :returns: returns this
                        :rtype: int
                        :raises ValueError: if something goes wrong
                        """)

    assert docstring.short_description == "Hello"
    assert docstring.long_description == ""
    assert docstring.meta["meta1"].argname == "meta1"
    assert docstring.meta["meta1"].type_name == ""
    assert docstring.meta["meta1"].description == "value1"
    assert docstring.meta["meta2"].argname == "meta2"
    assert docstring.meta["meta2"].type_name == ""
    assert docstring.meta["meta2"].description == "value2"
    #assert docstring.returns.description ==

# Generated at 2022-06-13 19:45:36.418338
# Unit test for function parse
def test_parse():
    text = 'The quick brown fox jumps over the lazy dog'
    docstring = parse(text)
    assert isinstance(docstring, Docstring)
    assert docstring.short_description == text

test_parse()

# Generated at 2022-06-13 19:45:41.771147
# Unit test for function parse
def test_parse():
    mydocstring = """This is a
    docstring.
    :param user_id: The user id.
    :type user_id: int
    :return: The user object.
    :rtype: User"""
    assert parse(mydocstring, style=Style.google).returns.type == "User"

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:45:51.922293
# Unit test for function parse
def test_parse():
    assert parse("""No summary.

:param name: The name to use.
:type name: str.
:param state: Current state to be in.
:type state: bool.
:returns: Description of return value.
:rtype: str.
""", style=Style.google)
    assert parse("""No summary.

:param name: The name to use.
:type name: str.
:param state: Current state to be in.
:type state: bool.
:returns: Description of return value.
:rtype: str.
""", style=Style.numpy)

# Generated at 2022-06-13 19:46:03.329925
# Unit test for function parse
def test_parse():
    """Test docstring_parser.parse."""


# Generated at 2022-06-13 19:46:08.645114
# Unit test for function parse
def test_parse():
    doc_string =  '''
    This function is written by summy
        Parameters:
            param1 - The first parameter.
            param2 - The second parameter.
        Returns:
            This is a description of what is returned.
        Raises:
            KeyError - Raises an exception.
    '''
    print(parse(doc_string))

# Generated at 2022-06-13 19:46:16.496995
# Unit test for function parse
def test_parse():
    text = """This is a function.
    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.
    Returns:
        bool: The return value. True for success, False otherwise.
    Meta:
        author: John Smith
        date: 1/1/2018
    """
    d = parse(text)
    assert d.short_desc == 'This is a function.'
    assert len(d.long_desc) == 0
    assert len(d.params) == 2
    assert len(d.returns) == 1
    assert len(d.meta) == 2

if __name__=='__main__':
    test_parse()

# Generated at 2022-06-13 19:46:23.679753
# Unit test for function parse
def test_parse():
    docstring = """One line summary.

    This is a multiline description
   """
    test = parse(docstring)
    assert len(test.args) == 0
    assert test.returns is None
    assert test.raises is None
    assert test.summary == 'One line summary.'
    assert len(test.meta) == 1
    assert test.meta['This is a multiline description'] == ''

# Generated at 2022-06-13 19:46:33.259748
# Unit test for function parse
def test_parse():
  # All of these statements should be true
  assert parse("This is a test string") is not None
  assert parse("This is a test string", Style.google) is not None
  assert parse("This is a test string", Style.sphinx) is not None
  assert parse("This is a test string", Style.numpy) is not None

# Generated at 2022-06-13 19:46:40.873382
# Unit test for function parse

# Generated at 2022-06-13 19:46:45.517060
# Unit test for function parse
def test_parse():
    text = '''Sums a and b.
    Parameters:
        a (int): The first number
        b (int): The second number
    Returns:
        int: The sum of a and b'''

    print(parse(text))

# Generated at 2022-06-13 19:46:57.988784
# Unit test for function parse
def test_parse():
    text = '''This is a docstring.
              :param name: A string
              :returns: None
              :raises ValueError: If ``name`` is invalid
           '''
    docstring = parse(text)
    assert docstring.short_description == 'This is a docstring.'
    assert docstring.long_description == ''
    assert docstring.meta['param']['name'].dtype == 'str'
    assert docstring.meta['param']['name'].description == 'A string'
    assert docstring.meta['returns'].dtype == None
    assert docstring.meta['returns'].description == 'None'
    assert docstring.meta['raises']['ValueError'].dtype == None

# Generated at 2022-06-13 19:47:10.088722
# Unit test for function parse
def test_parse():
    assert parse("""
        Test the parser.
    """) == Docstring(summary='Test the parser.')

    assert parse("""
        Test the parser.

        :foo: bar
        :baz: qux
    """) == Docstring(summary='Test the parser.', meta={'foo': 'bar', 'baz': 'qux'})

    assert parse("""
        Test the parser.

        :foo: bar
        :baz: qux
        """).meta['foo'] == 'bar'
    assert parse("""
        Test the parser.

        :foo: bar
        :baz: qux
        """).meta['baz'] == 'qux'

# Test parsing of a few known docstring styles

# Generated at 2022-06-13 19:47:16.046533
# Unit test for function parse
def test_parse():
    text = '''\
    This is a module docstring.

    This is just another paragraph.
        '''
    docstring = parse(text)
    assert 'This is a module docstring.' in docstring.short_description
    assert 'This is just another paragraph.' in docstring.long_description


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:47:19.360246
# Unit test for function parse
def test_parse():
    parse("abc abcde")
    parse("abc abcde", style=Style.google)
    parse("abc abcde", style=Style.numpy)
    parse("abc abcde", style=Style.napoleon)

# Main function
if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:47:29.294562
# Unit test for function parse
def test_parse():
    # Test for auto
    text = ('This is a description.\n'
            'This is a description, too.\n'
            ':type param1:  int\n'
            ':param param1: this is a integer value\n'
            ':returns: int\n'
            ':rtype: int\n'
            ':raises RuntimeError:\n'
            '    This is a runtime error.')
    d = parse(text, Style.auto)
    assert d.description == 'This is a description.\nThis is a description, too.\n'
    assert d.params['param1'].type_name == 'int'
    assert d.params['param1'].description == 'this is a integer value'
    assert d.return_type.type_name == 'int'
    assert d

# Generated at 2022-06-13 19:47:34.403795
# Unit test for function parse
def test_parse():
    text = '''
    pytest plugin to help with testing docker containers
 
    :param str name: name of container
    :param int status: if status is 0, then start; if status is 1, then stop; if status is 2, then remove
    :returns: a Tuple of the form (stdout, stderr) from executing the docker command.
    '''
    ret = parse(text)
    assert type(ret) is Docstring

# Generated at 2022-06-13 19:47:46.262107
# Unit test for function parse
def test_parse():
    docstring = \
"""
This is the summary of the function.

This is the description of the function.

:param param1: Description of the first parameter.
:param param2: Description of the second parameter.
:returns: Description of what is returned.
:raises keyError: raises an exception
"""
    parsed = parse(docstring)
    assert parsed.summary == "This is the summary of the function."
    assert parsed.description == "This is the description of the function.\n"
    assert parsed.returns == "Description of what is returned."
    assert parsed.raises == {'keyError': 'raises an exception'}
    assert parsed.params == {
        'param2': 'Description of the second parameter.',
        'param1': 'Description of the first parameter.'}

test_parse()

# Generated at 2022-06-13 19:47:56.323190
# Unit test for function parse
def test_parse():

    inputtext = """
    This is a docstring!
    It has two paragraphs
    """
    output = parse(inputtext)
    assert output.short_description == "This is a docstring!"
    assert output.long_description == "\nIt has two paragraphs\n"
    assert output.returns.annotation == None
    assert output.returns.description == None

# Generated at 2022-06-13 19:48:03.063688
# Unit test for function parse
def test_parse():
    text = '''\
        Summary:
            Describe a function

        Args:
            arg1: The first argument
            arg2: The second argument

        Returns:
            str: A string

        Raises:
            ValueError: If something bad happens

        Notes:
            Stuff about this function
    '''
    ret = parse(text)

# Generated at 2022-06-13 19:48:03.955293
# Unit test for function parse
def test_parse():
    text='''
    This is sample
    '''
    ds = parse(text)
    assert ds.short_description == 'This is sample'

# Generated at 2022-06-13 19:48:12.812733
# Unit test for function parse
def test_parse():
    assert(parse("""
            Function that returns a value.
            :type val: int
            :type arg2: int
            :rtype: int
            """))
    assert(parse("""
            Function that returns a value.
            :param val: integer value
            :param arg2: integer value
            :rtype: int
            """))
    assert(parse("""
            Function that returns a value.
            :param val: integer value
            :type val: int
            :param arg2: integer value
            :type arg2: int
            :rtype: int
            """))

# Generated at 2022-06-13 19:48:21.321866
# Unit test for function parse
def test_parse():
    ds = parse("""
    A first class docstring.

    Usage:
        find_user <name> [--age=<age>]
        find_user (-h | --help)

    Foobar.

    Options:
        -h --help     Show this screen.
        --age=<age>   Age of user [default: None].
    """, style=Style.sphinx)
    assert ds.short_description == "A first class docstring."
    assert ds.long_description == "\nFoobar."
    assert ds.usage == "find_user <name> [--age=<age>]" \
                       "\nfind_user (-h | --help)"

# Generated at 2022-06-13 19:48:31.726222
# Unit test for function parse
def test_parse():
    doc = """
    :param str name: the name of the user.
    :param int age: the age of the user.
    """
    result = parse(doc)
    assert result.meta['params'][0]['name'] == 'name'
    assert result.meta['params'][0]['type'] == 'str'
    assert result.meta['params'][0]['desc'] == 'the name of the user.'
    assert result.meta['params'][1]['name'] == 'age'
    assert result.meta['params'][1]['type'] == 'int'
    assert result.meta['params'][1]['desc'] == 'the age of the user.'

# Generated at 2022-06-13 19:48:34.066496
# Unit test for function parse
def test_parse():
    parse("This is a docstring")
    parse("This is a docstring", style=Style.google)
    parse("This is a docstring", style=Style.numpy)

# Generated at 2022-06-13 19:48:44.762893
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Parameter
    from docstring_parser.docstring import Docstring
    import re
    import inspect
    parseout = parse(inspect.getsource(parse))

    def pass_test(test_str, value):
        assert value in test_str

    print(parseout.short_description)
    assert parseout.short_description == "Parse the docstring into its components."
    for x in parseout.split_long_description:
        assert not re.match(r'( :.+: )|(\n *- )', x)
    pass_test(parseout.split_long_description[0], "The docstring is parsed into")
    pass_test(parseout.split_long_description[1], "parsed docstring representation")

# Generated at 2022-06-13 19:48:51.245896
# Unit test for function parse
def test_parse():
    doc = parse("""
        The first line is brief explanation, which may be completed with a
        longer one.

        The only argument is ``text``.

        :param text: docstring text to parse
        :returns: parsed docstring representation

        Examples:
            >>> text = '''
            ... This is an example docstring.
            ... It is indented with spaces
            ... rather than tabs.
            ... '''
            >>> result = parse(text)
            >>> print(result.short_description)
            This is an example docstring.
            >>> print(result.long_description)
            It is indented with spaces
            rather than tabs.
            >>> print(result.params[0].name)
            text
    """, style="google")
    print(doc)

if __name__ == "__main__":
    test_

# Generated at 2022-06-13 19:48:57.892744
# Unit test for function parse
def test_parse():
    docstring = parse("""
    Parse the docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """)
    assert docstring.short_description == "Parse the docstring into its components."
    assert docstring.long_description == ""
    assert docstring.returns == "parsed docstring representation"
    assert docstring.meta[0].arg_name == "text"
    assert docstring.meta[1].arg_name == "style"

# Generated at 2022-06-13 19:49:08.757555
# Unit test for function parse
def test_parse():
    import os
    file = os.path.dirname(os.path.realpath(__file__))+'/examples/example.py'
    with open(file) as file:
        example = file.read()

    parsed = parse(example)
    assert len(parsed.meta) == 2
    assert parsed.meta[0].name == 'addons'
    assert parsed.content.startswith('Example of parsing')
    assert parsed.short_description == 'Example of parsing'


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:49:17.071562
# Unit test for function parse
def test_parse():
    from docstring_parser import parse
    import sys
    test_string = """This is a test docstring
    :param param1: The first parameter.
    :param param2: The second parameter.
    :returns: This is a description of what is returned.
    :raises keyError: raises an exception
    """
    print("Input:\n" + test_string)
    result = parse(test_string)
    print("Output:\n" + str(result))


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:49:28.133949
# Unit test for function parse
def test_parse():
    # Test Google style parsing
    google_style_docstring = """Compute the ratio of a value to a total.

Args:
  value: A value.
  total: A value.

Returns:
  The quotient of value / total.
"""
    doc = parse(google_style_docstring, style=Style.google)
    assert doc.short_description == "Compute the ratio of a value to a total."
    assert doc.long_description == ""
    assert len(doc.meta) == 2
    assert doc.parameters[0].name == "value"
    assert doc.parameters[0].type_name == "A value."
    assert doc.parameters[1].name == "total"
    assert doc.parameters[1].type_name == "A value."
    assert doc.returns.type_name

# Generated at 2022-06-13 19:49:32.404553
# Unit test for function parse
def test_parse():
    assert parse('Hello world.') == Docstring(
        'Hello world.',
        meta=[],
        is_empty=False,
    )
    assert parse('Hello world.\n\nHello again.') == Docstring(
        'Hello world.\n\nHello again.',
        meta=[],
        is_empty=False,
    )
    # TODO: Add many more tests

# Generated at 2022-06-13 19:49:42.136889
# Unit test for function parse
def test_parse():
    doc = '''\
This is a function.

    :param a: parameter a
    :type a: str
    :param b: parameter b
    :type b: str
    :returns: return value
    :rtype: str
'''
    res = parse(doc)
    exp = Docstring(
        summary='This is a function.',
        body='',
        meta=[
            ('param', 'a', 'parameter a'),
            ('type', 'a', 'str'),
            ('param', 'b', 'parameter b'),
            ('type', 'b', 'str'),
            ('returns', '', 'return value'),
            ('rtype', '', 'str'),
        ]
    )
    assert res == exp

# Generated at 2022-06-13 19:49:45.198271
# Unit test for function parse
def test_parse():
    assert parse('Hello')
    assert parse('Hello', style='sphinx')
    assert parse('Hello', style='numpy')

# Generated at 2022-06-13 19:49:50.788942
# Unit test for function parse
def test_parse():
    text = '''
    This function parses the docstring on the given text.

    :param text: docstring text
    :param style: docstring style
    :returns: parsed docstring representation
    '''
    assert parse(text).short_description == 'This function parses the docstring on the given text.'

# Generated at 2022-06-13 19:49:59.651571
# Unit test for function parse
def test_parse():
    from docstring_parser.docstring import parse
    import docstring_parser.styles.google
    import docstring_parser.styles.numpy
    text = """\
    Return the number of times that the string "code" appears anywhere in the
    given string, except we'll accept any letter for the 'd', so "cope" and
    "cooe" count.

    :param str s: a string in which to look for the substring
    :param str code: the substring to search for. it's case-sensitive
    :param bool strict: if True, require an exact match
    :returns: number of times that code appears in s
    """
    parse(text)
    assert len(parse(text).params) == 3

    google = parse(text, style='Google')
    numpy = parse(text, style='Numpy')

# Generated at 2022-06-13 19:50:07.807213
# Unit test for function parse
def test_parse():
    docstring = """Function for testing docstrings
 
    Args:
        a (int): first number
        b (int): second number
    
    Returns:
        int: the total
    """

    parsed = parse(docstring, Style.googledoc)
    assert parsed.full_source == docstring
    assert parsed.summary == "Function for testing docstrings"
    assert parsed.description == ""
    assert parsed.params.keys() == ['a', 'b']
    assert parsed.params['a'] == "first number"
    assert parsed.returns == "the total"
    assert parsed.return_type == "int"

# Generated at 2022-06-13 19:50:17.171771
# Unit test for function parse
def test_parse():
    nptest.assert_raises(ParseError, parse, None)
    nptest.assert_raises(ParseError, parse, '')
    nptest.assert_raises(ParseError, parse, ' ')
    nptest.assert_raises(ParseError, parse, '    \n')
    nptest.assert_raises(ParseError, parse, "\n")
    nptest.assert_raises(ParseError, parse, "\n\n\n")
    nptest.assert_raises(ParseError, parse, "test")
    nptest.assert_raises(ParseError, parse, "test\n")
    nptest.assert_raises(ParseError, parse, "test\n\n\n")
    nptest.assert_

# Generated at 2022-06-13 19:50:30.830991
# Unit test for function parse
def test_parse():
    from nose.tools import assert_equal
    
    text = '''Solve a least-squares problem with bounds on the variables.

:param x0: is a starting guess
:type x0: ndarray
:param bounds: is a list of tuples specifying the lower and upper bound for
each independent variable [(xl0, xu0), (xl1, xu1), ...]
:type bounds: list of tuples
:param method: type of solver
:type method: str
:returns: array -- solution (if found)
:raises: RuntimeError
'''

# Generated at 2022-06-13 19:50:42.889428
# Unit test for function parse
def test_parse():
    # test case 1
    text = '''This is an example module.
    :param request: HttpRequest
    :type request: django.http.request.HttpReuqet
    :returns: HttpResponse
    :raises keyError: raises an exception
    '''
    assert parse(text) == Docstring(
        summary='This is an example module.',
        params={'request': {'type': 'django.http.request.HttpReuqet', 'desc': 'HttpRequest'}},
        returns={'type': 'HttpResponse', 'desc': None},
        exceptions={'keyError': {'type': None, 'desc': 'raises an exception'}},
        extra_sections=[],
        meta=[]
    )

    # test case 2

# Generated at 2022-06-13 19:50:44.806365
# Unit test for function parse
def test_parse():
    assert parse('').meta == {}
    assert parse('meta\n====\nanother\n-------\n\nBody.').meta == {'meta': 'another'}

# Generated at 2022-06-13 19:50:54.973462
# Unit test for function parse
def test_parse():
    import pkgutil
    import types
    module = types.ModuleType('test_parse')
    module.__file__ = '/tmp/test_parse'
    module.__loader__ = pkgutil.get_loader(module.__name__)
    module.__package__ = 'test_parse'
    f = open('/tmp/test_parse.py', 'w')
    f.write(test_parse.__doc__)
    f.close()
    pkgutil.imp.load_module(module.__name__, module.__file__,
                            module.__file__, module.__loader__)
    f = open('/tmp/test_parse.py')
    doc = f.read()
    f.close()
    print(doc)
    d = parse(doc)
    print(d)


# Generated at 2022-06-13 19:50:59.845353
# Unit test for function parse
def test_parse():
    text = """Summary line.

Extended description.

:param arg1: Description of arg1
:param arg2: Description of arg2
:returns: Description of return value.
:raises keyError: raises an exception
    """
    print(parse(text))

# Generated at 2022-06-13 19:51:12.886554
# Unit test for function parse
def test_parse():

    from docstring_parser import parse
    from docstring_parser.styles import Style

    text = """
        This is a module docstring.

        Parameters
        ----------
        a : int
            this is an 'a' param.
        b : str
            this is a 'b' param.

        Returns
        -------
        None
        """

    text_with_blank = """
        This is a module docstring.


        Parameters
        ----------
        a : int
            this is an 'a' param.

        b : str
            this is a 'b' param.


        Returns
        -------
        None
        """


# Generated at 2022-06-13 19:51:23.160162
# Unit test for function parse
def test_parse():
    text = """
This is a test docstring.

:param a: test a
:param b: test b
:type b: int
:returns: a + b
:rtype: int
"""

    doc = parse(text)
    assert len(doc.params) == 2
    assert len(doc.returns) == 1
    assert doc.returns[0].type_name == 'int'
    assert doc.returns[0].desc == 'a + b'

    doc = parse(text, Style.numpy)
    assert len(doc.params) == 2
    assert len(doc.returns) == 1
    assert doc.returns[0].type_name == 'int'
    assert doc.returns[0].desc == 'a + b'

    doc = parse(text, Style.google)