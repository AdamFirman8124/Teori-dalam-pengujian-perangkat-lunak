

# Generated at 2022-06-13 19:31:20.387027
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    A typical Google-style docstring.

    Args:
      param1: Description of `param1`.
      param2: Description of `param2` [default: None].
    Raises:
      KeyError: if unknonw key is encountered.
    Returns:
      Description of return value.
    """
    doc = parse(text)
    assert doc.short_description == "A typical Google-style docstring."
    assert doc.blank_after_short_description == False
    assert doc.long_description == None
    assert doc.blank_after_long_description == False

    assert len(doc.meta) == 3
    param1, param2, raises = doc.meta
    assert isinstance(param1, DocstringParam)
    assert param1.args == ['param', 'param1']
    assert param

# Generated at 2022-06-13 19:31:25.413650
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def foo(x, y, z=42):
        """Example function with types documented in the docstring.

        :param x: int. x param.
        :param y: str. y param.
        :param z: optional int. z param.
        :return: int. int.
        :raises ValueError: if x is not -1 or y is not None.
        """
        pass

    docstring = parse(inspect.getdoc(foo))
    assert docstring.short_description == "Example function with types documented in the docstring."
    assert docstring.long_description == None
    assert docstring.blank_after_long_description == False
    assert docstring.blank_after_short_description == True
    assert docstring.meta[0].args == ['param', 'x: int. x param.']
    assert doc

# Generated at 2022-06-13 19:31:37.552534
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """
    Verifies that the method parse of class GoogleParser works
    """
    text = '''
    This is a module capable of classifying 
    several models of data, such as text,
    images, audio, etc.

    Args:
        arg1 (str): a str variable
        arg2 (str): a str variable
        arg3 (int): a int variable
   
    Returns:
        dict: a dict variable
    '''
    parser = GoogleParser()
    obj = parser.parse(text)
    assert(obj.short_description == 'This is a module capable of classifying several models of data, such as text, images, audio, etc.')
    assert(obj.long_description == None)
    assert(obj.blank_after_short_description == False)

# Generated at 2022-06-13 19:31:50.027699
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    docstring = parser.parse(
        """
        Single-line summary.

        Multiline description.

        Args:
            fun: A function.
            args: Arguments.
        """
    )
    assert docstring.short_description == 'Single-line summary.'
    assert docstring.long_description == 'Multiline description.'
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description
    assert docstring.meta[1].args == ["param", "fun"]
    assert docstring.meta[1].description == 'A function.'
    assert docstring.meta[2].args == ["param", "args"]
    assert docstring.meta[2].description == 'Arguments.'

# Generated at 2022-06-13 19:31:55.399733
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''Summarize your function here.
    Args:
      param1: The first parameter.
      param2: The second parameter.
    Returns:
      The return value. True for success, False otherwise.'''
    parser = GoogleParser()
    # docstring = parser.parse(text)
    # print(docstring.meta)
    # assert False


# Generated at 2022-06-13 19:32:08.772467
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # happy path
    text = '''\
    Args:
        name: str. The name to use.
    Example:
        Use like this.
    '''
    doc = GoogleParser().parse(text)
    assert doc.short_description is None
    assert doc.long_description is None
    assert doc.meta[0].key == 'param'
    assert doc.meta[0].args[0] == 'param'
    assert doc.meta[0].args[1] == 'name'
    assert doc.meta[0].arg_name is None
    assert doc.meta[0].type_name is None
    assert doc.meta[0].description == 'str. The name to use.'
    assert doc.meta[1].key == 'examples'

# Generated at 2022-06-13 19:32:18.240375
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = '''Single line summary.
    Longer description.

    Parameters
    ----------
    a : int
        A number.
    b : bool, optional
        Another number.
    c : bool, optional
        Another number.
    Returns
    -------
    single : int
        Single return.
    Examples
    --------
    >>> a = 5
    '''
    res = GoogleParser().parse(doc)
    assert res.short_description == "Single line summary.", "short description"
    assert res.long_description == "Longer description.", "long description"
    assert res.blank_after_short_description == True, \
        "blank_after_short_description"
    assert res.blank_after_long_description == False, \
        "blank_after_long_description"

# Generated at 2022-06-13 19:32:33.153018
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    # Example 1-----------------------------
    text = '''
    This is an example for method test_GoogleParser_parse with input (text)
    and output (ret), using the class GoogleParser to parse the docstring.

    This method return a Docstring, which is a namedtuple with the following
    fields, in order:
    * short_description (str)
    * blank_after_short_description (bool)
    * long_description (str)
    * blank_after_long_description (bool)
    * meta (list; DocstringMeta instances)

    Args:
        text (str): Google-style docstring to parse.

    Returns:
        Docstring: parsed docstring

    '''

# Generated at 2022-06-13 19:32:44.392439
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser."""
    parser = GoogleParser()
    docstring = parser.parse("Test function.\n\nDescription.\n")
    assert docstring.short_description == "Test function."
    assert docstring.long_description == "Description."

    docstring = parser.parse("Test function.\n")
    assert docstring.short_description == "Test function."
    assert docstring.long_description is None

    docstring = parser.parse("")
    assert docstring.short_description is None
    assert docstring.long_description is None

    try:
        parser.parse("Test function.\n\nDescription:\n")
        assert False
    except ParseError as e:
        assert str(e) == "Expected paramenter name."



# Generated at 2022-06-13 19:32:53.292349
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    print("\n\nUnit test for method parse of class GoogleParser")
    # Test Case 1
    text = """
    Parse the Google-style docstring into its components.
    
    :returns: parsed docstring
    """
    ret = GoogleParser().parse(text)
    if ret.short_description != "Parse the Google-style docstring into its components.":
        raise Exception('Error in test_GoogleParser_parse: wrong short description')
    if ret.blank_after_short_description != True:
        raise Exception('Error in test_GoogleParser_parse: wrong blank_after_short_description')
    if ret.blank_after_long_description != False:
        raise Exception('Error in test_GoogleParser_parse: wrong blank_after_long_description')
    if ret.long_description != None:
        raise Exception

# Generated at 2022-06-13 19:33:10.533001
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    x = GoogleParser().parse(
        """
        Parse the Google-style docstring into its components.

        :returns: parsed docstring
        """
    )
    print(x.short_description)


# def test_GoogleParser_parse_no_returns():
#     x = GoogleParser().parse(
#         """
#         Parse the Google-style docstring into its components.
#         """
#     )
#     print(x.short_description)


# Generated at 2022-06-13 19:33:20.467099
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """
    Args:
        a: first param.
        b (str): second param.
        c (str, optional): third param. Defaults to None.
"""
    entity_list = GoogleParser().parse(docstring).meta
    for entity in entity_list:
        if(entity.args[1]=="a"):
            print(entity.args[1])
            print(entity.description)
            print(entity.arg_name)
            print(entity.type_name)
            print(entity.default)
            print(entity.is_optional)
        elif(entity.args[1]=="b"):
            print(entity.args[1])
            print(entity.description)
            print(entity.arg_name)
            print(entity.type_name)

# Generated at 2022-06-13 19:33:30.970688
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    A module for testing.

    This is a longer description.

    Args:
        arg1: The first argument.
        arg2 (optional, str): The second argument.
            Defaults to 'b'.  And it has two lines.
        arg3: The third argument.
    """
    d = GoogleParser().parse(text)

    assert len(d.meta) == 3

    meta = d.meta[0]
    assert meta.args == ['param', 'arg1']
    assert meta.arg_name == 'arg1'
    assert meta.type_name is None
    assert meta.is_optional is False
    assert meta.default is None
    assert meta.description == "The first argument."

    meta = d.meta[1]

# Generated at 2022-06-13 19:33:41.823906
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
    This is the short description.

    This is the long
    description.

    Attributes
    ----------
    attr1: type
        Description of `attr1`.

    attr2:
        Description of `attr2` without type.

    attr3 (:obj:`int`, optional)
        Description of `attr3`. Defaults to 0.
    '''
    parser = GoogleParser()
    docstring = parser.parse(text)
    print(docstring)



if __name__ == "__main__":
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:33:53.942022
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """"""
    assert GoogleParser().parse(docstring).short_description is None
    assert GoogleParser().parse(docstring).long_description is None
    assert GoogleParser().parse(docstring).blank_after_short_description is False
    assert GoogleParser().parse(docstring).blank_after_long_description is False
    assert GoogleParser().parse(docstring).meta == []

    docstring = """Docstring with no sections."""
    assert GoogleParser().parse(docstring).short_description == "Docstring with no sections."
    assert GoogleParser().parse(docstring).long_description is None
    assert GoogleParser().parse(docstring).blank_after_short_description is True
    assert GoogleParser().parse(docstring).blank_after_long_description is False
    assert GoogleParser().parse(docstring).meta == []



# Generated at 2022-06-13 19:33:58.376121
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = inspect.cleandoc(text="""
    test document

    :param astr: int
    :param bstr: str
    """)
    assert GoogleParser().parse(docstring).meta[0].arg_name == "astr"
    assert GoogleParser().parse(docstring).meta[1].arg_name == "bstr"

# Generated at 2022-06-13 19:34:09.519328
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Cretes a GoogleParser instance
    google_parser = GoogleParser()
    # Creates a docstring containing only short description
    docstring = inspect.cleandoc("""
        This is the short description.
    """)
    # Parses the docstring
    docstring = google_parser.parse(docstring)
    # Asserts the short description
    assert docstring.short_description == "This is the short description."
    # Asserts the long description exists
    assert docstring.long_description == None
    # Asserts the blank after short description not exists
    assert not docstring.blank_after_short_description
    # Asserts the blank after long description exists
    assert docstring.blank_after_long_description

    # Creates a docstring containing short and long descriptions

# Generated at 2022-06-13 19:34:20.691131
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
Args:
  x: A required field.
  y (int): An optional field.
    Defaults to 42.
Returns:
  A
Raises:
  InvalidArgumentError: Raised if `x` is None.
"""
    meta_list = GoogleParser().parse(text)

    assert meta_list.short_description == None
    assert meta_list.long_description == None
    assert meta_list.blank_after_long_description == False
    assert meta_list.blank_after_short_description == False

    assert meta_list.meta[0].args == ['param', 'x: A required field.']
    assert meta_list.meta[0].description == 'A required field.'
    assert meta_list.meta[0].__class__.__name__ == 'DocstringParam'
    assert meta

# Generated at 2022-06-13 19:34:26.037804
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
    """
    This is a docstring.

    This is the long description.

    Params:
        param1 -- parameter 1
        param2 (str) -- parameter 2
        param3 (str, optional) -- parameter 3
        param4 (str) -- parameter 4 [default: value]

    Returns:
        int -- return value
    """
    '''

    ret = GoogleParser()
    ret = ret.parse(text)
    assert ret.short_description == "This is a docstring"

# Generated at 2022-06-13 19:34:35.862521
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:34:48.998552
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser."""

    #  With basic description and parameters.
    docstring = GoogleParser().parse(
        """
    A short description.

    A long description.

    Args:
        arg1: The first argument.
        arg2: The second argument.
    """
    )
    assert docstring.short_description == "A short description."
    assert docstring.long_description == "A long description."
    assert docstring.meta[0].args == ["args", "arg1: The first argument."]
    assert docstring.meta[1].args == ["args", "arg2: The second argument."]

    #  With only short description.
    docstring = GoogleParser().parse("""A short description.""")
    assert docstring.short_description == "A short description."
    assert doc

# Generated at 2022-06-13 19:34:56.027484
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # First check the basic parsing of description and
    # one meta section.
    docstring = parse('''\
        This is a regular docstring

        :param param1: This is a parameter
        :type param1: int
        :returns: description
        :rtype: int
        ''')
    assert docstring.short_description == 'This is a regular docstring'
    assert docstring.long_description is None
    param1 = docstring.get_params()
    assert param1.description == 'This is a parameter'
    assert param1.type_name == 'int'
    assert param1.arg_name == 'param1'
    assert param1.is_optional is None
    assert param1.default is None
    returns = docstring.get_returns()
    assert returns.description == 'description'
   

# Generated at 2022-06-13 19:35:04.776510
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .examples import DOCSTRING_GOOGLE
    docstring = GoogleParser().parse(DOCSTRING_GOOGLE)
    assert docstring.short_description == "Example google-style docstring."
    assert docstring.meta[0].arg_name == "param1"
    assert docstring.meta[2].arg_name == "param3"

if __name__ == "__main__":
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:35:12.811389
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import _load_docstring
    from .common import _parse_docstring
    pgg = GoogleParser().parse
    pr = _parse_docstring
    ld = _load_docstring
    assert repr(pgg(ld('docstrings/mod.py'))) == repr(pr(ld('docstrings/mod.py')))
    assert repr(pgg(ld('docstrings/Foo.py'))) == repr(pr(ld('docstrings/Foo.py')))
    assert repr(pgg('\n')) == repr(pr('\n'))
    assert repr(pgg('   \n')) == repr(pr('   \n'))
    assert repr(pgg('\n   \n')) == repr(pr('\n   \n'))

# Generated at 2022-06-13 19:35:24.084702
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    gp = GoogleParser()
    docstring = """Short desription.

    Long description.

    Args / Arguments:

    Example:

    Examples:

    Attributes:

    """
    result = gp.parse(docstring)
    assert result.short_description == "Short desription."
    assert result.long_description == "Long description."
    assert len(result.meta) == 4
    assert isinstance(result.meta[0], DocstringMeta)
    assert result.meta[0].args == ['Args / Arguments']
    assert result.meta[0].description == ''
    assert isinstance(result.meta[1], DocstringMeta)
    assert result.meta[1].args == ['Example']
    assert result.meta[1].description == ''
    assert isinstance(result.meta[2], DocstringMeta)

# Generated at 2022-06-13 19:35:34.890396
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = ("""blabla.

blabla.

:param arg1: Parameter description.

:param arg2: Parameter description.
""")
    docstring_meta_1 = DocstringParam(args=["param", "arg1"], description="Parameter description.", arg_name="arg1", type_name=None, is_optional=None, default=None)
    docstring_meta_2 = DocstringParam(args=["param", "arg2"], description="Parameter description.", arg_name="arg2", type_name=None, is_optional=None, default=None)

# Generated at 2022-06-13 19:35:51.362983
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """
    Test parse method of class GoogleParser
    """

# Generated at 2022-06-13 19:35:59.267610
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    # test GoogleParser.parse function
    def test_class_google_parser():
        
        # test GoogleParser.parse function with empty docstring
        def test_empty_docstring():

            # get the result for parse an empty docstring
            result = GoogleParser().parse("")

            # get the expected result
            expected_result = Docstring()

            # notify that the test has been successfull
            print("Test successfull")

            # return the result
            return result, expected_result

        # test GoogleParser.parse function with only a short description docstring
        def test_short_description_docstring():

            # get the result for parse a docstring with only a short description
            result = GoogleParser().parse("This is a short description.")

            # get the expected result

# Generated at 2022-06-13 19:36:06.240457
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()

    # test parse
    doc = parser.parse("")
    assert all((
        doc.short_description,
        doc.long_description,
        doc.blank_after_short_description,
        doc.blank_after_long_description,
        doc.meta,
    )), "Empty docstring produced bad result"

    doc = parser.parse("Test string.")
    assert all((
        doc.short_description == "Test string.",
        doc.long_description,
        doc.blank_after_short_description,
        doc.blank_after_long_description,
        doc.meta,
    )), "Test string produced bad result"

    doc = parser.parse("Test string.\n")

# Generated at 2022-06-13 19:36:14.947418
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Asserting if the docstring parsed is correct
    docstring = GoogleParser().parse("""
        Args:
            param1 (int): The first parameter.
            param2 (str): The second parameter.
            param3 (Optional[int]): The third parameter.
                Defaults to 0. 
            param4 (str, optional): The fourth parameter.
                Defaults to 'a'.
            param5 (str, Optional[int]): The fifth parameter.
                Defaults to 'word'.

        Raises:
            ValueError: If `bar` is less than `foo`.
            ValueError: If `baz` is less than 10.
""")

    assert docstring.meta[0].arg_name == 'param1'
    assert docstring.meta[0].type_name == "int"

# Generated at 2022-06-13 19:36:25.235616
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc_str = \
"""Google-style short summary.

Longer description in Google-style.

Longer description in Google-style.

Longer description in Google-style.

Example:
  This is an example.
  This is an example.
  This is an example.

Returns:
  Longer description in Google-style.
  Longer description in Google-style.
  Longer description in Google-style.

Yields:
  Longer description in Google-style.
  Longer description in Google-style.
  Longer description in Google-style.
"""
    doc = GoogleParser().parse(doc_str)
    assert doc.short_description == "Google-style short summary."
    assert doc.blank_after_short_description

# Generated at 2022-06-13 19:36:36.586266
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    def assert_docstring(docstring, expected, warn = True):
        def assert_cell_value(cell, expected):
            assert cell.get_value() == expected

        def assert_docstring_param(param, expected):
            assert_cell_value(param.name, expected[0])
            assert_cell_value(param.type_name, expected[1])
            assert_cell_value(param.desc, expected[2])
            assert_cell_value(param.default, expected[3])

        def assert_docstring_return(return_, expected):
            assert_cell_value(return_.type_name, expected[0])
            assert_cell_value(return_.desc, expected[1])


# Generated at 2022-06-13 19:36:45.476669
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Test method parse of class GoogleParser"""
    # Unit test without a docstring
    text0 = ""
    expected0 = Docstring()
    expected0.meta = []
    expected0.short_description = None
    expected0.blank_after_short_description = False
    expected0.blank_after_long_description = False
    expected0.long_description = None
    assert parse(text0) == expected0

    # Unit test with a single paragraph docstring
    text1 = "Calculate the mean and standard deviation of data, given in a real vector X."
    expected1 = Docstring()
    expected1.meta = []
    expected1.short_description = "Calculate the mean and standard deviation of data, given in a real vector X."
    expected1.blank_after_short_description = False
    expected1.blank

# Generated at 2022-06-13 19:36:58.527414
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    A function that does something.

    Args:
        x: Something you want to pass.
        y: Something else.

    Returns:
        The thing.
    """
    doc_string = GoogleParser().parse(text)
    assert doc_string.short_description == "A function that does something."
    assert doc_string.long_description == (
        "Something you want to pass.\n"
        "\n"
        "Something else."
    )
    assert doc_string.meta[0].args == ["args", "x"]
    assert doc_string.meta[0].arg_name == "x"
    assert doc_string.meta[0].type_name == None
    assert doc_string.meta[0].description == "Something you want to pass."

# Generated at 2022-06-13 19:37:07.776300
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import textwrap

# Generated at 2022-06-13 19:37:16.415547
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """Summary line
    Extended description

    Args:
      arg1: Description of `arg1`.
      arg2: Description of `arg2` [default: 42].

    Returns:
      Description of return value.
    """


# Generated at 2022-06-13 19:37:28.722407
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:37:35.237322
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Case 1
    text = """
    Args:
        name (str): The name of the new object.
    Raises:
        ValueError: If the object name is not valid.

    Returns:
        int: The index of the new object.
    """
    # print(len(GoogleParser().parse(text).returns))
    assert len(GoogleParser().parse(text).returns) == 1

    # Case 2
    text = """
    Args:
        name (str): The name of the new object.
    Raises:
        ValueError: If the object name is not valid.

    Returns:
        int: The index of the new object.
        str: The index of the new object.
    """
    assert len(GoogleParser().parse(text).returns) == 2

    # Case 3

# Generated at 2022-06-13 19:37:40.547665
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """
    Google style docstring parser should parse docstring.
    """
    test_docstring = """
    Test docstring.

    This is a test docstring, used to check if the google docstring
    parser can parse it correctly.

    Parameters
    ----------
    name : str
        Name of the person.
    age : int
        Age of the person.
    Returns
    -------
    result : bool
        Result of the test.
    """

# Generated at 2022-06-13 19:37:50.359008
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:38:03.326030
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    source_code = """Google-style docstring parsing.

:param sections: Recognized sections or None to defaults.
:param title_colon: require colon after section title.
:return:
:raises ParseError: if an error occurs
"""
    test1 = GoogleParser().parse(source_code)
    assert isinstance(test1, Docstring)
    assert test1.short_description == 'Google-style docstring parsing.'
    assert test1.long_description == ":param sections: Recognized sections or None to defaults." \
                                     "\n:param title_colon: require colon after section title." \
                                     "\n:return:" \
                                     "\n:raises ParseError: if an error occurs"
    assert test1.blank_after_short_description
    assert not test1.blank_after_long_description

# Generated at 2022-06-13 19:38:09.583120
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():


    parser = GoogleParser()

# Generated at 2022-06-13 19:38:19.250399
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:38:26.120976
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """\
    short description
    long_description
    long_description
    long_description
    Args:
        a:
            aaa
            aaa
        b:
            bbb
            bbb
    Parameter:
        c:
            ccc
            ccc
    Parameters:
        d:
            ddd
            ddd
    Returns:
        eee
    Example:
        eee
    Examples:
        eee
    Exceptions:
        fff
    """
    result = GoogleParser().parse(text)
    assert result.short_description == "short description"
    assert result.blank_after_short_description
    assert result.long_description == "long_description\nlong_description\nlong_description"
    assert result.blank_after_long_description

# Generated at 2022-06-13 19:38:39.054900
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    # Tests for parse
    text = '''Single returns paragraph.
    '''
    assert parser.parse(text).meta[0].args == ['returns', 'Single returns paragraph.']
    # Tests for parse
    text = '''Returns:
        Single returns paragraph.
    '''
    assert parser.parse(text).meta[0].args == ['returns', 'Single returns paragraph.']
    # Tests for parse
    text = '''Returns:
        Single returns paragraph.
        
        Indented.
    '''
    assert parser.parse(text).meta[0].description == 'Single returns paragraph.\n\nIndented.'
    # Tests for parse
    text = '''Returns:
        Single returns paragraph.

        Indented.
    '''

# Generated at 2022-06-13 19:38:51.437424
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from collections import namedtuple

    TestParameters = namedtuple("TestParameters", ["text", "expected"])


# Generated at 2022-06-13 19:38:56.882819
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    import unittest

    from .common import Docstring, DocstringMeta, DocstringParam, DocstringRaises, DocstringReturns

    parser = GoogleParser()
    class TestGoogleParserParse(unittest.TestCase):
        def test_docstring_with_only_description_is_parsed_correclty(self):
            docstring = parser.parse("""This is a description""")
            self.assertEqual(docstring,
                             Docstring(
                                 'This is a description', None, False,
                                 False, None, [], None, None, None, [], [], [],
                                 [], None, None, []))


# Generated at 2022-06-13 19:39:00.836838
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = GoogleParser().parse(
    '''
    O(n)
    Returns the number of times that ``item`` occurs in the list.

    Parameters
    ----------
    item : str
        Some item you are looking for in the list.

    Returns
    -------
    count : int, > 0
        The number of times that ``item`` appears in the list.

    '''
)
    assert docstring.short_description == 'Returns the number of times that ``item`` occurs in the list.'


# Generated at 2022-06-13 19:39:10.678670
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    print("----------------------------\n"\
    + "* Testing method parse from class GoogleParser *\n"\
    + "----------------------------")
    # Function to define the example docstring
    def example_func():
        """\
        First line (short description).
    
        This is the main part of the docstring. It can span over multiple
        lines.
    
        Arguments:
            arg1 (int): First argument.
            arg2 (str): Second argument.
    
        Returns:
            bool: Whether the function did its job.
        """
        pass
    example_docstring = inspect.getdoc(example_func)
    # Get the actual result of the parse method
    actual_result = parse(example_docstring)
    # Define expected result
    expected_result = Docstring()
    expected_result.short_

# Generated at 2022-06-13 19:39:21.243024
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    # Test with no docstring
    assert GoogleParser().parse("") == Docstring()

    # Test with one line docstring
    parsed = GoogleParser().parse("A short description.")
    assert parsed.short_description == "A short description."

    # Test with one paragraph
    parsed = GoogleParser().parse("A short description.\n\nA long description.")
    assert parsed.short_description == "A short description."
    assert parsed.long_description == "A long description."
    assert parsed.blank_after_short_description
    assert parsed.blank_after_long_description

    # Test with two paragraphs
    parsed = GoogleParser().parse("A short description.\n\nA long description.\n\nAnother long description.")
    assert parsed.short_description == "A short description."

# Generated at 2022-06-13 19:39:32.650900
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    test_doc_string0 = '''This is a Google-style docstring, and
    the elements are parsed out.

    Here, the first paragraph is the short description.
    Second line, which is the long description.
    '''

    test_doc_string1 = '''This is a Google-style docstring, and
    the elements are parsed out.

    Args:
      param1 (:obj:`int`): The first parameter.
      param2 (:obj:`str`, optional): The second parameter. Defaults to 'Hello'.

    Returns:
      :obj:`tuple` of :obj:`int` and :obj:`str`: A tuple of an integer and string.
    '''


# Generated at 2022-06-13 19:39:34.810169
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    gp = GoogleParser()
    print(gp.parse.__doc__)

test_GoogleParser_parse()

# Generated at 2022-06-13 19:39:44.259265
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
        The docstring in this function has three sections: Parameters, Returns, and Example.

        :param x: a number representing a vector in space
        :param y: a number representing a vector in space
        :returns: a number representing a vector in space

        >>> vector_addition(1, 1)
        2
    """
    res = GoogleParser.parse(text)
    assert res.short_description is None
    assert res.long_description is None
    assert res.blank_after_short_description is False
    assert res.blank_after_long_description is False
    assert len(res.meta) == 4
    assert res.meta[0].args == ['x']
    assert res.meta[0].description == 'a number representing a vector in space'
    assert res.meta[1].args == ['y']


# Generated at 2022-06-13 19:39:49.106482
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Returns
    assert GoogleParser().parse("Returns:\n").short_description == None
    assert GoogleParser().parse("Returns:\n").long_description == None
    assert GoogleParser().parse("Returns:\n").meta == [
        DocstringMeta(args=["returns"], description=None)
    ]
    assert GoogleParser().parse("Returns: a\n").meta == [
        DocstringMeta(args=["returns"], description="a")
    ]
    assert GoogleParser().parse("Returns: a\n\nb").meta == [
        DocstringMeta(args=["returns"], description="a\n\nb")
    ]
    # Returns, return -> Returns
    assert GoogleParser().parse("return:\nb").meta == [
        DocstringMeta(args=["returns"], description="b")
    ]

# Generated at 2022-06-13 19:39:59.867627
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = "A short description.\nA long description.\n\nArgs:\nstring: An input string.\nint: An integer number."
    parser = GoogleParser()
    docstring_parsed = parser.parse(docstring)
    assert docstring_parsed.long_description == "A long description."
    assert docstring_parsed.short_description == "A short description."
    assert docstring_parsed.meta[0].description == "An input string."
    assert docstring_parsed.meta[1].description == "An integer number."
    assert docstring_parsed.meta[0].arg_name == "string"
    assert docstring_parsed.meta[1].arg_name == "int"
    assert len(docstring_parsed.meta) == 2

# Generated at 2022-06-13 19:40:01.240719
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    google_parser = GoogleParser()



# Generated at 2022-06-13 19:40:07.130081
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
    """
    Google-style docstring parsing.

    :param sections: Recognized sections or None to defaults.
    :param title_colon: require colon after section title.
    :returns: parsed docstring
    """'''
    parse(text)

# Generated at 2022-06-13 19:40:16.860655
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from inspect import cleandoc
    google_parser = GoogleParser()
    docstring = cleandoc("""
    This is the short description.

    This is the long description.

    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.
    Returns:
        int: The return value.
    Raises:
        ValueError: Raises an exception.
    """)

# Generated at 2022-06-13 19:40:19.608269
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser"""
    # TODO: Add tests
    pass

# Generated at 2022-06-13 19:40:27.651165
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    google_parser = GoogleParser()
    text = 'Description of the method\n\n    :param param1: this is a first param\n    :type param1: int\n    :param param2: this is a second param\n    :type param2: str\n    :param param3: this is a third param\n    :type param3: list\n    :returns: None\n\n'

# Generated at 2022-06-13 19:40:47.099162
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doctest_string = """Function description.
    
    Args:
        param1 (int): Parameter 1 description.
        param2 (str): Parameter 2 description.
    
    Returns:
        dict: Returns description.
    
    Raises:
        AttributeError:  Error description.
    """
    docstring = GoogleParser().parse(doctest_string)
    
    assert docstring.short_description == "Function description."
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == True

    assert docstring.meta[0].description == "Parameter 1 description."
    assert docstring.meta[0].args[0] == "param1"
    assert docstring.meta[0].args[1] == "int"
    assert docstring.meta[0].type_name