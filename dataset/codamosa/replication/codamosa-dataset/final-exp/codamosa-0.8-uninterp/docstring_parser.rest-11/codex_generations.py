

# Generated at 2022-06-13 19:52:27.288184
# Unit test for function parse
def test_parse():
    test_string = '''
        Example docstring.

        :param a: An integer.
        :param b: Optional string. Defaults to "None".
        :raises ValueError: if a negative integer is passed
        :returns: bool
        :returns: int
    '''
    docstring = parse(test_string)
    assert docstring.short_description == "Example docstring."
    assert docstring.long_description == '''
        :param a: An integer.
        :param b: Optional string. Defaults to "None".
        :raises ValueError: if a negative integer is passed
        :returns: bool
        :returns: int
    '''.strip()
    assert docstring.meta[0].arg_name == 'a'
    assert docstring.meta[0].description == 'An integer.'


# Generated at 2022-06-13 19:52:35.930001
# Unit test for function parse

# Generated at 2022-06-13 19:52:46.050478
# Unit test for function parse
def test_parse():
    docstring = """
    This is for testing the parsing of docstrings.
    This is the long description.

    This is new paragraph in the long description.

    :param a: Description of argument a
    :type a: int
    :param b: Description of argument b
    :type b: str
    :returns: Description of return value.
    :rtype: bool
    :raises ValueError: Description of what causes ValueError to be raised
    :raises TypeError: Description of what causes TypeError to be raised

    """

    ds = parse(docstring)
    assert ds.short_description == "This is for testing the parsing of docstrings."
    assert ds.blank_after_short_description
    assert not ds.blank_after_long_description

# Generated at 2022-06-13 19:52:56.159668
# Unit test for function parse
def test_parse():
    s = """
    Parse the ReST-style docstring into its components.

    :returns: parsed docstring
    """
    assert parse(s) == Docstring(
        short_description="Parse the ReST-style docstring into its components.",
        meta=[
            DocstringReturns(
                args=["returns"],
                description="parsed docstring",
                type_name=None,
                is_generator=False,
            )
        ],
    )

    s = """
    Parse the ReST-style docstring into its components.

    Returns the parsed docstring.
    """

# Generated at 2022-06-13 19:53:07.358846
# Unit test for function parse
def test_parse():
    text = """
    Short description.

    Long description
    with newlines.

    :param name: description
    :type name: str
    :param age:
        description
        with newlines
    :type age: int

    :returns: description
    :rtype: str
    """

# Generated at 2022-06-13 19:53:18.150102
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""

# Generated at 2022-06-13 19:53:24.863577
# Unit test for function parse
def test_parse():
    obj = parse.__code__
    assert parse(obj.co_consts[0]) == Docstring()
    assert parse(obj.co_consts[1]) == Docstring()
    assert parse(obj.co_consts[2]) == Docstring()
    assert parse(obj.co_consts[3]) == Docstring()


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:53:33.893352
# Unit test for function parse
def test_parse():
    assert parse("short description") == Docstring(
        short_description="short description"
    )
    assert parse("short description\n") == Docstring(
        short_description="short description"
    )
    assert parse("short description\n\n"
                 "long description") == Docstring(
        short_description="short description",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description="long description",
    )
    assert parse("short description\n\n"
                 "\n"
                 "long description") == Docstring(
        short_description="short description",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description="long description",
    )

# Generated at 2022-06-13 19:53:47.716236
# Unit test for function parse
def test_parse():
    """
    Tests that parse correctly:
      + handles empty docstrings correctly
      + correctly extracts the short description
      + correctly determines the number of blank lines between short and long descriptions
      + correctly extracts the long description
      + correctly parses all meta information
    """
    # Test for empty docstring
    docstring = parse(None)
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.meta == []

    # Test for docstring without meta information
    docstring = parse(
        """A function that adds x and y.

        :param x: The first number to add.
        :param y: The second number to add.
        """
    )
    assert docstring.short_description == "A function that adds x and y."

# Generated at 2022-06-13 19:54:00.770114
# Unit test for function parse
def test_parse():
    text = """
    Compute the algebraic connectivity of the graph.

    The algebraic connectivity is the second smallest eigenvalue of the
    Laplacian matrix of `G`.

    Parameters
    ----------
    G : graph
       A NetworkX graph

    Returns
    -------
    algebraic_connectivity : double
       Algebraic connectivity of `G`

    See Also
    --------
    laplacian_spectrum
    """
    docstring = parse(text)
    meta_params = docstring.meta[0]
    meta_returns = docstring.meta[1]

    assert docstring.short_description == "Compute the algebraic connectivity of the graph."
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description


# Generated at 2022-06-13 19:54:21.066237
# Unit test for function parse
def test_parse():
    from .common import Docstring
    from .syntax import python as python_syntax

    def build_docstring(text: str) -> Docstring:
        return Docstring(source_text=text)

    assert parse("") == build_docstring("")
    assert parse("\n") == build_docstring("\n")
    assert parse("    ") == build_docstring("    ")
    assert parse("\n\n") == build_docstring("\n\n")
    assert parse("    \n\n") == build_docstring("    \n\n")

    assert parse(
        "Do something."
    ) == build_docstring("Do something.")
    assert parse(
        "    Do something."
    ) == build_docstring("Do something.")

# Generated at 2022-06-13 19:54:28.113558
# Unit test for function parse
def test_parse():
    docstring = """
    This is short description.

    This is long description.

    :param foo:  It is a foo.
    :param bar=None: It is a bar.
    :type bar: str
    :returns: It is a return value.
    :rtype: str
    :raises ValueError: It raises the ValueError exception.
    """
    doc = parse(docstring)
    assert doc.short_description == 'This is short description.'
    assert doc.blank_after_short_description == True
    assert doc.long_description == 'This is long description.'
    assert doc.blank_after_long_description == True
    assert doc.meta[0].description == 'It is a bar.'
    assert doc.meta[0].arg_name == 'bar'

# Generated at 2022-06-13 19:54:34.168604
# Unit test for function parse

# Generated at 2022-06-13 19:54:45.205725
# Unit test for function parse
def test_parse():
    text = parse("""
    This is the summary line.

    This is the long description.
    """)
    assert text.long_description == "This is the long description."
    assert text.short_description == "This is the summary line."
    assert text.blank_after_short_description == False
    assert text.blank_after_long_description == False

    text = parse("""
    This is the summary line.

    This is the long description.

    """)
    assert text.long_description == "This is the long description."
    assert text.short_description == "This is the summary line."
    assert text.blank_after_short_description == False
    assert text.blank_after_long_description == True


# Generated at 2022-06-13 19:54:58.350626
# Unit test for function parse
def test_parse():
    d = """
    foo

    :param
    :returns
    """
    assert parse(d) == Docstring(
        short_description="foo",
        blank_after_short_description=True,
        long_description=None,
        blank_after_long_description=False,
        meta=[DocstringMeta(args=[], description="param"),
              DocstringMeta(args=[], description="returns")
              ],
    )

    d = """
    foo

    :param yep: thing
    :returns: nope
    """

# Generated at 2022-06-13 19:55:07.884838
# Unit test for function parse
def test_parse():
    '''
    test_parse(text)
    '''

# Generated at 2022-06-13 19:55:08.726276
# Unit test for function parse
def test_parse():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 19:55:18.431052
# Unit test for function parse
def test_parse():
    parse("""
    short description
    
    :param x: X
    """)
    parse("""
    short description
    
    :param x: X
    :param y: Y
    """)
    parse("""
    short description
    
    :param x: X
    :type x: A
    """)
    parse("""
    short description
    
    :param x: X
    :type x: A
    :param y:
    """)
    parse("""
    short description
    
    :param x: X
    :type x: A
    :param y: Y
    :type y: B
    """)

# Generated at 2022-06-13 19:55:29.634609
# Unit test for function parse
def test_parse():
    doc_string = '''
    This is a test docstring, it is multi-line.
    :param name: The name.
    :type name: str
    :param location: The location.
    :type location: str
    :returns: nothing
    :rtype: None
    '''
    doc = parse(doc_string)
    assert isinstance(doc, Docstring)
    assert isinstance(doc.short_description, str)
    assert doc.short_description == 'This is a test docstring, it is multi-line.'
    assert isinstance(doc.long_description, str)
    assert doc.long_description == ''
    assert doc.blank_after_short_description == True
    assert doc.blank_after_long_description == True

# Generated at 2022-06-13 19:55:35.654006
# Unit test for function parse

# Generated at 2022-06-13 19:55:48.880594
# Unit test for function parse
def test_parse():
    docstring_object = parse.__doc__
    # Checking the first 3 lines of docstring
    assert docstring_object.short_description == 'Parse the ReST-style docstring into its components.'
    assert docstring_object.blank_after_short_description == False
    assert docstring_object.long_description == ':returns: parsed docstring'
    # Checking if list of parameters is not empty
    assert len(docstring_object.meta) != 0
    for meta in docstring_object.meta:
        assert isinstance(meta, DocstringMeta)
        assert isinstance(meta.args, list)

# Generated at 2022-06-13 19:55:58.324740
# Unit test for function parse
def test_parse():
    docstring = """
    Short description.
    Long description.
    :param arg1: arg1 description.
    :type arg1: str
    :param arg2: arg2 description.
    :type arg2: str
    :rtype: str
    :returns: Return description.
    """

# Generated at 2022-06-13 19:56:14.480109
# Unit test for function parse
def test_parse():
    assert parse('') == Docstring()
    assert parse('abc 123') == Docstring(short_description='abc 123')
    assert parse('abc 123\n') == Docstring(
        short_description='abc 123',
        blank_after_short_description=True)
    assert parse('abc 123\n\n') == Docstring(
        short_description='abc 123',
        blank_after_short_description=True,
        blank_after_long_description=True)
    d = parse('abc 123\n\nxyz')
    assert d == Docstring(
        short_description='abc 123',
        blank_after_short_description=True,
        blank_after_long_description=True,
        long_description='xyz')

    d = parse(':param int a: Add a to x.')
    assert d

# Generated at 2022-06-13 19:56:24.340407
# Unit test for function parse
def test_parse():
    doc1 = """\
    A function for testing LSP docstring parsing.

    :param str arg1: The first argument.
    :param int arg2: The second argument. Defaults to 2.
    :return: The answer.
    :rtype: int
    :raises Exception: When an exception occurs.
    """

    doc2 = """\
    A function for testing LSP docstring parsing.

    Args:
        arg1 (str): The first argument.
        arg2 (int): The second argument. Defaults to 2.

    Returns:
        int: The answer.

    Raises:
        Exception: When an exception occurs.
    """


# Generated at 2022-06-13 19:56:34.263449
# Unit test for function parse
def test_parse():
    docstring = """
    This is a short description.

    This is a long description.

    :param foo: This is the first parameter.
    :type foo: bool
    :param bar: This is the second parameter.
    :type bar: str
    :return: This is the return value.
    :rtype: None
    """
    docstring = parse(docstring)
    assert docstring.short_description == "This is a short description."
    assert docstring.long_description == "This is a long description."
    assert len(docstring.meta) == 4
    assert isinstance(docstring.meta[0], DocstringParam)
    assert docstring.meta[0].arg_name == "foo"
    assert docstring.meta[0].type_name == "bool"

# Generated at 2022-06-13 19:56:46.547306
# Unit test for function parse
def test_parse():

    import unittest

    class TestParse(unittest.TestCase):
        def test_short_description(self):
            docstring = parse(
                """Lorem ipsum dolor sit amet, consectetur adipiscing elit."""
            )
            self.assertEqual(
                docstring.short_description,
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            )

        def test_long_description(self):
            docstring = parse(
                """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit."""
            )

# Generated at 2022-06-13 19:57:00.579490
# Unit test for function parse
def test_parse():
    docstring_v1 = """
    This is a test docstring

    :param name: the name of the item
    :param int rate: the rate in percent. Defaults to 15%
    :returns: the value of the item
    """

    docstring_v2 = """
    This is a test docstring

    :param name: the name of the item
    :param int rate: the rate in percent. Defaults to 15%
    :param int color: this is a test

    :returns: the value of the item
    """

    docstring_v3 = """
        A docstring.


        :param name: the name of the item
        :param int rate: the rate in percent. Defaults to 15%
        :raises ValueError: if value is invalid
        :returns: the value of the item
        """



# Generated at 2022-06-13 19:57:13.172505
# Unit test for function parse
def test_parse():
    docstring = """\
    Short description.

    More detailed description.

    :param arg1: argument one
    :param arg2: argument two
    :returns: something
    :raises ValueError: when arg1 == arg2
    :raises TypeError: when arg1 != arg2
    :raises: when arg2 != arg2
    :returns: something
    :yields: a thing
    """


# Generated at 2022-06-13 19:57:19.722453
# Unit test for function parse
def test_parse():
    test_docstring = """ shorter description

longer description

:param name: description of name
:param age: description of age
:returns: description of return value

"""
    result = parse(test_docstring)
    assert result.short_description == "shorter description"
    assert result.long_description == "longer description"
    assert result.blank_after_short_description == True
    assert result.blank_after_long_description == True
    assert result.meta[0].args[0] == "param"
    assert result.meta[0].args[1] == "name"
    assert result.meta[0].description == "description of name"
    assert result.meta[1].args[0] == "param"
    assert result.meta[1].args[1] == "age"

# Generated at 2022-06-13 19:57:30.758484
# Unit test for function parse
def test_parse():
    print("Testing parse")

    # test docstring with all possible formatting.
    assert parse.__doc__ == parse(parse.__doc__)

    # Test that all the docstring keys are correct and as expected.
    ds = parse.__doc__
    assert ds.short_description == "Parse the ReST-style docstring into its components."
    assert ds.blank_after_long_description == True
    assert ds.long_description == ":returns: parsed docstring"
    assert ds.blank_after_short_description == True
    assert ds.meta[0].args == ["returns"]
    assert ds.meta[0].arg_name == "parsed docstring"
    assert ds.meta[0].description == "parsed docstring"

# Generated at 2022-06-13 19:57:49.885214
# Unit test for function parse
def test_parse():
    doc = parse('''
    Parse the ReST-style docstring into its components.

    :param int x: The X coordinate.
    :param int y: The Y coordinate.
    :returns: parsed docstring
    :rtype: Docstring
    ''')

    assert doc.short_description == "Parse the ReST-style docstring into its components."
    assert doc.long_description == "The X coordinate.\nThe Y coordinate."
    assert doc.meta[0].type_name == "int"
    assert doc.meta[0].arg_name == "x"
    assert doc.meta[1].type_name == "int"
    assert doc.meta[1].arg_name == "y"
    assert doc.meta[2].type_name == "Docstring"


# Generated at 2022-06-13 19:58:02.601637
# Unit test for function parse
def test_parse():
    doc = inspect.cleandoc("""\
    Short description.

    Long description.

    :param int arg1: Parameter description
    :param arg2: Parameter description
    :returns: Return description
    :rtype: str
    :raises TypeError: Exception description
    :yields: Yield description
    :yields: float
    :cvar int cvar1: Variable description
    :ivar int ivar1: Variable description
    :vartype ivar1: int
    :keyword int kwarg1: Keyword argument description
    :keyword kwarg2: Keyword argument description
    :type kwarg2: int
    :kwarg int kwarg3: Keyword argument description
    """)

# Generated at 2022-06-13 19:58:10.120496
# Unit test for function parse
def test_parse():
    """Test ReST docstring parsing"""

    def test_case(text, result):
        assert parse(text) == result

    # TODO: Add more tests
    assert Docstring('Foo') == parse('''\
        Foo
        ''')
    assert Docstring('Foo', 'Bar') == parse('''\
        Foo

        Bar
        ''')
    assert Docstring('Foo', 'Bar', 'Baz') == parse('''\
        Foo
        :param foo: Foo
        Bar

        Baz
        ''')

# Generated at 2022-06-13 19:58:21.218862
# Unit test for function parse
def test_parse():
    """Unit test for function parse."""
    docstring = """\
        A very simple function.

        :param int x: A very important parameter.
        :param str y: A not so important parameter.
        :raises ValueError: if you get it wrong.
        """
    expected = Docstring()
    expected.short_description = "A very simple function."
    expected.long_description = "A very simple function."
    expected.blank_after_short_description = True
    expected.blank_after_long_description = False
    expected.meta.append(
        DocstringParam(
            args=["param", "int", "x"],
            description="A very important parameter.",
            arg_name="x",
            type_name="int",
            is_optional=None,
            default=None,
        )
    )


# Generated at 2022-06-13 19:58:29.815944
# Unit test for function parse

# Generated at 2022-06-13 19:58:41.211419
# Unit test for function parse
def test_parse():
    # Testing for parameters
    s = """The function foo takes two parameters.
    :param arg1: The first argument.
    :type arg1: string
    :param arg2: The 2nd argument.
    :type arg1: optional string, defaults to "default".

    :param arg3: The 3rd argument.
    :param arg4: The 4th argument.

    :param arg5: The 5th argument.
    :type arg5: str
    """
    docstring = parse(s)
    assert len(docstring.meta) == 5
    assert docstring.meta[0].arg_name == "arg1"
    assert docstring.meta[0].type_name == "string"
    assert docstring.meta[0].is_optional is False
    assert docstring.meta[1].arg_name == "arg2"

# Generated at 2022-06-13 19:58:57.318713
# Unit test for function parse
def test_parse():
    # empty docstring, nothing to parse
    docstring = parse("")
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.meta == []

    # only description
    docstring = parse("This is a description only docstring")
    assert docstring.short_description == "This is a description only docstring"
    assert docstring.long_description is None
    assert docstring.meta == []

    # both short and long descriptions
    docstring = parse("Short\n\nLong")
    assert docstring.short_description == "Short"
    assert docstring.long_description == "Long"
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description
    assert docstring.meta == []

    # short and long descriptions, with

# Generated at 2022-06-13 19:59:07.730443
# Unit test for function parse
def test_parse():
    """Use parse function to parse the docstring"""
    docstring = """
    You can parse a reStructuredText docstring with this function.

    :param int x: An interger.
    :param str y: A string.
    :rtype: dict
    :returns: This is a return type.
    """
    docstring = parse(docstring)
    assert docstring.short_description == "You can parse a reStructuredText docstring with this function."
    assert docstring.long_description == "An interger.\nA string.\n\nThis is a return type."
    assert docstring.meta[0].type_name == "int"
    assert docstring.meta[0].arg_name == "x"

# Generated at 2022-06-13 19:59:20.079460
# Unit test for function parse
def test_parse():
    # If a function is wrapped in a class, the name of the function will include the
    # class name, i.e. 'class.function'.  But if the function is not wrapped in a
    # class, then the function name will have no qualifiers, i.e. 'function'.
    # The following tests are designed to test both of these cases.
    def test():
        """
        test_parse short description
        :param int args0: test_parse positional parameter
        :type args1: str
        :param args1: test_parse keyword parameter
        :keyword args2: test_parse keyword parameter
        :type args2: str
        :returns:
        :rtype: None
        :raises ValueError:
        :yields:
        :ytype:
        """


# Generated at 2022-06-13 19:59:30.965345
# Unit test for function parse
def test_parse():
    text = """
        Short description.

        Long description.

        :param str test: A string parameter.
        :param int foo: A integer parameter.
        :raises ValueError: Raised when a value error occurs.
        :raises TypeError: Raised when a type error occurs.
        :returns: A string.
        """
    doc = parse(text)
    assert doc.short_description == "Short description."
    assert doc.blank_after_short_description
    assert not doc.blank_after_long_description
    assert doc.long_description == "Long description."
    assert len(doc.meta) == 5
    assert doc.meta[0].arg_name == "test" and doc.meta[0].type_name == "str"

# Generated at 2022-06-13 19:59:44.707556
# Unit test for function parse
def test_parse():
    # valid and invalid docstring
    assert parse("") == Docstring()
    assert parse("test") == Docstring(short_description='test')
    assert parse("test\n a") == Docstring(short_description='test', long_description='a')
    assert parse("test\n\ntest2") == Docstring(short_description='test', long_description='test2')
    assert parse("test\n\n\ntest2") == Docstring(short_description='test', long_description='\ntest2')
    assert parse("test\ntest2") == Docstring(short_description='test\ntest2')
    assert parse("test: Hello\n: test2") == Docstring(short_description='test: Hello', long_description=': test2')
    assert parse("test\n: Hello\n: test2")

# Generated at 2022-06-13 19:59:55.939532
# Unit test for function parse
def test_parse():
    # Basic test
    text = """quick brown fox
    jumps over the lazy dog

    :param a: foo
    :raises Exception: bar
    """
    ds = parse(text)
    assert ds.short_description == "quick brown fox"
    assert ds.long_description == "jumps over the lazy dog"
    assert ds.meta == [
        DocstringParam(
            args=["param", "a"], description="foo", arg_name="a", type_name=None, is_optional=False, default=None
        ),
        DocstringRaises(
            args=["raises", "Exception"], description="bar", type_name="Exception"
        ),
    ]

    # Test more options
    text = """quick brown fox
    jumps over the lazy dog

    :param int a: foo
    """


# Generated at 2022-06-13 20:00:07.211549
# Unit test for function parse
def test_parse():
    """Test parsing docstring :func:`parse`."""
    assert parse("") == Docstring()
    assert parse("Short description.") == Docstring(
        short_description="Short description."
    )
    assert parse("Short description.\n\nLong description.") == Docstring(
        short_description="Short description.",
        long_description="Long description.",
        blank_after_short_description=False,
        blank_after_long_description=False,
    )
    assert parse("Short description.\n Long description.") == Docstring(
        short_description="Short description.",
        long_description="Long description.",
        blank_after_short_description=True,
        blank_after_long_description=False,
    )

# Generated at 2022-06-13 20:00:19.659588
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    func = lambda a, b, c=1: None
    func.__doc__ = """
    Title

    :param a: The a parameter
    :type a: int
    :param b: The b parameter
    :type b: str
    :param c: The c parameter
    :returns: a + b + c
    :raises Exception: when anything goes wrong
    """

    docstr = parse(func.__doc__)
    # pylint: disable=line-too-long

# Generated at 2022-06-13 20:00:30.502742
# Unit test for function parse
def test_parse():
    """Test parse function for Rest."""
    docstring = """
    This is a normal function.

    :param a: This is a.
    :param b: This is b.
    :returns: return value.
    :return a + b
    """
    # docstring = ""
    # docstring = "\n\n"
    # docstring = "    \n    \n"
    # docstring = "    \n    \n    \n    \n"
    print(parse(docstring))
# test_parse()

# Generated at 2022-06-13 20:00:36.492399
# Unit test for function parse
def test_parse():
    # TODO: The docstring parsing does not handle nested quotes properly.
    # As an example, this test is failing because the default value for
    # the first parameter is being shown as:
    #
    #     ``"key " value``
    #
    # ... instead of
    #
    #     ``"key value"``
    #
    # This is due to the quote characters contained within 'value'
    # not being nested properly.
    #
    # However, we don't want to simply remove the outermost quote chars
    # in this case, because there are also cases where we'd want to show
    # the outermost quote chars, e.g.:
    #
    #     ``"key value"``
    #
    # For now, we just disable this test until we have time to fix this
    # more properly.
    return


# Generated at 2022-06-13 20:00:39.182037
# Unit test for function parse
def test_parse():
    test_text = \
        """
        """
    test_doc = parse(test_text)
    print(test_doc)

# Generated at 2022-06-13 20:00:47.859953
# Unit test for function parse
def test_parse():
    example = '''
    Do stuff.

    :param x: The stuff.
    :param y: The stuff you want.  Defaults to 'stuff'.
    :returns: Some stuff.
    :raises ValueError: If there's no stuff.
    :returns: int -- The number of stuff.
    :raises ValueError: If there's no stuff.
    '''


# Generated at 2022-06-13 20:00:58.758106
# Unit test for function parse
def test_parse():
    text_1 = """
    A text string.
    :param x: Some arg.
    :type x: int
    :raises ValueError: If something goes wrong.
    """


# Generated at 2022-06-13 20:01:08.409437
# Unit test for function parse
def test_parse():
    from .common import Docstring, DocstringMeta, DocstringParam, DocstringRaises, DocstringReturns
    from .common import ParseError

    assert parse("") == Docstring()
    assert parse("function") == Docstring(
        short_description="function",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description=None
    )

    # Short description with long description
    assert parse("function\n\nLong description.") == Docstring(
        short_description="function",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description="Long description."
    )

    # Short description with empty long description

# Generated at 2022-06-13 20:01:39.852148
# Unit test for function parse
def test_parse():
    text = """
    This is a very short description.

    This is a 
    very long description.

    : param1: str
    : param2: str

    : return: str
    """
    import inspect
    import re

    docstring = parse(text)

    text = inspect.cleandoc(text)
    #print(text)

    match = re.search("^:", text, flags=re.M)
    if match:
        desc_chunk = text[: match.start()]
        meta_chunk = text[match.start() :]
    else:
        desc_chunk = text
        meta_chunk = ""
    #print("meta_chunk", meta_chunk)

    parts = desc_chunk.split("\n", 1)
    #print("parts", parts)


# Generated at 2022-06-13 20:01:50.240018
# Unit test for function parse
def test_parse():
    import pytest
    docstring = "Test function\n:param str content: Content to be added.\n:return: The result\n"
    r = parse(docstring)
    assert r.short_description == 'Test function'
    assert r.blank_after_short_description == True
    assert r.long_description == None
    assert r.blank_after_long_description == False
    assert r.meta[0].args[0] == 'param'
    assert r.meta[0].args[1] == 'str'
    assert r.meta[0].args[2] == 'content'
    assert r.meta[0].description == 'Content to be added.'
    assert r.meta[0].type_name == 'str'
    assert r.meta[0].arg_name == 'content'