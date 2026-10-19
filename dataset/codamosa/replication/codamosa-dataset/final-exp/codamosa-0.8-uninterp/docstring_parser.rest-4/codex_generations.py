

# Generated at 2022-06-13 19:52:05.905076
# Unit test for function parse

# Generated at 2022-06-13 19:52:21.320871
# Unit test for function parse
def test_parse():
    """Test parsing the ReST docstring to the components"""

# Generated at 2022-06-13 19:52:30.498397
# Unit test for function parse
def test_parse():
    docstring = """
    Short description.

    Long description.

    :param arg1:
        Arg1 description
    :type arg1:
        int
    :param arg2:
        Arg2 description
    :type arg2:
        float
    :return:
        Return description
    :rtype:
        ndarray
    """
    doc = parse(docstring)
    assert doc.short_description == "Short description."
    assert doc.long_description == "Long description."
    assert doc.blank_after_short_description
    assert doc.blank_after_long_description
    assert len(doc.meta) == 4
    assert doc.meta[0].key == "param"
    assert doc.meta[0].arg_name == "arg1"
    assert doc.meta[0].type_name == "int"

# Generated at 2022-06-13 19:52:44.037507
# Unit test for function parse
def test_parse():
    test_docstring = """One line summary.

Longer description.
  May span multiple lines.

:param type_name arg_name: Argument description.
:param type_name arg_name: Argument description.

:returns: Description
:rtype: str
:yields: Description
:ytype: str

:raises TypeError: if an exception is raised
"""
    parsed = parse(test_docstring)
    assert parsed.short_description == "One line summary."
    assert (
        parsed.long_description
        == "Longer description.\n  May span multiple lines."
    )
    assert parsed.blank_after_short_description
    assert parsed.blank_after_long_description
    assert len(parsed.meta) == 3
    assert type(parsed.meta[0]) == Doc

# Generated at 2022-06-13 19:52:54.833883
# Unit test for function parse
def test_parse():
    text = """
    """
    parse(text) == Docstring()

    text = """
    """
    parse(text) == Docstring(
        short_description=None,
        blank_after_short_description=False,
        long_description=None,
        blank_after_long_description=True,
    )

    text = """
    """
    parse(text) == Docstring(
        short_description=None,
        blank_after_short_description=True,
        long_description=None,
        blank_after_long_description=False,
    )

    text = """
    """
    parse(text) == Docstring(
        short_description=None,
        blank_after_short_description=False,
        long_description="",
        blank_after_long_description=False,
    )

# Generated at 2022-06-13 19:53:06.826612
# Unit test for function parse
def test_parse():
    sample = '''
    A sample function that shows the use of doctest.

    :param int x: The first sample variable.
    :param str y: The second sample variable.
    :return:
    :raises ValueError: The error raised.
    :raises KeyError: The error raised.
    '''
    result = parse(sample)
    assert result.short_description == "A sample function that shows the use of doctest."
    assert len(result.meta) == 5
    assert result.meta[0].args == ['param', 'int', 'x']
    assert result.meta[0].description == "The first sample variable."
    assert result.meta[1].args == ['param', 'str', 'y']
    assert result.meta[1].description == "The second sample variable."
    assert result.meta[2].args

# Generated at 2022-06-13 19:53:15.634843
# Unit test for function parse
def test_parse():
    docstring = """
    Short description.

    Long description.

    :param type arg1: description
    :type arg1: type
    :param arg2: description
    :keyword type arg3: description
    :keyword arg4: description
    :returns: what is returned
    :rtype: type
    :rtype: desc
    :returns: desc
    :return: desc
    :yields: what is yielded
    :yields: desc
    :yield: desc
    :raises Exc: what exceptions are raised
    :raises Exc: desc
    :raise Exc: desc
    """
    assert parse(docstring)

test_parse()

# Generated at 2022-06-13 19:53:30.821885
# Unit test for function parse
def test_parse():
    source = r"""
    Docstring summary.
    
    Long description.
    
    :param a: A parameter.
    :type a: int
    :param b: Another parameter, defaults to None.
    :type b: str
    :param c: Yet another parameter, defaults to None.
    :type c: str
    :rtype: str
    :return: Return description
    :raises ValueError: raise description
    """
    actual = parse(source)

# Generated at 2022-06-13 19:53:42.977435
# Unit test for function parse
def test_parse():
    """
    Test that we can parse a docstring.
    """
    def dummy():
        """
        This is a short description.

        This is a long description.

        :param foo: this is a param
        :type foo: str
        :param bar: this is a param
        :param baz: this is a param
        :returns: None
        :rtype: None
        :raises ValueError: if things go wrong
        """

    docstring = parse(dummy.__doc__)
    assert docstring.short_description == "This is a short description."
    assert docstring.long_description == "This is a long description."
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description
    assert isinstance(docstring.meta[0], DocstringParam)


# Generated at 2022-06-13 19:53:49.956174
# Unit test for function parse
def test_parse():
    """Test parse function

    Example:
        >>> docstr = """

# Generated at 2022-06-13 19:54:03.378958
# Unit test for function parse
def test_parse():
    text = """
    Test docstring
    """

    assert parse(text) == Docstring(
        short_description = "Test docstring",
        blank_after_short_description = False,
        blank_after_long_description = False,
        long_description = None,
        meta = []
    )

    text = """
    Test docstring
    :param str name: Name of a parameter
    :param int age: Age of a parameter
    """


# Generated at 2022-06-13 19:54:13.403709
# Unit test for function parse
def test_parse():
    # Description-only
    text = """
    This is the description.
    """
    parsed = parse(text)
    assert parsed.short_description == "This is the description."
    assert not parsed.blank_after_short_description
    assert parsed.long_description is None
    assert parsed.meta == []
    assert parsed.blank_after_long_description

    # Description with parameters
    text = """
    This is the description.

    :param param1: Description of param1
    :param param2: Description of param2
    """
    parsed = parse(text)
    assert parsed.short_description == "This is the description."
    assert not parsed.blank_after_short_description
    assert parsed.long_description is None
    assert len(parsed.meta) == 2
    assert parsed.meta[0].arg_

# Generated at 2022-06-13 19:54:20.381497
# Unit test for function parse
def test_parse():
    docstring = """
    Parse the ReST-style docstring into its components.

    :returns: parsed docstring
    """
    ret = parse(docstring)
    print(ret)
    assert ret.short_description == "Parse the ReST-style docstring into its components."
    assert ret.blank_after_short_description == False
    assert ret.blank_after_long_description == False
    assert ret.long_description == None
    print(ret.meta[0].description)
    assert ret.meta[0].description == "parsed docstring"


# Generated at 2022-06-13 19:54:27.937060
# Unit test for function parse
def test_parse():
    test_doc_string = """
    This is a short description of the function.

    This is a long description of the function.
    This is a long description of the function.

    :param str arg1: Argument 1
    :param: Argument 2
    :returns: the return value
    """
    parse_results = parse(test_doc_string)
    assert (parse_results.short_description ==
                "This is a short description of the function.")
    assert (parse_results.long_description ==
                "This is a long description of the function.\nThis is a long description of the function.")
    assert (parse_results.blank_after_short_description == True)
    assert (parse_results.blank_after_long_description == False)

# Generated at 2022-06-13 19:54:32.225227
# Unit test for function parse
def test_parse():
    assert parse('test_function') == Docstring(
        short_description='test_function',
        blank_after_short_description=True,
        long_description=None,
        blank_after_long_description=False,
        meta=[],
    )

# Generated at 2022-06-13 19:54:35.317587
# Unit test for function parse
def test_parse():
    """Test docstring parsing."""
    import doctest

    return doctest.testmod(verbose=False)


# Generated at 2022-06-13 19:54:42.031889
# Unit test for function parse
def test_parse():
    t = inspect.cleandoc(r"""
        This is a docstring.
        It has two paragraphs.
        :param x: This is x.
        :param y: This is y.
        :param z: This is z. With some more stuff.
        :returns: a thing.
        :raises ValueError: if something

    """)

# Generated at 2022-06-13 19:54:55.881620
# Unit test for function parse
def test_parse():
    import typing as T

    docstring = inspect.cleandoc(
        """
        This function performs bread.

        :param str name: The name of the bread.
        :param str kind: The type of bread.
        :param int crustiness: Hardness of the crust.
        :param float weight: Weight of the bread, in Kg.
        :param float? price: Price of the bread, in dollars. Defaults to 0.5.
        :raises NotEnoughBreadError: When there is not enough bread.
        :raises TypeError: When something goes wrong.
        :returns: The bread object.
        """
    )


# Generated at 2022-06-13 19:55:00.132952
# Unit test for function parse
def test_parse():
    """
    This function verify the our parsing function works as expected.
    """
    input_string = """
    Parse the ReST-style docstring into its components.

    :returns: parsed docstring
    """
    parse(input_string)
    return



# Generated at 2022-06-13 19:55:09.158998
# Unit test for function parse
def test_parse():
    docstring = """This is a short description.

This is a long description.

:param arg1: argument 1
:type arg1: str
:param arg2: argument 2
:type arg2: int
:param arg3: argument 3
:type arg3: str or int
:returns: return type
:raises: raises error
:param optional_arg: an optional argument
:type optional_arg: str
:param optional_arg_with_default: an optional argument with a default value
:type optional_arg_with_default: str
:param optional_arg_with_type_and_default: an optional argument with a default value and a type
:type optional_arg_with_type_and_default: str
:key arg4: argument 4
:key arg5: argument 5
:key arg6: argument 6
"""
    expected

# Generated at 2022-06-13 19:55:27.141020
# Unit test for function parse
def test_parse():
    assert parse("").short_description is None  # type: ignore
    assert parse("").long_description is None  # type: ignore
    assert parse("").meta == []  # type: ignore

    assert parse("foo").short_description == "foo"  # type: ignore
    assert parse("foo").long_description is None  # type: ignore
    assert parse("foo").meta == []  # type: ignore

    assert (
        parse("foo\nbar").short_description == "foo"
    )  # type: ignore
    assert parse("foo\nbar").long_description == "bar"  # type: ignore
    assert parse("foo\nbar").meta == []  # type: ignore

    assert (
        parse("foo\n\nbar").short_description == "foo"
    )  # type: ignore

# Generated at 2022-06-13 19:55:38.582993
# Unit test for function parse
def test_parse():
    from . import render
    import pytest
    parse_and_render = lambda text: render(parse(text))

    # Simple example
    assert parse_and_render("""\
        Short description.

        Long description.
    """) == """\
    Short description.

    Long description.

    """

    # Argument descriptions
    assert parse_and_render("""\
        Short description.

        :param str arg1: this is where the description goes
        :param int arg2: this is where the description goes
    """) == """
    Short description.

    Arguments:
        arg1 (str): this is where the description goes
        arg2 (int): this is where the description goes

    """

    # Type annotations

# Generated at 2022-06-13 19:55:51.216671
# Unit test for function parse
def test_parse():
    docstring = '''
    This function adds two numbers

    :param a: first number
    :type a: float
    :param b: second number
    :type b: float
    :returns: The sum of the two numbers
    :rtype: float

    :Example:
    >>> add(1.0, 2.0)
    3.0
    '''

    parsed_docstring = parse(docstring)

    assert parsed_docstring.short_description == 'This function adds two numbers'
    assert parsed_docstring.long_description == '\n'.join(
        (
            ":Example:",
            ">>> add(1.0, 2.0)",
            "3.0",
        )
    )
    assert parsed_docstring.blank_after_short_description is True
    assert parsed_docstring

# Generated at 2022-06-13 19:55:59.536857
# Unit test for function parse
def test_parse():
    docstring = """Calculate the sum of two numbers.

:param first: Description of first number.
:param second: Description of second number.
:returns: The sum of the two numbers."""

    res = parse(docstring)

    assert res.short_description == "Calculate the sum of two numbers."
    assert res.long_description == None

# Generated at 2022-06-13 19:56:08.558050
# Unit test for function parse

# Generated at 2022-06-13 19:56:18.628100
# Unit test for function parse
def test_parse():
    s = """short description

long description

:param x: parameter 1
:param y: parameter 2
:param z: parameter 3
:returns: something
:raises ValidationError: some error
"""
    obj = parse(s)

    assert obj.short_description == "short description"
    assert obj.long_description == "long description"

    assert len(obj.meta) == 5
    assert isinstance(obj.meta[0], DocstringParam)
    assert isinstance(obj.meta[1], DocstringParam)
    assert isinstance(obj.meta[2], DocstringParam)
    assert isinstance(obj.meta[3], DocstringReturns)
    assert isinstance(obj.meta[4], DocstringRaises)


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et

# Generated at 2022-06-13 19:56:26.798122
# Unit test for function parse
def test_parse():
    docstring = parse("""Some very short description.
    And this is some intentionally long description that needs to be
    wrapped because it is too long.

    :param x: This is the X parameter
    :type x: int
    :raises: Exception, ValueError
    :returns: The summary of the function
    :rtype: int
    """)
    assert docstring.short_description == 'Some very short description.'
    assert docstring.long_description == """
    And this is some intentionally long description that needs to be
    wrapped because it is too long."""
    assert len(docstring.meta) == 3
    assert docstring.meta[0].arg_name == 'x'
    assert docstring.meta[0].type_name == 'int'
    assert docstring.meta[1].type_name is None
    assert doc

# Generated at 2022-06-13 19:56:28.626342
# Unit test for function parse
def test_parse():
    assert parse("Hey!")



# Generated at 2022-06-13 19:56:35.870288
# Unit test for function parse
def test_parse():
    docstring = """A very short description.

    This is a longer description. There are a couple of paragraphs, with
    some blank lines between them.

    :param int foo: This is the description of a parameter.
    :param str bar: This is the description of another parameter. It spans
                    multiple lines.
    :param bool baz: This is the description of yet another parameter. It has
                     a"default value."
    :return: gabble gabble
    :rtype: int
    :raises: A very short description of an exception.

    This is a paragraph that is part of the description of the return value.
    """
    assert parse(docstring).short_description == "A very short description."

# Generated at 2022-06-13 19:56:37.746893
# Unit test for function parse
def test_parse():
    # A function to test function parse
    # Return Docstring
    pass

# Generated at 2022-06-13 19:56:54.866938
# Unit test for function parse
def test_parse():
    docstring = """
    Some function

    This is a longer description that
    spans multiple lines.

    :Args:
        arg1 (str): description of arg1
        arg2 ("str?", "list[str]", "int?"): description of arg2
        arg3: description of arg3

    :Returns:
        str: description of ret

    :Raises:
        SomeException: description of exception
    """

# Generated at 2022-06-13 19:57:08.366691
# Unit test for function parse
def test_parse():
    text = '''A test function

    This function is meant to be an example of parsing a docstring.

    :param int a: A parameter named 'a'.
    :param any b: A parameter named 'b'.
    :keyword int c: A parameter named 'c'.
    :keyword any d: A parameter named 'd'.
    :raises ValueError: If any of the input arguments are invalid.
    :raises RuntimeError: If there is a problem accessing files.
    :returns: Nothing.
    :yields: The parameters in a list.
    '''
    string = parse(text)
    assert string.short_description == 'A test function'
    assert string.blank_after_short_description
    assert string.long_description == 'This function is meant to be an example of parsing a docstring.'
    assert not string

# Generated at 2022-06-13 19:57:17.840578
# Unit test for function parse
def test_parse():
    docstring = inspect.cleandoc("""
    Describes this function.

    Parameters:
        x: Type of parameter x.
        y: Type of parameter y.
        z: Type of parameter z.
        w: Type of parameter w?
    Returns:
        Returns a value
    Raises:
        ValueError: If something went wrong
    """)
    docstring = parse(docstring)
    assert docstring.short_description == "Describes this function."
    assert docstring.long_description == "Parameters:\n    x: Type of parameter x.\n    y: Type of parameter y.\n    z: Type of parameter z.\n    w: Type of parameter w?\nReturns:\n    Returns a value\nRaises:\n    ValueError: If something went wrong"
    assert len(docstring.meta) == 4

# Generated at 2022-06-13 19:57:29.281557
# Unit test for function parse
def test_parse():
    def run(docstring):
        obj = parse(docstring)
        assert repr(obj) == repr(parse(repr(obj)))
        return obj

    # Empty docstrings
    assert run("") == Docstring()
    assert run("\n") == Docstring()
    assert run("\n\n") == Docstring()

    # Short/long descriptions
    assert run("Hello, world.") == Docstring(short_description="Hello, world.")
    assert (
        run(
            """
        Foo bar baz.
        """
        )
        == Docstring(
            short_description="Foo bar baz.",
            long_description="Foo bar baz.",
            blank_after_short_description=True,
            blank_after_long_description=True,
        )
    )

# Generated at 2022-06-13 19:57:38.265819
# Unit test for function parse
def test_parse():
    docstring = Docstring()
    if not docstring:
        return ''
    text=inspect.cleandoc(docstring)
    match=re.search("^:",text,flags=re.M)
    if match:
        descChunk=text[:match.start()]
        metaChunk=text[match.start():]
    else:
        descChunk=text
        metaChunk=''
    return text
    print(text)
    print(descChunk)
    print(metaChunk)
    pass

# if __name__ == '__main__':
#     docstring = """This is short desc
#     This is long desc
#     :param arg1: this is arg1
#     :param arg2: this is arg2
#     :returns: this is return
#     :

# Generated at 2022-06-13 19:57:52.220552
# Unit test for function parse

# Generated at 2022-06-13 19:57:58.292744
# Unit test for function parse
def test_parse():
    import os
    from .common import (
        PARAM_KEYWORDS,
        RAISES_KEYWORDS,
        RETURNS_KEYWORDS,
        YIELDS_KEYWORDS,
        DocstringMeta
    )

    text = inspect.getdoc(parse)
    ds = parse(text)
    assert ds.short_description == "Parse the ReST-style docstring into its components."
    assert ds.blank_after_short_description
    assert ds.blank_after_long_description
    assert ds.long_description == """\
    :returns: parsed docstring"""
    assert len(ds.meta) == 1
    assert ds.meta[0] == DocstringMeta(args=[':returns'], description="parsed docstring")
    # the following two test cases

# Generated at 2022-06-13 19:58:14.344178
# Unit test for function parse
def test_parse():
    text = """\
    Parse the ReST-style docstring into its components.

    :param text: str
    :returns: Docstring
    """
    docstring = parse(text)
    assert docstring.short_description == "Parse the ReST-style docstring into its components."
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False

    args = docstring.meta[0].args
    assert args[0] == 'param'
    assert args[1] == 'text'
    assert args[2] == 'str'

    desc = docstring.meta[0].description
    assert desc == None
    assert docstring.meta[0].arg_name == 'text'
    assert docstring.meta

# Generated at 2022-06-13 19:58:19.036157
# Unit test for function parse
def test_parse():
    """ It tests all the cases for parse function.

    - Test cases with empty docstring.
    - Test cases for parsing description and meta information.
    - Test cases for parsing the different scenarios of meta information.
    - Test cases for testing the docstring which is less than the expected format.
    """
    from .test_common import test_parse_cases, DocstringTestCase

    # Empty docstring test cases

# Generated at 2022-06-13 19:58:28.523940
# Unit test for function parse
def test_parse():
    x = parse('''
    Short description.

    Long description.
    
    	Indented code sample
    
    :param foo: Foo
    :type foo: :class:`int`
    :param bar: Bar
    :type bar: :class:`int`
    :returns: Something
    :rtype: :class:`int`
    :raises: ValueError
    :raises: RuntimeError
    ''')
    assert x.short_description == 'Short description.'
    assert x.long_description == 'Long description.\n\n\tIndented code sample'
    assert x.blank_after_short_description == True
    assert x.blank_after_long_description == True
    assert len(x.meta) == 6

# Generated at 2022-06-13 19:58:45.430684
# Unit test for function parse
def test_parse():
    assert parse("test docstring") == Docstring(
        short_description="test docstring",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )

    assert parse("test docstring\n") == Docstring(
        short_description="test docstring",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )

    assert parse("test docstring\n\n") == Docstring(
        short_description="test docstring",
        blank_after_short_description=False,
        blank_after_long_description=True,
        long_description=None,
        meta=[],
    )


# Generated at 2022-06-13 19:58:52.130742
# Unit test for function parse
def test_parse():
    docstring = parse("""Test parse function.

    :param arg1: the first parameter
    :type arg1: int
    :param arg2: the second parameter
    :type arg2: str
    :return: return value
    :rtype: int
    :raises TypeError:
    :raises ValueError:
    """)

    assert docstring.short_description == "Test parse function."

    assert docstring.long_description == """
    the first parameter
    the second parameter
    return value
    raises ValueError

    raises TypeError
    """

    assert len(docstring.meta) == 4

    assert isinstance(docstring.meta[0], DocstringParam)
    assert docstring.meta[0].arg_name == "arg1"
    assert docstring.meta[0].type_name == "int"


# Generated at 2022-06-13 19:59:03.055346
# Unit test for function parse
def test_parse():
    """Unit test for function parse."""
    doc = """
        Short summary.

        Longer description. Can have multiple paragraphs.
        """
    assert parse(doc) == Docstring(
        short_description="Short summary.",
        blank_after_short_description=True,
        long_description="Longer description. Can have multiple paragraphs.",
        blank_after_long_description=True,
        meta=[],
    )

    doc = """
        Short summary.

        Longer description.

        :param foo: some info
        :param bar: some other info
        :keyword baz: something else
        """

# Generated at 2022-06-13 19:59:09.907905
# Unit test for function parse
def test_parse():
    text = '''
    Parse the ReST-style docstring into its components.

    :returns: parsed docstring
    '''
    test_docstring = parse(text)
    print(test_docstring.short_description)
    print(test_docstring.blank_after_long_description)
    print(test_docstring.blank_after_short_description)
    print(test_docstring.long_description)
    print(test_docstring.meta[0].args)
    print(test_docstring.meta[0].description)


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:59:21.251597
# Unit test for function parse
def test_parse():
    assert parse("") == parse("   ") == parse("""\
    """) is not None
    assert parse("""\
    Test a docstring parser.
    """).short_description == "Test a docstring parser."
    assert parse("""\
    Test a docstring parser.
    """).long_description is None
    assert parse("""\
    Test a docstring parser.
    """).blank_after_short_description is False
    assert parse("""\
    Test a docstring parser.
    """).blank_after_long_description is False

    assert parse("""\
    Test a docstring parser.

    This is a long description.
    """).short_description == "Test a docstring parser."
    assert parse("""\
    Test a docstring parser.

    This is a long description.
    """).long

# Generated at 2022-06-13 19:59:31.806949
# Unit test for function parse
def test_parse():
    f = lambda a, *b, c=1, d=2: 3
    docstring = parse(inspect.getdoc(f))
    assert docstring.short_description == "Test docstring."
    assert docstring.long_description == "Long description."

    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description

    assert len(docstring.meta) == 4

    assert docstring.meta[0].keyword == "param"
    assert docstring.meta[0].type_name == "int"
    assert docstring.meta[0].arg_name == "a"
    assert docstring.meta[0].description == "Test parameter."
    assert docstring.meta[0].default is None
    assert docstring.meta[0].is_optional is False

    assert docstring

# Generated at 2022-06-13 19:59:42.196610
# Unit test for function parse
def test_parse():
    from py2gcode.docstring.regex_format import parse
    input = '''
    The parser for regex-style docstrings.
    
    
    The ReST-style docstring is parsed into the following components.
    
    :param arg: description
    :param type arg: description
    :param type arg: description
    :param type arg? description
    
    
    
    
    
    
    
    
    :returns: returns description
    :returns: returns description
    :yields: yields description
    
    
    
    
    
    
    
    :raises TypeError: description
    :raises: description
    '''

# Generated at 2022-06-13 19:59:54.160871
# Unit test for function parse
def test_parse():
    input = """
    Short summary.

    This is a long description.

    :param a: This is a parameter description
    :type a: integer
    :param b: This is a parameter description that defaults to null
      and is optional.
    :type b: integer
    :param c: This is a parameter description that defaults to 3.
    :type c: integer
    :param d: This is a parameter description.
    :type d: integer
    :param e: This is a parameter description that defaults to null.
      It is optional.
    :type e: integer
    :param f: This is a parameter description.
    :returns: integer
    :raises Exception: An exception
    """

    docstring = parse(input)
    assert isinstance(docstring, Docstring)

# Generated at 2022-06-13 20:00:01.733969
# Unit test for function parse

# Generated at 2022-06-13 20:00:12.550948
# Unit test for function parse
def test_parse():
    docstring = """
    Example docstring for function parse.

    This is the long description.

    :param str a_string: the string to parse.
    :param int an_int: the int to parse.
    :param bool a_bool: the bool to parse.
    :raises ValueError: if there is a parsing error.
    :raises TypeError: if there is a type error.
    :returns: the parsed object.
    """
    doc_parsed = parse(docstring)
    assert doc_parsed.short_description == "Example docstring for function parse."
    assert doc_parsed.blank_after_short_description
    assert doc_parsed.long_description == "This is the long description."
    assert doc_parsed.blank_after_long_description

# Generated at 2022-06-13 20:00:26.604401
# Unit test for function parse
def test_parse():
    assert parse('Docstring with no meta information.').short_description == 'Docstring with no meta information.'

    assert parse('Docstring with\n\n    long description').short_description == 'Docstring with'
    assert parse('Docstring with\n\n    long description').long_description == 'long description'
    assert parse('Docstring with\n\n    long description').blank_after_short_description == True
    assert parse('Docstring with\n\n    long description').blank_after_long_description == False

    assert parse('Docstring with :param foo: meta information.').short_description == 'Docstring with meta information.'
    assert parse('Docstring with :param foo: meta information.').meta[0].description == 'meta information.'

    assert parse('Docstring with :param foo: meta information.').meta[0].arg_name

# Generated at 2022-06-13 20:00:33.933311
# Unit test for function parse
def test_parse():
    docstring = """
    short description
    short description again
    long description
    long description again
    :param x: X
    :param y: Y defaults to 100.
    :returns: None
    :raises Exception: exception
    """
    parsed = parse(docstring)
    assert parsed.short_description == "short description short description again"
    assert parsed.long_description == "long description long description again"
    assert parsed.meta[0] == DocstringParam(['param', 'x', 'X'], '', 'x', 'X', is_optional=None, default=None)
    assert parsed.meta[1] == DocstringParam(['param', 'y', 'Y'], '', 'y', 'Y', is_optional=None, default='100')

# Generated at 2022-06-13 20:00:45.126121
# Unit test for function parse
def test_parse():
    """Test parse()."""
    # Test docstrings with short description only
    assert parse("") == Docstring()
    assert parse("\n") == Docstring()
    assert parse("Sample function.") == Docstring(
        short_description="Sample function.",
    )
    assert parse("Sample function.\n") == Docstring(
        short_description="Sample function.",
    )
    assert parse("Sample function.\n\n") == Docstring(
        short_description="Sample function.",
    )
    assert parse("Sample function.\n\n\n") == Docstring(
        short_description="Sample function.",
    )

    # Test docstrings with short and long descriptions
    assert parse("Short desc.\nLong desc.") == Docstring(
        short_description="Short desc.",
        long_description="Long desc.",
    )

# Generated at 2022-06-13 20:00:51.218813
# Unit test for function parse
def test_parse():
    docstring = parse(
        """
    My function
    """
    )
    assert docstring.short_description == "My function"
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is True
    # assert len(docstring.meta) == 2
    # assert docstring.meta[0].args == ["param", "a", "b"]
    # assert docstring.meta[0].description.startswith("My first argument")
    # assert docstring.meta[0].is_optional is True
    # assert docstring.meta[1].args == ["param", "c"]
    # assert docstring.meta[1].description.startswith("My second argument")
    # assert docstring.meta[1].is_

# Generated at 2022-06-13 20:01:01.248281
# Unit test for function parse
def test_parse():
    docstring = ('Foobar.\n' +
                 '\n' +
                 ':param foo: A number.\n' +
                 ':param bar: A string.\n' +
                 ':return: The result of the operation.')

# Generated at 2022-06-13 20:01:10.409886
# Unit test for function parse
def test_parse():
    
    docstring = '''\
    This is a test docstring for the unit test.

    More than one line.

    :param arg1: the first argument
    :param arg2: the second argument
    :param arg3: the third argument
    :param arg4: the fourth argument
    :returns: a return value
    :raises Exception: if something goes south
    '''

    # confirm parsing config
    ds = parse(docstring)
    
    # compare config to parsed config
    assert ds.short_description == "This is a test docstring for the unit test."
    assert ds.long_description == '''\
    More than one line.
    '''
    assert ds.blank_after_short_description == True
    assert ds.blank_after_long_description == True

    assert d

# Generated at 2022-06-13 20:01:14.316110
# Unit test for function parse
def test_parse():
    docstr = """
    Short description.

    Long description

    :param str filename: name of the file to open

    In case file is missing.
    """
    parsed = parse(docstr)
    assert len(parsed.meta) == 1
    assert parsed.meta[0].description == "name of the file to open\n\nIn case file is missing."



# Generated at 2022-06-13 20:01:24.985875
# Unit test for function parse
def test_parse():
    docstring = """Parses the ReST-style docstring into its components.
    :param foo: optional foo param
    :type foo: str
    :param bar: optional bar param
    :type bar: int
    :param baz: optional baz param
    :param baz_type:
    :type baz_type: int
    :param bam: optional bam param
    :type bam: int
    :param bam_type:
    :param quux: optional quux param
    :type quux: int
    :type quux_type: str
    :returns: parsed docstring
    :rtype: object
    :raises: error parsing
    :raises: error parsing
    """
    result = parse(docstring)
    print(result)
    meta = result.meta
    assert meta

# Generated at 2022-06-13 20:01:34.241378
# Unit test for function parse
def test_parse():
    d = Docstring(
        short_description="This is a short description",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description="This is a long description",
        blank_after_meta=False,
        meta=[
            DocstringMeta(
                args=["KW"],
                description=(
                    "Some parameter description\n"
                    "that spans multiple lines\n"
                    "and may include LaTeX."
                ),
            ),
        ],
    )
    assert parse(d.rst) == d



# Generated at 2022-06-13 20:01:44.946914
# Unit test for function parse
def test_parse():
    params = [
        DocstringParam(
            ["param", "foo:", "int"],
            "The value of foo",
            "foo",
            "int",
            False,
            None,
        ),
        DocstringParam(
            ["param", "bar:", "list"],
            "A list of items",
            "bar",
            "list",
            True,
            None,
        ),
        DocstringParam(
            ["param", "baz:", "bool"],
            "defaults to True.",
            "baz",
            "bool",
            True,
            "True",
        ),
        DocstringParam(
            ["param", "xyzzy"],
            "No explanation needed",
            "xyzzy",
            None,
            None,
            None,
        ),
    ]
