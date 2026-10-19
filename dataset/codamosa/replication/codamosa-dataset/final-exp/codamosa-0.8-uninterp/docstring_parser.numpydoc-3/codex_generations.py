

# Generated at 2022-06-13 19:41:45.413359
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:41:54.497209
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    test a docstring
    Parameters
    ----------
    arg: type
        description
    arg2 : str, optional
        description
    """
    docstring = NumpydocParser().parse(text)
    assert docstring.short_description == "test a docstring"
    assert docstring.long_description == None
    assert docstring.blank_after_long_description == False
    assert docstring.blank_after_short_description == True
    assert len(docstring.meta) == 2
    assert docstring.meta[0].key == 'param'
    assert docstring.meta[0].args == ['param', 'arg']
    assert docstring.meta[0].description == "description"
    assert docstring.meta[0].arg_name == 'arg'
    assert docstring.meta[0].type

# Generated at 2022-06-13 19:42:01.098803
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    text = """DeprecationWarning
        This function will be removed in a future version.
        Please use the pandas.tseries module instead.
    """
    d = NumpydocParser().parse(text)
    assert d.meta[0].args == ["deprecation"]
    assert d.meta[0].description == text
    assert d.meta[0].version == "DeprecationWarning"
    assert d.short_description == ""
    assert d.long_description == ""

# Generated at 2022-06-13 19:42:07.458115
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    from .common import DocstringDeprecated
    sectionName = "deprecated"
    sectionText = ".. deprecated:: 1.2\n    Use :func:`foo` instead"
    section = DeprecationSection(sectionName, "deprecation")
    result = section.parse(sectionText)
    expected = [DocstringDeprecated(args=["deprecation"], description="Use :func:`foo` instead", version="1.2")]
    assert (result == expected)

# Generated at 2022-06-13 19:42:12.173361
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    text = ".. deprecated:: 1.0\n   Use deprecation section instead.\n"

    assert list(DeprecationSection("deprecated", "deprecated").parse(text))[0].description == "Use deprecation section instead."

# Generated at 2022-06-13 19:42:22.793468
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    ds = NumpydocParser(sections=[DeprecationSection("Deprecated", "deprecation")])
    text = """
    .. deprecated:: 0.1.1
        Do not use this function.
    """
    d = ds.parse(text)
    assert len(d.meta) == 1
    assert d.meta[0].args[0] == "deprecation"
    assert d.meta[0].args[1] == "0.1.1"
    assert d.meta[0].description == "Do not use this function."


# Generated at 2022-06-13 19:42:31.261668
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    section = DeprecationSection("Deprecated", "deprecation")
    text = '.. deprecated:: 0.0.0 \n\nHi'
    meta = list(section.parse(text))
    assert meta[0].description == "Hi"
    assert meta[0].version == "0.0.0"
    text = '.. deprecated:: 0.0.0 \n\nHi\nBye'
    meta = list(section.parse(text))
    assert meta[0].description == "Hi\nBye"
    assert meta[0].version == "0.0.0"


# Generated at 2022-06-13 19:42:38.197045
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    ds = """
fetch_sample_from_openml
    Returns a sample from the openml server.
    Arguments
    ---------
    data_id : int
        The data_id of the dataset to load.
    Datasets
        Datasets are loaded from the openml server.
    test
        test
     """
    expected = DocstringMeta([['fetch_sample_from_openml']],
                             description=None)
    expected.args = ['fetch_sample_from_openml']
    expected.description = 'Returns a sample from the openml server.'
    ds = parse(ds)
    assert str(ds) == str(expected)


# Generated at 2022-06-13 19:42:46.076335
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    kv_section = _KVSection(title=None, key=None)

    # No items
    assert list(kv_section.parse("")) == []

    # Single item
    assert list(kv_section.parse("key")) == [None]

    # Single item with value
    assert list(kv_section.parse("key\n    value")) == ["value"]

    # Single item with value spanning multiple lines
    assert list(kv_section.parse("key\n    value 1\n    value 2")) == [
        "value 1\nvalue 2"
    ]

    # Multiple items
    assert list(kv_section.parse("key 1\n    value 1\nkey 2")) == ["value 1"]

# Generated at 2022-06-13 19:42:56.168271
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    case1 = """Method to convert response to array
    Parameters
    ----------
    data: sequence
        to be converted
    Returns
    -------
    ndarray
        length of data
    Raises
    ------
    ValueError
        For zero length input.
    """
    case2 = """This method performs an action
    Parameters
    ----------
    input: sequence,
        description
    Returns
    -------
    ndarray, optional
        description
    Raises
    ------
    ValueError
        If the input cannot be processed
    Examples
    --------
    >> method(1)
    """

# Generated at 2022-06-13 19:43:13.727263
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert parse("Desc\nArgs:\n\targ:str") == Docstring(
        short_description = "Desc",
        blank_after_short_description = False,
        long_description = None,
        blank_after_long_description = False,
        meta = [
            DocstringParam(
                args = ["param", "arg"],
                description = None,
                arg_name = "arg",
                type_name = "str",
                is_optional = False,
                default = None
            )
        ]
    )

# Generated at 2022-06-13 19:43:20.850017
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This is a simple example of a docstring

    Parameters
    ----------
    a : int
        A number
    b : float
        A floating point number
    c : str
        A string
    d : object
        Another object
    e : list of float
        A list of float
    f : dict
        A dict

    Returns
    -------
    result : str
        The result of the function.
    """

    parsed = parse(text)
    assert parsed.short_description == "This is a simple example of a docstring"
    assert parsed.long_description == None
    assert parsed.blank_after_short_description == True
    assert parsed.blank_after_long_description == False

    assert len(parsed.meta) == 6

# Generated at 2022-06-13 19:43:30.795801
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    Note: This Unit test was for testing the NumpydocParser_parse method
          in the file numpydoc_parser.py.
    """

    parser = NumpydocParser()

# Generated at 2022-06-13 19:43:41.451290
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """
    This is an example of a numpy-style docstring.

    :param param1: This is parameter1.
    :type param1: int, optional
    :param param2: This is parameter2.
    :type param2: str, optional
    :returns: This is return type.
    :rtype: int
    """
    d = NumpydocParser().parse(docstring)
    assert d.long_description == None

# Generated at 2022-06-13 19:43:48.239522
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from io import StringIO
    from .common import _parse_docstring
    from .common import DocstringReturns,DocstringMeta,DocstringRaises,DocstringParam,Docstring
    from .common import DocstringDeprecated,DocstringReturns
    source = """

my_func is nothing special.

   For example:
       >>> my_func(1)
       1
       >>> my_func("hello")
       'hello'

Parameters
----------
arg1: int
    The first argument.
arg2: str
    The first argument.
arg3: bool, optional
    The first argument.

Returns
-------
str
    A string representation of ``arg1``.
"""
    parser = NumpydocParser()
    output = parser.parse(source)

# Generated at 2022-06-13 19:43:58.851106
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:04.093689
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This is a sample docstring for a class.

    Parameters
    ----------
    arg_name : type
        arg_description

    arg_2 : type, optional
        descriptions can also span
        multiple lines
    """
    parser = NumpydocParser()
    docstring = parser.parse(text)
    assert docstring.short_description == "This is a sample docstring for a class."
    assert len(docstring.meta) == 2
    assert docstring.meta[0].description == "arg_description"
    assert docstring.meta[1].description == "descriptions can also span\nmultiple lines"


# Generated at 2022-06-13 19:44:12.449730
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:19.055044
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = "This is the short description\n\nThis is the long description.\n\nParameters\n----------\narg_name\n    arg_description\narg_2 : type, optional\n    descriptions\n    can also span...\n    ... multiple lines\nRaises\n------\nValueError\n    A description of what might raise ValueError\nReturns\n-------\nreturn_name : type\n    A description of this returned value\nanother_type\n    Return names are optional, types are required"
    assert NumpydocParser().parse(text).short_description == "This is the short description"
    assert NumpydocParser().parse(text).long_description == "This is the long description."

# Generated at 2022-06-13 19:44:32.088003
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = """

    Parameters
    ----------
    arg1 : int
        Description of arg1.
    arg2 : str, optional
        Description of arg2, which is optional.

    Other Parameters
    ----------------
    x : int
        Description of x.

    Yields
    ------
    out : generator
        A description of the yield value.

    Raises
    ------
    SomeException
        Description of an exception.

    DeprecationWarning
        .. deprecated:: 1.0.0
            This function is deprecated.
    """
    docstring = parser.parse(text)

# Generated at 2022-06-13 19:44:48.060345
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    Test the method parse of class NumpydocParser for some examples.
    """
    desc ="""\
    Dummy Test Function

    This is a dummy test function.

    Parameters
    ----------
    a: str
        Throws an exception if len(a) != 2
    b: int, optional
        Default is 3. If it is 4, raises a ValueError.

    Returns
    -------
    str
        The result of concatenating a and b.
    """


# Generated at 2022-06-13 19:44:53.983066
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    d = """
    Parses a docstring into its components.

   :param text: docstring to parse
    :returns: parsed docstring
    """
    d = NumpydocParser().parse(d)
    assert d.short_description == 'Parses a docstring into its components.'
    assert len(d.meta) == 1
    assert len(d.meta[0].args) == 2
    assert d.meta[0].args[0] == 'param'
    assert d.meta[0].args[1] == 'text'

# Generated at 2022-06-13 19:44:56.881027
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Parses the numpy-style docstring into its components.

    :returns: parsed docstring
    """

    # ds = NumpydocParser().parse(text)
    ds = parse(text)
    print(ds)



# Generated at 2022-06-13 19:45:03.593729
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Example function.

    This function is an example.
    And it's worth trying it.

    Parameters
    ----------
    x : int
        This is an argument.
    y : str
        The second argument.

    Returns
    -------
    int
        The number of arguments.

    Raises
    ------
    Exception: Something is wrong.

    Warns
    -----
    FutureWarning: Something may be wrong.

    Warn
    ----
    FutureWarning: Something may be wrong.
    """
    result = NumpydocParser().parse(text)
    expected = Docstring()
    expected.short_description = 'Example function.'
    expected.blank_after_short_description = True
    expected.blank_after_long_description = True

# Generated at 2022-06-13 19:45:14.364068
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
    This is a method docstring.

    Parameters
    ----------
    arg1 : str
        Description of `arg1`
    arg2 : bool, optional (default=False)
        Description of `arg2`

    Returns
    -------
    bool
        Description of the return value
    '''


# Generated at 2022-06-13 19:45:21.681569
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_docstring_text = """This is the summary.

This is the long description. It can continue over multiple lines.

Parameters
----------
arg1 : float
    This is the description of arg1
arg2 : float
    This is the description of arg2

Returns
-------
float
    This is a description of the return value
"""
    ret = NumpydocParser().parse(test_docstring_text)
    short_desc = "This is the summary."
    long_desc = """This is the long description. It can continue over multiple lines."""

    assert ret.short_description == short_desc
    assert ret.long_description == long_desc

# Generated at 2022-06-13 19:45:29.010562
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This is a short description.

    This is a longer description.

    This can also contain multiple paragraphs.

    Parameters
    ----------
    text: str, optional
        This is a description of ``text``.


    Other Parameters
    ----------------
    f: int
        This is a description of ``f``.
    """
    docstring = NumpydocParser().parse(text)
    assert len(docstring.meta) == 2
    assert docstring.meta[0].args == ["param", "text"]
    assert docstring.meta[1].args == ["param", "f"]


# Generated at 2022-06-13 19:45:35.972517
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    test_docstr = \
        """
        Test function.

        Parameters
        ----------
        param1 : int, optional
            Description of param1
        param2 : str, optional
            Description of param2

        Returns
        -------
        str
            Description of return value
        """
    test_docstr_parser = parser.parse(test_docstr)

    assert test_docstr_parser.short_description == "Test function."
    assert test_docstr_parser.long_description == None
    assert test_docstr_parser.blank_after_long_description == False
    assert test_docstr_parser.blank_after_short_description == True

    metadata = test_docstr_parser.meta
    assert len(metadata) == 2  # 2 sections


# Generated at 2022-06-13 19:45:45.373816
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert parse("") == Docstring()

    lines = inspect.cleandoc(
        """
        This is a short description.

        This is a long description.

        Parameters
        ----------
        arg1 : int
            Description of arg1.

            It can span multiple
            lines.
        arg2 : str (optional)
            Description of arg2.
    """
    ).splitlines()

    desc = Docstring(
        short_description=lines[0],
        blank_after_short_description=False,
        long_description=lines[1],
        blank_after_long_description=False,
    )


# Generated at 2022-06-13 19:45:53.202480
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print("Testing NumpydocParser_parse...")
    text = (
        """\
        This is a description.
    
        :param arg: This is a param.
        :type arg: type
        :param arg: This is a param.
        :type arg: type
        """
    )
    text2 = (
        """\
        This is a description.
    
        :param arg: This is a param.
        :type arg: type
        :param arg: This is a param.
        :type arg: type
        :param arg: This is a param.
        :type arg: type
        """
    )
    parser = NumpydocParser()
    parsed_docstring = parser.parse(text)
    parsed_docstring2 = parser.parse(text2)
    assert parsed_docstring.short

# Generated at 2022-06-13 19:46:12.012885
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc_string = '''
    Short summary

    Longer multi-line summary

    Parameters
    ----------
    arg : str
        A required string argument
    kwarg : int
        A required numeric argument
    optkw : bool, optional
        An optional argument with default value False

    Returns
    -------
    bool
        A bool value
    '''

# Generated at 2022-06-13 19:46:24.531545
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .common import Docstring, DocstringDeprecated, DocstringMeta, DocstringParam, DocstringRaises, DocstringReturns
    from .common import DocstringShortDescription, DocstringLongDescription, DocstringBlankAfterShortDescription, DocstringBlankAfterLongDescription

    parser = NumpydocParser()

# Generated at 2022-06-13 19:46:33.218188
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = """
        This is the short description.

        And this is the long description.

        Parameters
        ----------
        param1 : int
            The first parameter.
        param2 : str
            The second parameter.
        param3
            The third parameter.

        Yields
        ------
        result: Any
            The result.
    """
    resut = parser.parse(text)
    # Test attribut blank_after_short_description
    assert resut.blank_after_short_description == True
    # Test attribut long_description
    assert resut.long_description == "And this is the long description."
    # Test attribut blank_after_long_description
    assert resut.blank_after_long_description == True
    # Test attribut short_description
    assert resut.short

# Generated at 2022-06-13 19:46:40.848931
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    string = """
    Some
    Docstring

    Parameters
    ----------

    a
        first parameter

    b: float
        second parameter

    Paremeters
    ----------

    c
        third parameter

    Returns
    -------

    x : float
        first return value

    y
        second return value

    Raises
    ------

    ValueError
        A description of what might raise ValueError

    """
    parser = NumpydocParser()
    docstring = parser.parse(string)
    assert docstring.short_description == "Some Docstring"
    assert docstring.long_description == "first parameter\n"\
                                         "second parameter\n"\
                                         "third parameter"
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False

# Generated at 2022-06-13 19:46:55.096092
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    function to test the method parse of class NumpydocParser
    """
    import astor

    # tests if the text passed is empty
    text = ''
    assert str(astor.to_source(parse(text))) == 'Docstring()'

    # tests if the docstring is single line
    text = 'this is a docstring'
    assert str(astor.to_source(parse(text))) == 'Docstring( short_description=\'this is a docstring\', long_description=None)'

    # tests if the docstring is a multi line docstring with a single line in
    # between
    text = 'this is a docstring\n  with a line in between'

# Generated at 2022-06-13 19:47:01.828155
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = r"""Summary line.

Extended description.

Parameters
----------
arg1 : int
    Description of `arg1`.
arg2 : str
    Description of `arg2` (with typos).

Returns
-------
bool
    Description of return value.
other_param : dict
    Other Parameters

Raises
------
ValueError
    If `arg2` has typos.

"""
    parser = NumpydocParser()

    ret = parser.parse(text)
    assert ret.short_description == "Summary line."
    assert ret.long_description == "Extended description."

    assert ret.meta[0].args == ["param", "arg1"]
    assert ret.meta[0].description == "Description of `arg1`."
    assert ret.meta[0].type_name == "int"

   

# Generated at 2022-06-13 19:47:13.981861
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring_text = '''\
    Some description.

    Parameters
    ----------
    arg_name : type
        arg_description.

    Raises
    ------
    TypeError
        If the type of ``arg_name`` is incorrect.

    Returns
    -------
    return_name : type
        return_description.
    '''
    expected_result = """\
    Some description.

    :param str arg_name: arg_description.
    :raises TypeError: If the type of ``arg_name`` is incorrect.
    :returns return_name: return_description.
    """
    assert expected_result == parse(docstring_text).to_sphinx()


# Generated at 2022-06-13 19:47:21.953327
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    from .common import (
        Docstring,
        DocstringDeprecated,
        DocstringMeta,
        DocstringParam,
        DocstringRaises,
        DocstringReturns,
    )

    parser = NumpydocParser()

    # Test empty string
    actual = parser.parse("")
    assert actual.short_description is None
    assert actual.long_description is None
    assert len(actual.meta) == 0

    # Test parameters and returns
    doc_string = """Parse the numpy-style docstring into its components.

    :param text: The docstring to process.
    :returns: A parsed docstring.
    """

    actual = parser.parse(doc_string)
    assert actual.short_description == "Parse the numpy-style docstring into its components."

# Generated at 2022-06-13 19:47:31.567326
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    s = """
    Parameters
    ----------
    a : int
        A numeric value.
    b : int, optional
        A numeric value.
    """
    parsed = NumpydocParser().parse(s)
    assert isinstance(parsed, Docstring)
    assert len(parsed.meta) == 1
    assert isinstance(parsed.meta[0], DocstringMeta)
    assert len(parsed.meta[0].args) == 2
    assert parsed.meta[0].args[0] == 'param'
    assert parsed.meta[0].args[1] == 'a'
    assert parsed.meta[0].description is not None
    assert len(parsed.meta[0].description) > 0
    parsed = NumpydocParser().parse("test docstring with no title")

# Generated at 2022-06-13 19:47:38.003472
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = parser.parse(
        """
        Set each pixel in the image to the given color.

        Parameters
        ----------
        color : tuple
            The color to set each pixel to.
        """
    )
    assert docstring.short_description == "Set each pixel in the image to the given color."
    assert docstring.long_description == None
    assert docstring.params[0].arg_name == "color"
    assert docstring.params[0].type_name == "tuple"
    assert docstring.params[0].description == "The color to set each pixel to."

# Generated at 2022-06-13 19:47:56.502225
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_str = '''
        test_str.

        Parameters
        ----------
        param: test_type

        Raises
        ------
        ValueError
            test_message.
        '''
    result = parse(test_str)
    assert result.short_description == test_str.split('\n')[1]
    assert result.long_description is None
    assert len(result.meta) == 2
    assert result.meta[0].args[0] == "param"
    assert result.meta[0].args[1] == "param"
    assert result.meta[0].type_name == "test_type"
    assert result.meta[1].args[0] == "raises"
    assert result.meta[1].args[1] == "ValueError"

# Generated at 2022-06-13 19:48:01.005859
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = "first line\n\nsecond line\n\nthird line\n"
    ret = parser.parse(docstring)
    assert ret.short_description == "first line"
    assert ret.long_description == "second line\n\nthird line"
    assert ret.blank_after_short_description
    assert ret.blank_after_long_description
    assert ret.meta == []


# Generated at 2022-06-13 19:48:13.889401
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:48:17.870620
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
    Test function

    Something with a `link <http://google.com>`_.

    Parameters
    ----------
    arg : int
        An argument
    other : float
        Another argument

    Raises
    ------
    ValueError
        For no good reason
    '''

    NumpydocParser().parse(text)

# Generated at 2022-06-13 19:48:34.374895
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """Some description
    with a second line
    and a new paragraph
    
    Parameters
    ----------
    a : int
        Some description for parameter a
    b : float, optional
        Some optional description for parameter b
        
    Returns
    -------
    c : int
        Some description for c
    """

    assert len(parse(text).meta) == 2
    assert parse(text).meta[0].type == 'param'
    assert parse(text).meta[0].kwargs['arg_name'] == 'a'
    assert parse(text).meta[0].kwargs['type_name'] == 'int'
    assert parse(text).meta[0].kwargs['is_optional'] == False
    assert parse(text).meta[1].type == 'returns'
    assert parse(text).meta[1].kwargs

# Generated at 2022-06-13 19:48:45.007302
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import inspect
    import sys

    import attr
    import pytest
    import pytest_check as check

    from numpydoc_parse import NumpydocParser, parse


# Generated at 2022-06-13 19:48:55.816632
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:49:01.793425
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''One line summary.
    Longer description.
    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.
    param3 : {'hi', 'lo'}, optional
        The third parameter.  Defaults to 'hi'.
    Returns
    -------
    description
        description
    """
    '''

    assert len(NumpydocParser().parse(text).meta) == 6

# Generated at 2022-06-13 19:49:06.173238
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert '\n' in parse.__doc__
    docs = '''
    Arguments
    ---------
    arg1 : int
        The first argument.
    arg2 : str
        The second argument.
    '''
    assert isinstance(parse(docs), Docstring)



# Generated at 2022-06-13 19:49:18.330820
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    short describe

    long describe

    Parameters
    ----------
    arg1 : int
        the first arg
    arg2 : float, optional
        the second arg

    Returns
    -------
    int
        int return value

    Raises
    ------
    ValueError
        When something bad happens

    See Also
    --------
    func2, func3

    Notes
    -----
    bla bla

    bla bla

    Examples
    --------
    >>> import foo
    >>> foo.func(5, 3)
    4
    >>> foo.func(5, 3.3)
    6

    """
    desc_short = "short describe"
    desc_long = """long describe"""

# Generated at 2022-06-13 19:49:33.529376
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:49:42.741852
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    title_list = ['Parameters',
        'Params',
        'Arguments',
        'Args',
        'Other Parameters',
        'Other Params',
        'Other Arguments',
        'Other Args',
        'Receives',
        'Receive',
        'Raises',
        'Raise',
        'Warns',
        'Warn',
        'Attributes',
        'Attribute',
        'Returns',
        'Return',
        'Yields',
        'Yield',
        'Examples',
        'Example',
        'Warnings',
        'Warning',
        'See Also',
        'Related',
        'Notes',
        'Note',
        'References',
        'Reference',
        'deprecated']

# Generated at 2022-06-13 19:49:56.263439
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Parse empty string
    assert parse('') == Docstring()

    # Parse without meta
    text = '''
        This is a short description.

        And this is the long one.
        It has two lines.
        '''

    # Remove indents and newlines for ease of comparison
    text = inspect.cleandoc(text)
    parts = text.split("\n", 1)
    assert parse(text) == Docstring(
        short_description=parts[0],
        long_description=parts[1] or None,
        blank_after_short_description=True,
        blank_after_long_description=True,
    )

    # Parse with meta

# Generated at 2022-06-13 19:50:07.064515
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    The add method

    This method is used to add numbers

    Parameters
    ----------
    num1: int
        First number to add
    num2: int
        Second number to add

    Returns
    -------
    result: int
        The sum of the given numbers
    """


# Generated at 2022-06-13 19:50:16.090229
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:50:25.896216
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    ds = """A one line summary of this function.

The short description spans multiple lines. It is indented.

Parameters
----------
param1 : int
    First parameter.
param2 : str
    Second parameter.
param3 : {'value', 'other'}, optional
    Third parameter. Default is 'value'.

Raises
------
NotImplementedError
    It hasn't been implemented yet.

Returns
-------
str
    A value in a string.
NoneType
    None.

Examples
--------
>>> example_func(42, 'example')
42
"""
    print(NumpydocParser().parse(ds))



# Generated at 2022-06-13 19:50:34.102870
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:50:46.624076
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:50:54.224437
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc = parse(
        """
        Short description.

        Docstrings may extend over multiple lines. Sections start with a header
        and are followed by a body, which are divided by a single newline.
        Everything is optional, including having multiple paragraphs.

        Parameters
        ----------
        arg1 : int
            The first argument.

        arg2 : str
            The second argument.

        Returns
        -------
        int
            The return value.
        """
    )

    assert isinstance(doc, Docstring)

    assert doc.short_description == "Short description."

    assert doc.long_description == "Docstrings may extend over multiple lines. Sections start with a header and are followed by a body, which are divided by a single newline. Everything is optional, including having multiple paragraphs."

    assert doc.blank_after_short_description is True

    assert doc

# Generated at 2022-06-13 19:51:01.613339
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    Numpydoc_Parser = NumpydocParser()
    text = "one\ntwo\nthree\n"
    ret = Numpydoc_Parser.parse(text)
    assert ret.short_description == "one"
    assert ret.long_description == "two\nthree"
    assert ret.blank_after_short_description == False
    assert ret.blank_after_long_description == False


# Generated at 2022-06-13 19:51:18.324119
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    t = """Deprecated :: version
            This function is deprecated
        Parameters
            arg1 : str
                A string
            arg2 : list
                An optional list
            arg3
                An optional argument with no type
        Returns
            returns_name : type
                A description of this returned value
            another_type
                Return names are optional, types are required
        """
    d = parse(t)
    assert d.short_description == None
    assert d.blank_after_short_description == False
    assert d.blank_after_long_description == False
    assert d.long_description == None
    assert len(d.meta) == 1
    assert isinstance(d.meta[0], DocstringDeprecated)
    assert d.meta[0].version == "version"