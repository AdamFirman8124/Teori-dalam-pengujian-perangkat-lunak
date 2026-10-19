

# Generated at 2022-06-13 19:41:42.662977
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    """Unit test for method parse of class DeprecationSection"""
    text = inspect.cleandoc('deprecated:: 0.1\n    description')
    deprecation_section = DeprecationSection('deprecated', 'deprecation')
    deprecation_section_meta = deprecation_section.parse(text)
    deprecation_section_meta_list = list(deprecation_section_meta)
    assert (len(deprecation_section_meta_list) == 1)
    assert (deprecation_section_meta_list[0].args == ['deprecation'])
    assert (deprecation_section_meta_list[0].description == 'description')
    assert (deprecation_section_meta_list[0].version == '0.1')


# Generated at 2022-06-13 19:41:50.486512
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    assert list(_KVSection("Parameters", "param").parse("")) == list()

    assert list(_KVSection("Parameters", "param").parse("arg_name\n    description")) == [DocstringMeta(["param", "arg_name"], description="description")]

    assert list(_KVSection("Parameters", "param").parse("arg_name\n    description\narg_2 : type\n    another description")) == [DocstringMeta(["param", "arg_name"], description="description"),DocstringMeta(["param", "arg_2"], description="another description")]


# Generated at 2022-06-13 19:42:00.872146
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Case 1: input string is empty
    assert (NumpydocParser().parse('') == Docstring())

    # Case 2: input string has short_description and long_description
    docstring_long1 = '''A short description.
    A longer description.
    '''
    docstring_long2 = '''A short description.

A longer description.
'''
    assert (NumpydocParser().parse(docstring_long1) == Docstring(short_description = 'A short description.',
        long_description = 'A longer description.', blank_after_long_description = False,
        blank_after_short_description = True))

# Generated at 2022-06-13 19:42:07.113408
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    section = DeprecationSection(title="Deprecation Warning", key="deprecated")
    description = inspect.cleandoc("\n    This is a deprecation warning\n")
    meta = section.parse(description)

    assert isinstance(meta, tuple)
    assert len(meta) == 1
    assert isinstance(meta[0], DocstringDeprecated)
    assert meta[0].description == description.strip()


# Generated at 2022-06-13 19:42:21.596710
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    '''Unit test for method parse of class _KVSection

    :param: A test string
    :return: None
    '''
    # Case where every line is parsed correctly
    test_string = (
        'key\n'
        '    value\n'
        'key2 : type\n'
        '    values can also span...\n'
        '    ... multiple lines\n'
    )
    result = _KVSection('key', 'meta_key_1').parse(test_string)
    assert next(result)[0] == 'key'
    assert next(result)[0] == 'key2'

# Generated at 2022-06-13 19:42:31.961812
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    """
    Method parse of class DeprecationSection
    Output: DocstringDeprecated
    """
    class_var = DeprecationSection("deprecated", "deprecation")
    str_var = """DeprecationWarning
    This function is deprecated and will be removed in future versions. Please
    use :class:`pint.Quantity` instead.
    """
    output = class_var.parse(text = str_var)
    assert output[0] == (
        DocstringDeprecated(
            args = ['deprecation'],
            description = 'This function is deprecated and will be removed in future versions. Please use :class:`pint.Quantity` instead.',
            version = 'DeprecationWarning',
        )
    )

# Generated at 2022-06-13 19:42:35.621610
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    section = _KVSection(title="test", key="test")
    lines = """
    key
        value
    key2 : type
        values can also span...
        ... multiple lines
    """
    meta = next(section.parse(lines))
    assert meta == DocstringMeta(["test"], description="value")



# Generated at 2022-06-13 19:42:44.979897
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = """Foo bar.

    Parameters
    ----------
    arg_a : str
        The first argument
    arg_b : int
        The second argument

    Return
    ------
    dict
        dict of str
    """

    doc = parser.parse(text)
    assert doc.short_description == 'Foo bar.'
    assert doc.long_description == 'The first argument\nThe second argument'
    assert len(doc.meta) == 2
    assert doc.meta[0].args[1] == 'arg_a'
    assert doc.meta[0].description == 'The first argument'
    assert doc.meta[0].arg_name == 'arg_a'
    assert doc.meta[0].type_name == 'str'

# Generated at 2022-06-13 19:42:50.006276
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    text = '''key
            value
        key2 : type
            values can also span...
            ... multiple lines'''

    section = _KVSection('-', '')
    meta = section.parse(text)

    assert isinstance(meta, T.Iterable)
    assert isinstance(list(meta)[0], DocstringMeta)
    assert meta.args[0] == ''
    assert meta.description == 'value'



# Generated at 2022-06-13 19:42:56.252012
# Unit test for method parse of class Section
def test_Section_parse():
    from .common import DocstringParam
    from textwrap import dedent
    sec = ParamSection("Parameters", "param")
    docstring = "a\n    a\nb : type\n    b"
    result = sec.parse(docstring)
    assert result == [DocstringParam(["param", "a"], description="a"),
                      DocstringParam(["param", "b"], description="b", type_name="type")]



# Generated at 2022-06-13 19:43:12.291244
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Test method

    Parameters
    ----------
    arg1 : int, optional
        First argument

    Returns
    -------
    str
        Test string
    """
    docstring_instance = NumpydocParser().parse(text)
    short_description, long_description, attributes = (
        docstring_instance.short_description,
        docstring_instance.long_description,
        docstring_instance.meta,
    )
    assert short_description == "Test method"
    assert long_description is None

# Generated at 2022-06-13 19:43:23.415558
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''Examples
    ----------
    This is an example of a long explanation

    >>> import numpy as np
    >>> np.array([1, 2, 3], dtype=np.object)
    array([1, 2, 3], dtype=object)

    '''
    assert text.find('Examples') == 0
    docstring = NumpydocParser().parse(text)
    assert str(docstring) == 'Meta:\n    examples:\n        …\n'
    assert docstring.meta[0].args[0] == 'examples'
    assert docstring.meta[0].description == 'This is an example of a long explanation\n\n>>> import numpy as np\n>>> np.array([1, 2, 3], dtype=np.object)\narray([1, 2, 3], dtype=object)'

# Generated at 2022-06-13 19:43:33.415934
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Args:
        input: The input value.
        name: The name of the input value.

    Returns:
        A value.

    Raises:
        ValueError: If any argument is invalid.
    """

    doc = NumpydocParser().parse(text)
    assert len(doc.meta) == 3
    assert doc.meta[0].args == ['param', 'input']
    assert doc.meta[0].description == 'The input value.'
    assert doc.meta[1].args == ['param', 'name']
    assert doc.meta[1].description == 'The name of the input value.'
    assert doc.meta[2].args == ['raises', 'ValueError']
    assert doc.meta[2].description == 'If any argument is invalid.'
    assert doc.short_description == ''
   

# Generated at 2022-06-13 19:43:43.197851
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import textwrap

    def _test_parse(text: str, expected: T.Dict[str, T.Optional[str]]):
        actual = NumpydocParser().parse(text)
        assert actual.short_description == expected["short_description"]
        assert actual.long_description == expected["long_description"]
        assert actual.blank_after_short_description == expected[
            "blank_after_short_description"
        ]
        assert actual.blank_after_long_description == expected[
            "blank_after_long_description"
        ]
        assert [
            (m.args, m.description)
            for m in actual.meta
            if m.args != ["see_also", "numpydoc"]
        ] == expected["meta"]


# Generated at 2022-06-13 19:43:48.916665
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc = inspect.cleandoc("""
    This is a unit test.

    blablabla

    Parameters
    ----------
    x : float
        x coordinate

    Returns
    -------
    float
        y coordinate
    """)

# Generated at 2022-06-13 19:43:59.457187
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Meta section test
    Docstring_meta = DocstringMeta(["param", "test_meta_param"], description="test_meta_param_desc")
    parser = NumpydocParser()
    doc = parser.parse('''test
        Parameters
        ----------
        test_meta_param:
            test_meta_param_desc''')
    assert len(doc.meta) == 1
    assert len(doc.meta[0].args) == 2
    assert doc.meta[0].args[0] == Docstring_meta.args[0]
    assert doc.meta[0].args[1] == Docstring_meta.args[1]
    assert doc.meta[0].description == Docstring_meta.description

    # Description section test
    doc = parser.parse('''testdesc
        testdesc2''')
   

# Generated at 2022-06-13 19:44:09.039057
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This docstring will contain
    a short description and a long description,
    separated by an empty line.

    Parameters
    ----------
    args : type
        description
        text can extend over
        multiple lines
    kwargs : type, optional
        optional keyword args:
        - with defaults:
            key : value, optional
                Default is 42.
        - without defaults:
            key : type, optional
                Description.
    
    Returns
    -------
    value : int
        Description of return type
    """

    # Check if the docstring is correctly parsed.

# Generated at 2022-06-13 19:44:16.406615
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = parser.parse("")
    assert text == Docstring()

    text2 = parser.parse("""
        doc_name.

        doc_description
    """)
    assert text2.short_description == "doc_name."
    assert text2.long_description == "doc_description"

    text3 = parser.parse("""
        doc_name.

        This is long description.
    """)
    assert text3.short_description == "doc_name."
    assert text3.long_description == "This is long description."

    text4 = parser.parse("""
        doc_name.
        This is long description.
    """)
    assert text4.short_description == "doc_name."
    assert text4.long_description == "This is long description."

   

# Generated at 2022-06-13 19:44:29.668219
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc = '''
    Simulate a simple random walk process.

    Parameters
    ----------
    start : `array_like` (float)
        The starting point of the random walk.

    Returns
    -------
    array_like (float)
        A random walk of length ``len(index)`` + 1.

    See Also
    --------
    :meth:`statsmodels.tsa.arima_process.arma_generate_sample`
    '''


# Generated at 2022-06-13 19:44:36.644021
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydoc_parser = NumpydocParser()
    docstring = numpydoc_parser.parse("First line of the docstring\n")
    assert docstring.short_description == "First line of the docstring"
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert docstring.meta == []

    docstring = numpydoc_parser.parse("""\
    First line of the docstring
    Second line of the docstring
    """)
    assert docstring.short_description == "First line of the docstring"
    assert docstring.long_description == "Second line of the docstring"
    assert docstring.blank_after_short_description is True
    assert docstring.blank

# Generated at 2022-06-13 19:44:46.947023
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print('Running test_NumpydocParser_parse')

    class Subclass(NumpydocParser):
        """Subclass of NumpydocParser with a custom section.

        """

        def __init__(self):
            super().__init__()
            self.add_section(
                Section(
                    "Additional",
                    "additional",
                )
            )

    # Test a single section header with a value
    text = dedent(
        """\
        Test a single section header with a value

        Parameters
        ----------
        arg_1
            A description of the argument
    """
    )
    docstring = Subclass().parse(text)

    assert docstring.short_description == "Test a single section header with a value"
    assert docstring.long_description == None

# Generated at 2022-06-13 19:44:55.363346
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Taken from https://numpydoc.readthedocs.io/en/latest/format.html#section-headers
    test_string1 = """This is a test function.
    
    This function does nothing but tests parsing of arguments.
    
    Parameters
    ----------
    arg1 : int
        First argument.
        Second line of first argument.
    arg2 : str, optional
        Second argument, default is 'world'.
    
    Returns
    -------
    Nothing.
    
    """


# Generated at 2022-06-13 19:45:02.279140
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """Short description

Long description, longer than
a single line.

Attributes
----------
c : string
    A string to be repeated

Returns
-------
repeated_string : string
    The string repeated `n` times

    """
    docstring = NumpydocParser().parse(text)
    assert docstring.short_description=="Short description"
    assert docstring.long_description=="Long description, longer than\na single line."
    assert docstring.meta[0].description=="A string to be repeated"
    assert docstring.meta[0].type_name=="string"
    assert docstring.meta[0].args[0]=="attribute"
    assert docstring.meta[0].args[1]=="c"

# Generated at 2022-06-13 19:45:13.257404
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = parser.parse(
        inspect.cleandoc(
            """
            The :func:`~typing.no_type_check` decorator

            This is the short description

            This is the long description


            Parameters
            ----------
            arg_name : arg_type
                arg_description
            arg_2 : arg_type, optional
                How to use the optional arg_2


            Returns
            -------
            return_type
                return_description

            Warns
            -----
            UserWarning
                if something weird happens


            References
            ----------
            https://www.python.org/dev/peps/pep-0484/
                PEP0484 specification
            """
        )
    )

    assert len(docstring.meta) == 4

# Generated at 2022-06-13 19:45:22.555181
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    Test the parse method of NumpydocParser class.

    :return: Nothing
    """
    print("\ninvoke test_NumpydocParser_parse")
    print("===============================")
    print("Test the parse method of NumpydocParser class")
    print("----------------------------------------------")
    test1 = """
    This is the short description.

    This is the long description.  The long description is
    used to demonstrate the wrapping of text, which should
    be automatically wrapped.

    Parameters
    ----------
    arg1 : int
        Description of `arg1`

    Returns
    -------
    bool
        Description of return value
    """
    print("\nTest 1")
    print("------")
    print("Input:\n", test1)
    ndp1 = NumpydocParser()
    ret

# Generated at 2022-06-13 19:45:29.492821
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    
    docstring = '''
    Takes an array of numbers and returns a tuple of numbers.
    The returned tuple contains the minimum and maximum
    numbers in the given array.

    :param numbers: Array of numbers
    :returns: A tuple of numbers
    :raises: :class:`ValueError` if the given iterable is empty
    '''
    NumpydocParser().parse(docstring)
    # should not be empty
    print(docstring)
    
if __name__ == "__main__":
    test_NumpydocParser_parse()

# Generated at 2022-06-13 19:45:40.767324
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    assert parser.parse("") == Docstring()

    text = """\
    This is a short description
    
    this is a longer description
    
    and it goes over multiple lines
    
    Parameters
    ----------
    arg1
        argument 1
    arg2 : str
        argument 2
    arg3, optional
        argument 3
    arg4, optional(default=1.2)
        argument 4
    
    Returns
    -------
    
    
    """

# Generated at 2022-06-13 19:45:51.552132
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    
    # Test empty docstring
    assert parse("").short_description is None
    assert parse("").long_description is None
    
    # Test short description
    assert parse("Short description").short_description == "Short description"
    assert parse("Short description").long_description is None
    
    # Test short description followed by blank line
    assert parse("Short description\n\n").short_description == "Short description"
    assert parse("Short description\n\n").long_description is None
    assert parse("Short description\n\n").blank_after_short_description
    
    # Test short description followed by newline and not followed by a blank line
    assert parse("Short description\nLong description").short_description == "Short description"
    assert parse("Short description\nLong description").long_description == "Long description"

# Generated at 2022-06-13 19:46:03.003985
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    Test NumpydocParser.parse() function.
    """
    class test:
        """
        Short description for test.

        This is the long description for test.

        Parameters
        ----------
        x: int, optional
            x parameter for test. Default is 0.
        y: dict
            y parameter for test.
        """
        def __init__(self):
            pass

    docstr = parse(test.__doc__)
    assert docstr.short_description == "Short description for test."
    assert docstr.long_description == "This is the long description for test."
    assert docstr.blank_after_long_description is True
    assert docstr.blank_after_short_description is False
    assert len(docstr.meta) == 2
    assert len(docstr.meta[0].args)

# Generated at 2022-06-13 19:46:05.931056
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import unittest
    import doctest
    suite = doctest.DocTestSuite(NumpydocParser)
    unittest.TextTestRunner().run(suite)


# Generated at 2022-06-13 19:46:12.605580
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text ="""
Parse the numpy-style docstring into its components.

:returns: parsed docstring


Parameters
----------
text : str
    docstring to parse

Return
------
Docstring
    parsed docstring

Raises
-------
ValueError
    if ``text`` is empty
    """

# Generated at 2022-06-13 19:46:24.936115
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    short description
    
    long description
    
    Parameters
    ------------
    arg_name
        arg_description
    arg_2 : type, optional
        descriptions can also span...
        ... multiple lines
        
    Raises
    -------
    ValueError
        A description of what might raise ValueError
    """
    docstring = NumpydocParser().parse(text)
    assert docstring.short_description == "short description"
    assert docstring.long_description == "long description"
    assert (
        docstring.meta[0].description == "arg_description"
    ) or (
        docstring.meta[0].description == "descriptions can also span...\n... multiple lines"
    )
    assert docstring.meta[1].description == "A description of what might raise ValueError"

# Generated at 2022-06-13 19:46:36.411385
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # setup
    text = inspect.cleandoc("""
    This is the example docstring.

    Parameters
    ----------
    a
        This is param a
    b: int
        This is param b
    c, optional
        This is param c

    Returns
    -------
    int
        This is the return value.

    Raises
    ------
    Exception
        This is a potential exception.
    """)
    parser = NumpydocParser()

# Generated at 2022-06-13 19:46:38.053311
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    pd = NumpydocParser()
    # This method is empty.



# Generated at 2022-06-13 19:46:46.778694
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydoc_parser = NumpydocParser()
    assert numpydoc_parser.parse("no\ndoc") == Docstring(short_description="no", long_description="doc")
    assert numpydoc_parser.parse("no\n\ndoc") == Docstring(short_description="no", long_description="doc")
    assert numpydoc_parser.parse("no\n\n\ndoc") == Docstring(short_description="no", long_description="\ndoc")
    assert numpydoc_parser.parse("\nno\n\n\ndoc") == Docstring(short_description="\nno", long_description="\ndoc")

# Generated at 2022-06-13 19:46:56.157568
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """\
    This is the first line of the first paragraph.

    This is the second paragraph.

    Parameters
    ----------
    foo : str
        A description of foo.

        Continuing description of foo.
    bar : int, optional
        A description of bar.

    Returns
    -------
    str
        A description of the return value.

        Continuing description of the return value.
    """
    assert NumpydocParser().parse(docstring) == NumpydocParser().parse(docstring)

# Generated at 2022-06-13 19:47:03.760100
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Short description.

    Longer description that can
    span multiple lines.

    Parameters
    ----------
    arg_name
        arg_description
    arg_2 : type, optional
        descriptions can also span
        ... multiple lines

    Raises
    ------
    ValueError
        A description of what might raise ValueError

    Returns
    -------
    return_name : type
        A description of this returned value
    another_type
        Return names are optional, types are required

    Examples
    --------
    >>> 1 + 1
    2
    """
    docstring = NumpydocParser().parse(text)
    assert docstring.short_description is not None
    assert docstring.long_description is not None

    # Parameters
    assert len(docstring.meta) == 8

# Generated at 2022-06-13 19:47:14.698194
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:47:17.686746
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    output = NumpydocParser().parse("""Parameters
    ----------
    title: str,
        Title of the plot, visible at the top of the figure
    """)
    assert output.meta[0].args == ['param', 'title']

# Generated at 2022-06-13 19:47:28.072347
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This is a short description

    Lorem ispum etc.

    Parameters
    ----------
    arg_1 : type, optional
        Description for arg_1.
        Default is "hello"
    arg_2 : type
        Description for arg_2
        Default is None

    Returns
    -------
    return_1
        Description for return_1

    See Also
    --------
    This is a ref

    """

    parsed_docstring = NumpydocParser().parse(text)
    assert parsed_docstring.short_description == 'This is a short description'
    assert parsed_docstring.blank_after_short_description == False
    assert parsed_docstring.long_description == 'Lorem ispum etc.'
    assert parsed_docstring.blank_after_long_description == False
    assert parsed_

# Generated at 2022-06-13 19:47:38.262421
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:47:47.980781
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Test success
    docstring = \
        """
        :param str arg_name: arg_description
        :param int arg2: arg2_description
        """
    doc = NumpydocParser().parse(docstring)
    assert (doc.meta[0].args == ["param", "arg_name"]), \
        "Incorrect parsing for :param directive"
    assert (doc.meta[1].args == ["param", "arg2"]), \
        "Incorrect parsing for :param directive"

    # Test failure
    docstring = \
        """
        :param str arg_name: arg_description
        :param int arg2: arg2_description
        :param str arg3: arg3_description
        """

# Generated at 2022-06-13 19:47:58.914277
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydocParser = NumpydocParser()
    assert numpydocParser.parse("") is not None
    assert numpydocParser.parse("") == Docstring()
    assert numpydocParser.parse("Test short description.") == Docstring(
            short_description="Test short description."
        )
    docstring = numpydocParser.parse("Test short description.\n\nTest long description.")
    assert docstring.short_description == "Test short description."
    assert docstring.blank_after_short_description == True
    assert docstring.long_description == "Test long description."
    assert docstring.blank_after_long_description == False

# Generated at 2022-06-13 19:48:11.427899
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:48:20.481090
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = "This is a test"
    result = parser.parse(text)
    assert(result.short_description == "This is a test")
    assert(result.long_description == None)
    assert(result.blank_after_short_description == False)
    assert(result.blank_after_long_description == None)
    assert(result.meta == [])

    text = "This is a test \n \n"
    result = parser.parse(text)
    assert(result.short_description == "This is a test")
    assert(result.long_description == None)
    assert(result.blank_after_short_description == True)
    assert(result.blank_after_long_description == None)
    assert(result.meta == [])

# Generated at 2022-06-13 19:48:25.703439
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """Summary line.

    Extended description.

    Parameters
    ----------
    arg1 : int
        Description of `arg1`

    arg2 :
        Description of `arg2`

    arg3 : optional, type
        Description of `arg3`

    arg4, optional:
        Description of `arg4`

    arg5 :
        Description of `arg5`

    Returns
    -------
    int or None
        Description of return value

    Warns
    -----
    UserWarning
        When something bad happened.

    Warns
    -----
    UserWarning
        When something bad happened.
    """
    ndparse = NumpydocParser()
    ndparse.parse(docstring)
    return ndparse.parse(docstring)

# Generated at 2022-06-13 19:48:33.055360
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import numpy
    parser = NumpydocParser()

    text = numpy.__doc__
    assert len(parser.parse(text)) > 0
    assert len(parser.parse(text).meta) > 0
    assert parser.parse(text).short_description != None
    assert parser.parse(text).long_description != None
    assert parser.parse(text).blank_after_long_description != None
    assert parser.parse(text).blank_after_short_description != None

# Generated at 2022-06-13 19:48:43.754015
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    # A docstring with a short description
    text = ('This is a short description. '
            'It has a second sentence.')
    parsed = parser.parse(text)
    # parsed.short_description
    assert parsed.short_description == text
    assert parsed.blank_after_short_description is False
    assert parsed.long_description is None
    assert parsed.blank_after_long_description is True
    assert parsed.meta == []

    # A docstring with a long description
    text = ('This is a short description.\n'
            '\n'
            'It has a second paragraph, which is\n'
            'indented, and a third paragraph\n'
            'which is not.\n'
            '\n'
            'It also has a fourth paragraph.')

# Generated at 2022-06-13 19:48:53.892746
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert (NumpydocParser().parse("this is a method to test unit test")) == Docstring(short_description='this is a method to test unit test', meta=[])
    assert (NumpydocParser().parse("this is a method to test unit test\n\nTEST")) == Docstring(short_description='this is a method to test unit test', long_description='TEST', meta=[])
    assert (NumpydocParser().parse("this is a method to test unit test\nTEST")) == Docstring(short_description='this is a method to test unit test', long_description='TEST', meta=[])

# Generated at 2022-06-13 19:49:04.273047
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    a_function_docstring = '''
    Short description.

    Long description.
    '''

    another_function_docstring = '''
    Short description.

    Long description.

    Parameters
    ----------
    arg
        The first argument.
    arg2 : str
        A second argument.
    'Another Section'
        With a title that is invalid Python.

    Raises
    ------
    ValueError
        The first exception type.
    '''

    function_docstring_without_params = '''
    Short description.

    Long description.
    '''

    def _read_docstring(function):
        return inspect.cleandoc(inspect.getdoc(function))


# Generated at 2022-06-13 19:49:19.319542
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Short description.

    Long description.

    Parameters
    ----------
    param_1
        Description of param_1
    param_2 : type, optional
        Description of param_2

    Raises
    ------
    KeyError
        When a key error
        is encountered.
    NameError
        When a name error
        is encountered.

    References
    ----------
    https://docs.python.org/3/library/functions.html#type
    """

    docstring = NumpydocParser().parse(text)

    assert docstring.short_description == "Short description."
    assert docstring.long_description == "Long description."

    assert len(docstring.meta) == 4
    assert docstring.meta[0].args[0] == "param"

# Generated at 2022-06-13 19:49:30.105326
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = '''
    This is a long description.  The first line
    is uninteresting.  The rest of the first paragraph is uninteresting.

    The second line of the first paragraph contains a list:

        - this
        - is
        - uninteresting

    The third paragraph also contains a list:

        1. this
        2. is
        3. uninteresting

    :Parameters:
    s: str
        This is a parameter

    :Returns:
        A dict with a single key, 's', mapped to the value passed
        to ``s``.

    '''

    doc = parser.parse(text)
    assert len(doc.meta) == 2
    assert doc.meta[0].description == "A dict with a single key, 's', mapped to the value passed to ``s``."


# Generated at 2022-06-13 19:49:40.977155
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from . import parse_docstring
    from .tests.fixtures.numpydoc import *

    assert parse_docstring(SYSTEM_FUNCTION) == NUMPYDOC_SYSTEM_FUNCTION
    assert parse_docstring(CLASS_WITH_METHODS) == NUMPYDOC_CLASS_WITH_METHODS
    assert parse_docstring(CLASS_WITH_METHODS) == NUMPYDOC_CLASS_WITH_METHODS
    assert (
        parse_docstring(CLASS_WITH_METHODS_AND_STATICMETHOD)
        == NUMPYDOC_CLASS_WITH_METHODS_AND_STATICMETHOD
    )

# Generated at 2022-06-13 19:49:54.897267
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This method returns the length of bitstring in bits.

    Parameters
    ----------
    b : Bitstring
    key : str, optional
        A keyword argument.

    Returns
    -------
    int
        The length of the bitstring.
    """
    parsed = NumpydocParser().parse(text)

# Generated at 2022-06-13 19:50:03.552026
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    
    
    
    A short description.
    
    Long description.
    
    Parameters
    ----------
    
    arg_name : type
        arg_desc
    
    arg2_name : type
        arg2_desc
        
    arg3_name : type, optional
        arg3_desc
        
    arg4_name : type(optional)
        arg4_desc
    
    Returns
    -------
    
    return_name : type
        return_desc
        
    See Also
    --------
    
    description
    """
    docstring = NumpydocParser().parse(text)
    assert docstring.short_description == "A short description."
    assert docstring.blank_after_short_description == True
    assert docstring.long_description == "Long description."
   

# Generated at 2022-06-13 19:50:08.968098
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring_raises_example = """
    docstring_raises_example
    ========================
    :param str name: Name to lookup.
    :returns: The number of times that name appears in the
        dictionary.
    :raises KeyError: Raises an exception.

    .. warning::

        This is a test for the method Parse of the class NumpydocParser.
    """
    NumpydocParser().parse(docstring_raises_example)
    assert True

# Generated at 2022-06-13 19:50:15.614613
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .common import Docstring
    from .numpydoc import NumpydocParser
    from .numpydoc import parse
    
    v1 = "DocstringParser." + "parse"
    v2 = "DocstringParser().parse"
    my_parser = NumpydocParser()
    

# Generated at 2022-06-13 19:50:27.991005
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring_1 = """
    Test

    Parameters
    ----------
    param1 : str
        Explanation 1

    other_param : str
        Explanation 2

    Returns
        str
            Explanation 3

    Warnings
        Explanation 4

    """
    docstring_2 = """
    Test

    Parameters
    ----------
    param1 : str
        Explanation 1

    Raises
    ------
    ValueError
        Explanation 2

    """

    docstring_3 = """
    Test

    Parameters
    ----------
    param1 : str, optional
        Explanation 1
        With default 'a'

    Raises
    ------
    ValueError
        Explanation 2

    """


# Generated at 2022-06-13 19:50:39.398796
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = '''Compute the log-likelihood of a Hessian.

The function returns the log-likelihood of the Hessian (the negative of
the Hessian log-determinant). The Hessian is assumed to be constant in
space.

Parameters
----------
H : array_like [shape (dim, dim)]
    A symmetric positive definite matrix

Returns
-------
loglike : float
    The log-likelihood of the Hessian H
'''

# Generated at 2022-06-13 19:50:44.728906
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    assert parser.parse('toto') == Docstring()
    assert parser.parse('toto\nparameters\n   tata\n') == Docstring()
    assert parser.parse('toto\nparameters\n   tata\ntutu') == Docstring()


# Generated at 2022-06-13 19:50:55.555005
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    str_parsed = """Parse the numpy-style docstring into its components.
    :returns: parsed docstring
    """
    ret = parse(str_parsed)
    assert(ret.short_description == "Parse the numpy-style docstring into its components.")
    assert(ret.meta[0].description == "parsed docstring")

# Generated at 2022-06-13 19:51:08.173634
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """method::

    my_method(arg1 : str) -> None
        Args:
            arg1: Parameter description

        Returns:
            None
"""

    d = NumpydocParser().parse(docstring)
    print(d.meta)

    r = Docstring()
    r.short_description = "method"
    r.meta = [
        DocstringMeta(["other_param", "arg1"], description="Parameter description", arg_name="arg1", type_name="str"),
        DocstringReturns(args=["returns"], description=None, type_name=None, is_generator=False)
    ]
    r.blank_after_long_description = False
    r.blank_after_short_description = True
    
    assert r == NumpydocParser().parse(docstring)

# Generated at 2022-06-13 19:51:14.170381
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    Test method parse of class NumpydocParser
    """
    ndParser = NumpydocParser()
    # Simple test
    try:
        text = """One line description.

        More details.
        """
    except:
        print("Unsuccesful test case of class NumpydocParser: method 'parse'")
        return 
    else:
        print("Succesful test case of class NumpydocParser: method 'parse'")
        return 





# Generated at 2022-06-13 19:51:24.009493
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    text = """

    This is the short description.
    This is the long description.

    Parameters
    ----------
    arg: str
        The first argument.
    arg2: int, optional
        The second argument (default is 2).

    Returns
    ------
    A value.
    """

    # Clean according to PEP-0257
    text = inspect.cleandoc(text)

    # Find first title and split on its position
    match = self.titles_re.search(text)
    if match:
        desc_chunk = text[: match.start()]
        meta_chunk = text[match.start() :]
    else:
        desc_chunk = text
        meta_chunk = ""

    # Break description into short and long parts