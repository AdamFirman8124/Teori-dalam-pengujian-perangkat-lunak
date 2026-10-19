

# Generated at 2022-06-13 19:31:07.277575
# Unit test for method add_section of class GoogleParser
def test_GoogleParser_add_section():
    text = '''Test

        Arguments:
            arg1: first arg
            arg2 (str): second arg

        Returns:
            NoneType: no return value
        '''
    docstr = GoogleParser()
    docstr.add_section(Section("Test", "test", SectionType.MULTIPLE))
    p_docstr = docstr.parse(text)
    # Test if new section is added to the list of sections.
    assert "Test" in docstr.sections.keys()
    # Test if new section is parsed.
    assert "test" in p_docstr.meta[0].args
    assert "test" in p_docstr.meta[1].args

# Generated at 2022-06-13 19:31:18.113532
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = GoogleParser().parse(text_example)
    assert docstring.short_description == "Summary line."
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == True
    assert docstring.meta[1].arg_name == "param2"
    assert docstring.meta[1].description == "The second parameter.\n\n- item 1\n- item 2"
    assert docstring.meta[2].description == "Raises a ValueError if the value is invalid."
    assert docstring.meta[3].type_name == "int"
    assert docstring.meta[3].default == "0"
    assert docstring.meta[4].type_name == "list"
    assert docstring.meta[4].is_generator == True


text_example

# Generated at 2022-06-13 19:31:30.432625
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    # Unit test description
    class TestCase:

        def __init__(self, desc, text, short_description, long_description, meta):
            self.desc = desc
            self.text = text
            self.short_description = short_description
            self.long_description = long_description
            self.meta = meta

        def __eq__(self, other):
            print(self.meta == other.meta)
            return self.short_description == other.short_description \
                    and self.long_description == other.long_description \
                    and self.meta == other.meta

        def __repr__(self):
            return self.desc

    # Unit test data

# Generated at 2022-06-13 19:31:42.192075
# Unit test for method add_section of class GoogleParser
def test_GoogleParser_add_section():
    """
    :return:
    """
    GOOGLE_TYPED_ARG_REGEX = re.compile(r"\s*(.+?)\s*\(\s*(.*[^\s]+)\s*\)")
    GOOGLE_ARG_DESC_REGEX = re.compile(r".*\. Defaults to (.+)\.")
    MULTIPLE_PATTERN = re.compile(r"(\s*[^:\s]+:)|([^:]*\]:.*)")

    def _build_meta(self, text: str, title: str) -> DocstringMeta:
        """Build docstring element.

        :param text: docstring element text
        :param title: title of section containing element
        :return:
        """

        section = self.sections[title]

# Generated at 2022-06-13 19:31:46.550956
# Unit test for method add_section of class GoogleParser
def test_GoogleParser_add_section():
    google_parser = GoogleParser()
    google_parser.add_section(Section("Raises", "raises", SectionType.MULTIPLE))
    assert ("Raises" in google_parser.sections)
    assert (google_parser.sections["Raises"].title == "Raises")
    assert (google_parser.sections["Raises"].key == "raises")
    assert (google_parser.sections["Raises"].type == SectionType.MULTIPLE)

# Generated at 2022-06-13 19:31:53.703141
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """
    A test for GoogleParser.parse method.

    Each of the following lines starts with a section title, followed by a colon,
    and a description.

    :param param1: description1. Defaults to True.
    :param int param2: description2. Defaults to 1.

    :yields: description3.
    
    :returns: description4."""

    docstring = GoogleParser().parse(docstring)


# Generated at 2022-06-13 19:32:05.562923
# Unit test for method add_section of class GoogleParser
def test_GoogleParser_add_section():
    parser = GoogleParser()
    parser.add_section(Section("Args", "param", SectionType.MULTIPLE))
    assert parser.parse('Args:\n    arg1\n    arg2')
    parser.add_section(Section("Args", "args", SectionType.MULTIPLE))
    assert parser.parse('Args:\n    arg1\n    arg2')
    assert parser.sections['Args'].key == 'args'
    parser.add_section(Section("Arguments", "args", SectionType.MULTIPLE))
    assert parser.parse('Args:\n    arg1\n    arg2')
    assert parser.parse('Arguments:\n    arg1\n    arg2')


# Generated at 2022-06-13 19:32:13.576169
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    google_parser = GoogleParser()
    docstring = google_parser.parse("""
    Args:
        param1 (str): Description of `param1`.
        param2 (int, optional): Description of `param2`. Defaults to 42.
            This description is multi-line.
        *args: Description of `args`.
        **kwargs: Description of `kwargs`.
    """)
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert docstring.meta[0].key == "param"
    assert docstring.meta[0].args == ["param", "param1 (str): Description of `param1`."]

# Generated at 2022-06-13 19:32:23.733705
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """This is a test
        This will be the long description.
        :param a: The first parameter.
        :param b: The second parameter.
        :raises ValueError: If a is not a number.
        :raises TypeError: If b is not a string.
        :returns: None
        """
    parsed_docstring_meta_list = GoogleParser().parse(text).meta
    assert parsed_docstring_meta_list[0].args == ["returns"]
    assert parsed_docstring_meta_list[0].description == "None"

    assert parsed_docstring_meta_list[1].args == ["raises", "ValueError"]
    assert parsed_docstring_meta_list[1].description == "If a is not a number."


# Generated at 2022-06-13 19:32:30.048748
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstr = """
    This function does something.

    First line of a longer explanation.

    Second line of a longer explanation.

    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.

    Returns:
        bool: The return value. True for success, False otherwise.
    """
    ds = parse(docstr)
    assert ds.returns.description == 'The return value. True for success, False otherwise.'
    assert ds.returns.args == ['returns', 'bool']
    assert ds.long_description == 'First line of a longer explanation.\n\nSecond line of a longer explanation.'
    assert ds.short_description == 'This function does something.'
    assert len(ds.params) == 2

# Generated at 2022-06-13 19:32:52.007819
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:32:58.358975
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def f(x):
        """Test function for GoogleParser.parse.
        
        :param x: some parameter
        :type x: int
        :param y: another parameter
        :returns: a value
        :rtype: int
        
        First line.
        
        Second line.
        
        Third line.
        """
        return x
    
    docstring = f.__doc__
    
    doc = GoogleParser().parse(docstring)

    assert doc.short_description == "Test function for GoogleParser.parse."
    assert doc.long_description == "First line.\n\nSecond line.\n\nThird line."
    assert doc.blank_after_short_description
    assert doc.blank_after_long_description
    assert len(doc.meta) == 2

# Generated at 2022-06-13 19:33:09.439434
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # __init__
    # None to defaults
    parser = GoogleParser()

# Generated at 2022-06-13 19:33:19.791796
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .docstring import Docstring
    from .docstring import DocstringMeta
    from .docstring import DocstringParam
    from .docstring import DocstringReturns
    from .docstring import DocstringRaises
    from .docstring import DocstringType

    # Test short description
    p = GoogleParser()
    d = p.parse("Short description")
    assert isinstance(d, Docstring)
    assert d.short_description == "Short description"
    assert d.blank_after_short_description == False
    assert d.blank_after_long_description == False
    assert d.long_description == None
    assert d.summary == None
    assert d.meta == []

    # Test short description with blank line after it
    p = GoogleParser()
    d = p.parse("Short description\n\n")
    assert isinstance

# Generated at 2022-06-13 19:33:30.466917
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = """Short description.

    Longer description.

    Args:
       one: First parameter
       two: Second parameter.

    Returns:
       Something

    """
    p = GoogleParser()
    res = p.parse(doc)
    assert res.short_description == "Short description."
    assert res.long_description == "Longer description."
    assert len(res.meta) == 2
    assert res.meta[0].key == "param"
    assert res.meta[1].key == "returns"
    assert res.meta[1].args[-1] == "Something"



# Generated at 2022-06-13 19:33:35.224000
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Setup variable
    s = "toto"
    self = GoogleParser()

    # Expected error
    pytest.raises(ParseError, self.parse, s)

# Generated at 2022-06-13 19:33:41.283285
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:33:53.354747
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstr = ("""
    Function to multiply 2 numbers

    Args:
        a: First number
        b (int): Second number
        c (str): Third number

    Returns:
        int: The multiplication of a and b
    """)
    meta = parser.parse(docstr)

    assert meta.short_description == "Function to multiply 2 numbers"
    assert meta.long_description == None

    assert isinstance(meta.meta[0], DocstringParam)
    assert meta.meta[0].args == ['param', 'a']
    assert meta.meta[0].arg_name == 'a'
    assert meta.meta[0].description == "First number"
    assert meta.meta[0].is_optional == False
    assert meta.meta[0].type_name == None

# Generated at 2022-06-13 19:34:01.263541
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse("") == Docstring()

    assert parse("Docstring.") == Docstring(
        short_description="Docstring.",
        blank_after_short_description=False,
        long_description=None,
        blank_after_long_description=False,
        meta=[],
    )

    assert parse("Docstring.\n") == Docstring(
        short_description="Docstring.",
        blank_after_short_description=True,
        long_description=None,
        blank_after_long_description=True,
        meta=[],
    )

    assert parse("Docstring.\n\n") == Docstring(
        short_description="Docstring.",
        blank_after_short_description=True,
        long_description="",
        blank_after_long_description=True,
        meta=[],
    )

# Generated at 2022-06-13 19:34:11.359265
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docs = ["""
  Args:
    user (str): TensorFlow user name.
    password (str): Password of TensorFlow user.
    project_name (str): Name of the project to initialize.
    project_name_2 (str): Name of the project to initialize.

  Raises:
    Exception: If an error occurs.
    ValueError: If an error occurs.
  """
    ]
    for doc in docs:
        docstring = GoogleParser().parse(doc)
        assert docstring.short_description is None
        assert docstring.blank_after_short_description is False
        assert docstring.long_description is None
        assert docstring.blank_after_long_description is False
        print(docstring)


# Generated at 2022-06-13 19:34:34.503431
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Test the parsing of a Google docstring."""

    def f(self, arg1, arg2=1):
        """
        Test function docstring.

        This docstring has a short description and a long description.

        Args:
            arg1 (int): Description of arg1. Default to 1.

        Kwargs:
            arg2 (str): Description of arg2. Defaults to "2".

        """
        pass


# Generated at 2022-06-13 19:34:38.473018
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert(GoogleParser().parse("").short_description == None)
    assert(GoogleParser().parse("").blank_after_short_description == False)
    assert(GoogleParser().parse("").blank_after_long_description == False)
    assert(GoogleParser().parse("").long_description == None)
    assert(GoogleParser().parse("").meta == [])


# Generated at 2022-06-13 19:34:47.068870
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def parse_and_print(text: str):
        print("GoogleParser.parse(%r)" % text)
        doc = GoogleParser().parse(text)
        print("    returns: %r" % doc)
        print("    repr: %r" % repr(doc))
        return doc

    doc = parse_and_print("")
    doc = parse_and_print("    ")
    doc = parse_and_print("foo")
    doc = parse_and_print("foo\n\n")
    doc = parse_and_print("foo\n\nbar\n")
    doc = parse_and_print("foo\n\nbar\n\n")
    doc = parse_and_print("foo\n\n\n")

# Generated at 2022-06-13 19:34:55.040116
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    string_example = inspect.cleandoc("""
        Args:
            arg1 (int): The first argument.
            arg2 (str): The second argument.
        Returns:
            bool: The return value. True for success, False otherwise.
        """)

    G = GoogleParser()
    docstr = G.parse(string_example)

    assert docstr.short_description == ""
    assert docstr.long_description == None
    assert docstr.blank_after_short_description == False
    assert docstr.blank_after_long_description == True
    assert 'arg1' in docstr.params.keys()
    assert 'arg2' in docstr.params.keys()
    assert docstr.returns.type_name == "bool"


# Generated at 2022-06-13 19:35:09.292118
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    result = parse("hello, world\n")
    assert isinstance(result, Docstring)
    assert result.short_description == "hello, world"
    assert result.meta == []
    result = parse("hello, world\n\nThis is a longer description.\n")
    assert result.short_description == "hello, world"
    assert result.long_description == "This is a longer description."
    assert result.blank_after_short_description
    assert result.blank_after_long_description
    result = parse("hello, world\nThis is a longer description.\n")
    assert result.short_description == "hello, world"
    assert result.long_description == "This is a longer description."
    assert not result.blank_after_short_description
    assert result.blank_after_long_description

# Generated at 2022-06-13 19:35:17.433958
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    gp = GoogleParser()
    text = """
    This docstring is used to test GoogleParser.parse()
    The argument 'text' can be a string of multiple lines. The first line
    is the summary line, the rest are the description.
    Arguments:
        arg1: the first argument
        arg2: the second argument
            The description of arg2 should be indented with two spaces.
        arg3: the third argument
    Returns:
        The return value
    """
    doc = gp.parse(text)
    print(doc)

    assert(doc.short_description == "This docstring is used to test GoogleParser.parse()\nThe argument 'text' can be a string of multiple lines. The first line\nis the summary line, the rest are the description.")

# Generated at 2022-06-13 19:35:27.744695
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def test_function():
        """Some description.

        This is a test function.

        :param foo: the foo param
        :type foo: str
        :param bar: the bar param
            This is a long description
            which spans multiple lines.
            With multiple sentences.
        :type bar: str
        :returns: a str

        .. code-block:: python

            foo = 1+1
            bar = foo*2
            return bar
        """
        return True

    text = inspect.getdoc(test_function)
    result = GoogleParser().parse(text)

    assert result.short_description == "Some description."

# Generated at 2022-06-13 19:35:32.811671
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    a = GoogleParser().parse(
        """
    Args:
        param1 (str): The first parameter.
        param2 (int, optional): The second one. Defaults to None.
        param3 (:obj:`list` of :obj:`str`, optional): param3. Defaults to None.

    Returns:
        bool: param2
        """
    )
    assert isinstance(a, Docstring)
    assert a.short_description == ""
    assert a.long_description is None
    assert a.blank_after_short_description is True
    assert a.blank_after_long_description is False
    assert len(a.meta) == 3
    assert isinstance(a.meta[0], DocstringParam)
    assert a.meta[0].description == "The first parameter."

# Generated at 2022-06-13 19:35:49.729194
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse("") == Docstring("", None, None, False, True)

    input_ = (
        "This is a short description.\n"
        "\n"
        "This is a long description.\n"
        "\n"
        "Args:\n"
        "    arg1 (int): Description of arg1\n"
        "    arg2: Description of arg2\n"
        "\n"
        "Returns:\n"
        "    bool: Description of return value\n"
        "\n"
    )

# Generated at 2022-06-13 19:35:58.381644
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # test case 1
    text = """
    Parse the Google-style docstring into its components.

    :param text: docstring element text
    :param title: title of section containing element
    :return:

    .. code-block::python

        parser = GoogleParser()
        parser.parse(text)
    """

# Generated at 2022-06-13 19:36:28.288392
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    One line summary.

    Extended description.

    Args:
      arg1(str): Description of arg1
      arg2(str, optional): Description of arg2
      arg3(str): Description of arg3. Defaults to "".

    Returns:
      Description of return value
    """

    doc = GoogleParser().parse(text)
    assert doc.short_description == "One line summary."
    assert doc.long_description == "Extended description."
    assert doc.blank_after_short_description
    assert doc.blank_after_long_description
    assert doc.meta[0].args[0] == "param"
    assert doc.meta[0].args[1] == "arg1(str)"
    assert doc.meta[0].description == "Description of arg1"

# Generated at 2022-06-13 19:36:38.204967
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def test_func(a, b):
        """
        Returns the sum of two numbers.

        :param a: first number
        :param b: second number
        :type a: int
        :type b: float
        :return: sum of a and b
        :rtype: float
        """
        return a + b

    docstring = GoogleParser().parse(inspect.getdoc(test_func))
    assert docstring.short_description == "Returns the sum of two numbers."
    assert (
        docstring.long_description
        == """
        :param a: first number
        :param b: second number
        :type a: int
        :type b: float
        :return: sum of a and b
        :rtype: float
        """
    )

# Generated at 2022-06-13 19:36:46.181621
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def a():
        """
        This is a docstring
        Raises:
            NameError: (description here)
            TypeError: (description here)

        Returns:
            value - description

        Yields:
            value - description
        """

    docstring = inspect.getdoc(a)
    result = GoogleParser().parse(docstring)
    assert result.short_description == "This is a docstring"
    raise_ele = result.meta[0]
    assert raise_ele.keyword == "raises"
    assert raise_ele.args[0] == "Raises"
    assert raise_ele.args[1] == "NameError"
    assert raise_ele.args[2] == "TypeError"
    assert raise_ele.description == "(description here)"
    return_ele = result.meta[1]

# Generated at 2022-06-13 19:36:59.069200
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
        These are the positional arguments:

            arg1 (int, optional): Description for arg1
            arg2 (int): Description for arg2

        These are the keyword arguments::

            kwarg1 (int): Description for kwarg1
            kwarg2 (int): Description for kwarg2

        :raises TypeError: if arg1 is of the wrong type
        :raises TypeError: if arg2 is of the wrong type
        :raises ValueError: if arg1 is 0
        :returns: the result of the calculation
        :rtype: int
    '''
    gp = GoogleParser()
    result = gp.parse(text)
    assert result.short_description == "These are the positional arguments:"

# Generated at 2022-06-13 19:37:03.868798
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import Docstring

    text = """
    Describes value.

    :param num: int, the number to describe
    :returns: short description
    :raises ValueError: in case of invalid value
    :raises TypeError: in case of bad type
    :other: other
    """
    print("\nTest parse:")
    print("--------------------------------")

    docstring = parse(text)

    print("Short desc:")
    print("Expected: Describes value.")
    print("Actual: " + str(docstring.short_description))
    print("\n")

    print("Long desc:")
    print("Expected: ")
    print("Actual: " + str(docstring.long_description))
    print("\n")

    print("Blank after short desc:")

# Generated at 2022-06-13 19:37:14.559254
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    gp = GoogleParser()
    assert gp.parse('') == Docstring()
    assert gp.parse('\n') == Docstring()
    assert gp.parse('haha') == Docstring(short_description='haha')
    assert gp.parse('haha\n') == Docstring(short_description='haha')
    assert gp.parse('haha\n\n') == Docstring(short_description='haha')
    assert gp.parse('haha\n    wang') == Docstring(short_description='haha')
    assert gp.parse('haha\n    wang\n') == Docstring(short_description='haha')
    assert gp.parse('haha\n    wang\n\n') == Docstring(short_description='haha')

# Generated at 2022-06-13 19:37:29.563429
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """Summary line.

Extended description.

Args:
    arg1 (int): Description of arg1
    arg2 (str): Description of arg2
    *args: Variable length argument list.
    **kwargs: Arbitrary keyword arguments.

Returns:
    bool: True if successful, False otherwise.
    """
    docstring = GoogleParser().parse(text)
    assert docstring.short_description == 'Summary line.'
    assert docstring.long_description == 'Extended description.'
    assert len(docstring.meta) == 4
    meta = docstring.meta[0]
    assert meta.args == ['param', 'arg1 (int)']
    assert meta.description == 'Description of arg1'
    assert meta.arg_name == 'arg1'
    assert meta.type_name == 'int'
   

# Generated at 2022-06-13 19:37:36.791622
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Zero input
    assert isinstance(GoogleParser().parse(''), Docstring)
    assert GoogleParser().parse('').short_description is None
    assert GoogleParser().parse('').long_description is None
    assert GoogleParser().parse('').meta == []
    # One input
    assert isinstance(GoogleParser().parse('Parse the Google-style docstring into its components.'), Docstring)
    assert GoogleParser().parse(
        'Parse the Google-style docstring into its components.').short_description == 'Parse the Google-style docstring into its components.'
    assert GoogleParser().parse(
        'Parse the Google-style docstring into its components.').long_description == 'Parse the Google-style docstring into its components.'

# Generated at 2022-06-13 19:37:41.882458
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse('''
    Summary line.

    Extended description.
    ''') == Docstring(
        short_description='Summary line.',
        long_description='Extended description.',
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[]
    )
    assert parse('''
    Summary line.

    Extended description:
      Line 1.
      Line 2.
    ''') == Docstring(
        short_description='Summary line.',
        long_description='Extended description:\n  Line 1.\n  Line 2.',
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[]
    )

# Generated at 2022-06-13 19:37:51.420493
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import sys
    import unittest

    from pydoctor import epydoc2stan

    class TestGoogleParser(unittest.TestCase):

        def assertEqualDocstring(self, expected, actual):
            self.assertEqual(expected.short_description, actual.short_description)
            self.assertEqual(expected.blank_after_short_description, actual.blank_after_short_description)
            self.assertEqual(expected.long_description, actual.long_description)
            self.assertEqual(expected.blank_after_long_description, actual.blank_after_long_description)
            self.assertEqual(len(expected.meta), len(actual.meta))

# Generated at 2022-06-13 19:38:44.200337
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from inspect import cleandoc
    from doctrans import Docstring, DocstringReturns
    from doctrans.parsers.google import GoogleParser
    from doctrans.parsers.google import DocstringMeta, DocstringParam
    from doctrans.parsers.google import DocstringRaises, DocstringReturns

    # Argument
    text = cleandoc('''
        A positional argument.

        :param arg1: The first argument.
        ''')

# Generated at 2022-06-13 19:38:50.949478
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstring = parser.parse('''
    This function returns the value of parameter foo.

    Args:
        foo: It can be either a number or an array.
    ''')
    
    assert docstring.short_description == 'This function returns the value of parameter foo.'
    assert docstring.long_description == 'It can be either a number or an array.'

# Generated at 2022-06-13 19:38:52.036329
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse(None) == Docstring()

GoogleParser.parse = test_GoogleParser_parse

# Generated at 2022-06-13 19:39:01.240774
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = parse('"""\nPurpose: used in the unit test for method GoogleParser.parse()\n"""')
    assert docstring.short_description == "Purpose: used in the unit test for method GoogleParser.parse()"

    docstring = parse('"""\nPurpose: used in the unit test for method GoogleParser.parse()\nImplementation details: you can see this chunk of docstring as a code sample\nReturns:\n    True\n"""')
    assert docstring.short_description == "Purpose: used in the unit test for method GoogleParser.parse()"
    assert docstring.long_description == "Implementation details: you can see this chunk of docstring as a code sample"
    # assert docstring.meta[0].description == "you can see this chunk of docstring as a code sample"

# Generated at 2022-06-13 19:39:10.948934
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()

    # normal docstring
    doctest = """

    A simple example docstring.

    :param p1: First param
    :type p1: int
    :param p2: second param
    :type p2: str, optional
    :param p3: third param
    :type p3: dict
    :return:
    :rtype: int
    :raises Exception1: When something goes wrong
    :raises Exception2: When other thing goes wrong
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    # method parse should return a Docstring object
    assert isinstance(parser.parse(doctest), Docstring)
    
    # method parse should return a Docstring with short_description "A simple example

# Generated at 2022-06-13 19:39:21.440886
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:39:30.733693
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    ds = """    This is a short description.

    This is the long description.

    Args:
      arg1:
        This is the long description of arg1.
      arg2:
        This is the long description of arg2.
      arg3:
        This is the long description of arg3.

    Returns:
      This is the long description of return value.
    """
    d = parser.parse(ds)
    assert d.short_description == "This is a short description."
    assert d.blank_after_short_description == True
    assert d.long_description == "This is the long description."
    assert d.blank_after_long_description == False
    assert len(d.meta) == 4
    assert d.meta[0].args == ['param', 'arg1']
   

# Generated at 2022-06-13 19:39:41.669136
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser"""
    parser = GoogleParser()
    # single title
    text1 = 'Args:\n    a: this is the first line of a\n        this is the second line of a\n    b: this is the first line of b\n        this is the second line of b'
    # multiple titles
    text2 = 'Parameters:\n    a: this is the first line of a\n        this is the second line of a\n    b: this is the first line of b\n        this is the second line of b\nRaises:\n    c: this is the first line of c\n        this is the second line of c\n    d: this is the first line of d\n        this is the second line of d'
    # multiple sections in the same title

# Generated at 2022-06-13 19:39:48.717351
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser"""

    def test_method(text: str, expected: T.Dict[str, T.Any]):
        actual: Docstring = GoogleParser().parse(text)
        assert actual.short_description == expected["short_description"]
        assert actual.blank_after_short_description == expected["blank_after_short_description"]
        assert actual.long_description == expected["long_description"]
        assert actual.blank_after_long_description == expected["blank_after_long_description"]
        assert actual.meta == expected["meta"]
    

# Generated at 2022-06-13 19:39:59.664043
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse('This is a simple Google-style docstring.').short_description == 'This is a simple Google-style docstring.'
    assert GoogleParser().parse('This is a simple Google-style docstring.\n\nThis is the long description.').short_description == 'This is a simple Google-style docstring.'
    assert GoogleParser().parse('This is a simple Google-style docstring.\n\nThis is the long description.').long_description == 'This is the long description.'
    assert GoogleParser().parse('This is a simple Google-style docstring.\n\nThis is the long description.').blank_after_short_description == True
    assert GoogleParser().parse('This is a simple Google-style docstring.\n\nThis is the long description.').blank_after_long_description == False