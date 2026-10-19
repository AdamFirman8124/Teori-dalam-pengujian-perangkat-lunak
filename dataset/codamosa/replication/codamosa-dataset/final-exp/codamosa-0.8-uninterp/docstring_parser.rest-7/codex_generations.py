

# Generated at 2022-06-13 19:52:27.622858
# Unit test for function parse
def test_parse():
    text = """This is docstring
    :param x: some x
    :param y: some y
    :param isOdd: whether the result is odd
    :returns: 10 or None
    """

    print(parse(text))

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:52:43.032205
# Unit test for function parse
def test_parse():
    doc = inspect.cleandoc(
        """
            Short description.

            Long description.

            :param T param: Parameter description.
            :param T param2: Parameter 2 description.
            :type param2: T
            :param param3: Parameter 3 description.
            :return: Returns description.
            :rtype: T
            :raises ValueError: If some value is invalid.
            :raises: If some other exception is raised.
        """
    )
    result = parse(doc)

# Generated at 2022-06-13 19:52:54.107542
# Unit test for function parse
def test_parse():
    docstring_text = """
    First line.

    Second line.

        >>> print("test")
        test
    
    : param arg1: first arg
    :type arg1: arg1 type
    :param arg2: second arg
    :param arg3: third arg
    :type arg3: arg3 type
    :return: return value
    :rtype: return type
    :raises: ValueError
    """
    docstring = parse(docstring_text)
    assert docstring.short_description == "First line."
    assert docstring.blank_after_short_description == True
    assert docstring.long_description == "Second line.\n\n>>> print(\"test\")\ntest"
    assert docstring.blank_after_long_description == True
    assert len(docstring.meta) == 4

# Generated at 2022-06-13 19:53:06.311341
# Unit test for function parse
def test_parse():
    class C1:
        """
        Short description.

        Long description.

        :param arg1: Argument 1.
        :raises ValueError: If something bad happens.
        """

    def func1():
        """
        Short description.

        Long description.

        :param arg1: Argument 1.
        :raises ValueError: If something bad happens.
        """

    def func2():
        """
        Short description.

        :param arg1: Argument 1.
        :raises ValueError: If something bad happens.
        :param arg2: Argument 2.
        :param arg3: Argument 3.
        :type arg2: list
        :type arg3: int, optional
        :returns: Description of return value.
        :rtype: int
        """


# Generated at 2022-06-13 19:53:17.331109
# Unit test for function parse
def test_parse():
    docstring = '"""This is a docstring."""'
    assert parse(docstring) == Docstring(
        short_description = 'This is a docstring.')

    docstring = """\
        This is a docstring.

        Parameters
        ----------
        arg1 : str
        arg2 : int, optional

        """

# Generated at 2022-06-13 19:53:31.423356
# Unit test for function parse
def test_parse():
    doc = parse("""Python function.

:param x: This is x.
:param str name: This is name.
:raises TypeError: When there is a type error.
:return: This is a return.
:returns: This is also a return.
:yield int: This is a yield.
:yields int: This is also a yield.
:returns int name: This is a return with a name and a type.
:yields: This is a yield type.
:other: This is other.
:return: This return has a
  multi-line
  description.
:returns: This return also has a
  multi-line
  description.
""")
    assert doc.short_description == "Python function."
    assert doc.blank_after_short_description is True
    assert doc.long_description

# Generated at 2022-06-13 19:53:43.206956
# Unit test for function parse
def test_parse():
    """Test function parse
    """
    docstring_text = """short description
    long description

    :param int a: first parameter
    """
    docstring = parse(docstring_text)
    assert docstring.short_description == "short description"
    assert docstring.long_description == "long description"
    assert len(docstring.meta) == 1

    docstring_text = """short description

    long description
    :param int a: first parameter
    """
    docstring = parse(docstring_text)
    assert docstring.short_description == "short description"
    assert docstring.long_description == "long description"
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description
    assert len(docstring.meta) == 1


# Generated at 2022-06-13 19:53:52.561179
# Unit test for function parse
def test_parse():

    text = """
    This is the docstring. It has one paragraph.

    One more paragraph.
    """
    print(parse(text))

    text = """
    This is the docstring. It has one paragraph.


    One more paragraph.
    """
    print(parse(text))

    text = """
    This is the docstring. It has one paragraph.


    One more paragraph.

    """
    print(parse(text))


# Generated at 2022-06-13 19:54:05.179958
# Unit test for function parse
def test_parse():
    text = """
    This is the short description.

    This is the long description.

    Here is the first meta information:
        :param arg1 - first param: description of arg1
        :type arg1: int
        :param arg2 - second param: description of arg2
        :type arg2: str
        :param arg3 - the third param:
    Here is the second meta information:
        :param arg4 - forth param: description of arg4
        :type arg4: str
        :param arg5 - fifth param: description

    :returns: something.
    """
    docstring = parse(text)
    assert docstring.short_description == "This is the short description."
    assert docstring.blank_after_short_description == True
    assert docstring.long_description == "This is the long description."
    assert doc

# Generated at 2022-06-13 19:54:11.200764
# Unit test for function parse
def test_parse():
    docstring = """summary line

extended description

:param str name: this is the name
:param int age: this is the age
:returns: None"""
    tree = parse(docstring)
    assert tree.short_description == "summary line"
    assert tree.blank_after_short_description
    assert tree.long_description == "extended description"
    assert tree.blank_after_long_description
    assert "name" in tree.params
    assert "age" in tree.params
    assert "returns" in tree.returns

# Generated at 2022-06-13 19:54:25.587289
# Unit test for function parse
def test_parse():
    """Testing function parse()."""
    doc = """Single line short description.

    No blank after short description.

    Single line long description.  No blank after long description."""

    expected = Docstring(
        short_description="Single line short description.",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description="Single line long description.",
        meta=[],
    )
    assert parse(doc) == expected

    doc = """Single line short description.

    Blank after short description.

    Single line long description.   Blank after long description.

    """


# Generated at 2022-06-13 19:54:37.753897
# Unit test for function parse
def test_parse():
    """Unit test for function parse."""
    def no_description():
        """
        :param param1:
        :returns:
        """
        pass

    def no_param():
        """
        Return ``True``.

        :returns:
        """
        pass

    def no_return():
        """
        Return ``True``.

        :param param1:
        """
        pass

    def complete():
        """
        Return ``True``.

        :param param1: int.
        :returns: bool.
        """
        pass

    def no_short_description():
        """
        :param param1: int.
        :returns: bool.
        """
        pass


# Generated at 2022-06-13 19:54:51.065584
# Unit test for function parse
def test_parse():
    input_string = """
    Test
    Test.
    :param str A: A B
    :param str B: ignore.
    :type str B: A
    :type str A: ignore.
    :param str C: ignore. C
    :returns: Test
    :param str D: Test
    :returns: Test
    :raises KeyError: Test
    """

# Generated at 2022-06-13 19:55:02.664373
# Unit test for function parse

# Generated at 2022-06-13 19:55:10.642007
# Unit test for function parse
def test_parse():
    "Run tests for function parse"
    import json


# Generated at 2022-06-13 19:55:20.009241
# Unit test for function parse
def test_parse():
    text = inspect.cleandoc("""
        This function does something.
    
        :param arg1: the first argument
        :param arg2: the second argument, defaults to 2
        :param arg3:
            the third argument (with long description)
        :raises Exception: when things go wrong
        :returns: None
        """)
    
    docstring = parse(text)
    assert docstring.short_description == "This function does something"
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == True
    assert docstring.long_description == None
    assert len(docstring.meta) == 4
    
    param_arg1, param_arg2, param_arg3 = docstring.meta[0:3]

# Generated at 2022-06-13 19:55:32.440505
# Unit test for function parse
def test_parse():
    doc = """Short description
    Long description

    :param x: The x parameter.
    :type x: int
    :param y: The y parameter
    :type y: int
    :returns: The return value.
    :rtype: int
    :raises ImportError: The exception type.
    """
    d = parse(doc)
    assert d.short_description == "Short description"
    assert d.long_description == "Long description"
    assert d.blank_after_short_description
    assert d.blank_after_long_description
    assert d.meta[0].args == ["param", "x", "The x parameter."]
    assert d.meta[0].type_name == "int"
    assert d.meta[0].arg_name == "x"
    assert d.meta[0].is_

# Generated at 2022-06-13 19:55:41.390594
# Unit test for function parse
def test_parse():
    # TODO: cover all main branches
    assert parse(None) == Docstring()

    doc = """
    The quick brown fox jumps over the lazy dog.

    :param a: squirrels
    :type a: str
    :param b: year
    :type b: int
    :param c: optional age
    :type c: int?

    :returns: a string
    :returns: a string?
    :returns: a string?
    :returns: a string?

    :rtype: int
    :rtype: int?
    :rtype: int?

    :parameter a: some description
    :parameter b: some description
    :type b: int
    """

    docstring = parse(doc)
    assert docstring.short_description == "The quick brown fox jumps over the lazy dog."


# Generated at 2022-06-13 19:55:53.800529
# Unit test for function parse
def test_parse():
    """Unit test for function `parse`."""
    doc = parse("""
       Short description.

       Longer description.

       :param a: Type of a.
       :param b: Type of b.

       :returns: Description of the return value.
       :rtype: int

       :raises TypeError: Description of the exception.
       :raises ValueError: Description of the exception.

       :type c: str
    """)
    assert doc.short_description == "Short description."
    assert doc.blank_after_short_description is True
    assert doc.blank_after_long_description is False
    assert len(doc.meta) == 11
    # pylint: disable=no-member
    assert doc.meta[0].description == "Longer description."

# Generated at 2022-06-13 19:56:03.071434
# Unit test for function parse
def test_parse():
    import sys
    text = parse(sys.modules[__name__].__doc__).__dict__
    expected = {
        'long_description':
        "ReST-style docstring parsing.\n\nArguments:\n    text: docstring\n\nReturns:\n    parsed docstring",
        'blank_after_long_description':
        True,
        'blank_after_short_description':
        True,
        'short_description':
        'ReST-style docstring parsing.',
        'meta': [
            {
                'description':
                "docstring\n\nReturns:\n    parsed docstring",
                'args': [
                    'text',
                ],
            },
        ],
    }
    assert text == expected

# Generated at 2022-06-13 19:56:18.505514
# Unit test for function parse
def test_parse():
    docstring = '''
    Short Description

    Long Description

    :param arg1: this is the first argument
    :type arg1: str
    :param arg2: this is a second argument
    :type arg2: int, optional
    :returns: description of return value
    :rtype: int
    :raises keyError: description
    '''
    dstring = parse(docstring)
    assert dstring.short_description == 'Short Description'
    assert dstring.long_description == 'Long Description'
    assert len(dstring.meta) == 4
    assert (dstring.meta[0].args == [ 'param', 'arg1' ])
    assert (dstring.meta[1].args == [ 'type', 'arg1', 'str' ])

# Generated at 2022-06-13 19:56:20.180550
# Unit test for function parse
def test_parse():
    """Test the function parse."""
    # TODO: Add unit test.
    pass



# Generated at 2022-06-13 19:56:25.641768
# Unit test for function parse
def test_parse():
    docstring = '''
        First line.
        This is a first paragraph.

        This is a second paragraph.
        : p: str - parameter name
            This is a description of parameter name.

        : r: str - return type
            This is a description of return type.
        '''
    print("test parse\n")
    print("input:\n")
    print(docstring, "\n")
    print("output:\n")
    print(parse(docstring))


# test_parse()

# Generated at 2022-06-13 19:56:30.583837
# Unit test for function parse
def test_parse():
    docstring = """
    Function that adds two numbers.

    Args:
        a: First number to be added.
        b: Second number to be added.

    Returns:
        The sum of the two numbers.
    """

    assert parse(docstring) is not None

# Generated at 2022-06-13 19:56:42.957133
# Unit test for function parse
def test_parse():
    """Tests all the possible cases at the moment"""
    def assert_parsed(
        text: str,
        short_description: T.Optional[str] = None,
        long_description: T.Optional[str] = None,
        meta: T.Tuple[DocstringMeta] = (),
        ignore: T.Optional[T.List[str]] = None,
        blank_after_short_description: bool = False,
        blank_after_long_description: bool = False,
    ):
        if not ignore:
            ignore = []
        parsed = parse(text)
        assert parsed.short_description == short_description
        assert parsed.long_description == long_description
        assert parsed.meta == meta
        assert parsed.blank_after_short_description == blank_after_short_description
        assert parsed.blank_after

# Generated at 2022-06-13 19:56:51.375631
# Unit test for function parse
def test_parse():
    docstring = '''Purpose:
        This is just a test function.

Args:
        x: first argument.
        y: second argument.
        z: third argument.
    '''
    ret = parse(docstring)
    assert(len(ret.meta) == 3)
    assert(ret.short_description == "Purpose:")
    assert(ret.blank_after_short_description)
    assert(ret.long_description == "This is just a test function.")
    
    docstring = '''Purpose:
This is just a test function.

Args:
    x: first argument.
    y: second argument.
    z: third argument.
'''
    ret = parse(docstring)
    assert(len(ret.meta) == 3)

# Generated at 2022-06-13 19:57:00.776081
# Unit test for function parse
def test_parse():
    expect = 'Expected one or two arguments for a param keyword.'
    docstring = ':para: a text.'
    with pytest.raises(ParseError):
        parse(docstring)
    docstring = ':param: a text.'
    with pytest.raises(ParseError):
        parse(docstring)
    docstring = ':param a: a text.'
    with pytest.raises(ParseError):
        parse(docstring)
    docstring = ':param a b: a text.'
    assert parse(docstring)



# Generated at 2022-06-13 19:57:13.306020
# Unit test for function parse
def test_parse():
    import os
    import sys
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(dir_path)
    from omxware.docstring.common import DocstringMeta
    from omxware.docstring.common import DocstringParam
    from omxware.docstring.common import DocstringRaises
    from omxware.docstring.common import DocstringReturns
    from omxware.docstring.common import Docstring
    from omxware.docstring import parser


# Generated at 2022-06-13 19:57:26.029847
# Unit test for function parse
def test_parse():
    test_docstring = """
    Short description.

    Description of function func.
    :param arg: Description of arg.
    :type arg: int
    :returns: Description of return value.
    :raises ValueError: If `arg` < 0.
    """
    doc = parse(test_docstring)
    assert doc.short_description == "Short description."
    assert doc.long_description == """
    Description of function func.
    """.strip()
    assert [x.args for x in doc.meta] == [
        ["param", "arg", "int"],
        ["returns", "int"],
        ["raises", "ValueError"],
    ]
    assert doc.meta[0].description == "Description of arg."
    assert doc.meta[0].type_name == "int"
    assert doc.meta

# Generated at 2022-06-13 19:57:34.281903
# Unit test for function parse
def test_parse():
    doc = '''
    This is the short description.

    This is the long description.

    :type key1: str
    :type key2: str | None
    :param key1: the first parameter
    :param key2: the second parameter or None
    :raises ValueError: if the value is not valid

    This is the end.
    '''
    parsed = parse(doc)
    assert parsed.short_description == doc.split('\n')[1]
    assert parsed.blank_after_short_description == True
    assert parsed.long_description == doc.split('\n')[3]
    assert parsed.blank_after_long_description == True

    assert parsed.meta[0].args == ['type', 'key1', 'str']
    assert parsed.meta[0].description == ''

    assert parsed.meta

# Generated at 2022-06-13 19:57:43.700639
# Unit test for function parse
def test_parse():
    """Test the docstring parser of module `rest."""
    import doctest

    if doctest.testmod().failed:
        raise ImportWarning("The docstring tests failed.")

# Generated at 2022-06-13 19:57:54.129379
# Unit test for function parse
def test_parse():
    # Test with few malformed docstrings
    malformed_docstrings = [
        """
    This docstring is missing both a short and long description.
    """,
        """
    But the malformation of this docstring is not so obvious
    since it has both a short and long description.
    """,
        """
    The malformation of this docstring is obvious
    since it has only long description
    """,
        """
    The malformation of this docstring is obvious
    since it has only short description.
    """,
    ]
    for malformed_docstring in malformed_docstrings:
        try:
            parse(malformed_docstring)
        except ParseError:
            pass
        else:
            raise Exception("Error not raised for malformed docstring")

    # Test with well-formed docstrings
    well_

# Generated at 2022-06-13 19:58:05.973000
# Unit test for function parse

# Generated at 2022-06-13 19:58:17.623546
# Unit test for function parse
def test_parse():
    text = """
    Compute the mean of a sequence of numbers.

    :param numbers: The numbers to process.
    :type numbers: iterable of numbers
    :returns: The mean of the numbers.
    :raises ValueError: If `numbers` is empty.
    :raises TypeError: If any element of `numbers` cannot be cast to a float.

    Examples:
      >>> mean([1, 2, 3])
      2.0
    """
    docstring = parse(text)
    print(docstring)
    # print(docstring.short_description)
    # print(docstring.long_description)
    # print(docstring.blank_after_short_description)
    # print(docstring.blank_after_long_description)
    # print(docstring.meta)

# Generated at 2022-06-13 19:58:27.743224
# Unit test for function parse
def test_parse():
    docstring = """Example function.

    This function has types.

    :param a: param a
    :type a: int
    :param b: param b
    :type b: string
    :param c: param c
    :type c: int
    :param d: param d with a defualt
    :type d: int
    :default d: 10
    :param e: param e with an empty default.
    :type e: int
    :default e:
    :param f: param f defaults to something.
    :type f: int
    :default f: 0
    """

# Generated at 2022-06-13 19:58:40.404765
# Unit test for function parse
def test_parse():
    # Test1: Test for no docstring
    assert parse("") == Docstring()

    # Test2: Test for docstring with only short description
    assert parse("short description") == Docstring(
        short_description="short description",
        blank_after_short_description=False,
        blank_after_long_description=False,
    )

    # Test3: Test for docstring with only one line long description
    assert parse("short description\nlong description") == Docstring(
        short_description="short description",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description="long description",
    )

    # Test4: Test for docstring with trailing whitespace

# Generated at 2022-06-13 19:58:56.970496
# Unit test for function parse
def test_parse():
    docstring = """First line of the short description.

The first line is a short description of the object, which may span multiple
lines. Following lines until the next paragraph break are considered part of
the short description. The short description may optionally be followed by a
blank line, followed by a long description until the next paragraph break.
Long description should be wrapped to 72 characters.

    A line of text that is indented with four spaces at the beginning
    is considered as part of the long description.

The long description may include multiple paragraphs.

:Returns:
    Any arbitrary text

:Keyword Arguments:
    * **some_param** (``str``):
        description
    * **some_other_param** (``bool``):
        description

:Raises:
    * ``ValueError``: description
    * ``SomeOtherError``: description
"""


# Generated at 2022-06-13 19:59:07.415490
# Unit test for function parse
def test_parse():
    doc = """\
    Single line summary.

    This is a long description.
    There are multiple lines.

    :param arg1: Description for arg1.
    :param arg2: Description for arg2.
    :type arg2: int

    :yields: Yields result 1.
    :yields: Yields result 2.
    """
    result = parse(doc)
    assert result.short_description == "Single line summary."
    assert result.long_description == (
        "This is a long description.\n"
        "There are multiple lines."
    )
    assert result.meta[0].args == ["param", "arg1"]
    assert result.meta[0].description == "Description for arg1."
    assert result.meta[1].args == ["param", "arg2", "int"]


# Generated at 2022-06-13 19:59:08.525218
# Unit test for function parse
def test_parse():
    import inspect
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-13 19:59:13.089391
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    # pylint: disable=invalid-name

    # Validate input argument type
    with raises(TypeError):
        parse('')


# Generated at 2022-06-13 19:59:33.612849
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()
    assert (
        parse("This is a description")
        == Docstring(
            short_description="This is a description",
            long_description=None,
            blank_after_short_description=False,
            blank_after_long_description=False,
        )
    )
    assert (
        parse("This is a description.\n\nWith more details.\n")
        == Docstring(
            short_description="This is a description.",
            long_description="With more details.",
            blank_after_short_description=True,
            blank_after_long_description=False,
        )
    )

# Generated at 2022-06-13 19:59:43.357809
# Unit test for function parse
def test_parse():
    text = '''Summary line.

    Extended description.

    :param file: file path
    :type file: str
    :param mode: 'r' for reading and 'w' for writing
    :type mode: str
    :return: File object
    :rtype: file
    :raises IOError: if the file cannot be read
    '''

    docstring = parse(text)

    assert docstring.short_description == "Summary line."
    assert docstring.long_description == "Extended description."

    assert len(docstring.meta) == 4

    meta = docstring.meta[0]
    assert meta.args == ["param", "file", "file"]
    assert meta.description == "file path"
    assert meta.arg_name == "file"
    assert meta.type_name == "str"

    meta

# Generated at 2022-06-13 19:59:55.361578
# Unit test for function parse
def test_parse():
    docstring = parse("""
    Test function.

    :param arg1: The first argument.
    :type arg1: str
    :param arg2: The second argument.
    :type arg2: int, optional
    :param arg3: The third argument.
    :param arg4: The fourth argument.
    :raises ValueError: If `bar` is less than `foo`.
    :returns: Description of return value.
    :rtype: int
    """)
    assert docstring.short_description == "Test function."
    assert docstring.long_description == "Test function."

# Generated at 2022-06-13 20:00:06.938695
# Unit test for function parse
def test_parse():
    """Test function parse."""
    ds = """
        this is a docstring.

        very long description
        ends with a blank line.

        :param arg1: description of parameter arg1
        :param arg2: description of parameter arg2
        :type arg2: int
        :param arg3, arg4: description of arg3 and arg4
        :returns: None
        :rtype: None
        :raises: Exception
        :raises ValueError, TypeError: description of raises
        :yields: value
        :yields ValueError: description of yields ValueError
        """
    doc = parse(ds)
    print(doc.short_description)
    print(doc.long_description)
    print(doc.blank_after_short_description)
    print(doc.blank_after_long_description)

# Generated at 2022-06-13 20:00:10.017610
# Unit test for function parse
def test_parse():
    doc = parse.__doc__
    print(doc)
    print(repr(parse(doc)))
    print(parse(doc).meta)


# Generated at 2022-06-13 20:00:21.536721
# Unit test for function parse

# Generated at 2022-06-13 20:00:33.971247
# Unit test for function parse
def test_parse():
    import logging
    import sys
    import platform
    import json
    logger = logging.getLogger()
    logging.basicConfig(level=logging.DEBUG)

    docsting = inspect.cleandoc('''
    A simple example of calculation.

    :param a: The A factor
    :type a: int

    :param b: The B factor
    :type b: int

    :returns: The result
    :rtype: int
    ''')


# Generated at 2022-06-13 20:00:45.208028
# Unit test for function parse
def test_parse():
    docstring = inspect.cleandoc(
        """Example function with types documented in the docstring.

    "param" and "type" both work.

        :param a: The first parameter.
        :type a: int, optional
        :returns: The return value.
        :rtype: bool

    Also supports optional parameters, as in Sphinx.

        :param b: Optional parameter, defaults to True.
        :type b: bool, optional

    Parameters
    ----------
    a : int
        The first parameter.
    b : bool
        The second parameter.

    Returns
    -------
    bool
        The return value. True for success, False otherwise.
    """
    )
    parsed = parse(docstring)

    assert parsed.short_description == "Example function with types documented in the docstring."
    assert parsed.blank_after

# Generated at 2022-06-13 20:00:55.808256
# Unit test for function parse

# Generated at 2022-06-13 20:01:04.207386
# Unit test for function parse
def test_parse():
    def func():
        """Short desc

        Long desc.

        :param arg1: First arg
        :type arg1: str
        :param arg2: Second arg
        :type arg2: str
        :param arg3: Third arg defaults to 3.
        :type arg3: int
        :param arg4: Fourth arg (optional, defaults to 4)
        :type arg4: int
        :raises TypeError:
        :raises ValueError:
        :returns:
        :rtype: None
        """
        pass

    docstring = parse(func.__doc__)

    assert docstring.short_description == "Short desc"

    assert docstring.long_description == "Long desc."

    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is False

# Generated at 2022-06-13 20:01:16.903374
# Unit test for function parse
def test_parse():
    assert parse('Function to parse a string') == Docstring(
        short_description="Function to parse a string",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )

    assert parse("Function to parse a string\n") == Docstring(
        short_description="Function to parse a string",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )


# Generated at 2022-06-13 20:01:21.248735
# Unit test for function parse
def test_parse():
    x = parse("""
    A sentence for documentation.

    Longer documentation.

    :param key: the key
    :param value: the value

    :returns:
    """)

    print(x.short_description)
    print(x.long_description)
    print(x.meta)

# Generated at 2022-06-13 20:01:29.106613
# Unit test for function parse
def test_parse():
    docstring = '''One line summary.
    Other description lines.
    :keyword: argument description.
    :keyword arg: description that continues here.

    :param arg1: parameter description
                  that continues here
    :type arg1: int
    :param arg2: parameter description.
    :param arg3: parameter description, defaults to [1, 2, 3].
                  and continues here.
    :rtype: tuple
    :raises ValueError: description
    :returns: description
    :yields: description
    '''

# Generated at 2022-06-13 20:01:33.681075
# Unit test for function parse
def test_parse():
    assert parse('A docstring') == Docstring(
        short_description='A docstring',
        long_description=None,
        meta=[],
    )
    assert parse('A docstring\n\nwith a long description') == Docstring(
        short_description='A docstring',
        long_description='with a long description',
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[],
    )

# Generated at 2022-06-13 20:01:46.664912
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()

    assert parse("short description") == Docstring(
        short_description="short description",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )

    docstring = parse(
        "short description\n"
        "long description\n"
    )
    assert docstring == Docstring(
        short_description="short description",
        long_description="long description",
        blank_after_short_description=False,
        blank_after_long_description=True,
        meta=[],
    )

    docstring = parse(
        "short description\n\n"
        "long description\n"
    )