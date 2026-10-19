

# Generated at 2022-06-13 19:52:23.279323
# Unit test for function parse
def test_parse():
    """Unit tests for function parse."""
    assert parse("") == Docstring()
    assert (
        parse(""""A function that does nothing.

        :returns: None
        """)
        == Docstring(
            short_description="A function that does nothing.",
            long_description=None,
            blank_after_short_description=True,
            blank_after_long_description=False,
            meta=[
                DocstringReturns(
                    description="None",
                    args=["returns"],
                    type_name=None,
                    is_generator=False,
                )
            ],
        )
    )

# Generated at 2022-06-13 19:52:33.114981
# Unit test for function parse
def test_parse():
  text = '''
  Function parse() for ReST-style docstring.
  This is a long description.
  :param foo: Foo
  :type foo: int
  :param bar: Bar
  :type bar: str
  :returns: The parsed docstring
  :rtype: Docstring
  '''

  doc = parse(text)
  assert doc.short_description == 'Function parse() for ReST-style docstring.'
  assert doc.long_description == 'This is a long description.'
  assert doc.blank_after_short_description == False
  assert doc.blank_after_long_description == True
  assert doc.meta[0].arg_name == 'foo'
  assert doc.meta[0].type_name == 'int'
  assert doc.meta[1].arg_name == 'bar'
 

# Generated at 2022-06-13 19:52:38.270837
# Unit test for function parse
def test_parse():
    doc = """
    A short description.

    A long description.

    :param str table: A database table name.
    :returns: A database connection string.
    """
    doc = parse(doc)
    assert len(doc.meta) == 2
    assert doc.meta[0].args == ["param", "str", "table"]
    assert doc.meta[0].description == "A database table name."
    assert doc.meta[1].args == ["returns"]
    assert doc.meta[1].description == "A database connection string."

# Generated at 2022-06-13 19:52:51.080616
# Unit test for function parse
def test_parse():
    description1 = """
    This is the description of the function
    """

    description2 = """
    This is the description of the function
    that goes over multiple lines
    and has a second paragraph
    """

    description3 = """
    This is the description of the function
    that goes over multiple lines
    and has a second paragraph

    And a third paragraph
    """

    description4 = """
    This is the description of the function

    And a third paragraph
    """

    description5 = """
    This is the description of the function


    And a third paragraph
    """

    description6 = """
    This is the description of the function that goes over multiple lines
    and has a second paragraph

    And a third paragraph
    """


# Generated at 2022-06-13 19:52:59.013302
# Unit test for function parse

# Generated at 2022-06-13 19:53:10.141997
# Unit test for function parse

# Generated at 2022-06-13 19:53:19.796118
# Unit test for function parse
def test_parse():
    """Unit test for function parse."""
    print("Testing function parse.")
    doc = '''
A one-line summary that does not use variable names
or the function name.

A longer, indented description that is like a paragraph and
that may use variables and function names.
:param int a: An integer argument named a.
:param str b: A string argument named b.
:returns: the return description
:raises ValueError:
    if a or b is non-positive
:raises KeyError:
    if a or b is non-positive
:raises FileNotFoundError:
    if the file is not found
'''
    d = parse(doc)
    print("short description: {}".format(d.short_description))
    print("long description: {}".format(d.long_description))

# Generated at 2022-06-13 19:53:32.104401
# Unit test for function parse
def test_parse():
    docstring = parse("""
        for test

        :param x: a parameter
        :type x: int
        :param b?: another parameter
        :return: test
        :rtype: str
    """)

    # docstring.meta[0]
    # type: DocstringMeta
    # args: ['param', 'x']
    # description: a parameter
    assert docstring.meta[0].args == ["param", "x"]
    assert docstring.meta[0].description == "a parameter"

    # docstring.meta[1]
    # type: DocstringMeta
    # args: ['type', 'x', 'int']
    # description: None
    assert docstring.meta[1].args == ["type", "x", "int"]

    # docstring.meta[2]
    # type: DocstringParam


# Generated at 2022-06-13 19:53:46.291864
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""

    lines1 = """\
    This function does something.

    :param foo: The foo.
    :type foo: str, optional
    :param quux: The quux defaults to 3.
    :type quux: int, optional
    :param bar: The bar, optional
    :returns: The return value.
    :rtype: int
    """
    lines2 = """\
    This function does something.

    :param int foo: The foo.
    :param int quux: The quux defaults to 3.
    :param bar: The bar, optional
    :returns: The return value.
    :rtype: int
    """

# Generated at 2022-06-13 19:53:53.773297
# Unit test for function parse
def test_parse():
    text = """
    Summary line.

    Extended description.

    :param arg1: The first argument.
    :type arg1: str
    :param arg2: The second argument.
    :type arg2: int, optional
    :returns: description of return value
    :rtype: bool
    :raises keyError: raises an exception
    """
    docstring = parse(text)

# Generated at 2022-06-13 19:54:03.861697
# Unit test for function parse
def test_parse():
    docstring = """\
    """
    assert parse(docstring) is None

# Generated at 2022-06-13 19:54:12.537195
# Unit test for function parse
def test_parse():
    text = """
        Short description.

        Long description.

        :param foo:
            This is the first line of a paragraph.

            This is the second line of it.

            Multiline :class:`arg <Argument>` paragraph is possible.
        :type foo: int
        :param bar: defaults to 42. (Optional)
        :type bar: bool
        :returns: nada
        :raises TypeError: if bad things happen.
    """
    doc = parse(text)

    assert doc.short_description == "Short description."
    assert doc.long_description == "Long description."
    assert doc.blank_after_short_description
    assert doc.blank_after_long_description
    assert len(doc.meta) == 4

# Generated at 2022-06-13 19:54:21.736206
# Unit test for function parse
def test_parse():

    # Correct input
    assert parse(None) == Docstring()
    assert parse("") == Docstring()
    assert parse("a") == Docstring(
        short_description="a",
        blank_after_short_description=True,
        long_description=None,
        blank_after_long_description=False,
        meta=[],
    )
    assert parse("a\n\n") == Docstring(
        short_description="a",
        blank_after_short_description=True,
        long_description=None,
        blank_after_long_description=False,
        meta=[],
    )

# Generated at 2022-06-13 19:54:26.079295
# Unit test for function parse
def test_parse():
    text = """
    Single line summary.
    Single line extended summary.
    
    :param arg1: The first argument.
    :type arg1: str
    :param arg2: The second argument.
    :type arg2: int, optional
    :returns: Description of return value
    :rtype: int
    
    """
    doc = parse(text)
    assert doc.meta[2].description == "Description of return value"


# Generated at 2022-06-13 19:54:30.677759
# Unit test for function parse
def test_parse():
    def f(x):
        """test
        :param x: parameter x
        :param y: parameter y
        :return: value returned
        :rtype: int
        """
        pass
    print(parse(inspect.getdoc(f)))

# Generated at 2022-06-13 19:54:40.362200
# Unit test for function parse

# Generated at 2022-06-13 19:54:52.799359
# Unit test for function parse
def test_parse():
    text = """
    Short description.

    Longer description.

    :returns: something
    :rtype: int
    :raises ValueError: if something went wrong
    """

    result = parse(text)
    assert result.short_description == "Short description."
    assert result.long_description == "Longer description."
    assert result.blank_after_short_description
    assert not result.blank_after_long_description
    assert result.meta[0].key == "returns"
    assert result.meta[0].arg_name is None
    assert result.meta[0].type_name == "something"
    assert not result.meta[0].is_generator
    assert result.meta[1].key == "rtype"
    assert result.meta[1].arg_name is None

# Generated at 2022-06-13 19:55:03.879219
# Unit test for function parse
def test_parse():

    # Test against a module docstring
    from . import docstring_parser

    docstr = parse(docstring_parser.__doc__)
    assert docstr.short_description == "Parse docstring into its components."
    assert docstr.blank_after_short_description == False
    assert docstr.long_description == """
    This module contains a single function, :func:`parse`, which accepts
    a docstring and returns its parsed version as a :class:`docstring_parser.Docstring`
    object.
    """
    assert docstr.blank_after_long_description == True

    # Test against a method docstring
    for meta in docstr.meta:
        if meta.args[0] == "raise":
            assert isinstance(meta, DocstringRaises)

# Generated at 2022-06-13 19:55:11.350228
# Unit test for function parse
def test_parse():
    docstring = parse(
        """
    Short description

    Long description

    :param arg1: first function argument
    :type arg1: str
    :param arg2: second function argument
    :type arg2: float
    :returns: type1 -- first return argument
    :returns: type2 -- second return argument
    """
    )

    assert docstring.short_description == "Short description"
    assert docstring.long_description == "Long description"
    assert docstring.meta[0] == DocstringParam(
        args=["param", "arg1", "arg2"], description=""
    )

# Generated at 2022-06-13 19:55:20.292420
# Unit test for function parse
def test_parse():
    """
    Test function parse.
    """
    test = Docstring()
    test.short_description = 'Do something with words'
    test.long_description = 'Do something with words and more words\npossibly multiple lines'
    example_line = '    >>> my_words = Words()'
    example_line2 = '    >>> my_words.add_words()'
    test.long_description = (
        f'{test.long_description}\n\nExample:\n{example_line}\n{example_line2}'
    )
    expected = test


# Generated at 2022-06-13 19:55:34.530849
# Unit test for function parse
def test_parse():
    print('Testing function parse')
    docstring = '''
        :param arg1: test arg
        :param type arg2: test arg2
        :returns: some value
        :raises Exception: some exception
    '''
    print(parse(docstring))

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:55:42.556862
# Unit test for function parse
def test_parse():
    """Verify parse()"""
    def test_parse_helper(text, expect):
        assert parse(text) == expect

    # Short description
    test_parse_helper(
        text="""\
        This is the short description.

        This is the long description.
        """,
        expect=Docstring(
            short_description="This is the short description.",
            blank_after_short_description=False,
            blank_after_long_description=False,
            long_description="This is the long description.",
            meta=[],
        ),
    )

    # Long description can be None

# Generated at 2022-06-13 19:55:44.593418
# Unit test for function parse
def test_parse():
    parse('parse(text: str) -> Docstring')

# Generated at 2022-06-13 19:55:55.754170
# Unit test for function parse
def test_parse():
    # Functional tests
    txt = """
    Short
    Long
    :param: x
    """
    docstring = parse(txt)
    assert docstring.meta == [
        DocstringMeta(args=["param"], description="x")
    ]

    txt = """
    Short
    Long
    :param x:
    """
    docstring = parse(txt)
    assert docstring.meta == [
        DocstringMeta(args=["param", "x"], description="")
    ]

    txt = """
    Short
    Long
    :param x: y
    """
    docstring = parse(txt)
    assert docstring.meta == [
        DocstringMeta(args=["param", "x"], description="y")
    ]


# Generated at 2022-06-13 19:56:03.981377
# Unit test for function parse

# Generated at 2022-06-13 19:56:13.509092
# Unit test for function parse
def test_parse():

    docstring = """
        Short description.

        Long description.

        
        :params foo:
            This is foo.
        """

    docstring = parse(docstring)

    expected = Docstring()
    expected.short_description = "Short description."
    expected.long_description = "Long description."
    expected.blank_after_short_description = True
    expected.blank_after_long_description = True

    expected.meta.append(
        DocstringParam(
            arg_name="foo",
            description="This is foo.",
            type_name=None,
            is_optional=None,
            default=None,
        )
    )

    assert docstring == expected



# Generated at 2022-06-13 19:56:22.529332
# Unit test for function parse
def test_parse():
    docstring = parse("""\
        :param int x:
            description of x.

        :param str y:
            description of y.
        """)
    assert docstring.meta[0].key == "param"
    assert docstring.meta[0].arg_name == "x"
    assert docstring.meta[0].description == "description of x."
    assert docstring.meta[0].type_name == "int"

    assert docstring.meta[1].key == "param"
    assert docstring.meta[1].arg_name == "y"
    assert docstring.meta[1].description == "description of y."
    assert docstring.meta[1].type_name == "str"

# Generated at 2022-06-13 19:56:24.508420
# Unit test for function parse
def test_parse():
    text = inspect.cleandoc(
        """
    """
    )



# Generated at 2022-06-13 19:56:34.383524
# Unit test for function parse

# Generated at 2022-06-13 19:56:46.661700
# Unit test for function parse
def test_parse():
    assert parse("test") == Docstring(
        short_description="test",
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )
    assert parse(":param x:") == Docstring(
        short_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[
            DocstringParam(
                args=["param", "x", "x"],
                description=None,
                arg_name="x",
                type_name=None,
                is_optional=None,
                default=None,
            )
        ],
    )

# Generated at 2022-06-13 19:57:02.266825
# Unit test for function parse
def test_parse():
    simple_docstring = """
    Return the sum of a and b.

    :param int a: first number
    :param int b: second number
    :return: a + b
    :rtype int:
    """
    parsed = parse(simple_docstring)
    assert parsed.short_description == "Return the sum of a and b."
    assert len(parsed.meta) == 2



# Generated at 2022-06-13 19:57:13.923191
# Unit test for function parse
def test_parse():
    text = """\
    Return the absolute value of the input argument.

    :type val: float or int
    :param val: The value whose absolute value is to be returned.
    :rtype: float or int
    :return: absolute value of val

    """

# Generated at 2022-06-13 19:57:26.794484
# Unit test for function parse

# Generated at 2022-06-13 19:57:37.001365
# Unit test for function parse
def test_parse():
    text = """
    Example class.

    :keyword arg_name: Argument description.
    :type arg_name: str
    :param type_name? arg_name: Parameter description with type.
    :type_name? arg_name: Parameter description without type.
    :param type_name? arg_name: Parameter description with type and default. Defaults to None.
    :keyword arg_name: Parameter description with type and optional.
    :type arg_name: str
    :return: Return description.
    :rtype: int

    More details.
    """

# Generated at 2022-06-13 19:57:50.418437
# Unit test for function parse
def test_parse():
    doc_string = """
    Args:
        arg1 (bool): The first parameter.
        no_type: The second parameter.
    """
    res = parse(doc_string)
    assert(res.short_description is None)
    assert(res.long_description is None)
    assert(res.blank_after_short_description is False)
    assert(res.blank_after_long_description is False)
    assert(len(res.meta) == 2)

    doc_string = """
    Args:
        arg1 (bool): The first parameter.
        no_type: The second parameter.

    Other stuff
    """

    res = parse(doc_string)
    assert(res.short_description is None)
    assert(res.long_description == "Other stuff")

# Generated at 2022-06-13 19:58:02.840278
# Unit test for function parse
def test_parse():
    docstring = """
       this is the first line
       this is the second line

       :raises: ValueError
       :param name: parameter description
       :type name: str
       :returns: returns description
       :rtype: str

       this is the third line
       this is the fourth line

       :param name2: parameter description
       :type name2: str
       :raises ValueError: this is the raised exception description

       this is the fifth line

    """

    doc_parsed = parse(docstring)
    assert doc_parsed.short_description == "this is the first line"
    assert doc_parsed.long_description == (
        "this is the second line\n\nthis is the third line\nthis is the "
        "fourth line"
    )

# Generated at 2022-06-13 19:58:14.241686
# Unit test for function parse
def test_parse():
    """Unit test for the parse function."""
    assert parse("") == Docstring()

    expected = Docstring(
        short_description="This is a function.",
        long_description="This function does something.\n\nWith a paragraph.",
        meta=[
            DocstringParam(
                args=["param", "str", "var"],
                description="This is a variable.",
                arg_name="var",
                type_name="str",
                is_optional=False,
                default="None",
            ),
            DocstringReturns(
                args=["returns", "str"], description="A string.", type_name="str", is_generator=False
            ),
        ],
    )


# Generated at 2022-06-13 19:58:24.808888
# Unit test for function parse
def test_parse():
    data = Docstring.parse("""Single line doc.
    :arg int a: int parameter
    :yields int: (int)
    :returns: int
    """)
    assert isinstance(data, Docstring)
    assert data.short_description == "Single line doc."
    assert data.long_description is None
    assert len(data.meta) == 3
    assert data.meta[0].keyword == "arg"
    assert data.meta[0].type_name == "int"
    assert data.meta[0].arg_name == "a"
    assert data.meta[1].keyword == "yields"
    assert data.meta[1].type_name == "int"
    assert data.meta[1].arg_name is None

# Generated at 2022-06-13 19:58:39.110312
# Unit test for function parse

# Generated at 2022-06-13 19:58:56.205082
# Unit test for function parse
def test_parse():
    """

    :return:
    """

# Generated at 2022-06-13 19:59:17.251134
# Unit test for function parse
def test_parse():
    s = '''
    Short description.

    Long description.

    :param test_param: description

    :returns: description
    '''
    d = parse(s)
    print(d)
    assert d.short_description == 'Short description.'
    assert d.blank_after_short_description
    assert d.long_description == 'Long description.'
    assert d.blank_after_long_description
    assert d.meta[0] == DocstringParam(['param', 'test_param'], 'description', 'test_param')
    assert d.meta[1] == DocstringReturns(['returns'], 'description', None)

if __name__ == "__main__":
    # execute only if run as a script
    test_parse()

# Generated at 2022-06-13 19:59:28.834795
# Unit test for function parse
def test_parse():
    docstring = """
    This is the short description.

    This is the long description.
    Blah blah blah.
    """
    ret = parse(docstring)
    assert not ret.meta
    assert ret.short_description == "This is the short description."
    assert ret.long_description == "This is the long description.\nBlah blah blah."
    assert ret.blank_after_short_description
    assert ret.blank_after_long_description

    docstring = """
    This is the short description.

    This is the long description.
    Blah blah blah.
    :param int x:
    """
    ret = parse(docstring)
    assert len(ret.meta) == 1
    param_meta = ret.meta[0]
    assert isinstance(param_meta, DocstringParam)
    assert param

# Generated at 2022-06-13 19:59:35.411089
# Unit test for function parse

# Generated at 2022-06-13 19:59:43.889667
# Unit test for function parse
def test_parse():
    func_name = __name__ + ".parse"
    text = inspect.getdoc(parse)

# Generated at 2022-06-13 19:59:55.811453
# Unit test for function parse
def test_parse():
    from inspect import cleandoc
    from pprint import pprint


# Generated at 2022-06-13 20:00:07.213586
# Unit test for function parse
def test_parse():
    """Test doc string parsing.

    :returns: None
    """
    docstring = """\
        This is a docstring.
        It is multi-line.

        :param x: parameter x
        :type x: float
        :param y: parameter y
        :type y: int
        :returns: float
        """
    ret = parse(docstring)
    assert ret.short_description == "This is a docstring."
    assert ret.blank_after_short_description is True
    assert ret.long_description == "It is multi-line."
    assert ret.blank_after_long_description is True
    assert len(ret.meta) == 3

    assert type(ret.meta[0]) is DocstringParam
    assert ret.meta[0].arg_name == "x"

# Generated at 2022-06-13 20:00:14.197217
# Unit test for function parse
def test_parse():
    my_docstring = """\
    One-line summary of the function.

    Extended description of the function.

    Parameters
    ----------
    arg1 : int
        Description of `arg1`.
    arg2 : str
        Description of `arg2`.

    Returns
    -------
    Example
        Description of return value.
    \

    """
    print(parse(my_docstring))


# Generated at 2022-06-13 20:00:23.766298
# Unit test for function parse
def test_parse():
    s = """\
    This is a description.

    This is a long description consisting of several
    paragraphs.

    :param x: this is a parameter
    :param int y: another param
    :param ?z: a param with an optional type
    :param a: a param with a default
        defaults to 1
    :param b: a param with a default and optional type
        defaults to 2
    :param ?c=something: a param with a default
    :param ?d=something: a param with a default and optional type
    :param ?e: a param with default value None
    :param ?f: a param with default value None and an optional type
    :type e: int

    :param g: a param with a type annotation
    :type g: int
    """

    d = parse(s)

# Generated at 2022-06-13 20:00:31.550753
# Unit test for function parse
def test_parse():
    text = '''
        This is a summary

        This is a longer explanation.

        :param name: this is parameter name
        :type name: str
        :param value: this is parameter value
        :type value: bool
        :returns: this is returns
        :rtype: bool
        :raises KeyError: raises description
    '''

    #print(parse(text))
    r0 = parse(text)

    assert r0.short_description == "This is a summary"
    assert r0.long_description == "This is a longer explanation."
    assert r0.blank_after_short_description is True
    assert r0.blank_after_long_description is False
    assert len(r0.meta) == 4

    assert r0.meta[0].description == "this is parameter name"
    assert r0

# Generated at 2022-06-13 20:00:42.429444
# Unit test for function parse
def test_parse():
    parsed = parse('''\
Test a docstring parsing for a function.

We test different arguments and keywords, ensuring there are no bugs.

:Parameters:
    - **first** (int) -- This is the first parameter.
    - **second** (int)
    - **third** (int) -- This parameter is optional and defaults to 0.
    - **fourth** (int) -- This parameter is optional, and has a default value.
        The default is ``None``.

:Returns:
    int - Another word. And another word.
    ''')

# Generated at 2022-06-13 20:00:51.140482
# Unit test for function parse
def test_parse():
    res = parse.__doc__
    docstring = parse(res)
    print(docstring)


# Generated at 2022-06-13 20:01:01.209654
# Unit test for function parse
def test_parse():
    # empty string
    parsed = parse("")
    assert parsed.short_description == None
    assert parsed.long_description == None
    assert parsed.meta == []
    assert parsed.blank_after_short_description == False
    assert parsed.blank_after_long_description == False

    # Give you a string, you return the parsed version.
    # This is pretty intense, I should make a few of them.
    raw = """\
    This is a docstring.

    This is the long description.

    This is the second paragraph of the long description.

    :param foo: this is a parameter
    :param bar: this is another parameter
    :returns: description of return value
    :raises Error: this is an exception
    """
    parsed = parse(raw)
    # print(parsed)
    assert parsed.short_

# Generated at 2022-06-13 20:01:10.410007
# Unit test for function parse
def test_parse():
    ta = textwrap.dedent("""
    :param int a: an integer
    :param str b: a string
    :param optional bool c: an optional boolean
    :param defaults to True d: a boolean
    :param str e: defaults to 'foo'.
    :param str e: defaults to `foo`.
    :yields: a boolean
    :yield int f: a boolean
    :returns: a boolean
    :return bool g: a boolean
    :raises: ValueError
    :raises ValueError h: ValueError
    :raises ValueError h: something
    :raises ValueError h: something else""")

    ds = parse(ta)
    assert ds.short_description == ''
    assert ds.blank_after_short_description == False
    assert ds.long_description == None


# Generated at 2022-06-13 20:01:22.102639
# Unit test for function parse
def test_parse():
    assert parse(
        """\
    Short description.

    Long description.
    """
    ) == Docstring(
        short_description="Short description.",
        long_description="Long description.",
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )

    assert parse(
        """\
    Short description.

    Long description.

    :returns: None
    """
    ) == Docstring(
        short_description="Short description.",
        long_description="Long description.",
        blank_after_short_description=False,
        blank_after_long_description=True,
        meta=[DocstringReturns(args=["returns"], description="None")],
    )


# Generated at 2022-06-13 20:01:26.377956
# Unit test for function parse
def test_parse():
    code = """
    This is the short description.

    This is the long description.
    It may go to multiple lines.
    """
    # Return type of parse is Docstring
    # Docstring is a namedtuple with
    # 5 fields
    assert parse(code).short_description == 'This is the short description.'
    assert parse(code).long_description == 'This is the long description.\nIt may go to multiple lines.'
    assert parse(code).blank_after_short_description == True
    assert parse(code).blank_after_long_description == True
    assert parse(code).meta == []

    # For a more complicated example

# Generated at 2022-06-13 20:01:30.568867
# Unit test for function parse
def test_parse():
    values = ":param a: this is help\n   this is help\n:param b: this is help\n:raises ValueError: this is help\n:raises ValueError"
    assert parse(values) is not None



# Generated at 2022-06-13 20:01:42.178525
# Unit test for function parse
def test_parse():
    def describe_parse(**kwargs):
        """
        :param kwargs:
        :return:
        """


# Generated at 2022-06-13 20:01:51.793783
# Unit test for function parse
def test_parse():
    from .common import Docstring
    from .common import DocstringMeta
    from .common import DocstringParam
    from .common import DocstringRaises
    from .common import DocstringReturns
