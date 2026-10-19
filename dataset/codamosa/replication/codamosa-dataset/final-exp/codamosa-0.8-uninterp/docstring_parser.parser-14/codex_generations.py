

# Generated at 2022-06-13 19:41:36.908197
# Unit test for function parse
def test_parse():
    doc = parse("""\
A simple, yet handy tool for parsing docstrings.

:param str text: docstring text to parse
:param Style style: docstring style
:returns: parsed docstring representation
:raises ParseError: when there is syntax error""")

    assert doc.short_description == "A simple, yet handy tool for parsing docstrings."
    assert doc.long_description == ""
    assert len(doc.params) == 2
    assert doc.params[0] == ("text", "docstring text to parse")
    assert doc.params[1] == ("style", "docstring style")
    assert doc.returns == "parsed docstring representation"
    assert doc.raises == "ParseError: when there is syntax error"
    assert len(doc.meta) == 2

# Generated at 2022-06-13 19:41:39.311795
# Unit test for function parse
def test_parse():
    return parse(
        """ This is a sample docstring.

        :param x: this is a parameter named x
        :param y: this is a parameter named y

        :returns: this is a return value.
        """,
    )


# Generated at 2022-06-13 19:41:44.944741
# Unit test for function parse
def test_parse():
    text = '''Description
    Description

    Parameters
    ----------
    n : int
        length of the timeseries of observation
    d : int
        number of features

    Returns
    -------
    x : ndarray, shape (n,d)
        simulated sequence of observations
    z : ndarray, shape (n)
        simulated sequence of states
    q : ndarray, shape (n)
        simulated sequence of durations
    '''

    ds = parse(text)
    assert len(ds.meta) == 1
    assert len(ds.sections) == 3
    assert ds.sections[0].name == 'Description'
    assert len(ds.sections[1].content) == 4
    assert ds.sections[1].name == 'Parameters'
    assert len(ds.sections[2].content) == 1


# Generated at 2022-06-13 19:41:54.111981
# Unit test for function parse
def test_parse():
    assert (parse('', style=Style.google).summary == '')
    assert (parse('''
    Args:
        a:
            a
            a
        b:
            b
            b''', style=Style.numpy).params["b"].description == 'b\nb')

    assert (parse('.. code-block::\n\na', style=Style.google).code_block == 'a')
    assert (parse('.. code-block::\n\na', style=Style.rst).code_block == 'a')
    assert (parse('.. code-block::\n\na', style=Style.rd) == None)
    assert (parse('.. code-block::\n\na', style=Style.epytext).code_block == 'a')

# Generated at 2022-06-13 19:41:56.954812
# Unit test for function parse
def test_parse():
    text = """This is a random string"""
    p = parse(text)
    assert isinstance(p, Docstring)

    text = """This 
        is another
        string"""
    p = parse(text)
    assert isinstance(p, Docstring)

test_parse()

# Generated at 2022-06-13 19:42:06.118538
# Unit test for function parse

# Generated at 2022-06-13 19:42:11.224799
# Unit test for function parse
def test_parse():
        """Test the docstring parsing function.
        """
        text= " the description.\n\nArgs:\n    param1:\n        descr1.\n    param2:\n        descr2. "
        d = parse(text)
        assert d.short_description == "the description."
        assert d.long_description == "the description."
        assert d.params['param1'] == "descr1."
        assert d.params['param2'] == "descr2."

# Generated at 2022-06-13 19:42:24.896485
# Unit test for function parse
def test_parse():
    """Unit test for function parse."""
    text = """Summary line.

Extended description.

Parameters
----------
arg1 : int
    Description of `arg1`
arg2 : str
    Description of `arg2`
Returns
-------
str
    Description of return value.
"""
    doc = parse(text)
    assert doc.summary == 'Summary line.'
    assert doc.description == 'Extended description.'
    assert doc.meta['arg1'].argname == 'arg1'
    assert doc.meta['arg1'].argtype == 'int'
    assert doc.meta['arg1'].description == 'Description of `arg1`'
    assert doc.meta['arg2'].argname == 'arg2'
    assert doc.meta['arg2'].argtype == 'str'

# Generated at 2022-06-13 19:42:26.830854
# Unit test for function parse
def test_parse():
    assert len(parse("hi").short_description) == 2
    assert len(parse("hi").short_description) == 2

# Generated at 2022-06-13 19:42:35.985205
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleStyle
    text = """
    This is a long description
    """
    assert parse(text) == Docstring(
        description='This is a long description',
        meta={},
        returns=None,
    )
    assert parse(text, style=Style.numpy) == Docstring(
        description='This is a long description',
        meta={},
        returns=None,
    )
    assert parse(text, style=Style.google) == Docstring(
        description='This is a long description',
        meta={},
        returns=None,
    )
    assert parse(text, style=GoogleStyle) == Docstring(
        description='This is a long description',
        meta={},
        returns=None,
    )


if __name__ == "__main__":
    test

# Generated at 2022-06-13 19:42:42.832252
# Unit test for function parse
def test_parse():
    result = parse.__doc__
    assert result == '''Parse the docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    '''

# Generated at 2022-06-13 19:42:51.142310
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()

    assert parse("one") == Docstring(short="one", body=[])

    assert parse("one\n\ntwo\n") == Docstring(short="one", body=["two"])

    assert parse("one\n\ntwo\n\nthree\n") == Docstring(short="one", body=["two", "three"])

    assert parse("one\n\n    two\n") == Docstring(short="one", body=["two"])

    assert parse("one\n\n    two\n\n    three\n") == Docstring(short="one", body=["two", "three"])

    assert parse("one\n\n    two\n\nthree\n") == Docstring(short="one", body=["two", "three"])

    assert parse

# Generated at 2022-06-13 19:43:01.170755
# Unit test for function parse
def test_parse():
    text = """
    :param port: The port to listen on.
    :param str host: The host to listen on. Defaults to 127.0.0.1
    :param bool debug: Whether to start the debugger.
    """
    ds = parse(text)
    assert ds.params[0].arg_name == "port"
    assert ds.params[0].description == "The port to listen on."
    assert ds.params[1].arg_name == "host"
    assert ds.params[1].description == "The host to listen on. Defaults to 127.0.0.1"
    assert ds.params[1].type_name == "str"
    assert ds.params[2].arg_name == "debug"

# Generated at 2022-06-13 19:43:13.063418
# Unit test for function parse
def test_parse():
    text = '''
    This is an example.

    Args:
        arg1 (int): The first value.
        arg2 (str): The second value.

    Returns:
        int: The return value.

    Raises:
        TypeError: The exception type.
        ValueError: The exception type.
    '''
    docstring = parse(text)
    for attr in ['short_description', 'long_description', 'meta', 'returns', 'raises']:
        assert hasattr(docstring, attr)
    assert docstring.short_description == 'This is an example.'
    assert docstring.long_description == 'This is an example.'

# Generated at 2022-06-13 19:43:24.197336
# Unit test for function parse
def test_parse():
    text = '''\
    Docstring for a function.

    Parameters
    ----------
    arg1 : int
        Description of arg1.

    Returns
    -------
    None.
    '''

    from docstring_parser.styles import NumpyStyle
    docstring = parse(text, style=NumpyStyle)

    assert docstring.short_description == 'Docstring for a function.'
    assert docstring.long_description == ''
    assert len(docstring.sections) == 3
    assert docstring.sections[0].title == 'Parameters'
    assert len(docstring.sections[0].content) == 1
    assert docstring.sections[0].content[0].arg_name == 'arg1'
    assert docstring.sections[0].content[0].type_name == 'int'

# Generated at 2022-06-13 19:43:29.756284
# Unit test for function parse
def test_parse():
    text = """\
    MyClass

    Parameters
    ----------
    x : int

    Attributes
    ----------
    attr : bool

    """
    assert len(parse(text).attributes) == 1
    assert len(parse(text, style=Style.numpy).sections) == 3
    assert len(parse(text).attributes) == 0
    assert len(parse(text, style=Style.google).sections) == 3

# Generated at 2022-06-13 19:43:42.819612
# Unit test for function parse
def test_parse():
    """Unit test for function parse."""


# Generated at 2022-06-13 19:43:53.272525
# Unit test for function parse
def test_parse():
    """This function tests if parse function works well"""
    docstring = """\
Description:
    Blabla bla.

Parameters
-----------
    arg1 : int
        blabla bla.
    arg2 : numpy.ndarray
        blabla bla.
"""

    parsed_docstring = parse(docstring)


# Generated at 2022-06-13 19:44:01.883887
# Unit test for function parse
def test_parse():
    text1 = '''This is my docstring
    @params x the first parameter
    @params y the second parameter
    @returns x squared
    '''
    text2 = '''This is my docstring
    :param x: the first parameter
    :param y: the second parameter
    :returns: x squared
    '''
    test1 = parse(text1)
    test2 = parse(text2)
    assert test1.summary == 'This is my docstring'

# Generated at 2022-06-13 19:44:05.446517
# Unit test for function parse
def test_parse():
    print('Testing unit for function parse...', end=' ')
    import doctest
    doctest.testmod()
    print('Done.')

if __name__ == '__main__':
    print(parse(sys.argv[1]))
    test_parse()

# Generated at 2022-06-13 19:44:11.204100
# Unit test for function parse
def test_parse():
    from doctest import testmod
    
    testmod(parse, raise_on_error=True)

# Generated at 2022-06-13 19:44:17.793215
# Unit test for function parse
def test_parse():
    # Test case:
    test_string = """
    Parse the docstring text into its components.

    Args:
        docstring_text: docstring text to parse
        style: docstring style, e.g. numpy, google, sphinx
        config:
            delimiters:
                parameter: ~
            spaces:
                at_code_begin: 1

    Yields:
        parsed components

    Raises:
        ParseError: if parsing failed
    """
    # Expected output:

# Generated at 2022-06-13 19:44:22.567752
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleStyle
    # input
    text = "This is a GoogleStyle docstring"
    style = GoogleStyle
    # output
    parse(text, style)
    assert(text.__class__ == str)
    assert(style.__class__ == type)

# Generated at 2022-06-13 19:44:28.190745
# Unit test for function parse
def test_parse():
    test_string = """The main parsing routine.
    @param text: docstring text to parse
    @param style: docstring style
    @returns: parsed docstring representation
    """
    assert parse(test_string, Style.google) == parse(test_string, Style.auto)



# Generated at 2022-06-13 19:44:36.078334
# Unit test for function parse
def test_parse():
    text = """A simple first line.

This is an example of a multiline
docstring.

:param str arg1: The first command line argument.
:param int arg2: The second command line argument.
:returns: Description of return value.
:raises Exception1: Description of exception.
:raises Exception2: Description of exception.
:raises Exception3: Description of exception.

Some more description.
Some more description.
Some more description.
"""
    docstring = parse(text)
    assert docstring.summary == 'A simple first line.'
    assert docstring.description == 'This is an example of a multiline\ndocstring.'
    assert docstring.extended_summary == 'Some more description.\nSome more description.\nSome more description.\n'

# Generated at 2022-06-13 19:44:42.708743
# Unit test for function parse
def test_parse():
    docstring = """Returns the sum of two numbers.
    :param x: first number
    :param y: second number
    :returns: the sum
    """
    result = parse(docstring, Style.auto)
    assert result.short_description == "Returns the sum of two numbers."
    assert result.long_description == ""
    assert result.params["x"] == "first number"
    assert result.params["y"] == "second number"
    assert result.returns == "the sum"

# Generated at 2022-06-13 19:44:51.205670
# Unit test for function parse
def test_parse():
    """Unit test for function parse."""

    from docstring_parser.styles import GoogleStyle
    g = GoogleStyle()
    docstring = """
    This is an example of Google style.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    """
    doc = g(docstring)
    print(doc.short_description)
    print(doc.long_description)
    print(doc.meta)
    assert doc.meta['Args'] == 'The first parameter.'


### Import Guard

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:44:55.129720
# Unit test for function parse
def test_parse():
    d = parse("""This is a function.

Args:
    a (str): A string.

Returns:
    str: A string.
    """)
    assert d.short_description == 'This is a function.'
    assert len(d.params) == 1
    assert d.params['a'].description.strip() == 'A string.'
    assert len(d.returns) == 1
    assert d.returns['str'].description.strip() == 'A string.'

# Generated at 2022-06-13 19:44:58.320046
# Unit test for function parse
def test_parse():
    docstring = """
    This is a docstring
    :param name: some name
    :type name: str
    :returns: name
    :rtype: str
    """
    parsed = parse(docstring)
    assert len(parsed.meta) == 2
    assert len(parsed.content) == 2

# Generated at 2022-06-13 19:45:05.120660
# Unit test for function parse
def test_parse():
    """
    Unit test function
    """
    docstring = """
    This is a function.

    Parameters
    ----------
    arg1 : int
        The first argument.
    arg2 : str
        The second argument.

    Returns
    -------
    str
        The return value.

    Raises
    ------
    AttributeError
        The `AttibuteError` exception.
    """
    print(parse(docstring))

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:45:21.021160
# Unit test for function parse
def test_parse():
    docs = "Goat"
    assert parse(docs) == parse(docs, Style.google)
    assert parse(docs, Style.numpy) == parse(docs, Style.auto)
    docs = "Goat\n:param: name"
    assert parse(docs) == parse(docs, Style.google)
    assert parse(docs, Style.numpy) == parse(docs, Style.auto)
    docs = "Goat\n:type name: str"
    assert parse(docs) == parse(docs, Style.numpy)
    assert parse(docs, Style.numpy) == parse(docs, Style.auto)

# Generated at 2022-06-13 19:45:28.725842
# Unit test for function parse
def test_parse():
    print('\nUnit test for parse()')
    print("Testing parse() using dry test...")
    text = """Ternary operator.

    :param x: condition expression
    :param y: value if condition is true
    :param z: value if condition is false
    :returns: either y or z based on condition
    """
    style = Style.auto
    print("  text=%s\n  style=%s" % (text, style))
    print("  parse(text, style)=%s" % parse(text, style))


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:45:33.663815
# Unit test for function parse
def test_parse():
    text = '''This is a test docstring.

    :param test_param1: str
    :param test_param2: str
    :returns: hello'''
    docstring = parse(text)

    assert docstring.short_description == 'This is a test docstring.'
    assert len(docstring.long_description) == 0
    assert len(docstring.params) == 2
    assert len(docstring.returns) == 1


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:45:44.146145
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import Google

    text = \
"""Author: John Doe.

Args:
    param1: The first parameter.
    param2: The second parameter.

Returns:
    bool: The return value. True for success, False otherwise.
"""
    
    docstring = parse(text)
    
    assert len(docstring.meta) == 4
    assert docstring.content == "Author: John Doe."
    assert docstring.short_description == "Args: ..."
    assert docstring.long_description == "Args: ...\nReturns: ..."
    assert str(docstring) == text
    
    assert docstring.get_section('args')
    assert docstring.get_section('param1')
    assert docstring.get_section('param2')

# Generated at 2022-06-13 19:45:49.638992
# Unit test for function parse
def test_parse():

    text = '''
    Hello World
    ===========

    This is a sample docstring.

    Parameters
    ----------
    a: int
        This is a.
    b: float
        This is b.

    Returns
    -------
    int
        0.
    '''
    ds = parse(text)
    assert ds.summary == 'Hello World'
    assert ds.description == 'This is a sample docstring.'
    assert ds.metada

# Generated at 2022-06-13 19:45:51.753826
# Unit test for function parse
def test_parse():
    assert(parse("""
        """)) == Docstring(short_description='', long_description='', meta=None, examples=[])


# Generated at 2022-06-13 19:45:55.287758
# Unit test for function parse
def test_parse():
    from textwrap import dedent
    docstring = dedent("""
        Sum two numbers
        """
        )
    docparse = parse(docstring)
    assert (docparse.short_description == 'Sum two numbers')

test_parse()

# Generated at 2022-06-13 19:46:03.004108
# Unit test for function parse
def test_parse():
    text = """
    A function that runs a lot of stuff.
    May be slow.
    You can even use it to turn the earth around.

    Parameters
    ----------
    arg1 : str
        The first argument.
    arg2 : int
        The second argument.
    longarg : float
        This argument is very long. Blah blah.
        Blah blah.

    Returns
    -------
    str
        A cheese.
    """
    parse(text)
    assert False


# Generated at 2022-06-13 19:46:06.410818
# Unit test for function parse
def test_parse():
    assert parse('a') == parse('a', style=Style.numpy)
    assert parse('a', style=Style.auto) == parse('a', style=Style.numpy)
    assert parse('a', style=Style.sphinx) == parse('a', style=Style.numpy)
    assert parse('a', style=Style.google) == parse('a', style=Style.numpy)



# Generated at 2022-06-13 19:46:16.499101
# Unit test for function parse
def test_parse():
    docstring = parse("""\
        A square with width & height of 1 unit.

        Parameters
        ----------
        x : float
            The x-coordinate of the upper left hand corner of the square.
        y : float
            The y-coordinate of the upper left hand corner of the square.
        """)

    assert len(docstring.meta) == 2
    assert docstring.meta[0].name == "x"
    assert docstring.meta[0].type_name == "float"
    assert docstring.meta[0].description == "The x-coordinate of the upper left hand corner of the square."
    assert docstring.meta[1].name == "y"
    assert docstring.meta[1].type_name == "float"

# Generated at 2022-06-13 19:46:33.857563
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleStyle
    import textwrap
    s = """Summary line.
    Extended description.
    Args:
    arg1 (int): Description of `arg1`
    arg2 (str): Description of `arg2`
    Returns:
    str. Description of return value.
    """
    s = textwrap.dedent(s)
    d = parse(s)
    assert d.short_description == 'Summary line.'
    assert d.long_description == 'Extended description.'
    assert d.returns[0].type_name == 'str'
    assert d.returns[0].description == 'Description of return value.'
    assert type(d) == GoogleStyle

# Generated at 2022-06-13 19:46:35.109442
# Unit test for function parse
def test_parse():
    pass

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:46:41.708406
# Unit test for function parse
def test_parse():
    test_docstring = """One line summary.

Further description.

:param foo: Description of foo.
:param bar: Description of bar.
:returns: Description of return value.
:raises ValueError: If something wrong happens.
:raises NotImplementedError: If something missing happens.
"""

    result = parse(test_docstring)
    
    expected = Docstring(summary='One line summary.',
                         description='Further description.',
                         params={'foo': 'Description of foo.',
                                 'bar': 'Description of bar.'},
                         returns='Description of return value.',
                         raises={'ValueError': 'If something wrong happens.',
                                 'NotImplementedError': 'If something missing happens.'})
    
    assert result == expected


# Generated at 2022-06-13 19:46:45.145791
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    text = """
    This is a first line.
    This is a second line.
    """
    parse(text, Style.javadoc)

# Generated at 2022-06-13 19:46:57.657675
# Unit test for function parse
def test_parse():
    text_napoleon = '''
        This is a docstring.

        :param foo: bar
        :return: baz
    '''
    text_sphinx = '.. This is a docstring.\n\n:param foo: bar\n:return: baz'
    text_google = 'The method name.\n\nArgs:\n    foo: bar\n\nReturns:\n    baz\n'
    text_numpy = 'The method name.\n\nParameters\n----------\nfoo : bar\n\nReturns\n-------\nbaz\n'
    text_numpy_old = 'The method name.\n\nParameters:\n    foo : bar\n\nReturns:\n    baz\n'


# Generated at 2022-06-13 19:47:06.761761
# Unit test for function parse
def test_parse():
    test_cases = [
        (
            '', # test case
            '', # expected result
            [] # params
        ),
        (
            'asdf', # test case
            'asdf', # expected result
            [] # params
        ),
        (
            'asdf',  # test case
            'asdf',  # expected result
            [{}] # params
        ),
    ]
    for test_case, expected_result, params in test_cases:
        assert parse(test_case, *params) == expected_result

# Generated at 2022-06-13 19:47:18.160937
# Unit test for function parse
def test_parse():
    assert parse('Multi-line  docstring')
    assert parse("""
    Multi-line
    docstring with extra leading and trailing lines
    """)
    assert parse("""
    Multi-line
    docstring with extra leading and trailing lines
    """.strip())
    assert parse("""
        Multi-line
        docstring with extra leading lines.
    """)
    assert parse("""
    Multi-line
    docstring with extra trailing lines.
        """)
    assert parse("""
        Multi-line
        docstring with extra leading and trailing lines.
        """.strip())
    assert parse("""
    Multi-line
    docstring with extra leading and trailing lines.
    """.strip())
    assert parse("""
    A single-line docstring.
    """)



# Generated at 2022-06-13 19:47:24.441116
# Unit test for function parse
def test_parse():
    text = """Some random text without any docstring.
    """
    #assert None == parse(text)
    #assert None == parse(text, style=Style.google)
    #assert None == parse(text, style=Style.numpy)
    assert None == parse(text, style=Style.auto)

    text = """Some random text without
    any docstring.
    """
    #assert None == parse(text)
    #assert None == parse(text, style=Style.google)
    #assert None == parse(text, style=Style.numpy)
    assert None == parse(text, style=Style.auto)

    text = """Random text with a
    few lines.
    """
    #assert None == parse(text)
    #assert None == parse(text, style=Style.google)
    #assert None == parse

# Generated at 2022-06-13 19:47:33.664861
# Unit test for function parse
def test_parse():
	docstring = """This is a test

@param param1 This is a param1
@param param2 This is a param2
@return This is the return value
"""
	parsed_docstring = parse(docstring, style = Style.sphinx)
	assert parsed_docstring.short_description == "This is a test"
	assert parsed_docstring.long_description == ""
	assert parsed_docstring.sections[0].heading == "Args"
	assert parsed_docstring.sections[0].get_param("param1").name == "param1"
	assert parsed_docstring.sections[0].get_param("param1").description == "This is a param1"
	assert parsed_docstring.sections[0].get_param("param2").name == "param2"

# Generated at 2022-06-13 19:47:45.768114
# Unit test for function parse
def test_parse():
    print("\n# Testing function parse...")

    # Test style auto
    text = """Unit test for function parse.
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    doc = parse(text,Style.auto)
    print("Test case 1:")
    print("Expected output:")
    print("[('Unit test for function parse.\n    :param text: docstring text to parse\n    :param style: docstring style\n    :returns: parsed docstring representation\n    ', 'google', {'param': [('text', 'docstring text to parse'), ('style', 'docstring style')], 'returns': ['parsed docstring representation']})]")
    print("Actual output:")
    print(doc.description)

# Generated at 2022-06-13 19:48:00.131677
# Unit test for function parse
def test_parse():
    assert parse('') == Docstring()
    assert parse('', Style.google) == Docstring()
    assert parse('', Style.numpy) == Docstring()
    assert parse('', Style.auto) == Docstring()

    text = 'Test docstring. This text should be parsed.'
    assert parse(text) == Docstring(text=text)
    assert parse(text, Style.google) == Docstring(text=text)
    assert parse(text, Style.numpy) == Docstring(text=text)
    assert parse(text, Style.auto) == Docstring(text=text)

    text = 'one line'
    assert parse(text, Style.google) == Docstring(text=text)
    assert parse(text, Style.numpy) == Docstring(text=text)
    assert parse(text, Style.auto)

# Generated at 2022-06-13 19:48:09.435273
# Unit test for function parse
def test_parse():
    """Parse a docstring."""
    # pylint: disable=missing-function-docstring
    assert parse('Hello, world!') == Docstring(content=['Hello, world!'])
    assert (parse('Hello, world!\n') ==
            Docstring(content=['Hello, world!']))
    assert (parse('Hello, world!\n\n') ==
            Docstring(content=['Hello, world!']))
    assert (parse('Hello, world!\n\n\n') ==
            Docstring(content=['Hello, world!']))



# Generated at 2022-06-13 19:48:12.867224
# Unit test for function parse
def test_parse():
    try:
        print(parse("""
           Hello world!!
        """))
    except ParseError as e:
        print(e)

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:48:21.077657
# Unit test for function parse
def test_parse():
    docstring = """
    Short Description
    
    Long Description
    
    :Arguments:
    
    -   **first**: description of the first parameter.
    -   **second**: description of the second parameter.
    -   **third**: description of the third parameter.

    :Return: The return value is `None`.

    :Raise: The raised value is `None`.

    """
    doc = parse(docstring)
    assert doc.meta['first']['type'] == 'param'
    assert doc.meta['second']['type'] == 'param'
    assert doc.meta['third']['type'] == 'param'
    assert doc.returns['type'] == 'return'
    assert doc.raises['type'] == 'raise'

# Generated at 2022-06-13 19:48:23.357517
# Unit test for function parse
def test_parse():
    marker = parse('Habitat\n----\n\n**Habitat**:\n\n\n\t\tAn introduction.')
    assert marker.meta['habitat'] == 'An introduction.'

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:48:28.223177
# Unit test for function parse
def test_parse():
    import unittest

    class test_parse(unittest.TestCase):
        def test_parse(self):
            # self.assertEqual(expected, parse(*, style=Style.auto))
            assert False # TODO: implement your test here


# Generated at 2022-06-13 19:48:39.789588
# Unit test for function parse
def test_parse():
    from docstring_parser.styles.sphinx import GoogleStyle
    def demo():
        """This is a unit test for function parse.

        Args:
            arg1: A positional argument.
            arg2 (int): An int argument.
            arg3 (:obj:`int`): Another int argument.

        Returns:
            True: if test succeeds.

        Raises:
            ValueError: If ``arg2`` is equal to ``arg3``.

        """
        if arg2 == arg3:
            raise ValueError('arg2 and arg3 cannot be equal!')
        return True

    docstring = parse(demo.__doc__, style=Style.sphinx)
    assert isinstance(docstring, GoogleStyle)

# Generated at 2022-06-13 19:48:48.554176
# Unit test for function parse
def test_parse():
    s = "One-line summary and a multi-line description.\n\n:param str name: Person's name\n:param int age: Person's age\n:return: A greeting as str."
    d = parse(s)
    assert d.short_description == "One-line summary and a multi-line description."
    assert d.long_description == ""
    assert len(d.meta) == 2
    for name, value in d.meta.items():
        if name.arg_name == "name":
            assert value.arg_type == "str"
            assert value.description == "Person's name"
        elif name.arg_name == "age":
            assert value.arg_type == "int"
            assert value.description == "Person's age"
    assert d.returns.arg_type == "str"


# Generated at 2022-06-13 19:48:58.644760
# Unit test for function parse
def test_parse():
    d = parse("""
    Parse the docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """)
    assert d.short_description == 'Parse the docstring into its components.'
    assert len(d.long_description) == 1
    assert d.meta['returns'].arg_type == 'return'
    assert d.meta['text'].arg_type == 'param'
    assert d.meta['style'].arg_type == 'param'
    assert d.meta['returns'].description == 'parsed docstring representation'


# Generated at 2022-06-13 19:49:01.136831
# Unit test for function parse
def test_parse():
    doc1 = parse(
        """This is a test module""", Style.google
    )

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:49:17.598719
# Unit test for function parse
def test_parse():
    doc1 = """Summary line.
    Extended description.

    Args:
        arg1: First argument.
        arg2: Second argument.

    Returns:
        Description of return value.
    """
    doc2 = """Summary line.
    Args:
        arg1: First argument.
    """
    doc3 = """
    Args:
        arg1: First argument.
    """

    print(parse(doc1, style = Style.numpy))
    print(parse(doc2, style = Style.numpy))
    print(parse(doc3, style = Style.numpy))
    print(parse(doc1, style = Style.google))
    print(parse(doc2, style = Style.google))
    print(parse(doc3, style = Style.google))

# Generated at 2022-06-13 19:49:18.253033
# Unit test for function parse
def test_parse():
    """Test the function parse"""
    pass

# Generated at 2022-06-13 19:49:29.502571
# Unit test for function parse
def test_parse():
    from docstring_parser.docstring import Docstring

# Generated at 2022-06-13 19:49:37.005464
# Unit test for function parse
def test_parse():
    docstring = '''
    Test parse Docstring
    :param test: test param
    :returns: test return
    '''
    # test parse
    try:
        test_content = parse(docstring)
        assert test_content.summary == "Test parse Docstring"
        print("Test parse:", test_content.summary)
    except Exception as e:
        print("Error: parse function failed")
    print("Test ok: parse")

# Generated at 2022-06-13 19:49:51.236809
# Unit test for function parse
def test_parse():
    assert parse('hello world') == Docstring(
        summary='hello world',
        description='',
        extended_summary='',
        body='',
        returns=None,
        raises=None,
        meta={})

    summary = 'This is the summary'
    description = '''
        This is the description.

        It can span multiple lines.

        Note that the indentation of the description is not significant.
        '''

    extended_summary = '''
        This is the extended summary.

        It can span multiple lines.

        Note that the indentation of the description is not significant.
        '''

    params = [
        ('arg1', 'This is the description for arg1.'),
        ('arg2', 'This is the description for arg2.'),
    ]


# Generated at 2022-06-13 19:49:52.419478
# Unit test for function parse
def test_parse():
    assert parse.__doc__ is not None

test_parse()

# Generated at 2022-06-13 19:49:56.091596
# Unit test for function parse
def test_parse():
    from docstring_parser import parse
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:49:57.458374
# Unit test for function parse
def test_parse():
    parse('test')

test_parse()

# Generated at 2022-06-13 19:50:04.859061
# Unit test for function parse
def test_parse():
    class Foo(object):
        """A sample class.

        Paragraph.

        Args:
            arg1: An argument.
        """

        def __init__(self, arg1):
            pass

    item = Foo('foo')
    text = item.__doc__

    parsed = parse(text)
    docstring = parsed.docstring()
    assert docstring.split('\n\n')[0] == 'A sample class.'
    assert parsed.summary == 'A sample class.'
    assert parsed.description == 'Paragraph.'

# Generated at 2022-06-13 19:50:12.983062
# Unit test for function parse

# Generated at 2022-06-13 19:50:29.100945
# Unit test for function parse
def test_parse():
    doc = """\
    My docstring

    :param a: argument a
    :type a: int
    :keyword b: keyword argument b
    :type b: str
    :raises ValueError: when a is 'wrong'

    * first item in a bulleted list
    * second item in a bulleted list
    with text flowing into next line

    1. first item in an enumerated list
    1. second item in an enumerated list
    again with text flowing into next line

    .. seealso:: other_function()
    """

    ret = parse(doc)
    assert ret.short_description == 'My docstring'

# Generated at 2022-06-13 19:50:40.894334
# Unit test for function parse
def test_parse():
    text = '''This is the summary

:param param1: This is the first parameter.
:type param1: str
:param param2: This is a second parameter.
:type param2: str
:returns: This is what is returned
:rtype: bool
:raises keyError: This is a description of a raised exception
:raises ImportError: This is a description of another raised exception
:raises DeprecationWarning: This is a description of another raised exception
:raises NotImplementedError: This is a description of another raised exception
:raises RuntimeError: This is a description of another raised exception
:raises PendingDeprecationWarning: This is a description of another raised exception
'''
    doc = parse(text)
    print(doc.short_description)
    print(doc.long_description)

# Generated at 2022-06-13 19:50:44.829091
# Unit test for function parse
def test_parse():
    text = "This module provides a simple command line interface."
    result = parse(text)
    assert result.short_description == text
    #     assert result.long_description.startswith('If called with a')



# Generated at 2022-06-13 19:50:54.973947
# Unit test for function parse
def test_parse():
    text = '''
        :param elems: elements
        :type elems: list/dict
        :param is_valid: is valid
        :type is_valid: bool
        :returns: bool -- True if is valid, False otherwise
        :raises ValueError: if elems is not valid

        Example:
            >>> validate_elems(['a', 'b', 'c'])
            True
            >>> validate_elems('a')
            Traceback (most recent call last):
            ValueError: elems is not a list or dict
    '''

    ret = parse(text)
    assert ret.short_description == ''
    assert len(ret.params) == 2
    assert len(ret.returns) == 1
    assert len(ret.meta) == 3
    assert len(ret.raises) == 1
   

# Generated at 2022-06-13 19:51:07.069685
# Unit test for function parse
def test_parse():
    """
    Unit test for function parse.
    """

    from docstring_parser.common import Docstring
    from docstring_parser import DocstringStyle
    docstring = """Summary line.

        Extended description.

        Parameters
        ----------
        arg1 : int
            Description of `arg1`
        arg2 : str
            Description of `arg2`

        Returns
        -------
        int
            Description of return value
        """
    expected = Docstring(
        'Summary line.\n\n    Extended description.\n    ',
        {
            'arg1': 'Description of `arg1`',
            'arg2': 'Description of `arg2`'
        },
        'Description of return value'
    )
    assert parse(docstring, DocstringStyle.numpy) == expected

# Generated at 2022-06-13 19:51:17.207387
# Unit test for function parse
def test_parse():
    text = """**Summary:**
         A test function
        **Examples:**
        >>> a = np.array([1, 2, 3])
        >>> a = a.ravel()
        **Parameters:**
        :param t: "test"
        :type t: str
        :returns: None
        """
    doc = parse(text)

    assert doc.summary == "A test function"
    assert doc.example == ">>> a = np.array([1, 2, 3])\n>>> a = a.ravel()"
    assert doc.parameters == [("t", "test", "str")]
    assert doc.returns == "None"

