

# Generated at 2022-06-13 19:52:21.709382
# Unit test for function parse

# Generated at 2022-06-13 19:52:28.428778
# Unit test for function parse
def test_parse():
    from .common import Docstring
    from subprocess import check_output
    # TODO: more automated testing

# Generated at 2022-06-13 19:52:43.249557
# Unit test for function parse
def test_parse():
    docstr = """\
    This is a description.
    This is a description.

    :param arg1: Description of arg1. Defaults to None.
    :param type arg2: Description of arg2.
    :param arg3: Description of arg3.
    :param arg4: Description of arg4.
    :type arg5: str
    :type arg6: str
    :type arg7: str

    :returns: Description.
    :rtype: str
    """
    parsed = parse(docstr)

    assert parsed.short_description == "This is a description."
    assert parsed.long_description == "This is a description."

# Generated at 2022-06-13 19:52:45.867859
# Unit test for function parse
def test_parse():
    text = """
Sample function.

:param x: First parameter.
:param y: Second parameter.
:returns: Does nothing.
"""
    print(parse(text))

# Generated at 2022-06-13 19:52:56.089702
# Unit test for function parse
def test_parse():
    text = inspect.cleandoc(
        """\
    This function computes the value of x squared.

    If a negative value is given, an exception is raised.

    A more elaborate description of the function.

    :param x: The value to square.
    :type x: float
    :returns: x**2
    :rtype: float
    :raises ValueError: if x is negative
    """
    )
    docstring = parse(text)
    assert docstring.short_description == "This function computes the value of x squared."
    assert docstring.long_description == "A more elaborate description of the function."
    assert docstring.meta[0].arg_name == "x"
    assert docstring.meta[0].type_name == "float"

# Generated at 2022-06-13 19:53:07.277800
# Unit test for function parse
def test_parse():

    text = """\
    The first line.

    The second line.

    :param foo: param desc

    Long desc

    :type foo: int

    :raises Exception: raises desc

    """

    parsed = parse(text)

    assert parsed.short_description == "The first line."
    assert parsed.long_description == "The second line.\n\nLong desc"
    assert parsed.blank_after_short_description
    assert parsed.blank_after_long_description

    assert parsed.meta[0].args == ["param", "foo"]
    assert parsed.meta[0].description == "param desc"
    assert parsed.meta[1].args == ["type", "foo"]
    assert parsed.meta[1].description == "int"
    assert parsed.meta[2].args == ["raises", "Exception"]

# Generated at 2022-06-13 19:53:18.078835
# Unit test for function parse
def test_parse():
    docstring = """A short summary.

A long description.

A paragraph in long description.

:param int arg1: A short description of arg1.
:param int arg2: A short description of arg2.
           This is a continuation of the previous line.
:param int? arg3: A short description of arg3.
:param int arg4 default: A short description of arg4.
:param int arg5 defaults to 3: A short description of arg5.
:return: A short description of return value.
:return:? int: A short description of return value.
:yield int: A short description of return value.
:raises TypeError: A short description of return value.
:raises ValueError: A short description of return value.
    """

# Generated at 2022-06-13 19:53:31.234665
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()
    assert parse("docstring.") == Docstring(
        short_description="docstring.",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
    )
    assert parse("docstring.\n") == Docstring(
        short_description="docstring.",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
    )
    assert parse("docstring.\n\n") == Docstring(
        short_description="docstring.",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=True,
    )

# Generated at 2022-06-13 19:53:45.237298
# Unit test for function parse
def test_parse():
    # No meta example
    doc = parse("This is a function.")
    assert doc.short_description == "This is a function."
    assert doc.long_description is None
    assert not doc.blank_after_short_description
    assert not doc.blank_after_long_description
    assert doc.meta == []

    # No meta example (type annotation)
    doc = parse("This is a function.\n\n:return: None")
    assert doc.short_description == "This is a function."
    assert doc.long_description == ""
    assert not doc.blank_after_short_description
    assert not doc.blank_after_long_description
    assert doc.meta == [DocstringReturns(["return"], "None", None, False)]

    # Meta example

# Generated at 2022-06-13 19:53:55.910434
# Unit test for function parse
def test_parse():
    from .testing import assert_docstring_equal

    # TODO: test other keyword types.


# Generated at 2022-06-13 19:54:12.513020
# Unit test for function parse
def test_parse():
    text = """
    Short description.

    Longer description. With a paragraph.

    :param int param_1: Param 1 description.

    :param int param_2:

    Param 2 description. With another paragraph.
    """
    docstring = parse(text)
    assert docstring.short_description == 'Short description.'
    assert docstring.long_description == 'Longer description.  With a paragraph.'
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == True
    assert len(docstring.meta) == 2

    param_1 = docstring.meta[0]
    assert isinstance(param_1, DocstringParam)
    assert param_1.arg_name == 'param_1'
    assert param_1.type_name == 'int'

# Generated at 2022-06-13 19:54:21.752175
# Unit test for function parse
def test_parse():
    text = """\
    """
    doc = parse(text)
    assert doc.short_description == None
    assert doc.long_description == None
    assert doc.meta == []
    assert doc.blank_after_short_description == False
    assert doc.blank_after_long_description == False
    assert not hasattr(doc, 'name')
    assert not hasattr(doc, 'args')

    text = """\
    """
    doc = parse(text)
    assert doc.short_description == None
    assert doc.long_description == None
    assert doc.meta == []
    assert doc.blank_after_short_description == False
    assert doc.blank_after_long_description == False

    text = """\
    Short description.
    Long description.
    """
    doc = parse(text)

# Generated at 2022-06-13 19:54:27.708654
# Unit test for function parse
def test_parse():
    if __name__ == "__main__":
        print(parse(
            """Parse the ReST-style docstring into its components.

            :param foo: This is foo.
            :param bar: This is bar. And this is the second line.
            :type bar: str
            :returns: parsed docstring
            :rtype: :class:`aiida_verdi.utils.docstring_parser.Docstring`
            :raises ValueError: If the docstring is bad
            """
        ))


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:54:36.818641
# Unit test for function parse
def test_parse():
    doctype = parse('''
    Tests the function parse by checking the format of the docstring
    meta.

    :param str A: Description
    :param str B: Description
    :param str C: Description
    :returns: Description
    :rtype: str
    ''')

    assert doctype.short_description == "Tests the function parse by checking the format of the docstring"
    assert doctype.long_description == "meta."
    assert doctype.meta[1] == DocstringMeta(args=['param', 'str', 'C'], description="Description")

# Generated at 2022-06-13 19:54:42.671489
# Unit test for function parse

# Generated at 2022-06-13 19:54:56.305515
# Unit test for function parse

# Generated at 2022-06-13 19:55:01.129361
# Unit test for function parse
def test_parse():
    text = """
    Args:
        arg1 (Type1): Description
            with multiple lines.
        arg2 (Type2, optional): Description
        arg3 (Type3, optional): Description, defaults to 'default'
            with multiple lines
    """
    a = parse(text)
    assert str(a) == text

# Generated at 2022-06-13 19:55:09.772213
# Unit test for function parse
def test_parse():
    from .common import Docstring

    input_docstring = """Simple example docstring.
    """
    expected_docstring = Docstring(
        short_description="Simple example docstring.",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )
    assert parse(input_docstring) == expected_docstring

    input_docstring = """Simple example docstring.

    Now with multiple lines
    """
    expected_docstring = Docstring(
        short_description="Simple example docstring.",
        long_description="Now with multiple lines",
        blank_after_short_description=True,
        blank_after_long_description=True,
        meta=[],
    )
    assert parse(input_docstring) == expected_doc

# Generated at 2022-06-13 19:55:19.404562
# Unit test for function parse
def test_parse():
    docstring = parse(inspect.cleandoc('''This is the summary line.
    This is the second line.
    :param foo: this is a param named foo
    :type foo: int
    :param bar:
    :type bar: str
    :returns: str
    :raises ValueError:
    '''))
    assert docstring.short_description == "This is the summary line."
    assert docstring.blank_after_short_description == True
    assert docstring.long_description == "This is the second line."
    assert docstring.blank_after_long_description == True
    assert docstring.meta[0].key == 'param'
    assert len(docstring.meta) == 2
    assert docstring.meta[0].arg_name == 'foo'

# Generated at 2022-06-13 19:55:27.193766
# Unit test for function parse
def test_parse():
    text = """
    Short description.

    Longer description.

    :arg arg1: The arg1
    :arg arg2: The arg2
    :type arg2: int
    :arg arg3: The arg3
    :type arg3: object
    :arg arg4: The arg4
    :type arg4: object
    :raises ValueError: when done wrong
    """
    print(parse(text))


# Local Variables:
# compile-command: "python ../../parse.py"
# End:

# Generated at 2022-06-13 19:55:53.085088
# Unit test for function parse
def test_parse():
    func_text = """
    A function

    More function text.

    :param str arg1: Argument 1.
    :param arg2: Argument 2.
    :param arg3=5: Argument 3.
    :param arg4?: Argument 4.
    :return: Argument 5.
    :rtype: str
    """
    result = parse(func_text)
    assert result.short_description == 'A function'
    assert result.blank_after_short_description == False
    assert result.blank_after_long_description == True
    assert result.long_description == 'More function text.'
    assert result.meta[0].args == ['param', 'str', 'arg1']
    assert result.meta[0].description == 'Argument 1.'
    assert result.meta[0].arg_name == 'arg1'

# Generated at 2022-06-13 19:56:02.970853
# Unit test for function parse
def test_parse():
    assert parse('') == Docstring()
    assert parse('This is a docstring.') == Docstring(
        short_description='This is a docstring.',
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )
    assert parse('\nThis is a docstring.') == Docstring(
        short_description='This is a docstring.',
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )

# Generated at 2022-06-13 19:56:16.670578
# Unit test for function parse
def test_parse():
    from .testing_utilities import print_diff
    from .testing_utilities import parse_test_lists

    test_cases = parse_test_lists("tests/data/rest_parse_tests.txt")
    
    for test in test_cases:
        print('Description:', test['description'])
        print('Input:', repr(test['input']))
        print('Expected output:', repr(test['expected_output']))
        # print('Expected output:', test['expected_output'])

        docstring = parse(test['input'])

        print('Actual output:', docstring)
        # print('Actual output:', repr(docstring))
        print()

        if docstring != test['expected_output']:
            print_diff(test['expected_output'], docstring)


# Generated at 2022-06-13 19:56:25.842629
# Unit test for function parse
def test_parse():
    # test for docstring with short description
    short_description = "This is short description"
    docstring = Docstring(
        short_description=short_description,
        long_description=None,
        meta=None,
    )
    assert parse(short_description) == docstring

    # test for docstring with short description and long description
    long_description = (
        "This is long description. This is long description."
        "This is long description. This is long description."
    )
    docstring = Docstring(
        short_description=short_description,
        long_description=long_description,
        meta=None,
    )
    docstring_with_empty_line = "{}\n\n{}".format(short_description, long_description)

# Generated at 2022-06-13 19:56:32.386021
# Unit test for function parse
def test_parse():
    """Test function parse"""
    ds = inspect.getdoc(parse)
    result = parse(ds)
    assert result['short_description'] == 'Parse the ReST-style docstring into its components.'
    assert result['meta'][0]['description'] == ':returns: parsed docstring'
    assert result['meta'][0]['type_name'] == 'Docstring'

# unit test for function _build_meta

# Generated at 2022-06-13 19:56:44.778064
# Unit test for function parse
def test_parse(): 
    assert parse('')==Docstring()
    assert parse('A short desc\n\nA long desc')==Docstring(short_description='A short desc',
    long_description='A long desc', blank_after_short_description=True,
    blank_after_long_description=False)
    assert parse(':return: a str\nthe returned value')==Docstring(short_description='the returned value',
long_description=None, blank_after_short_description=False, blank_after_long_description=False,
meta=[DocstringReturns(args=['return', 'str'], description='a str', type_name='str', is_generator=False)])

# Generated at 2022-06-13 19:56:52.877417
# Unit test for function parse
def test_parse():
    # This function was automatically generated. Please do not edit.
    # Generated Fri Nov 29 17:01:51 UTC 2019
    import json
    from . example_code import module_with_docstring

    text = module_with_docstring.__doc__


# Generated at 2022-06-13 19:57:06.624529
# Unit test for function parse
def test_parse():
    S = "Return the square of x.\n\n:param x: the number to be square.\n:type x: int.\n\n:param y: the number to be square.\n:type y: int.\n:return: square of x."

    assert parse(S).params is None
    assert parse(S).returns is None
    assert parse(S).raises is None

    assert parse(S).short_description == 'Return the square of x.'
    assert parse(S).blank_after_short_description == True
    assert parse(S).blank_after_long_description == True
    assert parse(S).long_description == ''

    assert len(parse(S).meta) == 3

    assert parse(S).meta[0].arg_name == 'x'

# Generated at 2022-06-13 19:57:16.930978
# Unit test for function parse
def test_parse():

    text = '''
        Short description.

        Long description.

        :param p: Parameter description.
        :returns: Returns description.
        :raises e: Raises description.
    '''

    docstring = parse(text)

    assert docstring.short_description == 'Short description.'
    assert docstring.long_description == 'Long description.'
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == True
    assert len(docstring.meta) == 3

    param = docstring.meta[0]
    assert isinstance(param, DocstringParam)
    assert param.args == ['param', 'p']
    assert param.description == 'Parameter description.'
    assert param.arg_name == 'p'
    assert param.type_name == None
   

# Generated at 2022-06-13 19:57:28.651973
# Unit test for function parse
def test_parse():
    docstring = """\
        Series of numbers.

        :param x: The argument of the sine function.
        :type x: int, float, array_like
        :return: Series of numbers.
        :rtype: numpy.ndarray

        :Example:

        >>> print(sine(1))
        >>> print(sine(numpy.pi))
    """
    result = parse(docstring)

# Generated at 2022-06-13 19:57:53.480210
# Unit test for function parse
def test_parse():
    docstring = parse("""This is our docstring.

    :param name: Name of the person
    :type name: str
    :param age: Age of the person
    :type age: int?
    :param colors: Colors of the person
    :type colors: list[str]
    :param defaults to "red": Color of the person
    :returns: Description of what is returned
    :raises ValueError: If 'age' < 0
    :raises TypeError: If 'age' is not an int
    :raises TypeError: If 'colors' is not a list or tuple
    :yields: Colors of the person
    """)
    assert docstring.short_description == "This is our docstring."
    assert docstring.long_description.startswith("Name of the person")
    assert docstring.long

# Generated at 2022-06-13 19:58:05.343130
# Unit test for function parse
def test_parse():
    docstring = parse("""
        This is the title.

        This is the long description.

        :param x: This is the first positional argument.
        :type x: int
        :param y: This is the second positional argument.
        :param z: This is a keyword-only argument.
        :raises RuntimeError: if things go wrong

        :returns: This is the return value.
        :rtype: int
    """)

    assert docstring.short_description == "This is the title."
    assert docstring.long_description == "This is the long description."
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is True

    meta = docstring.meta
    assert len(meta) == 4

    assert meta[0].arg_name == "x"


# Generated at 2022-06-13 19:58:16.863112
# Unit test for function parse

# Generated at 2022-06-13 19:58:27.208442
# Unit test for function parse
def test_parse():
    # test1: a simple docstring
    # test2: a simple docstring with a parameter
    # test3: a complex docstring with parameters and returns
    # test4: a complex docstring with parameters, raises, and yields
    # test5: a docstring with invalid keyword
    test1 = '''\
    This is a short description.

    This is a long description.

    :param arg1: a test parameter
    :param arg2: a test parameter
    :returns: nothing of importance
    :raises KeyError: when a key error is encountered
    '''
    test2 = '''\
    This is a short description.

    This is a long description.

    :param arg1: a test parameter.
    :returns: nothing of importance
    :raises KeyError: when a key error is encountered
    '''


# Generated at 2022-06-13 19:58:37.774753
# Unit test for function parse
def test_parse():
    assert parse("This is a short description.") == Docstring(
        short_description="This is a short description.",
    )
    assert parse("This is a short description.\n\nThis is a long description.") == Docstring(
        short_description="This is a short description.",
        long_description="This is a long description.",
    )
    assert parse("This is a short description.\nThis is a long description.") == Docstring(
        short_description="This is a short description.",
        blank_after_short_description=False,
        long_description="This is a long description.",
    )

# Generated at 2022-06-13 19:58:41.495416
# Unit test for function parse
def test_parse():
    t = """
    This is a short description.

    This is a long description.

    :param type_name? arg_name: description.

    :rtype:
    :returns:
    """
    print(parse(t))

# Generated at 2022-06-13 19:58:57.411094
# Unit test for function parse
def test_parse():
    rslt = parse(
        """Docstring of a class.
        :param int anumber: An integer.
        :type anumber: int
        :param bool logical: True if it is the logical choice. (default: False)
        :raises ValueError: If it is not the logical choice.
        :return: The same boolean.
        :rtype: bool
        """
    )
    assert rslt.short_description == "Docstring of a class."
    assert rslt.blank_after_short_description is False
    assert rslt.blank_after_long_description is False
    assert rslt.long_description is None
    assert rslt.meta[0].args == ['param', 'int', 'anumber']
    assert rslt.meta[0].description == 'An integer.'
    assert rslt.meta[0].arg

# Generated at 2022-06-13 19:59:13.554938
# Unit test for function parse
def test_parse():
    assert parse("This is a short description.") == Docstring(
        short_description="This is a short description.",
        blank_after_short_description=True,
        meta=[],
    )
    assert parse("This is a short description.\n") == Docstring(
        short_description="This is a short description.",
        blank_after_short_description=True,
        meta=[],
    )
    assert parse("This is a short description.\n\n") == Docstring(
        short_description="This is a short description.",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[],
    )

# Generated at 2022-06-13 19:59:24.353289
# Unit test for function parse
def test_parse():
    s = """This is the short description.

This is the long description. It can span
multiple lines.

:param int x: The x coordinate
:param y: The y coordinate
:returns: The distance between the two points.
:raises ValueError: If the inputs are invalid.
    """
    d = parse(s)
    assert d.short_description == 'This is the short description.'
    assert d.long_description == 'This is the long description. It can span\nmultiple lines.'
    assert d.meta[0].arg_name == 'x'
    assert d.meta[0].type_name == 'int'
    assert d.meta[1].arg_name == 'y'
    assert d.meta[1].type_name == None
    assert d.meta[2].type_name == None
    assert d

# Generated at 2022-06-13 19:59:38.534124
# Unit test for function parse
def test_parse():
    # no docstring
    docstring = parse("")
    assert docstring.short_description == None
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []

    # short description only
    docstring = parse("short description")
    assert docstring.short_description == "short description"
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []

    # short description and long description in separate paragraphs
    docstring = parse("short description\n\nwith a long description")
    assert docstring.short_description == "short description"
   

# Generated at 2022-06-13 20:00:01.152115
# Unit test for function parse
def test_parse():
    def foo(a: str, b: int = 3) -> T.Tuple[str, int]:
        """One line description.

        :param a: blah blah
                blah
        :type a: int
        :param b: defaults to 3.
        :type b: int
        :raises OSError: if the foobar failed
        :returns: x and y
        :rtype: Tuple[int, int]
        """
        pass


# Generated at 2022-06-13 20:00:11.075130
# Unit test for function parse
def test_parse():
    docstring = """
    This is a short description.

    This is a long description.

    :param arg_1: argument 1
    :param arg_2: argument 2
    :param arg_3: argument 3
    :param arg_4: argument 4
    """
    result = parse(docstring)
    assert result.short_description == "This is a short description."

    assert result.long_description == "This is a long description."

    assert result.meta[0].arg_name == "arg_1"
    assert result.meta[0].type_name == None
    assert result.meta[0].is_optional == None
    assert result.meta[0].default == None

    assert result.meta[1].arg_name == "arg_2"
    assert result.meta[1].type_name == None
    assert result

# Generated at 2022-06-13 20:00:22.400573
# Unit test for function parse

# Generated at 2022-06-13 20:00:30.156056
# Unit test for function parse
def test_parse():
    doc = inspect.cleandoc('''
        The first line is a short description.

        The rest of the docstring is a long description.
        It can be several lines long.

        :param x: annotated parameter
        :type x: int

        :returns: annotated return value
        :rtype: int
        ''')

# Generated at 2022-06-13 20:00:36.358365
# Unit test for function parse
def test_parse():
    docstring = """Single line docstring."""
    assert parse(docstring) == Docstring(short_description="Single line docstring.")

    docstring = """First line.
    Second line.
    """
    assert parse(docstring) == \
        Docstring(
            short_description="First line.",
            blank_after_short_description=False,
            blank_after_long_description=False,
            long_description="Second line.",
        )

    docstring = """First line.

    Second line.
    """
    assert parse(docstring) == \
        Docstring(
            short_description="First line.",
            blank_after_short_description=True,
            blank_after_long_description=False,
            long_description="Second line.",
        )


# Generated at 2022-06-13 20:00:36.911882
# Unit test for function parse
def test_parse():
    pass

# Generated at 2022-06-13 20:00:46.808249
# Unit test for function parse
def test_parse():
    assert str(parse("This is a brief description")) == \
        "Docstring(short_description='This is a brief description', " \
        "long_description=None, blank_after_short_description=True, " \
        "blank_after_long_description=False, meta=[])"
    assert str(parse("This is a brief description.\nThis is a long description.")) == \
        "Docstring(short_description='This is a brief description.', " \
        "long_description='This is a long description.', " \
        "blank_after_short_description=False, blank_after_long_description=False, " \
        "meta=[])"

# Generated at 2022-06-13 20:00:51.723085
# Unit test for function parse
def test_parse():
    docstring = inspect.getdoc(parse)
    parsed = parse(docstring)
    assert parsed.short_description == "Parse the ReST-style docstring into its components."
    assert parsed.long_description is not None
    assert parsed.long_description.startswith('\n    :param text: Docstring text to be parsed\n    :type')

# Generated at 2022-06-13 20:00:56.649363
# Unit test for function parse
def test_parse():
    doc = '''\
    :param a: this is a
    :param b: this is b
    :yields c: this is c
    :returns d: this is d
    :raises e: this is e
    :raises f: this is f

    '''
    docstring = parse(doc)
    print(docstring)

# Generated at 2022-06-13 20:01:04.714615
# Unit test for function parse
def test_parse():
    docstr = \
    """This is a summary.
    
    Arguments
    ---------
    count: int
        I am a counter.
    gen_count: int?
        How many to generate. Defaults to 5
    """

    doc = parse(docstr)
    assert doc.short_description == "This is a summary."
    assert doc.blank_after_short_description
    assert doc.long_description == "Arguments"
    assert doc.blank_after_long_description
    assert len(doc.meta) == 2
    assert doc.meta[0].arg_name == "count"
    assert doc.meta[0].type_name == "int"
    assert doc.meta[0].is_optional is False
    assert doc.meta[1].arg_name == "gen_count"

# Generated at 2022-06-13 20:01:20.486166
# Unit test for function parse
def test_parse():
    docstring = parse(
        """
    Return a tuple of the new and old values for the variable.

    Raises:
        ValueError: if the variable is not defined.
    """
    )

    print(docstring)

# Generated at 2022-06-13 20:01:28.644480
# Unit test for function parse
def test_parse():
    docstring = "single line docstring"
    d = parse(docstring)
    assert(d.short_description == docstring)

    docstring = "first line\nsecond line"
    d = parse(docstring)
    assert(d.short_description == "first line")
    assert(d.long_description == "second line")

    docstring = """first line
        second line"""
    d = parse(docstring)
    assert(d.short_description == "first line")
    assert(d.long_description == "second line")

    docstring = """first line
        second line

    """
    d = parse(docstring)
    assert(d.short_description == "first line")
    assert(d.long_description == "second line")
    assert(d.blank_after_short_description)


# Generated at 2022-06-13 20:01:40.254378
# Unit test for function parse
def test_parse():
    import pytest
    text = """Simple
    :param a: first param
    :type a: int
    :param b: second param
    :type b: str
    :param c: third param
        It's a multiline comment.
    :type c: float
    :param d: fourth param with default value.
    :type d: bool, defaults to True.
    :raises ValueError: if `a` is not positive.
    """
    parsed = parse(text)
    # Test short description
    assert parsed.short_description == "Simple"
    # Test long description
    assert parsed.long_description is None
    # Test blank lines after short desciption and long description
    assert parsed.blank_after_short_description is False
    assert parsed.blank_after_long_description is True
    # Test metas


# Generated at 2022-06-13 20:01:50.522504
# Unit test for function parse
def test_parse():
    text = """
    This is a short description.

    And this is a longer
    description.

    :param arg1: desc1
    :param arg2: desc2
    :param arg3: desc3
    :returns: desc4
    :raises ValueError: desc5
    :yields: desc6
    :param arg4: desc7
    :param int arg5: desc8
    """
    parsed = parse(text)

    assert parsed.short_description == "This is a short description."
    assert parsed.long_description == """And this is a longer
description."""
    assert parsed.blank_after_short_description is True
    assert parsed.blank_after_long_description is True

    assert len(parsed.meta) == 7