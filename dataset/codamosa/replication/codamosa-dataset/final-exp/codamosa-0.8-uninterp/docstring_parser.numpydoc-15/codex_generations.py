

# Generated at 2022-06-13 19:41:35.382523
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    s = _KVSection("Title" , "key")
    text = "key\n    value\n"
    it = s.parse(text)
    first_element = next(it, None)

    assert(first_element.args == ["key"])
    assert(first_element.description == "value")

# Generated at 2022-06-13 19:41:42.233836
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print('Testing NumpydocParser parse method')
    import os

    with open(os.path.join(os.path.dirname(__file__), 'numpydoc_texts', 'numpydoc_ex.txt')) as file:
        text = file.read()

    clean_text = inspect.cleandoc(text)
    parser = NumpydocParser()
    docstring = parser.parse(text)

    # split by sections
    sections = [line for line in clean_text.splitlines() if (line.startswith('-') and len(line) > 3)]

    # First test the short and long descriptions
    if docstring.short_description != clean_text.splitlines()[0]:
        raise Exception('The parsing of the short description failed')


# Generated at 2022-06-13 19:41:52.572505
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    assert list(_KVSection("", "").parse("")) == []
    assert list(_KVSection("", "").parse(" \n \n  ")) == []
    assert list(_KVSection("", "").parse("a\n b\n c")) == []

    # If a comment line has a key and value, it should be parsed
    assert list(
        _KVSection("", "").parse(
            "\n".join("key{} value{}".format(i, i) for i in range(8))
        )
    ) == [("key{}".format(i), "value{}".format(i)) for i in range(8)]

    # But if a comment line is empty or blank, it should be ignored

# Generated at 2022-06-13 19:41:56.164834
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    section = Section("Deprecation warning", "deprecation")
    text = """
    .. deprecated::
        this is the deprecation warning
    """
    assert list(section.parse(text))[0].description == "this is the deprecation warning"



# Generated at 2022-06-13 19:42:05.684858
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    section_parameter = ParamSection("Parameters", "param")
    line = """arg_name
            arg_description
        arg_2 : type, optional
            descriptions can also span...
            ... multiple lines"""

    element = inspect.cleandoc(line)

    lista = section_parameter.parse(element)

    lista[0] = DocstringParam(
        args=["param", "arg_name"],
        description="arg_description",
        arg_name="arg_name",
        type_name=None,
        is_optional=False,
        default=None,
    )

# Generated at 2022-06-13 19:42:13.528411
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_docstring = """
    This function calculates the sum of two numbers

    Parameters
    ----------
    x : int
        The first number
    y : float, optional
        The second number. Defaults to 0.

    Returns
    -------
    int
        Sum of the two numbers

    See Also
    --------
    sum : Computes the sum of all the numbers passed in arguments

    Examples
    --------
    >>> sum2(3, 99)
    102
    """
    parsed = parse(test_docstring)
    assert len(parsed.meta) == 4
    assert parsed.short_description == "This function calculates the sum of two numbers"

# Generated at 2022-06-13 19:42:18.844913
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    test_text = '''
        arg_name
            arg_description
        arg_2 : type, optional
            descriptions can also span...
            ... multiple lines
    '''
    assert _KVSection("Parameters", "param").parse(test_text) is not None



# Generated at 2022-06-13 19:42:24.322477
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    id_list = ['param', 'param', 'param', 'other_param', 'other_param', 'other_param', 'other_param', 'receives', 'receives', 'raises', 'raises', 'warns', 'warns', 'attribute', 'attribute', 'returns', 'yields', 'examples', 'examples', 'warnings', 'warnings', 'see_also', 'see_also', 'notes', 'notes', 'references', 'references', 'deprecation']

# Generated at 2022-06-13 19:42:27.006539
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    s = DeprecationSection("deprecated", "deprecation")
    text = 'deprecated:: 0.1.0 \n   description'
    a = s.parse(text)
    assert a
    a = next(a)
    assert a.description == 'description'
    assert a.version == '0.1.0'

# Generated at 2022-06-13 19:42:32.802592
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    s = _KVSection("title", "key")
    text = inspect.cleandoc("""key
        value
    key2 : type
        values can also span...
        ... multiple lines""")
    doc = s.parse(text)
    assert len(doc) == 2
    assert doc[0].args[0] == "key"
    assert doc[0].args[1] == "key"
    assert doc[0].description == "value"
    assert doc[1].args[0] == "key"
    assert doc[1].args[1] == "key2"
    assert doc[1].description == "values can also span...\n... multiple lines"



# Generated at 2022-06-13 19:42:47.760957
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print(NumpydocParser().parse.__doc__)
    print('\n')

# Generated at 2022-06-13 19:42:58.046476
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    class MySection(Section):
        def parse(self, text: str) -> T.Iterable[DocstringMeta]:
            yield DocstringMeta([], description=_clean_str(text))
    parser = NumpydocParser()
    assert parser.parse("") == Docstring()
    assert parser.parse("""
        Short description.

        Long description.

        Parameters
        ----------
        arg
            arg description
        arg2 : str, optional
            arg2 description
        """).meta == [
        DocstringParam(args=["param", "arg"], description="arg description"),
        DocstringParam(args=["param", "arg2"], description="arg2 description", type_name="str", is_optional=True),
    ]
    parser.add_section(MySection("MySection", "my_section"))
    assert parser.parse

# Generated at 2022-06-13 19:43:03.287130
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Test happy path
    docstring_1 = '''
    Created on Tue Sep 24 2019
    
    @author: rory
    @contact: Rory Stocks rory.st@pm.me
    @date: created on: 24/09/2019
    
    
    Take a pandas DataFrame and return a ml-friendly DataArray
    Parameters
    ----------
    dataframe : pandas.DataFrame
        DataFrame to convert
    Returns
    -------
    pandas.DataArray
        Converted DataArray
    '''

    docstring_1_parsed = NumpydocParser().parse(docstring_1)

    expected_1 = Docstring()
    expected_1.short_description = 'Take a pandas DataFrame and return a ml-friendly DataArray'

# Generated at 2022-06-13 19:43:14.370077
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:43:15.501030
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    pass


# Generated at 2022-06-13 19:43:26.712787
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    # empty docstring
    assert bool(NumpydocParser().parse("")) == False


# Generated at 2022-06-13 19:43:39.908717
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()


# Generated at 2022-06-13 19:43:47.232914
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    original_text = '''
    Parameters
    ----------
    n_components : int (default: 10)
        Number of components.

    Other Parameters
    ----------------
    n_its : int, optional
        Maximum number of iterations to perform.

        Default: 20

    Returns
    -------
    ac : AnisotropicCluster object
        The optimized, fitted model.
    '''
    text = original_text.strip()
    parser = NumpydocParser()
    ds = parser.parse(text)

    # test fields
    assert ds.short_description is None
    assert ds.long_description is None
    assert ds.blank_after_short_description is False
    assert ds.blank_after_long_description is False

    assert len(ds.meta) == 2

# Generated at 2022-06-13 19:43:57.885242
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    ret = NumpydocParser().parse(
        """
    description of the function
    can span...
    multiple lines
    """
    )
    assert ret
    assert ret.short_description == "description of the function"
    assert ret.long_description == "can span...\nmultiple lines"

    ret = NumpydocParser().parse(
        """
    description of the function
    can span...
    multiple lines

    Parameters
    ----------
    param_1 : type
        This parameter is...
        ...multilined

    Returns
    -------
    return_val : type
        This is the return value
    """
    )
    assert ret
    assert ret.short_description == "description of the function"
    assert ret.long_description == "can span...\nmultiple lines"
    assert ret.meta
   

# Generated at 2022-06-13 19:44:08.045971
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydoc_parser = NumpydocParser()
    assert numpydoc_parser.parse('This is my method\n' 
                                ':param arg0: first arg\n'
                                ':param arg1: second arg'
                                ) == NumpydocParser().parse('This is my method\n' 
                                ':param arg0: first arg\n'
                                ':param arg1: second arg'
                                )

# Generated at 2022-06-13 19:44:18.596927
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
        Single line description.
    
        Params
        ------
        param1 : int
            Parameter one.
        param2 : Decoder
            Parameter two.
    """
    docstr = NumpydocParser().parse(text)
    assert docstr.short_description == 'Single line description.'
    assert docstr.long_description == None
    assert docstr.blank_after_short_description == False
    assert docstr.blank_after_long_description == False
    assert len(docstr.meta) == 1
    assert len(docstr.meta[0].args) == 2
    assert docstr.meta[0].args[0] == 'param'
    assert docstr.meta[0].args[1] == 'param1'
    assert docstr.meta[0].description == 'Parameter one.'


# Generated at 2022-06-13 19:44:31.936671
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    description = """
    This is short description that
    spans multiple lines
    """
    returns_description = """
    This is a description of the return value
    """
    example = """
    >>> print(example)
    example
    """
    docstring = f"""
    {description}
    {example}
    Parameters:
        first_param: This is a description of the first parameter
        second_param: This is a description of the second parameter
    Yields:
        The yield type is specified by the given type
    Returns:
        {returns_description}
    """
    parser = NumpydocParser()
    parse_result = parser.parse(docstring)
    assert parse_result.short_description == description
    assert parse_result.long_description == example
    assert parse_result.blank_after_short_description

# Generated at 2022-06-13 19:44:42.147560
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = \
'''
This is a description of something.

:param name: name of the object.
:param second_name: name of another object.

:returns: list of strings.
'''
    doc = parser.parse(docstring)
    assert doc.short_description == 'This is a description of something.'

    # Check the parameters
    assert len(doc.meta) == 2
    assert doc.meta[0].args == ['param', 'name']
    assert doc.meta[0].description == 'name of the object.'
    assert doc.meta[1].args == ['param', 'second_name']
    assert doc.meta[1].description == 'name of another object.'

    # Check the return value
    assert len(doc.meta) == 2
    assert doc

# Generated at 2022-06-13 19:44:50.281340
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:55.457224
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = """
    This function does something awesome.

    This is a long description that spans multiple lines.

    Parameters
    ----------
    arg : int
        This argument does something.
    arg_with_default : int, optional
        Default is 1.
    kwarg : str, optional
        This keyword argument is optional.
        Default is 'a'.
    other_kwarg : str, optional
        This keyword argument is optional.
    """

# Generated at 2022-06-13 19:45:05.519156
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    testThis = NumpydocParser()
    testThis.parse("[a, b, c]\n\nParameters\n----------\nx : int\n    X coord.")
    testThis.parse("[a, b, c]\n\nParameters\n----------\nx : int\n    X coord.\n\nReturns\n-------\nNone if x is divisible by 2, else 0")
    testThis.parse("[a, b, c]\n\nParameters\n----------\nx : int\n    X coord.\n\nRaises\n------\nValueError\n    If x is not divisible by 2\n    \nReturns\n-------\nNone if x is divisible by 2, else 0")

# Generated at 2022-06-13 19:45:15.589755
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    test_text = """This is a function
    With a :class:`Function`-like signature

    Parameters
    ----------
    text : str
        What to parse

    Returns
    -------
    Docstring
        Parsed docstring

    Notes
    -----
    If the text is empty, an empty Docstring will be returned
    """

    parsed_docstring = parser.parse(test_text)
    assert parsed_docstring.short_description == "This is a function"

    assert parsed_docstring.long_description.startswith("With a Function-like")
    assert parsed_docstring.long_description.endswith("be returned")

    assert parsed_docstring.meta[0].args == ['param', 'text']
    assert parsed_docstring.meta[0].description.start

# Generated at 2022-06-13 19:45:21.499819
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    parser = NumpydocParser()

    # Check if parser is not None
    assert parser != None, 'parser is None'

    # Check if parser has a method parse
    assert hasattr(parser, 'parse'), 'parser has no method parse'

    # Check if call return a valid Docstring object
    assert not parser.parse('').__name__ is None, 'parser.parse returns None'


parser = NumpydocParser()

# Check if parser is not None
assert parser != None, 'parser is None'

# Check if parser has a method parse
assert hasattr(parser, 'parse'), 'parser has no method parse'

# Check if call return a valid Docstring object
assert not parser.parse('').__name__ is None, 'parser.parse returns None'

# Generated at 2022-06-13 19:45:30.871110
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''Parameters
    ----------
    engine : {'auto', 'pyarrow', 'fastparquet'}, default 'auto'
        Parquet library to use. If 'auto', then the option
        ``io.parquet.engine`` is used. The default ``io.parquet.engine``
        behavior is to try 'pyarrow', falling back to 'fastparquet' if
        'pyarrow' is unavailable.'''

    doc = NumpydocParser().parse(text)
    assert len(doc.meta) == 1

# Generated at 2022-06-13 19:45:42.419099
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:45:57.975740
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:46:01.925948
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydoc_parser = NumpydocParser()
    docstring = numpydoc_parser.parse(
        """
            This is a docstring

            Parameters
            ----------
            yr : int
                The year.
            param_2 : Union[int, float]
                Some description of param_2
        """
    )
    assert docstring.long_description == "This is a docstring"
    assert docstring.meta == []
    assert docstring.short_description == "This is a docstring"



# Generated at 2022-06-13 19:46:13.286821
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:46:25.707375
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Unit test for method parse of class NumpydocParser.

    """
    import os

    from .common import DocstringMeta
    from .parsers.google import _GoogleParser

    def _test_file(path: str) -> None:
        with open(path) as fp:
            text = fp.read()
        expected = _GoogleParser().parse(text)
        actual = parse(text)
        assert actual == expected
        actual_meta = []
        for meta in actual.meta:
            if isinstance(meta, DocstringMeta) and len(meta.args) > 0:
                actual_meta.append(meta)
        actual_meta.sort(key=str)
        expected_meta = []

# Generated at 2022-06-13 19:46:37.051770
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # case 1
    text = """
    This is the docstring!
    It spans several lines,
    but is terminated by a blank line.
    It's time to parse it.
    This is the docstring!
    It spans several lines,
    but is terminated by a blank line.
    It's time to parse it.
    """
    result = parse(text)
    assert result.short_description == "This is the docstring!"
    assert result.long_description == "It spans several lines, but is terminated by a blank line. It's time to parse it."

    # case 2

# Generated at 2022-06-13 19:46:45.914906
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # test parse
    # lst = ["Returns","Return","Yields","Yield", "Raises","Raise"]
    lst = ["Returns"]

    for s in lst:
        parser = NumpydocParser()
        parser.add_section(ReturnsSection(s, "returns"))
        text = ".. {}:: foo or None".format(s)
        result = parser.parse(text)
        assert result.short_description is None
        assert len(result.meta) == 1
        assert result.meta[0].type_name == "foo or None"
        assert result.meta[0].description is None
        assert result.meta[0].return_name is None
        assert result.meta[0].is_generator is False


# Generated at 2022-06-13 19:46:58.019145
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = inspect.cleandoc(
        """\
        Parameters
        ----------
        arg1 : int
            The first parameter.
        arg2 : str
            The second parameter.
        arg3 : list of ints
            The third parameter.
        """
    )
    docstring = parser.parse(text)
    assert docstring.short_description == ""
    assert docstring.long_description == ""
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False
    assert len(docstring.meta) == 3
    assert docstring.meta[0].description == "The first parameter."
    assert docstring.meta[0].arg_name == "arg1"

# Generated at 2022-06-13 19:47:11.169168
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = """This is a sample docstring
    Parameters
    ----------
    arg_name
        arg_description
    arg_2 : type, optional
        descriptions can also span...
        ... multiple lines
    """
    result = parser.parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description == "This is a sample docstring"
    assert len(result.meta) == 2
    assert isinstance(result.meta[0], DocstringParam)
    assert isinstance(result.meta[0], DocstringParam)
    assert result.meta[0].args[1] == 'arg_name'
    assert result.meta[0].description == 'arg_description'
    assert result.meta[1].args[1] == 'arg_2'


# Generated at 2022-06-13 19:47:20.750204
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """Create an instance.

    Parameters
    ----------
    name : str, optional
        Param with optional type annotation

    args : some_type
        A parameter with no type annotation which
        spans multiple lines
    """

    docstring_meta = [
        DocstringMeta(args=['param'], arg_name='name', description='Param with optional type annotation', type_name='str', is_optional=True), 
        DocstringMeta(args=['param'], arg_name='args', description='A parameter with no type annotation which spans multiple lines', type_name='some_type')
    ]

    docstring_meta_tests = NumpydocParser(sections=[Section('Parameters', 'param')]).parse(docstring)

    assert docstring_meta == docstring_meta_tests.meta


# Generated at 2022-06-13 19:47:30.803683
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    raw_text = """
    This is a docstring.

    Parameters
    ----------
    a : int
        first param

    b : str = 'hello'
        second param

    Returns
    -------
    None

    Raises
    ------
    ValueError
        if a == 0
    """


# Generated at 2022-06-13 19:47:47.232110
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import docsting_parser
    text = """
    This is a numpydoc docstring.

    This is the short description.
    This is the long description.
    
    Parameters
    ----------
    param: type
        This is a param.
    other_param: other_type
        This is a param.
    """
    result = docsting_parser.NumpydocParser().parse(text)
    assert result.short_description == "This is the short description."
    assert result.long_description == "This is the long description."
    assert result.blank_after_short_description == True
    assert result.blank_after_long_description == False

    param = result.meta[0]
    assert param.args[0] == 'param'
    assert param.description == 'This is a param.'
    


# Generated at 2022-06-13 19:47:58.373930
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text_0 = """
    A short description
    A long description spanning multiple lines.
    Parameters
    ----------
    arg_name : str, optional
        Description of ``arg_name``, which has type ``str``, and is
        optional.
    arg_2 : int, optional
        Description of ``arg_2``, which has type ``int``, and is
        also optional.
    Other Parameters
    ----------------
    other_arg : int, optional
        Description of ``other_arg``.
    Returns
    -------
    return_name : str
        Description of ``return_name``.
    See Also
    --------
    Some other function : This is a reference to ``some_other_function``.
    """


# Generated at 2022-06-13 19:48:10.868387
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

    from docscrape.numpydoc import parse
    from docscrape.core import parse_docstring


    def f():
        """Short description.

        Long description.

        Parameters:
        -----------
        arg1
            arg1 description
        arg2 : optional
            arg2 description

        Returns:
        --------
        something : optional
            something description

        """

    docstring = parse_docstring(f.__doc__)

    assert docstring.short_description == "Short description."
    assert docstring.long_description == "Long description."
    assert docstring.blank_after_short_description is False

# Generated at 2022-06-13 19:48:20.274441
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:48:28.171244
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring=r"""
        Get the right-hand sides of a set of equations.

        Parameters
        ----------
        eqs : list of `sympy.relational.Relational`
            List of equations.

        Returns
        -------
        rhses : list of `sympy.Basic`
            A list of right-hand side expressions.

        Examples
        --------
        >>> from sympy import Eq
        >>> from sympy.codegen.array_utils import get_rhs
        >>> get_rhs([Eq(x**2, 1)])
        [1]

    """
    NumpydocParser().parse(docstring)

# Generated at 2022-06-13 19:48:39.733527
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:48:48.523796
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import pprint
    parser = NumpydocParser()

# Generated at 2022-06-13 19:49:00.225488
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = '''This is short description
    This is long description
    This is more description
    
    Parameters
    ----------
    arg_name : type
        arg_description
    arg_2 : type, optional
        descriptions can also span...
        ... multiple lines
    Other Parameters
    ---------
    arg_name
        arg_description
    arg_2 : type
        descriptions can also span...
        ... multiple lines
    '''


# Generated at 2022-06-13 19:49:03.884665
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    Test if the parser of numpy-style docstrings works as expected.
    """
    import doctest
    doctest.run_docstring_examples(NumpydocParser.parse, globals())



# Generated at 2022-06-13 19:49:12.064946
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from pathlib import Path
    import pytest
    from os.path import join
    from .utils import load_docstring

    test_dir = Path(__file__).parent.absolute()
    test_dir = join(test_dir, "testdata/test_numpydoc/")
    expected_out = {
        "test_numpydoc_simple.py": "test_numpydoc_simple.json",
        "test_numpydoc_detailed.py": "test_numpydoc_detailed.json",
    }

    for sf, ef in expected_out.items():
        # Parsing
        d = load_docstring(sf)
        docstring = NumpydocParser().parse(d)

        # Testing

# Generated at 2022-06-13 19:49:23.833997
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    assert parser.parse("") == Docstring()


# Generated at 2022-06-13 19:49:28.398251
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydoc_parser = NumpydocParser()
    assert numpydoc_parser.parse(None) == Docstring()
    assert numpydoc_parser.parse('"""foo"""') == Docstring(short_description='foo')


# Generated at 2022-06-13 19:49:34.729154
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = parser.parse('''
    This is a description
    that spans multiple
    lines.

    Parameters
    ----------
    arg1 : str
        First argument
    arg2 : Optional[str] = None
        Second argument

    Returns
    -------
    int
        Return value
    ''')
    assert docstring.long_description == '''
    This is a description
    that spans multiple
    lines.
    '''.strip()
    assert docstring.meta[0].args == ['param', 'arg1']
    assert docstring.meta[0].description == '''
        First argument
    '''.strip()
    assert docstring.meta[0].type_name == 'str'
    assert docstring.meta[0].is_optional == False

# Generated at 2022-06-13 19:49:39.351169
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    parser = NumpydocParser()
    docstring = '''This function
    gets the last response from
    responses.

    Parameters
    ----------
    responses : list of dict
        The responses.

    Returns
    -------
    :class:`dict`
        Last response.
    '''
    assert parser.parse(docstring)



# Generated at 2022-06-13 19:49:53.100577
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:50:02.670963
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_data = """
    short desc
    long desc
    Parameters
    ----------
    x: int
        Parameter x.
    y: float, optional
        Parameter y.
    Returns
    -------
    total: int
        Sum of x and y.
    """
    result = NumpydocParser().parse(test_data)

# Generated at 2022-06-13 19:50:13.116199
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
    This is the short description.

    This is the
    long description.

    Parameters
    ----------
    
    param_1 : str, optional
        Description of first parameter. This can span multiple lines.

    param_2 : int, optional
        Description of second parameter.

    Returns
    -------
    
    str
        Description of return value.
    '''
    doc_string = NumpydocParser().parse(text)
    assert doc_string.short_description == "This is the short description."
    assert doc_string.long_description == "This is the\nlong description."
    assert doc_string.blank_after_short_description == False
    assert doc_string.blank_after_long_description == True
    params = doc_string.meta[0][0][1]

# Generated at 2022-06-13 19:50:25.899781
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .trim import trim_docstring

# Generated at 2022-06-13 19:50:34.254422
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_str = '''
    This is a summary
    description

    Parameters
    ----------

    arg_1
        This is a description of arg_1, which spans more than one line
    arg_2 : float
        Default is 2.5. This is a description of arg_2

    Raises
    ------
    ValueError
        A description of what might raise ValueError

    Returns
    -------
    out : float
        A description of the returned value
        Default is 2.5.

    '''
    doc = NumpydocParser().parse(test_str)
    keys = ['param', 'raises', 'returns']
    assert doc.short_description == ''
    assert keys == [c.key for c in doc.meta]
    assert doc.meta[0].type_name == 'float'

# Generated at 2022-06-13 19:50:46.745087
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    ds = """
    This is the short description.

    This is the long description.

    Parameters
    ----------
    param1
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    int
        The return value.
    """
    # parse the docstring using default sections
    parsed = NumpydocParser().parse(ds)

    # check the description
    assert parsed.short_description == "This is the short description."
    assert parsed.long_description == (
        "This is the long description.\n"
    )
    assert not parsed.blank_after_short_description

    # check the parameters section
    param_sec = parsed.meta[0]
    assert param_sec.key == "param"
    assert len(param_sec.args) == 1 and param_

# Generated at 2022-06-13 19:51:22.773433
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """Test description

    More description

    Parameters
    ----------
    param : str
        Param description

    def : int
        Param description

    Key-value pairs are fine too without any type
    foo

    baz : int
        Can be nested like this

    Raises
    ------
    ValueError
        This is a raise

    Warnings
    --------

    This is a warning

    Raises
    ------
    ValueError
        This is a raise

    Warnings
    --------

    This is a warning

    Examples
    --------
    >>> a = "This is a example"
    >>> print(a)
    This is a example

    See Also
    --------
    inspect
    yaml
    """

    expected = Docstring()

    # Description section
    expected.short_description = "Test description"
    expected.blank