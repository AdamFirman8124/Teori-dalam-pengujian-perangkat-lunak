

# Generated at 2022-06-13 19:41:40.318009
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doctext = '''
    Function to do something initially

    Parameters
    ----------
    var1 : int
        square of this number

    var2 : str
        string data

    Attribute
    ---------
    attr1 : int
        square of this number

    attr2 : str
        string data

    Returns
    -------
    var1 : int
        square of this number

    var2 : str
        string data

    Warnings
    --------
    This is a warning

    Warns
    -----
    This is another warning

    Raises
    ------
    ValueError
        if something is wrong

    Example
    -------
    >>> a = 1
    >>> b = 2

    '''
    res = NumpydocParser()
    doctext = inspect.cleandoc(doctext)

# Generated at 2022-06-13 19:41:45.454668
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Unit test for method parse of class NumpydocParser"""
    text = """
        Define the parameters that describe the solver and its tolerances.

        Parameters
        ----------
        tol : float
            tolerance to achieve.
        eps : float, optional
            small number to prevent division by zero.
        max_iter : int
            maximum number of iterations of the solver.
        x0 : array
            initial guess.

        Returns
        -------
        x : array
            optimized parameters.
        f : float
            final function value.
    """
    parser = NumpydocParser()
    docstring = parser.parse(text=text)
    print(docstring)
    assert docstring.short_description == "Define the parameters that describe the solver and its tolerances."

# Generated at 2022-06-13 19:41:54.200268
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """ test the unit test of method parse of class NumpydocParser """
    my_instance = pdoc.parse.NumpydocParser(sections=None)

# Generated at 2022-06-13 19:42:04.226923
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import textwrap

    parser = NumpydocParser()

    test_docstring = textwrap.dedent(
        """
        This is a very short description.

        This is a longer description that can span
        multiple lines.

        Parameters
        ----------
        param : str
            Description of param.
        param2 : Optional[int]
            Description of param2.

        Other Parameters
        ----------------
        other_param : float
            Description of other_param.

        Raises
        ------
        ValueError
            Description of when ValueError is raised.

        Returns
        -------
        dict
            Dictionary of the parsed arguments.
        """
    )
    test_result = parser.parse(test_docstring)
    assert test_result.short_description == "This is a very short description."

# Generated at 2022-06-13 19:42:12.454502
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    def do_test(case_name, string, short_description, long_description, blank_after_short_description, blank_after_long_description, meta, docstring=None):
        parser = NumpydocParser()
        docstring = docstring or parser.parse(string)
        assert docstring.short_description == short_description
        assert docstring.long_description == long_description
        assert docstring.blank_after_short_description == blank_after_short_description
        assert docstring.blank_after_long_description == blank_after_long_description
        assert docstring.meta == meta


# Generated at 2022-06-13 19:42:25.510288
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:42:35.125104
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''the numpy-style docstring

    Parameters
    ----------
    text : str
        the numpy-style docstring

    Returns
    -------
    Docstring
        parsed docstring
    '''
    doc = NumpydocParser().parse(text)
    assert doc.short_description == 'the numpy-style docstring'
    assert doc.long_description == None
    assert isinstance(doc.meta, list)
    assert isinstance(doc.meta[0], DocstringParam)
    assert doc.meta[0].arg_name == 'text'
    assert doc.meta[0].type_name == 'str'
    assert doc.meta[0].description == 'the numpy-style docstring'
    assert doc.meta[0].is_optional == False

# Generated at 2022-06-13 19:42:44.825497
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    def method():
        """Test method

        Parameters
        ----------
        param : type
            Description

        Returns
        -------
        value1, value2
            Description

        Raises
        ------
        ValueError
            Description

        See Also
        --------
        foo

        Examples
        --------
        example

        Deprecation warning
        -------------------
        version
            description.
        """

    # Test method parsing
    res = NumpydocParser().parse(inspect.getdoc(method))

# Generated at 2022-06-13 19:42:54.255280
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:43:03.074893
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc_string = '''
    Test method.

    This is test

    Parameters
    ----------
    arg1 : int
        First argument

    arg2 : int, optional
        Second argument

    Raises
    ------
    ValueError
        A description of what might raise ValueError

    '''

# Generated at 2022-06-13 19:43:18.478818
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # If short description is empty, short_description is None, not ''
    docstring = inspect.cleandoc('')\
                + inspect.cleandoc('\n\n')\
                + inspect.cleandoc('Args:')\
                + inspect.cleandoc('    arg_1:')\
                + inspect.cleandoc('        Description of arg_1')\
                + inspect.cleandoc('    arg_2:')\
                + inspect.cleandoc('        Description of arg_2')
    expected_result = Docstring(short_description=None, long_description=None)
    expected_result.meta.append(DocstringParam(args=['param', 'arg_1'],
                                               description='Description of arg_1',
                                               arg_name='arg_1'))

# Generated at 2022-06-13 19:43:29.302177
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    ds1 = """
        Square each element of the input.

        :param x: The array in which to square each element.
        :type x: ndarray

        :returns: The element-wise square of the input.
        :rtype: ndarray

        :raises ValueError: if any value is negative
    """


# Generated at 2022-06-13 19:43:36.780459
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc = """
    Example with only short description

    Example with both short and long description
    """

    assert parse(doc).short_description == doc.split('\n')[1].strip()
    #assert parse(doc).long_description == None
    #assert parse(doc).blank_after_short_description == False
    #assert parse(doc).blank_after_long_description == False
    #assert parse(doc).meta == []



# Generated at 2022-06-13 19:43:45.130833
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    docstring = r"""
        This is short description.

        This is long description.

        Parameters
        ----------
        arg : int
            Parameter description.
        kw1 : int, optional
            Another parameter.
        kw2 : str, optional, default='abc'
            Another parameter.

        Returns
        -------
        List[int]
            Return description
    """

# Generated at 2022-06-13 19:43:50.554860
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    def parse_int(text):
        parser = NumpydocParser()
        docstring = parser.parse(text)
        return docstring.meta.parameters['param'].type_name

    assert parse_int('arg_name\n    arg_description') == 'int'
    assert parse_int('arg_name\n    arg_description\n    Other lines') == 'int'
    assert parse_int('arg_name\n    arg_description\nOther lines') == 'int'
    assert parse_int('arg_name: int\n    arg_description') == 'int'
    assert parse_int('arg_name: \n    arg_description') == 'int'
    assert parse_int('arg_name:\n    arg_description\n    Other lines') == 'int'

# Generated at 2022-06-13 19:43:55.601663
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:03.182170
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    Test for method parse of class NumpydocParser
    """

# Generated at 2022-06-13 19:44:11.794197
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    body = """
    Short desc.

    Long desc.
    Can also be multi-line.

    Parameters
    ----------
    name
        type. Default is value.
        Long description.

    Returns
    -------
    type
        Long description

    Raises
    ------
    ValueError
        Long description.

    Warns
    -----
    UserWarning
        Long description.

    Examples
    --------
    >>> from this import sizzle
    >>> sizzle.foobar(baz=1)
    bla

    See Also
    --------
    other_func, sizzle.foobar

    Warnings
    --------
    Deprecated in version 1.0. Use ``other_func`` instead.

    .. deprecated:: 1.0
        Will be removed in version 1.1. Use ``other_func`` instead.

    """
    parser

# Generated at 2022-06-13 19:44:19.377146
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # test the case that text is empty
    text = ""
    r = NumpydocParser().parse(text)
    assert r.short_description is None
    assert r.blank_after_short_description is False
    assert r.blank_after_long_description is False
    assert r.long_description is None
    assert len(r.meta) == 0

    # test the case that description part and meta part both have content
    text = """Short description.

    Long description.

    Parameters
    ----------
    the_first_param : string
        First parameter
    the_second_param : string
        Second parameter

    Returns
    -------
    string
        The output of the function
    """

    r = NumpydocParser().parse(text)
    assert r.short_description == "Short description."

# Generated at 2022-06-13 19:44:31.323508
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:49.027051
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    ndparser = NumpydocParser([
        Section('ThisIsATest', 'test_section'),
        Section('ThisIsAnotherTest', 'another_test_section')
    ])

    ndparser.sections['ThisIsATest'].parse = lambda x: [DocstringMeta(['test_section'], description='Parse did this')]
    ndparser.sections['ThisIsAnotherTest'].parse = lambda x: [DocstringMeta(['another_test_section'], description='Parse did that')]

    ret = ndparser.parse('This is a test\n-------------\n\nThis is text\n\nThisIsAnotherTest\n--------------\n\nThis is more text')

    assert ret.short_description == 'This is a test'
    assert ret.long_description == 'This is text'
    assert ret

# Generated at 2022-06-13 19:44:56.997763
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    # testing documnet with all of the paragraph (short, long, meta)
    doc = 'short\nlong\n\nParameters\n----------\n\nparam: str\n    param desc'
    expect = Docstring(
        short_description='short',
        long_description='long',
        meta=[
            DocstringMeta(
                [
                    'param'
                ],
                type_name='str',
                description='param desc'
            )
        ]
    )

    assert parser.parse(doc) == expect

    # testing with only meta paragraphs
    doc = 'Parameters\n----------\n\nparam: str\n\n    param desc'

# Generated at 2022-06-13 19:45:03.691084
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This is a short description of the function.

    This is the long description of the function.
    It can span multiple lines.

    Parameters
    ----------
    arg1 : int
        First arg.

    arg2 : str
        Second arg.

    Returns
    -------
    int or None
        This is the return description.
    """

    docstring = parse(text)
    long_description = next((
        item for item in docstring.meta
        if isinstance(item, DocstringMeta)
        and item.args == ["long_description"]
    ), None)
    assert long_description is not None
    assert long_description.description is not None
    assert long_description.description.startswith("This is the long")
    assert long_description.description.endswith("lines.")

    assert docstring

# Generated at 2022-06-13 19:45:07.200470
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
        Parameters
        ----------
        hello: int
            A number that says hello
        """

    ret = NumpydocParser().parse(text)


# Generated at 2022-06-13 19:45:16.512611
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    npd = NumpydocParser()
    ds = npd.parse("""
    Short description

    Long description.

    Also long.

    Parameters
    ----------
    arg_name : arg_type, optional
        arg description. Default is ``5``.

    Returns
    -------
    return_name : return_type
        return description
    """)
    assert ds.short_description == "Short description"
    assert ds.long_description == "Long description.\n\nAlso long."
    assert len(ds.meta) == 2
    assert ds.meta[0].args[0] == "param"
    assert ds.meta[0].args[1] == "arg_name"
    assert "arg_type" in ds.meta[0].arg_name

# Generated at 2022-06-13 19:45:27.028361
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    Unit test for NumpydocParser.parse
    """
    text = inspect.cleandoc("""
        Split array into chunks of the same format.

        Parameters
        ----------
        n : int
            Number of splits in each axis.

        Raises
        ------
        ValueError
            If n is not a sequence of ints.
    """)
    ds = NumpydocParser().parse(text)
    assert len(ds.short_description) > 0
    assert len(ds.long_description) > 0
    assert ds.blank_after_short_description == True
    assert ds.blank_after_long_description == False
    assert len(ds.meta) == 2

# Generated at 2022-06-13 19:45:28.774717
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import doctest
    doctest.testfile("section_parser.txt", optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-13 19:45:35.832543
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:45:45.271032
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:45:53.120551
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_impl = getattr(NumpydocParser(), 'parse')
    text = '''
        Calculates the (unnormalized) log of the softmax over the last dimension
        of the input array.

        :param input: input array
        :type input: numpy.ndarray, required
        :param axis: axis to compute over
        :type axis: int
        :param keepdims: whether to keep dimension or not
        :type keepdims: bool
        :return: (unnormalized) log of the softmax over the last dimension
        :rtype: numpy.ndarray
    '''
    result = test_impl(text)
    assert result.short_description == 'Calculates the (unnormalized) log of the softmax over the last dimension of the input array.'
    assert result.blank_after_short_description

# Generated at 2022-06-13 19:46:13.508227
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc_text1 = """ This is a numpy docstring, parse it for its elements.
    Parameters
    ----------
    arg1 : int
        An integer.
    arg2 : float
        A float.
    Returns
    ----------
    str
        A string.

    See also
    ----------
    Docstring.
    """
    docstring1 = parse(doc_text1)
    assert (not docstring1.blank_after_short_description)
    assert (not docstring1.blank_after_long_description)
    assert (docstring1.short_description == "This is a numpy docstring, parse it for its elements.")
    assert (docstring1.long_description == None)
    assert (docstring1.meta[0].args[0] == "param")

# Generated at 2022-06-13 19:46:26.051587
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

# Generated at 2022-06-13 19:46:37.215304
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Sample docstring that follows Numpy style
    text = """This is a simple docstring.
    :param int age: Age of the person in years.
    :param str name: Name of the person.
    :return: personal information
    :rtype: dict
    """
    # Initialize a parser
    parser = NumpydocParser()
    ret = parser.parse(text)
    # Test whether the attributes of the Docstring instance are as expected
    assert ret.short_description == "This is a simple docstring.", "Short description failed."
    assert ret.long_description == "", "Long description failed."
    assert ret.blank_after_short_description == True, "Blank after short description failed."
    assert ret.blank_after_long_description == False, "Blank after long description failed."

# Generated at 2022-06-13 19:46:46.296983
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """
    This is a description of the docstring.
    This can be multi-line.

    :param param: description of param
    :type param: str

    :raises KeyError: raises an exception
    :returns: description of return
    :rtype: int
    """
    parser = NumpydocParser()
    result = parser.parse(docstring)
    assert result.short_description == "This is a description of the docstring."
    assert result.long_description == "This can be multi-line."
    assert len(result.meta) == 3
    assert result.meta[0].keywords == ["param"]
    assert result.meta[0].args == ["param", "param"]
    assert result.meta[0].description == "description of param"

# Generated at 2022-06-13 19:46:48.492605
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    obj = NumpydocParser()
    assert obj.parse('') == Docstring()


# Generated at 2022-06-13 19:46:59.285150
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:47:12.579783
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:47:18.575249
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """\
        Args:
            arg1 (int):
                default is 2
            arg2 (str, optional):
                default='test'
            arg3 (int, optional):
                default='test'

        """
    parser = NumpydocParser()
    doc = parser.parse(docstring)
    print(doc.meta)
    print(doc.long_description)
    print(doc.short_description)
    return doc

# Generated at 2022-06-13 19:47:23.141553
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    doc_string = parser.parse(NumpydocParser.__doc__)
    assert doc_string.long_description
    assert doc_string.long_description.endswith('.')
    for entry in doc_string.meta:
        assert entry.description.endswith('.')

# Generated at 2022-06-13 19:47:24.887386
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert NumpydocParser().parse("") == Docstring()


# Generated at 2022-06-13 19:47:35.009164
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    # Setup our test objects
    test_object = DeprecationSection
    test_string = ".. deprecated:: " + "1.0.0" + "\n\t" + "hello world"
    # Test the method parse
    assert next(test_object._parse_item(test_string, test_object.key)) ==  DocstringDeprecated(description='hello world', key='deprecated', version='1.0.0')

# Generated at 2022-06-13 19:47:42.432459
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    ds = DeprecationSection("deprecated", "deprecation")
    example_text = """
        .. deprecated:: 1.0

            This is the deprecated part
    """
    example_parse = [DocstringDeprecated(args=['deprecation'], description='This is the deprecated part', version='1.0')]
    assert ds.parse(example_text) == example_parse


# Generated at 2022-06-13 19:47:45.260675
# Unit test for constructor of class YieldsSection
def test_YieldsSection():
    y=YieldsSection("Yields", "yields")
    if(y.is_generator==True):
        print("Pass")
    else:
        print("Fail")
        

# Generated at 2022-06-13 19:47:50.430369
# Unit test for constructor of class DeprecationSection
def test_DeprecationSection():
    assert DeprecationSection("deprecated", "deprecation").title == "deprecated"
    assert DeprecationSection("deprecated", "deprecation").key == "deprecation"
    assert DeprecationSection("deprecated", "deprecation").title_pattern == "^\\.\\.\\s*(deprecated)\\s*::"

# Generated at 2022-06-13 19:47:54.866024
# Unit test for method parse of class Section
def test_Section_parse():
    section = Section("title1", "key1")
    text = "header\n----\nbody"
    assert section.parse(text) == DocstringMeta([section.key], description=_clean_str(text))



# Generated at 2022-06-13 19:48:01.294767
# Unit test for constructor of class ParamSection
def test_ParamSection():
    ps = ParamSection("Parameters", "param")
    assert ps.title == "Parameters"
    assert ps.key == "param"
    assert ps.title_pattern == r'^(Parameters)\s*?\n{}\s*$'.format("-" * len("Parameters"))


# Generated at 2022-06-13 19:48:08.642370
# Unit test for constructor of class ParamSection
def test_ParamSection():
    section = ParamSection("Parameters", "param")
    assert section.title_pattern == r"^(Parameters)\s*?\n-*$"
    assert section.parse("A description")[0].description == "A description"
    assert section.parse("A description\n-----------\n")[0].description == "A description"
    assert section.parse("A description")[0].args == ['param']


# Generated at 2022-06-13 19:48:09.749500
# Unit test for constructor of class DeprecationSection
def test_DeprecationSection():
    a = DeprecationSection


# Generated at 2022-06-13 19:48:10.407396
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    pass

# Generated at 2022-06-13 19:48:14.442908
# Unit test for constructor of class Section
def test_Section():
    section = Section("title", "key")
    assert section.title == "title"
    assert section.key == "key"
    assert section.title_pattern == "^title\s*?\n-*\s*$"


# Generated at 2022-06-13 19:48:32.370447
# Unit test for function parse
def test_parse():
    assert parse('Something') == Docstring(short_description='Something')
    assert parse('Something\n') == Docstring(short_description='Something')
    assert parse('Something\n'*2) == Docstring(short_description='Something')
    assert parse('Something\n'*2 + '\n') == Docstring(short_description='Something')



# Generated at 2022-06-13 19:48:34.024644
# Unit test for constructor of class ReturnsSection
def test_ReturnsSection():
    section = ReturnsSection('Returns', 'returns')
    assert section.is_generator == False


# Generated at 2022-06-13 19:48:34.637395
# Unit test for method parse of class Section
def test_Section_parse():
    pass

# Generated at 2022-06-13 19:48:37.601501
# Unit test for constructor of class Section
def test_Section():
    section = Section(title = "Parameters", key = "param")
    assert section.title == "Parameters"
    assert section.key == "param"
    

# Generated at 2022-06-13 19:48:47.302122
# Unit test for function parse
def test_parse():
    docstring = """
    Single-line description.

    Multi
    line
    description.

    Parameters
    ----------
    arg1 : str
        Long description of the first argument
    arg2 : list of int
        Second argument, with no real description

    Returns
    -------
    list of str
        Describes that we return a list of strings
    """
    parsed = parse(docstring)

    assert parsed.short_description == "Single-line description."
    assert parsed.long_description == "Multi\nline\ndescription."
    assert parsed.blank_after_short_description is True
    assert parsed.blank_after_long_description is False

    params = parsed.get("param")
    assert len(params) == 2

    params_dict = {}

# Generated at 2022-06-13 19:48:58.240265
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """Short description

    Long description with line breaks


    Parameters
    ----------
    arg : str
        first argument
    arg_2 : int, (optional)
        second argument
    arg_3 : float(42)
        third argument

    Returns
    -------
    None
        always
    """

    parser = NumpydocParser()
    doc = parser.parse(docstring)

    assert doc.short_description == "Short description"
    assert doc.long_description == "Long description with line breaks"

# Generated at 2022-06-13 19:49:04.448796
# Unit test for constructor of class ReturnsSection
def test_ReturnsSection():
    # Set default value
    title = 'This is Title'
    key = 'This is Key'
    
    # Create a ReturnsSection object
    rt = ReturnsSection(title, key)
    
    # Test if the constructor is working
    assert rt.title == title, "The constructor is Wrong"
    assert rt.key == key, "The constructor is Wrong"

    # Test is_generator
    assert rt.is_generator == False, "The is_generator default value is wrong"
    
    

# Generated at 2022-06-13 19:49:15.740938
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    text = """
        arg_name
            arg_description
        arg_2 : int, optional
            descriptions can also span...
            ... multiple lines
    """
    numpydoc_parser = NumpydocParser()
    section = ParamSection("Parameters", "param")
    parsed_text = list(section.parse(inspect.cleandoc(text)))
    assert parsed_text[0].name == "param"
    assert parsed_text[0].args[0] == "arg_name"
    assert parsed_text[0].description == "arg_description"
    assert parsed_text[1].name == "param"
    assert parsed_text[1].args[0] == "arg_2"
    assert parsed_text[1].type_name == "int"
    assert parsed_text[1].is_optional == True


# Generated at 2022-06-13 19:49:17.641540
# Unit test for constructor of class Section
def test_Section():
    s = Section("Parameters", "param")
    assert s.title == "Parameters"
    assert s.key == "param"

# Generated at 2022-06-13 19:49:23.095383
# Unit test for constructor of class Section
def test_Section():
    testSection = Section("Parameters:", "parameters")
    assert testSection.title_pattern == r"^(Parameters:)\s*?\n{0}\s*$".format("-" * len("Parameters:"))
    assert testSection.parse("testing the class")[0].args == ["parameters"]
    assert testSection.parse("testing the class")[0].description == "testing the class"


# Generated at 2022-06-13 19:49:55.869184
# Unit test for constructor of class NumpydocParser
def test_NumpydocParser():
    section = Section("this title", "this key")
    sections = NumpydocParser(sections = [section])
    assert sections.sections == {"this title":section}

# Generated at 2022-06-13 19:49:59.197275
# Unit test for constructor of class YieldsSection
def test_YieldsSection():
  y = YieldsSection("Yields", "yields")
  assert y.is_generator == True
  assert y.key == "yields"
  assert y.title == "Yields"

# Generated at 2022-06-13 19:50:09.044347
# Unit test for method parse of class Section
def test_Section_parse():
    # Create a section factory for testing purpose
    class testSection(Section):
        def __init__(self, title: str, key: str) -> None:
            super().__init__(title, key)
        
        def parse(self, text: str) -> T.Iterable[DocstringMeta]:
            yield DocstringMeta([self.key], description=_clean_str(text))

    # Create a test docstring text
    testText = "Test\n---\nThis is a test"

    testMeta = next(testSection(title="Test", key="test").parse(testText))
    
    assert testMeta.description == "This is a test", "Function testSection parse() does not create the correct meta"
    assert testMeta.args == ["test"], "Function testSection parse() does not create the correct meta"

# Unit test

# Generated at 2022-06-13 19:50:11.151705
# Unit test for constructor of class Section
def test_Section():
    title = "Parameters"
    key = "param"
    para = Section(title,key)
    assert para.title == title
    assert para.key == key


# Generated at 2022-06-13 19:50:15.800840
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    text = """
        arg1
            arg1 description
        arg2 : type
            arg2 description
    """
    parsed = list(_KVSection('test_title', 'test_key').parse(text))
    assert parsed == [
        DocstringMeta(['test_key', 'arg1'], 'arg1 description'),
        DocstringMeta(['test_key', 'arg2'], 'arg2 description')
    ]

# Generated at 2022-06-13 19:50:28.040705
# Unit test for method parse of class Section
def test_Section_parse():
    text1 = """arg_name
            arg_description
        arg_2 : type, optional
            descriptions can also span...
            ... multiple lines"""

    parser1 = ParamSection("Arguments", "param")
    docstring1 = parser1.parse(text1)
    assert(docstring1[0].arg_name == "arg_name")
    assert(docstring1[0].type_name is None)
    assert(docstring1[0].is_optional is None)
    assert(docstring1[0].default is None)
    assert(docstring1[1].arg_name == "arg_2")
    assert(docstring1[1].type_name == "type")
    assert(docstring1[1].is_optional == True)
    assert(docstring1[1].default is None)


# Generated at 2022-06-13 19:50:34.863051
# Unit test for constructor of class Section
def test_Section():
    title_one = "this is a test"
    key_one = "test"
    doc_string = Section(title_one, key_one)
    assert doc_string.title == title_one
    assert doc_string.key == key_one
    title_two = "this is test 2"
    key_two = "test 2"
    doc_string_two = Section(title_two, key_two)
    assert doc_string_two.title != title_one
    assert doc_string_two.key != key_one


# Generated at 2022-06-13 19:50:38.872728
# Unit test for constructor of class ParamSection
def test_ParamSection():
    param_section = ParamSection("Parameters", "param")
    assert param_section.title == "Parameters"
    assert param_section.key == "param"


# Generated at 2022-06-13 19:50:44.082862
# Unit test for constructor of class _SphinxSection
def test__SphinxSection():
    s = _SphinxSection("title1","key1")
    # title_pattern should have a pattern equal to "^\.\.\s*(title1)\s*::"
    if s.title_pattern != "^\.\.\s*(title1)\s*::":
        raise AssertionError("Section constructor does not work correctly")

# Generated at 2022-06-13 19:50:47.992099
# Unit test for constructor of class _SphinxSection
def test__SphinxSection():
    section1 =  _SphinxSection(
        title="returns",
        key="returns",
    )

    assert section1.title_pattern == r"^\.\.\s*(returns)\s*::"
    return True
