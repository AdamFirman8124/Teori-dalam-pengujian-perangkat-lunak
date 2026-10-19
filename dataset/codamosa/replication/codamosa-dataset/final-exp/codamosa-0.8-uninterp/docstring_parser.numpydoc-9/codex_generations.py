

# Generated at 2022-06-13 19:41:54.596029
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = """
    this is a test of parse method in class NumpyDocParser.
    it was written to verify the correct implimentation of
    a numpydoc-style docstring.

    Parameters
    ----------
    param_1 : type, optional
    param_2
    """
    doc_string = parser.parse(text)

    assert len(doc_string.meta) == 2
    assert doc_string.meta[0].args[0] == 'param'
    assert doc_string.meta[0].args[1] == 'param_1'
    assert doc_string.meta[1].args[0] == 'param'
    assert doc_string.meta[1].args[1] == 'param_2'

# Generated at 2022-06-13 19:42:04.594097
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    d1 = parser.parse("""
Short description.

    Long description.
    Ignores blank lines, but includes others.
    """)

    assert d1.short_description == "Short description."
    assert d1.long_description == "Long description.\nIgnores blank lines, but includes others."
    assert d1.blank_after_short_description == True
    assert d1.blank_after_long_description == False

    d2 = parser.parse("""
Short description.

    Long description.

    Ignores blank lines, but includes others if non-whitespace.
    """)

    assert d2.short_description == "Short description."
    assert d2.long_description == "Long description.\n\nIgnores blank lines, but includes others if non-whitespace."

# Generated at 2022-06-13 19:42:12.780433
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    sample = '''
    Parameters
    ----------
    a : type
        description
    b : type
        description

    Raises
    -------
    ValueError
        description
    '''


# Generated at 2022-06-13 19:42:25.664095
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:42:35.237489
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
       This is a summary
       lines.

       This is a description of the function. It spans several lines.

       Parameters
       ----------
       arg : int
           argument description.

       arg2 : type
           argument description.

       arg3 : type, optional
           argument description.

       Raises
       ------
       ValueError
           if `arg` is invalid.
       """
    doc = parse(text)
    assert doc.long_description == "This is a description of the function. It spans several lines."
    assert doc.short_description == "This is a summary lines."
    assert len(doc.meta) == 2

    assert len(doc.meta[0]) == 3
    assert doc.meta[0][0].type == "parameter"
    assert doc.meta[0][0].arg_name == "arg"

# Generated at 2022-06-13 19:42:44.868142
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert parse(
        """Short description
        Over multiple lines.
        """
    ) == Docstring(
        short_description="Short description",
        long_description="Over multiple lines.",
    )

    assert parse(
        """Short description
        Over multiple lines.
        
        """
    ) == Docstring(
        short_description="Short description",
        long_description="Over multiple lines.",
        blank_after_long_description=True,
    )

    assert parse(
        'Short description\nwith no trailing newline\n'
    ) == Docstring(short_description='Short description\nwith no trailing newline')


# Generated at 2022-06-13 19:42:49.180042
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = '''
    Parameters
    ----------
    other : array_like
    '''
    parsed_docstring = parser.parse(docstring)
    assert parsed_docstring.meta[0].key == ['param']


if __name__ == "__main__":
    test_NumpydocParser_parse()

# Generated at 2022-06-13 19:42:59.461013
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    def function(arg1, arg2=None, *, kw1, kw2=2, **kwargs):
        """Function docstring

        This function is used to test the parse method of class
        NumpydocParser.

        Parameters
        ----------
        arg1 : type
            description of arg1
        arg2, optional : type
            description of keyword argument arg2
        kw1 : type
            description of keyword argument kw1
        kw2 : type, optional
            description of keyword argument kw2

        Returns
        -------
        ret_1 : type
            description
        ret_2 : type
            description

        Raises
        ------
        ValueError
            If something goes wrong
        """
        pass

    docstring = parse(function.__doc__)


# Generated at 2022-06-13 19:43:08.020795
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_string = """\
    This is a function

    Parameters
    ----------
    A : type(s)
        First param to the function
    DoesOtherThings : bool
        DoesOtherThings param of the function

    Returns
    -------
    ThisIsReturned : type
        This is what is returned

    Raises
    ------
    None

    Warns
    -----
    None

    Warnings
    --------
    None
    """
    assert NumpydocParser().parse(test_string)


# Generated at 2022-06-13 19:43:17.163995
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Test of NumpyDocParser.parse()
    Parameters
    ----------
    test : type, optional
        This is a test of the Parameters section methods
    Raises
    ------
    NotImplementedError
        This is a test of the Raises section method
    Returns
    -------
    None
        This is a test of the Returns section method
    """
    d = NumpydocParser().parse(text)
    assert d.short_description == "Test of NumpyDocParser.parse()"

# Generated at 2022-06-13 19:43:24.203673
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    title = 'Example'
    text = 'Hello'
    p = NumpydocParser()
    p.parse(text)
    p.add_section(Section(title, 'examples'))
    p.parse(text)

# Generated at 2022-06-13 19:43:26.796184
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Unit test for method parse of class NumpydocParser."""
    from .test_common import _test_parse_docs
    _test_parse_docs(parse)



# Generated at 2022-06-13 19:43:39.967136
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    ex = '''    Compute the mean and std deviation on a moving window.
    The moving window size is *winsize*, and the output arrays are
    of size *(len(x) - winsize + 1)*.

    Parameters
    ----------
    x : array_like
        Input array.
    axis : int, optional
        The axis along which the moving average is computed.
        By default, the moving average is computed along the last
        axis of the input array.
    params : Parameter, optional
        A Parameter instance, returned by a `Parameters` class
    Returns
    -------
    y : array_like
        The mean of the data in the moving window.
    w : array_like
        The standard deviation of the data in the moving window.
    '''
    res = parser.parse

# Generated at 2022-06-13 19:43:44.789355
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:43:50.287108
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from pydocstring.utils import read_contents
    text = read_contents('test_examples/numpy_example.txt')
    doc = NumpydocParser().parse(text)

    assert doc.short_description.startswith("Example:")
    assert doc.short_description.endswith("?>")
    assert doc.blank_after_short_description
    assert doc.long_description is None
    assert not doc.blank_after_long_description
    assert len(doc.meta) == 9
    assert doc.meta[0] == DocstringMeta(['param', 'param'], 'short param description')
    assert doc.meta[1] == DocstringMeta(['param', 'param2'], 'long param description\n    Covers multiple lines')
    assert doc.meta[2] == DocstringMeta

# Generated at 2022-06-13 19:43:58.112789
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_cases = [
        "",
        "Single line docstring",
        "multi\nline\ndocstring\n",
        (
            "Single line docstring\n"
            "======================\n"
            "multiline docstring\n"
            ".. parameter:: param1\n"
            "    multiline parameter definition 1\n"
            ".. parameter:: param2\n"
            "    multiline parameter definition 2\n"
            "\n"
            ".. warning:: this is a warning"
        ),
    ]


# Generated at 2022-06-13 19:44:04.238337
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc_str = """\
    Short description.

    Longer description.

    Parameters
    ----------
    arg1 : str
        Description of arg1

    arg2 : int, optional
        Description of arg2

    arg3: list
        Description of arg3

    arg4 : str
        Description of arg4
    """
    parsed_result = parse(doc_str)
    return parsed_result

# Generated at 2022-06-13 19:44:09.619716
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    m = NumpydocParser()
    text = """
    hey

    this is a docstring

    Parameters
    ----------
    name : type
        some description
    """

    docstring = m.parse(text)
    assert(docstring.short_description == "hey")
    assert(docstring.long_description == "this is a docstring")
    assert(len(docstring.meta) == 1)
    assert(docstring.meta[0].description == "some description")

# Generated at 2022-06-13 19:44:17.847344
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:31.664620
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This is a test for method parse

    Parameters
    ----------
    text : str
        This is a parameter

    Returns
    -------
    Docstring
        This is a return value

    Examples
    --------
    This is an example

    Warnings
    --------
    This is a warning

    See Also
    --------
    None

    Notes
    -----
    This is a note
    """
    actual = NumpydocParser().parse(text)
    assert actual.short_description == 'This is a test for method parse'
    assert actual.long_description == 'This is a test for method parse'
    assert actual.blank_after_short_description is True
    assert actual.blank_after_long_description is True
    
    assert actual.meta[0].args == ['param', 'text']
    assert actual

# Generated at 2022-06-13 19:44:44.577585
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    Test case 1:
    Input -
        """

# Generated at 2022-06-13 19:44:53.831783
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert parse('first line\n\n    second line') == \
        Docstring(
            short_description='first line',
            long_description='second line',
            meta=[],
            blank_after_long_description=True,
            blank_after_short_description=True)
    assert parse('first line\n\n.. deprecated:: testing') == \
        Docstring(
            short_description='first line',
            long_description=None,
            meta=[DocstringDeprecated(
                args=['deprecation'],
                description=None,
                version='testing')],
            blank_after_long_description=False,
            blank_after_short_description=True)

# Generated at 2022-06-13 19:45:03.212376
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
        One line summary.

        Long description.

        Parameters
        ----------
        param1 : str
            First parameter
        param2
            Second parameter

        Raises
        ------
        ValueError
            Something went wrong
        AssertionError
            Something else went wrong

        Returns
        -------
        int
            The number of items

        Yields
        ------
        str
            An item

        Examples
        --------
        >>> one
        1
        >>> two
        2
        >>> three
        3

        Warnings
        --------
        No warnings.

        References
        ----------
        [0] https://example.org
    '''

# Generated at 2022-06-13 19:45:10.744123
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
            Compute the absolute value element-wise.

            This function only supports inputs that

            Parameters
            ----------
            input : array_like
                Input array.

            Returns
            -------
            absolute : ndarray
                Result.
            """
    print(list(NumpydocParser().parse(text).meta))
    # TODO: assert results


if __name__ == "__main__":
    # TODO: Add test suite
    test_NumpydocParser_parse()

# Generated at 2022-06-13 19:45:18.952303
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """\
    This is the short description.

    This is the long description.

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    str
        The return value.
    """

    result = NumpydocParser().parse(text)

    assert result.short_description == "This is the short description."
    assert result.long_description == "This is the long description."
    assert result.meta[0] == DocstringMeta(["param", "param1"], description="The first parameter.", arg_name="param1", type_name="int", is_optional=False, default=None)

# Generated at 2022-06-13 19:45:28.890049
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .common import Docstring
    from .common import DocstringParam
    from .common import DocstringReturns
    from .common import DocstringRaises
    from .common import DocstringDeprecated
    from .common import DocstringMeta

    numpydoc_parser = NumpydocParser()
    result = numpydoc_parser.parse(
        """
        This is some function.

        Its docstring is
        multi-line
        and contains a parameter and a return value.

        Parameters
        ----------
        arg : argtype
            This is the argument.

        Returns
        -------
        rettype
            This is the return value.

        Warns
        -----
        UserWarning
            If you do something wrong.
        """
    )

# Generated at 2022-06-13 19:45:30.753775
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert NumpydocParser().parse("\n") == Docstring()
    assert NumpydocParser().parse("") == Docstring()



# Generated at 2022-06-13 19:45:42.156109
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # test short and long description
    tc = '''short desc
        long desc'''
    d = NumpydocParser().parse(tc)
    assert d.short_description == 'short desc'
    assert d.long_description == 'long desc'
    assert d.blank_after_short_description == False
    assert d.blank_after_long_description == False

    tc = '''short desc
        long desc
    '''
    d = NumpydocParser().parse(tc)
    assert d.short_description == 'short desc'
    assert d.long_description == 'long desc'
    assert d.blank_after_short_description == True
    assert d.blank_after_long_description == False

    tc = '''short desc\n        long desc\n    '''
    d = Numpydoc

# Generated at 2022-06-13 19:45:48.180653
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert dict(parse('\n    Return a\n    -------\n    r: int\n        a + b\n').meta[0]) == {
        'args': ['returns'],
        'return_name': None,
        'type_name': 'int',
        'is_generator': False,
        'description': 'a + b',
    }


# Generated at 2022-06-13 19:45:59.750813
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser=NumpydocParser()

# Generated at 2022-06-13 19:46:07.956794
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print("Start test_NumpydocParser_parse")
    parser = NumpydocParser()
    ret = parser.parse("")
    assert ret == Docstring()

    ret = parser.parse("Single line.")
    assert ret.short_description == "Single line."
    assert ret.blank_after_short_description == False
    assert ret.long_description == None
    assert ret.blank_after_long_description == True
    assert ret.meta == []

    ret = parser.parse("Single line.\n")
    assert ret.short_description == "Single line."
    assert ret.blank_after_short_description == True
    assert ret.long_description == None
    assert ret.blank_after_long_description == True
    assert ret.meta == []

    ret = parser.parse("\nSingle line.")
   

# Generated at 2022-06-13 19:46:17.143635
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    
    def f(a, b, c=0):
        """This is a test function
        
        Parameters
        ----------
        a : int
            This is a
        b : str
            This is b
        c : int, optional
            This is c  
            
        Returns
        -------
        float
            This is the return value
            
        Notes
        -----
        This is a note
        
        Examples
        --------
        >>> f(1, '2', 3)
        0.0
        
        """
        return 0.0

    ndp = NumpydocParser()

    docstring = ndp.parse(f.__doc__)

    # check the short and long descriptions
    assert docstring.short_description == "This is a test function"

# Generated at 2022-06-13 19:46:28.778184
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:46:38.599086
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """
    A docstring.

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

    Raises
    ------
    ValueError
        A description of what might raise ValueError
    """

    parser = NumpydocParser()
    doc = parser.parse(docstring)

    assert doc.short_description == "A docstring."
    assert doc.long_description is None
    assert doc.blank_after_short_description is True
    assert doc.blank_after_long_description is True

    assert len(doc.meta) == 7


# Generated at 2022-06-13 19:46:47.033496
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .common import Docstring
    from .numpydoc import NumpydocParser

    first_docstring = Docstring()
    first_docstring.short_description = 'First line of docstring.'
    first_docstring.long_description = (
        'Longer description, which can contain\n'
        'multiple paragraphs.\n' +
        '\n' +
        'Args:\n' +
        '    param1: The first parameter.\n' +
        '    param2: The second parameter.\n'
    )
    first_docstring.blank_after_short_description = True
    first_docstring.blank_after_long_description = False

# Generated at 2022-06-13 19:46:58.886846
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    class TestClass:
        """
        This is a test class.

        Parameters
        ----------
        arg1 : str
            This is a test argument
        arg2 : int
            This is a test argument

        Returns
        -------
        str
            A string.
        float
            A float.

        Examples
        --------
        >>> TestClass('test1', 1)
        TestClass(arg1='test1', arg2=1)
        """

        def __init__(self):
            pass


# Generated at 2022-06-13 19:47:11.998682
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    # example docstring
    docstring = """
    This is some docstring.

    Parameters
    ----------
    param1
        This is the first param

    param2 : string, optional
        This is the second param. It defaults to None
    """

    doc = parser.parse(docstring)

    assert len(doc.meta) == 2
    assert isinstance(doc.meta[0], DocstringParam)
    assert doc.meta[0].arg_name == 'param1'
    assert doc.meta[0].type_name is None
    assert doc.meta[0].default is None
    assert doc.meta[1].arg_name == 'param2'
    assert doc.meta[1].type_name == 'string'
    assert doc.meta[1].default == 'None'


# Generated at 2022-06-13 19:47:18.540059
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert len(parse("hello world").meta) == 0
    assert parse("hello world\n").long_description is None
    assert parse("\nhello world").short_description is None
    assert parse("hello world\n\n").short_description == "hello world"
    assert parse("hello world\n\n").long_description == ""
    assert parse("hello world\n\n").long_description is not None
    assert parse("hello world\n\n").long_description != "hello world"
    assert len(parse("hello world\n\n\n").meta) == 0
    assert parse("hello world\n\n\n").short_description == "hello world"
    assert parse("hello world\n\n\n").long_description == ""
    assert parse("hello world\n\n\n").long_description is not None

# Generated at 2022-06-13 19:47:24.668297
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:47:31.714191
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    instance = NumpydocParser()
    text = '''
    Parse the numpy-style docstring into its components.

    Returns
    -------
    parsed docstring
    '''
    result = instance.parse(text)
    assert(result.short_description == 'Parse the numpy-style docstring into its components.')
    assert(result.long_description == None)
    assert(result.blank_after_short_description == True)
    assert(result.blank_after_long_description == False)
    assert(result.meta[0] == DocstringMeta(['returns'], description=None))

# Generated at 2022-06-13 19:47:45.961635
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    def foo(a, b, c=None):
        """
        short desc

        long desc

        Parameters
        ----------
        a : type
            desc
        b : param b
            desc
        c : (optional), default 'foobar'
            desc

        Raises
        ------
        ValueError
            if an invalid value was found

        Return
        ------
        x : int
            The return value.

        Notes
        -----
        .. note:: This is a note in a note section.

        This is an ordinary paragraph.

        References
        ----------
        See Also
        --------
        otherfunc : related function

        Examples
        --------
        Examples should be written in doctest format, and should illustrate how
        to use the function/class.
        >>> x = foo(1)
        """
        pass


# Generated at 2022-06-13 19:47:57.351816
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Test Parsing of "Example" and "Example"
    test_str = """
    A test example:

    Examples
    --------
    >>> import test
    >>> test.parse()
    >>> 1+1
    2
    """
    expected_result = Docstring()
    expected_result.short_description = 'A test example:'
    expected_result.blank_after_short_description = True
    expected_result.blank_after_long_description = False

    # Expected result of parsing long description
    long_desc = DocstringMeta(['examples'],
        description='>>> import test\n>>> test.parse()\n>>> 1+1\n2')
    expected_result.long_description = [long_desc]

    # Test that actual result of parsing matches expected result

# Generated at 2022-06-13 19:48:10.143053
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:48:16.579787
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text="""This function provides a convenient way to generate a continuous
    random variable in a specified range.

Parameters
----------
value : numeric
    Value (or array of values) to be appended to `rvs`.

Returns
-------
rvs : ndarray
    Array containing the appended elements.

Notes
-----
This is an example !

Examples
--------

Raises
------
"""
    assert NumpydocParser().parse(text)



# Generated at 2022-06-13 19:48:32.987590
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:48:43.662068
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    s = '''
    Calculate the absolute value of the argument.

    Parameters
    ----------
    x : array
        Values whose absolute values are returned

    Returns
    -------
    float
        Result

    '''
    assert NumpydocParser().parse(s).short_description == 'Calculate the absolute value of the argument.'
    s = '''
    Calculate the absolute value of the argument.\n
    Parameters
    ----------
    x : array
        Values whose absolute values are returned

    Returns
    -------
    float
        Result

    '''
    assert NumpydocParser().parse(s).short_description == 'Calculate the absolute value of the argument.'

# Generated at 2022-06-13 19:48:53.772892
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    parser = NumpydocParser()

    text = """\
    A summary line.

    The following paragraphs are a long description. It can be
    some paragraphs long.

    Parameters
    ----------
    arg1 : type
        Description of `arg1`.

    arg2 : {'type'}, optional
        Description of `arg2`. (default: 'type')

    Raises
    ------
    ValueError
        Description of `ValueError`.
    """

    actual = parser.parse(text)

# Generated at 2022-06-13 19:49:04.178306
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # reference: https://numpydoc.readthedocs.io/en/latest/format.html
    text = """
    This is a summary
    This is a long description
    
    Parameters
    ----------
    x : int
        This is the first parameter
    y : str
        This is the second parameter
    
    Returns
    -------
    tuple
        This is the return value
    
    Raises
    ------
    ValueError
        When something wrong happens
    """
    ret = NumpydocParser().parse(text)
    assert ret.short_description == "This is a summary"
    assert ret.long_description == "This is a long description"
    assert ret.blank_after_short_description
    assert ret.blank_after_long_description
    assert len(ret.meta) == 3
   

# Generated at 2022-06-13 19:49:12.253765
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:49:21.480089
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    metadata = {
        'short_description': 'Test paragraph',
        'long_description': 'Returns the number',
        'blank_after_short_description': False,
        'blank_after_long_description': False,
        'meta': [
            DocstringMeta(['param'], 'a', "The first parameter"),
            DocstringMeta(['param'], 'b', "The second parameter"),
            DocstringMeta(['returns'], None, "The type of the returned object"),
            DocstringMeta(['examples'], None, '>>> func(1, 2)\\n3\\n>>> func(4, 5)\\n9')
        ]
    }


# Generated at 2022-06-13 19:49:33.531685
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
    Add a doctest
    --------------

    .. doctest::

        >>> np.add(1, 2)
        3
        >>> np.add(np.arange(3), np.arange(3))
        array([0, 2, 4])


    '''

    expected_short_desc = "Add a doctest"
    expected_blank_after_short_desc = True
    expected_blank_after_long_desc = False
    expected_long_desc = ".. doctest::\n    >>> np.add(1, 2)\n    3\n    >>> np.add(np.arange(3), np.arange(3))\n    array([0, 2, 4])"

# Generated at 2022-06-13 19:49:46.035093
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    text = inspect.cleandoc("""\
        Short description.

        Parameters
        ----------
        arg1
            Argument 1 description.

        arg2
            Argument 2 description.

        Returns
        -------
        return_value
            Return value description.

        Raises
        ------
        ValueError
            If something goes wrong.

        See Also
        --------
        func3
        func4

        Notes
        -----
        Some notes or references.
        """)

    docstring = parser.parse(text)

    assert docstring.short_description == "Short description."


# Generated at 2022-06-13 19:49:58.072023
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    def func(i0:float, i1:float=1.0, *args, i2, **kwargs):
        """This is a test function 'func'.

        Parameters
        ----------
        i0 : float
            This is a required float
        i1 : float, optional
            This is an optional float, with a default
        i2 : int
            This is a named keyword argument
        args : tuple
            This is a tuple argument
        kwags : dict
            This is a dict argument
        """

    # Test correct function
    func_sig = inspect.signature(func)
    func_doc = inspect.getdoc(func)
    result = NumpydocParser().parse(func_doc)
    assert result.short_description
    assert result.long_description
    assert result.blank_after_short_description


# Generated at 2022-06-13 19:50:08.225423
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """
    A function that can be called.

    :param param1: This is a first parameter
    :param param2: This is a second parameter
    :returns: This is a description of what is returned
    :raises keyError: We get a keyerror
    """
    output = NumpydocParser().parse(docstring)

# Generated at 2022-06-13 19:50:13.438611
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert parse(
        """
        Parameters:
            param1 : int
                The first parameter.
            param2 : str
                The second parameter.

        Raises:
            ValueError
                If `param2` is equal to ''.
        """
    ) == Docstring(
        """
        Parameters:
            param1 : int
                The first parameter.
            param2 : str
                The second parameter.

        Raises:
            ValueError
                If `param2` is equal to ''.
        """
    )


# Generated at 2022-06-13 19:50:26.166088
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydoc_parser = NumpydocParser()
    docstring = numpydoc_parser.parse(text=x)
    assert docstring.short_description == "Test"
    assert docstring.long_description == "Test \nlong \ndescription"
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == True
    assert len(docstring.meta) == 6
    assert docstring.meta[0][0] == "param"
    assert docstring.meta[0][1] == "a"
    assert docstring.meta[0][2] == None
    assert docstring.meta[0][3] == None
    assert docstring.meta[0][4] == None
    assert docstring.meta[0].description == "test a"

# Generated at 2022-06-13 19:50:34.275624
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = """
    simple docstring

    Parameters
    ----------
    x : int, optional
        The first arg, defaults to 1.

    y : float
        The second arg.

    z : str, optional
        The third arg, defaults to 'foo'.

    Returns
    -------
    int:
        The return value.

    """
    docstring = parser.parse(docstring)
    print(docstring.meta.param_meta)
    print(docstring.meta.returns_meta)


if __name__ == "__main__":
    from .docstring_parser import DocstringParser
    from docstring_parser.common import Docstring
    import os
    import json

    path = os.path.dirname(__file__)

# Generated at 2022-06-13 19:50:46.784265
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    text = """
    This is the documentation for the function foo.
    Parameters
    ----------
    x : int
        Version number.
    y : int
        Description that spans multiple lines
    Returns
    -------
    out : int
        Description here.
    """

    docstring = NumpydocParser().parse(text)
    assert docstring.short_description == "This is the documentation for the function foo."
    assert (
        docstring.long_description == "Parameters\n----------\nx : int\n    Version number.\ny : int\n    Description that spans multiple lines\nReturns\n-------\nout : int\n    Description here."
    )
    assert docstring.meta[0].args == ["param", "x"]
    assert docstring.meta[0].description == "Version number."

# Generated at 2022-06-13 19:50:56.389687
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    .. title:: Clase NumpydocParser
        This is a longer description.
        It can span several lines.

        This is another paragraph.
        See also :ref:`kittens`.
    .. note::
        This is a note
    .. seealso::
        This is a seealso
    .. deprecated:: 1.0.0
        This is a deprecation
    """
    expected = Docstring()
    expected.short_description = "Clase NumpydocParser"
    expected.long_description = """This is a longer description.
It can span several lines.

This is another paragraph.
See also kittens.
"""
    expected.blank_after_short_description = True
    expected.blank_after_long_description = False

# Generated at 2022-06-13 19:51:11.372884
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    Test for method parse of class NumpydocParser.

    :returns: True if success, False otherwise
    """
    parser = NumpydocParser()
    docstring_text = """
    This is a short description.

    This is a long description.

    Parameters
    ----------
    arg1 : str
        Description of `arg1` goes here.
    arg2: bool, optional
        Description of `arg2` goes here.
        Default is `False`.
    arg3
        Description of `arg3` goes here.
    arg4 : complex
        Description of `arg4`  goes here.
    other_param
        Description of `other_param` goes here.

    Returns
    -------
    bool
        Description of the return value.
    """
    docstring = parser.parse(docstring_text)