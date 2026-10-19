

# Generated at 2022-06-13 19:52:21.580534
# Unit test for function parse
def test_parse():
    d = """Function parse

Parse a docstring into its components.

    Arguments:
        text (str): docstring to parse.

    Returns:
        (Docstring): parsed docstring.
"""
    p = parse(d)
    assert p.short_description == "Function parse"
    assert p.long_description == "Parse a docstring into its components."
    assert isinstance(p.meta[0], DocstringParam)
    assert p.meta[0].arg_name == "text"
    assert p.meta[0].type_name == "str"
    assert p.meta[0].is_optional is None
    assert p.meta[0].default is None
    assert isinstance(p.meta[1], DocstringReturns)
    assert p.meta[1].type_name == "Docstring"

#

# Generated at 2022-06-13 19:52:28.382042
# Unit test for function parse
def test_parse():
    """Test function parse"""

    from .test_common import test_docstring, test_meta
    from .test_common import test_param, test_param_typed
    from .test_common import test_raises
    from .test_common import test_returns
    from .test_common import test_returns_typed
    from functools import wraps


    def run_and_assert_parse(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            doc = func(self, *args, **kwargs)
            parsed = parse(doc)
            func(self, parsed)

        return wrapper


    class ParserTest:
        def parse(self, doc):
            return parse(doc)


# Generated at 2022-06-13 19:52:40.359767
# Unit test for function parse
def test_parse():
    res = parse(
        """Test parse
        :param arg1: something
        :param arg2: something else
        """
    )
    assert res.short_description == "Test parse"
    assert res.long_description is None
    assert len(res.meta) == 2
    assert type(res.meta[0]) is DocstringParam
    assert res.meta[0].arg_name == "arg1"
    assert type(res.meta[1]) is DocstringParam
    assert res.meta[1].arg_name == "arg2"

# Generated at 2022-06-13 19:52:46.446919
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    text="""
        Split a given string and return the result as list. The "maxsplit"
        arguments describes the maximum number of splits.

        :param str s: string to split
        :param int maxsplit: maximum number of splits
        """
    parse_result=parse(text)
    assert parse_result.short_description=="Split a given string and return the result as list. The 'maxsplit' arguments describes the maximum number of splits."
    assert parse_result.blank_after_short_description==True
    assert parse_result.blank_after_long_description==False
    assert parse_result.long_description is None
    assert len(parse_result.meta)==2
    assert isinstance(parse_result.meta[0],DocstringParam)
    assert parse_result.meta[0].arg

# Generated at 2022-06-13 19:52:53.452573
# Unit test for function parse
def test_parse():
    text = """\
    This is my function.

    It does important things.

    :param x: This is x
    :param y: This is y
    :param z: This is z

    :returns: int -- The return value.
    """
    pack = parse(text)
    print(pack)
    print(pack.short_description)
    print(pack.long_description)
    print(len(pack.meta))


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:53:05.772814
# Unit test for function parse
def test_parse():
    doc = """Return inner most braces

    there are two type of braces: round and square

    :param [s]: string to parse
    :returns: string between inner most braces
    :raises InvalidBraces: when input string doesn't contain a pair of braces
    """
    docstring = parse(doc)
    assert docstring.short_description == 'Return inner most braces'
    assert docstring.long_description == 'there are two type of braces: round and square'
    assert len(docstring.meta) == 3
    assert docstring.meta[0].description == 'string to parse'
    assert docstring.meta[1].description == 'string between inner most braces'
    assert docstring.meta[2].description == "when input string doesn't contain a pair of braces"



# Generated at 2022-06-13 19:53:16.214679
# Unit test for function parse
def test_parse():
    """Unit tests for function parse."""

    assert parse("hello") == Docstring(
        short_description="hello",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )

    assert parse(
        inspect.cleandoc(
            """
        hello

        long desc
        """
        )
    ) == Docstring(
        short_description="hello",
        long_description="long desc",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[],
    )


# Generated at 2022-06-13 19:53:30.926704
# Unit test for function parse

# Generated at 2022-06-13 19:53:44.920011
# Unit test for function parse
def test_parse():
    """Unit test for function parse."""
    # Empty docstring.
    assert parse("") == Docstring()
    # No meta information.
    x = Docstring()
    x.short_description = "A simple docstring."
    x.long_description = "Short description.\n\nLong description."
    x.blank_after_short_description = True
    x.blank_after_long_description = True
    assert parse(
        "A simple docstring.\n\nShort description.\n\nLong description."
    ) == x
    # Raises information.
    x = Docstring()
    x.short_description = "A simple docstring."

# Generated at 2022-06-13 19:53:50.743403
# Unit test for function parse
def test_parse():
    docstring = """
    Short description.

    Long description.

    :param x: bla
    :param y: bla
    :returns: bla
    :rtype: str
    :raises ValueError: bla
    """
    result = parse(docstring)
    assert result.short_description == "Short description."
    assert result.blank_after_short_description == True
    assert result.long_description == "Long description."
    assert result.blank_after_long_description == False
    assert len(result.meta) == 4
    assert result.meta[0].arg_name == "x"
    assert result.meta[1].arg_name == "y"
    assert result.meta[2].type_name == "str"
    assert result.meta[3].type_name == "ValueError"



# Generated at 2022-06-13 19:54:05.844132
# Unit test for function parse

# Generated at 2022-06-13 19:54:13.301617
# Unit test for function parse

# Generated at 2022-06-13 19:54:22.289986
# Unit test for function parse
def test_parse():
    test = """\
    This is the Summary.

    This is the Long Description.
    """
    result = parse(test)
    assert result.short_description == "This is the Summary."
    assert result.blank_after_short_description == False
    assert result.long_description == "This is the Long Description."
    assert result.blank_after_long_description == True
    assert result.meta == []

    test = """\
    This is the Summary.

    :param str arg1: This is the 1st argument.
    :param int arg2: This is the 2nd argument.
    """
    result = parse(test)
    assert result.short_description == "This is the Summary."
    assert result.blank_after_short_description == False
    assert result.long_description == None
    assert result.blank_after

# Generated at 2022-06-13 19:54:25.769582
# Unit test for function parse
def test_parse():
    text = """
    First line.
    Second Line.

    :param param1: this is a parameter
    :param param2: this is a parameter
    :returns: None
    """
    docstring = parse(text)
    assert len(docstring.meta) == 3

# Generated at 2022-06-13 19:54:37.833626
# Unit test for function parse
def test_parse():
    # Example 1
    text = """\
    parse: Parse a ReST-style docstring into its component parts.

    :param foo: Example
    :type foo: int
    :param bar: Example 2
    :type bar: str
    :rtype: Tuple[DocstringReturns, ...]
    :returns: The parsed docstring.
    :raises Exception: If the world has ended.

    Example of long description.

    Another paragraph of the long description.
    """
    # expected result

# Generated at 2022-06-13 19:54:51.813327
# Unit test for function parse
def test_parse():
    docstring = """Single line short description
    Multi line long description
    
    :param param1: Parameter 1
    :type param1: str
    :returns: Some integer
    :rtype: int
    """
    parsed = parse(docstring)
    assert parsed.short_description == "Single line short description"
    assert parsed.long_description == "Multi line long description"
    assert parsed.blank_after_short_description == True
    assert parsed.blank_after_long_description == True
    assert parsed.meta[0] == DocstringParam(args=['param1', 'str'], description='Parameter 1', arg_name='param1', type_name='str', is_optional=False, default=None)

# Generated at 2022-06-13 19:54:57.077133
# Unit test for function parse
def test_parse():
    doc_str = """\
    This is a test docstring.

    :param arg: An argument
    :type arg: str
    :returns: This is a return
    :rtype: str
    """

    actual = parse(doc_str)

# Generated at 2022-06-13 19:55:07.263816
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()
    assert parse("Nothing.") == Docstring(
        short_description="Nothing.",
        long_description=None,
        meta=[],
        blank_after_short_description=True,
        blank_after_long_description=False,
    )
    assert parse("\n  Nothing.\n") == Docstring(
        short_description="Nothing.",
        long_description=None,
        meta=[],
        blank_after_short_description=True,
        blank_after_long_description=False,
    )
    assert parse("Nothing.\nNothing else.") == Docstring(
        short_description="Nothing.",
        long_description="Nothing else.",
        meta=[],
        blank_after_short_description=True,
        blank_after_long_description=False,
    )


# Generated at 2022-06-13 19:55:14.364294
# Unit test for function parse
def test_parse():
    docstring = parse(
        """
Parse the ReST-style docstring into its components.

:returns: parsed docstring
:rtype: dict

:returns: some other type
"""
    )
    if len(docstring.meta) != 2:
        print("expected 2 meta entries")
    if docstring.meta[0].args != ['returns']:
        print("expected returns keyword")
    if docstring.meta[1].args != ['rtype', 'dict']:
        print("expected rtype dict")

test_parse()

# Generated at 2022-06-13 19:55:24.594533
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()
    assert parse("hey there") == Docstring(
        short_description="hey there", long_description=None
    )
    assert parse("hey there\n\nmore...") == Docstring(
        short_description="hey there",
        long_description="more...",
        blank_after_short_description=True,
        blank_after_long_description=False,
    )
    assert parse("hey there\nmore...") == Docstring(
        short_description="hey there",
        long_description="more...",
        blank_after_short_description=False,
        blank_after_long_description=False,
    )

# Generated at 2022-06-13 19:55:37.213136
# Unit test for function parse
def test_parse():
    """
    The function of test_parse is to test whether the function parse is working or not
    if the function parse is working properly, the docstring statement is printed
    if the function parse is not working properly, a Parse Error exception will be thrown
    """
    try:
        s = """
        This is a short description.

        This is the long description.

        :param int hello: This is a parameter.
        :raises ValueError: This is a raised exception.
        :returns str: This is the return value.
        """
        docstring = parse(s)
        print(docstring)
    except ParseError as pe:
        print(pe)

# Generated at 2022-06-13 19:55:49.680693
# Unit test for function parse
def test_parse():
    docstring = """Examples
----------------

Quick start::

   >>> from pprint import pprint
   >>> import json
   >>> # read JSON file
   >>> with open('person.json') as f:
   ...     data = json.load(f)
   >>> pprint(data)
   {'address': {'city': 'chicago', 'street': 'Main Street'},
    'age': 25,
    'firstname': 'John',
    'lastname': 'Doe',
    'phone': ['123-456-789', '987-654-321']}
   >>> # write JSON file
   >>> with open('person.json', 'w') as f:
   ...     json.dump(data, f)

"""
    #print(parse(docstring))


# Generated at 2022-06-13 19:55:58.840863
# Unit test for function parse
def test_parse():
    docstring = """One line summary
    Extended description.

    :param str foo: Foo it.
    :param bar: Bar it.
    :returns: The return.
    """
    parsed = parse(docstring)
    assert parsed.short_description == "One line summary"
    assert parsed.long_description == "Extended description."
    assert parsed.blank_after_short_description == True
    assert parsed.blank_after_long_description == False
    assert len(parsed.meta) == 3

    meta = parsed.meta[0]
    assert meta.args == ["param", "str", "foo"]
    assert meta.arg_name == "foo"
    assert meta.type_name == "str"
    assert meta.is_optional == False
    assert meta.default == None

# Generated at 2022-06-13 19:56:15.022749
# Unit test for function parse
def test_parse():
    from .docstring_parser import parse
    from .common import Docstring
    docstring = '''
        Parse the docstring into its components.

        :param x: blah blah blah
        :type x: int

        :return: parsed docstring
        :rtype: Docstring
    '''
    ds = parse(docstring)

# Generated at 2022-06-13 19:56:24.831213
# Unit test for function parse
def test_parse():
    docstring = """short desc

This is the long description.

    It might include Python code.

:param foo: a foo argument
:type foo: str
:param bar: bar argument
:type bar: int
:returns: return value

"""
    parsed = parse(docstring)
    assert 'This is the long description.' == parsed.long_description
    assert 'short desc' == parsed.short_description

# Generated at 2022-06-13 19:56:34.638295
# Unit test for function parse
def test_parse():
    code = """
    Function to add two numbers

    :param x: The first number
    :type x: int
    :param y: The second number
    :type y: int
    :returns: The sum of the two numbers
    :rtype: int
    """

# Generated at 2022-06-13 19:56:46.860197
# Unit test for function parse
def test_parse():
    assert parse(None) == Docstring()
    assert parse("") == Docstring()
    assert parse("Hello world") == Docstring(
        short_description="Hello world",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )
    assert parse(" Hello world \n") == Docstring(
        short_description="Hello world",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )

# Generated at 2022-06-13 19:57:01.030719
# Unit test for function parse

# Generated at 2022-06-13 19:57:05.823392
# Unit test for function parse
def test_parse():
    doc = """
    Short Description.

    This function does a simple test.

    Args:
        input_data: a list of numbers
        return_data: a list of numbers
    Returns:
        a list of numbers
    """
    print(parse(doc))

test_parse()

# Generated at 2022-06-13 19:57:16.377242
# Unit test for function parse
def test_parse():
    doc = parse("""
    One-liner.

    Two-liner.

    :param x: An integer.
    :param y: A string.
    :returns: x + y.
    :raises ValueError: If x < 0
    """)
    assert doc.short_description == "One-liner."
    assert doc.blank_after_short_description
    assert doc.long_description == "Two-liner."
    assert doc.blank_after_long_description
    assert doc.meta[0].arg_name == "x"
    assert doc.meta[0].type_name == "An integer."
    assert doc.meta[0].description == "An integer."
    assert doc.meta[1].arg_name == "y"
    assert doc.meta[1].type_name == "A string."
    assert doc

# Generated at 2022-06-13 19:57:31.300404
# Unit test for function parse
def test_parse():
    docstring = """This is the first line of docstring.
    It is the description of the function.
    :param arg1: this is arg1
    :type arg1: int
    :param arg2: description of arg2
    :type arg2: int
    :return: int
    :rtype: int
    :param arg3: ...
    :type arg3: list
    :param arg4: ...
    :type arg4: list
    :param arg5: ...
    :type arg5: list
    :param arg6: ...
    :type arg6: list
    :returns: an int
    :rtype: int
    :raises: None
    """
    result = parse(docstring)
    print(result)


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:57:38.974245
# Unit test for function parse
def test_parse():
    docstring = '''
    Short description.

    Long description.

    :param x: Tuple representing location of element.
               Defaults to (0, ).
               Supports an arbitrary number of dimensions.
    :type x: tuple
    :returns: Element at specified location.
              If element does not exist, returns None.
    :rtype: scalar or None
    :raises RuntimeError: For some reason.
    '''

# Generated at 2022-06-13 19:57:52.559431
# Unit test for function parse
def test_parse():
    doc = parse.__doc__
    ds = parse(doc)
    assert isinstance(ds, Docstring)
    assert ds.short_description == "Parse the ReST-style docstring into its components."
    assert ds.long_description is not None
    assert ds.blank_after_short_description is True
    assert ds.blank_after_long_description is False
    assert len(ds.meta) == 2

    ds = parse("")
    assert isinstance(ds, Docstring)
    assert ds.short_description is None
    assert ds.long_description is None
    assert ds.blank_after_short_description is False
    assert ds.blank_after_long_description is False
    assert len(ds.meta) == 0


# Generated at 2022-06-13 19:58:01.679940
# Unit test for function parse
def test_parse():
    assert parse('"""\n test \n"""') == Docstring()
    tmp = DocstringReturns(
        args=['Returns'],
        description='No return value.',
        type_name=None,
        is_generator=False
    )
    assert parse('"""\n test \n\n:Returns: No return value. \n\n"""') == Docstring(
        short_description="test",
        blank_after_short_description=True,
        blank_after_long_description=True,
        long_description=None,
        meta=[tmp],
    )

# Generated at 2022-06-13 19:58:12.378572
# Unit test for function parse
def test_parse():
    text ='''\
        Function Description
        
        :param one: First integer
        :type one: int
        :param two: Second integer
        :type two: int
        :returns: a+b
        :rtype: int
        :raises ValueError: one or both inputs are not integers
        
        Another paragraph
    '''
    assert parse(text).short_description == "Function Description"
    assert len(parse(text).meta) == 4
    assert parse(text).meta[0].args[0] == "param"
    assert parse(text).meta[0].args[1] == "one: First integer"
    assert parse(text).meta[3].args[0] == "raises"

# Generated at 2022-06-13 19:58:18.350779
# Unit test for function parse
def test_parse():
    # Case 1: docstring with several meta chunks each starting with a colon
    text = """This is a docstring.
        :param arg_a: the a argument
        :type arg_a: int
        :param arg_b: the b argument
        :type arg_b: int
        :param arg_c: the b argument
        :returns: return value
        """
    docstring = parse(text)
    assert len(docstring.meta) == 4
    assert docstring.meta[0].arg_name == "arg_a"
    assert docstring.meta[1].arg_name == "arg_b"
    assert docstring.meta[2].arg_name == "arg_c"
    assert docstring.meta[3].arg_name is None

    # Case 2: docstring with a single meta chunk starting with a colon

# Generated at 2022-06-13 19:58:28.122236
# Unit test for function parse
def test_parse():
    text = """\
    Return a string with a specified number of repetitions
    of a specified string.
    :param str string: The string to be repeated.
    :param int number: The number of times to repeat the string.
    :returns: str - String with the repeated value.
    """
    docstring = parse(text)

    assert(docstring.short_description == "Return a string with a specified number of repetitions of a specified string.")
    assert(docstring.long_description == "The string to be repeated.\nThe number of times to repeat the string.")
    assert(docstring.blank_after_short_description == False)
    assert(docstring.blank_after_long_description == False)
    assert(docstring.meta[0].arg_name == 'string')

# Generated at 2022-06-13 19:58:40.549246
# Unit test for function parse
def test_parse():
    """Test to parse the docstring"""
    from .common import assert_docstring_equal


# Generated at 2022-06-13 19:58:44.144177
# Unit test for function parse
def test_parse():
    text = """
    test
    :type x: int
    :type y: str
    """
    print(parse(text))

# Generated at 2022-06-13 19:58:51.213760
# Unit test for function parse
def test_parse():
    assert not parse("")
    assert parse("This is the short description.") == Docstring(
        short_description="This is the short description."
    )
    assert parse("A short description.") == Docstring(
        short_description="A short description."
    )
    assert parse("This is the short description.\n\nThis is the long description.") == Docstring(
        short_description="This is the short description.",
        blank_after_short_description=True,
        long_description="This is the long description.",
    )

# Generated at 2022-06-13 19:59:06.683995
# Unit test for function parse
def test_parse():
    # type (T.Any) -> None
    example = """
        This is the short description.
    
        This is the long description.
    
        :param foo: This is a parameter named foo
        :param bar: This is a parameter named bar
        :param baz: This is a parameter named baz
        """
    doc = parse(example)
    assert doc.short_description == "This is the short description."
    assert doc.long_description == "This is the long description."
    assert len(doc.meta) == 3
    assert [m[0] for m in doc.meta] == ["param", "param", "param"]
    assert [m[1] for m in doc.meta] == ["foo", "bar", "baz"]

# Generated at 2022-06-13 19:59:13.368062
# Unit test for function parse
def test_parse():
    docstring_text = """This is a description of a func.

:param x: The name of the first parameter.
:param y: The name of the second parameter. Defaults to 42.
:type y: any
:param z: The name of the third parameter. Defaults to 1+1.
:type z: int
:returns: The description of the return value.
:rtype: int
:raises ValueError: An exception that is raised
"""

    docstring = parse(docstring_text)

    assert docstring.short_description == "This is a description of a func."
    assert docstring.long_description == "The description of the return value."
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == True
    assert docstring.meta[0].arg_

# Generated at 2022-06-13 19:59:24.218082
# Unit test for function parse
def test_parse():
    """ Parse Test """
    res = parse("""path_id: Path ID
    :param path_id: The path id
    :type path_id: required
    :param path_id: Path ID.
    :param path_id: Path ID.
    :param path_id: Path ID.
    :param path_id: Path ID.
    :type path_id: number
    :type path_id: number
    :param path_id: Path ID.
    
    
    
    
    
    
    :param path_id: Path ID.
    :param path_id: Path ID.
    :raises: The error.
    :yields: The yield
    :returns: The return.
    :returns: The return.
    """)
    print(res.short_description)


# Generated at 2022-06-13 19:59:32.984830
# Unit test for function parse
def test_parse():
    doc = """First line.

    More lines.

    :param x:
        Description of x.
    :returns:
        Description of return.
    """
    ret = parse(doc)
    assert ret.short_description == "First line."
    assert ret.blank_after_short_description
    assert ret.long_description == "More lines."
    assert ret.blank_after_long_description
    assert len(ret.meta) == 2

    assert ret.meta[0].keyword == "param"
    assert ret.meta[0].arg_name == "x"

    assert ret.meta[1].keyword == "returns"
    assert ret.meta[1].type_name is None

# Generated at 2022-06-13 19:59:43.008388
# Unit test for function parse
def test_parse():
    def func_one():
        """This function does one thing.

        :param arg1: the first parameter
        :type arg1: str
        :param arg2: the second parameter
        :type arg2: int, optional
        :param arg3: the third parameter, defaults to True
        :type arg3: bool

        :returns: None
        :raises ValueError: when something bad happens

        This is the first paragraph of the long description.

        This is the second paragraph of the long description.
        """
        pass

    docstring = parse(func_one.__doc__)

    # Testing __repr__()

# Generated at 2022-06-13 19:59:55.013401
# Unit test for function parse
def test_parse():
    doc1 = '''One-line short description.
    Long description is indented.

    And it
    can span
    multiple lines.
    '''

    doc2 = '''Single-line short description.

    And this one is followed by two blank lines.

    :param foo: Foo takes an integer
    :type foo: int
    :param bar: Bar takes a string
    :type bar: str

    :returns: None.
    '''

    doc3 = '''A docstring with only a short description.

    :param foo:
    :type foo:
    :param bar:
    :type bar:
    :raises ImportError:
    '''


# Generated at 2022-06-13 20:00:02.077826
# Unit test for function parse
def test_parse():
    """Unit test for function parse."""
    string = """
        :param a: a
        :type a: str
        :param b: b
        :type b: str
        :param c: c
        :param d: c
        :returns: type
        :rtype: str
        :raises: Exception
        :yields: type
        :ytype: str
        :yields: type
        :ytype: str
        :returns: type
        :rtype: str
        :raises: Exception
        """
    docstring = parse(string)
    assert len(docstring.meta) == 10
    assert isinstance(docstring.meta[0], DocstringParam)
    assert docstring.meta[0].arg_name == 'a'
    assert docstring.meta[0].type_name

# Generated at 2022-06-13 20:00:13.248314
# Unit test for function parse
def test_parse():
    from .common import DocstringParam, DocstringReturns, DocstringRaises

# Generated at 2022-06-13 20:00:23.172151
# Unit test for function parse

# Generated at 2022-06-13 20:00:26.790062
# Unit test for function parse
def test_parse():
    # print(parse(inspect.getdoc(parse)))
    assert(parse(inspect.getdoc(parse)) is not None)

# Generated at 2022-06-13 20:00:42.936816
# Unit test for function parse
def test_parse():
    sut = parse("""\
    this docstring does not have a blank after short description
    The short description.
    The long description.
    With a blank after it.
    :arg int x: The x coordinate.
    :arg int y: The y coordinate.
    :raises np.NumpyError: when x or y is negative.
    :raises ValueError: when x or y is too large.
    :returns: a point (x, y)
    :yields int: an int
    :returns: a point (x, y)
    """)
    assert not sut.blank_after_short_description
    assert sut.short_description == 'The short description.'
    assert sut.blank_after_long_description

# Generated at 2022-06-13 20:00:49.997198
# Unit test for function parse
def test_parse():
    text = '''\
    This is a summary.

    Here is the long description.

    :param param1: this is param1
    :type param1: int or float
    :param param2: this is param2
    :type param2: str
    :returns: this is return
    :rtype: int
    '''
    d = parse(text)
    assert len(d.meta) == 3
    assert d.meta[0].arg_name == 'param1'
    assert d.meta[0].type_name == 'int or float'
    assert d.meta[0].is_optional is None
    assert d.meta[0].default is None
    assert d.meta[1].arg_name == 'param2'
    assert d.meta[1].type_name == 'str'

# Generated at 2022-06-13 20:01:00.388994
# Unit test for function parse
def test_parse():
    """
    This is a unit test for the function "parse" in module 'restyled_docstring'
    """

    assert parse("case 1") == Docstring(
        short_description="case 1",
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )

    assert parse("case 1\n\ndescription: a") == Docstring(
        short_description="case 1",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description="description: a",
        meta=[],
    )


# Generated at 2022-06-13 20:01:09.772832
# Unit test for function parse
def test_parse():
    """Tests parsing of docstrings
    """
    doc = """Description

    :param foo: the foo element.
    :type foo: int
    :param bar: the bar element.
    :type bar: str
    :param egg: the egg element.
    :type egg: int or str
    :param pig: the pig element.
    :type pig: int, str or None
    :raises ValueError: if the input is invalid
    :yields: a value
    :yields: another value
    :yields: yet another value
    :returns: the average
    :returns: the average, in another style
    :returns: None
    """

# Generated at 2022-06-13 20:01:15.164798
# Unit test for function parse
def test_parse():
    docstring = r"""
    Short summary.

    Longer
    description.

    :param foo:
        The foo parameter.
    :type foo: bar
    :param bar:
        The bar parameter.
    :type bar: baz
    :param biz:
        The biz parameter.
    :type biz: baz
    """
    ds = parse(docstring)
    assert ds.short_description == "Short summary."
    assert ds.long_description == "Longer\ndescription."
    assert len(ds.meta) == 3
    assert ds.meta[0].args == ["param", "foo"]
    assert ds.meta[0].description == "The foo parameter."
    assert ds.meta[0].arg_name == "foo"
    assert ds.meta[0].type

# Generated at 2022-06-13 20:01:16.577143
# Unit test for function parse
def test_parse():
    # to be implemented
    pass

# Generated at 2022-06-13 20:01:26.385901
# Unit test for function parse

# Generated at 2022-06-13 20:01:34.903037
# Unit test for function parse
def test_parse():
    parsing_string = parse("""This is a description.

*:param cls: a particular class.
:param verbose: Output progress messages, defaults to False.
:returns: The number of images in the directory.
:raises ValueError: If the directory does not exist.
    """)

    for meta in parsing_string.meta:
        print(meta.__class__)
        print(meta.args)
        print(meta.description)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 20:01:45.561394
# Unit test for function parse
def test_parse():
    assert parse('The first line of a docstring.\n\nThe second line of the docstring.') == Docstring(short_description='The first line of a docstring.', blank_after_short_description=True, blank_after_long_description=True, long_description='The second line of the docstring.', meta=[])
    assert parse(':param x: The first parameter.') == Docstring(short_description=None, blank_after_short_description=False, blank_after_long_description=False, long_description=None, meta=[DocstringParam(args=['param', 'x'], description='The first parameter.', arg_name='x', type_name=None, is_optional=None, default=None)])

# Generated at 2022-06-13 20:01:53.943564
# Unit test for function parse