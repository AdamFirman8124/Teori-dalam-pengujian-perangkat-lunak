

# Generated at 2022-06-13 19:41:54.013704
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    section = _KVSection("Key", "key")
    text = "key\n  value\nkey2 : type\n  values can also span...\n  ... multiple lines"
    
    result = list(section.parse(text))

    if(result[0].description == _clean_str("value") and result[1].description == _clean_str("values can also span...\n  ... multiple lines")):
        print("test__KVSection_parse: success")
    else:
        print("test__KVSection_parse: fail")

test__KVSection_parse()


# Generated at 2022-06-13 19:42:04.077581
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    # Test a valid case
    text = """
        key
            value
        key2 : type
            values can also span...
            ... multiple lines
    """
    output = next(ParamSection("Parameters", "param").parse(text))
    assert output.args == ["param", "key"]
    assert output.description == "value"
    assert output.arg_name == "key"
    assert output.type_name == None
    assert output.is_optional == None
    assert output.default == None

    output = next(ParamSection("Parameters", "param").parse(text))
    assert output.args == ["param", "key2"]
    assert output.description == "values can also span..."
    assert output.arg_name == "key2"
    assert output.type_name == "type"
    assert output.is_optional == None

# Generated at 2022-06-13 19:42:12.421940
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:42:22.996205
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    p = _KVSection("test","test")
    teststr = "a\n    b\nb : int\n    c"
    meta1 = p._parse_item("a", "b")
    assert meta1.description == "b"
    meta2 = p._parse_item("b : int", "c")
    assert meta2.description == "c"
    meta3 = p._parse_item("c : str", "")
    assert meta3.description == ""
    meta4 = p._parse_item("d", "e")
    assert meta4.description == "e"

# Generated at 2022-06-13 19:42:26.330287
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    # setup
    sec = _KVSection('test', 'test')
    
    # test 1
    text = """\
        key
        key2 : type
            descriptions can also span...
            ... multiple lines
        """

    ret = sec.parse(text)
    assert list(ret) == [], "KVSection didn't return the expected value"


# Generated at 2022-06-13 19:42:33.018495
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    assert _KVSection("Parameters", "param").parse("") == []
    assert _KVSection("Parameters", "param").parse("arg_name\n    arg_description") == [DocstringParam(args=['param', 'arg_name'], arg_name='arg_name', default=None, description='arg_description', is_optional=None, type_name=None)]
    assert _KVSection("Parameters", "param").parse("arg_2 : type, optional\n    descriptions can also span...\n    ... multiple lines") == [DocstringParam(args=['param', 'arg_2'], arg_name='arg_2', default=None, description='descriptions can also span...\n... multiple lines', is_optional=True, type_name='type')]

# Generated at 2022-06-13 19:42:42.154237
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    # Test for description
    assert parse("""
A docstring
""").short_description == "A docstring"

    assert (
        parse("""
A docstring

""").short_description
        == "A docstring"
    )

    assert (
        parse("""
A docstring
    """).short_description
        == "A docstring"
    )

    assert (
        parse("""


A docstring
    """).short_description
        == "A docstring"
    )

    assert parse("""


A docstring

""").long_description == "A docstring"

    assert parse("""


A docstring

with a long description


""").long_description == "A docstring\nwith a long description"


# Generated at 2022-06-13 19:42:47.579160
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    assert parser.parse("") == Docstring()

    assert parser.parse("Hello world") == Docstring(
        short_description="Hello world",
        long_description=None,
        meta=[],
    )

    assert parser.parse("Hello world\n\nThis is a docstring.") == Docstring(
        short_description="Hello world",
        long_description="This is a docstring.",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[],
    )


# Generated at 2022-06-13 19:42:51.106995
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    title = "Other Parameters"
    key = "OtherParams"
    section = _KVSection(title, key)
    assert section.title == title
    assert section.key == key
    text = "arg_name\n    arg_description\narg_2 : type, optional\n    descriptions can also span...\n    ... multiple lines"
    section.parse(text)


# Generated at 2022-06-13 19:43:01.171588
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    class _KVSection(Section):
        def __init__(self, title: str, key: str) -> None:
            self.title = title
            self.key = key

        @property
        def title_pattern(self) -> str:
            return r"^({})\s*?\n{}\s*$".format(self.title, "-" * len(self.title))

        def _parse_item(self, key: str, value: str) -> DocstringMeta:
            pass

        def parse(self, text: str) -> T.Iterable[DocstringMeta]:
            for match, next_match in _pairwise(KV_REGEX.finditer(text)):
                start = match.end()
                end = next_match.start() if next_match is not None else None

# Generated at 2022-06-13 19:43:17.304462
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Setup test
    test_doc =\
    """
    .. _test_NUMPYdoc_parse:

    Parameters
    ----------
    a : int
        a value
    b : float, optional
        another value

    Returns
    -------
        a result

    Raises
    ------
    ValueError:
        If a value is wrong

    See Also
    --------
    test_numpydoc_parse.AttrList:
        Attribute list class
    """

    parser = NumpydocParser()
    doc = parser.parse(test_doc)

    assert len(doc.meta) == 3
    assert isinstance(doc.meta[0], DocstringParam)
    assert doc.meta[0].arg_name == 'a'
    assert doc.meta[0].type_name == 'int'
    assert doc

# Generated at 2022-06-13 19:43:23.360093
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text1 = '''This is a very simple function.

    Parameters
    ----------
    p1 : str
        A parameter with a description that spans
        multiple lines.
    p2 : int, optional
        Another parameter, with a default value of 42.

    Raises
    ------
    ValueError
        When the input is negative.

    Returns
    -------
    int
        Output value.

    Warns
    -----
    UserWarning
        When the input is zero.

    See Also
    --------
    OtherFunction

    Examples
    --------
    >>> simple_function('hello world')
    42
    '''
    assert parse(text1).long_description == 'This is a very simple function.'
    assert parse(text1).meta[0].args == ['param', 'p1']

# Generated at 2022-06-13 19:43:29.170557
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    d = ("""
    Test documentation

    This tests parsed documentation
    """)
    result = parser.parse(d)
    expected = Docstring(
        short_description="Test documentation",
        long_description="This tests parsed documentation",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[]
    )
    assert result == expected


# Generated at 2022-06-13 19:43:42.452554
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:43:47.498713
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
       Mostly flat description with some
       line breaks.

       Parameters
       ----------
       arg1 : float
           First argument.
       arg2 : int
           Second argument.
       arg3 : float
           Third argument.
           This is set by default. [default: 1.0]


       Raises
       ------
       ValueError
           If something goes wrong.

       Returns
       -------
       float
           The result.
       '''


# Generated at 2022-06-13 19:43:57.157430
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """"""
    parser = NumpydocParser()
    doc = inspect.cleandoc("""
    Compute the discretized pseudotimes and other information

    :param data: AnnData
    :param groupby: string, optional (default: None)
        The key of the observation grouping to consider.
    :param color_map: string, optional (default: None)
        A valid matplotlib color map name.
    :return:
        Returns an AnnData object with the following fields added.
    :rtype: AnnData
    """)

    ret = parser.parse(doc)
    assert ret.short_description == 'Compute the discretized pseudotimes and other information'



# Generated at 2022-06-13 19:43:59.240677
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Parse the numpy-style docstring into its components.

    :returns: parsed docstring
    """
    print(parse(text))

# Generated at 2022-06-13 19:44:03.190077
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = texts.numpydoc_test_docstring_string
    expected = texts.numpydoc_test_docstring_parsed
    assert parser.parse(text) == expected


# Generated at 2022-06-13 19:44:08.292351
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    class C:
        """
        The numpy-style docstring:

        :param arg_name: arg_description
        :type arg_name: type

        :param arg_2: arg_2 description
            which can span multiple lines

        :param arg_3: arg_3 description
        :type arg_3: type

        .. deprecated:: 0.1.0
            A warning about this function's deprecation until version 1.

        :returns: return_description

        :raises ValueError: raise_description
        :raises ValueError: raise_description
        :raises ValueError: raise_description

        :warns ValueError: warn_description

        :example: example_description
        """
        pass

    text = C.__doc__
    parser = NumpydocParser()
    ret = parser.parse(text)



# Generated at 2022-06-13 19:44:12.342626
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Parameters
    ----------
    x : str
        This is a string.
    name : str, optional
        Name of the method.
    """
    obj = NumpydocParser()
    assert len(obj.parse(text).meta) == 1
    assert obj.parse(text).meta[0].description == "Name of the method."


# Generated at 2022-06-13 19:44:29.393365
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    # empty (None)
    assert parser.parse(None) == Docstring()

    # empty (empty string)
    assert parser.parse("") == Docstring()

    # empty (just whitespace)
    assert parser.parse("\n\n  \t") == Docstring()

    # simplest example
    assert parser.parse("hello") == Docstring(
        short_description="hello",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )

    # simplest example plus newlines

# Generated at 2022-06-13 19:44:35.911575
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:38.126042
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydocParseObj = NumpydocParser()
    numpydocParseObj.parse("""No params.
        """
    )

# Generated at 2022-06-13 19:44:47.544216
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This is a test function

    Parameters
    ----------
    arg_1 : int
        A simple argument

    arg_2 : str, optional
        An optional argument

    arg_3 : str
        Default is ``one``

    arg_4 : int
        Default is ``2``

    arg_5 : str
        Defaults to ``"one"``

    Raises
    ------
    ValueError
        If `arg_1` is not 10

    Returns
    -------
    str
        The value of `arg_2` or ``Default`` if unspecified
    """
    doc = NumpydocParser().parse(text)
    assert doc.short_description == 'This is a test function'
    assert len(doc.meta) == 7
    assert doc.meta[0].key == 'param'

# Generated at 2022-06-13 19:44:55.858787
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Docstrings used by the unit test
    doc1 = """A simple docstring

    Additional lines in the docstring
    """

    doc2 = """A simple docstring with keywords

    :param arg_name: arg_description

    Additional lines in the docstring
    """

    doc3 = """A simple docstring with keywords

    :param arg_name: arg_description

    :type arg_name: type_description

    Additional lines in the docstring
    """

    doc4 = """A simple docstring with empty line above keyword


    :param arg_name: arg_description

    Additional lines in the docstring
    """


# Generated at 2022-06-13 19:45:02.437045
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
    This is a function.

    Parameters
    ----------
    a : array
        Parameter a.
    b : array
        Parameter b.

    Returns
    -------
    c : float
        Parameter c.

    Examples
    --------
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_numpy.py

    Section breaks are created by resuming unindented text. Section breaks
    are also implicitly created anytime a new section starts.
    '''
    parser = NumpydocParser()
    docstring = parser.parse(text)
    print(docstring.meta)

test_NumpydocParser_parse()

# Generated at 2022-06-13 19:45:13.462530
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    # Without all optional parameters and with no attributes
    parser.parse('''
    doc
        The one-line description.
        The rest of the description.

        Parameters
        ----------
        a : int
            The first parameter.

        Returns
        -------
        None
            Return description.
    ''')
    # Without doc
    parser.parse('''
        Parameters
        ----------
        a : int
            The first parameter.

        Returns
        -------
        None
            Return description.
    ''')
    # Without doc and without required parameters
    parser.parse('''
        Returns
        -------
        None
            Return description.
    ''')
    # Without doc, without required parameters and without attributes

# Generated at 2022-06-13 19:45:19.024721
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """
        This is a method summary line.

        Parameters
        ----------
        arg_name : type
            description

        arg_2 : type, optional
            description

        arg_3 : type, optional(default=1)
            description
        """
    assert parse(docstring).long_description == ' This is a method summary line.\n'
    assert parse(docstring).meta[0].type_name == 'type'
    assert parse(docstring).meta[1].default == '1'

# Generated at 2022-06-13 19:45:22.603925
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    NumpydocParser().parse("""
        title:
            paragraph1
            paragraph2.

        section1:
            title2:
                text2

        section2:
            title3:
                text3
    """)

# Generated at 2022-06-13 19:45:31.721559
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # method parse of class NumpydocParser
    # using class NumpydocParser instace
    parser = NumpydocParser()
    # class NumpydocParser method parse
    # input

# Generated at 2022-06-13 19:45:44.256074
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    # test 1
    text = """\
    This is the short summary

    This is the long summary

    Parameters
    ----------
    arg1
        arg1 description
    arg2 : type, optional
        arg2 description

    Raises
    ------
    ValueError
        A description of what might raise ValueError

    See Also
    --------
    :func:`func1`
    :func:`func2`
    """

    expected = Docstring()
    expected.short_description = "This is the short summary"
    expected.blank_after_short_description = True
    expected.blank_after_long_description = False
    expected.long_description = "This is the long summary"

# Generated at 2022-06-13 19:45:52.510864
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """
    Short description

    Long description
    multi-line

    Parameter
        arg_name
            arg_description
        arg_2 : type, optional
            descriptions can also span...
            ... multiple lines
    """

    # Setup
    numpydoc_parser = NumpydocParser()

    # Expectations
    short_description = "Short description"
    blank_after_short_description = False
    long_description = "Long description\nmulti-line"
    blank_after_long_description = True

# Generated at 2022-06-13 19:45:57.617037
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    s = "Hello World"
    docstring = NumpydocParser().parse(s)
    docstring.short_description == s
    docstring.long_description == None
    docstring.blank_after_short_description == False
    docstring.blank_after_long_description == False
    docstring.meta == []


# Generated at 2022-06-13 19:46:09.357763
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydoc_parser = NumpydocParser()
    text = '''
    This is a function.
    This is a function.More lines.

    Parameters
    ----------
    arg_name : type, optional
        A description of the argument.

    Returns
    -------
    return_name : type
        A description of the return value.
    '''
    doc_string = numpydoc_parser.parse(text)
    assert doc_string.short_description == 'This is a function.'
    assert doc_string.long_description == 'This is a function.More lines.'
    assert doc_string.blank_after_short_description == False
    assert doc_string.blank_after_long_description == True
    # The meta element is a list
    assert len(doc_string.meta) == 2
    assert doc

# Generated at 2022-06-13 19:46:17.866861
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from pathlib import Path
    from .common import Docstring, DocstringMeta, DocstringParam, DocstringReturns
    from .common import DocstringRaises, DocstringDeprecated

    section_path = Path(__file__).parent / "test_sections.rst"
    with open(section_path, "r") as f:
        text = f.read()

    docstring = NumpydocParser().parse(text)

# Generated at 2022-06-13 19:46:29.160242
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Function doing the following:
    - this
    - that
    Then, it takes the following params:
    - first : str
        A very long description
        with some more data
        and even more
    - second [default=5]
        Another description
    The method returns:
    - 1
    - 2
    """
    docstring = NumpydocParser().parse(text)
    assert docstring.short_description == "Function doing the following:"
    assert docstring.long_description == "- this\n- that"
    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is False
    assert len(docstring.meta) == 2
    assert docstring.meta[0].description.startswith(
        "A very long description"
    )

# Generated at 2022-06-13 19:46:38.804472
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:46:42.099500
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    dd = parser.parse('hello world\n.. deprecated:: 1.3.2\n\ndeprecation text')
    assert dd.meta[1].args[0] == "deprecation"



# Generated at 2022-06-13 19:46:56.158279
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    # empty docstring
    res = parser.parse("")
    assert res.short_description == None
    assert res.long_description == None

    # test different types of docstring
    test_docstring = """
    Docstring with only short_description

    Docstring with only long_description
    """
    res = parser.parse(test_docstring)
    assert res.short_description == 'Docstring with only short_description'
    assert res.long_description == 'Docstring with only long_description'
    assert res.blank_after_short_description == False
    assert res.blank_after_long_description == True


# Generated at 2022-06-13 19:47:02.284549
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert parse("") == Docstring()

    d = parse("""
    A short description.

    A long description.

    Parameters
    ----------
    a : int
        Parameter A
    b : str, optional
        Parameter B

    Returns
    -------
    int
        Return value
    """
    )
    assert d.short_description == "A short description."
    assert d.long_description == "A long description."
    assert d.meta[0] == DocstringParam(
        args=["param", "a"],
        type_name="int",
        description="Parameter A",
        arg_name="a",
    )

# Generated at 2022-06-13 19:47:11.953078
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # create a NumpydocParser object and add a new section to the parser
    parser = NumpydocParser()
    new_section = Section("Test", "test")
    parser.add_section(new_section)

    # create a test docstring

# Generated at 2022-06-13 19:47:21.111357
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydoc_parser = NumpydocParser()
    docstring_meta_list = numpydoc_parser.parse('This is short description\nThis is long description\n\nParameter1\n    This is parameter1 long description\nParameter2 : int, optional\n    This is parameter2 long description')
    assert docstring_meta_list.short_description == 'This is short description'
    assert docstring_meta_list.long_description == 'This is long description'
    assert docstring_meta_list.blank_after_short_description == True
    assert docstring_meta_list.blank_after_long_description == False
    assert len(docstring_meta_list.meta) == 2

# Generated at 2022-06-13 19:47:31.024943
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    .. title:: something
        possibly over multiple lines

    title
        value

    title2 : type
        values can also span...
        ... multiple lines

    """
    ret = NumpydocParser().parse(text)

    assert ret.short_description is None
    assert ret.blank_after_short_description is False
    assert ret.blank_after_long_description is False
    assert ret.long_description is None
    assert len(ret.meta) == 2

    title = ret.meta[0]
    assert title.name=='title'
    assert title.description=='value'
    assert title.args==[]

    title2 = ret.meta[1]
    assert title2.name=='title2'
    assert title2.description=='values can also span...\n    ... multiple lines'


# Generated at 2022-06-13 19:47:38.722360
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    text: str = """
    Some short description

        def foo(
            arg1: str,
            arg2: float = 1.0,
            *args,
            kwarg1: str = "hello",
            kwarg2: int = 2,
            **kwargs,
        ) -> None:
            pass

    Examples
        >>> foo("hello")
        >>> foo("world", 3, kwarg1="bye")
        >>> foo("world", kwarg1="default")

    Warnings
        This method is deprecated in version 1.0
    """


# Generated at 2022-06-13 19:47:48.207501
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

# Generated at 2022-06-13 19:47:53.972959
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    A short description
    A longer description

    Parses numpy-style docstring into its components.

    Parameters
    ----------
    text : str
        Docstring to be parsed

    Returns
    -------
    Docstring
        Parsed docstring
    """
    section = NumpydocParser().parse(text)
    assert section.short_description == 'A short description'
    assert section.long_description == 'A longer description\n\nParses numpy-style docstring into its components.'
    assert section.blank_after_short_description == True
    assert section.blank_after_long_description == True
    assert section.meta[0].args == ['param', 'text']
    assert section.meta[0].description == 'Docstring to be parsed'
    assert section.meta[0].arg_name

# Generated at 2022-06-13 19:48:04.575599
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
  # This is how a function's docstring looks like
  text = """Generate a random token.
  Returns:
    str: A random token.
  """

  # This is the output of method parse of class NumpydocParser
  output_parse_text = NumpydocParser().parse(text)

  # Test if the output is correct
  assert output_parse_text.short_description == 'Generate a random token.'
  assert output_parse_text.blank_after_short_description == True
  assert output_parse_text.blank_after_long_description == True
  assert output_parse_text.long_description == None
  assert output_parse_text.meta == [DocstringMeta(['returns'], None, 'A random token.')]


# Generated at 2022-06-13 19:48:16.012600
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # test sample docstring parser
    parser = NumpydocParser()
    # test short description
    assert parser.parse("""
        Short description
        More details
        More details
    """).short_description == "Short description"
    # test long description
    assert parser.parse("""
        Short description
        More details
        More details
    """).long_description == "More details\nMore details"
    assert parser.parse("""
        Short description
        More details
        More details
    """).blank_after_short_description == True
    assert parser.parse("""
        Short description
        More details
        More details
    """).blank_after_long_description == True

# Generated at 2022-06-13 19:48:32.403793
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .common import Docstring
    from .npd import NumpydocParser
    """
        Test function parse of class NumpydocParser
    """
    # Test case 1
    text='''
    This is a short description.

    This is a long description. It can have multiple lines.
    '''
    reference_desc='''\
    This is a short description.

    This is a long description. It can have multiple lines.
    '''
    npd_parser=NumpydocParser()
    assert npd_parser.parse(text).as_docstring(is_markdown=False) == Docstring(reference_desc)

    # Test case 2

# Generated at 2022-06-13 19:48:43.085609
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    print(parser.parse('some function'))
    print(parser.parse('some function\n\nfunction description'))
    print(parser.parse('some function\n\nfunction description\n\nparams: int, optional'))

# Generated at 2022-06-13 19:49:00.180512
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    sample = """
    my function

    Arguments:
        arg1 : type
            description

        arg2 : other_type
            second description

        arg3 : list_of_things, optional
            this is optional
            has a default of []
            more description

    Other Arguments:
        other1 : other_type
            other argument description

    Raises:
        ValueError : if something goes wrong

    Returns:
        return_name : type
            return description

    Example:
        >>> function(arg1=True)
    """

    parser = NumpydocParser()
    docstring = parser.parse(sample)
    print(docstring.to_json(indent=4))

    print(docstring.short_description)
    print([p.description for p in docstring.meta])

# Generated at 2022-06-13 19:49:09.713741
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    ndp = NumpydocParser()
    test_1 = """
    This is the short description

    This is the long
    description.

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    """
    test_2 = """
    This is the short description

    This is the long
    description.

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Raises
    ------
    KeyError
        When a key error
        occurs.

    Returns
    -------
    bool
        True if successful, False otherwise.

    """

# Generated at 2022-06-13 19:49:12.147682
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Test NumpydocParser.parse method"""
    # TODO
    pass

# Generated at 2022-06-13 19:49:21.483357
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .numpydoc import parse
    ex = '''This function does some stuff.
    Parameters
    ----------
    arg : str
        A description of the argument
    arg2 : int, optional
        Description of the second argument. Default is 5.
    key1 = 'Value1', key2 = 2
        And here is a non-standard kwarg
    Returns
    -------
    string
        A description of the returned value
    Warnings
    --------
    This is a warning
    Notes
    -----
    Some notes
    Examples
    --------
    >>> some_function()
    'some_value'
    References
    ----------
    .. [1] Some reference
    '''

    res = parse(ex)

    assert res.short_description == 'This function does some stuff.'
    assert res.long_description == ''


# Generated at 2022-06-13 19:49:31.639237
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """Summation of 1/n**3 from 1 to n.

    Parameters
    ----------
    n : int
        Upper limit.

        Parameters
        ----------
        n : int
            Upper limit.

    Returns
    -------
    float
        1/n**3 sum.

    Examples
    --------
    >>> euler_zeta(3)
    1.2020569031595942

    Notes
    -----
    The magic happens in Cython.

    """
    parsed_docstring = parse(docstring)
    assert parsed_docstring.short_description == "Summation of 1/n**3 from 1 to n."
    assert parsed_docstring.long_description == "The magic happens in Cython."
    assert parsed_docstring.blank_after_short_description

# Generated at 2022-06-13 19:49:42.460272
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """
    Parameters
    ----------
    x : int, optional
        A description of what x is.

    z : int, optional
        A description of what z is.

    Returns
    -------
    int
        A description of what this returns.
    """

# Generated at 2022-06-13 19:49:47.036031
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Test case 1
    assert NumpydocParser().parse("this is a numpydoc docstring") == Docstring(
        short_description="this is a numpydoc docstring", meta=[]
    )
    # Test case 2
    assert NumpydocParser().parse("this is a numpydoc docstring. \n" +
                                  "Args: \n" +
                                  "    arg_1 (type): description") == Docstring(
        short_description="this is a numpydoc docstring.",
        meta=[
            DocstringParam(
                args=["param", "arg_1"],
                description="description",
                arg_name="arg_1",
                type_name="type",
                is_optional=False,
            ),
        ],
    )
    # Test case 3
    assert N

# Generated at 2022-06-13 19:49:58.598363
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = Docstring()
    docstring.short_description = "A demo for showing docstring parsing"
    docstring.blank_after_short_description = False
    docstring.blank_after_long_description = False
    docstring.long_description = (
        "Longer description with multiple paragraphs\n\n"
        "Here is a new paragraph.\n\n"
        "And another."
    )

# Generated at 2022-06-13 19:50:08.299071
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Case 1: 
    text ="""
    This is the short description.
    This line is not indented.
    This is the long description.  It should be indented.
    
        This line is indented and belongs to the long description.
        As does this one.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    int
        Description of return value

    """
    expected_short = "This is the short description."
    expected_long = "This is the long description. It should be indented.\n\n    This line is indented and belongs to the long description.\n    As does this one."
    expected_blank_1 = True
    expected_blank_2 = True

# Generated at 2022-06-13 19:50:15.190201
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    # test of method parse
    text = """
        This is a description

        Parameters
        ----------
        arg_1 : str
            This is a description of the first argument.

        arg_2 : int
            This is a description of the second argument.

        Returns
        -------
        value : int
            Returns the value
        """
    docstring = NumpydocParser().parse(text)
    print(docstring)
    assert docstring.short_description == 'This is a description'
    assert docstring.long_description == 'Parameters\n----------\narg_1 : str\n    This is a description of the first argument.\n\narg_2 : int\n    This is a description of the second argument.\n\nReturns\n-------\nvalue : int\n    Returns the value'
    assert docstring.blank

# Generated at 2022-06-13 19:50:30.832253
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    # Unit test for empty docstring
    assert '' == len(parser.parse(''))

    # Unit test for short description
    shortDescription = parser.parse('short description')
    assert 'short description' == shortDescription.short_description
    assert '' == shortDescription.long_description
    assert '' == shortDescription.meta

    # Unit test for long description
    longDescription = parser.parse(
        'First line of the docstring\nSecond line of the docstring\nLast line of the docstring')
    assert 'First line of the docstring' == \
        longDescription.short_description
    assert 'Second line of the docstring\nLast line of the docstring' == \
        longDescription.long_description
    assert '' == longDescription.meta

    # Unit test for short description and title
   

# Generated at 2022-06-13 19:50:42.889037
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """function to test method parse of class NumpydocParser"""
    parser = NumpydocParser()
    text = '''
        This is the `short description.

        This is the long
        description.  Longer than a single line.

        This is a warning section:

        .. warning::
            You should probably read this.

        You can also put in examples,
        which are useful for teaching::

            >>> print(a + b)
            5

        Parameters
        ----------
        first : int
            This is the first parameter.
        second
            This is the second parameter.

        Returns
        -------
        str
            This is the return value.

        Raises
        ------
        ValueError
            This exception is raised when `x` is out of bounds.
        '''

# Generated at 2022-06-13 19:50:49.607439
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Test unparseable
    assert parse(None) == Docstring()

    # Test empty
    assert parse("") == Docstring()

    # Test title but no body
    assert parse("Title\n-----") == Docstring(
        short_description="Title", blank_after_short_description=True,
        blank_after_long_description=True
    )

    # Test title and body
    assert parse("Title\n-----\nBody") == Docstring(
        short_description="Title", blank_after_short_description=False,
        long_description="Body", blank_after_long_description=True
    )

    # Test body with preceding blank

# Generated at 2022-06-13 19:50:55.375129
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = parser.parse("""
    .. title:: something
        possibly over multiple lines
    """)
    ref = Docstring(
        short_description="",
        long_description="",
        meta=[
            DocstringMeta(
                args=["title"],
                description="something\npossibly over multiple lines",
            )
        ],
    )
    assert docstring == ref


# Generated at 2022-06-13 19:51:06.060558
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Parse the numpy-style docstring into its components.

    :param text: docstring text
    :returns: parsed docstring

    Short description.

    Long description.

    This is three paragraphs.

    Parameters
    ----------
    text : str
        Docstring text.

    Returns
    -------
    result : Docstring
        Parsed docstring.

    Raises
    ------
    ValueError
        If this result is not a Docstring.
    """

    docstring = NumpydocParser().parse(text)

    # check docstring
    print(docstring.short_description)

test_NumpydocParser_parse()

# Generated at 2022-06-13 19:51:16.893754
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """\
    This function does some cool stuff

    Parameters
    ----------
    arg1 : str
        The first argument
    arg2 : int
        The second argument

    Returns
    -------
    str
        The return value

    Raises
    ------
    AttributeError
        The reason why it is raised
    """
    ds = NumpydocParser().parse(docstring)
    assert ds.short_description.strip() == "This function does some cool stuff"
    assert len(ds.meta) == 3
    assert len(ds.meta[0]) == 1
    assert ds.meta[0][0].description.strip() == "The first argument"
    assert len(ds.meta[1]) == 1
    assert ds.meta[1][0].description.strip() == "The second argument"
