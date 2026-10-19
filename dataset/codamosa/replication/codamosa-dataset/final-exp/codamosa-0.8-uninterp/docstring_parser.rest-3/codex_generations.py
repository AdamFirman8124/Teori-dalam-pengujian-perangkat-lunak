

# Generated at 2022-06-13 19:52:21.734290
# Unit test for function parse

# Generated at 2022-06-13 19:52:28.426637
# Unit test for function parse
def test_parse():
    test_string = """
    Short description.

    Long description.

    :rtype:  str
    :param arg:  this is a arg
    :param arg2:  this is also a arg
    :raises TypeError:  if arg is None
    :returns:  this is a return value
    :returns optional:  this is an optional return value
    :returns (tuple):  this is a tuple
    :returns (list):  this is a list
    :raises ValueError:  if the value is wrong

    The last paragraph of the docstring.
    """


# Generated at 2022-06-13 19:52:43.251755
# Unit test for function parse
def test_parse():
    text = """A function.
    
    :param foo: A parameter. Defaults to 1.
    :param bar: A parameter.
    :param baz: Another parameter.
    :param baz2: Another parameter.
    :returns: Stuff
    :returns: type
    :raises: Exception
    :raises: exception
    :yields: Stuff
    :yields: type
    :return: xxx
    :blah: xxx
    """
    docstring = parse(text)
    assert docstring.short_description == 'A function.'
    assert docstring.long_description == 'A parameter. Defaults to 1.\nA parameter.\nAnother parameter.\nAnother parameter.\nStuff\nxxx'
    assert len(docstring.meta) == 11
    assert docstring.meta

# Generated at 2022-06-13 19:52:54.149216
# Unit test for function parse
def test_parse():
    text_simple = "This is a simple docstring\n"
    text_simple_with_blank_line = "This is a simple docstring with a blank line\n\n"
    text_simple_with_long_description = """\
    This is a simple docstring with a long description
    Like this one!
    """
    text_simple_with_long_description_inline = """\
    This is a simple docstring with a long description like this one inline!
    """
    text_simple_with_long_description_2_blank_lines = """\
    This is a simple docstring with a long description like this one with
    two blank lines!


    """

# Generated at 2022-06-13 19:53:06.309683
# Unit test for function parse

# Generated at 2022-06-13 19:53:14.539128
# Unit test for function parse
def test_parse():
    text = """
    This is the short description.

    This is the long description. It can span
    multiple lines.

    :param int foo: Foo description
    :type foo: List of ints
    :param bar: Bar description
    :type bar: List of str
    :returns: Return description
    :rtype: List of str
    :return something: Something description
    :rtype something: List of str
    :yields: Yield description
    :ytype: List of str
    :yield an_item: An item description
    :ytype an_item: List of str
    :raises Exception: Raises description
    :raises TypeError: Raises description
    :raises: Raises description
    :raises TypeError: Raises description
    """
    ds = parse(text)
    assert d

# Generated at 2022-06-13 19:53:28.109762
# Unit test for function parse
def test_parse():
    comment = """\
    Example function with types documented in the docstring.

    :param int a: The first int.
    :param int b: The second int.
    :returns: The return value.
    :rtype: int
    """

    docstring: Docstring = parse(comment)
    assert docstring.short_description == "Example function with types documented in the docstring."
    assert docstring.meta == [
        DocstringParam(["param", "int", "a"], "The first int."),
        DocstringParam(["param", "int", "b"], "The second int."),
        DocstringReturns(["returns"], "The return value.", "int"),
    ]



# Generated at 2022-06-13 19:53:37.111942
# Unit test for function parse
def test_parse():
    text = '''Single line short description.
    Multi-line
    long description.

    :param int foo: Parameter foo
    :param int bar: Parameter bar

    :raises ValueError: Exception raised when the input is invalid.
    :returns: output
    '''

# Generated at 2022-06-13 19:53:49.949302
# Unit test for function parse
def test_parse():
    doc = parse(
        """\
        This is a short description.

        This is a long description.

        :type foo: str
        :type bar: int|None
        :type baz: list or None
        :param i: Some integer.
        :param foo: Some string.
        :param bar: Some integer or None.
        :param baz: Either a list or None.
        :raises Exception: Something bad happened.
        :raises RuntimeError: Something bad happened.
        :returns: None
        :returns: Something
        :return: None
        :return: Something
        :yields: None
        :yields: Something
        :yield: None
        :yield: Something
        :rtype: int
        """
    )


# Generated at 2022-06-13 19:54:03.076768
# Unit test for function parse
def test_parse():
    docstring = """
    Do some stuff.

    :param foo: The foo.
    :type foo: int
    :raises ValueError: If x is greater than y.
    :returns: None
    :rtype: str
    """
    expected = Docstring()
    expected.short_description = "Do some stuff."
    expected.blank_after_short_description = False
    expected.long_description = ""
    expected.blank_after_long_description = True

    doc_item = DocstringParam(
        args=["param", "foo", "int"],
        description="The foo.",
        arg_name="foo",
        type_name="int",
        is_optional=False,
        default=None,
    )
    expected.meta.append(doc_item)

    doc_item = DocstringRaises

# Generated at 2022-06-13 19:54:37.225567
# Unit test for function parse
def test_parse():
    docstring = parse("""Initialize a new parser.
        :param foo: the foo of the bar
        :param bar: the bar of the foo (defaults to some
            nonsensical value)
        :type bar: int
        :returns: the parsed result
        :rtype: int
        :raises ValueError: if the value is invalid
        """)
    assert docstring.short_description == "Initialize a new parser."
    assert docstring.long_description == ("the foo of the bar\nthe bar of "
                                          "the foo (defaults to some\nnonsen"
                                          "sical value)")
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description

    assert len(docstring.meta) == 4


# Generated at 2022-06-13 19:54:51.306017
# Unit test for function parse
def test_parse():
    s = """\
    My func.

    :param name: The name to use.
    :param state: Current state to be in.
    :raises ValueError: Raised if `name` is empty.
    :rtype: None
    """
    p = parse(s)
    assert p.short_description == "My func."
    assert p.long_description == "The name to use.\nCurrent state to be in."
    assert p.blank_after_short_description is True
    assert p.blank_after_long_description is True
    assert len(p.meta) == 3
    assert p.meta[0].arg_name == "name"
    assert p.meta[1].arg_name == "state"
    assert p.meta[1].description == "Current state to be in."
    assert p.meta

# Generated at 2022-06-13 19:54:53.216482
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    import doctest

    doctest.testmod()

# Generated at 2022-06-13 19:55:04.208494
# Unit test for function parse
def test_parse():
    docstring = """
This is a very short description.

This is a very long description.

:param arg: The first argument.
:type arg: bool
:param arg2: The second argument.
:type arg2: int
:return: Nothing
:rtype: None
    """


# Generated at 2022-06-13 19:55:11.489310
# Unit test for function parse
def test_parse():
    doc = """
This is a brief description.

This is a long description.

:param int x: the x parameter
:param str s: string parameter that defaults to "abc".
:param z: Another param
:param NoneType f: a param without a type
:return: the return value
:rtype:
    """

    ret = parse(doc)
    assert isinstance(ret, Docstring)

    params = ret.meta_as_dict()["params"]
    assert isinstance(params, dict)
    assert len(params) == 4
    assert isinstance(params["x"], DocstringParam)
    assert params["x"].type_name == "int"
    assert params["x"].is_optional is False
    assert params["x"].default is None

    assert isinstance(params["s"], DocstringParam)
   

# Generated at 2022-06-13 19:55:15.785230
# Unit test for function parse
def test_parse():
    docstring = parse('short desc\n\nlong desc\n\n:arg x: desc\n:return: desc\n:param y: desc\n:returns z: desc')
    assert docstring.short_description == 'short desc'
    assert docstring.long_description == 'long desc'
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False
    assert docstring.meta[0].__class__.__name__ == 'DocstringParam'
    assert docstring.meta[0].type_name == None
    assert docstring.meta[0].is_optional == False
    assert docstring.meta[0].arg_name == 'x'
    assert docstring.meta[1].__class__.__name__ == 'DocstringReturns'

# Generated at 2022-06-13 19:55:18.875552
# Unit test for function parse
def test_parse():
    text = """
    This is a test of the parse function.

    :param int x:
        This is x.
    """
    print(parse(text))



# Generated at 2022-06-13 19:55:31.034738
# Unit test for function parse
def test_parse():
    docstring = r"""
        Test for parse function

        This is a long description

        :param name: this is name
        :type name: str
        :param age: this is age
        :type age: int, optional
        :returns: test return
        :rtype: str
        :raises ValueError: an error occurred
        :raises TypeError: another error occurred
    """
    parsed = parse(docstring)
    assert parsed.short_description == "Test for parse function"
    assert parsed.long_description == \
        "This is a long description"
    assert parsed.meta[0].arg_name == "name"
    assert parsed.meta[0].type_name == "str"
    assert parsed.meta[1].arg_name == "age"

# Generated at 2022-06-13 19:55:38.704645
# Unit test for function parse
def test_parse():
    docstring = """\
    Short summary.

    Long-ish summary

    Parameters
    ----------
    arg: str
        Short arg description

    arg2: str
        Short arg2 description

    arg3: str
        Short arg3 description.
        Longer line in arg3.
        Even longer.

    arg4: int
        Short arg4 description

    arg5: str, optional
        Short arg5 description. Defaults to 'foo'.

    arg6: str, optional
        Short arg6 description. Defaults to:
            ['a', 'b', 'c']

    arg7: int, optional
        Short arg7 description. Defaults to the value of:
            somefunction()

    Returns
    -------
    str
        Short return description

    Raises
    ------
    OSError
        Short error description
    """


# Generated at 2022-06-13 19:55:44.542032
# Unit test for function parse
def test_parse():
    # docstring = """A short description.
    #
    # :param a: The first parameter.
    # :param b: The second parameter.
    # :type b: str
    # :returns: None
    # :raises ValueError: Raises ValueError.
    # """
    # print(parse(docstring))
    pass



# Generated at 2022-06-13 19:56:14.560699
# Unit test for function parse
def test_parse():
    def f():
        """Get a rectangle.

        :param int x: The x coordinate.
        :param int y: The y coordinate.
        :param int width: The rectangle width. Defaults to 0.
        :param int height: The rectangle height. Defaults to 0.
        :returns Rectangle: The rectangle.

        """
        return

    ds = parse(f.__doc__)

    assert ds.short_description == "Get a rectangle."
    assert ds.blank_after_short_description
    assert ds.long_description is None
    assert ds.blank_after_long_description

    assert len(ds.meta) == 4

    assert ds.meta[0].args == ["param", "int", "x"]
    assert ds.meta[0].arg_name is None
    assert ds

# Generated at 2022-06-13 19:56:24.416767
# Unit test for function parse
def test_parse():
    docstring = parse(
        """
    Return the top 1 favorite programming language from a list of language
    preferences, per each user or the global average.

    :param lang_pref: a list of tuples of (user, language, frequency index)
    :type lang_pref: list of tuples
    :param as_dict: if True, return a dict
    :type as_dict: bool
    :rtype: str or dict
    :returns: the favorite language
    """
    )

    assert docstring.short_description == "Return the top 1 favorite programming language from a list of language preferences, per each user or the global average."
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == True

# Generated at 2022-06-13 19:56:34.324075
# Unit test for function parse
def test_parse():
    s = """\
        Short description.

        Long description.

        :param str name: description
        :param int age: description
        :returns: description
        """
    docstring = parse(s)
    assert docstring.short_description == 'Short description.'
    assert docstring.long_description == 'Long description.'
    assert docstring.blank_after_short_description

# Generated at 2022-06-13 19:56:41.799431
# Unit test for function parse
def test_parse():
    docstring = """
    Parse the ReST-style docstring into its components.

    :returns: parsed docstring
    """
    result = parse(docstring)
    assert isinstance(result, Docstring)
    assert isinstance(result.meta, list)
    assert len(result.meta) == 1
    assert isinstance(result.meta[0], DocstringReturns)
    assert result.meta[0].description == "parsed docstring"

# Generated at 2022-06-13 19:56:50.704413
# Unit test for function parse

# Generated at 2022-06-13 19:57:03.299905
# Unit test for function parse

# Generated at 2022-06-13 19:57:14.460552
# Unit test for function parse
def test_parse():
    ''' Testing parse function'''
    docstring = """Testing parse function
    :param tuple(int) tup: Parameter description
    :returns int [some]:
        Return description

        With more description
    :raises ValueError: If an exception is raised
    """
    d = parse(docstring)
    assert d.short_description == 'Testing parse function'
    assert d.long_description == 'Return description\n\nWith more description'
    assert d.blank_after_short_description == True
    assert d.blank_after_long_description == True
    assert d.meta[0].arg_name == 'tup'
    assert d.meta[0].type_name == 'tuple(int)'
    assert d.meta[0].is_optional == None
    assert d.meta[0].default == None


# Generated at 2022-06-13 19:57:27.126836
# Unit test for function parse
def test_parse():
    import pytest

    with pytest.raises(ParseError):
        parse("")
    with pytest.raises(ParseError):
        parse("\n")

    docstring = parse("hello world")
    assert docstring.short_description == "hello world"
    assert docstring.long_description is None
    assert docstring.meta == []

    docstring = parse("hello world\n\nbar")
    assert docstring.short_description == "hello world"
    assert docstring.blank_after_short_description
    assert docstring.long_description == "bar"

    docstring = parse("foo:\n  bar")
    assert docstring.short_description == "foo:"
    assert docstring.long_description == "  bar"


# Generated at 2022-06-13 19:57:37.333390
# Unit test for function parse
def test_parse():
    """
    Test parse function.
    """
    assert parse("""
    Short description.

    Long description.
    """) == Docstring(
        short_description="Short description.",
        blank_after_short_description=True,
        long_description="Long description.",
        blank_after_long_description=True,
        meta=[],
    )

    assert parse("""
    Short description.

    Long description with
    another line.
    """) == Docstring(
        short_description="Short description.",
        blank_after_short_description=True,
        long_description="Long description with\nanother line.",
        blank_after_long_description=True,
        meta=[],
    )


# Generated at 2022-06-13 19:57:50.659757
# Unit test for function parse
def test_parse():
    from .common import TEST_DOCSTRING_PARAMS_EXPECT_STR

    r = parse(TEST_DOCSTRING_PARAMS_EXPECT_STR)
    assert r.short_description == "hi"
    assert r.long_description == "hihihi"
    assert r.blank_after_short_description is True
    assert r.blank_after_long_description is False
    assert len(r.meta) == 1
    assert r.meta[0].args == ['param', 'arg_name']
    assert r.meta[0].description == 'doc'
    assert r.meta[0].arg_name == 'arg_name'
    assert r.meta[0].type_name == None
    assert r.meta[0].is_optional == None
    assert r.meta[0].default == None

    r

# Generated at 2022-06-13 19:58:16.270302
# Unit test for function parse
def test_parse():
    test1 = """
    """
    assert parse(test1) == Docstring()

    test1_long = """
    One line short description.

    More detailed description.
    """
    assert parse(test1_long) == Docstring(
        short_description="One line short description.",
        blank_after_short_description=True,
        long_description="More detailed description.",
        blank_after_long_description=True,
    )

    test1_long_no_blank = """
    One line short description.

    More detailed description.
    """

# Generated at 2022-06-13 19:58:26.801390
# Unit test for function parse
def test_parse():
    """
    Test the function parse.
    """
    txt_1 = """
    The function docstring.

    :type x: int
    :type y: float, optional
    :type z: bool, default True

    :param x: An int.
    :param y: A float (default 1.0).
    :param z: A bool, defaults to True.

    :raises: Exception if something happens.

    :rtype: list
    :returns: a list of values
    """
    txt_1_parsed = """
    The function docstring.
    """
    txt_2_parsed = """
    :type x: int
    """
    txt_3_parsed = """
    :type y: float, optional
    """

# Generated at 2022-06-13 19:58:39.942857
# Unit test for function parse
def test_parse():
    docstring = """This is the short description.
The long description is quite long

    It can contain code
    and blank lines


:param arg1: description
:param arg2: description
:param arg3: description
:type arg3:
:rtype:
:raises:
:returns:
"""
    test = parse(docstring)
    assert test.short_description == 'This is the short description.'
    assert test.long_description == 'The long description is quite long\n\nIt can contain code\nand blank lines'
    assert len(test.meta) == 6
    assert test.meta[0].args == ['param', 'arg1']
    assert test.meta[0].description == 'description'
    assert test.meta[5].args == ['returns']

# Generated at 2022-06-13 19:58:48.962043
# Unit test for function parse
def test_parse():
    """Test function parse"""
    docstring = """
    A short description of the function.

    A long description of the function and how it works.

    :param arg1:
        The first argument.

        This is the first argument and is required.
    :type arg1: str
    :param arg2: The second argument.
    :type arg2: int
    :returns:
        The return value.

        This is the return value.
    :rtype: bool
    """

    result = parse(docstring)
    assert isinstance(result, Docstring)

    result = parse("")
    assert isinstance(result, Docstring)

    result = parse("A short description")
    assert isinstance(result, Docstring)


# Generated at 2022-06-13 19:58:59.859114
# Unit test for function parse
def test_parse():
    docstring = """
    This is the short description.

    This is the long description.

    :param foo: this is foo
    :param bar: this is bar with defaults to 4.
    :param baz: this is baz with a default that defies sanity
                 and also spans multiple lines
    :returns: nothing
    :raises ValueError: if things go wrong
    """

# Generated at 2022-06-13 19:59:09.045220
# Unit test for function parse
def test_parse():
    text = """\
        This is a short description.

        This is a long
        description.

        :param arg1: This is the first argument.
        :param arg2: This is the second argument.
    """
    assert parse(text).short_description == "This is a short description."
    assert parse(text).long_description == "This is a long description."
    assert parse(text).blank_after_short_description
    assert not parse(text).blank_after_long_description
    assert not parse(text).meta


# Generated at 2022-06-13 19:59:21.200042
# Unit test for function parse
def test_parse():
    doc_str = """
    Summary line.
    Extended description.

    :param arg_name: Description of arg_name.
    :type arg_name: builtins.int
    :param kwarg_name: Description of kwarg_name.
    :type kwarg_name: builtins.bool
    :returns: Description of return value.
    :rtype: float
    :raises ZeroDivisionError: Description of ZeroDivisionError.
    """
    doc = parse(doc_str)
    assert doc.short_description == "Summary line."
    assert doc.long_description == "Extended description."
    assert doc.blank_after_short_description == True
    assert doc.blank_after_long_description == False
    assert len(doc.meta) == 4
    assert doc.meta[0] == Doc

# Generated at 2022-06-13 19:59:31.782263
# Unit test for function parse
def test_parse():
    doc = """Summary line.

Description of what this does, how it does it,
and any other relevant information.

    :param foo: Foo, this is a description of foo.
    """

    parsed = parse(doc)
    assert parsed.short_description == 'Summary line.'
    assert parsed.long_description == 'Description of what this does, how it does it,\nand any other relevant information.'
    assert len(parsed.meta) == 1
    assert parsed.meta[0].args == ['param', 'foo']
    assert parsed.meta[0].description == 'Foo, this is a description of foo.'

    doc = """Summary line.
:param bar: Bar, this is a description of bar.
    """

    parsed = parse(doc)
    assert parsed.short_description == 'Summary line.'
    assert parsed.long

# Generated at 2022-06-13 19:59:42.157230
# Unit test for function parse
def test_parse():
    doc = """
    Basic function documentation.

    .. code-block:: python

        with open("file.txt") as f:
            for line in f:
                print(line)

    :param name: some keyword.
    :return: The return value. True for success, False otherwise.
    :rtype: boolean

    :param optional arg1: An optional parameter.
    :param optional arg2: Another optional parameter.
    """
    res = parse(doc)
    #print(res)


# Generated at 2022-06-13 19:59:54.109954
# Unit test for function parse

# Generated at 2022-06-13 20:00:13.400698
# Unit test for function parse
def test_parse():
    docstring = parse(
        """Shows information about a given member.
    Parameters
    ----------
    member : :class:`discord.Member`
        The member to show information of.
    Returns
    -------
    None
        Returns nothing.
    """
    )
    assert docstring.short_description == "Shows information about a given member."

# Generated at 2022-06-13 20:00:23.241496
# Unit test for function parse
def test_parse():
    # Testing: def foo(bar, baz): """baz that foo(bar)."""
    docstring = parse("""
    baz that foo(bar)
    """)
    assert docstring.short_description == "baz that foo(bar)"
    assert docstring.blank_after_short_description == False
    assert docstring.long_description == None
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []

    # Testing: def foo(bar, baz): """baz that foo(bar).

    # Foo foo foo.
    # """
    docstring = parse("""
    baz that foo(bar).

    Foo foo foo.
    """)
    assert docstring.short_description == "baz that foo(bar)."
    assert docstring.blank_after_short_

# Generated at 2022-06-13 20:00:31.018214
# Unit test for function parse
def test_parse():
    docstring = parse('''
    This is a short description.
    This is a long description.

    :param type_name arg_name: This is a desc.
    :param int arg_name: This is a desc.
    :param int arg_name: This is a desc.
    :param int arg_name: This is a desc.
    :returns str: This is a desc.
    ''')
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description == 'This is a long description.'
    assert docstring.blank_after_long_description is True
    assert docstring.meta[0].arg_name == 'type_name'
    assert docstring.meta[0].type_name == 'type_name'
    assert docstring.meta[1].arg_name

# Generated at 2022-06-13 20:00:36.934267
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()

    s = "One line docstring."
    assert parse(s) == Docstring(short_description=s)

    s = "One line docstring with colon: and period."
    assert parse(s) == Docstring(short_description=s)

    s = "One line docstring.\n"
    assert parse(s) == Docstring(short_description="One line docstring.")

    s = "One line docstring with colon: and period.\n"
    assert parse(s) == Docstring(
        short_description="One line docstring with colon: and period."
    )

    s = "One line docstring.\n\n"
    assert parse(s) == Docstring(
        short_description="One line docstring.", blank_after_short_description=True
    )



# Generated at 2022-06-13 20:00:46.841271
# Unit test for function parse
def test_parse():
    from pprint import pprint

# Generated at 2022-06-13 20:00:52.104963
# Unit test for function parse
def test_parse():
    print(parse(
        """
        docstring.

        .. code-block:: python

            test code
            test code

        .. code-block:: python

            test code

                test code
        """))

    print(parse(
        """
        docstring.

        :returns:
            this is return

        :param x: int
            this is x"""
    ))

# Generated at 2022-06-13 20:01:01.797738
# Unit test for function parse
def test_parse():
    """Test for function parse.

    :returns: success or failure of test
    :rtype: bool
    """
    from .common import Docstring, DocstringParam, DocstringRaises, DocstringReturns

    # case: no docstring
    docstring = Docstring()
    assert parse("") == docstring

    # case: empty docstring only contains short description
    docstring.short_description = "short description"
    assert parse("short description") == docstring

    # case: short description
    docstring.short_description = "short description"
    assert parse(":short description") == docstring

    # case: short description with newline
    docstring.short_description = "short description"
    assert parse(":\nshort description") == docstring

    # case: short description with whitespace

# Generated at 2022-06-13 20:01:09.140929
# Unit test for function parse
def test_parse():
    docstring = inspect.getdoc(parse)
    print("\nPrinting the description of the function parse:")
    print(docstring)
    print("\nPrinting the type of the docstring:")
    print(type(docstring))
    print("\nPrinting the type of the docstring after parsing:")
    print(type(parse(docstring)))
    print("\nPrinting the _build_meta class of the docstring after parsing:")
    print(parse(docstring).meta)
    print("\nPrinting the type of the _build_meta class after parsing:")
    print(type(parse(docstring).meta))



# Generated at 2022-06-13 20:01:14.840288
# Unit test for function parse
def test_parse():
    doc = """\
    test_parse

    tests the parse function

    :param keywords: keywords
    :type keywords: list
    :returns: return
    :rtype: str
    :raises exception: raises exception
    :yields: yields
    """
    result = parse(doc)
    print(result)
    assert result.short_description == 'test_parse'
    assert result.long_description == 'tests the parse function'
    assert result.blank_after_short_description == False
    assert result.blank_after_long_description == True # True after strip()
    assert len(result.meta) == 4
    assert isinstance(result.meta[0],DocstringParam)
    assert result.meta[0].args[0] == 'param'

# Generated at 2022-06-13 20:01:25.406150
# Unit test for function parse
def test_parse():
    from pprint import pprint
    from .parse_doctest import test_parse_doctest
    from .parse_googledoc import test_parse_googledoc
    
    def verify_text(text, expected):
        result = parse(text)
        assert (result == expected)
       
    def test_parse_text(text: str, expected: Docstring, fn_name: str = "fn"):
        try:
            doc = parse(text)
            assert doc == expected
            return True
        except AssertionError as e:
            print("\nTesting {}".format(fn_name))
            print("=" * 50)
            print("text:")
            print("=" * 50)
            print(text)
            print("=" * 50)
            print("parsed:")

# Generated at 2022-06-13 20:01:42.848199
# Unit test for function parse
def test_parse():
    text = '''
    Something totally amazing.
    
    :param my_param: Something nice.
    :type my_param: int
    :param another_param: Something nice.
    :type another_param: int
    :returns: Something nice.
    '''
    result = parse(text)
    assert result.short_description == 'Something totally amazing.'
    assert result.meta[0].arg_name == 'my_param'
    assert result.meta[1].arg_name == 'another_param'
    assert result.meta[2].description == 'Something nice.'


# Generated at 2022-06-13 20:01:52.246326
# Unit test for function parse
def test_parse():
    doc1 = parse("")
    assert doc1.short_description == None
    assert doc1.blank_after_short_description is None
    assert doc1.long_description == None
    assert doc1.blank_after_long_description is None
    assert doc1.meta == []
    doc2 = parse("""\
        Short description.

        Long description.

        :param name: The name to display.
        :param value: The value to display.
        :raises ValueError: If `name` is empty.
        :returns: The removed item.
        :raises KeyError: If `name` is not in the dictionary.
        :returns: The removed item.
        :param name: The name to display.
        :param value: The value to display.
        """)