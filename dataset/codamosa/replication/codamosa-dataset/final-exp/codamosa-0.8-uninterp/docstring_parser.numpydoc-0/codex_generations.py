

# Generated at 2022-06-13 19:41:43.064537
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc = """
    .. title:: something
            possibly over multiple lines
    """
    ret = NumpydocParser().parse(doc)
    assert ret.short_description == None
    assert ret.long_description == None
    assert len(ret.meta) == 1
    assert type(ret.meta[0]) == DocstringMeta
    assert ret.meta[0].args[0] == 'see_also'
    assert ret.meta[0].description == 'something possibly over multiple lines'
    doc = """
    .. title:: something
            possibly over multiple lines
    ..Other::
    """
    ret = NumpydocParser().parse(doc)
    assert ret.short_description == None
    assert ret.long_description == None
    assert len(ret.meta) == 2
    assert type(ret.meta[0]) == Doc

# Generated at 2022-06-13 19:41:48.897397
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    with open("../data/deprecation.txt") as f:
        text = f.read()
        f.close()
    dep_sec = DeprecationSection("Deprecation Warning", "deprecation")
    doc_meta = list(dep_sec.parse(text))
    assert doc_meta[0].description == "Some value"
    assert doc_meta[0].version == "0.0.2"

# Generated at 2022-06-13 19:41:56.473903
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    test_section = inspect.cleandoc('''.. deprecated::
    0.1
    it's just a test''')
    test_section_without_description = inspect.cleandoc('''.. deprecated::
    0.1''')

    def test_section_parsing(section):
        meta = DeprecationSection("deprecated", "deprecation").parse(section)
        meta = next(meta)
        assert meta.description == "it's just a test"
        assert meta.version == "0.1"
        assert meta.args == ['deprecation']

    test_section_parsing(test_section)

    meta = DeprecationSection("deprecated", "deprecation").parse(test_section_without_description)
    meta = next(meta)
    assert meta.description is None
    assert meta

# Generated at 2022-06-13 19:41:58.749348
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    assert NumpydocParser().parse('').meta == [], "An empty docstring should return no metadata"


# Generated at 2022-06-13 19:42:07.133935
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    parser = NumpydocParser()
    parser.add_section(DeprecationSection("deprecated", "deprecation"))

    text = """
.. deprecated:: 1.2.0
    \tUse ``test`` instead of ``test2``, which is removed in verison ``1.4.0``.
    \tAlso ``test3`` is deprecated.
    """
    docstring = parser.parse(text)
    assert (len(docstring.meta) == 2)
    assert (docstring.meta[1].args[0] == "deprecation")
    assert (docstring.meta[1].description == "Use ``test`` instead of ``test2``, which is removed in verison ``1.4.0``. Also ``test3`` is deprecated.\n\n")

# Generated at 2022-06-13 19:42:15.472550
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    text = """
    .. deprecated:: 0.1.1

        This function is deprecated.

    """
    factory = DeprecationSection("deprecated", "deprecation")
    data = list(factory.parse(text))
    assert len(data) == 1
    assert data[0].args == ['deprecation']
    assert data[0].description == "This function is deprecated."
    assert data[0].version == "0.1.1"

# Generated at 2022-06-13 19:42:22.992475
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    NumpydocParser().parse("")
    NumpydocParser().parse("\n")
    NumpydocParser().parse("python parse method\n")
    NumpydocParser().parse("NumpydocParser().parse(\"\")\n")
    NumpydocParser().parse("NumpydocParser\n Parameters\n   Parameterslkjejfkl")



# Generated at 2022-06-13 19:42:26.757915
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    d = DeprecationSection("Deprecated", "deprecated")
    expected = [DocstringDeprecated(
        args=['deprecated'], description='Here is a description.', version='2.0'
    )]
    docstring = d.parse('2.0\n\n    Here is a description.')
    assert list(docstring) == expected



# Generated at 2022-06-13 19:42:35.949680
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Test text with no titles
    s = "Just some docstr"
    assert parse(s).short_description == s

    # Test text with title at the beginning
    s = "Title\n\nJust some docstr"
    assert parse(s).short_description is None
    assert parse(s).long_description == "Title\n\nJust some docstr"

    # Test text with title in the middle
    s = "Some docstr\n\nTitle\n\nMore docstr"
    assert parse(s).short_description == "Some docstr"
    assert parse(s).long_description == "Title\n\nMore docstr"

    # Test text with title at the end
    s = "Some docstr\n\nTitle"
    assert parse(s).short_description == "Some docstr"

# Generated at 2022-06-13 19:42:45.285666
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = """
    Summarize information about the process or its state

    This function is useful for printing the current value of simulation
    parameters in the output console.

    Parameters
    ----------
    t : float
        The time at which to print the report
    y : list
        The state of the system at time t
    args : dict
        Extra metadata to be included in the report.
    """
    doc = parser.parse(docstring)
    assert doc.short_description == "Summarize information about the process or its state"
    assert doc.long_description == "This function is useful for printing the current value of simulation\nparameters in the output console."
    assert doc.blank_after_short_description == True
    assert doc.blank_after_long_description == False

# Generated at 2022-06-13 19:43:03.308043
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = r"""Example function with types documented in the docstring.

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

    Raises
    ------
    KeyError
        When a key is not found.

    """
    ret = parse(text)
    assert ret.short_description == 'Example function with types documented in the docstring.'
    assert ret.blank_after_short_description
    assert ret.long_description == 'The first parameter.\n        The second parameter.'
    assert not ret.blank_after_long_description
    assert len(ret.meta) == 3
    assert type(ret.meta[0]) is DocstringParam

# Generated at 2022-06-13 19:43:14.359157
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:43:25.844004
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:43:36.877308
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import io
    from . import load
    from . import dumps

    # Setup
    test_file = io.StringIO(
        ".. deprecated:: 1.0\n    Because, reasons\n\n.. see_also::\n    * The standard library\n"
    )
    expected = Docstring(
        short_description="",
        long_description=None,
        meta=[
            DocstringDeprecated(
                args=["deprecation"],
                description="Because, reasons",
                version="1.0",
            ),
            DocstringMeta(
                args=["see_also"], description="* The standard library"
            ),
        ],
    )

    # Perform test
    result = load(test_file, parser=NumpydocParser())

    # Verify
    assert result == expected, dumps(result) == dumps

# Generated at 2022-06-13 19:43:45.165718
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
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

    Raises
    ------
    ValueError
        A description of what might raise ValueError

    """

    docstring = parse(text)
    # test the short description
    assert docstring.short_description == "Short description."

    # test the long description
    assert docstring.long_description == "Long description."
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == True

    # test meta


# Generated at 2022-06-13 19:43:56.388220
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    doc = """
    This is the short description.

    This is the first line of the long description.

    This is the second line of the long description.

    Parameters
    ----------
        param_1 : some type
            This is the first parameter.

        param_2 : some other type
            This is the second parameter.

    Returns
    -------
        bool
            This is the return value.

    Warning
    -------
        This is the warning.
    """
    docstring = parser.parse(doc)
    print(docstring)
    assert docstring.short_description == 'This is the short description.'
    assert docstring.long_description == 'This is the first line of the long description.\n\nThis is the second line of the long description.'

# Generated at 2022-06-13 19:44:03.588444
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """A short description.

    A long description which spans multiple lines.

    **kwargs : optional
        Keyword arguments.
        Can span multiple
        lines.

    Returns
    -------
    flag : bool (optional)
        Flag whether something was done.
    """

    docstring = NumpydocParser().parse(text)
    assert docstring.short_description == "A short description."
    assert docstring.long_description == "A long description which spans multiple lines."
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False

    # test empty docstring
    docstring_empty = NumpydocParser().parse("")
    assert docstring_empty.short_description == None
    assert docstring_empty.long_description == None
    assert docstring_

# Generated at 2022-06-13 19:44:05.362004
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    r = parser.parse("")
    assert "", r

# Generated at 2022-06-13 19:44:08.819435
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '/**\
    A function docstring.\
    ---\
    This is a unit test for method parse of class NumpydocParser\
    */'
    docstring = NumpydocParser().parse(text)
    assert isinstance(docstring, Docstring)


# Generated at 2022-06-13 19:44:16.257991
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:32.544890
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    txt = '''
    Parameters
    ----------
    arg : type
        A description of this parameter
    kwarg : type
        A description of this keyword argument
    Returns
    -------
    type
        A description of this return value
    Raises
    ------
    TypeError
        Some special cases might raise a TypeError
    '''

    p = NumpydocParser().parse(txt)

    assert p.long_description == txt
    assert p.meta[0].args == ['param', 'arg']
    assert p.meta[0].description == 'A description of this parameter'
    assert p.meta[0].type_name == 'type'

    assert p.meta[1].args == ['param', 'kwarg']
    assert p.meta[1].description == 'A description of this keyword argument'
    assert p

# Generated at 2022-06-13 19:44:43.115199
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:50.874912
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    s = NumpydocParser()
    docstring = """\
    Test Docstring

    Test Docstring
    """
    result = s.parse(docstring)
    assert result.short_description == 'Test Docstring'

    docstring = """\
    Test Docstring

    Test Docstring

    Test Docstring
    """
    result = s.parse(docstring)
    assert result.short_description == 'Test Docstring'

    docstring = """\
    Test Docstring

    Test Docstring

    :param arg1: Test Param
         Test Param\n\n
    """
    result = s.parse(docstring)
    assert result.meta[0].args[0] == 'param'


# Generated at 2022-06-13 19:44:58.899899
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .common import Docstring, DocstringDeprecated, DocstringMeta, DocstringParam, DocstringRaises, DocstringReturns
    text = """
    Short description.

    Long description.
    """
    parser = NumpydocParser()
    result = parser.parse(text)
    assert result == Docstring(short_description="Short description.", long_description="Long description.", meta=[])

    text = """
    Short description.

    :param arg: A parameter
    :rtype: Something
    """
    parser = NumpydocParser()
    result = parser.parse(text)

# Generated at 2022-06-13 19:45:10.052682
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # testing for numpydoc_parser.parse
    assert parse("") == Docstring()
    assert parse("   \n    ") == Docstring()
    assert parse("Foo") == Docstring(
        short_description=("Foo"),
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )
    assert parse("Foo\n") == Docstring(
        short_description=("Foo"),
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
        meta=[],
    )

# Generated at 2022-06-13 19:45:22.625755
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert parse("") == Docstring()


# Generated at 2022-06-13 19:45:25.553601
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    testString = '''
        """
        This is a test

        This is a longer description
        """
    '''

    result = NumpydocParser().parse(testString)

    assert result.short_description is None
    assert result.long_description is None
    assert result.blank_after_short_description is False
    assert result.blank_after_long_description is False

# Generated at 2022-06-13 19:45:35.420718
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # docstring without numpydoc parameters
    text = "This is a docstring"
    docstring = NumpydocParser()
    docstring.parse(text)
    assert docstring.short_description == text
    assert docstring.long_description == None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []

    # docstring with numpydoc parameters
    text = """This is a docstring
    Parameters:
        param: description of param
        param2: description of param2
    """
    docstring = NumpydocParser()
    docstring.parse(text)
    assert docstring.short_description == "This is a docstring"
    assert docstring.long_description == None
    assert docstring

# Generated at 2022-06-13 19:45:45.166948
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """\
Sample docstring

Note: This is a sample docstring.

Parameters
----------
a : optional
    An optional string.
    Default is '1'.

b : list, optional
    The second argument.

Returns
-------
dict
    A dictionary containing b"""
    result = NumpydocParser().parse(text)
    assert result.short_description == "Sample docstring"
    assert result.long_description == """\
Note: This is a sample docstring.

Parameters
----------
a : optional
    An optional string.
    Default is '1'.

b : list, optional
    The second argument.

Returns
-------
dict
    A dictionary containing b"""
    assert result.blank_after_short_description == True
    assert result.blank_after_long_description == False
    assert result

# Generated at 2022-06-13 19:45:51.585045
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = '''
    This is a short description.

    This is a
    long description.

    Parameters
    ----------
    arg1 : type
        description.
    arg2 : type, optional
        description.
    '''
    parse_result = parser.parse(text)
    assert parse_result.short_description == "This is a short description."
    assert parse_result.long_description == "This is a long description."
    assert len(parse_result.meta) == 2
    assert parse_result.meta[0].args == ["param", "arg1"]

# Generated at 2022-06-13 19:46:04.799131
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert NumpydocParser().parse("nothing here") == Docstring()

    test_docstring = NumpydocParser().parse("""
        Short description.

        Long description.

        Parameters
        ----------
        arg
            Describes argument.

        warn
            Describes warning.

        Other Parameters
        ----------------
        other_arg : type
            Describes other argument.

        Yields
        ------
        yields
            Describes yielding.
        """)

    assert test_docstring.short_description == "Short description."
    assert test_docstring.blank_after_short_description
    assert test_docstring.long_description == "Long description."
    assert test_docstring.blank_after_long_description

# Generated at 2022-06-13 19:46:15.548815
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = NumpydocParser().parse("""\
    First line.

    Second line.  Third line.  Fourth line.

    Parameters
    ----------
    arg1
        arg1's description.
    arg2
        arg2's description.  Continued.
    arg3 : type, optional
        arg3's description.  Continued.

    Raises
    ------
    ValueError
        Describes what raises ValueError.
    TypeError
        Describes what raises TypeError.

    Returns
    -------
    str
        Describes what returns.
    """)
    assert len(docstring.meta) == 3
    param_meta, raises_meta, returns_meta = docstring.meta[:3]
    assert param_meta.args == ["param"]
    assert returns_meta.args == ["returns"]
    assert raises_

# Generated at 2022-06-13 19:46:27.913824
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # instantiate class NumpydocParser
    np = NumpydocParser()
    test_docstring = """
    A docstring.

    Parameters
    ----------
    arg1 : str, optional
        The first argument.
    arg2 :
        The second argument.

    Returns
    -------
    None

    Other Parameters
    ----------------
    arg3 : int, optional
        Yet another argument.

    Raises
    ------
    RuntimeError
        Something went wrong.

    Examples
    --------
    >>> x = 1

    See Also
    --------
    astropy.nddata.support_nddata

    .. note:: you can add notes to your docstring
    .. todo:: and todos too!

    """
    docstring = np.parse(test_docstring)

# Generated at 2022-06-13 19:46:38.213322
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    _parser = NumpydocParser()
    test_docstring = """
        This is a Title
        -------------

        Short description.

        Long description.

        Attributes
        ----------

            an_attr
                The first attribute.

                This attribute takes a very long time to explain.

            another_attr : str
                The second attribute.

        Warning
        -------

            This function requires careful use.

        Blabla
        -----

            It is important to have a blank line after warning.
        """
    _docstring = _parser.parse(test_docstring)

    assert _docstring.short_description == "Short description."
    assert _docstring.long_description == "Long description."
    assert _docstring.blank_after_short_description == True
    assert _docstring.blank_after_long_description == True
   

# Generated at 2022-06-13 19:46:40.239049
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # TODO: need to write unit test for method parse of class NumpydocParser
    pass



# Generated at 2022-06-13 19:46:47.497803
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    input = """
    :param a: this is a param
    :param b: this is another param
    :param c: c
              c c
              c c
    :param d: d
    :param e: e
    :param f: f
    :param g: g
    :returns: returns something
    """
    a = NumpydocParser()
    a.parse(input)

# Generated at 2022-06-13 19:46:59.140214
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:47:12.381200
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc = """
    This is the short description.

    This is the long description.
    It can go over multiple lines.

    Parameters
    ----------
    arg_name : str
        This is the arg_name argument.
        It can also span multiple lines.
    arg_2 : int
        This is the arg_2 argument.

    Returns
    -------
    str
        This is the return type.

    """
    parser = NumpydocParser()

# Generated at 2022-06-13 19:47:21.297699
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # assertEqual(toBeTestedInstance.parse(text), expectedResult, "Message in case of error")
    numpydocParser = NumpydocParser()
    text = '''

Returns:
    True if the objects are the same type and have the same value.
    False otherwise.
    '''
    docstring = numpydocParser.parse(text)
    expected = Docstring(short_description=None, long_description=None, meta=[DocstringMeta(['returns'], description='True if the objects are the same type and have the same value.\nFalse otherwise.')])
    assert expected == docstring, "Expected result is not correct"
    text = '''
    Examples:
    >>> 'hello' == 'bye'
    False
    >>> 'hello' == 'hello'
    True
    '''

# Generated at 2022-06-13 19:47:31.109388
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import re

    text = """\
    Parse the numpy-style docstring into its components.

    :returns: parsed docstring

    Examples:
        The following is an example::

            >>> example_parse('test numpydoc parsing')
            NumpydocResult(description='test numpydoc parsing', meta=[...])

    .. deprecated:: 0.3
        This method is deprecated.
        Replaced by :func:`numpydoc.parse`.
    """

    docstring = NumpydocParser().parse(text)

    # test description
    if not docstring.short_description == 'Parse the numpy-style docstring into its components.':
        raise Exception('short_description should be \'Parse the numpy-style docstring into its components.\' but is {}'.format(docstring.short_description))



# Generated at 2022-06-13 19:47:45.646880
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """Numpydoc-style docstring parsing.

.. seealso:: https://numpydoc.readthedocs.io/en/latest/format.html

Parameters
----------
param1 : int
    Description of parameter `param1`.
param2 : :obj:`list` of :obj:`str`
    Description of parameter `param2`, which has a rather long
    description.

Raises
------
IndexError
    If index is out of range.
RuntimeError
    If some other error occurred.

Returns
-------
int
    The value between `low` and `high` inclusive.
"""
    parser = NumpydocParser()
    docstring = parser.parse(text)
    assert len(docstring.meta) == 3

# Generated at 2022-06-13 19:47:57.025180
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_parse_text = '''One line summary.
    More detailed description.
    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2
    Returns
    -------
    int
        Description of return value.
    '''
    test_case = NumpydocParser().parse(test_parse_text)
    assert test_case.short_description == 'One line summary.'
    assert test_case.long_description == 'More detailed description.'
    assert test_case.meta[0].args[0] == 'param'
    assert test_case.meta[0].args[1] == 'arg1'
    assert test_case.meta[0].description == 'Description of arg1'
    assert test_case.meta[0].arg_name == 'arg1'

# Generated at 2022-06-13 19:48:09.890891
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """A numpy-style docstring (:term:`NumPy style).

    Parameters
    ----------
    first : str
        The first description, can also span...
        ... multiple lines

    second : str
        The second description.

    Returns
    -------
    str
        The parsed docstring, in a format easily...
        ... convertible to other formats.

    See Also
    --------
    :class:`Docstring`
    """

    parser = NumpydocParser()
    parsed = parser.parse(docstring)
    assert not parsed.blank_after_short_description
    assert not parsed.blank_after_long_description
    assert parsed.short_description == "A numpy-style docstring (:term:`NumPy style)."

# Generated at 2022-06-13 19:48:19.551547
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:48:24.045357
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """This is the text for the docstring.
It can be long and span across lines.

Parameters
----------
a : int
    The first parameter.
b : str
    The second parameter.

Returns
-------
x : list
    The returned list.
y : tuple
    The returned tuple.
"""
    d = NumpydocParser().parse(text)
    assert len(d.meta) == 3
    assert d.meta[0].key == 'param'
    assert d.meta[1].key == 'param'
    assert d.meta[2].key == 'returns'
    assert d.meta[2].args[0] == 'returns'
    assert len(d.meta[2].args) == 1

# Generated at 2022-06-13 19:48:36.133420
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = inspect.cleandoc("""
    This is the short description.

    This is the long description.  It is longer
    than the short description.

    Parameters
    ----------
    a : int
        The first argument.
    b : int, optional
        The second argument.  Defaults to 42.

    Warnings
    --------
    .. warning::
        There's nothing that can be done here.
    """)

    result = NumpydocParser().parse(text)

    assert result.short_description == "This is the short description."
    assert result.long_description.startswith("This is the long description")

    assert len(result.meta) == 2
    assert result.meta[0].args == ["param", "a"]
    assert result.meta[1].args == ["warnings"]



# Generated at 2022-06-13 19:48:46.129495
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydoc_parser = NumpydocParser()

# Generated at 2022-06-13 19:48:57.070368
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This is a short description of this method.
    This is a long description of this method.
    It can split over multiple lines.

    Parameters
    ----------
    arg_name : type, optional
        A long description for this argument. It can also split over multiple
        lines.
    arg_name2 : type or None, optional
        Default "default_value". Another description.
    Raises
    ------
    ValueError
        A description of what might raise ValueError.
    Returns
    -------
    return_name : type
        A description of this returned value.
    Yields
    ------
    return_name : type
        A description of this yielded value.
    """
    from . import Docstring

# Generated at 2022-06-13 19:49:07.113136
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:49:18.981074
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_data1 = """
    test parse 1

    Parameters
    ----------
    arg1 : str
        arg1 description
    arg2 : int, optional
        arg2 description

    Returns
    -------
    str
        return description

    Raises
    ------
    ValueError
        if something
    """
    test_data2 = """
    test parse 2

    Parameters
    ----------
    arg1
        arg1 description

    Returns
    -------
    str, optional
        return description

    Raises
    ------
    ValueError
        if something
    """

    test_data3 = """
    test parse 3

    Parameters
    ----------
    arg1 : int
        arg1 description

    Returns
    -------
    str
        return description

    Raises
    ------
    Exception
        if something
    """

   

# Generated at 2022-06-13 19:49:33.231352
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    ndp = NumpydocParser()
    test_docstring = '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
    result = ndp.parse(test_docstring)
    # test that the str representation of the result is the string that was parsed
    assert str(result) == test_docstring
    # test that the str representation of the long description of the result has the same number of lines as the test docstring
    assert len(str(result.long_description).split('\n')) == len(test_docstring.split('\n'))
    # test that the long description is 'None'
    assert result.long_description is None
    # test that the short description is 'None'
    assert result.short

# Generated at 2022-06-13 19:49:39.392309
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc = NumpydocParser()
    doc_string = doc.parse('''
        test_NumpydocParser_parse
            (Bool) Return true if it succeedes
        ''')
    assert doc_string.short_description == 'test_NumpydocParser_parse'
    assert doc_string.long_description == '(Bool) Return true if it succeedes'


# Generated at 2022-06-13 19:49:53.159267
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:50:01.906372
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:50:03.798195
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    NumpydocParser().parse("""Notes
    -----
    test""")


# Generated at 2022-06-13 19:50:12.288140
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:50:17.345498
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text_input = """
    One-line summary.

    More detailed summary, which can contain newlines.
    """

    text_output = Docstring(
        short_description="One-line summary.",
        blank_after_short_description=True,
        long_description="More detailed summary, which can contain newlines.",
        blank_after_long_description=True,
        meta=[],
    )
    assert parse(text_input) == text_output

# Generated at 2022-06-13 19:50:23.027061
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Required argument ``my_test_function`` must be a function.
    If you want to use the default, pass None.
    
    Parameters
    ----------
    my_test_function : None or callable
        This is my test function.
    
    Returns
    -------
    out : bool
        Description of return value
    """

# Generated at 2022-06-13 19:50:32.376188
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    text = '''
        :param a: This is param a
        :param b: This is param b
        :param c: This is param c(optional)
        :param d: This is param d(optional)
        :param e: This is param e, default is 10
        '''
    numpydoc_parser = NumpydocParser()
    docstring = numpydoc_parser.parse(text)
    assert type(docstring.meta) == list
    assert len(docstring.meta) == 5
    assert docstring.meta[-1].arg_name == 'e'
    assert docstring.meta[-1].default == '10'
    # Change the title of last parameter
    last_section = ParamSection("Other Args", "other_param")

# Generated at 2022-06-13 19:50:45.215782
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser(sections=DEFAULT_SECTIONS)

    def check_parse(dct, **kwargs):
        assert parser.parse(dct).__dict__ == kwargs

    def sphinx_section(section, title, key, text):
        return (
            f".. {title}:: {section}\n"
            f"    {text}\n"
            "\n"
        )

    # no tags - only description
    check_parse("Some text.", short_description="Some text.")
    check_parse("\nSome\nlong\ndescription\n.", long_description="Some\nlong\ndescription")

# Generated at 2022-06-13 19:51:02.633940
# Unit test for constructor of class _KVSection
def test__KVSection():
    assert '_KVSection'


# Generated at 2022-06-13 19:51:06.162727
# Unit test for constructor of class _SphinxSection
def test__SphinxSection():
    assert _SphinxSection(".. title:: something\nposiblly over multiple lines", "key").title


# Unit testing for constructor of class _KVSection

# Generated at 2022-06-13 19:51:11.373177
# Unit test for constructor of class YieldsSection
def test_YieldsSection():
    yield_section = YieldsSection("Yields","yields")
    assert(yield_section.is_generator == True)
    yield_section.is_generator = False
    assert(yield_section.is_generator == False)


# Generated at 2022-06-13 19:51:13.036109
# Unit test for constructor of class DeprecationSection
def test_DeprecationSection():
    assert DeprecationSection("deprecated", "deprecation") is not None


# Generated at 2022-06-13 19:51:18.652273
# Unit test for constructor of class _SphinxSection
def test__SphinxSection():
    # test successful match
    section = _SphinxSection("Parameters", "param")
    assert section.title_pattern == "^\.\.\s*(Parameters)\s*::"

    # test failed match
    section = _SphinxSection("Parameters", "param")
    with pytest.raises(AssertionError):
        section.title_pattern == "^\.\.\s*(Parameters):?"
