

# Generated at 2022-06-13 19:52:21.730200
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    assert parse("") == Docstring()

    docstr = parse("Short description.")
    assert docstr.short_description == "Short description."
    assert docstr.long_description is None
    assert len(docstr.meta) == 0

    docstr = parse("Short description.\n\nLong description.")
    assert docstr.short_description == "Short description."
    assert docstr.long_description == "Long description."
    assert len(docstr.meta) == 0

    docstr = parse("Short description.\n\nLong description.\na.b.\n\n")
    assert docstr.short_description == "Short description."
    assert docstr.long_description == "Long description.\na.b."
    assert len(docstr.meta) == 0


# Generated at 2022-06-13 19:52:28.439143
# Unit test for function parse

# Generated at 2022-06-13 19:52:38.514862
# Unit test for function parse
def test_parse():
    docstring = '''This is a function.
    
:param arg1: parameter
:type arg1: int
:param arg2: parameter
:type arg2: int
'''
    parsed = parse(docstring)
    print(parsed.short_description)
    print(parsed.long_description)
    print([p.description for p in parsed.meta])


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:52:46.028941
# Unit test for function parse
def test_parse():
    docstring = """One line summary.
    Additional details.

    :param arg1: The first argument.
    :type arg1: str
    :param arg2: The second argument.
    :type arg2: int, optional
    :returns: Description of return value.
    :rtype: int
    """
    d = parse(docstring)
    assert d.short_description == "One line summary."
    assert d.long_description == "Additional details."
    assert d.blank_after_short_description == True
    assert d.blank_after_long_description == False
    assert len(d.meta) == 4
    assert d.meta[0].args == ['param', 'arg1']
    assert d.meta[0].arg_name == "arg1"

# Generated at 2022-06-13 19:52:56.158932
# Unit test for function parse
def test_parse():
    """Test function parse"""
    # Read docstring_example.py
    with open("docstring_example.py", "r") as fd:
        text = fd.read()
    # Split into functions
    text = text.split("\n\n")
    # Print out errors if docstring is not found
    if len(text) < 2:
        raise ValueError("No docstring found")
    # Parse the docstring
    parsed = parse(text[1])
    
    # Check length of parsed strings
    assert(len(parsed.short_description) > 0)
    assert(len(parsed.long_description) > 0)
    
    # Check parsed string
    assert(parsed.short_description == "My library")

# Generated at 2022-06-13 19:53:07.358730
# Unit test for function parse
def test_parse():
    """ Test for parse function """
    pars_docc = parse("""
    Funzione utile per calcolare la differenza di due numeri
        :param x: il primo numero
        :type number: int
        :param y: il secondo numero
        :type number: int
        :return: intero che rappresenta la differenza tra i numeri
        Differenza tra due numeri
        :raises NumberException: se entrambi i numeri sono negativi
    """)
    assert type(pars_docc) is Docstring
    assert pars_docc.blank_after_short_description is True
    assert pars_docc.short_description == "Funzione utile per calcolare la differenza di due numeri"

# Generated at 2022-06-13 19:53:18.115577
# Unit test for function parse
def test_parse():
    text = """
        The quick brown fox jumps over the lazy dog.

        :param int x: The x coordinate.

        :param int y: The y coordinate.
        :param int width: The width of the window.
        :param int height: The height of the window.
        :param int color?: The color of the window. Optional.

        :returns int: The area of the window.
        :raises ValueError: if color is out of range.
        :raises ValueError: if height or width are negative.

        :yields: The build string.
    """
    result = parse(text)
    assert result.short_description == "The quick brown fox jumps over the lazy dog."

# Generated at 2022-06-13 19:53:31.676949
# Unit test for function parse
def test_parse():
    """Unit test function parse."""
    assert not parse("")
    assert parse("A short phrase.").short_description == "A short phrase."

    assert parse("A short phrase.\n\nA longer,\nmore detailed phrase.\n\n") == Docstring(
        short_description="A short phrase.",
        blank_after_short_description=False,
        long_description="A longer,\nmore detailed phrase.",
        blank_after_long_description=True,
        meta=[],
    )


# Generated at 2022-06-13 19:53:39.746702
# Unit test for function parse
def test_parse():
    text = """
        :param s: this is a string
        :param n: this is an int
        :rtype: str
    """
    doc = parse(text)
    assert len(doc.meta) == 3
    assert doc.meta[0].arg_name == "s"
    assert doc.meta[1].arg_name == "n"
    assert doc.meta[2].is_generator == False

# Generated at 2022-06-13 19:53:44.112494
# Unit test for function parse
def test_parse():
    docstring = """
        :param str arg1: This is a first argument.
        :param int arg2: This is a second argument.
    """
    doc = parse(docstring)

    assert len(doc.meta) == 2
    assert doc.long_description is None



# Generated at 2022-06-13 19:54:04.594023
# Unit test for function parse
def test_parse():
    doc = inspect.getdoc(parse)
    expected_doc = parse(doc)
    assert expected_doc == parse(doc)

# Generated at 2022-06-13 19:54:09.157894
# Unit test for function parse
def test_parse():
    code = """
    Test docstring.

    :param a: The `a` parameter
        does this.
    :type a: int
    :param b: The `b` parameter.
    :type b: int
    """
    print(parse(code))

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:54:19.636933
# Unit test for function parse
def test_parse():
    # test short description
    res = parse("short description.")
    assert res.short_description == "short description."

    # test long description
    res = parse("short description. \n\n first long description line. \n second long description line.")
    assert res.short_description == "short description."
    assert res.blank_after_short_description == True
    assert res.blank_after_long_description == True
    assert res.long_description == "first long description line. \n second long description line."

    res = parse("short description. first long description line. \n second long description line.")
    assert res.short_description == "short description."
    assert res.blank_after_short_description == False
    assert res.blank_after_long_description == True

# Generated at 2022-06-13 19:54:27.880685
# Unit test for function parse
def test_parse():
    text = """
    An example docstring.

    :param foo: A foo.
    :type foo: Optional[str]
    :param bar: A bar.
    :type bar: Optional[bool]
    :returns: A baz.
    :rtype: Optional[float]
    """

    doc = parse(text)

    assert doc.short_description.strip() == "An example docstring."
    assert doc.long_description is None
    assert doc.blank_after_short_description is False
    assert doc.blank_after_long_description is False
    assert len(doc.meta) == 3
    assert type(doc.meta[0]) == DocstringParam
    assert doc.meta[0].description == "A foo."
    assert doc.meta[0].arg_name == "foo"
    assert doc.meta

# Generated at 2022-06-13 19:54:39.137321
# Unit test for function parse

# Generated at 2022-06-13 19:54:47.670264
# Unit test for function parse
def test_parse():
    text = '''
        Short description.

        Long description.

        :param str foo: A foo.
        :param str bar: A bar.
        :returns: Returned thing.
    '''
    ret = parse(text)
    assert len(ret.meta) == 3
    assert ret.meta[1].arg_name == 'bar'
    assert ret.meta[2].arg_name is None
    assert ret.meta[2].type_name == 'Returned thing'


# Generated at 2022-06-13 19:55:00.242240
# Unit test for function parse

# Generated at 2022-06-13 19:55:09.218907
# Unit test for function parse
def test_parse():
    docstr = r'''
    :param arg1: Parameter 1.
    :param arg2: Parameter 2. Defaults to 2.

    :param arg3:
        Parameter 3.
        Defaults to 3.

    :raises IndexError: Index is out of range

    Short description.

    Long description.
    '''
    parsed = parse(docstr)
    assert parsed.short_description == "Short description."
    assert parsed.long_description == "Long description."
    assert parsed.blank_after_short_description is True
    assert parsed.blank_after_long_description is True
    assert len(parsed.meta) == 3
    assert parsed.meta[0].description == 'Parameter 1.'
    assert parsed.meta[1].description == 'Parameter 2. Defaults to 2.'

# Generated at 2022-06-13 19:55:18.896262
# Unit test for function parse
def test_parse():
    assert (
        parse("Short description.\n\nLong description.\n")
        == Docstring(
            short_description='Short description.',
            long_description='Long description.',
            blank_after_short_description=True,
            blank_after_long_description=False,
            meta=[],
        )
    )

    for s in [
        'Expected one argument for a :raises: keyword.',
        'Expected one or two arguments for a :param: keyword.',
        'Expected one or no arguments for a :return: keyword.',
        'Expected one or no arguments for a :yields: keyword.',
    ]:
        assert s in repr(parse.__doc__)


# Generated at 2022-06-13 19:55:31.085470
# Unit test for function parse
def test_parse():
    original = """
    Short description.

    Long description. Returns an integer.

    :param foo: Bar.
    :raises ValueError: If `foo` is not valid.
    :raises AttributeError: If `foo` is not valid or previously raised an error.
    :returns: A new integer.
    :rtype: int
    """

    docstring = parse(original)

    assert docstring.short_description == "Short description."
    assert docstring.long_description == "Long description."
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description
    assert len(docstring.meta) == 6
    assert docstring.meta[0].description == "Bar."
    assert docstring.meta[1].description == "If `foo` is not valid."
    assert doc

# Generated at 2022-06-13 19:55:54.066106
# Unit test for function parse
def test_parse():
    def parse_assert(text, short_description=None, long_description=None):
            docstring = parse(text)
            assert docstring.short_description == short_description
            assert docstring.long_description == long_description

    with pytest.raises(ParseError):
        parse_assert(":", "", "")

    with pytest.raises(ParseError):
        parse_assert("hello\n:", "hello", "")

    with pytest.raises(ParseError):
        parse_assert("hello\n:abc\n:abc", "hello", "")

    parse_assert("hello", "hello", None)
    parse_assert("\nhello", "hello", None)
    parse_assert("hello\n", "hello", None)

# Generated at 2022-06-13 19:56:03.771011
# Unit test for function parse
def test_parse():
    passed = True
    result = parse('''
        This is a short description.
        This is a longer description.
        ''')
    if result.short_description != 'This is a short description.':
        passed = False
    if result.long_description != 'This is a longer description.':
        passed = False
    if result.blank_after_short_description != True:
        passed = False
    if result.blank_after_long_description != True:
        passed = False
    if len(result.meta) != 0:
        passed = False

    result = parse('''
        This is a short description. This is a longer description.
        ''')
    if result.short_description != 'This is a short description.':
        passed = False

# Generated at 2022-06-13 19:56:14.519180
# Unit test for function parse
def test_parse():
    assert parse("") is not None
    assert parse("") == Docstring()

    assert parse("Short desc.") is not None
    d = parse("Short desc.")
    assert d.short_description == "Short desc."
    assert d.long_description is None
    assert len(d.meta) == 0

    assert parse("Short desc.\n") is not None
    d = parse("Short desc.\n")
    assert d.short_description == "Short desc."
    assert d.long_description is None
    assert len(d.meta) == 0
    assert d.blank_after_short_description is True
    assert d.blank_after_long_description is True

    assert parse("Short desc.\n\n") is not None
    d = parse("Short desc.\n\n")

# Generated at 2022-06-13 19:56:24.376953
# Unit test for function parse

# Generated at 2022-06-13 19:56:34.294240
# Unit test for function parse

# Generated at 2022-06-13 19:56:46.534404
# Unit test for function parse

# Generated at 2022-06-13 19:57:00.581193
# Unit test for function parse
def test_parse():
    """Test the parser."""

    def test(text: str, expected_dict: T.Dict[str, T.Any]) -> None:
        """Test parsing of a given docstring."""
        docstring = parse(text)
        for attr, value in expected_dict.items():
            assert getattr(docstring, attr) == value

    test(
        text="",
        expected_dict={
            "short_description": None,
            "long_description": None,
            "blank_after_short_description": False,
            "blank_after_long_description": False,
            "meta": [],
        },
    )


# Generated at 2022-06-13 19:57:13.172032
# Unit test for function parse
def test_parse():
    docstring = """
    This is a simple docstring.
    This is the second line.

    :param name: Name for the template.
    :type name: str
    :returns: A string containing everything in the template
        except CHANGEME_* variables.
    :rtype: str
    :raises ValueError: if the template is empty

    This is the long description.
    """

    docstring = parse(docstring)
    docstring.short_description == "This is a simple docstring."
    docstring.long_description == """
    This is the long description."""
    docstring.blank_after_short_description == True
    docstring.blank_after_long_description == False
    docstring.meta[0].key == "param"
    docstring.meta[0].arg_name == "name"

# Generated at 2022-06-13 19:57:24.495696
# Unit test for function parse
def test_parse():
    res = parse("""
    Description of function foo.

    :param arg1: Description of arg1
    :type arg1: str, optional
    :param arg2: Description of arg2
    :param arg3: Description of arg3
    :returns: Description of return
    :rtype: str
    :raises: AttributeError, KeyError
    :raises KeyError: Blah blah
    :raises: KeyError, IndexError
    """)
    print("The res:", res)


if __name__ == "__main__":

    print("__file__:", __file__)
    print("__name__:", __name__)

    test_parse()

# Generated at 2022-06-13 19:57:36.325714
# Unit test for function parse
def test_parse():
    doc = inspect.cleandoc(
        """
    Summary line.

    Extended description.
    Extended description continued.

    :param a: parameter a.
    :param b: parameter b.
    :type b: str
    :param c: parameter c.
    :type c: int, optional
    :param d: parameter d.
    :type d: bool, optional
    :param e: parameter e.
        defaults to 1.
    :return: something
    :rtype: str
    :raises: exception
    """
    )
    parsed = parse(doc)
    assert parsed.short_description == "Summary line."
    assert parsed.long_description == "Extended description.\n" "Extended description continued."
    assert parsed.blank_after_short_description is False
    assert parsed.blank_after_long_

# Generated at 2022-06-13 19:58:03.193501
# Unit test for function parse
def test_parse():
    def f():
        """
        Some short description.

        And some long description.

        :param foo: description of foo
        :type foo: int
        :param bar: description of bar
        :type bar: str
        :param baz: description of baz with line breaks in it.

        On a new line.
        :type baz: float
        """

    docstring = parse(f.__doc__)

    assert docstring.short_description == "Some short description."
    assert docstring.blank_after_short_description == True
    assert docstring.long_description == "And some long description."
    assert docstring.blank_after_long_description == True

    assert docstring.meta[0].arg_name == "foo"
    assert docstring.meta[0].type_name == "int"
    assert doc

# Generated at 2022-06-13 19:58:15.013810
# Unit test for function parse
def test_parse():
    print('=======================')
    print('test_parse')
    print('=======================')
    doc = """
    title
    =====

    short description

    long description
    """

    print(doc)
    r = parse(doc)
    print(r)

    doc = """
    title
    =====

    short description

    :param str arg1:
    :param str arg2:
    """
    print(doc)
    r = parse(doc)
    print(r)

    doc = """
    title
    =====

    short description

    :param str arg1:
    :param int arg2:
    :param str arg3:
    """
    print(doc)
    r = parse(doc)
    print(r)


# Generated at 2022-06-13 19:58:23.865255
# Unit test for function parse
def test_parse():
    def test_function():
        """
        This is a docstring.

        This is a long description.

        :param param: This is a parameter.
        :param int param: This is a parameter.
        :param int param: This is a parameter.
        """
        pass

    docstring = parse(inspect.getdoc(test_function))
    print(docstring)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:58:32.740380
# Unit test for function parse
def test_parse():
    text = """
    Short summary.

    :param arg1: description
    :param arg2: description
    :param arg3: description
    :returns: description
    :raises: description
    :yields: description
    """
    result = parse(text)
    for k, v in result.__dict__.items():
        print(k, ":", v)

# Generated at 2022-06-13 19:58:43.903063
# Unit test for function parse
def test_parse():
    docstring = """\
    Short summary.

    This is the long description.

    :param arg1: this is a first argument
    :type arg1: str
    :param arg2: this is a second argument
    :type arg2: int, optional
    :param arg3: this is a third argument
    :type arg3: bool, optional
    :param arg4: this is a fourth argument, defaults to True.
    :param arg5: this is a fifth argument
    :type arg5: int
    :raises ValueError: on negative input
    :return: docstring returns
    :rtype: str
    """


# Generated at 2022-06-13 19:58:58.147013
# Unit test for function parse
def test_parse():
    from .common import DocstringParam
    from .common import DocstringReturns
    from .common import DocstringRaises
    from .common import DocstringMeta
    from .common import Docstring
    from .common import TYPE_COMMENT_SYMBOLS
    from .rest import parse
    from .rest import PARAM_KEYWORDS
    from .rest import RETURNS_KEYWORDS
    from .rest import RAISES_KEYWORDS
    from .rest import YIELDS_KEYWORDS


# Generated at 2022-06-13 19:59:14.338088
# Unit test for function parse
def test_parse():
    empty = """
    """
    x = parse(empty)
    assert x.short_description is None
    assert x.long_description is None
    assert x.blank_after_short_description is False
    assert x.blank_after_long_description is False

    short = """
    Short description.
    """
    x = parse(short)
    assert x.short_description == "Short description."
    assert x.long_description is None
    assert x.blank_after_short_description is False
    assert x.blank_after_long_description is False

    long = """
    Short description.
    Long description.
    """
    x = parse(long)
    assert x.short_description == "Short description."
    assert x.long_description == "Long description."
    assert x.blank_after_short_description

# Generated at 2022-06-13 19:59:25.710293
# Unit test for function parse
def test_parse():
    docstring = """
    This is an example docstring.

    :param a: This is an argument.
    :param b: This is another argument.  
    """

    # Generate the json object.

# Generated at 2022-06-13 19:59:34.144943
# Unit test for function parse
def test_parse():
    docstring = """This is a docstring.

    This is the long description.

    :param arg1: the first argument
    :type arg1: int
    :param arg2: the second argument
    :type arg2: string, optional
    :param arg3: the third argument
    :type arg3: string, optional
    :returns: description of return value
    :raises AttributeError: description of exception
    :raises TypeError: description of exception
    """

# Generated at 2022-06-13 19:59:43.386808
# Unit test for function parse
def test_parse():
    docstring = '''\
    The foo function does something.

    :param str arg1: The first argument.
    :type arg1: str
    :param str arg2: The second argument.
    :param int arg3: The third argument.
    :param str arg4: The fourth argument. Optional. Defaults to something.
    :returns: tuple of str

    :raises ValueError: For something.
    :raises KeyError: For something.
    :raises TypeError: For something.

    :returns: For something.
    '''

# Generated at 2022-06-13 20:00:00.661257
# Unit test for function parse
def test_parse():
    text = """This is a function.

:param name: The name
:type name: str

:param age: The age
:type age: int

:param sex: The sex
:type sex: str

:returns: This is the return value
:rtype: str

:raises ValueError: if a value is invalid"""
    ret = parse(text)
    assert ret.short_description == "This is a function."
    assert ret.long_description == "The name\nThe age\nThe sex"

    assert ret.meta[0].arg_name == "name"
    assert ret.meta[0].type_name == "str"
    assert ret.meta[1].arg_name == "age"
    assert ret.meta[1].type_name == "int"

# Generated at 2022-06-13 20:00:08.302597
# Unit test for function parse
def test_parse():
    s = "Parse the ReST-style docstring into its components.\n\n:returns: parsed docstring"
    p = parse(s)
    assert p.short_description == "Parse the ReST-style docstring into its components."
    assert not p.blank_after_short_description
    assert not p.long_description
    assert not p.blank_after_long_description
    assert len(p.meta) == 1
    assert p.meta[0].args == ['returns']
    assert p.meta[0].description == 'parsed docstring'

    s = "Hello\n:test: blabla"
    p = parse(s)
    assert p.short_description == "Hello"
    assert not p.blank_after_short_description
    assert not p.long_description

# Generated at 2022-06-13 20:00:15.290722
# Unit test for function parse
def test_parse():
    doc = inspect.cleandoc("""Parse the ReST-style docstring into its components."""
    """

    :arg:
    :param foo:
    :type foo:
    :param bar:
    :type bar:
    :returns: parsed docstring
    :rtype: dict
    :raises TypeError: if an invalid type is given
    """)
    parse(doc)

# Generated at 2022-06-13 20:00:24.688501
# Unit test for function parse
def test_parse():
    doc_string = """Sum values of the ``'A'`` column from DataFrame.

:param df: Input DataFrame.
:type df: pandas.DataFrame
:param a: The column to select.
:type a: str, optional
:param b: The ``b`` parameter.
:type b: int, optional

:raises TypeError: When ``a`` is not a ``str``.
:returns: The sum of values.
:rtype: int
"""

# Generated at 2022-06-13 20:00:34.722483
# Unit test for function parse
def test_parse():
    code = """
    """
    docstring = parse(code)
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.meta == []

    code = """
        """
    docstring = parse(code)
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.meta == []

    code = """Simple function.
    """
    docstring = parse(code)
    assert docstring.short_description == "Simple function"
    assert docstring.long_description is None
    assert docstring.meta == []

    code = """Simple function."""
    docstring = parse(code)
    assert docstring.short_description == "Simple function."
    assert docstring.long_description is None
    assert docstring.meta

# Generated at 2022-06-13 20:00:45.737048
# Unit test for function parse
def test_parse():
    func_with_docstring = parse(inspect.getdoc(parse))
    assert func_with_docstring.short_description == "Parse the ReST-style docstring into its components."
    assert (
        func_with_docstring.long_description == ":returns: parsed docstring"
    )
    assert func_with_docstring.blank_after_short_description == True
    assert func_with_docstring.blank_after_long_description == False

    func_without_docstring = parse(inspect.getdoc(test_parse))
    assert func_without_docstring.short_description is None
    assert func_without_docstring.long_description is None
    assert func_without_docstring.blank_after_short_description is False
    assert func_without_docstring.blank_after_long_

# Generated at 2022-06-13 20:00:56.161584
# Unit test for function parse
def test_parse():
    docstring = """Test docstring for parse

Parameters
----------
a : int
    First parameter
b : str
    Second parameter

Returns
-------
int
    Sum of a and b

Raises
-------
TypeError
    If a or b is not a number
"""
    docstring_without_params = """Test docstring for parse

Returns
-------
int
    Sum of a and b

Raises
-------
TypeError
    If a or b is not a number
"""
    docstring_with_meta = """Test docstring for parse

:param int a: First parameter
:param str b: Second parameter
:returns int: Sum of a and b
:raises TypeError: If a or b is not a number
"""

# Generated at 2022-06-13 20:01:07.016404
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()
    assert parse("   ") == Docstring()
    assert parse("\n    \n") == Docstring()

    assert parse(" a\n b\n") == Docstring(
        short_description=None,
        long_description="a\nb",
        blank_after_short_description=True,
        blank_after_long_description=True,
        meta=[],
    )

    assert parse(" a\n b\n:") == Docstring(
        short_description=None,
        long_description="a\nb",
        blank_after_short_description=True,
        blank_after_long_description=True,
        meta=[],
    )


# Generated at 2022-06-13 20:01:15.780757
# Unit test for function parse
def test_parse():
    from .numpy import parse
    doc_str = """This is a docstring.
    
    :param a: this is A
    :param b: this is B
    :returns: the sum of A and B
    :raises: None
    """
    d = parse(doc_str)
    assert d.short_description == "This is a docstring."
    assert d.long_description == "the sum of A and B"
    assert d.blank_after_short_description == True
    assert d.blank_after_long_description == True
    assert len(d.meta) == 3

    assert d.meta[0].keyword == "param"
    assert d.meta[0].args[0] == "a"
    assert d.meta[0].args[1] == "b"
    assert d.meta

# Generated at 2022-06-13 20:01:25.948085
# Unit test for function parse
def test_parse():
    docstring = inspect.cleandoc('''
        Function that does something.

        :param in1: first input
        :type in1: int | float

        :param in2: second input. It is an integer
        :type in2: int

        :param in3: third input. Defaults to [0].
        :type in3: list

        :param in4: fourth input. Defaults to None.
        :type in4: int?

        :param in5: fifth input.
        :type in5: int | float?

        :returns: int if in1 is an int, float if in1 is a float.
        :rtype: int | float

        :raises TypeError: if something is wrong
        ''')

    doc = parse(docstring)


# Generated at 2022-06-13 20:01:46.795116
# Unit test for function parse