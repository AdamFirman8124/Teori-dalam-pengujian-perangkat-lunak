

# Generated at 2022-06-13 19:31:15.173993
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser."""
    
    # Prepare an example Docstring for validation of the parse result
    docstring = Docstring()
    docstring.short_description = "A short description"
    docstring.blank_after_short_description = True

# Generated at 2022-06-13 19:31:21.916032
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    raw_doc = """
    Class summary line.

    Long description line 1.
    Long description line 2.

    Args:
        param1 (int): Description of `param1`.
        param2 (int, optional): Description of `param2`. Defaults to 42.
        param3 (bool): Description of `param3`.

    Returns:
        Description of return value.

    Raises:
        ValueError: Description of raised exception.
    """
    doc = parse(raw_doc)
    print("=" * 40)
    print("doc.short_description:")
    print(doc.short_description)
    print("=" * 40)
    print("doc.long_description:")
    print(doc.long_description)
    print("=" * 40)
    print("doc.blank_after_short_description:")
   

# Generated at 2022-06-13 19:31:34.738227
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Simple case with just a description
    desc = inspect.cleandoc(
        """This function calculates the sum of its two
        parameters.
        """
    )
    expected = Docstring(
        short_description="This function calculates the sum of its two parameters.",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )

    test_case = GoogleParser().parse(desc)
    assert test_case == expected

    # With an additional section

# Generated at 2022-06-13 19:31:44.760522
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    A short sentence.

    A long sentence with some more details.
    It can span multiple lines.

    Parameters
    ----------
    var : type name
        Description of the variable.

        It can be multiple lines long.
        But not too long.
        Bla bla.
    """
    doc = GoogleParser().parse(text)
    assert doc.short_description == "A short sentence."
    assert doc.blank_after_short_description is True
    assert doc.long_description == "A long sentence with some more details.\n" \
                                   "It can span multiple lines."
    assert doc.blank_after_long_description is True
    assert len(doc.meta) == 1
    assert doc.meta[0].args == ["param", "var"]

# Generated at 2022-06-13 19:31:55.468789
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """\
    Short description.

    More description with
    multiple lines.

    Args:
      arg1: argument name.
      arg2: argument name.

    Returns:
      Something.
    """
    parser = GoogleParser()
    parsed = parser.parse(text)
    assert parsed.short_description == "Short description."
    assert parsed.long_description == "More description with multiple lines."
    assert parsed.blank_after_short_description
    assert parsed.blank_after_long_description
    assert isinstance(parsed.meta[0], DocstringParam)
    assert parsed.meta[0].arg_name == "arg1"
    assert parsed.meta[0].description == "argument name."
    assert isinstance(parsed.meta[1], DocstringParam)

# Generated at 2022-06-13 19:32:08.877198
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = inspect.cleandoc(
        """
    Single line description.

    Long description.

    Args:
        arg1 (type1): description1
        arg2 (type2, optional): description2
        arg3 (type3): description3. Defaults to True.

    Returns:
        str: return description

    Raises:
        MyError: Always.
        YourError: Whenever.
        HisError: Whatever.
    """
    )

# Generated at 2022-06-13 19:32:24.896147
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    expected_returns = DocstringReturns(args=['Returns'], description='the size of the stack', type_name=None, is_generator=False)
    expected_yields = DocstringReturns(args=['Yields'], description='the size of the stack', type_name=None, is_generator=True)
    expected_raises = DocstringRaises(args=['Raises'], description='the size of the stack', type_name=None)
    expected_param = DocstringParam(args=['Args'], description='the size of the stack', arg_name='size', type_name=None, is_optional=False, default=None)
    expected_meta_1 = DocstringMeta(args=['Args'], description='the size of the stack')

# Generated at 2022-06-13 19:32:30.511620
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    g = GoogleParser()
    d = g.parse("""
    Parses the Google-style docstring into its components.

    :returns: parsed docstring
    """)
    assert(isinstance(d, Docstring))
    

# Generated at 2022-06-13 19:32:41.819486
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse('') == Docstring()
    assert parse('"""An empty docstring.")') == Docstring(
        short_description=None,
        blank_after_short_description=False,
        long_description=None,
        blank_after_long_description=False,
        meta=[],
    )
    assert parse('"""A short docstring."') == Docstring(
        short_description='A short docstring.',
        blank_after_short_description=False,
        long_description=None,
        blank_after_long_description=False,
        meta=[],
    )

# Generated at 2022-06-13 19:32:51.592154
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    mp = GoogleParser()
    text = '''
    Parse the Google-style docstring into its components.

    :param text: A docstring.
    :param kwargs: Arguments to `parse`.
    :returns: parsed docstring
    '''
    doc = mp.parse(text)
    assert len(doc.meta) == 3
    assert doc.short_description == "Parse the Google-style docstring into its components."
    assert doc.long_description == ":param text: A docstring.\n:param kwargs: Arguments to `parse`.\n:returns: parsed docstring"
    assert doc.blank_after_short_description == False
    assert doc.blank_after_long_description == False
    assert doc.meta[0].args == ['param', 'text']
    assert doc.meta

# Generated at 2022-06-13 19:33:03.169643
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("") == Docstring()
    assert GoogleParser().parse("\n") == Docstring(short_description="")

    docstring = GoogleParser().parse("Example of google docstring.")
    assert docstring.short_description == "Example of google docstring."

    docstring = GoogleParser().parse(
        "Example of google docstring.\n\nWith additional description.\n..."
    )
    assert (
        docstring.long_description
        == "With additional description.\n..."
    )

    docstring = GoogleParser().parse(
        "Example of google docstring.\nWith additional description.\n..."
    )
    assert (
        docstring.long_description
        == "With additional description.\n..."
    )


# Generated at 2022-06-13 19:33:15.675578
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """
    Test case for method parse of class GoogleParser.
    """

# Generated at 2022-06-13 19:33:23.176182
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    test_data = """
    Short summary.

    Long description.

    Arguments:
        arg_name (typename): Description.
    Raises:
        ValueError: If arg_name is invalid.

    Returns:
        typename: Result of operation.

    """
    parsed = parser.parse(test_data)
    assert parsed.short_description == "Short summary."
    assert parsed.long_description == "Long description."
    assert parsed.blank_after_short_description is True
    assert parsed.blank_after_long_description is True
    assert len(parsed.meta) == 3
    assert parsed.meta[0].args == ['arg_name']
    assert parsed.meta[0].description == "Description."
    assert parsed.meta[1].args == ['raises']
   

# Generated at 2022-06-13 19:33:32.768950
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # text as string
    text = """
    This function does something.

    Args:
        arg1 (str): The first argument.
        arg2 (:obj:`int`, optional): The second argument. Defaults to None.

    Returns:
        int: The return value.

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.

    """
    # expected result as Docstring
    expected = Docstring()
    expected.short_description = "This function does something."

# Generated at 2022-06-13 19:33:42.877981
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    doc = parser.parse("""
    			This is a test.
    			
    			Arguments:
    			    test_arg (str): This is a test_arg.
    			""")
    assert doc.short_description == 'This is a test.'
    assert doc.long_description is None
    assert len(doc.meta) == 1
    assert doc.meta[0].description == 'This is a test_arg.'
    assert doc.meta[0].keyword == "param"

# Generated at 2022-06-13 19:33:55.217114
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """This is a short description.

    This is a long description.

    Args:
        param1(int): a parameter
        param2(str): another parameter

    Returns:
        a return value

    Raises:
        Exception: an exception"""

    result = GoogleParser().parse(text)
    assert result.string == text
    assert result.short_description == "This is a short description."
    assert (
        result.long_description
        == "This is a long description.\n\n    Returns:         a return value"
    )
    assert result.blank_after_short_description
    assert result.blank_after_long_description
    assert result.meta[0].args == ("param", "param1(int): a parameter")
    assert result.meta[0].description == "a parameter"
    assert result

# Generated at 2022-06-13 19:34:01.870623
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:34:11.741767
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse(None) == Docstring()
    assert parse("") == Docstring()

    assert parse("Short desc. Long desc") == Docstring(
        short_description="Short desc.",
        blank_after_short_description=False,
        long_description="Long desc",
        blank_after_long_description=False,
        meta=[],
    )
    assert parse("Short desc.\n\nLong desc") == Docstring(
        short_description="Short desc.",
        blank_after_short_description=True,
        long_description="Long desc",
        blank_after_long_description=False,
        meta=[],
    )

# Generated at 2022-06-13 19:34:23.066638
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    global my_parser
    my_parser = GoogleParser()

    assert my_parser.parse("") == Docstring()

    doc = my_parser.parse("""\
        A function docstring.

        It can be multiple lines long.

        :param a: A parameter.
        """)
    assert doc.short_description == "A function docstring."
    assert doc.long_description == "It can be multiple lines long."
    assert doc.blank_after_short_description
    assert not doc.blank_after_long_description
    assert len(doc.meta) == 1
    assert doc.meta[0].args == ["param", "a"]
    assert doc.meta[0].description == "A parameter."


# Generated at 2022-06-13 19:34:33.577471
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = inspect.cleandoc("""This is short summary.

    This is long summary.

    Args:
        arg1 (int): the first argument.
        arg2 (str): the second argument. Defaults to 'default'.
    """)

    parser = GoogleParser()
    result = parser.parse(doc)
    assert result.short_description == 'This is short summary.'
    assert result.long_description == 'This is long summary.'
    assert result.blank_after_short_description == True
    assert result.blank_after_long_description == False

    assert len(result.meta) == 2
    arg1_meta = result.meta[0]
    assert arg1_meta.args == ['param', 'arg1 (int)']
    assert arg1_meta.arg_name == 'arg1'
    assert arg1

# Generated at 2022-06-13 19:34:43.607607
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    test_string = '"""Parse the Google-style docstring into its components.\n\n:returns: parsed docstring\n"""\n'
    assert repr(GoogleParser().parse(test_string)) == repr(Docstring(short_description='Parse the Google-style docstring into its components.', blank_after_short_description=False, long_description='returns: parsed docstring', blank_after_long_description=True))
    test_string = '"""Parse the Google-style docstring into its components."""\n'
    assert repr(GoogleParser().parse(test_string)) == repr(Docstring(short_description='Parse the Google-style docstring into its components.', blank_after_short_description=True, long_description=None, blank_after_long_description=False))

# Generated at 2022-06-13 19:34:53.495143
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc_string = """
            Options:
                -h, --help        Print help message.
                --halt-on-failure Stop the program if any test fails.
                --coverage        Produce a coverage report.
                --profile         Produce a profiling report.
                --tests=<ABC>     Run tests in <ABC>..
                --output=<file>   Write test output to <file> instead of stdout.
                --xunit=<file>    Write xunit test output to <file> instead of stdout.
                --debug           Run test in debug mode.
    """
    doc = GoogleParser().parse(doc_string)
    assert doc.meta[0].args == ["param", "coverage"]
    assert doc.meta[0].description == "Produce a coverage report."
    assert doc.meta[0].arg_name

# Generated at 2022-06-13 19:35:08.326466
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """Summary line.

    Extended description.

    Args:
        arg1: This is arg1
        arg2: This is arg2. Defaults to None
        arg3 (int): This is arg3
        arg4 (Optional[int]): This is arg4

    Example:
        Examples can be given using either the ``Example`` or ``Examples``
        sections. Sections support any reStructuredText formatting, including
        literal blocks::

            $ python example_google.py
    """

# Generated at 2022-06-13 19:35:17.061920
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for GoogleParser.parse
    
    Verifies that the parsing of the docstring works correctly.
    No content is tested, only the structure of the parsed docstring
    """
    parser = GoogleParser()
    docstring = parser.parse(
        inspect.cleandoc("""
        This is a short description of the function.

        This is a longer description. It spans across multiple lines.

        By default, a blank line is required after the short description.
        But Google style docstrings do not require a blank line after the long
        description.

        Arguments:
            arg1 (int): Description of arg1.
            arg2 (:obj:`int`, optional): Description of arg2. Defaults to 1.

        Returns:
            bool: Description of return value.
        """))


# Generated at 2022-06-13 19:35:27.266034
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = '''Example::

        def example(self):
            '''
    doc += '''
        This method is an example.
        '''
    doc += '''
        Args:
            param1(str): The first parameter.
            param2(int, optional): The second parameter. Defaults to None.

        Returns:
            bool: The return valu.
        '''
    parsed = parse(doc)
    assert parsed.short_description == "Example::"
    assert parsed.long_description == "This method is an example."
    assert parsed.blank_after_short_description is True
    assert parsed.blank_after_long_description is True
    assert parsed.meta[0].args == ["param", "param1(str)"]
    assert parsed.meta[0].arg_name == "param1"

# Generated at 2022-06-13 19:35:36.819713
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    google_parser = GoogleParser()
    assert google_parser.parse(None) == Docstring()
    assert google_parser.parse("") == Docstring()
    assert google_parser.parse(" \t ") == Docstring()
    assert google_parser.parse("\n") == Docstring()

    google_parser = GoogleParser()
    docstring = google_parser.parse(
        """The first line is a short description.

    The second line is a long
    description.

    Args:
      param1(type): The first parameter. Defaults to ""
      param2 (type): The second parameter.
        Defaults to None.
        Another line for long description

    Returns:
        type: The return value. True for success, False otherwise.
    """
    )

# Generated at 2022-06-13 19:35:51.970895
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring_text = """
    Example of google-style.

    Function to do x and y.

    Arguments:
        arg1: int
            The first argument.
        arg2: str
            The second argument.

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `arg2` is equal to `arg1`.

    Returns:
        int
            The return value. True for success, False otherwise.
    """
    parser = GoogleParser()
    result = parser.parse(docstring_text)
    assert result.short_description == 'Example of google-style.'
    assert result.long_description == 'Function to do x and y.'
    assert result.blank_after_short_description is True
    assert result.blank_

# Generated at 2022-06-13 19:35:59.701483
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import Docstring, DocstringMeta, DocstringParam, DocstringRaises, DocstringReturns
    GoogleParserObj = GoogleParser()
    assert GoogleParserObj.parse('Test.') == Docstring(short_description='Test.', long_description=None, meta=[], blank_after_short_description=False, blank_after_long_description=False)
    assert GoogleParserObj.parse('Test.\n\n ') == Docstring(short_description='Test.', long_description=' ', meta=[], blank_after_short_description=True, blank_after_long_description=False)

# Generated at 2022-06-13 19:36:06.524124
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    google_parser = GoogleParser()
    assert type(google_parser) == GoogleParser
    doc_string = google_parser.parse("this is a docstring")
    assert doc_string.short_description == "this is a docstring"
    assert doc_string.long_description == None
    assert len(doc_string.meta) == 0
    doc_string = google_parser.parse("""\
            this is a\n
            docstring\n
            """)
    assert doc_string.short_description == None
    assert doc_string.long_description == "this is a docstring"
    assert doc_string.blank_after_short_description == False
    assert doc_string.blank_after_long_description == True
    assert len(doc_string.meta) == 0


# Generated at 2022-06-13 19:36:13.993894
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    ds = GoogleParser().parse('''
        # Title:
        #
        # Short:
        #
        # Args:
        #   param1 (str):
        #   param2 (str):
        #
        # Returns:
        #   str:
        #
        # Raises:
        #   ValueError:
        #
        ''')
    assert ds.meta[0].args[0] == 'param', ds.meta[0].args[0]
    assert ds.meta[1].args[0] == 'returns', ds.meta[1].args[0]


# Generated at 2022-06-13 19:36:24.860213
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    text = """
        Single line summary.

        Multiline description.

        Args:
            arg_name (int): description of arg_name

            arg_name2 (T.Optional[T.Sequence[T.Union[T.Sequence[int], int]]]): description of arg_name2

        Returns:
            int: description of return value
    """
    docstring = parser.parse(text)
    assert len(docstring.meta) == 3
    assert docstring.meta[0].description == "description of arg_name"
    assert docstring.meta[1].description == "description of arg_name2"
    assert docstring.meta[2].description == "description of return value"


# Generated at 2022-06-13 19:36:31.080809
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    if __name__ == "__main__":
        GoogleParser().parse(
            """
        Hello.
        There are many like it, but this one is mine.

        Args:
            name: Name of things.
            value: Value of things.

        Returns:
            The given value.
        """
    )

# Generated at 2022-06-13 19:36:39.710181
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import DocstringParam, DocstringReturns
    parser = GoogleParser()
    text = """
    Args:
        a: blabla
        b (type): blabla
  
    Attributes:
        a: blabla
        b (type): blabla
    """

    # Args:
    #     a: blabla
    #     b (type): blabla
    docstring = parser.parse(text)

# Generated at 2022-06-13 19:36:47.328248
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    # testing for docstring without meta data
    docstring = parser.parse("""
        Single line docstring.
        Single line docstring.
        """)
    assert docstring.short_description == "Single line docstring."
    assert docstring.long_description == "Single line docstring."
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == True
    assert len(docstring.meta) == 0
    # testing for docstring with single meta data
    docstring = parser.parse("""
        Single line docstring.
        Single line docstring.

        Single line docstring.

        Single line docstring.
        """)
    assert docstring.short_description == "Single line docstring."

# Generated at 2022-06-13 19:36:59.769477
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()

    # case 1
    text = """
    Google-style docstrings.

    This module provides a single function, `parse`, which will parse Google-
    style docstrings into an instance of :class:`Docstring`.

    The following is an example Google-style docstring::

        """
    # act
    result = parser.parse(text).__dict__

    # assert
    assert len(result) == 5
    assert result["short_description"] == "Google-style docstrings."
    assert result["blank_after_short_description"] == True
    assert result["long_description"] == "This module provides a single function, `parse`, which will parse Google-\nstyle docstrings into an instance of :class:`Docstring`."
    assert result["blank_after_long_description"] == True

# Generated at 2022-06-13 19:37:08.560517
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Test with no docstring
    docstring = ""
    result = Docstring()
    assert GoogleParser().parse(docstring) == result

    # Test with one-line docstring
    docstring = "Test one-line docstring."
    result = Docstring(
        short_description="Test one-line docstring.",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )
    assert GoogleParser().parse(docstring) == result

    # Test with multi-line docstring
    docstring = """\
Test multi-line docstring.

This part is the long description.
    """

# Generated at 2022-06-13 19:37:16.749061
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    text = """\
        Args:
            arg1 (int): The first parameter.
            arg2 (str): The second parameter.
            arg3 (str, optional): The third parameter.

        Returns:
            str: The return value.

        Raises:
            ValueError: If `bar` is equal to `baz`.

        """
    docstring = parser.parse(text)
    assert docstring.short_description == None
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert len(docstring.meta) == 1
    assert docstring.meta[0].description == "The return value."
    assert len(docstring.meta[0].args) == 2

# Generated at 2022-06-13 19:37:29.856762
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
  text = text_from_doc(GoogleParser.parse)
  assert text == """Parse the Google-style docstring into its components.

:returns: parsed docstring"""
  text = text_from_doc(GoogleParser.add_section)
  assert text == """Add or replace a section.

:param section: The new section."""
  text = text_from_doc(GoogleParser)
  assert text == """Setup sections.

:param sections: Recognized sections or None to defaults.
:param title_colon: require colon after section title."""

if __name__ == "__main__":
  for name in dir():
    if name.startswith("test_"):
      print(name)
      eval(name)()

# Generated at 2022-06-13 19:37:34.716766
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    results = GoogleParser().parse("""
    Tests the correct path.
    Raises:
        something
    """)
    results_dict = results._asdict()
    # print(results_dict)
    assert results_dict["short_description"] == "Tests the correct path."
    assert len(results_dict["meta"]) == 1
    assert results_dict["meta"][0].args == ["raises", "something"]
    assert results_dict["meta"][0].description is None

# Generated at 2022-06-13 19:37:40.051823
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse(None) == Docstring()
    assert GoogleParser().parse('') == Docstring()

    with pytest.raises(ParseError) as excinfo:
        GoogleParser().parse('\n    :key: \n    :key: \n')
    assert str(excinfo.value) == 'Can\'t infer indent from ":\n    :key: "'

    with pytest.raises(ParseError) as excinfo:
        GoogleParser().parse('\n    :key: \n:key: \n')
    assert str(excinfo.value) == 'No specification for "key": ":\n:key: "'


# Generated at 2022-06-13 19:37:51.977859
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    source_code = [
        """Test docstring for Google-style."""
    ]

    expected_result = [
        Docstring(
            short_description='Test docstring for Google-style.',
            long_description=None,
            meta=[],
            blank_after_short_description=False,
            blank_after_long_description=False,
        )
    ]

    for source, result in zip(source_code, expected_result):
        assert GoogleParser().parse(source) == result

# Generated at 2022-06-13 19:38:01.956285
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = '''Short description.

    Long description.

    Args:
        first_arg (first_arg_type, optional): Description of first_arg.
            Defaults to None.
        second_arg (second_arg_type): Description of second_arg.
        third_arg (third_arg_type): Description of third_arg.

    Returns:
        Description of return value or values.
        '''
    google_parser = GoogleParser()
    docstring = google_parser.parse(docstring)
    assert docstring.short_description == 'Short description.'
    assert docstring.long_description == 'Long description.'
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description
    assert docstring.meta[0].args == ['param', 'first_arg']

# Generated at 2022-06-13 19:38:08.441733
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse('Adds two numbers together.') == Docstring(short_description='Adds two numbers together.', blank_after_short_description=False, blank_after_long_description=False, long_description=None, meta=[])


# Generated at 2022-06-13 19:38:18.785019
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    description = "This is my description"
    short_desc = "short desc"
    long_desc = "long desc"
    description_with_examples = description + "\nExamples:\n    foo\n    bar\n"
    description_with_example = description + '\n\nExample:\n    foo\n'
    description_with_params = description + "\n\nParameters:\n"
    description_with_example_params = (
        description
        + '\n\nExample:\n    foo\n\nParameters:\n    foo : int\n    bar : str'
    )

# Generated at 2022-06-13 19:38:25.734748
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # case 1
    text = "Summarize the function\n\nDescription of the function."
    docstring = GoogleParser().parse(text)
    if (docstring.short_description != 'Summarize the function') or (docstring.long_description != 'Description of the function.'):
        print("short description: ", docstring.short_description)
        print("long description: ", docstring.long_description)
        print("Error: case 1")

    # case 2
    text = "Summarize the function\n\nArgs:\n  arg1 (int): Argument 1.\n\nReturns:\n  int: The return value."
    docstring = GoogleParser().parse(text)

# Generated at 2022-06-13 19:38:38.808089
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:38:50.774091
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from . import doctest_utils

    doctest_utils.test_doctest(doctest_utils.GoogleParser, "parse")



if __name__ == "__main__":
    import os
    import sys
    import doctest
    import unittest

    this_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, os.path.abspath(os.path.join(this_dir, "..")))

    from . import doctest_utils

    doctest_utils.testmod(
        doctest_utils.GoogleParser, optionflags=doctest.ELLIPSIS
    )

    unittest.main(argv=[sys.argv[0]])

# Generated at 2022-06-13 19:38:58.703059
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:39:02.881823
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def func(arg1, arg2):
        """
        Some docstring examples

        :param arg1: some parameter
        :param arg2: another parameter
        :return:
        """

    docstring = parse(inspect.getdoc(func))
    docstring.meta[0].description == "Some docstring examples"
    docstring.meta[1].description == "some parameter"
    docstring.meta[2].description == "another parameter"
    docstring.meta[3].description == None

# Test for method parse of class GoogleParser with big empty space before docstring

# Generated at 2022-06-13 19:39:11.880133
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import DocstringMeta
    from pprint import pprint
    from .common import Docstring, DocstringParam, DocstringRaises, DocstringReturns
    # No param
    doc = GoogleParser().parse("""A test.
    """)
    assert doc == Docstring(short_description='A test.', long_description=None)

    # Param
    doc = GoogleParser().parse("""A test.

    :param foo: The foo.
    """)
    assert doc == Docstring(
        short_description='A test.',
        long_description=None,
        meta=[DocstringParam(args=['param', 'foo'], description='The foo.', arg_name='foo', type_name=None, is_optional=None, default=None)]
    )

    # Param with type
    doc = GoogleParser().parse

# Generated at 2022-06-13 19:39:24.058088
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    GoogleParser().parse(''' 
        Args:
            text: the text to parse
        Returns:
            parsed docstring
        ''')

    GoogleParser().parse(''' 
        Args:
            text: the text to parse      
        Returns:
            parsed docstring
        ''')
    GoogleParser().parse(''' 
        Args:
            text: the text to parse 
        Description:
            parsed docstring
        ''')
    GoogleParser().parse(''' 
        Args:
            text: the text to parse 
            test:
                the test to parse
            jjj:
                jjjj
        Description:
            parsed docstring
        ''')

# Generated at 2022-06-13 19:39:30.101572
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()

    text = '''A simple example with no detail.

    This is the second paragraph of the docstring.
    '''
    result = parser.parse(text)
    expected = Docstring(
        short_description='A simple example with no detail.',
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description='This is the second paragraph of the docstring.',
        meta=[],
    )
    assert result == expected


# Generated at 2022-06-13 19:39:32.750450
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """
    :param x: parameter x
    :return: 
    """
    assert GoogleParser().parse(docstring).meta[0].args == ["param", "x"]
    assert GoogleParser().parse(docstring).meta[1].args == ["return", ""]


# Generated at 2022-06-13 19:39:41.241730
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = '''First line
    Second line
    
    Some description here.
    More description here.
    
    Parameters
    ----------
    param1 : string
        first parameter
    param2 : int
        second parameter
    
    Returns
    -------
    int
        description of return
    
    Raises
    ------
    KeyError
        when a key error
        is encountered
    '''

    ret = parse(doc)
    print(ret.short_description)
    print(ret.long_description)
    print(ret.meta)
    print(dir(GoogleParser()), '\n\n')

test_GoogleParser_parse()

# Generated at 2022-06-13 19:39:48.446108
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    doc_string = """

    """
    res = parser.parse(doc_string)
    assert res.short_description == None
    assert res.blank_after_short_description == False
    assert res.blank_after_long_description == True
    assert res.long_description == None
    assert len(res.meta) == 0

    doc_string = """
        Short description.

        Longer description.
    """
    res = parser.parse(doc_string)
    assert res.short_description == "Short description."
    assert res.blank_after_short_description == True
    assert res.blank_after_long_description == False
    assert res.long_description == "Longer description."
    assert len(res.meta) == 0


# Generated at 2022-06-13 19:39:59.378868
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    # for param
    # is_optional == None
    text = """
    Foo.
    Foo

    Parameters
    ----------
    x : optional
        foo.
    """
    docstring = parse(text)
    assert docstring
    assert docstring.short_description == "Foo."
    assert docstring.long_description == "Foo"
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == True
    meta = docstring.meta[0]
    assert meta.keys() == ['param', 'x']
    assert meta.description == "foo."
    assert meta.arg_name == "x"
    assert meta.type_name == "optional"
    assert meta.is_optional is None
    assert meta.default is None


    # is_optional

# Generated at 2022-06-13 19:40:08.718975
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
  print("In test_GoogleParser_parse")
  gp = GoogleParser()
  ds = gp.parse("""
    short description

    long description

    Args:
        arg1: description1
          extra description
        arg2: description2
          extra description

    Returns:
        description3
        extra description
    Raises:
        Exception: description5
          extra description

      Attributes:
        attribute1: description1
          extra description
        attribute2: description2
          extra description
  """)

  assert ds.short_description == "short description"
  assert ds.long_description == "long description"
  assert len(ds.meta) == 4

  # Arguments
  assert len(ds.meta[0].args) == 1
  assert ds.meta[0].args[0] == "param"
 

# Generated at 2022-06-13 19:40:17.537562
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = Docstring()
    # Build docstring
    doc.short_description = "A docstring."
    doc.long_description = "This is a description.\n" \
        "This is another line of the description.\n" \
        "\n" \
        "This is a third line of the description.\n"
    param = DocstringParam(
        args=["param", "arg"],
        description="The description.",
        arg_name="arg",
        type_name="str",
        is_optional=True,
        default=None
    )
    returns = DocstringReturns(
        args=["return", "None"],
        description="Description.",
        type_name="None",
        is_generator=False
    )

# Generated at 2022-06-13 19:40:26.894540
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert parse("") == Docstring()
    # Single line short description
    docstring = Docstring(
        short_description="Short description.",
        blank_after_short_description=True,
        blank_after_long_description=False,
    )
    assert parse("Short description.") == docstring
    # Multi line short description
    docstring = Docstring(
        short_description="Short description.",
        blank_after_short_description=False,
        blank_after_long_description=False,
    )
    assert parse("Short description.\n") == docstring
    docstring = Docstring(
        short_description="Short description.",
        blank_after_short_description=False,
        blank_after_long_description=True,
    )
    assert parse("Short description.\n\n") == docstring
    #

# Generated at 2022-06-13 19:40:37.567595
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Empty docstring
    assert parse("") == Docstring()

    # Simple description
    assert parse("This is a simple description.") == Docstring(
        short_description="This is a simple description.",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )

    # Short and long description
    assert parse("This is a short description.\n\nThis is a long description.") == Docstring(
        short_description="This is a short description.",
        long_description="This is a long description.",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[],
    )

    # Long description after one new line

# Generated at 2022-06-13 19:40:55.720931
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstr = '''
        Arguments:
            arg1 (str): the first argument.
            arg2 (str): the second argument. Defaults to "foo".

        Raises:
            ValueError: if something wrong happens
    '''
    ds = GoogleParser().parse(docstr)

    print(ds)
    assert len(ds.meta) == 3
    assert ds.meta[0].args[1] == "arg1 (str)"
    assert ds.meta[1].args[1] == "arg2 (str)"
    assert ds.meta[1].description == "the second argument. Defaults to \"foo\"."
    assert ds.meta[2].args[1] == "ValueError: if something wrong happens"

if __name__ == "__main__":
    test_GoogleParser_parse()