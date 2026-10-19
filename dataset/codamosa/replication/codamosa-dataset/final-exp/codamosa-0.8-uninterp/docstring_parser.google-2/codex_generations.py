

# Generated at 2022-06-13 19:31:41.017898
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    g=GoogleParser()
    docstring = g.parse("""
        A sample docstring.

        Some more text.

        Args:
            a: a sample argument
            b (int): another sample argument
            c (bool, optional): a third sample argument
              This argument has a multi-line description.

        Raises:
            A sample exception.

        Examples:
            Some example code.

        Returns:
            A sample return value.
            Another sample return value.

        Yields:
            A sample return value.

        Attributes:
            a: A sample attribute.

        """)
    print(docstring)
    assert docstring.short_description == "A sample docstring."
    assert docstring.long_description == "Some more text."
    assert docstring.blank_after_short_description
    assert docstring.blank

# Generated at 2022-06-13 19:31:49.877354
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # No such parser
    assert parse('Hello world.') == Docstring(meta=[DocstringMeta(args=['desc'], description='Hello world.')])
    # No such parser, but with indent
    assert parse('  Hello world.') == Docstring(meta=[DocstringMeta(args=['desc'], description='Hello world.')])
    # No such parser, but with blank line
    assert parse('\nHello world.') == Docstring(meta=[DocstringMeta(args=['desc'], description='Hello world.')])
    # No such parser, but with blank line at last
    assert parse('Hello world.\n') == Docstring(meta=[DocstringMeta(args=['desc'], description='Hello world.')])
    # No such parser, but with indent and blank line
    assert parse('  \nHello world.') == Doc

# Generated at 2022-06-13 19:32:00.689982
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """
    Unit test for method parse of class GoogleParser
    """

    assert(parse("") == Docstring())
    assert(parse("\n") == Docstring())
    assert(parse("\n\n") == Docstring())

    assert(parse("a") == Docstring("a", None, False, False))
    assert(parse("a\n") == Docstring("a", None, False, True))
    assert(parse("a\n\n") == Docstring("a", None, True, False))
    assert(parse("a\n\n\n") == Docstring("a", None, True, True))
    assert(parse("a\n\nb") == Docstring("a", "b", False, True))
    assert(parse("a\n\nb\n") == Docstring("a", "b", True, True))

# Generated at 2022-06-13 19:32:06.011922
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = \
    """Docstring to test.
    
    One line.
    
    :param arg_1: arg1 description
    :param arg_2: arg2 description
    :param arg_3 (int): arg3 description
    :param arg_4 (str, optional): arg4 description
    :param arg_5 (bool?): arg5 description
    :param arg_6 (None): arg6 description. Defaults to None.
    :type arg_6: None
    :param arg_7 (int): arg7 description. Defaults to 1.
    :raises err: err description
    :returns: return description
    :yields: yield description
    """
    d = parse(text)
    assert d.short_description == "Docstring to test."
    assert d.blank_after_short_description

# Generated at 2022-06-13 19:32:16.524955
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    print("parse")

# Generated at 2022-06-13 19:32:21.404351
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import doctest

    g_parser = GoogleParser()
    g_parser.add_section(Section("Reference", "references", SectionType.MULTIPLE))
    g_parser.add_section(Section("Note", "notes", SectionType.SINGULAR))

    result = doctest.testmod()
    assert result.failed == 0

# Generated at 2022-06-13 19:32:26.370835
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """\
    This is a test docstring.

    Args:
        param1 (str): The first parameter.
        param2 (str): The second parameter.

    Returns:
        str: The return value. True for success, False otherwise.
    """
    s = parse(text)
    assert s.short_description == "This is a test docstring."
    assert s.long_description == None
    assert s.blank_after_short_description == True
    assert s.blank_after_long_description == False

# Generated at 2022-06-13 19:32:27.516742
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("Hello, world.") == Docstring(short_description="Hello, world.")



# Generated at 2022-06-13 19:32:39.483602
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Test method parse() of class GoogleParser."""
    # Test default sections
    doc = inspect.cleandoc(
        """
    Test function.

    Params:

    arg1 (int): Argument 1.
    arg2 (int): Argument 2. Defaults to 3.

    Raises:

    Error: Something went wrong.

    Returns:

    int: The sunshine.
    """
    )
    parsed = parse(doc)
    assert parsed.short_description == "Test function."
    assert parsed.long_description is None
    assert parsed.blank_after_short_description is True

# Generated at 2022-06-13 19:32:48.853332
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import sphinx
    import mock
    P = GoogleParser()
    # Test empty
    expected = Docstring()
    docstr = P.parse('')
    assert docstr == expected
    # Test only short
    expected.short_description = "Test short"
    docstr = P.parse('Test short')
    assert docstr == expected
    # Test void long
    expected.blank_after_short_description = True
    expected.long_description = None
    docstr = P.parse('Test short\n\n')
    assert docstr == expected
    # Test short and long
    expected.blank_after_short_description = False
    expected.long_description = 'Test long'
    expected.blank_after_long_description = True
    docstr = P.parse('Test short\nTest long\n\n')

# Generated at 2022-06-13 19:33:06.462182
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    test_string = """This is a test string for parse.
    Testing edge cases:
    Arguments:
        arg1: Here is a description for arg1.
        arg2: Here is a description for arg2.
        arg3 (str): Here is a description for arg3 with type.
    Returns:
        str: Here is a description for returns.
    """
    assert GoogleParser().parse(test_string).meta[0] == DocstringParam(
        args=['param', 'arg1'],
        description='Here is a description for arg1.',
        arg_name='arg1',
        type_name=None,
        is_optional=None,
        default=None,
    )

# Generated at 2022-06-13 19:33:12.092388
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Unit: E1, E2
    assert parse("GoogleParser") == parse("GoogleParser\n")
    assert parse("GoogleParser:(\n"
                 "\tdef parse(self, text: str) -> Docstring: pass\n)") == parse("GoogleParser:(\n"
                                                                                  "\tdef parse(self, text: str) -> Docstring: pass\n)\n")

# Generated at 2022-06-13 19:33:21.189927
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """
    method parse of class GoogleParser
    """
    # Setup
    text = inspect.cleandoc("""
    This is a docstring with some parameters.

    Args:
        first_param (int): the first parameter. Defaults to 42.
        second_param (int): the second parameter. Defaults to 42.

    Returns:
        int: the sum of the two parameters.
    """)

# Generated at 2022-06-13 19:33:31.521775
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
        Args:
            a: a
            b (optional): b
            c (bool): c
            d (:obj:`int`): d
        Returns:
            :obj:`bool`
        Raises:
            :obj:`ValueError`: if not valid
        """
    ret = GoogleParser().parse(text)
    assert ret is not None
    assert ret.short_description is None
    assert ret.long_description is None
    assert ret.blank_after_short_description is False
    assert ret.blank_after_long_description is False
    assert len(ret.meta) == 4
    assert ret.meta[0] is not None
    assert ret.meta[0].args == ["param", "a"]
    assert ret.meta[0].description == "a"
    assert ret.meta

# Generated at 2022-06-13 19:33:45.318769
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Set of tests for _build_single_meta
    def test_single_meta(self, input_str, key, args, desc):
        section = Section("title", key, SectionType.SINGULAR)
        result = self._build_single_meta(section, input_str)
        if args:
            self.assertEqual(result.args, args)
        else:
            self.assertEqual(result.args, ["title"])
        if desc:
            self.assertEqual(result.description, desc)
        else:
            self.assertEqual(result.description, input_str)
        if key == "return":
            self.assertEqual(result.type_name, None)
        elif key == "param":
            raise ParseError("Expected paramenter name.")

# Generated at 2022-06-13 19:33:50.501784
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    d = "hello world"
    expected = Docstring()
    expected.short_description = "hello world"
    expected.blank_after_short_description = False
    assert GoogleParser().parse(d) == expected

if __name__ == "__main__":
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:33:57.756786
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text="\n    Arguments:\n    ------\n    a : int\n        A integer number.\n    b : str\n        A string.\n    \n    Returns:\n    ------\n    str\n        Sum of a and b.\n    "
    assert str(GoogleParser().parse(text)) == "a : int\n        A integer number.\n    b : str\n        A string.\n    \n    str\n        Sum of a and b."


# Generated at 2022-06-13 19:34:09.032315
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:34:15.170146
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import DocstringParam, DocstringReturns, DocstringRaises
    parser = GoogleParser()

    doc = """
    Short summary.

    Longer summary.

    Args:
        name (str): Name of the staff. Defaults to None.
        age (int, optional): Age of the staff.
        salary (str?): Salary of the staff.

    Returns:
        str: Return value. Defaults to None.
          Return value description.

    Raises:
        Exception: Error description.

    """
    result = parser.parse(doc)
    assert (
        result.short_description == "Short summary."
    ), result.short_description

# Generated at 2022-06-13 19:34:25.442327
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    # Test basic parsing.
    text = """short desc

    long desc
    """

    doc = parse(text)
    assert doc.short_description == "short desc"
    assert doc.long_description == "long desc"

    # Test parameter parsing.
    text = """short desc

    long desc

    Args:
        arg1 (str): description.
        arg2 (int): description.
    """

    doc = parse(text)
    assert doc.short_description == "short desc"
    assert doc.long_description == "long desc"
    assert len(doc.meta) == 2
    assert doc.meta[0].args == ["Args", "arg1 (str): description."]
    assert doc.meta[0].arg_name == "arg1"
    assert doc.meta[0].type_name == "str"

# Generated at 2022-06-13 19:34:37.412377
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # test case 1
    # single return
    lines = "Hello world"
    expected_returns = Docstring(short_description=lines, long_description=None)
    actual_returns = parse(lines)
    assert actual_returns == expected_returns

    # test case 2
    # multiple returns
    lines = "Hello world\n\n     aaa\n     bbb\n"
    expected_returns = Docstring(short_description='Hello world', long_description="aaa\nbbb")
    actual_returns = parse(lines)
    assert actual_returns == expected_returns

    expected_returns = Docstring(short_description='Hello world', long_description="aaa\nbbb")
    actual_returns = parse(lines)
    assert actual_returns == expected_returns

    #

# Generated at 2022-06-13 19:34:51.993135
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Instance: p
    p = GoogleParser()
    # Docstring: doc
    doc = """This function does something.
    
    This is a longer explanation.
    
    Args:
        arg1 (str): The first argument.
        arg2 (int): The second argument.
    """
    # Parse doc

# Generated at 2022-06-13 19:35:06.972563
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert(parse("") == Docstring())
    assert(parse("Hello world") == Docstring("Hello world"))
    assert(parse("Hello\nworld") == Docstring("Hello", "world"))
    assert(parse("Hello world\n\nlonger") == Docstring("Hello world", ""))
    assert(parse("Hello world\n\nlonger\n\n") == Docstring("Hello world", "longer"))
    assert(parse("Hello\nworld\n\nlonger") == Docstring("Hello", "world", ""))
    assert(parse("Hello world\n\nlonger\n\nwith more") ==
           Docstring("Hello world", "longer", "with more"))

# Generated at 2022-06-13 19:35:11.906798
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    gp = GoogleParser()
    ds = gp.parse('Description of the example\nThis is an example')
    assert ds == Docstring(
        short_description='Description of the example',
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description='This is an example',
        meta=[])


# Generated at 2022-06-13 19:35:14.685656
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    for title, key, type in DEFAULT_SECTIONS:
        assert title in GoogleParser().sections
        assert GoogleParser().sections[title].key == key
        assert GoogleParser().sections[title].type == type

# Generated at 2022-06-13 19:35:25.500606
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    text = "This is a very short description.\n\nThis is a full description."
    assert parser.parse(text) == Docstring(
        short_description="This is a very short description.",
        blank_after_short_description=True,
        long_description="This is a full description.",
        blank_after_long_description=False,
        meta=[]
    )
    
    text = "This is a very short description."
    assert parser.parse(text) == Docstring(
        short_description="This is a very short description.",
        blank_after_short_description=False,
        long_description=None,
        blank_after_long_description=False,
        meta=[]
    )
    
    text = "This is a very short description. This is a full description."


# Generated at 2022-06-13 19:35:36.013428
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # testing method with case when there's no docstring
    text = ""
    assert len(GoogleParser().parse(text).meta) == 0

    # testing method with case when there's only description
    text = "This is description"
    ret = GoogleParser().parse(text)
    assert len(ret.meta) == 0
    assert ret.short_description == "This is description"
    assert ret.long_description == None

    # testing method with valid docstring

# Generated at 2022-06-13 19:35:41.887035
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstring = """
    Example Google style docstrings.

        Args:
            param1 (int): The first parameter.
            param2 (str): The second parameter. Defaults to ''.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            bool: The return value. True for success, False otherwise.

    """
    assert isinstance(parser.parse(docstring), Docstring)

# Generated at 2022-06-13 19:35:49.676038
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc_string = '''
    Calculate the sum of two numbers.

    Parameters
    ----------
    a : int
        The first number.
    b : int
        The second number.

    Returns
    -------
    int
        The sum of two numbers.

    Raises
    ------
    TypeError
        When one of the inputs is not an integer.
    '''
    parsed_result = GoogleParser().parse(doc_string)
    info = parsed_result.__repr__()
    print(info)

# Generated at 2022-06-13 19:35:58.349532
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    parser = GoogleParser()
    parsed = parser.parse(
    """
    Args:
        str: String to check

    Returns:
        List[str]: list of the input string tokens
    """
    )

    assert parsed.short_description is None
    assert parsed.blank_after_short_description is False
    assert parsed.blank_after_long_description is True
    assert parsed.long_description is None

    assert len(parsed.meta) == 2

    assert parsed.meta[0].args == ['param', 'str: String to check']
    assert parsed.meta[0].description == 'String to check'
    assert parsed.meta[0].arg_name == 'str'
    assert parsed.meta[0].type_name == 'String'
    assert parsed.meta[0].default is None
    assert parsed.meta

# Generated at 2022-06-13 19:36:12.499722
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """\
    Function description.

    :param a: Parameter description.
    :param b: Parameter description.

        Multiline parameter description.
    :type b: str

    :returns: Return description.

    :raises RuntimeError: Description of raised exception.
    """
    res = GoogleParser().parse(docstring)
    assert res.short_description == "Function description."
    assert res.blank_after_short_description == False
    assert res.blank_after_long_description == False
    assert res.long_description is None
    assert res.meta[0].args == ['param', 'a']
    assert res.meta[0].description == 'Parameter description.'
    assert res.meta[1].args == ['param', 'b']

# Generated at 2022-06-13 19:36:23.554125
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = GoogleParser().parse('''A one-line summary that does not use variable names or the function name.

Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.

Args:
  arg1: Description of arg1
  arg2: Description of arg2

Returns:
  Description of return value.
Raises:
  SomeError: If some error occurs.
''')
    assert doc.short_description == 'A one-line summary that does not use variable names or the function name.'
    assert doc.long_description == '''Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.'''
    assert doc.blank_after_short_description == True
    assert doc.blank_after_long_description == True
    assert doc

# Generated at 2022-06-13 19:36:30.280084
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    ret = parse('''Title: Adds two numbers together.
Summary: Adds two numbers together.

Description of the function.

Arguments:
    x: The first number to add.
    y: The second number to add.

Returns:
    The sum of x and y.

Example:
    Print the sum of 2 and 3:

    >>> print(add(2, 3))
    5\n''')
    # Assign expected output to variable exp_ret

# Generated at 2022-06-13 19:36:39.328245
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:36:40.993407
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    #TODO:
    pass


# Generated at 2022-06-13 19:36:43.191933
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    print("Start Unit test for method parse of class GoogleParser")
    t = "Create a parser instance."
    p = GoogleParser()
    print(p.parse(t))



# Generated at 2022-06-13 19:36:53.680021
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse("") == Docstring()
    assert parse("a") == Docstring("a", None)
    assert parse("a\n\nb") == Docstring("a", "b")
    assert parse("a:") == Docstring("a", None)
    assert parse("a:\nb") == Docstring("a", None)
    assert parse("a:\nb\n") == Docstring("a", "b")
    assert parse("a\n\nb:") == Docstring("a", None)
    assert parse("a\n\nb:\nc") == Docstring("a", "b:\nc")



# Generated at 2022-06-13 19:37:04.684885
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    p = GoogleParser()
    doc = """
    Short summary.

    Longer summary.
    """
    assert p.parse(doc) == Docstring(
        short_description="Short summary.",
        blank_after_short_description=True,
        long_description="Longer summary.",
        blank_after_long_description=True,
        meta=[],
    )
    doc = """
    Short summary.

    Longer summary.


    Arguments:

        name (str): Argument.
    """

# Generated at 2022-06-13 19:37:15.288768
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def parse(text: str) -> Docstring:
        """Parse the Google-style docstring into its components.

        :returns: parsed docstring
        """
        return GoogleParser().parse(text)
    # correct arguments

# Generated at 2022-06-13 19:37:28.061159
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:37:47.340908
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    GoogleParser().parse('''
        Short summary.
        Longer description.

        Args:
            var1: Description for `var1`.
            var2: Description for `var2`.

        Returns:
            Description of return value.
            Description of return value.

        Raises:
            ValueError: Description of `ValueError` raised.
            AttributeError: Description of `AttributeError` raised.

        Examples:
            Examples should be written in doctest format, and
            should illustrate how to use the function.

            >>> a=[1,2,3]
            >>> print([x + 3 for x in a])
            [4, 5, 6]
    ''')



"""
Tests for GoogleParser class
"""

import unittest
from os import path

from docstingutils.parse.google import GoogleParser



# Generated at 2022-06-13 19:37:50.546409
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstring = inspect.getdoc(parser.parse)
    assert parser.parse(docstring)


# Generated at 2022-06-13 19:38:01.136997
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
  parser = GoogleParser()
  if parser.parse("") != Docstring():
    raise AssertionError()

# Generated at 2022-06-13 19:38:07.743306
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse("") == parse.__doc__
    assert parse("\n\n") == parse.__doc__
    assert parse("\n\n\n") == parse.__doc__
    assert parse("\n\n\n\n") == parse.__doc__
    assert parse("\n\n  \n\n") == parse.__doc__
    assert parse("\n\n  \n\n  ") == parse.__doc__
    assert parse("\n\n\n foo bar \n\n") == "foo bar"
    assert (
        parse("\n\n\n foo bar \n\n\n") == "foo bar " + parse.__doc__
    )  #

# Generated at 2022-06-13 19:38:18.281058
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    class Test:
        '''Test  class

        before
            Test class
        '''
        def test_func(self):
            '''Test method

            after
                Test method
            '''

    assert Test.__doc__ == Test().test_func.__doc__
    docstring = GoogleParser().parse(Test.__doc__)
    assert docstring.short_description == 'Test  class'
    assert docstring.long_description == 'before\n    Test class'
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == True

    docstring = GoogleParser().parse(Test().test_func.__doc__)
    assert docstring.short_description == 'Test method'
    assert docstring.long_description == 'after\n    Test method'
   

# Generated at 2022-06-13 19:38:29.453490
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = '"""This is a docstring with everything in it.\n' + '\n' + 'Args:\n' + '    a: Parameter a.\n' + '    b: Parameter b.\n' + '\n' + 'Returns:\n' + '    int: returns sum.\n' + '\n' + 'Raises:\n' + '    ValueError: if values a or b are out of bound.\n' + '\n' + 'Examples:\n' + '    >>> sum(1, 2)\n' + '    3\n' + '"""\n'
    p = GoogleParser()
    print(p.parse(docstring))


# Generated at 2022-06-13 19:38:33.050388
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser=GoogleParser()
    docstring=parser.parse('Test docstring.')
    assert docstring.short_description=='Test docstring.'

# Generated at 2022-06-13 19:38:39.654095
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # CONST
    # REQUIRE
    text = "Euler's number (2.718...), to available precision."
    parser = GoogleParser()
    expected =Docstring(
        meta=[
            DocstringMeta(args=['examples'], description='Euler\'s number (2.718...), to available precision.'),
        ],
        short_description=None,
        long_description=None,
        blank_after_short_description=True,
        blank_after_long_description=False
    )
    # ENSURE
    assert parser.parse(text) == expected


# Generated at 2022-06-13 19:38:51.986224
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    This function does a thing.

    This function does a thing.

    Args:
        arg1 (str): The first argument.
        arg2 (int): The second argument.

    Returns:
        str: The return value.

    Raises:
        ValueError: if a value error occurred
    """
    parser = GoogleParser()
    docstring = parser.parse(text)
    assert docstring.short_description == "This function does a thing."
    assert docstring.long_description == "This function does a thing."
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False
    
    assert docstring.meta[0].args == ['param', 'arg1 (str)']

# Generated at 2022-06-13 19:38:55.847868
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    Args:
        input (:obj:`int`, optional): The size of the vocabulary,
            i.e. maximum integer index + 1.
            Defaults to 210.
        output (:obj:`int`, optional): The number of hidden units.
            Defaults to 512.
        bidirectional (:obj:`bool`, optional): If ``False``,
            the RNN is unidirectional. Defaults to ``True``.

    """
    assert GoogleParser().parse(text) == parse(text)

# Generated at 2022-06-13 19:39:10.432077
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    s = Docstring()
    # test for no docstring
    assert GoogleParser().parse(None) == s
    # test for short description
    sd = 'A short description'
    s.short_description = sd
    assert GoogleParser().parse(sd) == s
    # test for long description
    ld = 'A long description'
    s.blank_after_short_description = True
    s.blank_after_long_description = True
    s.long_description = ld
    assert GoogleParser().parse(sd + "\n\n" + ld) == s
    # test for meta data
    m = DocstringMeta(args = ['Returns'], description = 'A docstring')
    s.meta = [m]

# Generated at 2022-06-13 19:39:21.077155
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:39:26.119090
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # test results
    res = {'short_description': 'Parse the Google-style docstring into its components.',
           'blank_after_short_description': True,
           'long_description': '\n    :returns: parsed docstring\n    ',
           'blank_after_long_description': False,
           'meta': [{'args': ['Params', 'text'], 'arg_name': 'text', 'type_name': 'str', 'description': 'The text to', 'is_optional': False, 'default': None}],
           'children': []}

    docstring = """Parse the Google-style docstring into its components.

    :param text: The text to
    :returns: parsed docstring
    """

    gp = GoogleParser()
    assert gp.parse(docstring) == res


# Generated at 2022-06-13 19:39:32.067013
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    ds = """
        Args:
            arg1 (str, optional): this is arg1. Defaults to ''.
            arg2 (int, optional): this is arg2. Defaults to 0.

        Returns:
            str, int: string is arg1, int is arg2

        Raises:
            ValueError: if arg2 is not numeric.
            TypeError: if arg1 is not a str.
        """
    # print(GoogleParser().parse(ds))
    print(parse(ds))


if __name__ == "__main__":
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:39:42.430635
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:39:47.222748
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    TITLE_COLONS = [True, False]
    for tc in TITLE_COLONS:
        gp = GoogleParser(title_colon=tc)

        # test case 1
        docstring = """
        short description

        long description

        example:
            example code

        returns:
            return_type:
            return_desc.
        """
        parsed_docstring = gp.parse(docstring)

# Generated at 2022-06-13 19:39:47.829444
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    pass



# Generated at 2022-06-13 19:39:58.779251
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    test_cases = [
        ("""
         Params:
            a:
                1
        """, ["Params a: 1\n"]),
        (
            """
         Params:
            a: int(1), optional
                1
                2
        """,
            ["Params a (int(1)), optional: 1\n2\n"],
        ),
        (
            """
         Params:
            a: int(1), optional
                1
        """,
            ["Params a (int(1)), optional: 1"],
        ),
        (
            """
         Params:
            a: int(1)
                1
        """,
            ["Params a (int(1)): 1"],
        ),
    ]

# Generated at 2022-06-13 19:40:08.356093
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:40:17.390978
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from textwrap import dedent
    d = dedent('''\
        Do something with args.

        Args:
            foo (int, optional): Foo bar. Defaults to 1.
            bar: str
                Bar baz.

        Returns:
            None''')
    d = GoogleParser().parse(d)
    assert(d.short_description)
    assert(d.long_description)
    assert(d.meta)
    assert(d.meta[0])
    assert(d.meta[0].args)
    assert(d.meta[0].args[0] == "param")
    assert(d.meta[0].args[1] == "foo (int, optional)")
    assert(d.meta[0].description == "Foo bar. Defaults to 1.")

# Generated at 2022-06-13 19:40:36.859985
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    This is a short description.

    This is a long description.
    It has multiple lines.
    It explains the function in detail.

    Args:
        arg1 (int): Description of arg1.
        arg2 (list[int]): Description of arg2.

    Returns:
        Description of return.

    Raises:
        TypeError: On invalid argument.

    Example:
    >>> hello()
    "world"
    """
    ret = GoogleParser().parse(text)
    assert ret.short_description == "This is a short description."
    assert ret.blank_after_short_description
    assert ret.long_description == """This is a long description.
It has multiple lines.
It explains the function in detail."""
    assert ret.blank_after_long_description

# Generated at 2022-06-13 19:40:47.381567
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    short_desc = "Generate a plot of the partial autocorrelations"