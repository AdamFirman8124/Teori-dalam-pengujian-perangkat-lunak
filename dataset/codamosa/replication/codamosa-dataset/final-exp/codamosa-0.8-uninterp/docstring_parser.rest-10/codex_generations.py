

# Generated at 2022-06-13 19:52:16.830540
# Unit test for function parse
def test_parse():
    doc = """Do some crazy calculations.
    :param int arg1: the first value
    :param arg2: the second value
    :param int arg3: the third value"""
    ds = parse(doc)
    assert ds.short_description == 'Do some crazy calculations.'
    assert ds.long_description is None
    assert len(ds.meta) == 3
    assert ds.meta[0].args == ["int", "arg1"]
    assert ds.meta[0].type_name == "int"


# Generated at 2022-06-13 19:52:18.605487
# Unit test for function parse
def test_parse():
    from .common import _assert_equal_docstrings
    _assert_equal_docstrings(parse, __doc__)



# Generated at 2022-06-13 19:52:27.631303
# Unit test for function parse
def test_parse():
    # TODO: figure out a less fragile way of testing this.
    docstring = """
    My function.
    
    This is a multi-line description.
    
    Parameters
    ----------
    arg : str
        Some value
    arg2 : str, optional
        Some value
    
    Returns
    -------
    int
        Something
    """
    doc = parse(docstring)
    assert str(doc.short_description) == "My function."
    assert doc.long_description == "This is a multi-line description."
    assert doc.blank_after_short_description
    assert doc.blank_after_long_description

    meta = doc.meta.get("param")
    assert meta[0].arg_name == "arg"
    assert meta[0].type_name == "str"

# Generated at 2022-06-13 19:52:43.038634
# Unit test for function parse
def test_parse():
    string = """
    test_parse_1 is a function for parse docstring.

    :param str arg1: docstring
    :param int arg2: docstring
    :return: docstring
    :rtype: str
    """

    doc = parse(string)
    assert doc.short_description == "test_parse_1 is a function for parse docstring."
    assert doc.long_description == "param str arg1: docstring\nparam int arg2: docstring\nreturn: docstring\n"
    assert len(doc.meta) == 4
    assert doc.meta[0].args == ['param', 'str', 'arg1'] 
    assert doc.meta[0].description == "docstring"
    assert doc.meta[0].arg_name == 'arg1'
    assert doc.meta[0].type_name

# Generated at 2022-06-13 19:52:54.107983
# Unit test for function parse
def test_parse():
    """Unit test for function parse."""

    def test_parse(doc, expected):
        assert parse(doc) == expected

    test_parse("", Docstring())
    test_parse(" ", Docstring())
    test_parse("\t", Docstring())
    test_parse("\n", Docstring())
    test_parse("\n\n", Docstring())
    test_parse("\n\n\n", Docstring())

    test_parse(
        "Foo.\n",
        Docstring(
            short_description="Foo.",
            blank_after_short_description=True,
            blank_after_long_description=False,
            long_description=None,
            meta=[],
        ),
    )


# Generated at 2022-06-13 19:53:06.308863
# Unit test for function parse
def test_parse():
    docstring = parse("""
        Short description.

        Long description.

        :param arg1: arg1 description
        :type arg1: int
        :return: return description
        :rtype: float"""
    )
    assert docstring.short_description == "Short description."
    assert docstring.long_description == "Long description."
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False
    assert docstring.meta[0].arg_name == "arg1"
    assert docstring.meta[0].type_name == "int"
    assert docstring.meta[0].is_optional == False
    assert docstring.meta[0].default == None
    assert docstring.meta[0].description == "arg1 description"

# Generated at 2022-06-13 19:53:14.530965
# Unit test for function parse
def test_parse():
    doc1 = """
    This is the short description.

    This is the first line of the long description.

    This is the second line.
    """
    assert parse(doc1).short_description == "This is the short description."
    assert parse(doc1).long_description == "This is the first line of the long description.\n\nThis is the second line."

    doc2 = doc1 + """

    :param arg1: this is an argument.
    :type arg1: int
    :raises IOError: if an I/O error occurs.
    :returns: this is what is returned.
    :rtype: int

    """
    doc2_parse = parse(doc2)
    assert doc2_parse.short_description == "This is the short description."

# Generated at 2022-06-13 19:53:28.109578
# Unit test for function parse
def test_parse():
    docstring = parse(
        """
        This docstring is an example of a return keyword.

        Args:
          param1 (int): The first parameter.
          param2 (str): The second parameter.

        Returns:
          str: The return value.

        Raises:
          ValueError: If `param2` is equal to `param1`.
        """
    )
    assert len(docstring.meta) == 3
    assert docstring.meta[0].arg_name == 'param1'
    assert docstring.meta[0].type_name == 'int'
    assert docstring.meta[0].is_optional is None
    assert docstring.meta[0].default is None
    assert docstring.meta[0].description == 'The first parameter.'
    assert docstring.meta[1].arg_name == 'param2'

# Generated at 2022-06-13 19:53:34.748731
# Unit test for function parse
def test_parse():
    assert parse("""
            Short description.

            Long description.
        """) == Docstring(
        short_description="Short description.",
        long_description="Long description.",
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )


# Generated at 2022-06-13 19:53:41.653211
# Unit test for function parse
def test_parse():
    docstring = "Takes two number and divide the first one by the second one."
    assert parse(docstring).short_description == "Takes two number and divide the first one by the second one."

    docstring = "Takes two number and divide the first one by the second one.\n\n"
    assert parse(docstring).short_description == "Takes two number and divide the first one by the second one."
    assert parse(docstring).blank_after_short_description is True
    assert parse(docstring).blank_after_long_description is True
    assert parse(docstring).long_description is None

    docstring = "   Takes two number and divide the first one by the second one.\n\n"
    assert parse(docstring).short_description == "Takes two number and divide the first one by the second one."
   

# Generated at 2022-06-13 19:53:53.375452
# Unit test for function parse

# Generated at 2022-06-13 19:54:05.521561
# Unit test for function parse
def test_parse():
    """"Parse a docstring into its components."""

# Generated at 2022-06-13 19:54:08.488372
# Unit test for function parse
def test_parse():
    a = parse("""
    Create a new empty list.

    :param foo:
        This is a long description.
        The second line of the description.
    """)
    print(a)

test_parse()

# Generated at 2022-06-13 19:54:18.217379
# Unit test for function parse
def test_parse():
    docstring = parse("""
    Args:
        arg1: Arg1 description
        arg2 (str): Arg2 description.
                     A longer description that spans multiple lines.
                     It includes :code:`formatting options`.
        arg3 (int): Arg3 description.
    Returns:
        A string that details the return value.
        This spans multiple lines.
    """)
    
    print("Short description:\n" + docstring.short_description)
    print("Long description:\n" + docstring.long_description)
    for meta in docstring.meta:
        print("Meta content:\n{}".format(meta.args))
        print("Meta description:\n{}".format(meta.description))

# Generated at 2022-06-13 19:54:26.899834
# Unit test for function parse

# Generated at 2022-06-13 19:54:38.621616
# Unit test for function parse
def test_parse():
    text = """\
    Example function with types documented in the docstring.

    :param int bar: Description of bar
    :raises ValueError: If `bar` is negative.

    :returns: A dict object
    """
    docstring = parse(text)
    assert docstring.short_description == "Example function with types documented in the docstring."
    assert docstring.blank_after_short_description is False
    assert docstring.long_description is None
    assert docstring.blank_after_long_description is False
    assert len(docstring.meta) == 2
    assert isinstance(docstring.meta[0], DocstringParam)
    assert docstring.meta[0].args == ['param', 'int', 'bar']
    assert docstring.meta[0].description == 'Description of bar'
    assert docstring.meta

# Generated at 2022-06-13 19:54:51.800723
# Unit test for function parse
def test_parse():
    docstring_snip = """
    This is a snippet for testing parse function.
    This is a snippet for testing parse function.
    This is a snippet for testing parse function.
    This is a snippet for testing parse function.

    Parameters
    ----------
    file_name : str
        The name of the file.

    Returns
    -------
    file_contents : str
        The content of the file.

    Raises
    ------
    IOError
        In case of something bad.
    """

    result = parse(docstring_snip)
    assert(type(result) == Docstring)
    assert(result.short_description == "This is a snippet for testing parse function. This is a snippet for testing parse function. This is a snippet for testing parse function. This is a snippet for testing parse function.")

# Generated at 2022-06-13 19:54:59.239993
# Unit test for function parse
def test_parse():
    docstring = '''Test the ReST-style docstring into its components.

    :returns: parsed docstring
    '''
    ds = parse(docstring)
    assert ds.short_description == 'Test the ReST-style docstring into its components.'
    assert len(ds.meta) == 1
    assert ds.meta[0].args[0] == 'returns'
    assert ds.meta[0].description == 'parsed docstring'

# Generated at 2022-06-13 19:55:02.665534
# Unit test for function parse
def test_parse():
    source = inspect.getsource(parse)
    s = parse(source)

    assert s
    assert all(s.short_description, s.long_description, s.meta)
    assert len(s.meta) == 12


# Generated at 2022-06-13 19:55:09.219104
# Unit test for function parse
def test_parse():
    """Test the parse function."""

# Generated at 2022-06-13 19:55:16.359947
# Unit test for function parse
def test_parse():
    def my_function():
        """Ths is a test docstring.
        :param test:This is a test parameter
        :param test2: This is another test parameter.
        :yields: a test yield
        :raises ValueError: This is a test raise
        """
        pass
    assert parse(my_function.__doc__)

# Generated at 2022-06-13 19:55:23.029245
# Unit test for function parse
def test_parse():
    text = inspect.cleandoc("""
        This is the short description.

        This is the long description. It can take multiple lines,
        but must be indented.

        A blank line is used to separate paragraphs.

        :arg name: The name of the function.
        :arg parent: The parent class.
        :keyword repr: The repr value.
        :raises ValueError: If the value is incorrect.
        :returns: A nicely formatted string.
    """)
    result = parse(text)

    # Test short description
    assert result.short_description == "This is the short description."
    assert result.blank_after_short_description is False

    # Test long description

# Generated at 2022-06-13 19:55:26.686739
# Unit test for function parse
def test_parse():
    add : int
    """
    Test function to check the parse function
    :param a: int
    :param b: int
    :returns: int
    """
    pass

# Generated at 2022-06-13 19:55:38.212014
# Unit test for function parse
def test_parse():
    text = """

    This is a function that does nothing but return stuff.

    :param a: first parameter
    :param b: second parameter
    :type b: list
    :returns: something
    :raises ValueError: ???


    """
    doc = parse(text)
    assert not doc.short_description
    assert doc.blank_after_short_description
    assert doc.long_description

    doc = parse(inspect.cleandoc(text))
    assert not doc.short_description
    assert not doc.blank_after_short_description
    assert doc.long_description


# Generated at 2022-06-13 19:55:41.812465
# Unit test for function parse
def test_parse():
    docstring = """Returns:
        str: The title of this book.
    """
    print(parse(docstring))


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:55:54.107828
# Unit test for function parse
def test_parse():
    assert parse("""\
        short string
        """)._asdict() == Docstring(
        short_description="short string",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )._asdict()

    assert parse("""\
        short string

        long string
        """)._asdict() == Docstring(
        short_description="short string",
        long_description="long string",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[],
    )._asdict()


# Generated at 2022-06-13 19:56:03.798227
# Unit test for function parse

# Generated at 2022-06-13 19:56:13.352074
# Unit test for function parse
def test_parse():
    """
    >>> test = '''
    ... This is the short description.
    ...
    ... This is the long description.
    ...
    ... :param: one two three   Long description of one two three.
    ... '''
    >>> parse(test)
    Docstring(short_description='This is the short description.', blank_after_short_description=False, long_description='This is the long description.', blank_after_long_description=False, meta=[DocstringParam(args=['param', 'one', 'two', 'three'], description='Long description of one two three.', arg_name='one two three', type_name=None, is_optional=None, default=None)])
    """
    pass

# Generated at 2022-06-13 19:56:23.437900
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    assert parse(
        """
        One line summary.

        First paragraph.

        Second paragraph.

        :param foo:
            This describes the foo parameter.
        """
    ) == Docstring(
        short_description="One line summary.",
        long_description="First paragraph.\nSecond paragraph.",
        meta=[
            DocstringParam(
                description="This describes the foo parameter.",
                arg_name="foo",
                type_name=None,
                is_optional=None,
                default=None,
            )
        ],
        blank_after_short_description=False,
        blank_after_long_description=True,
    )


# Generated at 2022-06-13 19:56:33.596287
# Unit test for function parse
def test_parse():
    # function has no docstring
    assert parse("") == Docstring()

    # function has one-line docstring
    assert parse("str(object='') -> str") == Docstring(
        short_description="str(object='') -> str",
    )

    # function has one-line docstring without ending newline
    assert parse("str(object='') -> str") == Docstring(
        short_description="str(object='') -> str",
    )

    # function has one-line docstring with ending newline
    assert parse("str(object='') -> str\n") == Docstring(
        short_description="str(object='') -> str",
        blank_after_short_description=True,
        blank_after_long_description=False,
    )

    # function has newline-terminated

# Generated at 2022-06-13 19:56:49.144866
# Unit test for function parse
def test_parse():
    test_string = """Test Function.

This is a long description.

:param int arg1: This is argument 1.
:param int arg2: This is argument 2.
:param bool arg3: This is argument 3.
:returns: Description of return value.
:raises ValueError: This is the error message.
"""

    ret = parse(test_string)
    assert ret.short_description == "Test Function."
    assert ret.long_description == "This is a long description."
    assert ret.blank_after_short_description == True
    assert ret.blank_after_long_description == False
    assert len(ret.meta) == 4
    assert ret.meta[0].type_name == "int"
    assert ret.meta[0].arg_name == "arg1"

# Generated at 2022-06-13 19:57:02.328915
# Unit test for function parse
def test_parse():
    assert(parse("") == Docstring())
    assert(parse("test") == Docstring(short_description="test"))
    assert(parse("test\nfoo\nbar") == Docstring(short_description="test", long_description="foo\nbar"))
    assert(parse("test\n\nfoo\nbar") == Docstring(short_description="test", blank_after_short_description=True, long_description="foo\nbar"))
    assert(parse("test\n\nfoo\nbar\n\n") == Docstring(short_description="test", blank_after_short_description=True, blank_after_long_description=True,long_description="foo\nbar"))

# Generated at 2022-06-13 19:57:13.963253
# Unit test for function parse
def test_parse():
    """Test docstring parsing."""
    text = """\
    Short description
    Long description.

    :param name: The name to use.
    :type name: str
    :param age: age of the person.

    :returns: int

    :raises AttributeError: Raises AttributeError.
    :raises TypeError: Raises TypeError.
    """
    docstring = parse(text)

    assert docstring.short_description == "Short description"
    assert docstring.blank_after_short_description
    assert docstring.long_description == "Long description."
    assert docstring.blank_after_long_description
    assert docstring.meta[0].arg_name == "name"
    assert docstring.meta[0].type_name == "str"

# Generated at 2022-06-13 19:57:26.845484
# Unit test for function parse
def test_parse():
    code = """\
    This is a function with a docstring.

    :param param1: This is the first param
    :type param1: string
    :param param2: This is a second param
    :type param2: integer, optional
    :returns: this is something

    This is a long description.
    """

    res = parse(code)

    assert res.short_description == "This is a function with a docstring."
    assert res.long_description == "This is a long description."
    assert len(res.meta) == 2
    assert res.meta[0].args[0] == "param1"
    assert res.meta[0].arg_name == "param1"
    assert res.meta[0].type_name == "string"

# Generated at 2022-06-13 19:57:34.758771
# Unit test for function parse
def test_parse():
    ds = inspect.cleandoc(
        """
    Function docstring

    :param arg1: The first argument
    :param arg2: The second argument
    :raises SomeError: If something bad happens
    :returns: Nothing
    :param arg3: The third argument
    :raises OtherError: If something else bad happens
    """
    )

    parsed = parse(ds)

    assert parsed.short_description == "Function docstring"

    assert parsed.meta[0].description == "The first argument"
    assert parsed.meta[0].args == ["param", "arg1"]

    assert parsed.meta[1].description == "The second argument"
    assert parsed.meta[1].args == ["param", "arg2"]

    assert parsed.meta[2].description == "If something bad happens"
    assert parsed.meta

# Generated at 2022-06-13 19:57:48.591420
# Unit test for function parse
def test_parse():
    # Docstring with short and long description
    docstring = '''
    Short description.

    Long description.

    :param name: The name of the attribute.
    :type name: :class:`.Str`
    :param value: The value of the attribute.
    :type value: :class:`.Value`
    :param ref: The owner of the attribute.
    :type ref: :class:`.Obj`
    :returns: New attribute.
    :rtype: :class:`.Attr`
    :raises AttributeError: Raised if the object is not an object.
    '''
    docstring_parsed = parse(docstring)
    assert docstring_parsed.short_description == "Short description."
    assert docstring_parsed.long_description == "Long description."
    assert docstring_

# Generated at 2022-06-13 19:58:01.719851
# Unit test for function parse
def test_parse():
    s = '''\n        This is the first line of the long description.

        This is the second line of the long description.
        '''
    assert parse(s) == Docstring(
        short_description='This is the first line of the long description.',
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description='This is the second line of the long description.',
        meta=[],
    )


# Generated at 2022-06-13 19:58:12.428522
# Unit test for function parse
def test_parse():
    parse("")
    parse("Test")
    parse("Test\n")
    parse("Test\n\n")
    parse("Test\n\n\n")
    parse("Test.\n")
    parse("Test.\n\n")
    parse("Test.\n\n\n")
    parse(":")
    parse("Test\n:")
    parse("Test.\n:")
    parse("Test:\n:")
    parse("Test:\n:\n")
    parse("Test:\n:  \n")
    parse("Test:\n:  \n\n")
    parse("Test:\n:  \n\n\n")
    parse("Test:\n:     :")
    parse("Test:\n:     :Test")
    parse("Test:\n:     :Test \n")
    parse

# Generated at 2022-06-13 19:58:21.481723
# Unit test for function parse
def test_parse():
    doc = parse(
        """One-sentence summary.

        Detailed description.

        :param int a: Parameter a.
        :param int b: Parameter b.
        """
    )
    assert doc.short_description == "One-sentence summary."
    assert doc.long_description == "Detailed description."
    assert len(doc.meta) == 2
    assert doc.meta[0].arg_name == "a"
    assert doc.meta[0].type_name == "int"
    assert doc.meta[1].arg_name == "b"
    assert doc.meta[1].type_name == "int"

# Generated at 2022-06-13 19:58:29.978404
# Unit test for function parse
def test_parse():
    """Tests the parse function"""
    docstring = """
    """
    assert (str(parse(docstring)) == str(Docstring()))

    docstring = """
A short description.

A long description.
"""
    assert (str(parse(docstring)) == str(Docstring(
        short_description="A short description.",
        long_description="A long description.",
    )))

    docstring = """
:param arg1: description
:param arg2: description
"""

# Generated at 2022-06-13 19:58:45.818880
# Unit test for function parse
def test_parse():
    t1 = """
    Short summary.

        Args:
            foo: a foo
            bar: a bar

        Returns:
            a
            b
    """
    ret = parse(t1)
    assert isinstance(ret.meta[0], DocstringParam)
    assert ret.meta[0].arg_name == "foo"
    assert ret.meta[1].arg_name == "bar"
    assert isinstance(ret.meta[2], DocstringReturns)
    assert ret.meta[2].type_name == ""
    assert ret.meta[2].description == "a\nb"

if __name__ == '__main__':
    t1 = """
    Short summary.

        Args:
            foo: a foo
            bar: a bar

        Returns:
            a
            b
    """
    ret

# Generated at 2022-06-13 19:58:54.148055
# Unit test for function parse
def test_parse():
    doc = inspect.cleandoc(
        """Test docstring
        :param str name: name of the person.
        :param address: address of the person.
        :type address: dict.
        :returns: a string.
        :raises InvalidTypeException:
        """
    )

    docstring = parse(doc)
    assert(docstring.short_description == "Test docstring")
    assert(len(docstring.meta) == 4)
    assert(docstring.meta[0].args == ['param', 'str', 'name'])
    assert(docstring.meta[0].description == "name of the person.")
    assert(docstring.meta[0].arg_name == 'name')
    assert(docstring.meta[0].type_name == 'str')

# Generated at 2022-06-13 19:59:00.100924
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    text = """
    Test
    ----

    Test.
    """
    doc = parse(text)
    assert doc.short_description == "Test"
    assert doc.long_description == "Test."
    assert doc.blank_after_short_description is True
    assert doc.blank_after_long_description is False
    assert len(doc.meta) == 0



# Generated at 2022-06-13 19:59:09.225787
# Unit test for function parse
def test_parse():
    doc = """This is a docstring.

    There are two paragraphs in this docstring.
    """

    docstring = parse(doc)
    print(docstring)
    assert docstring.short_description is not None
    assert docstring.long_description is not None
    assert len(docstring.meta) == 0

    doc = """This is a docstring.
    :keyword arg1: keyword 1
    :keyword arg2: keyword 2
    :returns: None

    There are two paragraphs in this docstring.
    """

    docstring = parse(doc)
    print(docstring)
    assert docstring.short_description is not None
    assert docstring.long_description is not None
    assert len(docstring.meta) == 2
    assert docstring.meta[0].name == 'returns'

# Generated at 2022-06-13 19:59:19.562513
# Unit test for function parse
def test_parse():
    doc_string = '''
    def add(a: int, b: int) -> int:
    """
    This is a short description.

    This is a long description.
    """
    raise TypeError("abc")
    '''
    docstr = parse(doc_string)
    assert docstr.short_description == 'def add(a: int, b: int) -> int'
    assert docstr.long_description == 'This is a long description.'
    assert docstr.meta[0].arg_name == 'a'
    assert docstr.meta[1].arg_name == 'b'
    assert docstr.meta[3].description == 'abc'

# Generated at 2022-06-13 19:59:35.326299
# Unit test for function parse
def test_parse():
    """Unit test for function parse.
    """

    assert parse("") == Docstring(
        short_description=None,
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )

    assert parse(
        "    "
    ) == Docstring(
        short_description=None,
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )


# Generated at 2022-06-13 19:59:43.864250
# Unit test for function parse

# Generated at 2022-06-13 19:59:55.814691
# Unit test for function parse

# Generated at 2022-06-13 20:00:06.299769
# Unit test for function parse
def test_parse():
    """Parse a simple docstring"""
    given_str = """
    Extract string and convert to list of keys

    :param string: String to extract keys from.
    :param separator: One or more characters to use as separators.
        Defaults to a single space.
    :param maxsplit: Maximum number of splits to perform.
        -1 means no limit.

    :returns: List of keys.
    """

    ret_obj = parse(given_str)
    # print(ret_obj)
    assert ret_obj.short_description == "Extract string and convert to list of keys"
    assert len(ret_obj.long_description) == 0
    assert ret_obj.meta[2].arg_name == "separator"


# Generated at 2022-06-13 20:00:18.940263
# Unit test for function parse
def test_parse():
    import unittest

    class TestParse(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_simple_docstring(self):
            text = "This is a simple docstring for testing."
            result = parse(text)
            self.assertEqual(result.short_description, text)

        def test_metadata(self):
            text = """
            Short description.
            :param int a: parameter a.
            :param int b: parameter b.
            :return: metadata.
            """.strip()
            result = parse(text)
            self.assertEqual(result.short_description, "Short description.")
            self.assertEqual(len(result.meta), 3)

# Generated at 2022-06-13 20:00:34.643252
# Unit test for function parse
def test_parse():
    doc = """
    Add a and b.

    :param a: first addend
    :type a: int
    :param b: second addend
    :type b: int
    :returns: a + b
    :rtype: int
    :raises ZeroDivisionError: if b is zero
    """

    result = parse(doc)

# Generated at 2022-06-13 20:00:45.729727
# Unit test for function parse

# Generated at 2022-06-13 20:00:51.556775
# Unit test for function parse
def test_parse():
    input = """\
    """
    output = Docstring()
    assert parse(input) == output

    input = """
    test.
    """
    output = Docstring(
        short_description="test.",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=None,
        meta=[],
    )
    assert parse(input) == output

    input = """
    test.
    more test.
    """
    output = Docstring(
        short_description="test.",
        long_description="more test.",
        blank_after_short_description=False,
        blank_after_long_description=True,
        meta=[],
    )
    assert parse(input) == output

    input = """
    test.

    more test.
    """

# Generated at 2022-06-13 20:01:01.475361
# Unit test for function parse
def test_parse():
    print('test parse')

    param_str = ':param str arg_name: Argument description.'

    assert "str arg_name" == parse(param_str).meta[0].args
    assert "Argument description." == parse(param_str).meta[0].description
    assert "str" == parse(param_str).meta[0].type_name
    assert "arg_name" == parse(param_str).meta[0].arg_name
    assert False == parse(param_str).meta[0].is_optional
    assert None == parse(param_str).meta[0].default

    param_str = ':param str? arg_name: Argument description.'

    assert "str? arg_name" == parse(param_str).meta[0].args

# Generated at 2022-06-13 20:01:10.442509
# Unit test for function parse
def test_parse():
    """
    Test the function parse
    """
    print("Testing the function parse")
    text = ""
    if (parse(text) != Docstring()):
        print("Test failed")
    text = """
    short
    long
    """
    if (parse(text) != Docstring(
        short_description = "short",
        blank_after_short_description = True,
        blank_after_long_description = True,
        long_description = "long"
    )):
        print("Test failed")
    text = """
    test :
        meta
    """

# Generated at 2022-06-13 20:01:17.579776
# Unit test for function parse
def test_parse():
    from .common import Docstring, DocstringMeta, DocstringParam, DocstringRaises, DocstringReturns


# Generated at 2022-06-13 20:01:22.240468
# Unit test for function parse
def test_parse():
    docstring = '''
This is short description.


This is long description.

Args:
  foo: this is foo
  bar: this is bar
  baz (int): this is int baz

Returns:
    string: blabla
    '''
    parsed_docstring = parse(docstring)
    assert parsed_docstring.short_description == "This is short description."
    assert parsed_docstring.long_description == "This is long description."
    assert len(parsed_docstring.meta) == 3
    assert parsed_docstring.meta[0].args == ['foo', 'this', 'is', 'foo']
    assert parsed_docstring.meta[0].arg_name == 'foo'
    assert parsed_docstring.meta[0].type_name == None
    assert parsed_docstring.meta

# Generated at 2022-06-13 20:01:25.281141
# Unit test for function parse
def test_parse():
    text = '''
        This is a test function.

        This is the long description.
        In multiple lines.

        :param p1: Parameter one.
        :type p1: Type one.
        :param p2: Parameter two.

        :returns: This is the return.
        :rtype: return type.
        :yields: This is a yield.
        :raises: TypeError

        :key: value
        :key: value

    '''
    out = parse(text)
    print(out.meta[0])

# Generated at 2022-06-13 20:01:31.085064
# Unit test for function parse
def test_parse():
    text = '''
    :param arg:
    :
    '''
    parsed_docstring = parse(text)
    assert isinstance(parsed_docstring.meta, list)
    assert isinstance(parsed_docstring.meta[0], DocstringMeta)
    assert parsed_docstring.meta[0].arg_name is None


# Generated at 2022-06-13 20:01:37.791878
# Unit test for function parse
def test_parse():
    text = """Argument parsing.
    
    :param str x: The X coordinate.
    :param int y: The Y coordinate, defaults to 2.
    :param bool z: The Z coordinate, defaults to False.
    :returns int: The sum of the coordinates.
    :raises ValueError: If any coordinate is negative.
    """

    print(parse(text))

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 20:01:50.483079
# Unit test for function parse
def test_parse():
    docstring = inspect.cleandoc("""\
    This is short description.

    This is long description.
    """)

    assert parse(docstring) == Docstring(
        short_description="This is short description.",
        blank_after_short_description=True,
        long_description="This is long description.",
        blank_after_long_description=True,
        meta=[],
    )

    docstring = inspect.cleandoc("""\
        This is short description.

        This is long description.

        :param foo: parameter
        :return: value
        """)
