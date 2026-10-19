

# Generated at 2022-06-13 19:52:20.240556
# Unit test for function parse
def test_parse():
    doc = """\
    Short description.

    Long description.

    :param int argname2: arg2 desc.
    :param argname: arg desc.
    :type argname: int
    :rtype: int
    :returns: return value desc.
    :raises ValueError: raise desc.
    """
    ret = parse(doc)

    assert ret.short_description == "Short description."
    assert ret.blank_after_short_description
    assert ret.long_description == "Long description."
    assert not ret.blank_after_long_description
    assert len(ret.meta) == 5
    assert isinstance(ret.meta[0], DocstringParam)
    assert ret.meta[0].arg_name == "argname2"
    assert ret.meta[0].type_name == "int"
   

# Generated at 2022-06-13 19:52:24.867596
# Unit test for function parse
def test_parse():
    doc = parse("""
    Short description.

    Long description.

    :param int x: x coordinate.
    :param int y: y coordinate.
    :param z: z coordinate.
    :type z: int
    :param int foo: this is foo.
    :param: no argument for x.
    :returns: the sum.
    :rtype: int
    """)

    assert doc.short_description == 'Short description.'
    assert doc.long_description == 'Long description.'
    assert doc.blank_after_short_description
    assert doc.blank_after_long_description

    assert doc.meta[0].arg_name == 'x'
    assert doc.meta[0].description == 'x coordinate.'
    assert doc.meta[0].type_name == 'int'

# Generated at 2022-06-13 19:52:34.735692
# Unit test for function parse
def test_parse():
    docstring = """
    Example module.

    This module does stuff.

    :param x: The first param.
    :param y: The second param.
    :returns: None
    """
    result = parse(docstring)
    print(result.short_description)
    print(result.long_description)
    print(result.blank_after_short_description)
    print(result.blank_after_long_description)
    print(result.meta)

    print(result.meta[0])
    print(result.meta[0].args)
    print(result.meta[0].description)
    print(result.meta[0].type_name)
    print(result.meta[0].is_optional)
    print(result.meta[0].default)

    print(result.meta[1])
    print

# Generated at 2022-06-13 19:52:45.347251
# Unit test for function parse
def test_parse():
    docstring = '''
        Short description.

        Long description.

        :param bar the bar to use
        :type bar: str

        :param baz: the baz to use
        :type baz: str

        :param quux: the quux to use
        :type quux: str

        :raises NotImplementedError: if the function is not implemented
        :raises ValueError: if the function is implemented
        :raises: DeprecationWarning if the function is deprecated
        '''
    ret = parse(docstring)
    assert ret.short_description == "Short description."
    assert ret.long_description == "Long description."
    assert ret.blank_after_short_description == True
    assert ret.blank_after_long_description == False
    assert len(ret.meta) == 6

# Generated at 2022-06-13 19:52:55.735734
# Unit test for function parse
def test_parse():
    doc = inspect.cleandoc('''
        Summary line.

        Extended description.

        :param x: description of x
        :type x: type of x
        :returns: description of return value
        :rtype: return type
        :raises ValueError: description of exception
        :raises TypeError: description of exception
    ''')
    expected = inspect.cleandoc('''
        Summary line.

        Extended description.

        :param  x: type of x - description of x
        :returns: return type - description of return value
        :raises ValueError: description of exception
        :raises TypeError: description of exception
    ''')
    assert parse(doc).dumps() == expected

if __name__ == "__main__":
    print(parse("hello").dumps())

# Generated at 2022-06-13 19:53:07.033640
# Unit test for function parse
def test_parse():
    d = parse('''
        ''')
    assert d.short_description is None
    assert d.long_description is None
    assert d.blank_after_short_description is False
    assert d.blank_after_long_description is False
    assert len(d.meta) == 0


    d = parse('''short description.

        long description.
        ''')
    assert d.short_description == 'short description.'
    assert d.long_description == 'long description.'
    assert d.blank_after_short_description is False
    assert d.blank_after_long_description is False
    assert len(d.meta) == 0


    d = parse('''short description.

        long description.
        ''')
    assert d.short_description == 'short description.'
    assert d.long

# Generated at 2022-06-13 19:53:17.828941
# Unit test for function parse
def test_parse():
    """Parse the doc string"""
    text = """Single line docstring.

Multi-line docstring.

    :param type_name arg_name: Description.
    :type type_name: Description.
    :keyword type_name arg_name: Description.
    :raises Exception: Description.
    :yields type_name: Description.
    :yields: Description.
    :returns type_name: Description.
    :returns: Description.
    :rtype type_name: Description.
    """

# Generated at 2022-06-13 19:53:31.552998
# Unit test for function parse
def test_parse():
    # test parse
    assert parse("") == Docstring()

    doc = parse("""This is a function.

    This function is really cool.
    It does great things.""")
    assert doc.short_description == "This is a function."
    assert doc.long_description == """This function is really cool.
It does great things."""
    assert len(doc.meta) == 0

    doc = parse("""This is a function.

    :param  foo : The foo argument.
    :type     foo : int
    :param  bar: The bar argument.
    :type     bar: str
    :returns: The return value.
    :rtype: bool""")
    assert doc.short_description == "This is a function."
    assert doc.long_description is None

# Generated at 2022-06-13 19:53:45.676073
# Unit test for function parse

# Generated at 2022-06-13 19:53:53.545599
# Unit test for function parse
def test_parse():
    docstring_text = """
    This function does a thing.

    :param a: description for a
    :param b: description for b
    :type a: str
    :type b: int
    :returns: description for return value
    :rtype: str
    :raises OSError: raises when something goes wrong
    :raises TypeError: raises when something else goes wrong
    :raises ValueError: raises when something else goes wrong
    :other: something to ignore

    """

    docstring = parse(docstring_text)

    assert docstring.short_description == "This function does a thing."

# Generated at 2022-06-13 19:54:09.022659
# Unit test for function parse
def test_parse():
    class test:
        "short_description\n\nlong_description\n"

# Generated at 2022-06-13 19:54:15.035576
# Unit test for function parse
def test_parse():
    docstring = """
A short summary, appearing on the first line.

A detailed description of a function.

:param argname: description of a parameter
:param argname: description of a parameter

:returns: description of the return value
    """
    print(parse(docstring))

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:54:24.934691
# Unit test for function parse
def test_parse():
    doc = """Test function parse in docstring.py
    :param str name: Name.
    :returns: A string.
    """
    result = parse(doc)
    print(result.meta)
    assert result.meta[0].description == "Name."
    assert result.meta[0].arg_name == "name"
    assert result.meta[0].type_name == "str"
    assert result.meta[0].is_optional is False
    assert result.meta[0].default is None
    assert result.meta[1].description == "A string."
    assert result.meta[1].type_name == "str"
    assert result.meta[1].is_optional is None
    assert result.meta[1].default is None

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:54:37.337906
# Unit test for function parse
def test_parse():
    def test_func():
        """this is a test function
        :param x: x is an integer
        :returns: the value of the parameter x
        """
        return x

# Generated at 2022-06-13 19:54:48.757501
# Unit test for function parse
def test_parse():
    doc = parse(
        """
    Loads an image with the given filename.
    :param filename: name of the image
    :type filename: str
    :rtype: Image
    """
    )

    assert doc.short_description == "Loads an image with the given filename."
    assert len(doc.meta) == 1

    param = doc.meta[0]
    assert isinstance(param, DocstringParam)
    assert param.arg_name == "filename"
    assert param.type_name == "str"
    assert param.description == "name of the image"
    assert not param.is_optional
    assert param.default is None

# Generated at 2022-06-13 19:54:59.286344
# Unit test for function parse
def test_parse():
    """Test for function parse."""
    from .common import DocstringParam

    docstring = """
        Test docstring.

        :type arg1: str
        :param arg2: Test description
        :rtype: Test description
        """
    parsed = parse(docstring)
    assert len(parsed.meta) == 3
    assert isinstance(parsed.meta[1], DocstringParam)
    assert parsed.meta[1].arg_name == 'arg2'
    assert parsed.meta[1].type_name is None
    assert parsed.meta[1].is_optional is None
    assert parsed.meta[1].default is None
    return True


# Generated at 2022-06-13 19:55:04.632108
# Unit test for function parse
def test_parse():
    docstring = '''
    Short description.

    Long description.
    '''

    result = parse(docstring)

    assert result.short_description == 'Short description.'
    assert result.blank_after_short_description == True
    assert result.blank_after_long_description == True
    assert result.long_description == 'Long description.'
    assert result.meta == []


# Generated at 2022-06-13 19:55:14.186021
# Unit test for function parse
def test_parse():
    docstring = """This is a short description.

    This is a long
    description.

    :param foo: This is a parameter.
    :type foo: int
    :param bar: This is another parameter.
    :type bar: str
    :param int baz: This is a third parameter.
    :param qux: This is a fourth parameter.
    :type qux: dict, optional
    :param quux: This is a fifth parameter, defaults to True.
    :type quux: bool, optional
    :returns:
    :rtype: dict

    """
    result = parse(docstring)

# Generated at 2022-06-13 19:55:21.895106
# Unit test for function parse
def test_parse():
    docstring = '''Simple function for testing.

    :param arg1: Description of the first parameter.
    :type arg1: str

    :param arg2: Description of the second parameter.
    :type arg2: int, optional

    :param arg3: Description of the third parameter; defaults to 'Hello World!'.
    :type arg3: str

    :raises TypeError: When something very bad happens.
    :raises ValueError: When something even worse happens.

    :returns: Description of what is returned.
    :rtype: bool
    '''


# Generated at 2022-06-13 19:55:26.624925
# Unit test for function parse
def test_parse():
    import unittest
    import textwrap
    import inspect

    class TestParse(unittest.TestCase):
        def test_basic(self):
            text = textwrap.dedent(
                """
                This is my module docstring.

                It is the first thing we see.

                It provides in-depth information about the module.
                """
            )
            docstring = parse(text)
            assert docstring.short_description == "This is my module docstring."
            assert not docstring.blank_after_short_description
            assert not docstring.blank_after_long_description
            with self.assertRaises(AttributeError):
                docstring.meta


# Generated at 2022-06-13 19:55:44.644512
# Unit test for function parse
def test_parse():
    # Test examples from Sphinx documentation
    # https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html?highlight=docstring#using-documentation-strings
    assert parse(
        inspect.cleandoc(
            """
        A very simple function
    """
        )
    ) == Docstring(
        short_description="A very simple function",
        blank_after_short_description=True,
        blank_after_long_description=False,
    )


# Generated at 2022-06-13 19:55:50.664641
# Unit test for function parse
def test_parse():
    result = (
        parse("A single line of text.")
    )
    assert result == Docstring(
        short_description="A single line of text.",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )

    result = (
        parse("")
    )
    assert result == Docstring(
        short_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )

    result = (
        parse("A single line of text.\n")
    )

# Generated at 2022-06-13 19:55:56.702389
# Unit test for function parse
def test_parse():

    doc = parse('''This is a short description.

    This is the long description.

    :param int arg: param documentation example
    ''')
    assert doc.short_description == "This is a short description."
    assert doc.long_description == "This is the long description."
    assert doc.meta[0].arg_name == "arg"
    assert doc.meta[0].description == "param documentation example"
    assert doc.meta[0].type_name == "int"

# Generated at 2022-06-13 19:56:12.426713
# Unit test for function parse
def test_parse():
    print(parse('test_parse'))
    print(parse('test_parse\n'))
    print(parse('test_parse\n\n'))
    print(parse(''))
    print(parse('Return the sine of x (measured in radians).'))
    print(parse('Return the sine of x (measured in radians).\n'))
    print(parse('Return the sine of x (measured in radians).\n\n'))
    print(parse('\nReturn the sine of x (measured in radians).'))
    print(parse('\n\nReturn the sine of x (measured in radians).'))
    print(parse('\n\nReturn the sine of x (measured in radians).\n'))

# Generated at 2022-06-13 19:56:13.523960
# Unit test for function parse
def test_parse():
    pass

# Generated at 2022-06-13 19:56:23.566148
# Unit test for function parse
def test_parse():
    """
    Simple unit test for function parse

    Runs parse on a sample docstring and prints output.
    """
    docstring = """\
    This is a sample docstring

    This is the long description. It can be separated from
    the short description by a blank line. The line above
    has a blank line as well to show how this is done.
    """
    print(docstring)
    print()
    print(parse(docstring))
    print()

# Generated at 2022-06-13 19:56:33.628011
# Unit test for function parse
def test_parse():
    text = """
    A short description.

    A long description.

    :param name: object name
    :type name: str
    :param value: object value
    :type value: int
    :returns: a dict
    :rtype: dict
    """

    ret = parse(text)
    assert ret.short_description == "A short description."
    assert ret.long_description == "A long description."

    assert len(ret.meta) == 3
    _meta = ret.meta
    _meta0: DocstringParam = _meta[0]
    assert _meta0.args == ["param", "name"]
    assert _meta0.description == "object name"
    assert _meta0.type_name is None
    assert _meta0.is_optional is None
    assert _meta0.default is None

    _

# Generated at 2022-06-13 19:56:45.842099
# Unit test for function parse
def test_parse():
    def foo():
        """
        This is a test function
        :param name: the name of the person
        :type name: str

        :param age: the age of the person
        :type age: int, optional
        :default age: 20
        :returns test_value: the test value
        """
        pass

    d = parse(inspect.getdoc(foo))

    assert d.short_description == "This is a test function"
    assert d.blank_after_short_description is True
    assert d.blank_after_long_description is True
    assert d.long_description == ""

    assert isinstance(d.meta[0], DocstringParam)
    assert d.meta[0].args == ["param", "name", "name"]
    assert d.meta[0].description == "the name of the person"

# Generated at 2022-06-13 19:56:58.679862
# Unit test for function parse
def test_parse():
    s = """\
        Parse the ReST-style docstring into its components.

        :param string text: text to parse
        :returns: parsed docstring
        """

    doc = parse(s)

    res = [DocstringMeta(
        args=["param", "string", "text"],
        description="text to parse",
    ), DocstringMeta(
        args=["returns"],
        description="parsed docstring",
    )]

    assert doc.short_description == "Parse the ReST-style docstring into its components."
    assert doc.blank_after_short_description == False
    assert doc.blank_after_long_description == True
    assert doc.long_description == None
    assert doc.meta == res


# Generated at 2022-06-13 19:57:06.705417
# Unit test for function parse
def test_parse():
    docstring = """
    Compute the average.

    :param a: the first value
    :type a: float
    :param b: the second value
    :type b: float
    :returns: the average of the inputs
    :rtype: float
    :raises ZeroDivisionError: if b is zero
    """
    test_docstring = parse(docstring)
    print(test_docstring.short_description)
    print(test_docstring.long_description)
    print(test_docstring.blank_after_short_description)
    print(test_docstring.blank_after_long_description)
    for m in test_docstring.meta:
        print(m)

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:57:26.937405
# Unit test for function parse
def test_parse():
    #: type: Docstring
    docstring = parse(inspect.cleandoc(inspect.getsource(parse)))

    assert docstring.short_description == "Parse the ReST-style docstring into its components."
    assert (
        docstring.long_description
        == """\
        :returns: parsed docstring"""
    )
    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is False
    assert len(docstring.meta) == 7

    assert docstring.meta[0] == DocstringParam(
        ["param", "text", "str"],
        "docstring to parse",
        arg_name="text",
        type_name="str",
        is_optional=False,
    )
    assert docstring.meta[1] == Docstring

# Generated at 2022-06-13 19:57:34.812155
# Unit test for function parse

# Generated at 2022-06-13 19:57:48.648522
# Unit test for function parse
def test_parse():
    doc = """Return a list of the arguments accepted by a Python function.

Args:
    func: a Python function or Python method.
        If a method is given, the underlying function is extracted.
    include_positional: specify whether to include positional-only
        arguments into the result.

Returns:
    A list of the argument names accepted by the function.
"""
    doc_obj = parse(doc)
    assert doc_obj.short_description == doc.split('\n')[0]
    assert doc_obj.blank_after_short_description
    assert doc_obj.long_description == inspect.cleandoc(doc.split('\n', 1)[1])
    assert doc_obj.blank_after_long_description
    assert len(doc_obj.meta) == 4
    assert doc_obj.meta[0].arg_name

# Generated at 2022-06-13 19:58:01.757439
# Unit test for function parse

# Generated at 2022-06-13 19:58:12.534538
# Unit test for function parse
def test_parse():
    doc = """Short summary.

This is the long description.

:param str a: A string.

:param b: A string.
"""
    parsed = parse(doc)
    assert parsed.short_description == "Short summary."
    assert parsed.long_description == "This is the long description."

    assert len(parsed.meta) == 2
    assert parsed.meta[0].arg_name == "a"
    assert parsed.meta[0].type_name == "str"

    assert parsed.meta[1].arg_name == "b"
    assert parsed.meta[1].type_name is None

if __name__ == "__main__":
    doc = """Short summary.

This is the long description.

:param str a: A string.

:param b: A string.
"""
   

# Generated at 2022-06-13 19:58:23.902400
# Unit test for function parse

# Generated at 2022-06-13 19:58:38.748496
# Unit test for function parse
def test_parse():
    docstring = """
       This is a function
       
       :param x: integer
       :param y: integer
       
       :returns: integer
    """
    parsed = parse(docstring)
    print(parsed)
    assert(parsed.short_description == 'This is a function')
    assert(parsed.long_description == None)
    assert(parsed.blank_after_short_description)
    assert(not parsed.blank_after_long_description)
    assert(len(parsed.meta) == 2)

    assert(parsed.meta[0].arg_name == 'x')
    assert(parsed.meta[0].type_name == 'integer')
    assert(parsed.meta[0].is_optional is False)

# Generated at 2022-06-13 19:58:48.248863
# Unit test for function parse
def test_parse():
    text = """
    Does the foo.
    :param x: X.
    :type x: int
    :param y: Y.
    :type y: int?
    :param z: Z.
      defaults to X + Y.
    :returns: A.
    """
    docstring = parse(text)
    assert docstring.short_description == "Does the foo."
    assert docstring.blank_after_short_description is True
    assert docstring.long_description is None
    assert docstring.blank_after_long_description is None
    assert docstring.meta[0].args == ["param", "x"]
    assert docstring.meta[1].args == ["type", "x"]
    assert docstring.meta[2].args == ["param", "y"]

# Generated at 2022-06-13 19:58:50.753525
# Unit test for function parse
def test_parse():
    # Raising an exception so that tests will fail.
    #assert False, "test_parse() needs unit tests"
    assert True, "test_parse() needs unit tests"

# Generated at 2022-06-13 19:59:01.702131
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()

    doc = parse("""
Hello, world!

:param foo: Bar.
""")
    assert doc.short_description == "Hello, world!"
    assert doc.blank_after_short_description is False
    assert doc.blank_after_long_description is False

    doc = parse("""
Hello, world!


:param foo: Bar.
""")
    assert doc.short_description == "Hello, world!"
    assert doc.blank_after_short_description is True
    assert doc.blank_after_long_description is False

    doc = parse("""
Hello, world!

This is a long description.

:param foo: Bar.
""")
    assert doc.short_description == "Hello, world!"
    assert doc.blank_after_short_description is False


# Generated at 2022-06-13 19:59:21.200586
# Unit test for function parse
def test_parse():
    input = """
    This function does stuff.
    
    :param x: The x value.
    :param y: The y value.
    :returns: The sum of x and y.
    """
    result = parse(input)
    assert (
        result.short_description
        == "This function does stuff."
    )
    assert (
        result.long_description
        == ""
    )
    assert (
        result.blank_after_long_description
        == False
    )
    assert (
        result.blank_after_short_description
        == True
    )
    assert (
        result.meta[0].description
        == "The x value."
    )
    assert (
        result.meta[0].arg_name
        == "x"
    )

# Generated at 2022-06-13 19:59:36.871933
# Unit test for function parse
def test_parse():

    assert parse("") == Docstring()
    assert parse("short") == Docstring(
        short_description="short",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )
    assert parse("short\n\nlong") == Docstring(
        short_description="short",
        long_description="long",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[],
    )
    assert parse("short\nlong") == Docstring(
        short_description="short",
        long_description="long",
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )

# Generated at 2022-06-13 19:59:43.415173
# Unit test for function parse
def test_parse():
    example_docstring = """
    This is a docstring with meta information.

    :param int foo: This is foo.
    """
    assert parse(example_docstring) == Docstring(short_description="This is a docstring with meta information.", blank_after_short_description=True, long_description=None, blank_after_long_description=False, meta=[DocstringParam(args=['param', 'int', 'foo'], description='This is foo.', arg_name='foo', type_name='int', is_optional=False, default=None)])
    pass # Yay!

# Generated at 2022-06-13 19:59:48.608920
# Unit test for function parse
def test_parse():
    test_string = '''
    test function
    :param int num: a number
    :type test_type
    :returns:
    '''

    doc = parse(test_string)
    print(doc)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:59:54.535126
# Unit test for function parse

# Generated at 2022-06-13 20:00:01.877141
# Unit test for function parse
def test_parse():
    doc = parse("""test function
    :param x: the function input parameter
    :return: the function output value
    :raise in case of error
    """)
    assert doc.short_description == "test function"
    assert doc.long_description is None
    assert doc.blank_after_short_description is False
    assert doc.blank_after_long_description is False
    assert len(doc.meta) == 3
    param_text = [param.description for param in doc.meta]
    assert param_text[0] == "the function input parameter"
    assert param_text[1] == "the function output value"
    assert param_text[2] == "in case of error"
    assert doc.meta[0].arg_name == "x"
    assert doc.meta[1].arg_name is None
    


# Generated at 2022-06-13 20:00:10.320384
# Unit test for function parse
def test_parse():
    x = parse("""hello
    here is a description of the function
    :param int x: the x value
    :returns int: the output of the function
    :raises Exception: if an error occurs
    """)
    assert x.short_description == "hello"
    assert x.long_description == "here is a description of the function"
    assert x.meta[0].arg_name == "x"
    assert x.meta[0].type_name == "int"
    assert x.meta[0].is_optional == False
    assert x.meta[1].type_name == "int"
    assert x.meta[1].is_generator == False

# Generated at 2022-06-13 20:00:21.805489
# Unit test for function parse
def test_parse():
    def test_fixture(f: Docstring):
        assert f.short_description is None
        assert f.long_description is None
        assert f.blank_after_short_description is True
        assert f.blank_after_long_description is True

# Generated at 2022-06-13 20:00:32.331544
# Unit test for function parse
def test_parse():
    """ Test the parsing of a ReST style docstring """
    def test():
        """ A function with a ReST style docstring
        :param test_input: the input parameter
        :type test_input: integer
        :returns:
        :rtype: none
        """
        pass

    docstring = parse(inspect.getdoc(test))
    assert docstring.short_description == "A function with a ReST style docstring"
    assert docstring.meta[0].param_name == "test_input"
    assert docstring.meta[0].type_name == "integer"


# Generated at 2022-06-13 20:00:33.418803
# Unit test for function parse
def test_parse():
    assert isinstance(parse("This is a test."), Docstring)


# Generated at 2022-06-13 20:00:44.214891
# Unit test for function parse
def test_parse():
    docstring = """Summary line.
    Extended description of function.

    :param arg1: Description of `arg1`
    :type arg1: str
    :param arg2: Description of `arg2`
    :type arg2: int, optional
    :returns: Description of return value.
    :rtype: bool
    :raises keyError: We miscalculated our value
    :raises ImportError: We couldn't find the module we tried to import

    """
    d = parse(docstring)

    assert(d.short_description == "Summary line.")
    assert(d.long_description == "Extended description of function.")
    assert(d.blank_after_short_description == True)
    assert(d.blank_after_long_description == False)


# Generated at 2022-06-13 20:00:54.839028
# Unit test for function parse
def test_parse():
    A = DocstringParam(
        args=['param', 'x:', 'name'],
        description='param name:\n    short description\n    \n    long description',
        arg_name='name',
        type_name='x',
        is_optional=False,
        default=None,
    )
    B = DocstringParam(
        args=['param', 'x?:', 'name2'],
        description='param name2?:\n    short description\n    \n    long description',
        arg_name='name2',
        type_name='x',
        is_optional=True,
        default=None,
    )

# Generated at 2022-06-13 20:01:03.568289
# Unit test for function parse

# Generated at 2022-06-13 20:01:07.040427
# Unit test for function parse
def test_parse():
    docstring = """
        This is my awesome docstring.

        Args:
            x (list[int]): The first parameter.

        Raises:
            RuntimeError: If no data was found.

        Returns:
            pandas.DataFrame: [description]

        Yields:
            str: [description]
    """
    res = parse(docstring)
    assert res

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 20:01:15.809955
# Unit test for function parse
def test_parse():
    test_str = """
    This is a test.

    :param a: type is int
    :rtype: int
    :raises AttributeError:
    """

# Generated at 2022-06-13 20:01:18.278792
# Unit test for function parse
def test_parse():
    ret = parse(
        """Test function.
    :param str arg1: This is the first parameter
    :returns: Description of return
    :raises KeyError: raises an exception
    :raises ValueError: does not raise an exception
    """
    )
    print(ret)
    return

test_parse()

# Generated at 2022-06-13 20:01:27.494914
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    text = """
    This is a short description that only has one line.

    This is short description that has two lines.

    This is a long description that only has one line.

    This is a long description that has two lines.

    :param int/float x:
        a

        b

    :param str y:
    :param Union[int, float] z:
    :param Optional[bool] b:
        c
    :returns int:
    :returns Optional[float]:
    :raises ValueError:
    :raises KeyError:
    :raises Optional[Exception]:
    """
    docstr = parse(text)
    assert docstr.short_description == "This is a short description that only has one line."

# Generated at 2022-06-13 20:01:39.851790
# Unit test for function parse
def test_parse():
    text = '''
    This is a sample docstring.

    :param a: First parameter
    :param b: Second parameter
    :param c?: Third parameter
    :returns: The return value
    :raises: exception1, exception2
    '''
    doc = parse(text)
    assert doc.short_description == 'This is a sample docstring.'
    assert doc.blank_after_short_description
    assert doc.long_description == None
    assert doc.blank_after_long_description
    assert len(doc.meta) == 3
    assert doc.meta[0] == DocstringParam(args=['param', 'a', 'First'], description='parameter')
    assert doc.meta[1] == DocstringParam(args=['param', 'b', 'Second'], description='parameter')

# Generated at 2022-06-13 20:01:50.198679
# Unit test for function parse
def test_parse():
    assert Docstring() == parse("")
    assert Docstring() == parse("   \n \n \n ")
    assert Docstring() == parse("\n\n\n")

    assert Docstring(
        short_description="Foo",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description="Bar",
    ) == parse(
        """
    Foo

    Bar"""
    )

    assert Docstring(
        short_description="Foo",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description="Bar",
    ) == parse(
        """
    Foo
    Bar"""
    )
