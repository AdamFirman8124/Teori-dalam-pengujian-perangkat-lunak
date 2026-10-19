

# Generated at 2022-06-13 19:42:10.875952
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    sample = """
    one line summary
    multiple line summary
    see also keywords
    x
    y
    z
    Parameters
    ----------
    arg_name
        arg_description
    arg_2 : type
        descriptions can also span...
        ... multiple lines

    attributes:
    arg_name
        arg_description
    arg_2 : type
        descriptions can also span...
        ... multiple lines
    """
    parsed = NumpydocParser().parse(sample)
    assert parsed.short_description == "one line summary"
    assert parsed.long_description == "multiple line summary\nsee also keywords\nx\ny\nz"
    assert parsed.blank_after_short_description
    assert not parsed.blank_after_long_description
    assert len(parsed.meta) == 2

    meta = parsed.meta

# Generated at 2022-06-13 19:42:24.725986
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .numpydoc import parse
    from .common import Docstring, DocstringParam, DocstringRaises
    from .sphinx import SphinxParser
    import pprint


# Generated at 2022-06-13 19:42:29.529675
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    def func_1(param1, param2, param3 = None):
        """Test function with simple docstring"""

        return param1, param2, param3

    parser = NumpydocParser()
    print(parser.parse(text=inspect.getdoc(func_1)).meta)

test_NumpydocParser_parse()

# Generated at 2022-06-13 19:42:38.049812
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .base import BaseParser
    from .google import GoogleParser
    from .numpydoc import NumpydocParser
    from .sphinx import SphinxParser

    my_text_1 = """
        This is a sentence.

        This is another sentence.

        Args:
            arg_1 (str): Description of `arg_1`. Default is 'arg_1'.
            arg_2 (int): Description of `arg_2`. Default is 42.

        Returns:
            str: Description of return value.
        """

    my_text_2 = """
        This is a sentence.

        This is another sentence.
        """


# Generated at 2022-06-13 19:42:43.433788
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    text = """.. deprecated:: 01
        .. deprecated version
    """
    section = DeprecationSection("deprecated", "deprecated")
    docstring_meta_list = list(section.parse(text))
    assert docstring_meta_list[0].args == ["deprecated"]
    assert docstring_meta_list[0].description == "01"
    assert docstring_meta_list[0].version is None


# Generated at 2022-06-13 19:42:50.681156
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:43:00.786525
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """A long summary which can be over multiple lines.

Parameters
----------
arg1 : int
    The first argument
arg2 : str, optional
    The second argument

Raises
------
ValueError
    If ``arg2`` is supplied but not ``arg1``

Returns
-------
None"""
    docstring = NumpydocParser().parse(text)
    assert docstring.short_description == 'A long summary which can be over multiple lines.'
    assert docstring.long_description == 'The first argument\n    The second argument'
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False
    assert docstring.meta[0].description == 'The first argument'
    assert docstring.meta[1].description == 'The second argument'
    assert docstring

# Generated at 2022-06-13 19:43:12.748320
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    text = ".. deprecated:: 0.1"
    doc = DeprecationSection("deprecated", "deprecation")
    ds = doc.parse(text)
    assert next(ds) == DocstringDeprecated(args=['deprecation'], description=None, version='0.1')

    text = ".. deprecated:: 0.1\n    obsoleted by some other function."
    doc = DeprecationSection("deprecated", "deprecation")
    ds = doc.parse(text)
    assert next(ds) == DocstringDeprecated(args=['deprecation'], description='obsoleted by some other function.', version='0.1')

    text = ".. deprecated:: 0.1\n    obsoleted by some other function.\n    "

# Generated at 2022-06-13 19:43:19.266008
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    print('NumpydocParser')
    text = 'deprecated since version 1.1.1: Use :obj:`~numpydoc.Docscraper.prepare_docstring` instead.'
    d = NumpydocParser()
    assert d.parse(text).meta[0].description == 'Use :obj:`~numpydoc.Docscraper.prepare_docstring` instead.'
    assert d.parse(text).meta[0].version == '1.1.1'

# Generated at 2022-06-13 19:43:27.877068
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    s = 'Deprecated since version 0.9: This class is deprecated and will be '\
        'removed in 0.11, use `aiohttp.ClientSession` instead.'
    section = DeprecationSection("deprecated", "deprecation")
    doc = section.parse(s)
    doc = list(doc)
    assert doc[0].description == "This class is deprecated and will be " \
                                 "removed in 0.11, use `aiohttp.ClientSession` instead."
    assert doc[0].version == "0.9"
    assert doc[0].args[0] == "deprecation"

# Generated at 2022-06-13 19:43:38.741626
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    ns = NumpydocParser()
    assert type(ns.parse('')) == Docstring
    assert type(ns.parse('a')) == Docstring
    assert type(ns.parse('a\nb')) == Docstring

# Generated at 2022-06-13 19:43:46.713462
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """
    Function that parses correctly.

    Raises
    ------
    SyntaxError
        If you write something wrong
        in the numpydoc.

    Returns
    -------
    int
        The number of rows

    See Also
    --------
    astropy.io.ascii.read_csv
        Since this is essentially
        a wrapper for this.
    """
    docstring2 = """
    Function that parses correctly.

    Parameters
    ----------
    arg : int
        Argument that makes sense
    """

    class Test:
        """Class that is used for testing."""
        def test_func(self, test_arg1: int, test_arg2: str) -> str:
            """Testing parsing."""
            return test_arg2

    parser = NumpydocParser()
    assert parser

# Generated at 2022-06-13 19:43:57.383767
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:07.657159
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = parser.parse(
        """Calculate mean of data which is not missing.

    Parameters
    ----------
    data : array_like
        Input data.
    axis : int
        Axis along which mean are computed.
    skipna : boolean, optional
        Exclude missing values (True).
    level : int or None
        If not None, computes the mean along the given level,
        collapsing it into the new axis.

    Returns
    -------
    mean : ndarray, see dtype parameter above
        Return the mean of the array elements. If `out` is specified,
        `out` is returned. If `out` is not specified, a new array is
        created and returned.
    """
    )

# Generated at 2022-06-13 19:44:15.404958
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    class Test:
        def test_method(self):
            """
            Example signature.

            Some description of this method.

            Parameters
            ----------
            param_1: type
                Some description of param_1.
            param_2: type
                Some description of param_2.

            Returns
            -------
            str
                Some description of the return value.
            """
            pass
    
    docstring = inspect.getdoc(Test.test_method)
    parsed = NumpydocParser().parse(docstring)
    assert parsed.short_description == "Example signature."
    assert parsed.long_description == "Some description of this method."
    assert parsed.meta[0].args == ["param", "param_1"]
    assert parsed.meta[0].description == "Some description of param_1."

# Generated at 2022-06-13 19:44:27.195474
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = '''
    Get the file path of the temporary directory created by the
    tmpdir fixture.

    :returns: path string
    '''
    docstring_parser = NumpydocParser()
    docstring = docstring_parser.parse(docstring)
    assert docstring.short_description == "Get the file path of the temporary directory created by the tmpdir fixture."
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False
    assert docstring.meta[0].description == "path string"
    assert docstring.meta[0].args == ["returns"]


# Generated at 2022-06-13 19:44:35.528609
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:45.684145
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:51.059907
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:58.414495
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:45:16.441006
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .common import Docstring, DocstringMeta, DocstringParam, DocstringReturns
    from numpydoc.docscrape_sphinx import get_doc_object
    doc = get_doc_object(NumpydocParser.parse)

# Generated at 2022-06-13 19:45:27.027420
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    test = "parse the docstring.\n\nParameters\n----------\nflag : bool\n    A bool flag.\n\nReturns\n-------\nint\n    An integer."
    docstring = parser.parse(test)
    assert docstring.short_description == "parse the docstring."
    assert docstring.long_description == "Parameters\n----------\nflag : bool\n    A bool flag.\n\nReturns\n-------\nint\n    An integer."
    assert docstring.meta[0].args == ['param', 'flag']
    assert docstring.meta[0].description == 'A bool flag.'
    assert docstring.meta[1].args == ['returns']
    assert docstring.meta[1].description == 'An integer.'

# Unit test

# Generated at 2022-06-13 19:45:37.395726
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''\
        Short description.

        Parameters
        ----------
        x : int
            The x coordinate.
        y : int
            The y coordinate.

        Returns
        -------
        value : int
            The value at the given coordinates.

        Raises
        ------
        RuntimeError
            If the underlying array is not initialized.
    '''
    actual = NumpydocParser().parse(text)

# Generated at 2022-06-13 19:45:46.290149
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    # Python function docstring

# Generated at 2022-06-13 19:45:53.671679
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import pydocstyle.violations as v


# Generated at 2022-06-13 19:46:03.049950
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This is a short description
    This is a longer description,
    which goes over several lines.

    Parameters
    ----------
    arg_name
        arg_description
    arg_2 : type, optional
        descriptions can also span...
        ... multiple lines
    arg_3 : type, optional
        This is another description
    arg_3 : type
        This is another description

    Returns
    -------
    return_name : type
        A description of this returned value
    another_type
        Return names are optional, types are required
    """
    print(NumpydocParser().parse(text))
    assert(True)

# Generated at 2022-06-13 19:46:14.093218
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Create a few numpydoc-style docstrings for testing.
    docstring_1 = """The first line is short description. \n\nThe next, \n\
is a longer description. It can contain code.\n\n\
Parameters\n---------\nname_1 : str\n    Description of name_1\n\n\
Other Parameters\n--------------\nname_2 : int\n    Description of name_2.\n\
Default is 1.\n\n\
Returns\n-------\nstr\n    Description of return value.\n"""

# Generated at 2022-06-13 19:46:26.718645
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    Test method parse of class NumpydocParser
    """
    numpydocParser = NumpydocParser()
    ret = numpydocParser.parse("")
    print("Test NumpydocParser.parse() 1: OK")
    print("\t ret : ", ret)
    print("\t ret.short_description : ", ret.short_description)
    print("\t ret.long_description : ", ret.long_description)
    print("\t ret.blank_after_short_description : ",
          ret.blank_after_short_description)
    print("\t ret.blank_after_long_description : ",
          ret.blank_after_long_description)
    print("\t ret.meta : ", ret.meta)
    assert ret.short_description == None
    assert ret.long

# Generated at 2022-06-13 19:46:34.400625
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """Summary line.

Extended description.


Parameters
----------
arg1 : int
    Description of arg1
arg2
    Description of arg2

Returns
-------
int
    Description of return value

"""
    docstring = NumpydocParser().parse(docstring)
    assert docstring.short_description == "Summary line."
    assert docstring.long_description == "Extended description."
    assert docstring.meta[0] == DocstringParam(['param', 'arg1'], 'Description of arg1', arg_name='arg1', type_name='int')
    assert docstring.meta[1] == DocstringParam(['param', 'arg2'], 'Description of arg2', arg_name='arg2', type_name=None)

# Generated at 2022-06-13 19:46:44.877268
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''\
    Get the version of a package.
    
    Parameters
    ----------
    distribution : :class:`pkg_resources.Distribution`
        This can be either a path to a local egg file, or a Distribution object as returned by pkg_resources.working_set.find().
    '''

    doc = NumpydocParser().parse(text)

    print(doc.short_description)
    print(doc.long_description)
    print(doc.blank_after_short_description)
    print(doc.blank_after_long_description)

    for i in doc.meta:
        print(i.args, i.description)

if __name__ == '__main__':
    test_NumpydocParser_parse()

# Generated at 2022-06-13 19:47:14.153716
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstringParser = NumpydocParser()
    docstring = inspect.cleandoc("""
        This is a short description
        and a long description.
        Parameters:
            param: type
                description
            param2: type2
                description2
        Returns:
            This is a returntype
            and a returnsdescription
        Warnings:
            This is a warning
        Raises:
            TypeError:
                This is a typeerror
    """)
    docstringObject = docstringParser.parse(docstring)
    assert docstringObject.short_description == "This is a short description"
    assert docstringObject.long_description == "and a long description."
    assert docstringObject.meta[0].args == ['param', None]
    assert docstringObject.meta[1].args == ['param2', None]


# Generated at 2022-06-13 19:47:22.041435
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    text = """
        First line of text

        Second line of text
        """

    expected_short_description = "First line of text"
    expected_long_description = "Second line of text"
    expected_blank_after_short_description = False
    expected_blank_after_long_description = False

    docstring = parser.parse(text)
    assert (
        docstring.short_description == expected_short_description
    ), "function NumpydocParser parse short description is not correct"
    assert (
        docstring.long_description == expected_long_description
    ), "function NumpydocParser parse long description is not correct"

# Generated at 2022-06-13 19:47:28.122497
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc = '''
    Parse the numpy-style docstring into its components.

    This method will parse the docstring text into its component parts.

    Parameters
    ----------
    text : str
        Docstring body text

    Returns
    -------
    Docstring
        Parsed docstring
    '''
    result = NumpydocParser().parse(doc)
    assert result == Docstring()

# Generated at 2022-06-13 19:47:36.698765
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print("Start to test NumpydocParser.parse() ...")
    numpydoc_parser = NumpydocParser()
    docstring = numpydoc_parser.parse(
    """
    Simple example of a docstring.
    Parses into a Docstring namedtuple.
    """
    )
    assert docstring.short_description == "Simple example of a docstring."
    assert docstring.long_description == "Parses into a Docstring namedtuple."
    assert docstring.meta == []
    assert len(docstring.meta) == 0

# Generated at 2022-06-13 19:47:38.926047
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-13 19:47:48.348195
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = """Simple line.

    One paragraph.

    Params
    ------
    arg1
        type
        blabla

    arg2
        type
        blabla

    Yields
    ------
    A
        blabla

    Raises
    ------
    Exception
        blabla

    See Also
    --------
    :func:`test`
    """
    parsed_docstring = parser.parse(text)
    assert isinstance(parsed_docstring, Docstring), "parsed docstring is not a Docstring object"
    assert parsed_docstring.short_description == "Simple line.", "short description is not Simple line."
    assert parsed_docstring.long_description == "One paragraph.", "long description is not One paragraph."
    assert parsed_docstring

# Generated at 2022-06-13 19:47:59.125018
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    actual = NumpydocParser().parse(
        '''
        Short description.
    
        Long description.
    
        Parameters
        ----------
        arg1 : int
            The first argument.
        arg2 : str
            The second argument.
    
        Returns
        -------
        dict
            A dictionary with a key ``"foo"``.
    
        
        """'''
    )

# Generated at 2022-06-13 19:48:00.541687
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert(NumpydocParser().parse("""
    """))


# Generated at 2022-06-13 19:48:13.149960
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = parser.parse("""\
    Method for spectral clustering

    .. deprecated:: 2.0
        This method will be removed in future releases.

    Parameters
    ----------
    data
        Data matrix.
    """)
    assert docstring.short_description == "Method for spectral clustering"
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False
    assert len(docstring.meta) == 2
    assert docstring.meta[0].args[0] == "deprecation"
    assert docstring.meta[0].args[1] == None
    assert docstring.meta[0].version == "2.0"
    assert docstring.meta[0].description

# Generated at 2022-06-13 19:48:21.553829
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:49:09.308343
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
            The short summary line.

            The long description, and note that paragraphs are separated by
            a blank line.

            Parameters
            ----------
            arg_name: int, optional
                A description of the parameter.

                And a second paragraph.

                Default is None.

            arg_2 : type
                A description of arg_2.

            Returns
            -------
            return_name : type
                A description of the return.

            Examples
            --------
            >>> example
            >>> example

            References
            ----------
            The references.

            '''
    parser = NumpydocParser()
    docstring = parser.parse(text)

    assert docstring.short_description == 'The short summary line.'
    assert docstring.long_description == 'The long description, and note that paragraphs are separated by\na blank line.'

# Generated at 2022-06-13 19:49:14.086355
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    expected_results = Docstring(long_description='long desc\n', short_description='short desc')
    text = 'short desc\n\nlong desc\n'
    assert parser.parse(text) == expected_results



# Generated at 2022-06-13 19:49:21.288615
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = parser.parse.__doc__

    assert parser.parse(docstring).short_description == "Parse the numpy-style docstring into its components."
    assert parser.parse(docstring).long_description == ":returns: parsed docstring"
    assert parser.parse(docstring).blank_after_short_description == True
    assert parser.parse(docstring).blank_after_long_description == False
    assert parser.parse(docstring).meta[0].args == ['returns']
    assert parser.parse(docstring).meta[0].description == "parsed docstring"


# Generated at 2022-06-13 19:49:31.459930
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """
docstring
    for method

Arguments
    this is the description of arg1
    it can span multiple lines
    arg1 : str
        And this is the description of
        arg1 's type
    arg2 : int, optional
        And this is the description of
        arg2 's type

Returns
    And this is the description
    of what is returned
    return_value: str
        And this is the description of
        return_value 's type

Raises
    And this is the description
    of what is raised
    ValueError
        And this is the description
        of the ValueError
    """
    parser = NumpydocParser()
    docstring = parser.parse(docstring)
    assert docstring.short_description == "docstring"
    assert docstring.blank_after_short

# Generated at 2022-06-13 19:49:42.301470
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This is a short description.

    This is a long description.
    """
    docstring = NumpydocParser().parse(text)
    assert(docstring.short_description == "This is a short description.\n")
    assert(docstring.long_description == "This is a long description.\n")
    assert(docstring.blank_after_short_description == True)
    assert(docstring.blank_after_long_description == True)

    text2 = """
    This is a short description.

    This is a long description.

    Parameters
    ----------
    a : bool
        A bool.
    b : integer
        An integer.
    """
    docstring2 = NumpydocParser().parse(text2)

# Generated at 2022-06-13 19:49:45.908759
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
        one
        two
        three
        '''
    assert parse(text) is not None


# Generated at 2022-06-13 19:49:57.999532
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """
    Tests that NumpyDocParser parses docstrings with default sections.

    :param str a: an argument
    :param int b: the number of things

    :raises ValueError: when value is not valid

    :rtype: str

    :returns:
        a string of the form "You passed 'a' and 'b'".

    :Example:
        >>> parse("1")
        >>> parse("2")
        >>> parse("3")
        >>> parse("4")

    :seealso:
        other helpful functions
    """

    parser = NumpydocParser()
    doc = parser.parse(docstring)

    assert doc.short_description == "Tests that NumpyDocParser parses docstrings with default sections"


# Generated at 2022-06-13 19:50:08.149829
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import urllib.parse
    import datetime
    s = """
        Summary line.

        Extended description.

        Extended description continued.

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

    t = parse(s)
    assert(t.short_description == "Summary line.")
    assert(_clean_str(t.long_description) == "Extended description. Extended description continued.")
    assert(t.meta == [
            DocstringMeta(["param", "arg1"], description="Description of arg1"),
            DocstringMeta(["param", "arg2"], description="Description of arg2"),
            DocstringMeta(["returns"], description="Description of return value"),
])

    #

# Generated at 2022-06-13 19:50:15.119827
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    #Create a class
    class Simple(object):
        """Simple class description

        Simple class description
        continues here

        Parameters
        ----------
        a : int
            parameter a
        b : list
            parameter b

        Raises
        ------
        ValueError
            If a < 0

        Returns
        -------
        retval : int
            Return value
        """

        def __init__(self, a, b):
            self.a = a
            self.b = b

        def get(self):
            return self.a

    ds = Simple.__doc__
    docstring = NumpydocParser().parse(ds)
    assert docstring.short_description == "Simple class description"
    assert docstring.long_description == "Simple class description continues here"

# Generated at 2022-06-13 19:50:27.609503
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    # test without a docstring
    assert parser.parse(None) == Docstring()
    # test with a blank docstring
    assert parser.parse('') == Docstring()
    # test with a docstring start with a newline
    assert parser.parse('\n \n') == Docstring()
    # test with a docstring that a start with a comment
    assert parser.parse('#') == Docstring()
    # test with a docstring that a start with a comment and a newline
    assert parser.parse('#\n') == Docstring()
    # test with a docstring that a start with a comment and a space and a newline
    assert parser.parse('# \n') == Docstring()
    # test with a docstring that a start with a comment and a space and a newline and

# Generated at 2022-06-13 19:51:14.639416
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpy_docstring = """
    This is a numpy docstring
    """

    assert parse(numpy_docstring) == Docstring(
        short_description='This is a numpy docstring',
        long_description=None,
        meta=[]
    )

    numpy_docstring = """
    This is a numpy docstring
    that spans multiple lines

    And this is a long description
    """

    assert parse(numpy_docstring) == Docstring(
        short_description='This is a numpy docstring',
        long_description='that spans multiple lines\n\nAnd this is a long description',
        meta=[]
    )


    numpy_docstring = """
    This is a numpy docstring
    """


# Generated at 2022-06-13 19:51:24.289051
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    text = """
    This is a description of the function

    """
    ret = NumpydocParser().parse(text)
    assert ret.short_description == "This is a description of the function"

    text = """
    This is a description of the function divided
    across
    multiple lines

    """
    ret = NumpydocParser().parse(text)
    assert ret.short_description == "This is a description of the function divided"

    text = """
    This is the short description
    and this is the long description

    """
    ret = NumpydocParser().parse(text)
    assert ret.short_description == "This is the short description"
    assert ret.long_description == "and this is the long description"
    assert ret.blank_after_short_description
    assert not ret.blank_after_long