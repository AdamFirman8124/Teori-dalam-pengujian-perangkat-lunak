

# Generated at 2022-06-13 19:41:52.499558
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    p = NumpydocParser()
    assert p.parse("") == Docstring()
    assert p.parse("test") == Docstring(short_description='test')
    assert p.parse("test\n\ntest2") == Docstring(
        short_description='test', long_description='test2'
    )
    assert p.parse("test\n  test2") == Docstring(
        short_description='test', long_description='test2', blank_after_short_description=False
    )
    assert p.parse("test\n  test2\n  test3") == Docstring(
        short_description='test', long_description='test2\n\ntest3', blank_after_short_description=False, blank_after_long_description=False
    )

# Generated at 2022-06-13 19:41:58.907603
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    s = DeprecationSection("deprecation","")
    result = s.parse("")
    assert next(result) == DocstringDeprecated([""], "None", "None")
    result = s.parse("\n")
    assert next(result) == DocstringDeprecated([""], None, None)
    result = s.parse("0.3.4\ntest1234")
    assert next(result) == DocstringDeprecated([""], "test1234", "0.3.4")

# Generated at 2022-06-13 19:42:04.155395
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print('----- test_parse start -----')
    parser = NumpydocParser()

# Generated at 2022-06-13 19:42:07.634140
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print("test_NumpydocParser_parse")
    parser = NumpydocParser()
    func = inspect.currentframe().f_code
    docstring = parser.parse(inspect.getdoc(func))
    print(docstring.long_description)



# Generated at 2022-06-13 19:42:11.842024
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert parse("Example:\n  This is simple valid docstring.") is not None
    assert parse("") is not None
    assert parse(None) is not None

test_NumpydocParser_parse()


# Generated at 2022-06-13 19:42:20.267259
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    import textwrap
    txt = textwrap.dedent("""\
        .. deprecated:: 1.1.1
            Text here
    """)

    # assert that parse returns a list with one DocStringDeprecated object
    assert next(DeprecationSection("deprecated", "deprecation").parse(txt)) == DocstringDeprecated(args=['deprecation'], description='Text here', version='1.1.1')


# Generated at 2022-06-13 19:42:28.344195
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = '''
    Short description

    Long description

    Parameters
    ----------
    first : str
        The first parameter.
    second : int, optional
        The second one.

    Returns
    -------
    None
    '''

# Generated at 2022-06-13 19:42:34.708735
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    from .docstring import DocstringDeprecated
    d = DeprecationSection('deprecated', 'deprecation')
    result = d.parse(
'''
0.1.1
    Use :func:`~collections.deque.rotate` instead.
'''
    )
    assert list(result) == [DocstringDeprecated(args=['deprecation'],
                                                description='Use :func:`~collections.deque.rotate` instead.',
                                                version='0.1.1')]


# Generated at 2022-06-13 19:42:44.339698
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = '''First line of the summary.
    Second line of the summary.

    The rest of the docstring.
    '''

    parsed = parser.parse(text)
    assert parsed.short_description == 'First line of the summary.'
    assert parsed.long_description == 'Second line of the summary.\n\nThe rest of the docstring.'
    assert not parsed.blank_after_short_description
    assert not parsed.blank_after_long_description
    assert len(parsed.meta) == 0

    text = '''First line of the summary.
    Second line of the summary.

    The rest of the docstring.
    More docstring.
    '''

    parsed = parser.parse(text)
    assert parsed.short_description == 'First line of the summary.'

# Generated at 2022-06-13 19:42:51.337430
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # initialization of the parser
    ndparse = NumpydocParser()
    # create test docstring

# Generated at 2022-06-13 19:43:25.844798
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_str = '''
    This is a short description.
        
    This is a longer description
    that gets split over multiple
    lines.
    
    Parameters
    ----------
    arg_name
        arg_description
    arg_2 : type, optional
        descriptions can also span...
        ... multiple lines
    
    Attributes
    ----------
    attr_name : type
        attr_description
    
    Raises
    ------
    ValueError
        A description of what might raise ValueError
    '''
    result = NumpydocParser().parse(test_str)
    
    assert result.short_description == 'This is a short description.'
    assert result.long_description == 'This is a longer description that gets split over multiple lines.'
    assert result.blank_after_short_description == True
    assert result

# Generated at 2022-06-13 19:43:39.780095
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    out = NumpydocParser().parse(test_docstring)
    assert out.short_description == "A fibonacci generator"
    assert out.long_description == (
        "This is a generator that produces numbers in the fibonacci "
        "sequence.\n\nThe fibonacci sequence is a sequence of numbers "
        "where the next number in the sequence is the sum of the previous "
        "two numbers in the sequence.\nThe sequence looks like this: "
        "1, 1, 2, 3, 5, 8, 13, ..."
    )
    assert out.blank_after_short_description
    assert out.blank_after_long_description
    assert len(out.meta) == 3
    assert isinstance(out.meta[0], DocstringParam)

# Generated at 2022-06-13 19:43:47.129207
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc_string = "DocString example. Another line of Doc String\n\n" \
                 "The docstring may have a long description which is " \
                 "really long.\n\n" \
                 "Parameters:\n-----------\n" \
                 "param1 : type\n    param1 description\n\n" \
                 "param2 : type\n    param2 description\n\n"\
                 "Returns:\n----------\n" \
                 "return_name : type\n    A description of this returned value\n\n" \
                 "another_type\n    Return names are optional, types are required\n\n"

    parsed_doc_string = NumpydocParser().parse(doc_string)
    assert parsed_doc_string.short_description == 'DocString example. Another line of Doc String'
   

# Generated at 2022-06-13 19:43:57.769327
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert NumpydocParser().parse('') == Docstring()
    assert NumpydocParser().parse('\n\n') == Docstring(
        short_description='',
        long_description='',
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[]
    )
    assert NumpydocParser().parse('\n\n\n') == Docstring(
        short_description='',
        long_description='',
        blank_after_short_description=True,
        blank_after_long_description=True,
        meta=[]
    )

# Generated at 2022-06-13 19:44:07.967302
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    # test parse method of class NumpydocParser
    # test with docstring that contain only short description
    text = """This function computes the XOR of two booleans."""
    d = parser.parse(text)
    assert d.short_description == "This function computes the XOR of two booleans."
    assert d.long_description == None
    assert d.blank_after_short_description == False
    assert d.blank_after_long_description == False
    assert d.meta == []

    # test with docstring that have short description only
    text = """This function computes the XOR of two booleans.
    
    """
    d = parser.parse(text)

# Generated at 2022-06-13 19:44:15.653633
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """A one-line summary that does not use variable names or the
    function name.

    Several sentences providing an extended description. Refer to
    variables using back-ticks, e.g. `var`.

    Parameters
    ----------
    arg1 : int
        Description of `arg1`
    arg2 : str
        Description of `arg2`
    arg3 : :obj:`list` of :obj:`str`
        Description of `arg3`

    Returns
    -------
    int
        Description of return value
    """
    docstring = NumpydocParser().parse(text)
    
    assert docstring.short_description == "A one-line summary that does not use variable names or the\n    function name."
    assert docstring.blank_after_short_description == False
    assert docstring.long_description

# Generated at 2022-06-13 19:44:25.390913
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    test.

    Parameters
    ----------
    string:
        String to parse
    arg: arg
        some arg

    Raises
    ------
    ValueError

    Returns
    -------
    int
    """

    docstring = NumpydocParser().parse(text)

    assert len(docstring.meta) == 3
    assert docstring.meta[0].type == 'param'
    assert docstring.meta[1].type == 'raises'
    assert docstring.meta[2].type == 'returns'


# Generated at 2022-06-13 19:44:34.865743
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc = """
    A function that does something.
        Parameters
            :x: The first parameter
            :y: The second parameter
        Returns
            This is something the function returns
            :return: int
            :rtype: int
    """
    assert (
        parse(doc).short_description
        == "A function that does something."
    )
    assert parse(doc).long_description == """Parameters
            :x: The first parameter
            :y: The second parameter
        Returns
            This is something the function returns
            :return: int
            :rtype: int"""
    assert parse(doc).meta[0].args == ["param", "x"]
    assert parse(doc).meta[0].description == "The first parameter"
    assert parse(doc).meta[1].args == ["param", "y"]

# Generated at 2022-06-13 19:44:45.231104
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Create instance
    n = NumpydocParser()

    # Setup
    long_test = """
        Test long description
        """

    description_test = """
        Test description
        """

    short_description_test = """
        Test short description
        """


# Generated at 2022-06-13 19:44:49.954300
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .common import DocstringMeta, DocstringParam, DocstringRaises, DocstringReturns, DocstringDeprecated
    parser = NumpydocParser()


# Generated at 2022-06-13 19:45:01.534147
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

# Generated at 2022-06-13 19:45:17.117023
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    header = "Hello world"
    paragraph = "This is a paragraph."
    section_title = "Parameters"
    arg_name = "arg_name"
    arg_type = "type"
    arg_desc = "arg description"

    ret = NumpydocParser().parse(
        f"{header}\n{paragraph}\n{section_title}\n{arg_name}: {arg_type}\n"
        + f"    {arg_desc}\n\n"
    )
    assert ret.short_description == header
    assert ret.blank_after_short_description == False
    assert ret.long_description == paragraph
    assert ret.blank_after_long_description == True
    assert len(ret.meta) == 4
    assert ret.meta[0].description == arg_name
    assert ret.meta[1].description

# Generated at 2022-06-13 19:45:23.589116
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    func_description = '''
    .. this is a title
    this is a description
    which is on a second line.
    '''
    assert NumpydocParser().parse(func_description).long_description == "this is a description\n    which is on a second line."
    assert NumpydocParser().parse(func_description).short_description == ".. this is a title"

if __name__ == "__main__":
    test_NumpydocParser_parse()

# Generated at 2022-06-13 19:45:32.468327
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:45:43.386117
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstringSections = [
        Section('Parameters', 'param'),
        ReturnsSection('Returns', 'returns'),
        YieldsSection('Yields', 'yields'),
        RaisesSection('Raises', 'raises')
    ]
    numpydocParser = NumpydocParser(docstringSections)

    # Test that short description, long description and blank lines are parsed correctly
    assert (numpydocParser.parse('')).short_description == None
    assert (numpydocParser.parse('')).long_description == None
    assert (numpydocParser.parse('')).blank_after_short_description == False
    assert (numpydocParser.parse('')).blank_after_long_description == False

    assert (numpydocParser.parse('short_description')).short_

# Generated at 2022-06-13 19:45:52.180179
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    section1 = Section(title="Parameters", key="param")
    section2 = ParamSection("Params", "param")
    section3 = RaisesSection("Raises", "raises")
    section4 = Section("Example", "examples")
    section5 = Section("Note", "notes")
    section6 = Section("Warning", "warnings")
    section7 = ReturnsSection("Returns", "returns")
    section8 = YieldsSection("Yields", "yields")
    section9 = Section("See Also", "see_also")
    section10 = Section("Related", "see_also")
    section11 = DeprecationSection("deprecated", "deprecation")

# Generated at 2022-06-13 19:46:03.700963
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Unit test for NumpydocParser.parse."""
    class TestClass:
        def test_func(self, i: int = 0, j: int = 1) -> str:
            """Do something.

            Parameters
            ----------
            i : int, optional
                This is `i`.

            j : int, optional
                This is `j`.

            Returns
            -------
            str
                Return something.

            Note
            ----
            This is a note.
            """
            return ""

    doc = inspect.getdoc(TestClass.test_func)

    assert parse(doc).short_description == "Do something."

# Generated at 2022-06-13 19:46:14.640404
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """summary line

    Extended description

    Parameters
    ----------
    arg1 : int
        Description of `arg1`
    arg2 : str, optional
        Description of `arg2` (the default is '2').
    arg3 : str, optional, defaults to '3'
        Description of `arg3` (the default is '3').
    arg4, optional, defaults to 4
        Description of `arg4` (the default is 4).
    arg5 : int, optional (default: 5)
        Description of `arg` (the default is 5).

    Returns
    -------
    int
        Description of return value.
    """
    ds = parse(text)
    assert ds.short_description == "summary line"
    assert ds.long_description == (
        "Extended description"
    )

# Generated at 2022-06-13 19:46:27.328740
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:46:37.707493
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Does a simple test of the parse method of the NumpydocParser class
    # If a section with a key 'short_description' is not in sections
    # the parse method returns a Docstring object with a None value for
    # short_description
    # If a section with a key 'short_description' is in sections
    # the parse method returns a Docstring object with the value of the
    # short_description stored in the first line of the string stored in
    # the parameter text
    text = '''First line of docstring
Second line of docstring'''
    parser = NumpydocParser()
    sections_dict = parser.sections
    sections_dict_key_list = list(sections_dict.keys())
    short_description_section_key = 'short_description'

# Generated at 2022-06-13 19:46:52.107901
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    actual_output = NumpydocParser().parse(
        """
method

    This method is used to test NumpydocParser.parse().
    It only has 1 parameter.

Parameters
----------
x
    An integer.
"""
    )
    expected_output = Docstring(
        short_description="method",
        blank_after_short_description=True,
        blank_after_long_description=False,
        long_description="This method is used to test NumpydocParser.parse(). It only has 1 parameter.",
        meta=[
            DocstringMeta(args=["param"], description="An integer."),
        ],
    )
    assert actual_output == expected_output


# Generated at 2022-06-13 19:47:01.614252
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Parse the numpy-style docstring into its components.

    :returns: parsed docstring

    Parameters
    ----------
    text : str
        input text

    Returns
    -------
    Docstring
        parsed docstring

    Raises
    ------
    KeyError
        if the parsing fails

    Other Parameters
    ----------------
    whatever : int
        whatever you want
    """
    docstring = NumpydocParser().parse(text)

    # expected values for the docstring
    docstring_short_description = "Parse the numpy-style docstring into its components."

# Generated at 2022-06-13 19:47:13.623863
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = '''
        The sky is blue.

        :param int sky: the sky
        :returns: the sky
        :rtype: int
    '''

    parsed = NumpydocParser().parse(docstring)
    assert parsed.short_description == "The sky is blue."
    assert parsed.blank_after_short_description == False
    assert parsed.blank_after_long_description == False
    assert parsed.long_description == None
    assert parsed.meta[0].args == ["param","sky"]
    assert parsed.meta[0].arg_name == "sky"
    assert parsed.meta[0].type_name == "int"
    assert parsed.meta[0].is_optional == False
    assert parsed.meta[0].default == None



# Generated at 2022-06-13 19:47:16.525867
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = "docstring...\n\n    Something\n    More\n\n    """
    text += "Returns\n------\n    object\n    """
    NumpydocParser().parse(text)

# Generated at 2022-06-13 19:47:26.380594
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:47:35.199498
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """Module level docstring

    Parameters
    ----------
    param1 : str
        Description of param1
    param2 : int (optional)
        Description of param2
    param3 : :class:`ClassName`
        Description of param3

    Returns
    -------
    str
        Description of return

    See Also
    --------
    :class:`ClassName`
        Class reference
    """

    ndp = NumpydocParser()
    docstring = ndp.parse(text)
    assert docstring.short_description == 'Module level docstring'

# Generated at 2022-06-13 19:47:46.872138
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    '''
    numpy style docstring parsing.

    check the docstring parsing,
    return_name is None
    '''
    example = """
    The docstring of this function.

    Parameters
    ----------
    arg1 : int
        The first argument.
    arg2 : str, optional
        The second argument.
    arg3 : dict, keyword only
        The third argument.

    Returns
    -------
    sum : str
        The return value.

    Other Parameters
    ----------------
    kwarg1 : float
        Another keyword argument.

    """
    res=parse(example)
    print(res)

    assert res.short_description=='The docstring of this function.'
    assert res.long_description=='The first argument.\nThe second argument.\nThe third argument.'

# Generated at 2022-06-13 19:47:52.451125
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Unit test for method parse of class NumpydocParser."""
    print('Testing NumpydocParser.parse')

    try:
        import doctest
        doctest.testmod()
    except ImportError:
        import sys
        import traceback
        traceback.print_exc(file=sys.stdout)

# Generated at 2022-06-13 19:48:00.944694
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = inspect.cleandoc("""Some function that does something.
    Parameters
    ----------
    some_arg : type
        this is a description
    arg_2 : type, optional
        this arg has a default
        default value: 3
    arg_3 : type
        this arg has no default
    Notes
    -----
    For more information see the :ref:`some section <sec:some_section>` in the
    project documentation.
    Example
    -------
    some code example
    """
                                )
    expected = Docstring()
    expected.short_description = "Some function that does something."
    expected.long_description = "For more information see the :ref:`some section <sec:some_section>` in the project documentation.\nExample\n-------\nsome code example"
    expected.blank_after

# Generated at 2022-06-13 19:48:13.196657
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydoc_parser = NumpydocParser()
    assert numpydoc_parser.parse("testing\n") == Docstring(short_description='testing')
    assert numpydoc_parser.parse("testing\n\n") == Docstring(short_description='testing')
    assert numpydoc_parser.parse("testing\n\nlong description\n") == Docstring(short_description='testing', blank_after_short_description=True, blank_after_long_description=False, long_description='long description')
    assert numpydoc_parser.parse("testing\n\nlong description\n\n") == Docstring(short_description='testing', blank_after_short_description=True, blank_after_long_description=True, long_description='long description')

# Generated at 2022-06-13 19:48:20.963958
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydoc_parser = NumpydocParser()
    src_code = """
    """
    docstring = numpydoc_parser.parse(src_code)
    print(docstring)


# Generated at 2022-06-13 19:48:26.344548
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring_text = """\
    Test function.

    Parameters
    ----------
    arg1 : str
        Describe arg1.
    arg2 : str, optional
        Describe arg2. Default is 'default'.

    Returns
    -------
    ret : str
        Describe ret.

    Raises
    ------
    ValueError
        Explain when a ValueError is raised.
    TypeError
        Explain when a TypeError is raised.

    Warns
    -----
    RuntimeWarning
        Explain when a RuntimeWarning is issued.

    References
    ----------
    [4] `Numpy Documentation (numpy.org/doc)
        <https://numpy.org/doc>`_
    """

    res = NumpydocParser().parse(docstring_text)
    assert len(res.meta) == 7
    assert res

# Generated at 2022-06-13 19:48:37.509893
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_input1 = """
    A Functions with paramaterized values
    Parameters
    ----------
    data : countable, iterable
        The data to be tested.

    value : numeric
        The value of interest (default is 0)

    Returns
    -------
    int
        Number of occurrences of value in data.

    Notes
    -----
    The value parameter is positional only for version 0.16.0 and later.

    Examples
    --------
    Count the number of zeros in a list:

    >>> count([0, 1, 0, 2, 0])
    3

    Count the number of sixes in a tuple:

    >>> count((1, 2, 3, 6, 6, 6, 6, 7, 8, 6), 6)
    4

    """
    output = NumpydocParser().parse(test_input1)
   

# Generated at 2022-06-13 19:48:47.227725
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:48:58.208089
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
    Given a string and a string dictionary, this function
    replaces all occurrences of strings in the dictionary
    with the given replacement string.

    Parameters
    ----------
    str : string to be processed
    dic : replacement dictionary

    Returns
    -------
    str_rep : string with replacements processed
    '''
    parser = NumpydocParser()
    result = parser.parse(text)

    assert result.short_description == 'Given a string and a string dictionary, this function'
    assert result.blank_after_short_description == True
    assert result.blank_after_long_description == True
    assert result.long_description == 'replaces all occurrences of strings in the dictionary with the given replacement string.'
    assert len(result.meta) == 2
    assert result.meta[0].args == ['param', 'str']

# Generated at 2022-06-13 19:49:08.087032
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = '''Short description.

    And the rest.

    Parameters
    ----------
    param
        Param description.
    param2 : type, optional
        Param description.

    Raises
    ------
    ValueError
        Description of what might raise ValueError

    Other Parameters
    ----------------
    other_param
        Description of other param.

    Returns
    -------
    str
        Description of return value.
    int
        A second return value.

    Yields
    ------
    str
        Description of yielded value.
    int
        A second yielded value.

    Examples
    --------
    >>> print('hello')
    hello
    >>> 1 + 1
    2

    Warnings
    --------
    This is a warning.

    Notes
    -----
    Some notes.
    '''
    parser = NumpydocParser

# Generated at 2022-06-13 19:49:19.395288
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    g = NumpydocParser.parse(docstring_test_1)
    h = NumpydocParser.parse(docstring_test_2)
    i = NumpydocParser.parse(docstring_test_3)
    j = NumpydocParser.parse(docstring_test_4)
    k = NumpydocParser.parse(docstring_test_5)
    l = NumpydocParser.parse(docstring_test_6)
    m = NumpydocParser.parse(docstring_test_7)
    n = NumpydocParser.parse(docstring_test_8)
    o = NumpydocParser.parse(docstring_test_9)
    p = NumpydocParser.parse(docstring_test_10)

# Generated at 2022-06-13 19:49:29.499569
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # TODO
    # text = """
    #     This is a short description
    #     This is a long description
    #
    #     Parameters
    #     ----------
    #     arg_1 : arg_1_type
    #         a description
    #     arg2 : arg2_type
    #         another description
    #
    #
    #     Returns
    #     -------
    #     return_1 : return_1_type
    #         a description
    #     returns_2 : returns_2_type
    #         another description
    # """
    # print(NumpydocParser().parse(text))

    pass

if __name__ == "__main__":
    test_NumpydocParser_parse()

# Generated at 2022-06-13 19:49:39.692292
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from . import render
    from . import parse
    from . import items
    from . import common
    from . import render

    nps = NumpydocParser()
    docstring = nps.parse("""
    .. deprecated:: 1.0
        some text
    """)
    assert docstring.short_description == None
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False
    assert docstring.meta[0].key == 'deprecation'
    assert docstring.meta[0].description == 'some text'
    assert docstring.meta[0].args[1] == 1.0

# Generated at 2022-06-13 19:49:46.577584
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    actual = NumpydocParser().parse('Input:               An open file or file-like object.')
    # print(actual.meta)
    print(actual.meta[0].description)
    print(actual.meta[0].arg_name)

if __name__ == '__main__':
    test_NumpydocParser_parse()

# Generated at 2022-06-13 19:49:56.586669
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    section = DeprecationSection("deprecated", "deprecation")
    text = inspect.cleandoc('''Deprecated since version 5.0
    This is an example of deprecated code.''')
    result = [x.description for x in section.parse(text)]
    expected_result = ['This is an example of deprecated code.']
    assert result == expected_result



# Generated at 2022-06-13 19:50:01.305847
# Unit test for constructor of class ParamSection
def test_ParamSection():
    test_data = "param_name : int\n    param_description"
    section = ParamSection("section_name","param")
    assert str(section.parse(test_data)) == "['section_name', 'param_name', 'param_description', None, 'param_name', 'int', False] "

# Generated at 2022-06-13 19:50:08.667066
# Unit test for constructor of class ReturnsSection
def test_ReturnsSection():
    a = ReturnsSection("Returns", "returns")
    assert a.title == 'Returns'
    assert a.key == 'returns'
    assert a.is_generator == False
    b = ReturnsSection("Yields", "yields")
    assert b.is_generator == True
    assert b.title == 'Yields'
    assert b.key == 'yields'
    c = ReturnsSection("Warns", "warns")
    assert c.is_generator == False
    assert c.title == 'Warns'
    assert c.key == 'warns'


# Generated at 2022-06-13 19:50:15.445752
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = "short description\n\nlong description\n\nParameters\n----------\nparam1\n\ndescription of param1\n\nx\n\ndescription of x\n\nExamples\n--------\nexample text\n\n"
    ds = NumpydocParser().parse(text)
    assert ds.short_description == "short description"
    assert ds.long_description == "long description"
    assert ds.blank_after_short_description
    assert ds.blank_after_long_description
    assert len(ds.meta) == 2
    assert ds.meta[0].args[-1] == 'param1'
    assert ds.meta[0].description == 'description of param1'
    assert ds.meta[1].description == 'example text'

# Generated at 2022-06-13 19:50:27.890934
# Unit test for method add_section of class NumpydocParser
def test_NumpydocParser_add_section():
    parser = NumpydocParser()

    # add_section() has a section argument, add a section argument
    custom_section = Section('Arguments', 'args')
    parser.add_section(custom_section)
    assert 'Args' in parser.sections

    # add_section() has a section argument, change a section argument
    custom_section2 = Section('Arguments', 'args2')
    parser.add_section(custom_section2)
    assert 'args2' in parser.sections    
    
    # add_section() has a section argument, change a section argument
    custom_section2 = Section('arguments2', 'args2')
    parser.add_section(custom_section2)
    assert 'args2' not in parser.sections    
    assert 'arguments2' in parser.sections

# Generated at 2022-06-13 19:50:29.871865
# Unit test for constructor of class _SphinxSection
def test__SphinxSection():
    assert _SphinxSection("deprecated", "deprecation").title_pattern == r"^\.\.\s*(deprecated)\s*::"

# Generated at 2022-06-13 19:50:30.960720
# Unit test for constructor of class NumpydocParser
def test_NumpydocParser():
    parser = NumpydocParser()


# Generated at 2022-06-13 19:50:33.600539
# Unit test for constructor of class ReturnsSection
def test_ReturnsSection():
    r_section = ReturnsSection("ReturnsSection", "constructed_returns_section")

    if r_section.title is not "ReturnsSection":
        raise AssertionError("incorrect title")

# Generated at 2022-06-13 19:50:41.243754
# Unit test for constructor of class Section
def test_Section():
    # create a new section, with title="Parameters" and key="param"
    test_section1 = Section("Parameters", "param")
    # check if test_section1 has the attributes "title" and "key"
    # and if the value of title is "Parameters" and the value of key is "param"
    assert test_section1.title == "Parameters"
    assert test_section1.key == "param"


# Generated at 2022-06-13 19:50:52.250790
# Unit test for method parse of class _KVSection

# Generated at 2022-06-13 19:51:03.423400
# Unit test for constructor of class ReturnsSection
def test_ReturnsSection():
    test_ReturnsSection = ReturnsSection("Returns", "returns")
    test_ReturnsSection.is_generator
    test_ReturnsSection.key
    test_ReturnsSection.title
    test_ReturnsSection.title_pattern
    test_ReturnsSection._parse_item("a", "b")


# Generated at 2022-06-13 19:51:05.381217
# Unit test for constructor of class Section
def test_Section():
    sec = Section("Title","key")
    assert sec


# Generated at 2022-06-13 19:51:15.083784
# Unit test for function parse
def test_parse():
    docstring = """Get rid of the Docstring for now by wrapping it in a function.
                   Simple function
                   Parameters
                   ----------
                   x: int
                       the first number
                   y: int
                       the second number
                   Returns
                   -------
                   int
                       the sum of x and y
                   """
    test_parse_result = parse(docstring)

# Generated at 2022-06-13 19:51:30.413932
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """\
        Short description.

        Long description.

        Parameters
        ----------
        arg_name
            arg_description
        arg_2 : type, optional
            descriptions can also span...
            ... multiple lines

        Returns
        -------
        return_name : type
            A description of this returned value
        another_type
            Return names are optional, types are required

        Warns
        -----
        Warnings
            can occur

        Raises
        ------
        ValueError
            A description of what might raise ValueError

        Other Parameters
        ----------------
        other_attr : other_type
            Other long description.\
        """
    result = NumpydocParser().parse(text)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."