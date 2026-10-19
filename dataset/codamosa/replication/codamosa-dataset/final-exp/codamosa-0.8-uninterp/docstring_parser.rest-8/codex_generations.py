

# Generated at 2022-06-13 19:52:10.302850
# Unit test for function parse
def test_parse():
    example = """
    Example of a docstring with a short description and a long description.

    :param x: an integer argument.
    :type x: int
    :param y: an optional float argument.
    :type y: float
    :raises IndexError: when x is out of bounds.
    :returns: the product of x and y.
    :rtype: float or None
    """

    p = parse(example)
    assert p.short_description == 'Example of a docstring with a short description and a long description.'
    assert p.long_description == 'the product of x and y.'
    assert len(p.meta) == 4
    assert isinstance(p.meta[0], DocstringParam)
    assert p.meta[0].key == 'param'

# Generated at 2022-06-13 19:52:17.550745
# Unit test for function parse
def test_parse():
    fn = inspect.getsource(parse)
    text = "This is a short description"
    doc = """
        This is a short description
        This is a long description
        :arg1: a1
        :arg2: a2
        :returns: result
    """
    assert parse(text)

    assert parse(doc).short_description == "This is a short description"
    assert parse(doc).long_description == "This is a long description"
    assert parse(doc).meta == [
        DocstringMeta(
            ['arg1', 'a1'], 'a1'
        ),
        DocstringMeta(['arg2', 'a2'], 'a2'),
        DocstringMeta(['returns', 'result'], 'result')
    ]


# Generated at 2022-06-13 19:52:24.251962
# Unit test for function parse
def test_parse():
    ds = parse.__doc__

    ds_parsed = parse(ds)
    assert ds_parsed.short_description == "Parse the ReST-style docstring into its components."
    assert (ds_parsed.long_description ==
        ":returns: parsed docstring"
    )
    assert (ds_parsed.meta[0].arg_name ==
        "parsed docstring"
    )
    assert ds_parsed.meta[0].key == "returns"
    assert len(ds_parsed.meta) == 1


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:52:34.076732
# Unit test for function parse
def test_parse():
    text = """
    Short description.

    Long
    description.

    :param foo: Foo arg
    :param int bar: Bar arg
    :param int? baz: Baz arg
    :param int bla: Bla arg
    :return: Returns something
    :raises ValueError: Raises this
    :yields int: Yields this
    """

# Generated at 2022-06-13 19:52:44.683025
# Unit test for function parse
def test_parse():
    text = """
        Function sample

        :param int x: The x coordinate.
        :param bool y: The y coordinate.
        :param string name: The name of the player.
        """
    d = parse(text)
    assert d.short_description == "Function sample"
    assert d.long_description is None
    assert len(d.meta) == 3

    assert d.meta[0].description == "The x coordinate."
    assert d.meta[0].args == ["param", "int", "x"]
    assert d.meta[0].arg_name == "x"
    assert d.meta[0].type_name == "int"
    assert d.meta[0].is_optional is None
    assert d.meta[0].default is None

    assert d.meta[1].description == "The y coordinate."


# Generated at 2022-06-13 19:52:55.300303
# Unit test for function parse
def test_parse():
    func_str = '''
    """
    Some function.

    :param arg1: docstring for arg1.
    
    :param arg2: docstring for arg2. Default is 5.
    :type arg2: int

    :param arg3: docstring for arg3. Default is None.
    :type arg3: str

    :raises Exception: If something bad happens

    :return: docstring for return value.
    :rtype: str
    """
    '''
    
    d = parse(func_str)
    assert(d.short_description == 'Some function.')
    meta = d.meta
    assert(isinstance(meta[0], DocstringParam))
    assert(meta[0].arg_name == 'arg1')
    assert(meta[0].type_name is None)

# Generated at 2022-06-13 19:53:06.913520
# Unit test for function parse
def test_parse():
    docstring = """\
    First line of the docstring.

    Second paragraph of the docstring.

    :param arg1: The first argument.
    :type arg1: int
    :param arg2: The second argument.
    :type arg2: str
    :param arg3: The third argument.
    :type arg3: bool
    :return: None
    :rtype: None
    :raises AttributeError: If the attribute does not exist.
    :raises ValueError: If the attribute does not have the correct value.
    """

# Generated at 2022-06-13 19:53:17.718800
# Unit test for function parse
def test_parse():
    # Test with no text
    text = ""
    test = parse(text)
    assert test == Docstring()

    # Test with text that doesn't follow the proper format
    text = "This is not a proper docstring"
    try:
        parse(text)
        assert False
    except ParseError:
        assert True

    # Test with a docstring that only has descriptions
    text = "This is the short description\n\nAnd this is the long description."
    test = parse(text)
    assert test == Docstring(
        short_description="This is the short description",
        long_description="This is the long description.",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[],
    )

    # Test with a docstring that has both descriptions and meta information


# Generated at 2022-06-13 19:53:31.017362
# Unit test for function parse

# Generated at 2022-06-13 19:53:43.091606
# Unit test for function parse

# Generated at 2022-06-13 19:54:04.109489
# Unit test for function parse
def test_parse():
    docstring = parse("""
        Test function.
        
        Test function with a docstring.
    """)
    assert docstring.short_description == "Test function."
    assert docstring.long_description == "Test function with a docstring."
    assert len(docstring.meta) == 0

    docstring = parse("""
        Test function.
        
        Test function with a docstring.
        
        :param x: an int
        :type x: int
        :param y: a string
        :type y: str
    """)
    assert docstring.short_description == "Test function."
    assert docstring.long_description == "Test function with a docstring."
    assert len(docstring.meta) == 2


# Generated at 2022-06-13 19:54:14.357207
# Unit test for function parse
def test_parse():
    def foo():
        """docstring for foo

        :param bar: bar
        :param str baz: baz
        :param int quux?: quux?
        :defaults to 42.
        :returns: return value
        :rtype: int
        :returns int: return value
        :return: return value
        :yields: yield value
        :yields int: yield value
        :yield: yield value
        :raises: raise value
        :raises int: raise value
        """

    ds = parse(foo.__doc__)
    assert ds.short_description == "docstring for foo"
    assert ds.blank_after_short_description is True
    assert ds.blank_after_long_description is True
    assert ds.long_description == ""

    assert len

# Generated at 2022-06-13 19:54:24.526872
# Unit test for function parse
def test_parse():
    docstring = \
"""
This is a short description.

This is a long description.

:param arg1: This is a long description.
:param arg2: This is a long description.
:returns: This is a long description.
"""
    parsed = parse(docstring)
    assert str(parsed) == docstring
    assert parsed.short_description == "This is a short description."
    assert parsed.long_description == "This is a long description."
    assert parsed.meta[0].keyword == "param"
    assert parsed.meta[0].args == ["param", "arg1"]
    assert parsed.meta[0].description == "This is a long description."
    assert parsed.meta[1].keyword == "param"
    assert parsed.meta[1].args == ["param", "arg2"]
   

# Generated at 2022-06-13 19:54:37.144739
# Unit test for function parse
def test_parse():
    assert parse("""This is a line.""") == Docstring(
        short_description="This is a line.",
        blank_after_short_description=False,
        long_description=None,
        blank_after_long_description=False,
        meta=[],
    )
    assert parse("""This is a line.

And this is another line.

And this is another line.
"""
                 ) == Docstring(
        short_description="This is a line.",
        blank_after_short_description=True,
        long_description="And this is another line.\n\nAnd this is another line.",
        blank_after_long_description=False,
        meta=[],
    )
    assert parse("""This is a line.


And this is another line.

And this is another line.
"""
                 )

# Generated at 2022-06-13 19:54:39.246501
# Unit test for function parse
def test_parse():
    assert parse("") is not None
    assert parse("  ") is not None


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-13 19:54:42.659343
# Unit test for function parse
def test_parse():
    text = inspect.cleandoc("""
    """
    )
    print(parse(text))

if __name__ == "__main__":

    test_parse()

# Generated at 2022-06-13 19:54:56.305516
# Unit test for function parse
def test_parse():
    docstring = '''
    Short description.
    
    Long description.
    
    :param arg: A description.
    :type arg: str
    :param arg2: A description.
    :param arg3: A description.
    :type arg3: int
    :return: A description.
    :rtype: str
    :returns: A description.
    :raises ValueError: A description.
    :raises ValueError: A description.
    :raises ValueError: A description.
    '''
    doc = parse(docstring)
    assert len(doc.meta) == 7
    assert doc.short_description == 'Short description.'
    assert doc.long_description == 'Long description.'
    assert doc.blank_after_short_description
    assert doc.blank_after_long_description
    assert doc

# Generated at 2022-06-13 19:55:05.984056
# Unit test for function parse
def test_parse():
    """ Unit test for parse() """
    print("Running Test Parse")
    docstring_text = """This is a summary line.

    This is a test of the doctest module.
    Ignore this line.

    This is another line.

    This line should be blank.

    :param name: The name of the user.
    :param age: The age of the user.
    :returns: Something about the return value.

    """
    docstring = parse(docstring_text)
    print(docstring)
    print('-------')
    print('Test parse() complete')
    print('---------------------------------')


if __name__ == "__main__":
    print("Running tests for ReST-style docstring parsing")
    test_parse()

# Generated at 2022-06-13 19:55:09.455818
# Unit test for function parse
def test_parse():
    assert parse("foo") == Docstring(
        short_description="foo",
        blank_after_short_description=False,
        blank_after_long_description=None,
        long_description=None,
        meta=[],
    )



# Generated at 2022-06-13 19:55:14.775798
# Unit test for function parse
def test_parse():
    docstring = """Este es el docstring de una prueba
        :param a: este es el parametro a
        :type a: int
        :param: b: este es el parametro b
        :returns: int
        """
    print(parse(docstring))


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:55:34.731424
# Unit test for function parse
def test_parse():
    def f(x: int, y: float = 3.14) -> tuple:
        """Test function for docstring parsing.

        :param x: first argument
        :type x: integer
        :param y: second argument (defaults to 3.14)
        :type y: float
        :returns: the unit test results
        """


# Generated at 2022-06-13 19:55:42.663062
# Unit test for function parse
def test_parse():
    from .common import Docstring, DocstringMeta, DocstringParam, DocstringRaises, DocstringReturns
    from .common import ParseError

    text = """
    Short description.

    Long description.
    """
    docstring = parse(text)
    assert isinstance(docstring, Docstring)
    assert docstring.short_description == "Short description."
    assert docstring.long_description == "Long description."
    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is True
    assert len(docstring.meta) == 0

    text = """
    Short description.
    """
    docstring = parse(text)
    assert isinstance(docstring, Docstring)
    assert docstring.short_description == "Short description."
    assert docstring.long_description

# Generated at 2022-06-13 19:55:54.694123
# Unit test for function parse
def test_parse():

    from .common import Docstring
    import pytest
    from .sample_docstrings import RST_STYLE_SAMPLE
    from .fixtures import rst_sample_docstring
    from .sample_docstrings import DOCSTRINGS

    for doc in DOCSTRINGS:
        parsed = parse(doc)
        assert parsed == rst_sample_docstring

    with pytest.raises(TypeError):
        parse(123)

    with pytest.raises(TypeError):
        parse(True)

    with pytest.raises(ValueError):
        parse([])


    # # Sanity check
    # assert parse(RST_STYLE_SAMPLE) == rst_sample_docstring
    #
    # with pytest.raises(TypeError):
    #     parse(123)
    #
   

# Generated at 2022-06-13 19:56:04.010345
# Unit test for function parse
def test_parse():
    from . import test_data

    def _test(buffer):
        doc = parse(buffer)
        assert doc.short_description == test_data.FUNCTION_SHORT_DESCRIPTION
        assert doc.long_description == test_data.FUNCTION_LONG_DESCRIPTION
        assert len(doc.meta) == test_data.FUNCTION_META_LEN
        for expected, actual in zip(test_data.FUNCTION_META, doc.meta):
            assert expected == actual

    _test(test_data.FUNCTION_DOCSTRING)
    _test("%s\n\n" % test_data.FUNCTION_DOCSTRING)
    _test("%s\n" % test_data.FUNCTION_DOCSTRING)


# Generated at 2022-06-13 19:56:14.722496
# Unit test for function parse
def test_parse():
    docstring = parse(
        """
    This is the short description.

    This is the long description.

    :param a: A parameter.
    :type a: This is the type.
    :param b: Another parameter.
    :returns: This is a return value.
    :rtype: This is the return type.

    """
    )
    assert docstring.short_description == "This is the short description."
    assert docstring.long_description == "This is the long description."
    assert docstring.blank_after_short_description
    assert not docstring.blank_after_long_description

    assert len(docstring.meta) == 2
    assert docstring.meta[0].type == DocstringParam
    assert docstring.meta[0].arg_name == "a"

# Generated at 2022-06-13 19:56:24.568108
# Unit test for function parse
def test_parse():
    test_docstring = """This is a simple function.

:param arg1: Description of first argument.
:type arg1: str
:param arg2: List of ints.
:type arg2: list
:param arg3: (Optional) A dictionary.
:type arg3: dict
:param arg4: (Optional, defaults to 1) An int.
:type arg4: int
:returns: Some value.
:rtype: int
:raises ValueError: If something goes wrong.
"""

    output = parse(test_docstring)
    assert output.short_description == "This is a simple function."
    assert output.blank_after_short_description == False
    assert (
        output.long_description == "Description of first argument.\nList of ints."
    )
    assert output.blank_after_long

# Generated at 2022-06-13 19:56:34.441042
# Unit test for function parse
def test_parse():
    assert parse(
        """
        """
    ) == Docstring(
        short_description=None,
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )
    assert parse(
        """
        short description
        """
    ) == Docstring(
        short_description="short description",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )

# Generated at 2022-06-13 19:56:46.699708
# Unit test for function parse
def test_parse():
    assert parse.__annotations__["text"] == str
    assert parse(None) == Docstring()

    text = "One line docstring."
    doc = parse(text)
    assert doc.short_description == "One line docstring."
    assert not doc.long_description
    assert doc.meta == []

    text = "One line docstring.\n"
    doc = parse(text)
    assert doc.short_description == "One line docstring."
    assert not doc.long_description
    assert doc.meta == []

    text = "One line docstring.\n\n"
    doc = parse(text)
    assert doc.short_description == "One line docstring."
    assert not doc.long_description
    assert doc.meta == []

    text = "One line docstring.\n\n"
   

# Generated at 2022-06-13 19:56:58.928984
# Unit test for function parse
def test_parse():
    
    text= """
    
    
    
    
        This is a docstring.
    
    :param x: The X coordinate.
    :param y: The Y coordinate.
    
    
    
    
    
    
    
    :returns: The sum of x and y.
    :rtype: int
    """
    result = parse(text)
    
    assert len(result.meta) == 6
    assert result.meta[0].description == 'The X coordinate.'
    assert result.meta[1].description == 'The Y coordinate.'
    assert result.meta[2].description == 'The sum of x and y.'
    assert result.meta[3].description == 'int'
    
    

# Generated at 2022-06-13 19:57:07.014017
# Unit test for function parse
def test_parse():
    docstring = '''\
        This function does something.

        :param int param1: The first parameter.
        :param param2: The second parameter.
        :returns: Nothing.
        :raises ValueError: If anything goes wrong.

        Some more description.\
        '''
    parsed = parse(docstring)
    assert parsed.short_description == 'This function does something.'
    assert parsed.long_description == 'Some more description.'
    assert parsed.blank_after_short_description
    assert parsed.blank_after_long_description
    assert parsed.meta[0].args == ['param', 'int', 'param1']
    assert parsed.meta[0].is_optional is False
    assert parsed.meta[0].default is None
    assert parsed.meta[0].type_name == 'int'

# Generated at 2022-06-13 19:57:26.795032
# Unit test for function parse
def test_parse():
    text = """\
        myfunc(a, b, c)
        Short description
        Long
        multi-line
        description.

        :param a: Parameter a
        :type a: str
        :type unknown: will raise an exception
        :param b: Parameter b
        :type b: int
        :param c: Parameter c
        :type c: float
        :returns:
        :rtype: bool
        :some: garbage
        :raises ValueError: if something bad happens
        """

    d = parse(text)

    assert d.short_description == "myfunc(a, b, c)"
    assert d.blank_after_short_description is False
    assert d.long_description == "Short description\nLong\nmulti-line\ndescription."
    assert d.blank_after_long

# Generated at 2022-06-13 19:57:34.178604
# Unit test for function parse
def test_parse():
    d = parse("""
    Hello!

    :param int val: Value.
    :returns: Nothing.
    """)

    assert d.short_description == "Hello!"
    assert d.long_description == None
    assert d.blank_after_short_description == True
    assert d.blank_after_long_description == True
    assert len(d.meta) == 2
    assert d.meta[0].description == "Value."
    assert d.meta[1].description == "Nothing."


# Generated at 2022-06-13 19:57:48.478293
# Unit test for function parse
def test_parse():
    d = parse("""A function that adds its arguments.

    :param a: the first number
    :param int b: the second number
    :returns: the sum
    :raises ValueError: if x is negative
    """)
    assert d.short_description == "A function that adds its arguments."
    assert d.long_description == "the sum"

# Generated at 2022-06-13 19:57:59.887750
# Unit test for function parse
def test_parse():
  text = "Hello world\n\nMulti-line\n\n:param name: The character's name\n:type name: str\n:default name: John Doe"
  text = parse(text)
  assert text.short_description == 'Hello world'
  assert text.meta[0].description == "Hello world"
  assert text.meta[0].args[0] == 'name'
  assert text.meta[0].type_name == 'str'
  assert text.meta[0].arg_name == 'name'
  assert text.meta[0].is_optional == False
  assert text.meta[0].default == 'John Doe'

# Generated at 2022-06-13 19:58:10.220294
# Unit test for function parse

# Generated at 2022-06-13 19:58:21.218108
# Unit test for function parse
def test_parse():
    docstring = """Single line docstring.

    Long description is on multiple lines.

    :param foo: The first parameter.

    :type foo: str

    :param bar: The second parameter.
    :type bar: int, optional

    :returns: 

    :rtype: None

    :raises ValueError: if something bad happens.
    """

    parsed_docstring = parse(docstring)
    assert parsed_docstring

    assert parsed_docstring.short_description == "Single line docstring."
    assert parsed_docstring.long_description == 'Long description is on multiple lines.'
    assert parsed_docstring.blank_after_short_description

    assert len(parsed_docstring.meta) == 4
    assert type(parsed_docstring.meta[0]) == DocstringParam
    assert parsed_doc

# Generated at 2022-06-13 19:58:29.816063
# Unit test for function parse
def test_parse():
    # Test simple docstrings
    assert parse('Foo bar') == Docstring(
        short_description='Foo bar', long_description=None
    )
    assert parse('') == Docstring()
    assert parse('Foo bar\nzoo barg') == Docstring(
        short_description='Foo bar',
        long_description='zoo barg',
        blank_after_short_description=True,
        blank_after_long_description=False,
    )
    assert parse('Foo bar\n\nzoo barg') == Docstring(
        short_description='Foo bar',
        long_description='zoo barg',
        blank_after_short_description=True,
        blank_after_long_description=True,
    )

# Generated at 2022-06-13 19:58:41.238917
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()
    assert parse("short description") == Docstring(
        short_description="short description"
    )
    assert parse("short description\n") == Docstring(
        short_description="short description"
    )
    assert parse("short description\n\n") == Docstring(
        short_description="short description"
    )
    assert parse("short description\n\n\n") == Docstring(
        short_description="short description"
    )
    assert parse("short description\n\nlong description\n") == Docstring(
        short_description="short description",
        long_description="long description",
        blank_after_short_description=True,
    )

# Generated at 2022-06-13 19:58:45.650385
# Unit test for function parse
def test_parse():
    x = parse.__globals__['DocstringMeta']
    print(x)


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:58:51.163663
# Unit test for function parse
def test_parse():
	docstring = """
		:param doc_type: str
			The type of document
			this attribute is optional.
		:param doc_size: int
			The size of the document
			this attribute is required.
			defaults to None.

		:raises DocumentError: If there was a problem processing the document.
		:returns: A doc_size byte array of randomly generated bytes.
		:yields: A doc_size byte array of randomly generated bytes.
		"""
	ret = parse(docstring)
	assert len(ret.meta) is 4

# Generated at 2022-06-13 19:59:13.893561
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()
    assert parse(" ") == Docstring()
    assert parse("\n") == Docstring()
    assert parse("test\n") == Docstring(
        short_description="test"
    )
    assert parse("test\n\n") == Docstring(
        short_description="test",
        blank_after_short_description=True,
    )
    assert parse("test\n\nboom") == Docstring(
        short_description="test",
        long_description="boom",
    )
    assert parse("test\n\nboom\n\n") == Docstring(
        short_description="test",
        long_description="boom",
        blank_after_long_description=True,
    )
    assert parse("test\n:param x: blah blah")

# Generated at 2022-06-13 19:59:25.356852
# Unit test for function parse
def test_parse():
    t = """Find a hyponym match in a conceptnet graph, depth-first from a given
start point.

    Parameters
    ----------
    start : str
        The node id of the start point.
    relation : str
        A relation to filter on.
    include_endpoints : bool, default False
        Whether to include start and end points in the returned path.
    exclude_start : bool, default False
        Whether to exclude the start node from being considered as a hyponym.
    """
    s = parse(t)
    assert(s.short_description == "Find a hyponym match in a conceptnet graph, depth-first from a given start point.")

# Generated at 2022-06-13 19:59:33.923417
# Unit test for function parse
def test_parse():
    # Source:
    # class Parent(object):
    #    '''
    #    parent example
    #    :param x:
    #    :param y:
    #    :returns:
    #    :rtype:
    #    :raises:
    #    '''
    #    def __init__(self, x, y):
    #        ''

    text = '''parent example
        :param x:
        :param y:
        :returns:
        :rtype:
        :raises:'''

    result = parse(text)
    assert result.short_description == 'parent example'
    assert result.blank_after_short_description == True
    assert result.blank_after_long_description == True
    assert result.long_description == None

# Generated at 2022-06-13 19:59:43.157578
# Unit test for function parse
def test_parse():
    my_docstring = """
    :param int length: the length of the rectangle
    :param int width: the width of the rectangle

    :returns: The area of the rectangle
    """
    my_docstring_output = parse(my_docstring)
    my_docstring_output.meta[0].description == 'the length of the rectangle'
    my_docstring_output.meta[0].arg_name == 'length'
    my_docstring_output.meta[0].type_name == 'int'
    my_docstring_output.meta[1].description == 'the width of the rectangle'
    my_docstring_output.meta[1].arg_name == 'width'
    my_docstring_output.meta[1].type_name == 'int'



# Generated at 2022-06-13 19:59:55.214160
# Unit test for function parse
def test_parse():
  docstring = """
    This function does something

    :param foo: the foo argument
    :type foo: int
    :param bar: the bar argument
    :type bar: int
    :param baz: the baz argument
    :type baz: int
    :return: None
    :rtype: None
  """
  res = parse(docstring)
  assert(res.long_description == "This function does something")
  assert(res.blank_after_short_description == True)
  assert(res.short_description == "This function does something")
  assert(res.blank_after_long_description == True)
  assert(isinstance(res.meta, list))
  assert(isinstance(res.meta[0], DocstringParam))
  assert(isinstance(res.meta[1], DocstringParam))


# Generated at 2022-06-13 20:00:02.325536
# Unit test for function parse
def test_parse():
    docstring = """Test parse method.
        :param name: name
        :type name: str
        :param age: age
        :type age: str
    """
    result = parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description == 'Test parse method.'
    assert result.long_description == 'name\n        \n        age'

# Generated at 2022-06-13 20:00:13.588900
# Unit test for function parse
def test_parse():
    """
    Test function parse
    """
    desc = """
    Function docstring
    :param arg: argument
    :param kwarg kwarg: keyword argument
    :raises SomeError: what this raises
    :returns: nothing
    """
    d = parse(desc)

    assert d.short_description == "Function docstring"
    assert len(d.meta) == 3
    assert d.meta[0] == DocstringParam(
        ["param", "arg", "arg"], "argument", "arg", None, None, None
    )
    assert d.meta[1] == DocstringParam(
        ["param", "kwarg", "kwarg"],
        "keyword argument",
        "kwarg",
        None,
        None,
        None,
    )
    assert d.meta[2] == Doc

# Generated at 2022-06-13 20:00:23.349194
# Unit test for function parse
def test_parse():
  docstring = '''
  Short description.

  Long description.

  :param str arg1:
      Argument 1.
  :type str arg2:
      Argument 2.
  :param int arg3:
      Argument 3.
  :returns:
      Returns something.
  :rtype int:
      Returns something else.
  :raises type error:
      Raises an error.
  :raises:
      Raises an error with no type.
  '''
  

# Generated at 2022-06-13 20:00:34.257220
# Unit test for function parse
def test_parse():
    
    # Tests return values
    test_return_values = []
    test_return_values.append(parse("""
    Test fuction. 

    Parameters
    ----------
    
    text : str
        File name. 
    """))

    test_return_values.append(parse("""
    Test fuction. 

    Parameters
    ----------
    text : str
        File name. 
        
    Returns
    -------
    ret : Docstring
        Parsed docstring.
    """))

    test_return_values.append(parse("""
    Test fuction. 

    Parameters
    ----------
    text : str
        File name. 
        
    Returns
    -------
    text : str
        File name. 
    """))


# Generated at 2022-06-13 20:00:45.490142
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""

# Generated at 2022-06-13 20:00:54.869726
# Unit test for function parse
def test_parse():
    """Verify that the docstring is parsed correctly."""
    doc = """
    This function does three things.

    1. It does this.

    2. It does that.

    3. It does the last thing.

    :param int arg1: The first parameter.
    :keyword arg2: The second parameter, defaults to 'hi'.
    :yields: (float, str)
    :raises ValueError: If something bad happens.
    :raises: TypeError
    """
    parsed = parse(doc)
    assert parsed.short_description == "This function does three things."
    assert parsed.blank_after_short_description is True
    assert parsed.blank_after_long_description is True

# Generated at 2022-06-13 20:01:03.568191
# Unit test for function parse
def test_parse():
    """Unit test for function parse."""
    assert parse("Simple test") == Docstring(
        short_description="Simple test", long_description=None, meta=[]
    )
    assert parse("Simple test\nSomething longer") == Docstring(
        short_description="Simple test",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description="Something longer",
        meta=[],
    )
    # Trailing whitespace
    assert parse("Simple test\nSomething longer\n\n") == Docstring(
        short_description="Simple test",
        blank_after_short_description=True,
        blank_after_long_description=True,
        long_description="Something longer",
        meta=[],
    )
    # Indented short description

# Generated at 2022-06-13 20:01:08.913468
# Unit test for function parse
def test_parse():
    doc = """
    This is a function.

    It's cool.
    """

    docstring = parse(doc)
    print(docstring)
    assert docstring.short_description == "This is a function."
    assert docstring.long_description == "It's cool."
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description


# Generated at 2022-06-13 20:01:16.904020
# Unit test for function parse
def test_parse():
    docstring = """
    Short description.
    
    Full description.
    """
    d = parse(docstring)
    assert d.short_description == "Short description."
    assert d.long_description == "Full description."
    assert d.meta == []
    assert d.blank_after_short_description == True
    assert d.blank_after_long_description == True

    docstring = """
    Short description. Full description.
    """
    d = parse(docstring)
    assert d.short_description == "Short description. Full description."
    assert d.long_description == None
    assert d.blank_after_short_description == False
    assert d.blank_after_long_description == False


# Generated at 2022-06-13 20:01:21.909623
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()
    assert parse(None) == Docstring()

    assert parse('foo') == Docstring(
        short_description='foo',
        long_description=None,
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[],
    )
    assert parse('\n') == Docstring(
        short_description=None,
        long_description='',
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )
    assert parse('\n\n') == Docstring(
        short_description=None,
        long_description='',
        blank_after_short_description=False,
        blank_after_long_description=True,
        meta=[],
    )

# Generated at 2022-06-13 20:01:29.476772
# Unit test for function parse
def test_parse():
    document = """Summary line.

This is the longer description.
    """
    assert parse(document).__dict__ == {
        "short_description": 'Summary line.',
        "long_description": 'This is the longer description.',
        "blank_after_short_description": True,
        "blank_after_long_description": False,
        "meta": []
    }

    document = """Summary line.

This is the longer description.

:param arg1: This is arg1.
:param arg2: This is arg2.
:raises TypeError: This is a type error.
:return: This is a return value
"""

# Generated at 2022-06-13 20:01:41.083720
# Unit test for function parse
def test_parse():
    src = """
    Parse the ReST-style docstring into its components.

    :returns: parsed docstring
    :rtype: Docstring
    :param text: Text to parse
    :type text: string
    :raises ParseError: Indicates an error
    :param optional: An optional parameter
    :type optional: Optional[str]
    :default optional: "Optional value"
    :param optional2: A second optional parameter
    :type optional2: Optional[str] = "Optional value"
    """


# Generated at 2022-06-13 20:01:51.065566
# Unit test for function parse
def test_parse():
    assert parse("") == parse("\n") == parse("\n\n")
    assert parse("lorem ipsum") == Docstring(
        short_description="lorem ipsum", blank_after_short_description=True
    )
    assert parse("lorem ipsum\ndolor sit amet.") == Docstring(
        short_description="lorem ipsum",
        blank_after_short_description=False,
        blank_after_long_description=True,
        long_description="dolor sit amet.",
    )