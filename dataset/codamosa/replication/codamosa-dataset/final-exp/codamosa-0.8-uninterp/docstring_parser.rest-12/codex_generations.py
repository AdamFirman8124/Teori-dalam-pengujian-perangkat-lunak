

# Generated at 2022-06-13 19:52:09.929843
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()
    assert parse("Hello.") == Docstring(
        short_description="Hello.",
        long_description=None,
        blank_after_short_description=True,
        blank_after_long_description=True,
        meta=[],
    )
    assert parse("Hello.\n") == Docstring(
        short_description="Hello.",
        long_description=None,
        blank_after_short_description=True,
        blank_after_long_description=True,
        meta=[],
    )
    assert parse("Hello.\n\n") == Docstring(
        short_description="Hello.",
        long_description=None,
        blank_after_short_description=True,
        blank_after_long_description=True,
        meta=[],
    )

# Generated at 2022-06-13 19:52:17.002700
# Unit test for function parse
def test_parse():
    text_1 = """
    Write to a file
    :param path: The path to write to
    :param content: The content to write
    """
    result = parse(text_1)
    assert result.short_description == "Write to a file"
    assert result.long_description is None
    assert result.blank_after_short_description is False
    assert result.blank_after_long_description is False

# Generated at 2022-06-13 19:52:24.926999
# Unit test for function parse
def test_parse():
    doc = parse(
        """\
        Short description.

        Long description.

        :param type_name arg_name: parameter description.
        :param str arg_name: parameter description.
        :param type_name arg_name: parameter description.
        :param type_name arg_name: parameter description.

        :return: return value description.
        :rtype: str
        :yields type_name: yields description.
        :yields: yields description.
        :raises ValueError: if something bad happens.
        :raises: if something bad happens.
        """
    )

    assert doc.short_description == "Short description."
    assert doc.long_description == "Long description."
    assert doc.blank_after_short_description
    assert doc.blank_after_long_description


# Generated at 2022-06-13 19:52:34.810879
# Unit test for function parse
def test_parse():
    text = """\
    Short description.
    Long description.
    :param x: A positional argument.
    :param y: A keyword argument.
    """
    ds = parse(text)
    assert ds.short_description == "Short description."
    assert ds.long_description == "Long description."
    assert len(ds.meta) == 2
    assert ds.meta[0].description == "A positional argument."
    assert ds.meta[0].type_name is None
    assert ds.meta[0].is_optional is None
    assert ds.meta[0].default is None
    assert ds.meta[1].description == "A keyword argument."
    assert ds.meta[1].type_name is None
    assert ds.meta[1].is_optional is None

# Generated at 2022-06-13 19:52:46.117423
# Unit test for function parse
def test_parse():
    dstring = r'''
        This is the short description.

        And now the long description. It should also be indented.
        And can span multiple lines as well.

        :param int foo: Foo is the first argument.
        :param int bar: Bar is the second argument.
        :param int baz? defaults to 42.
        :returns: Something.
        :rtype: int
        :raises ValueError: If something bad happened.

        :param str foo: Foo is the first argument.
        :param str bar: Bar is the second argument.
        :returns: Something.
        :rtype: str
        :raises ValueError: If something bad happened.
    '''


# Generated at 2022-06-13 19:52:49.316419
# Unit test for function parse
def test_parse():
    """Testing for parse"""
    doc = """this is a test
    :param x: x description
    :type x: int
    :param y: test description
    :type y: str
    :return: return descriptions
    :rtype: int
    :raises ValueError: test error
    :raises TypeError: test error
    """
    print(parse(doc))

# Generated at 2022-06-13 19:52:55.011425
# Unit test for function parse
def test_parse():
    text = """
        Create a new list with a copy of the first element added to the beginning.

        :param list list: The list to copy and add to.

        :param element element: The element to add to the new list.

        :returns: The newly created list.

        :raises NoSuchElementException: If the element does not exist.
    """
    doc_str = parse(text)

    assert doc_str.short_description == 'Create a new list with a copy of the first element added to the beginning.'
    assert doc_str.long_description == 'The newly created list.'
    assert doc_str.blank_after_short_description == True
    assert doc_str.blank_after_long_description == False
    assert doc_str.meta[2].arg_name == 'list'

# Generated at 2022-06-13 19:53:06.915382
# Unit test for function parse
def test_parse():
    code = """Hello world.

    This is a longer description.

    :param str p1: This is p1.
    :param p2: This is p2.
    :param p3: This is p3.
    :returns: This is the return value.
    :raises ValueError: This is a ValueError.
    """
    docstring = parse(code)
    # assert str(docstring) ==
    #     "Hello world.\n\nThis is a longer description.\n\n"
    #     ":param str p1: This is p1.\n"
    #     ":param p2: This is p2.\n"
    #     ":param p3: This is p3.\n"
    #     ":returns: This is the return value.\n"
    #

# Generated at 2022-06-13 19:53:08.361254
# Unit test for function parse
def test_parse():
    assert(parse("")) == parse("")

# Generated at 2022-06-13 19:53:18.427789
# Unit test for function parse
def test_parse():
    docstring = parse("""
    Dummy function

    :param a:  hello
    :type a: str
    :param b:  world
    :type b: str
    :param c:  !
    :type c: str
    :return: str
    :rtype: str
    :raises TypeError
    """)

    assert docstring.short_description == "Dummy function"
    assert docstring.long_description == None

    assert len(docstring.meta) == 4
    assert docstring.meta[0].args == ["param", "a"]
    assert docstring.meta[0].description == "hello"
    assert isinstance(docstring.meta[0], DocstringParam)
    assert docstring.meta[1].args == ["type", "a"]

# Generated at 2022-06-13 19:53:29.826030
# Unit test for function parse
def test_parse():
    docstring = """
    Parse the ReST-style docstring into its components.

    :returns: parsed docstring
    :rtype: Docstring
    """
    docstring_parsed = parse(docstring)
    print(docstring_parsed)


# Generated at 2022-06-13 19:53:37.763718
# Unit test for function parse
def test_parse():
    """Test for parse"""
    docstring = """
    Hello this is a docstring
    with multiple lines.

    :param foo: This is foo.
    :param bar: This is bar.
    :returns: This is returns
    :raises Exception: This is raises
    :yields: This is yields
    :returns int: This is returns with type
    :raises Exception int: This is raises with type
    :yields str: This is yields with type
    :returns int: This is returns with type

    """
    ret = parse(docstring)
    assert ret.short_description == "Hello this is a docstring\nwith multiple lines."
    assert len(ret.meta) == 9
    assert ret.meta[0].arg_name == "foo"

# Generated at 2022-06-13 19:53:50.268565
# Unit test for function parse

# Generated at 2022-06-13 19:53:59.462312
# Unit test for function parse
def test_parse():
    def func(a: str) -> int:
        """Calculates some stuff.

        :param a: The arg.
        :type a: str
        :yields: int

        """
        return 1

    print(parse(func.__doc__))
    func = """Calculates some stuff.
    
    :param a: The arg.
        :type a: str
    :yields: int
    
    """
    print(parse(func))

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:54:07.745008
# Unit test for function parse
def test_parse():
    def func():
        """Short description.

        long description.

        This is the long description.

        :param arg1: description of arg1
        :type arg1: int
        :type arg2: str
        :param arg2: description of arg2
        :type arg2: str
        :param arg3: description of arg3. defaults to 2.
        :type arg3: int
        :param arg4: description of arg4
        :type arg4: int
        :raises ValueError: if something bad happens
        :returns: int -- the return value

        :sometag: value for sometag
        """

# Generated at 2022-06-13 19:54:18.900790
# Unit test for function parse

# Generated at 2022-06-13 19:54:27.394930
# Unit test for function parse
def test_parse():
    import sys
    import types
    import unittest
    import textwrap

    def function():
        """Short description.

        Long description.

        :param arg_name:
            Argument description.
        :type arg_name: str
        :param arg_name2: Argument description.
        :type arg_name2: str
        :returns: True for success.
        :rtype: bool
        :raises ValueError: if something bad happened.
        """
        pass


# Generated at 2022-06-13 19:54:38.845792
# Unit test for function parse
def test_parse():
    docstring = """\
    Short description.

    A much longer description with two lines.

    :param arg1: Description of arg1.
    :param arg2: Description of arg2.
    :type arg1: str
    :type arg2: str
    :returns: Description of the return value.
    :rtype: int
    """
    parsed = parse(docstring)
    assert parsed.short_description == "Short description."
    assert parsed.blank_after_short_description is False
    assert parsed.long_description == "A much longer description with two lines."
    assert parsed.blank_after_long_description is False
    assert len(parsed.meta) == 3
    meta = parsed.meta
    assert isinstance(meta[0], DocstringParam)
    assert isinstance(meta[1], DocstringParam)

# Generated at 2022-06-13 19:54:46.674520
# Unit test for function parse
def test_parse():

    # not ReST style
    text = "Docstring: doc for a function"
    ret1 = parse(text)
    assert ret1.short_description == "Docstring"

    # ReST style
    text = "Docstring:\n\ndoc for a function\n"
    ret2 = parse(text)
    assert ret2.short_description == "Docstring"
    assert ret2.long_description == "doc for a function"

# Generated at 2022-06-13 19:54:59.442438
# Unit test for function parse
def test_parse():
    key1 = "Returns:"
    type1 = "integer"
    arg1 = None
    desc1 = "Description for first line"
    key2 = "Raises:"
    type2 = "Exception"
    arg2 = None
    desc2 = "Description for second line"
    key3 = "Args:"
    type3 = "int"
    arg3 = "first"
    desc3 = "Description for third line"

    doc_string = "Short description\n\n" + key1 + " " + type1 + " " + desc1 + "\n" + key2 + " " + type2 + " " + desc2 + "\n" + key3 + " " + type3 + " " + arg3 + "." + desc3

    parsed = parse(doc_string)
    assert isinstance(parsed, Docstring)
   

# Generated at 2022-06-13 19:55:10.292090
# Unit test for function parse
def test_parse():
    """ Test function parse """
    docstring_text = """A function to extract returns from a docstring.
    Args:
        meta (list): List of DocstringMeta objects to filter.

    Returns:
        list: Filtered list of DocstringMeta objects.
    """
    ret = parse(docstring_text)
    print(ret)
    return ret


# Generated at 2022-06-13 19:55:16.611107
# Unit test for function parse
def test_parse():
    """
    Unit test for function parse
    """
    text = """Test docstring

    :param int arg: Description
    :returns: Description
    """
    doc = parse(text)
    assert len(doc.meta) == 2
    assert doc.meta[0].key == "param"
    assert doc.meta[0].type_name == "int"
    assert doc.meta[0].arg_name == "arg"
    assert doc.meta[1].key == "returns"

# Generated at 2022-06-13 19:55:26.632456
# Unit test for function parse
def test_parse():
    print("*"*80)
    print(parse.__name__)
    print("*"*80)

    class F:
        """
        Does a bit of math.

        Here's some description of the function that
        spans multiple lines.

        :param x: first parameter
        :type x: int
        :param y: second parameter
        :type y: int
        :param z: third parameter
        :type z: str
        :returns: the result
        :rtype: float
        :raises: TypeError
        """

    import pprint
    pprint.pprint(parse(inspect.getdoc(F)))

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:55:38.170622
# Unit test for function parse
def test_parse():
    # Test empty docstring
    assert parse("").short_description == None
    assert parse("").long_description == None
    assert not parse("").meta

    assert parse("    ").short_description == None
    assert parse("    ").long_description == None
    assert not parse("    ").meta

    # Test normal docstring without meta information
    docstring = """Sum of two numbers.

    This is a long description.
    """
    assert parse(docstring).short_description == "Sum of two numbers."
    assert (
        parse(docstring).long_description
        == "This is a long description."
    )
    assert repr(parse(docstring).meta) == repr([])

    docstring = """Sum of two numbers."""
    assert parse(docstring).short_description == "Sum of two numbers."
    assert parse

# Generated at 2022-06-13 19:55:50.673239
# Unit test for function parse

# Generated at 2022-06-13 19:55:59.113341
# Unit test for function parse
def test_parse():
    assert not parse("")
    assert parse("Test.").short_description == "Test."
    assert parse("Test.\n").short_description == "Test."
    assert parse(" Test.\n\t ").short_description == " Test.\n\t "
    assert parse("Test.\n\nAnother")
    assert parse("Test.\n\nAnother!").short_description == "Test."
    assert parse("Test.\n\nAnother!").long_description == "Another!"
    assert parse("Test.\n\n\nAnother!").long_description == "Another!"
    assert parse("Test.\n\n\nAnother!").blank_after_long_description == True
    assert parse("\nTest.\n\n\nAnother!\n\n\n")

# Generated at 2022-06-13 19:56:15.323845
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()
    assert parse("Hello.").short_description == "Hello."

    assert parse("Hello.\n   There.\n     General.").short_description == "Hello."
    assert parse("Hello.\n   There.\n     General.") == Docstring(
        short_description="Hello.",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description="There.\nGeneral.",
        meta=[],
    )
    assert parse("Hello.\n\n   There.\n     General.") == Docstring(
        short_description="Hello.",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description="There.\nGeneral.",
        meta=[],
    )
   

# Generated at 2022-06-13 19:56:25.048958
# Unit test for function parse
def test_parse():
    """Test docstring parsing."""
    ds = Docstring()
    ds.short_description = "This is a test."
    ds.blank_after_short_description = False
    ds.long_description = "More information here."
    ds.blank_after_long_description = True
    ds.meta.append(DocstringMeta(args=[":rtype:"], description="int"))
    ds.meta.append(DocstringRaises(args=[":raises:", "ValueError"], description="If something is wrong."))
    ds.meta.append(DocstringParam(args=[":param", "str", "name"], description="The name of a thing."))
    ds.meta.append(DocstringParam(args=[":param", "str", "name?"], description="The name of a thing (optional)."))

# Generated at 2022-06-13 19:56:34.804340
# Unit test for function parse
def test_parse():
    text = """\
        Short description.

        Long description.

        :param a: A param.
        :type a: int
        :param b: Another param.
        :type b: str

        :returns: a string
        :rtype: str
        """

# Generated at 2022-06-13 19:56:47.014303
# Unit test for function parse
def test_parse():
    text = """
    Test parse.

    :param arg: Test argument.
    :returns: Nothing
    :raises Exception: Exception
    """
    docstring = parse(text)
    assert docstring.short_description == "Test parse."
    assert docstring.meta[0] == DocstringParam(
        args=["param", "arg"],
        description="Test argument.",
        type_name=None,
        is_optional=None,
        default=None,
    )
    assert docstring.meta[1] == DocstringReturns(
        args=["returns"], description="Nothing", type_name=None
    )
    assert docstring.meta[2] == DocstringRaises(
        args=["raises", "Exception"], description="Exception", type_name="Exception"
    )


# Generated at 2022-06-13 19:57:12.141879
# Unit test for function parse
def test_parse():
    assert parse("""
        Short description.

        Longer description.

        :param str arg_name: description
    """) == Docstring(
        short_description="Short description.",
        long_description="Longer description.",
        blank_after_short_description=True,
        blank_after_long_description=True,
        meta=[DocstringParam(args=["param", "str", "arg_name"], description="description", arg_name="arg_name", type_name="str", is_optional=False, default=None)],
    )


# Generated at 2022-06-13 19:57:13.536970
# Unit test for function parse
def test_parse():
    return parse(inspect.cleandoc(parse.__doc__))

# Generated at 2022-06-13 19:57:26.334592
# Unit test for function parse
def test_parse():
    # test docstring with all possible docstrings
    long_desc = "Long description\nOn multiple lines and also contains:\n    def class(self):\n        pass\n"
    docstring = parse("Short description\n\n" + long_desc + ":param x: parameter x\n:param y: parameter y\n:return: returns\n:returns: returns\n:returns type: return type\n\n:raises Exception: raises exception\n\n:rtype: return type\n\n:type x: type of x\n:yields: yields\n")
    assert docstring.short_description == "Short description"
    assert docstring.blank_after_short_description == True
    assert docstring.long_description == long_desc
    assert docstring.blank_after_long_description == True


# Generated at 2022-06-13 19:57:34.458058
# Unit test for function parse
def test_parse():
    assert parse('This is a docstring.\nIt doesn\'t quite work currently.') == \
        Docstring(short_description='This is a docstring.',
                  long_description='It doesn\'t quite work currently.',
                  meta=[])
    assert parse('This is a docstring.\n\nIt doesn\'t quite work currently.') == \
        Docstring(short_description='This is a docstring.',
                  long_description='It doesn\'t quite work currently.',
                  meta=[])

# Generated at 2022-06-13 19:57:48.534161
# Unit test for function parse
def test_parse():
    print("Testing function `parse`")
    from pprint import pprint as pp
    from io import StringIO
    from types import SimpleNamespace

    def test_case(
        text,
        expected_short_desc,
        expected_long_desc,
        expected_blank_after_short_desc,
        expected_blank_after_long_desc,
        expected_meta,
        expected_first_param_index,
    ):
        text = text.strip().replace('"""', "").replace('"""', "")


# Generated at 2022-06-13 19:57:52.720974
# Unit test for function parse
def test_parse():
    docstring = """Summary line.
    Extended description of function.

    :param arg1: Description of arg1
    :param arg2: Description of arg2
    :returns: Description of return value.
    :raises Exception: Description of exception.

    """

    doc = parse(docstring)
    assert doc.short_description == "Summary line."
    assert doc.long_description == "Extended description of function."
    assert doc.blank_after_short_description is True
    assert doc.blank_after_long_description is False
    assert len(list(doc.meta)) == 3

# Generated at 2022-06-13 19:58:04.633623
# Unit test for function parse
def test_parse():
    docstr = """
    This function returns nothing.

    :param arg1: this is first argument
    :param arg2: this is second argument
    :return: nothing
    """
    ret = parse(docstr)
    assert isinstance(ret, Docstring)
    assert ret.short_description == 'This function returns nothing.'
    assert ret.long_description == 'nothing'
    assert ret.blank_after_short_description == True
    assert ret.blank_after_long_description == False

    assert len(ret.meta) == 2
    assert isinstance(ret.meta[0], DocstringParam)
    assert isinstance(ret.meta[1], DocstringReturns)
    assert ret.meta[0].arg_name == 'arg1'
    assert ret.meta[0].type_name == None

# Generated at 2022-06-13 19:58:16.441664
# Unit test for function parse
def test_parse():

    # Test function with no docstring
    def test_0():
        pass

    docstring = parse(inspect.getdoc(test_0))
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert len(docstring.meta) == 0

    # Test function with short description
    def test_1():
        """Short description"""

    docstring = parse(inspect.getdoc(test_1))
    assert docstring.short_description == 'Short description'
    assert docstring.long_description is None
    assert len(docstring.meta) == 0

    # Test function with long description
    def test_2():
        """Short description

        Long description.
        """

    docstring = parse(inspect.getdoc(test_2))

# Generated at 2022-06-13 19:58:26.913907
# Unit test for function parse

# Generated at 2022-06-13 19:58:37.322498
# Unit test for function parse
def test_parse():
    docstring = """This is a docstring.
    """
    assert parse(docstring).short_description == 'This is a docstring.'

    docstring = """This is a docstring.
    This is a long description.
    """
    assert parse(docstring).short_description == 'This is a docstring.'
    assert parse(docstring).long_description == 'This is a long description.'
    assert parse(docstring).blank_after_short_description == True
    assert parse(docstring).blank_after_long_description == False

    docstring = """This is a docstring.
    This is a long description.

    """
    assert parse(docstring).short_description == 'This is a docstring.'
    assert parse(docstring).long_description == 'This is a long description.'
    assert parse(docstring).blank_

# Generated at 2022-06-13 19:59:22.441800
# Unit test for function parse
def test_parse():
    docstring = parse("""
        This is a docstring.

        This is a blank line

        :param name: Name of the person
        :type name: str
        :param city: The city of the person
        :type city:  str
        :default city: 'London'
        :returns: Full name
        :rtype: str
    """)

    assert docstring.short_description == "This is a docstring."
    assert docstring.long_description == "This is a blank line"
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description

    for arg in docstring.meta:
        if arg.arg_name == "name":
            assert arg.type_name == "str"
            assert arg.is_optional is None
            assert arg.default is None


# Generated at 2022-06-13 19:59:32.540715
# Unit test for function parse

# Generated at 2022-06-13 19:59:42.612562
# Unit test for function parse
def test_parse():
    docstring = 'This is a test docstring \n of type ReST \n \n :param a: test_argument \n :type a: str \n :param b: test_argument \n :type b: int \n :param c: optional argument with a default \n :type c: str \n :default c: this is the default value \n :param d?: optional argument \n :type d?: int \n :returns: the output of this function \n :rtype: tuple: (str, int) \n :yields: the output of this generator \n :ytype: (str, int) \n :raises MyError: if there is a problem \n :exception MyError: if there is a problem'
    parsed_docstring = parse(docstring)
    assert parsed_docstring is not None

# Generated at 2022-06-13 19:59:54.773125
# Unit test for function parse
def test_parse():
    docstring_test = """
    This is a sentence.
    :param int a: This is another sentence.
    :param int b: This is a sentence that
    spans multiple lines.
    :returns: A value of variable b.
    """
    docstring = parse(docstring_test)

# Generated at 2022-06-13 20:00:01.991000
# Unit test for function parse
def test_parse():
    '''
    Test cases:
    Parse correctly:
    - short and long descriptions
    - multiple and single meta information
    Parse incorrectly:
    - raise errors 
    '''

# Generated at 2022-06-13 20:00:12.893199
# Unit test for function parse

# Generated at 2022-06-13 20:00:23.025103
# Unit test for function parse
def test_parse():
    import inspect

    class TestDocs:
        def test1(self, bar=1, baz=None):
            """
            This is the short description.

            This is the long description.

            :param bar: This is the description of the ``bar`` parameter.
            :type bar: int
            :param baz: This is the description of the ``baz`` parameter.
            :type baz: str
            :returns: description of return value
            :rtype: int
            :raises ValueError: description of exception
            :raises Exception: description of exception
            """

        def test2(self):
            """Short description

            This is the long description.

            :returns: description of return value
            :rtype: int
            """


# Generated at 2022-06-13 20:00:31.782890
# Unit test for function parse
def test_parse():
    text = '''
    parse ReST-style docstring into its components.

    :returns: parsed docstring
    :raises: an error if the parsing failed
    '''
    assert parse(text).short_description == 'parse ReST-style docstring into its components.'
    assert parse(text).long_description == 'an error if the parsing failed'
    assert parse(text).meta[0].description == 'parsed docstring'
    assert parse(text).meta[1].description == 'an error if the parsing failed'


# Generated at 2022-06-13 20:00:42.938713
# Unit test for function parse
def test_parse():
    assert repr(parse("")) == repr(
        Docstring(
            short_description=None,
            blank_after_short_description=False,
            blank_after_long_description=False,
            long_description=None,
            meta=[],
        )
    )
    assert repr(parse("\n")) == repr(
        Docstring(
            short_description=None,
            blank_after_short_description=False,
            blank_after_long_description=False,
            long_description=None,
            meta=[],
        )
    )

# Generated at 2022-06-13 20:00:53.017528
# Unit test for function parse
def test_parse():
    docstring = parse("""
    This is my docstring
                        :param  str  first_arg:  First argument
                        :param str second_arg = 'foo':  Second argument

    This is the description
                       :param str third_arg: This is the third arg.
                     :type third_arg: str
    :raises: ValueError


    """)

    assert docstring.short_description == "This is my docstring"
    assert docstring.blank_after_short_description == True
    assert docstring.long_description == "This is the description"
    assert docstring.blank_after_long_description == False

    meta = docstring.meta
    assert len(meta) == 4
    assert isinstance(meta[0], DocstringParam) and meta[0].arg_name == "first_arg"
    assert isinstance

# Generated at 2022-06-13 20:01:18.307111
# Unit test for function parse
def test_parse():
    """Unit test for function parse."""
    assert (
        "short description" == parse("short description").short_description
    )
    assert (
        "long description" == parse("short description\n\nlong description").long_description
    )
    assert (
        "long description" == parse("short description\nlong description").long_description
    )
    assert (
        "long description" == parse("short description\n\nlong description").long_description
    )

# Generated at 2022-06-13 20:01:27.495557
# Unit test for function parse

# Generated at 2022-06-13 20:01:29.382042
# Unit test for function parse

# Generated at 2022-06-13 20:01:41.012835
# Unit test for function parse
def test_parse():
    assert parse(" ") == Docstring()


# Generated at 2022-06-13 20:01:51.028896
# Unit test for function parse
def test_parse():
    print("Testing the parse function")
    docstring = parse("""\
    Test the parse function.

    :param a: First parameter.
    :type a: int
    :param b: Second parameter.
    :type b: string
    :returns: Return value.
    :rtype: string
    :raises ImportError: Exception.
    :raises ValueError: Exception.
    """)
    print("Short description: {}".format(docstring.short_description))
    print("Long description: {}".format(docstring.long_description))
    print("Blank after short description: {}".format(
        docstring.blank_after_short_description))
    print("Blank after long description: {}".format(
        docstring.blank_after_long_description))
    print("Meta:")