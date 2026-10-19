

# Generated at 2022-06-13 19:31:05.058639
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    pass



# Generated at 2022-06-13 19:31:15.365904
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .epytext import EpytextParser
    epytext = """
        Parse the Google-style docstring into its components.

        :param SectionType section_type: The type of
                docstring to parse.
        :param str text: The docstring to parse, as a
                string.

        :returns: parsed docstring
        :rtype: Docstring
    """
    epytext_2 = """
        Parse the Google-style docstring into its components.

        @Param SectionType section_type: The type of
                docstring to parse.
        @Param str text: The docstring to parse, as a
                string.

        @returns parsed docstring
        @rtype str
    """

# Generated at 2022-06-13 19:31:22.042548
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """\
        Short description.

        Long description.
        """
    assert GoogleParser().parse(text) == Docstring(
        short_description="Short description.",
        long_description="Long description.",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[]
    )

    text = """\
        Short description.

        Long description.

        """
    assert GoogleParser().parse(text) == Docstring(
        short_description="Short description.",
        long_description="Long description.",
        blank_after_short_description=True,
        blank_after_long_description=True,
        meta=[]
    )

    text = """\
        Short description.

        """

# Generated at 2022-06-13 19:31:34.827443
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # example
    assert {} == GoogleParser().parse('')

    # simple
    assert {
        'short_description': 'Returns the sum of a and b',
        'blank_after_short_description': False,
        'blank_after_long_description': False,
        'long_description': None,
        'meta': [
            DocstringReturns(
                args=['return', 'int'],
                description='The return value.',
                type_name='int',
                is_generator=False
            )
        ]
    } == GoogleParser().parse(
        """\
    Returns the sum of a and b

    :return int: The return value.
    """
    )

    # 2 returns

# Generated at 2022-06-13 19:31:44.830842
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    # Test with explicit parser and settings
    expected = Docstring(
        short_description="My short description.",
        blank_after_short_description=False,
        long_description="Long description.",
        blank_after_long_description=False,
        meta=[
            DocstringParam(
                args=["Params", "arg_name (str)"],
                description="Argument description.",
                arg_name="arg_name",
                type_name="str",
                is_optional=False,
                default=None,
            ),
            DocstringReturns(
                args=["Return", "return_name"],
                description="Return description.",
                type_name="return_name",
                is_generator=False,
            ),
        ],
    )

# Generated at 2022-06-13 19:31:53.134437
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Test GoogleParser.parse()"""
    parser = GoogleParser()
    text = """\
        Parse the Google-style docstring into its components.
        This module supports parsing Google-style docstrings.
        Args:
                text (str): the docstring to parse.
        Returns:
                Docstring: model of docstring.
        """
    docstring = parser.parse(text)
    assert docstring.short_description == "Parse the Google-style docstring into its components."
    assert docstring.long_description == "This module supports parsing Google-style docstrings."

# Generated at 2022-06-13 19:32:07.164704
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Test parsing of short description
    assert GoogleParser().parse("Desc").short_description == "Desc"
    assert GoogleParser().parse("Desc\nDesc\ni").long_description == "Desc\nDesc"
    assert GoogleParser().parse("Desc\nDesc\ni").blank_after_long_description

    # Test parsing of long description
    assert GoogleParser().parse("Desc\nDesc\n\ni").long_description == "Desc\nDesc"
    assert not GoogleParser().parse("Desc\nDesc\n\ni").blank_after_long_description
    assert GoogleParser().parse("Desc\nDesc\n\n").long_description == "Desc\nDesc\n"
    assert GoogleParser().parse("Desc\nDesc\n\n").blank_after_long_description

# Generated at 2022-06-13 19:32:16.984258
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def test_func():
        """
        Long description
        :param a: first parameter
        :type a: str
        :param b: second parameter
        :type b: str
        :returns: return value
        :rtype: str
        """
    def test_func2():
        """
        Long description
        :param a: first parameter
        :type a: str
        :param b: second parameter
        :type b: str
        :returns: returns value
        :rtype: str
        """
    def test_func3():
        """
        Long description
        :Example: example text
        :Example: example text
        """
    def test_func4():
        """
        Long description
        :example: example text
        :example: example text
        """

# Generated at 2022-06-13 19:32:25.972910
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    d = '''Test Google-style docstring.

Args:
    node_id:
        A NodeId identifier.
    namespace_idx:
        Namespace index for the NodeId.
    integer_id:
        Integer identifier for the NodeId.
    string_id:
        String identifier for the NodeId.
    byte_string_id:
        Opaque byte string identifier for the NodeId.
    guid_id:
        GUID identifier for the NodeId.
    integer_id:
        Integer identifier for the NodeId.

Returns:
    Boolean indicator if the NodeId is valid.

Raises:
    ValueError:
        If the NodeId is not valid.

'''
    ds = parse(d)
    assert ds.short_description == "Test Google-style docstring."

# Generated at 2022-06-13 19:32:31.553787
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import (
        DocstringParam,
        DocstringRaises,
        DocstringReturns,
    )
    docstring = """A python file used to test docstring.

Raises:
    Exception: when something wrong happens.

Args:
    param:   a parameter for test.
    other_param: other parameter for test.

Returns:
    string: a return value for test.
    """
    docstring_parser = GoogleParser()
    result = docstring_parser.parse(docstring)

# Generated at 2022-06-13 19:32:52.935703
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Setup the parser
    parser = GoogleParser()
    # Parse a test docstring
    doc = parser.parse(
        inspect.cleandoc(
            """This method has one parameter, a string, and returns a list.
        Any empty lines in the body must be preserved.

        Args:
            arg1 (str): String argument.
        Returns:
            list: String as list of characters.
        """
        )
    )
    # Check results
    assert doc.short_description == "This method has one parameter, a string, and returns a list."
    assert doc.long_description == "Any empty lines in the body must be preserved."
    assert doc.blank_after_short_description == True
    assert doc.blank_after_long_description == True
    assert len(doc.meta) == 2
    # Check first metain

# Generated at 2022-06-13 19:32:53.937400
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
  import doctest
  doctest.testmod()

# Generated at 2022-06-13 19:33:05.466002
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    c = GoogleParser()
    assert c.parse("Hello, world!") == Docstring(
        short_description="Hello, world!",
        long_description=None,
        docstring_meta=[],
        blank_after_short_description=True,
        blank_after_long_description=False,
    )
    assert c.parse("""Hello, world!

    This is a long description.
    It consists of multiple lines.
    """) == Docstring(
        short_description="Hello, world!",
        long_description="This is a long description.\nIt consists of multiple lines.",
        docstring_meta=[],
        blank_after_short_description=False,
        blank_after_long_description=False,
    )

# Generated at 2022-06-13 19:33:11.612247
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # test case 1
    docstring = '''A function that writes "Hello World" on the console.

Args:
    message (str, optional): The message to print. Defaults to "Hello World!".
    number (int, optional): The number of times to print the message.
        Defaults to 1.

Returns:
    int: The number of characters written.
'''
    parser = GoogleParser()
    parsed = parser.parse(docstring)
    assert isinstance(parsed, Docstring)

    assert parsed.short_description == 'A function that writes "Hello World" on the console.'
    assert parsed.blank_after_short_description == False
    assert parsed.blank_after_long_description == True
    assert parsed.long_description == None

    assert len(parsed.meta) == 3
    assert parsed.meta

# Generated at 2022-06-13 19:33:20.989148
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''Example with underscores.

Args:
    normal: No special characters.
    _single_leading_underscore: forbidden by convention.
    single_trailing_underscore_: stored as a string.
    __double_leading_underscore__: "magic" objects or attributes that live in
                                   user-controlled namespaces.
    __double_leading_and_trailing_underscore__: "magic" objects or attributes
                                                that live in user-controlled
                                                namespaces.

Raises:
    AttributeError: The ``Raises`` section is a list of all exceptions
        that are relevant to the interface.
    ValueError: If `param2` is equal to `param1`.

'''

    # call the function parse of class GoogleParser
    ret = GoogleParser().parse(text)


# Generated at 2022-06-13 19:33:31.370533
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
  # Comment
  parser = GoogleParser()

# Generated at 2022-06-13 19:33:39.043522
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    google_parser = GoogleParser()
    docstring = google_parser.parse("""
        Args:
            test (test): test test
        
        Returns:
            returns
    """)
    docstring = google_parser.parse("""
            Args:
                test (test): test test
                
            Returns:
                returns
        """)


# Generated at 2022-06-13 19:33:51.398531
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def parse_eval(text: str) -> Docstring:
        parser = GoogleParser()
        return parser.parse(text)

    def parse_some_text(text: str) -> bool:
        parsed_data = parse_eval(text)
        if parsed_data is None:
            return True
        else:
            return False

    # Test case 1: False case
    text = """Description
        Args:
            short: short description
        Returns:
            Returns: long description
    """
    assert parse_some_text(text) == False

    # Test case 2: True case
    text = """Description
        Args:
            short: short description
        Returns:
            long description
    """
    assert parse_some_text(text) == True

    # Test case 3: True case

# Generated at 2022-06-13 19:34:00.454599
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    google_parser = GoogleParser()
    doc = """
    Short single-line summary.

    More detailed multi-line description.

    Args:
        first (str): First parameter.
        second (str): Second parameter, with a somewhat
                      long description.

    Returns:
        str: The return value. True for success, False otherwise.

    Raises:
        AttributeError
    """

# Generated at 2022-06-13 19:34:10.849972
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # test a function
    def function():
        """
        This is a function.

        Args:
            arg1(int): this is arg1
            arg2(int): this is arg2
        Returns:
            int: this is return
        """
        return 42
    # get the docstring
    text = function.__doc__
    # parse the docstring
    docstring = GoogleParser().parse(text)
    # test for excpected results
    assert docstring.short_description == "This is a function."
    assert docstring.long_description == None
    assert docstring.meta[0].args == ["param", "arg1(int)"]
    assert docstring.meta[0].arg_name == "arg1"
    assert docstring.meta[0].type_name == "int"
    assert docstring.meta

# Generated at 2022-06-13 19:34:25.649790
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = "Makes a list of words from the example sentence, then randomly selects one and returns it.\n"
    docstring = GoogleParser().parse(text)
    assert docstring.short_description == text.strip("\n")
    assert docstring.long_description == None

    text = "Makes a list of words from the example sentence, then randomly selects one and returns it.\n\n"
    docstring = GoogleParser().parse(text)
    assert docstring.short_description == text.strip("\n")
    assert docstring.long_description == None

    text = "Makes a list of words from the example sentence, then randomly selects one and returns it.\n\nExtra text here."
    docstring = GoogleParser().parse(text)

# Generated at 2022-06-13 19:34:35.619851
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    google = GoogleParser()
    # test the method parse of class GoogleParser
    assert google.parse("""test_GoogleParser_parse()
           docstring.
           """
          ) == Docstring(short_description="test_GoogleParser_parse()\n           docstring.", 
                         blank_after_short_description=True,
                         long_description=None,
                         blank_after_long_description=False,
                         meta=[])
    # test the method parse of class GoogleParser
    assert google.parse("""test_GoogleParser_parse()
           docstring.
           """
          ) != Docstring(short_description="test_GoogleParser_parse()\n           docstring.", 
                         blank_after_short_description=False,
                         long_description=None,
                         blank_after_long_description=False,
                         meta=[])


# Generated at 2022-06-13 19:34:38.523471
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Examples of valid method calls:
    #     parse(text)

    # TODO: Write unit tests
    assert False

# Generated at 2022-06-13 19:34:47.130658
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from sample import sample
    import google_docstring.strings
    docstring = GoogleParser().parse(google_docstring.strings.sample_docstring)
    assert docstring.short_description == "This is a sample docstring."
    assert docstring.long_description == "This is a sample docstring.\n\nIt demonstrates how to use parameters in docs."
    assert len(docstring.meta) == 6
    assert docstring.meta[0].description == "This is an argument parameter."
    assert docstring.meta[0].type_name == "str"
    assert docstring.meta[1].description == "This is a second argument parameter."
    assert docstring.meta[1].type_name == "int"
    assert docstring.meta[2].description == "This is a first exception parameter."

# Generated at 2022-06-13 19:34:53.763987
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Test parse of GoogleParser."""
    docstring = '/**\n' + \
                '* Create a new instance.\n' + \
                '*\n' + \
                '* @param n\n' + \
                '* @return\n' + \
                '*/'
    docstringCode = GoogleParser().parse(docstring)
    print(docstringCode.short_description)
    print(docstringCode.long_description)
    print(docstringCode.meta)
    assert type(docstringCode) is Docstring


# Generated at 2022-06-13 19:34:57.344410
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = GoogleParser().parse.__doc__
    assert docstring == "Parse the Google-style docstring into its components."

# Generated at 2022-06-13 19:35:10.273547
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    print("test_GoogleParser_parse() begin")
    content = '''docstring of GoogleParser

Args:
    text: docstring of GoogleParser
    sections: Recognized sections or None to defaults.
Returns:
    parsed docstring
Raises:
    ParseError: raised exception
Yields:
    returns parsed docstring
    '''
    parser = GoogleParser()
    ds = parser.parse(content)
    print(ds)



    content = '''docstring of GoogleParser

Args:
    text: docstring of GoogleParser
    sections: Recognized sections or None to defaults.
Returns:
    parsed docstring
Raises:
    ParseError: raised exception
Yields:
    returns parsed docstring
    '''
    parser = GoogleParser()
    ds = parser.parse(content)
   

# Generated at 2022-06-13 19:35:18.039840
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    g = GoogleParser()
    docstring = """One line summary.

    Extended description.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> a = [1, 2, 3]
        >>> print [x + 3 for x in a]
        [4, 5, 6]

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.
    """
    parsed_text = g.parse(docstring)
    assert isinstance(parsed_text, Docstring)
    assert parsed_text.short_description == "One line summary."
    assert parsed_text.long_description == "Extended description."
    assert parsed_text.blank_

# Generated at 2022-06-13 19:35:28.370287
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse("") == Docstring()

    assert parse("no title\nand long description") == Docstring(
        short_description="no title",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description="and long description",
    )

    assert parse("\nno title\nand long description\n") == Docstring(
        short_description="no title",
        blank_after_short_description=True,
        blank_after_long_description=True,
        long_description="and long description",
    )

    assert parse("Arguments:\n  foo: bar\n") == Docstring(
        meta=[DocstringParam(args=["param", "foo"], description="bar")]
    )


# Generated at 2022-06-13 19:35:36.509755
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    class TestPython:
        """
        문서주석

        첫줄
        둘줄
        셋줄

        Examples
        --------
        >>> x = 1
        >>> print(x)

        Arguments
        =========
        x: int
            x 의 설명 
            첫줄
            둘줄

        y: str
            y 의 설명 

        Raises
        ======
        Exception
            Exception 을 발생시킨다
        """

        def __init__(self, x, y):
            pass

    parser = GoogleParser()
    docstring = parser.parse(TestPython.__doc__)
   

# Generated at 2022-06-13 19:35:48.450677
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from . import assert_docstring_equal
    text = """\
    Short description.

    More detailed description.

    Args:
      arg1: First arg.
      arg2: Second arg. Defaults to None.
    Kwargs:
      kwarg1: First kwarg.
      kwarg2: Second kwarg. Defaults to True.
    Returns:
      The return value.

    Raises:
      Exception1: If something happens.
      Exception2: If something else happens.

    """
    docstring = parse(text)

# Generated at 2022-06-13 19:35:57.349098
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    def gs(s: str) -> str:
        print(s)
        p = GoogleParser().parse(s)
        print(repr(p))
        return s


# Generated at 2022-06-13 19:35:58.108136
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse(None) == Docstring()

# Generated at 2022-06-13 19:36:05.315683
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = '''
    :param x: The x value
    :param y: The y value
    :type x: int
    :type y: int
    :return: The sum of x and y
    :rtype: int

    Examples
    --------
    >>> add_numbers(1, 2)
    3
    '''
    parser = GoogleParser()
    doc = parser.parse(docstring)
    assert len(doc.meta) == 6
    assert doc.short_description is None
    assert doc.long_description is None

    assert doc.meta[0].args == ['param', 'x: The x value']
    assert doc.meta[0].description == 'The x value'
    assert doc.meta[0].arg_name == 'x'
    assert doc.meta[0].type_name is None
   

# Generated at 2022-06-13 19:36:14.341767
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Test parse
    docstring = """Single line docstring."""
    docstring_parsed = GoogleParser().parse(docstring)
    assert docstring_parsed.short_description == "Single line docstring."

    docstring = """Single line docstring.
    Long description.
    """
    docstring_parsed = GoogleParser().parse(docstring)
    assert docstring_parsed.short_description == "Single line docstring."
    assert docstring_parsed.long_description == "Long description."

    docstring = """Single line docstring.

Long description.
    """
    docstring_parsed = GoogleParser().parse(docstring)
    assert docstring_parsed.short_description == "Single line docstring."

# Generated at 2022-06-13 19:36:24.792216
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    d = """Short description.

    Long description.

    Returns:
        dict:
            Returns dict.

    Raises:
        AttributeError: Atribute error.

    """
    docstring = parse(d)
    assert docstring.short_description == "Short description."
    assert docstring.long_description == "Long description."
    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is False
    assert docstring.meta[0].args == ["returns", "dict"]
    assert docstring.meta[0].description == "Returns dict."
    assert docstring.meta[0].arg_name == "dict"
    assert docstring.meta[1].args == ["raises", "AttributeError"]
    assert docstring.meta[1].description == "Atribute error."

# Generated at 2022-06-13 19:36:36.459087
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """test for method parse in class GoogleParser"""
    print('Testing GoogleParser.parse()')
    parser = GoogleParser()
    docstring = """
    This is a short description.
    And a long description.
    Args:
    variable (str): the variable to use
    variable2 (str): The variable.
    variable: the variable.
    Returns:
    variable (str): The variable.
    """
    parsed_docstring = parser.parse(docstring)
    assert parsed_docstring.short_description == "This is a short description."
    assert parsed_docstring.long_description == 'And a long description.'
    assert parsed_docstring.blank_after_short_description == True
    assert parsed_docstring.blank_after_long_description == False

# Generated at 2022-06-13 19:36:45.406185
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """This is a short description.

This is a long description.

Args:
    arg1_name: Type of arg1. Defaults to None.
    arg2_name (int): Type of arg2. Defaults to 0.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by two blank lines. Section breaks are also
implicitly created anytime a new section starts. Section bodies *may* be
indented:

Examples:
    Examples should usually be written in the form::

        $ python example_google.py

"""

# Generated at 2022-06-13 19:36:50.116254
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    print(parser.parse("""Returns the length of the vector.

Args:
    vector: Vector to find the length of.
"""))

if __name__ == "__main__":
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:37:02.648020
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()

    docstring = parser.parse('"""Docstring."""')
    assert docstring.short_description == "Docstring."

    docstring = parser.parse('"""\nDocstring.\n"""')
    assert docstring.short_description == "Docstring."

    docstring = parser.parse('"""\nDocstring.\n"""')
    assert docstring.short_description == "Docstring."

    docstring = parser.parse('"""\nDocstring\nmore\n"""')
    assert docstring.short_description == "Docstring"
    assert docstring.long_description == "more"

    docstring = parser.parse('"""\nDocstring\n\nmore\n"""')
    assert docstring.short_description == "Docstring"
    assert docstring.long_description == "more"

# Generated at 2022-06-13 19:37:11.374087
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
  test_text = """
  This is a test for method parse of class GoogleParser
  """
  p = GoogleParser()
  result = p.parse(test_text)
  print(result.short_description)
  print('test_GoogleParser_parse passed')

test_GoogleParser_parse()

# Generated at 2022-06-13 19:37:24.095618
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:37:31.523809
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    '''Test parse method of GoogleParser class'''

    def test_func():
        '''
        Unit test for method parse of class GoogleParser

        This long description should explain fully what this function does.
        '''

    p = GoogleParser()

    test_func_doc = test_func.__doc__
    doc = p.parse(test_func_doc)
    assert doc.short_description == 'Test parse method of GoogleParser class'
    assert doc.long_description == 'This long description should explain fully what this function does.'
    assert doc.blank_after_short_description == True
    assert doc.blank_after_long_description == True


# Generated at 2022-06-13 19:37:47.267269
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    # Test that method parse returns the object Docstring
    # with the correct fields
    def f(x: int, y: int = 2, z: int = 3) -> int:
        """
        function f docstring

        This function calculates sum of arguments.

        :param x: parameter x.
        :type x: int
        :param y: parameter y. Defaults to 2.
        :type y: int
        :param z: parameter z.
        :type z: int
        :return: Sum of x, y and z.
        :rtype: int
        """
        return x + y + z

    assert isinstance(parser.parse(f.__doc__), Docstring)
    assert parser.parse(f.__doc__).short_description == "function f docstring"

# Generated at 2022-06-13 19:37:54.214162
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docString = GoogleParser()
    # Parse description only
    assert docString.parse(
        """
    Short description.

    Long description.

    """
    ) == Docstring(
        short_description="Short description.",
        long_description="Long description.",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[],
    )

    # Parse description with examples

# Generated at 2022-06-13 19:38:03.352575
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    g = GoogleParser(title_colon=True)

    # Test method signature

    text = """Summary:
Description:
Args:
"""
    docstring = g.parse(text)

    assert docstring.short_description == "Summary"
    assert docstring.long_description == "Description"
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["Args"]

    text = """Summary:
Args:
"""
    docstring = g.parse(text)

    assert docstring.short_description == "Summary"
    assert docstring.long_description is None
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args == ["Args"]

    text = """Summary:
Description:
Raises:
"""
    docstring = g.parse(text)

# Generated at 2022-06-13 19:38:09.607234
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """GIVEN a docstring WHEN parse is called THEN a Docstring is returned with the parsed data."""
    parser = GoogleParser()
    docstring = parser.parse("""Function to test.

Short description of the function.

Long description of the function.

Attributes:
    test_argument (str): Description of test_argument.
    other_argument (str, optional): Description of other_argument.

Returns:
    str: The return value.
    """)
    # Returned Docstring should contain the parsed data
    assert docstring.short_description == "Short description of the function."
    assert docstring.long_description == "Long description of the function."
    assert "DocstringParam" in [type(e).__name__ for e in docstring.meta]

# Generated at 2022-06-13 19:38:10.642794
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse("") == Docstring()



# Generated at 2022-06-13 19:38:19.980851
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
This is a function.

Arguments:
    arg1 (int): An argument. Defaults to 0.
    arg2 (str): Another argument.
    arg3 (bool):
        A boolean argument. Defaults to False.

Returns:
    int: Returns 5.
    '''
    text2 = '''
This is a function.

Args:
    arg1 (int): An argument. Defaults to 0.
    arg2 (str): Another argument.
    arg3 (bool):
        A boolean argument. Defaults to False.

Returns:
    int: Returns 5.
    '''

# Generated at 2022-06-13 19:38:33.259227
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    #Test cases
    #Test case 1
    text1  = """\
    Args:
      arg1 (str): Description of `arg1`.
      arg2 (Optional[str]): Description of `arg2`.

    Returns:
      None: If the return type is not specified, the return type is `None` by
        default.
    """

    #Test case 2
    text2  = """\
    Args:
      a (:obj:`int`, :obj:`float`): Description of `a`.
      b (:obj:`list` of :obj:`bool`): Description of `b`.

    Returns:
      None: If the return type is not specified, the return type is `None` by
        default.
    """

    #Test case 3

# Generated at 2022-06-13 19:38:55.638980
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser"""
    assert parse("docstring") == Docstring(
        short_description="docstring", long_description=None, meta=[]
    )
    assert parse("docstring\n") == Docstring(
        short_description="docstring", long_description=None, meta=[]
    )
    assert parse(" docstring") == Docstring(
        short_description="docstring", long_description=None, meta=[]
    )
    assert parse("docstring\nlong") == Docstring(
        short_description="docstring",
        long_description="long",
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )

# Generated at 2022-06-13 19:39:02.065492
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    text = """\
        This is the short description. Long description follows.

        It can be several lines long.
    """
    result = parser.parse(text)
    assert result.short_description == "This is the short description."
    assert result.blank_after_short_description == True
    assert result.long_description == """\
        Long description follows.

        It can be several lines long.
    """
    assert result.blank_after_long_description == False
    assert len(result.meta) == 0
    text = """\
        This is the short description. Long description follows.

        It can be several lines long.

        Attributes
        ----------
        first
            The first attribute.
        second
            The second one.
    """
    result = parser.parse(text)
    assert result

# Generated at 2022-06-13 19:39:11.507118
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text="""
    Arguments:
        param1 (str):
            description param1
        param2 (float): description param2
        param3 (bool,optional): description param3, Defaults to True.
        param4 (bool?): description param4

    Returns:
        str
        float

    Yields:
        bool
    """

    docstring = GoogleParser().parse(text)

    assert docstring.short_description is None
    assert docstring.long_description is None

    assert len(docstring.meta)==7

    param1 = docstring.meta[0]
    assert param1.args == ["param", "param1 (str)"]

    param2 = docstring.meta[1]
    assert param2.args == ["param", "param2 (float)"]

# Generated at 2022-06-13 19:39:21.734901
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text1 = """ A short summary of the object.

        A detailed summary of the object. This may be
        multi-line.

        Arguments:
            arg1 (str): Description of `arg1`.
            arg2 (str): Description of `arg2`.

        Raises:
            ValueError: Description of exception.
        """

    text2 = """A short summary of the object.

        A detailed summary of the object. This may be
        multi-line.

        Args:
            arg1 (str): Description of `arg1`.
            arg2 (str): Description of `arg2`.

        Raises:
            ValueError: Description of exception.
        """


# Generated at 2022-06-13 19:39:29.048877
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    test_text = "Summary line (must be a first line)\n\nLong description line 1\n\nLong description line 2\n\nParameters\n----------\nx : str\n    Parameter x documentation\n    lines\n\ny : List[int]\n    Parameter z documentation,\n    lines\n\nRaises\n------\nValueError\n    If something\n    goes wrong\n\nReturns\n-------\nNone\n    Returning nothing\n"
    g_parse = GoogleParser()
    g_parse.parse(test_text)
    assert True


# Generated at 2022-06-13 19:39:34.495075
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse(
        """A very short description.

    A longer description with some examples::

        >>> foo()
        1
        2
        3

    """
    ) == Docstring(
        "A very short description.",
        "\n    A longer description with some examples::\n        >>> foo()\n        1\n        2\n        3",
        False,
        True,
    )

# Generated at 2022-06-13 19:39:44.001121
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser"""

    # Test for Google format docstrings with no content.
    assert GoogleParser().parse("") == Docstring()

    # Test for Google format docstrings with basic content.
    docstring = GoogleParser().parse(
        """
    Short description

    Long description

    Args:
        arg1: arg1 in Args section.
        arg2: arg2 in Args section.

    Raises:
        ValueError: if arg1 > 10.
        TypeError: if arg2 is not integer.
    """
    )

# Generated at 2022-06-13 19:39:49.780571
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstring = parser.parse("""
    Description

    Args:
        argument1 (int): Description

    Returns:
        int: Description

    Raises:
        ValueError: Description
    """)
    assert docstring.short_description == "Description"
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False
    assert docstring.meta[0].args == ["param", "argument1 (int)"]
    assert docstring.meta[1].args == ["returns", "int"]
    assert docstring.meta[2].args == ["raises", "ValueError"]


# Generated at 2022-06-13 19:40:00.236228
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    d = "This is a test docstring."
    r = parse(d)
    assert r.short_description == "This is a test docstring." and r.long_description == None

    d = "This is a test docstring.\nThis is long description."
    r = parse(d)
    assert r.short_description == "This is a test docstring." and r.long_description == "This is long description."
    assert r.blank_after_short_description == True and r.blank_after_long_description == False

    d = "This is a test docstring.\n\nThis is long description."
    r = parse(d)
    assert r.short_description == "This is a test docstring." and r.long_description == "This is long description."

# Generated at 2022-06-13 19:40:03.409833
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    test_cases = {
        'docstring': 'Python module docstring\n\nMore docs.',
    }
    for case in test_cases:
        assert case == GoogleParser().parse(test_cases[case])

# Generated at 2022-06-13 19:40:25.291627
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import pytest
    text = """A simple example.
        :param x: factor
        :param y: another factor
        :type y: float
        :raises RuntimeError: if x > 100, it will fail
        :returns: x + y, i.e. the result of addition
        Examples
            >>> add(4, 6)
            10
        """

# Generated at 2022-06-13 19:40:30.129818
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parts = re.split(r"\n{2,}", __doc__)
    if len(parts) == 1:
        return None
    docstring = parts[1].strip("\n")
    parsed = GoogleParser().parse(docstring)
    return parsed



# Generated at 2022-06-13 19:40:32.578302
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert type(GoogleParser().parse("Google-style docstring parsing.")) == type(
        Docstring()
    )



# Generated at 2022-06-13 19:40:40.302965
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:40:46.870406
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text ="""
    brief description
    longer description

    Arguments:
        arg1 (str): description 1
        arg2 (str): description 2
        arg3 (str, optional): description 3. Defaults to arg3 description.

    Raises:
        AttributeError: if attribute error is encountered
        KeyError: if key error is encountered

    Returns:
        int: return description

    """
    parser = GoogleParser()
    docstring = parser.parse(text)
    # Test attributes of class Docstring
    assert(docstring.short_description == "brief description")
    assert(docstring.long_description == "longer description")
    assert(docstring.blank_after_short_description == True)
    assert(docstring.blank_after_long_description == True)
    # Test attributes of class DocstringMeta