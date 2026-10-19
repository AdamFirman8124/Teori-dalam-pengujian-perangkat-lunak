

# Generated at 2022-06-13 19:31:20.912062
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    google_parser = GoogleParser()
    docstring = google_parser.parse('Parse the Google-style docstring into its components.\n\nReturns:\n    parsed docstring')
    assert docstring.short_description == 'Parse the Google-style docstring into its components.'
    assert docstring.long_description == 'Returns:\nparsed docstring'
    assert docstring.meta[0].args == ['returns', 'Returns']
    assert docstring.meta[0].arg_name == 'Returns'
    assert docstring.meta[0].description == 'parsed docstring'
    assert docstring.meta[0].type_name == 'Returns'
    assert docstring.meta[0].is_generator == False


# Generated at 2022-06-13 19:31:23.736699
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    d = Docstring('test', 'test', ['test'], 'test')
    assert(GoogleParser().parse('test') == d)


# Generated at 2022-06-13 19:31:36.253882
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # json file read in
    import json
    from .common import DOCSTRINGS
    # datasets
    ds_dir = '../datasets/'
    fname = ds_dir + 'docstrings.json'
    # read json file
    with open(fname) as f:
        data = json.load(f)
    #
    print("# =================================")
    print("# Functionality test")
    print("# =================================")
    #
    # test
    ds = GoogleParser().parse(data[DOCSTRINGS[0]])
    ds1 = GoogleParser().parse(data[DOCSTRINGS[3]])
    ds2 = GoogleParser().parse(data[DOCSTRINGS[4]])
    ds3 = GoogleParser().parse(data[DOCSTRINGS[5]])

# Generated at 2022-06-13 19:31:49.725890
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:31:55.180237
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
        """

    result = GoogleParser().parse(text)
    assert(result.short_description is None)
    assert(result.blank_after_short_description == False)
    assert(result.blank_after_long_description == False)
    assert(result.long_description is None)
    assert(result.meta == [])



# Generated at 2022-06-13 19:31:58.306224
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    method = inspect.getfullargspec(GoogleParser.parse).args
    assert method ==  ['self','text']


# Generated at 2022-06-13 19:32:10.169988
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse('  A short description.\nA short description.\n') == Docstring(short_description='A short description.', blank_after_short_description=True, long_description='A short description.', blank_after_long_description=False, meta=[])
    assert GoogleParser().parse('  A short description.\n\nA short description.\n') == Docstring(short_description='A short description.', blank_after_short_description=False, long_description='A short description.', blank_after_long_description=False, meta=[])

# Generated at 2022-06-13 19:32:19.006219
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = GoogleParser().parse(
        """__init__(self, num_blocks=[3, 4, 6, 3], expansion=6, bottleneck_width=[1, 2, 4, 4])

        Building Block of MobileNetV2

        Args:
            num_blocks (list): Number of blocks in each block_layer.
            expansion (int): Width multiplier.
            bottleneck_width (list): Width of each bottleneck layer.
            """
    )
    if docstring.short_description == "Building Block of MobileNetV2":
        print("short description is correct")
    else:
        print("short description is not correct")

    # print(docstring.meta)

# Generated at 2022-06-13 19:32:20.954339
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    GoogleParser_test = GoogleParser()
    output = GoogleParser_test.parse("test_method")
    print(output)



# Generated at 2022-06-13 19:32:28.171610
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # No input
    docstring = GoogleParser().parse('')
    assert docstring.short_description is None
    assert docstring.long_description is None

    # Short description only
    docstring = GoogleParser().parse('Short description.')
    assert docstring.short_description == 'Short description.'
    assert docstring.long_description is None
    assert docstring.meta == []

    # Long description only
    docstring = GoogleParser().parse(
        'Short description.\n'
        '\n'
        'Long description.')
    assert docstring.short_description == 'Short description.'
    assert docstring.long_description == 'Long description.'
    assert docstring.meta == []

    # Long description only with two newlines after short description

# Generated at 2022-06-13 19:32:37.951216
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    expected = {
        "short_description": None,  # 'My class',
        "long_description": None,  # 'Longer description of my class',
        "blank_after_short_description": False,
        "blank_after_long_description": False,
        "meta": [
            {"args": ["param", "f"], "arg_name": "f",
                "description": "The param.", "type_name": "float"}],
    }
    docstr = GoogleParser().parse('''
        My class

        Longer description of my class

        Args:
            f (float): The param.
    ''')
    for key in expected:
        assert expected[key] == getattr(docstr, key)

# Generated at 2022-06-13 19:32:45.520427
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()

    doc = '''One line summary.

Long description.

Arguments:
  a (int): First integer.
  b (int): Second integer.

Returns:
  int: Sum of integers.

Raises:
  TypeError: If bad things happen.'''

    ds = parser.parse(doc)
    assert len(ds.meta) == 5
    assert ds.short_description == "One line summary."
    assert ds.long_description == "Long description."
    assert ds.meta[0].__class__.__name__ == "DocstringParam"
    assert ds.meta[0].arg_name == "a"
    assert ds.meta[0].type_name == "int"
    assert ds.meta[0].description == "First integer."

# Generated at 2022-06-13 19:32:53.886868
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    print("Testing class GoogleParser and method parse")

    ds = """
    This is the short description.

    This is the long description. It can have multiple lines.
    """

    print("    Testing docstring:\n\n{}".format(ds))

    print("    Expected output:")

    ds_expected = Docstring(
        short_description="This is the short description.",
        blank_after_short_description=True,
        long_description="This is the long description. It can have multiple lines.",
        blank_after_long_description=True,
        meta=[],
    )


# Generated at 2022-06-13 19:33:05.404828
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    d = parser.parse("""Summary line.

        Extended description of function.

        Parameters
        ----------
        arg1 : int
            Description of `arg1`

        arg2 : str
            Description of `arg2`

        Returns
        -------
        int
            Description of return value

        Raises
        ------
        ValueError
            If `arg2` is equal to `arg1`.
        """)
    assert d.short_description == "Summary line."
    assert d.blank_after_short_description
    assert d.long_description == "Extended description of function."
    assert d.blank_after_long_description
    assert len(d.meta) == 3
    assert d.meta[0].description == "Description of `arg1`"

# Generated at 2022-06-13 19:33:16.894786
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    assert parser.parse('') == "{}"
    assert parser.parse('this') == "{'short_description': 'this'}"
    assert parser.parse(' this') == "{'short_description': 'this'}"
    assert parser.parse('  this') == "{'short_description': 'this'}"
    assert parser.parse('\nthis') == "{'short_description': 'this'}"
    assert parser.parse('\n this') == "{'short_description': 'this'}"
    assert parser.parse('\n\nthis') == "{'short_description': 'this'}"
    assert parser.parse('\n this\n') == "{'short_description': 'this'}"
    assert parser.parse('  this\n') == "{'short_description': 'this'}"

# Generated at 2022-06-13 19:33:23.532489
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser_ = GoogleParser()
    mock_self = MagicMock()
    arg0 = MagicMock(spec=str)
    arg1 = MagicMock(spec=str)
    arg2 = MagicMock(spec=str)

    def _se(arg0, arg1, arg2):
        mock_self._setup()
        mock_self.sections = {arg0: arg1}
        mock_self.title_colon = arg2

        # Mock return value
        ret = MagicMock(spec=Docstring)

        return ret

    # Set up context manager mock
    with patch.object(GoogleParser, "__init__", _se):
        # Call method
        ret = parser_.parse(arg0)

    # Check return value
    assert ret is ret


# Generated at 2022-06-13 19:33:28.346031
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """

         A short summary
         -----------

         A long description

         Arguments
         ----------
         arg1 : int
             Description of arg1.

         arg2 : int
             Description of arg2.

         Returns
         ----------

         A short summary
         -----------

         A long description

         Arguments
         ----------
         arg1 : int
             Description of arg1.

         arg2 : int
             Description of arg2.

         Returns
         ----------
         """

    assert(parse(text).short_description == 'A short summary')
    assert(parse(text).long_description == 'A long description\n')
    assert(parse(text).blank_after_short_description == False)
    assert(parse(text).blank_after_long_description == False)

# Generated at 2022-06-13 19:33:36.264098
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Test
    print("Parse 'Returns' section")
    text = """\
    Returns a list of the numbers 1, 2 and 3
    """
    print("Input: " + text)
    print("Output: ", GoogleParser().parse(text))
    print("\n")

    print("Parse 'Raises' section")
    text = """\
    Raises:
        TypeError: if its argument is not a number
    """
    print("Input: " + text)
    print("Output: ", GoogleParser().parse(text))
    print("\n")

    print("Parse 'Yields' section")
    text = """\
    Yields:
        int: The next number in the iterator.
    """
    print("Input: " + text)
    print("Output: ", GoogleParser().parse(text))

# Generated at 2022-06-13 19:33:48.423439
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc = """
    Test test test.

    Args:
        a (int): Test parameter
        b (str): Test parameter

    Returns:
        int

    Raises:
        TestError: Test
    """


# Generated at 2022-06-13 19:33:56.404115
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    gp = GoogleParser()
    testDocs = ["", "b", "b\nc", "b\nc\nd"]
    for testDoc in testDocs:
        print("\ntestDoc = {}".format(testDoc))
        ds = gp.parse(testDoc)
        print("ds = {}".format(ds))
    # Halt
    raise Exception("STOP")


GOOGLE_PARSER = GoogleParser()


parse_google = GOOGLE_PARSER.parse

# Generated at 2022-06-13 19:34:11.521783
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """This is an example docstring.
    This is the first line of a long description.

     This is the second line of the long description.

    Args:
        arg1 (str): The first argument.
        arg2 (str): The second argument.

    Returns:
        str: The return value.
    """
    result = parse(text)
    assert result.short_description == "This is an example docstring."
    assert result.long_description == "This is the first line of a long description.\n\n This is the second line of the long description.\n"
    assert result.blank_after_short_description == True
    assert result.blank_after_long_description == True
    assert result.meta[0].args == ['param', 'arg1 (str)']

# Generated at 2022-06-13 19:34:22.811316
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
    This is a test for the GoogleParser and the method parse
    '''
    assert GoogleParser().parse(text) == Docstring(meta=[])
    text = '''
    This is a test
    :param x: The x coordinate
    '''
    assert GoogleParser().parse(text) == Docstring(meta=[])
    text = '''
    This is a test
    :param x: The x coordinate
    :type x: int

    :returns: The x coordinate
    :rtype: int
    '''
    assert GoogleParser().parse(text) == Docstring(meta=[])

# Generated at 2022-06-13 19:34:33.237298
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from pydoctor.docwriter.rest import ReSTWriter
    from pydoctor.model.classdef import ClassDef
    from pydoctor.model.module import Module
    from pydoctor.model.function import Function

    test_inst = GoogleParser()
    dummy_cls = ClassDef(None, "dummy_cls", None, None)
    dummy_mod = Module(None, "dummy_mod", None)
    dummy_func = Function(None, "dummy_func", None)
    dummy_cls.obj = dummy_cls
    dummy_mod.obj = dummy_mod
    dummy_func.obj = dummy_func
    # test the method parse with a couple of example docstring
    # test parse with default args
    print(test_inst.parse(dummy_cls.docstring()).meta)

# Generated at 2022-06-13 19:34:38.260259
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """\
This is a sample module.


Args:
    param1: This is the first param.
    param2: This is a second param.


Returns:
    This is a description of what is returned.
    This is a description of what is returned.

    :returns: This is a description of what is returned.
    :rtype: str
"""

# Generated at 2022-06-13 19:34:46.618282
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    The short version.

    The long version.

    Parameters
    ---------
    arg1 : str
        First argument.
    arg2 : int, optional
        Second argument. Defaults to 42.

    Returns
    -------
    None
        No return.
    """

    doc = parse(text)
    # print(doc)
    assert doc.short_description == "The short version."
    assert doc.long_description == "The long version."
    assert doc.meta[0].args == ["param", "arg1 : str\n        First argument."]
    assert doc.meta[1].args == [
        "param",
        "arg2 : int, optional\n        Second argument. Defaults to 42.",
    ]

# Generated at 2022-06-13 19:34:55.066523
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import Docstring, DocstringMeta
    from .common import DocstringParam, DocstringRaises, DocstringReturns

    # Examples
    docstring = '''
    Short description.

    Long description.

    Args:
        arg1 (int): Description of arg1.
        arg2 (str, optional): Description of arg2. Defaults to 'default'.
        arg3 (bool, optional): Description of arg3. Defaults to True.

    Returns:
        int: Description of return value.
    '''

# Generated at 2022-06-13 19:35:04.272790
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = ':param param1: Parameter one. \n\n:param param2: Parameter two.\n'

    parsed_docstring = parse(text)

    assert parsed_docstring.short_description == None
    assert parsed_docstring.long_description == None
    assert parsed_docstring.blank_after_short_description == True
    assert parsed_docstring.blank_after_long_description == False

    assert len(parsed_docstring.meta) == 2

 
    assert parsed_docstring.meta[0].args[0] == "param"
    assert parsed_docstring.meta[0].args[1] == "param1"
    assert parsed_docstring.meta[0].description == "Parameter one."

    assert parsed_docstring.meta[1].args[0] == "param"
   

# Generated at 2022-06-13 19:35:10.488587
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    text = """
    A.
    B.
    C.

    Arguments:
      arg0 (:obj:`int`, optional): 1. Defaults to 0.
      arg1 (:obj:`int`, optional): 2. Defaults to 1.
    """
    text = inspect.cleandoc(text)
    parse(text)


if __name__ == "__main__":

    test_GoogleParser_parse()

# Generated at 2022-06-13 19:35:19.750091
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():


    text_input = """Short summary.

Long description.

Params:
    arg1 (str): Parameter 1.
    arg2 (str): Parameter 2.

Example:
    >>> a = 1
    >>> b = 2
    >>> c = a + b
    >>> c
    3
    """
    parser = GoogleParser()
    docstring = parser.parse(text_input)
    assert len(docstring.meta) == 5


# Generated at 2022-06-13 19:35:30.865364
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring="""
        Google-style docstring parser.

        Short Description.

        Long Description.

        :Args:
            - p: *int*, **required**.
            - q: *int*, **optional**. Defaults to 0.

        :Examples:
            >>> p = 1
            >>> q = 0
            >>> print(p + q)
            1
        """
    docstring_dict=GoogleParser().parse(docstring)
    print(docstring_dict)

if __name__ == "__main__":
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:35:39.777830
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("") == Docstring()
    # Check if the case of docstrings without sections are correctly parsed
    assert GoogleParser().parse("short-desc\n\nlong-desc") == Docstring(
        short_description="short-desc",
        blank_after_short_description=True,
        blank_after_long_description=True,
        long_description="long-desc",
    )
    assert GoogleParser().parse("short-desc\nlong-desc") == Docstring(
        short_description="short-desc",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description="long-desc",
    )

# Generated at 2022-06-13 19:35:48.055136
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    """Unit test for method parse of class GoogleParser"""
    parser = GoogleParser()

# Generated at 2022-06-13 19:35:57.093201
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    text1 = '''
        \tThis is short description.

        This is long description.
        Bla bla bla.
        '''
    enter = parser.parse(text1)
    assert enter.short_description == 'This is short description.'
    assert enter.long_description == 'This is long description.\nBla bla bla.'
    assert enter.blank_after_short_description == False
    assert enter.blank_after_long_description == True
    
    text2 = '''
        \tThis is short description

        This is long description.
        Bla bla bla.
        '''
    enter = parser.parse(text2)
    assert enter.short_description == 'This is short description'

# Generated at 2022-06-13 19:36:03.944093
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Test docstring not given
    ret = GoogleParser().parse(text = '')
    assert ret.short_description == None
    assert ret.long_description == None
    assert ret.meta == []
    assert 'Docstring' in ret.__str__()
    assert 'short_description=None' in ret.__str__()
    assert 'long_description=None' in ret.__str__()
    assert 'meta=[]' in ret.__str__()
    assert 'blank_after_short_description=' in ret.__str__()
    assert 'blank_after_long_description=' in ret.__str__()

    # Test docstring given
    ret = GoogleParser().parse("""
    Test docstring.
    """)
    assert ret.short_description == 'Test docstring.'

# Generated at 2022-06-13 19:36:09.275153
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()
    text = "The __init__ method.\n    Example:\n" \
           "        self.arg = arg\n\n" \
           "    Args:\n" \
           "        arg: The argument.\n\n" \
           "    Returns:\n" \
           "        Nothing\n"
    result = parser.parse(text)
    assert result.short_description == "The __init__ method."
    assert result.long_description == "Example:        self.arg = arg"
    assert result.blank_after_long_description == True
    assert result.blank_after_short_description == True
    assert len(result.meta) == 3
    assert result.meta[0].description == "The argument."
    assert result.meta[0].arg_name == "arg"
   

# Generated at 2022-06-13 19:36:20.584767
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # []
    parser = GoogleParser()
    docstring = parser.parse('')
    assert docstring.meta == []
    assert docstring.short_description == None
    assert docstring.long_description == None
    # ['\n']
    docstring = parser.parse('\n')
    assert docstring.meta == []
    assert docstring.short_description == None
    assert docstring.long_description == None
    # ['\n\n']
    docstring = parser.parse('\n\n')
    assert docstring.meta == []
    assert docstring.short_description == None
    assert docstring.long_description == None
    # ['    \n']
    docstring = parser.parse('    \n')
    assert docstring.meta == []
    assert docstring.short_description == None
   

# Generated at 2022-06-13 19:36:25.277271
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Arrange
    text_test = '''

Method to parse a docstring

Args:
    arg_test (str): Description of test
    arg_test2 (str): Description of test2
    arg_test3 (str): Description of test3

Returns:
    None
    '''

    # Act
    result = parse(text_test)

    return


# Generated at 2022-06-13 19:36:36.626422
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:36:42.961756
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """\
    One line summary.

    Further description.

    Examples
    --------

        >>> a = 1
        >>> a
        1

    Parameters
    ----------
    xyz : str, optional
        The length of a side of the cube.

    Attributes
    ----------
    attr1 : str
        Bar.

        Class A
        Class B
        Class C

    attr2 : int
        Baz.
        Class A
        Class B

    Returns
    -------
    volume : float
        The volume of a cube.

    Yields
    ------
    volume : float

    Raises
    ------
    ValueError
        If `xyz` is not a positive integer.
    """
    dr = parse(text)
    assert dr.short_description == 'One line summary.'
    assert dr.long_description

# Generated at 2022-06-13 19:36:56.332345
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    return
    # Docstring with only description
    docstring = GoogleParser().parse("""Description""")
    assert docstring.short_description == "Description"
    assert docstring.long_description is None
    assert docstring.meta == []

    # Docstring with description and two sections
    docstring = GoogleParser().parse(
        """Description
    Section 1:
        chunk 1
    Section 2:
        chunk 2"""
    )
    assert docstring.short_description == "Description"
    assert docstring.long_description is None
    assert len(docstring.meta) == 2
    assert docstring.meta[0].args == ("Section 1", "chunk 1")
    assert docstring.meta[0].description == None
    assert docstring.meta[1].args == ("Section 2", "chunk 2")
    assert docstring

# Generated at 2022-06-13 19:37:08.357766
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:37:16.722342
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '/**\n\
                A module level docstring.\n\
                \n\
                Args:\n\
                    arg1: Argument with a type.\n\
                    arg2: A required argument.\n\
                    arg3: Argument with a default value.\n\
                        Default: \'a default value\'\n\
                    arg4: Argument with a default value specified in the docstring.\n\
                        Default: the value of arg4 in the signature.\n\
                Returns:\n\
                    The return type and description.\n\
                Raises:\n\
                    KeyError: Raises an exception.\n\
                """\n'
    parsed_docstring = GoogleParser().parse(text)
    assert parsed_docstring.short_description == 'A module level docstring.'
    assert parsed_doc

# Generated at 2022-06-13 19:37:28.908612
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Titles are at column 1
    assert parse("Args:\n"
                 "  test: parameter") == (
        "['Args:\\n  test: parameter'], "
        "[], [], OrderedDict(), None, None, False, False, None)")

    # Titles are at column 2
    assert parse(" Args:\n"
                 "  test: parameter") == (
        "['Args:\\n  test: parameter'], "
        "[], [], OrderedDict(), None, None, False, False, None)")

    # Titles are at column 1, colon is optional
    assert parse("Args\n"
                 "  test: parameter") == (
        "['Args\\n  test: parameter'], "
        "[], [], OrderedDict(), None, None, False, False, None)")



# Generated at 2022-06-13 19:37:35.361573
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Method parse of class GoogleParser without parameters
    str = inspect.cleandoc("""
        This is a short description.

        This is a long
        description.

        Attributes
        ----------
        attr1 : str
            This is attr1.
        attr2 : int
            This is attr2.

        Examples
        --------
        This is an example.
        """)
    docstring: Docstring = GoogleParser().parse(str)
    assert docstring.short_description == 'This is a short description.'
    assert len(docstring.meta) == 2
    assert docstring.meta[0].description == 'This is attr1.'
    assert docstring.meta[0].arg_name == 'attr1'
    assert docstring.meta[0].type_name == 'str'

# Generated at 2022-06-13 19:37:38.103172
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    parser = GoogleParser()

    text = """
    GoogleParser.parse(text)

    Parse the Google-style docstring into its components.

    Args:
        self (GoogleParser): The object.
        text (str): The text.

    Returns:
        Docstring: parsed docstring
    """

    print(parser.parse(text))


# Generated at 2022-06-13 19:37:48.845847
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = '''
    Parse docstring into its components.

    :param text: docstring
    :returns: parsed docstring
    :raises ValueError: when docstring is empty
    '''
    parsed = parse(docstring)
    assert parsed.short_description == 'Parse docstring into its components.'
    assert parsed.long_description == None
    assert parsed.blank_after_long_description == False
    assert parsed.blank_after_short_description == True

    assert parsed.meta[0].description == 'parsed docstring'
    assert parsed.meta[0].args[0] == 'returns'
    assert parsed.meta[0].args[1] == None
    assert parsed.meta[1].description == 'when docstring is empty'

# Generated at 2022-06-13 19:37:59.323873
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    def test_function():
        """
        Test for parse

        :return:
        """
        pass

    expected_output = Docstring(
        short_description="Test for parse",
        long_description=None,
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[DocstringParam(
            args=["param", ":return:"],
            description=None,
            arg_name=":return:",
            type_name=None,
            is_optional=None,
            default=None
        )],
    )

    docstring = parse(inspect.getdoc(test_function))

    assert docstring == expected_output

# Generated at 2022-06-13 19:38:07.092515
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    docstring = """\
    A short description of the module.

    This is a longer description.

    Args:
        arg_one (int): Description of arg_one.
        arg_two (str): Description of arg_two.
        arg_three (bool): Description of arg_three. Defaults to True.\
"""

# Generated at 2022-06-13 19:38:17.581716
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """Parses Google-style docstrings.

    Args:
        text: text of the docstring

    Returns:
        Parsed docstring.
    """

# Generated at 2022-06-13 19:38:24.811239
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # **Replace with your own test**
    #
    # You should test:
    #   (1) Correct output for different inputs
    #   (2) Raising exceptions correctly with different inputs
    #

    # Simple test to check if your code runs without error. Delete this before
    # submitting your assignment.
    txt1 = 'This is a short description.\n    This is a long description.'
    txt2 = 'This is a short description.\n\nThis is a long description.\n'
    txt3 = 'This is a short description.\n\n\nThis is a long description.'
    txt4 = 'This is a short description.\n\n\n\nThis is a long description.\n'
    txt5 = 'This is a short description.\nLong is accurate.'
    txt

# Generated at 2022-06-13 19:38:40.511014
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():

    # Instance of GoogleParser
    p = GoogleParser()

    # Test case: docstring with only a short description and no indent
    expected_output = Docstring(
        short_description='Encrypt a plaintext message with AES, using a secret encryption key.',
        long_description=None,
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[]
    )
    docstring = 'Encrypt a plaintext message with AES, using a secret encryption key.'
    output = p.parse(docstring)
    assert output == expected_output, 'p.parse({}) -> {} != {}'.format(repr(docstring), repr(output), repr(expected_output))

    # Test case: docstring with only a short description and indent

# Generated at 2022-06-13 19:38:55.529481
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = """
    This function adds two numbers.

    :param a: first number
    :param b: second number
    :returns: sum of the two numbers
    """
    parser = GoogleParser()
    res = parser.parse(text)
    assert len(res.meta) == 3
    assert isinstance(res.meta[0], DocstringMeta)
    assert isinstance(res.meta[1], DocstringParam)
    assert isinstance(res.meta[2], DocstringReturns)
    assert res.meta[1].arg_name == "a"
    assert res.meta[1].type_name is None
    assert res.meta[1].is_optional is None
    assert res.meta[1].default is None
    assert res.meta[2].is_generator is False



# Generated at 2022-06-13 19:39:01.963521
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Default test values
    text = "text"
    desc_chunk = "desc_chunk"
    meta_chunk = "meta_chunk"
    long_desc_chunk = "long_desc_chunk"
    short_description = "short_description"
    long_description = "long_description"
    title = "title"
    chunk = "chunk"
    indent_match = "indent_match"
    indent = "indent"
    part = "part"
    args = "args"
    description = "description"
    type_name = "type_name"
    arg_name = "arg_name"
    default = "default"

    # Test case 1
    parser = GoogleParser()
    ret = parser.parse(text)

    # Test case 2
    text = None
    ret

# Generated at 2022-06-13 19:39:05.409021
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    google_parser = GoogleParser()
    doc_string = google_parser.parse("""Returns the total number of receipts.
    :rtype: string
    :returns: the total number of receipts
    """)
    return doc_string


# Generated at 2022-06-13 19:39:13.232543
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = '''
    Convert the specified data into an ONNX model.

    :param symbol: The input symbol.
    :param params: A dictionary of name to `NDArray`.
    :param inputs: A list of input variable names (strings).
    :param outputs: A list of output variable names (strings).

    :returns: The ONNX model as a string.
    '''
    parser = GoogleParser()
    output = parser.parse(text)
    print('short_description: {}'.format(output.short_description))
    print('long_description: {}'.format(output.long_description))
    print('blank_after_short_description: {}'.format(output.blank_after_short_description))
    print('blank_after_long_description: {}'.format(output.blank_after_long_description))
   

# Generated at 2022-06-13 19:39:22.371779
# Unit test for method parse of class GoogleParser

# Generated at 2022-06-13 19:39:31.309091
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Release under CC0 1.0 Universal (Public Domain)
    """test_GoogleParser_parse
    Tests GoogleParser.parse() method.
    """
    docstring = r"""
        A very short description.

        A longer description.

        Args:
            arg1 (int): The first argument that can be documented.
            arg2 (str): The second argument that can be documented.

        Returns:
            str: The return value.

        Raises:
            TypeError: if arguments are not of the correct type.
            ValueError: if arguments are out of bounds.

        Example:
            Examples:

                import google_parser

                google_parser.parse("<docstring>")
    """
    parser = GoogleParser()

    parsed = parser.parse(docstring)
    assert parsed is not None
    # Build reference
    ref_doc

# Generated at 2022-06-13 19:39:36.578543
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse('') == Docstring()
    assert GoogleParser().parse('\n') == Docstring()
    assert GoogleParser().parse(' ') == Docstring()
    assert GoogleParser().parse('\n ') == Docstring()
    assert GoogleParser().parse('\n Args:\n') == Docstring()
    assert GoogleParser().parse('\n Args: a\n') == Docstring()

    ret = Docstring()
    ret.short_description = ''
    ret.long_description = ''
    assert GoogleParser().parse('\n a') == ret
    assert GoogleParser().parse('\n a\n') == ret
    assert GoogleParser().parse('\n a\n\n') == ret

    ret = Docstring()
    ret.short_description = 'a'
    ret.blank_after_short_

# Generated at 2022-06-13 19:39:43.445798
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    doc_string = """
    Parse the docstring.

    Blah blah blah.

    Args:
        arg1 (str): The first argument.
        arg2 (int): The second argument.

    Returns:
        bool: The return value. True for success, False otherwise.

    Raises:
        AttributeError: The ``Blah`` attribute.
        ValueError: If `blah` is not specified.
    """
    ret = parse(doc_string)
    print(ret)


if __name__ == "__main__":
    test_GoogleParser_parse()

# Generated at 2022-06-13 19:39:49.804231
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text1 = '''Test Function Docstring

Args:
    param1(str): The first parameter.
    param2 (:obj:`int`, optional): The second parameter. Defaults to 2.
    param3(:obj:`list` of :obj:`str`): The third parameter.

'''
    g = GoogleParser()
    result1 = g.parse(text1)
    assert result1.short_description == "Test Function Docstring"
    assert result1.long_description == None
    assert result1.blank_after_short_description == True
    assert result1.blank_after_long_description == True
    assert len(result1.meta) == 3
    assert result1.meta[0].keyword == "param"

# Generated at 2022-06-13 19:40:02.637672
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    #Test docstring is not empty
    assert GoogleParser().parse("I am a docstring")
    #Test the short description is the line before the first title
    assert GoogleParser().parse("I am the first line\nArguments: I am the second\nreturns: i am the third").short_description == "I am the first line"

    #Test the long description is all the lines between the first title and the second
    assert (
        GoogleParser().parse(
            "\nI am the first line \nArguments: I am the second\nI am the thrid line\nreturns: i am the fourth"
        )
        .long_description
        == "I am the thrid line"
    )

    #Test the long description includes all the lines between the first title and the second

# Generated at 2022-06-13 19:40:08.291402
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    text = 'CLI to run command on remote host.'
    assert (GoogleParser().parse(text))

    text = """CLI to run command on remote host.

    This is a wrapper to the runremote command.

    You can run with the following command:

        runremote -s "string to match" command arg1 arg2

    Arguments:
        s (str):   String to match and run the command against
        command (str): Command to run
    """
    doc = GoogleParser().parse(text)
    assert doc


# Generated at 2022-06-13 19:40:17.361971
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # test empty
    assert GoogleParser().parse("") == Docstring()

    # test simple
    assert GoogleParser().parse("Hello World") == Docstring(
        short_description="Hello World",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )
    # test simple
    assert GoogleParser().parse("Hello World\n") == Docstring(
        short_description="Hello World",
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )

    # test simple two lines

# Generated at 2022-06-13 19:40:26.895890
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    assert GoogleParser().parse("""
    Return a property attribute for new-style classes (classes that derive from
    `object`).
    """) == Docstring(
        short_description="Return a property attribute for new-style classes (classes that derive from `object`).",
        long_description=None,
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[],
    )

# Generated at 2022-06-13 19:40:37.567419
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    from .common import TestData
    from .common import TestParams
    all_test_data, test_params = TestData.get_all_test_data_and_params()
    for module, test_datas in all_test_data.items():
        if test_params["all_modules"] or module in test_params["modules"]:
            print("\n\nModule", module)
            for test_data in test_datas:
                print("\n\nTest Data", test_data)
                docstring_str = test_data.docstring
                if docstring_str is not None:
                    print("\n", docstring_str)
                    ret_Docstring = GoogleParser().parse(docstring_str)

# Generated at 2022-06-13 19:40:47.747797
# Unit test for method parse of class GoogleParser
def test_GoogleParser_parse():
    # Test different combinations of input parameters
    googleParser = GoogleParser()
    docstring = googleParser.parse("")

    assert docstring.short_description==None, "Wrong short description"
    assert docstring.long_description==None, "Wrong long description"
    assert len(docstring.meta)==0, "Wrong meta data"

    docstring = googleParser.parse("   A short description.\n \n\tA long description. \n")
    assert docstring.short_description=="A short description.", "Wrong short description"
    assert docstring.long_description=="A long description.", "Wrong long description"
    assert docstring.blank_after_short_description==True, "Wrong blank after short description"