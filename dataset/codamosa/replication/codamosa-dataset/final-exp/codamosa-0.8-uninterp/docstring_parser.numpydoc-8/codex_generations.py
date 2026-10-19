

# Generated at 2022-06-13 19:42:03.808467
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    Test the method NumpydocParser.parse
    :return:
    """
    parser = NumpydocParser()
    params = parser.parse("""
    This is a description.

    Parameters
    ----------
    arg1: int, optional
        First argument.
    arg2: float
        Second argument.

    """
    )

    assert params.meta[0].args == ['param', 'arg1']
    assert params.meta[0].description == 'First argument.'
    assert params.meta[0].arg_name == 'arg1'
    assert params.meta[0].default is None
    assert params.meta[0].is_optional
    assert params.meta[0].type_name == 'int'

    assert params.meta[1].args == ['param', 'arg2']
    assert params.meta

# Generated at 2022-06-13 19:42:07.409465
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    text = 'deprecated:: 0.4.0\n This function is deprecated.'
    section = DeprecationSection('deprecated', 'deprecation')
    docstring = section.parse(text)
    assert list(docstring).pop().description == 'This function is deprecated.'



# Generated at 2022-06-13 19:42:12.640289
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    dep = DeprecationSection("deprecated","deprecation")
    dep_res = dep.parse("1.0" + "\n" + "Deprecated Method")
    assert dep_res[0].version is not None
    assert dep_res[0].description is not None

# Generated at 2022-06-13 19:42:25.602514
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # text = '''
    #     Docstring for func::
    #
    #         short description
    #
    #         extended description
    #
    #         Returns
    #         -------
    #         list
    #             returns a list
    #         void
    #             returns nothing
    # '''
    text = '''
    Docstring for func::

        short description

        extended description

        Returns
        -------
        returns a list

    '''
    docstring = NumpydocParser().parse(text)
    assert docstring.short_description == 'short description'
    assert docstring.long_description == 'extended description'
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description
    assert docstring.meta[0].args == ['returns', '']


# Generated at 2022-06-13 19:42:35.200376
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Test the parser method of class NumpydocParser"""

# Generated at 2022-06-13 19:42:42.590651
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text_1 = """
    This is short description.

    This is long description. It can span over multiple lines.

    Parameters
    ----------
    arg_1
        This is description of arg_1.
    arg_2 : type, optional
        By default it is None. Default: None. This is description of arg_2.

    Returns
    -------
    out : np.ndarray
        Description of returned value.

    Raises
    ------
    TypeError
        If something goes wrong.
    """
    actual_1 = parse(text_1)

# Generated at 2022-06-13 19:42:46.878036
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    """Test method DeprecationSection.parse()"""
    content = """.. deprecated:: 1.6
    Support for this feature has been deprecated and will be removed in a later
    version.
"""
    result = DeprecationSection("deprecated", "deprecation").parse(content)
    expected = [DocstringDeprecated(args=["deprecation"], description=None, version="1.6")]
    assert result == expected


# Generated at 2022-06-13 19:42:53.089603
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    text = ".. deprecated:: 1.4\n   Replaced by :func:`bar`.\n"
    assert parse(".. deprecated:: 1.4\n" + "   Replaced by :func:`bar`.\n") == NumpydocParser().parse(".. deprecated:: 1.4\n" + "   Replaced by :func:`bar`.\n")
    assert parse(".. deprecated:: 1.4\n" + "   Replaced by :func:`bar`.\n").meta.args[0] == "deprecation"
    assert parse(".. deprecated:: 1.4\n" + "   Replaced by :func:`bar`.\n").meta.description == "Replaced by :func:`bar`."

# Generated at 2022-06-13 19:43:02.408650
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert parse("") == Docstring()

    doc = Docstring(
        short_description="My sweet function",
        long_description="func that does a thing.\n\n    Args:\n        val (int): val",
        meta=[
            DocstringParam(
                args=["param", "val"],
                description="val",
                arg_name="val",
                type_name="int",
                is_optional=False,
            ),
        ],
    )

    assert parse("My sweet function") == doc._replace(
        long_description=None,
        blank_after_short_description=False,
        blank_after_long_description=False,
    )

    assert parse("My sweet function\n\nArgs:\n        val (int): val") == doc


# Generated at 2022-06-13 19:43:05.107882
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    assert list(DeprecationSection('', '').parse('')) == [DocstringMeta(['deprecation'], None, None)]


# Generated at 2022-06-13 19:43:18.550663
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc = \
"""
One line summary

This is an extended description

foo : int
    description of foo

Attributes
    description of foo

Raises:
    ValueError: If a value is not of the expected format (e.g.,
        not an int).
    TypeError: If a value is of the wrong type

    .. deprecated:: 0.9
        Use :class:`~.SomethingClass` instead.
"""
    parser = NumpydocParser()
    docstring = parser.parse(doc)
    assert docstring.short_description == "One line summary"
    assert docstring.long_description == "This is an extended description"
    assert docstring.meta[0].__class__ == DocstringParam
    assert docstring.meta[0].args[0] == "param"

# Generated at 2022-06-13 19:43:29.341663
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print("Testing unit test for method parse of class NumpydocParser")
    
    parser = NumpydocParser()
    docstring = parser.parse("""
        adds `addend` to the value, and returns a new instance

        Parameters
        ----------
        addend : :class:`mul_name`
            the value to add
        mulend : :class:`mul_name`, optional
            another value to multiply the first by,
            defaulting to 2
    """)
    assert docstring
    print("test_NumpydocParser_parse: ", docstring.meta[0].args)
    assert docstring.meta[0].args == ["param", "addend"], "test_NumpydocParser_parse"

# Generated at 2022-06-13 19:43:41.229610
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = """\
    Parameters
    ----------
    arg_1
        Description of arg_1
    arg_2 : type
        Description of arg_2

    Raises
    ------
    KeyError
        When a key error

    """
    docstring = parser.parse(text)
    assert len(docstring.meta) == 2
    assert docstring.meta[0].args == ["param", "arg_1"]
    assert docstring.meta[1].args == ["raises", "KeyError"]
    assert docstring.meta[1].first_line == "When a key error"


# Unit tests for method parse of class NumpydocParser

# Generated at 2022-06-13 19:43:48.060380
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """
        Hello, world.

        This is a long
        description.

        Parameters
        ----------
        name : str, optional
            This is a long parameter description
            which spans multiple lines.

        value : int
            This is a long parameter description
            which spans multiple lines.

        Raises
        ------
        ValueError
            This is a long exception description,
            which spans multiple lines.

        See Also
        --------
        This is a long :doc:`reference`
        which spans multiple lines.
        """

    ndp = NumpydocParser()
    ret = ndp.parse(docstring)


# Generated at 2022-06-13 19:43:58.709513
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    # Test deprecation warning
    text = """
    .. deprecated:: 2.0

       Rewrite ``astropy.io.ascii.read()`` to use astropy.io.asciio.read()
    """
    assert parser.parse(text).meta[0] == DocstringMeta(['deprecation'],
        description='Rewrite ``astropy.io.ascii.read()`` to use astropy.io.asciio.read()',
        version='2.0')

    # Test one-line description
    text = """
    Short description.

    Parameters
    ----------
    arg1 : str
    arg2 : int
    """
    assert parser.parse(text).short_description == 'Short description.'

    # Test short description followed by blank line

# Generated at 2022-06-13 19:44:06.461399
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_cases = [
        (
            """
        :param a: 1
        :param b: 2
                """,
            {"a": 1, "b": 2},
        )
    ]

    for test_case in test_cases:
        docstring = NumpydocParser().parse(test_case[0])
        docstring_params = {
            param.arg_name: param.default
            for param in docstring.meta
            if param.key == "param"
        }
        assert docstring_params == test_case[1]

# Generated at 2022-06-13 19:44:11.378383
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = '''
    This is the short description.
    
    This is the long description.  The long description
    can be several lines.
    
    Parameters
    ----------
    arg1 : int
        Description of `arg1`
    
    arg2 : str
        Description of `arg2`
    '''
    docstring = NumpydocParser().parse(docstring)
    assert docstring.short_description == 'This is the short description.'
    assert docstring.long_description == 'This is the long description.  The long description\n    can be several lines.'
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == True
    assert len(docstring.meta) == 1

# Generated at 2022-06-13 19:44:19.229119
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydoc_parser = NumpydocParser()
    docstring = numpydoc_parser.parse(
        """\
        A function to parse the numpy-style docstring into its components.

        Parameters
        ----------
        text: str
            Text of a docstring to parse.

        Returns
        -------
        Docstring
            Parsed docstring.

        Warnings
        --------
        All parameters are required.
        """
    )
    assert isinstance(docstring, Docstring)
    assert docstring.short_description == (
        "A function to parse the numpy-style docstring into its components."
    )
    assert docstring.blank_after_short_description is True
    assert docstring.long_description is None
    assert docstring.blank_after_long_description is False

    meta = docstring

# Generated at 2022-06-13 19:44:27.572280
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
    Parse the numpy-style docstring into its components.

    Parameters
    ----------
    text : str
        The docstring to parse.

    Returns
    -------
    Docstring
        The parsed docstring
    '''
    assert NumpydocParser().parse(text).meta[0].args == ('param', 'text')


if __name__ == "__main__":
    test_NumpydocParser_parse()

# Generated at 2022-06-13 19:44:35.866644
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:48.778537
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:56.809073
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

# Generated at 2022-06-13 19:45:03.545068
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_input = """
    Brief description.

    More detailed description.

    Parameters
    ----------
    param1 : type
        Descriptions can span multiple lines
    param2
        Parens within type names (for numpy dtypes) are ignored.
        If a parameter has no type, this syntax is ignored.

    Returns
    -------
    return_1 : type
        Descriptions can span multiple lines.
    """

# Generated at 2022-06-13 19:45:14.325985
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    s = "test test"
    docstring = NumpydocParser().parse(s)
    assert docstring.short_description == "test test"
    assert docstring.long_description is None
    assert docstring.meta == []
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False

    s = "test test\n\nmore tests"
    docstring = NumpydocParser().parse(s)
    assert docstring.short_description == "test test"
    assert docstring.long_description == "more tests"
    assert docstring.meta == []
    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is False

    s = "test test\nmore tests\n\n"


# Generated at 2022-06-13 19:45:23.539992
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    # doctest for method parse of class NumpydocParser
    def _test_parse(text, obj):
        assert parse(text) == obj

    # Test case for one line docstring

    text1 = """
        a test docstring
        """
    obj1 = Docstring(
        long_description="a test docstring",
        short_description="a test docstring",
        blank_after_long_description=True,
        blank_after_short_description=True,
        meta=[],
    )

    # Test case for long description with a blank line following the short description

    text2 = """
        a test docstring

        And a long description
        """

# Generated at 2022-06-13 19:45:32.434713
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text1 = """
    Some description.

    Parameters
    ----------
    ``param`` : {'linear', 'poly', 'rbf', 'sigmoid', 'cosine', 'precomputed'}, optional (default='rbf')
        Kernel.

    Returns
    -------

    """

    text2 = """
    Some description.

    Parameters
    ----------
    ``param`` : {'linear', 'poly', 'rbf', 'sigmoid', 'cosine', 'precomputed'}, optional (default='rbf')
        Kernel.

    Returns
    -------
    ``return1`` : bool
        If true then True , else False

    """

    text3 = """Some description."""


# Generated at 2022-06-13 19:45:37.768546
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    class C:
        """
        test short
        test long


        Parameters
        ----------
            param1 : str
                description 1
                description 2
            param2 : int
                description 3

        Returns
        -------
            str
                description 4

        """

    m = parse(C.__doc__)
    print(m)

# Generated at 2022-06-13 19:45:46.524297
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .common import Docstring
    ds = NumpydocParser().parse("""\
    Short description

    Long description is over multiple
    lines.

    Parameters
    ----------
    arg1 : str
        First required argument.
    arg2 : int, optional
        Second optional argument. Default is 1.

    Returns
    -------
    None
    """)

# Generated at 2022-06-13 19:45:57.890995
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    #
    # Test for parameters section
    #
    # first parameter is optional and has a default value
    text = """
    Title of class

    Parameters
    ----------
    param : str
        first parameter

    param_2 : int(optional)
        second parameter

    param3 : float=3.0
        third parameter has defaults
    """
    r = NumpydocParser().parse(text)
    assert r.meta[0].args == ["param", "param"]
    assert r.meta[0].description == "first parameter"
    assert r.meta[1].args == ["param", "param_2"]
    assert r.meta[1].description == "second parameter"
    assert r.meta[1].type_name == "int"
    assert r.meta[1].is_optional

# Generated at 2022-06-13 19:46:03.752257
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    # Test short description parsing
    short_description = "short description"
    assert parse(short_description).short_description == short_description

    # Test long description parsing
    long_description = "long description"
    assert parse("{}\n{}".format(short_description, long_description)).long_description == long_description

    # Test blank_after_short_description parsing
    assert parse("{}\n{}".format(short_description, long_description)).blank_after_short_description == True
    assert parse("{} {}".format(short_description, long_description)).blank_after_short_description == False

    # Test blank_after_long_description parsing
    assert parse("{}\n{}".format(short_description, long_description)).blank_after_long_description == False

# Generated at 2022-06-13 19:46:12.928991
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc = """
    """

    docstring = NumpydocParser().parse(doc)
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert not docstring.blank_after_short_description
    assert not docstring.blank_after_long_description
    assert docstring.meta == []



# Generated at 2022-06-13 19:46:19.614590
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Documentation for the namedtuple
    text = """\
    A single side of a card game. A card game consists
    of a collection of CardSide.

    Parameters
    ----------
    name : CardSideName
        The name of the side.
    image_fn : str
        The file name of the image to use for this side
    is_hidden : bool
        True if the side is hidden from the user (default True)
    """

    ds = NumpydocParser().parse(text)
    assert ds.short_description == "A single side of a card game."
    assert (
        ds.long_description == "A card game consists of a collection of CardSide."
    )
    assert ds.blank_after_short_description
    assert ds.blank_after_long_description


# Generated at 2022-06-13 19:46:30.138411
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .common import DocstringReturns
    from .common import DocstringParam
    from .common import Docstring
    from .common import DocstringRaises

    # test empty docstring
    assert NumpydocParser().parse("") == Docstring()
    # test docstring with short description only
    assert NumpydocParser().parse("Test") == Docstring(short_description="Test")
    # test docstring with short description and long description
    assert NumpydocParser().parse("Test\n\nTest test") == Docstring(
        short_description="Test",
        long_description="Test test",
        blank_after_short_description=True,
        blank_after_long_description=False,
    )
    # test docstring with short description, long description and meta information

# Generated at 2022-06-13 19:46:36.235432
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:46:42.479891
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This is a short description.

    This is a long description.

    .. deprecated: 0.3
        Replaced by :func:`other_function`.

    .. warning::

        This is a warning issued by the function.

    Parameters
    ----------
    param_str : str
        A str parameter.

    param_int : int
        An int parameter.

    param_tuple : tuple
        A tuple parameter.

    param_default : int, optional
        This parameter defaults to 0.

    param_list : list, optional
        This parameter defaults to [0].

    param_optional : int, optional
        This parameter is optional.

    param_none : int, optional
        This parameter is set to None by default.

    Returns
    -------
    int
        The greatest common divisor.
    """
    doc

# Generated at 2022-06-13 19:46:46.861349
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Regression test for #13
    desc = 'Some description of the function'
    ret = Docstring(
        short_description=desc,
    )
    assert NumpydocParser().parse(desc) == ret


# Generated at 2022-06-13 19:46:51.658058
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    parser.parse("""arg_name
                   arg_description
                   arg_2 : type, optional
                   descriptions can also span...
                   ... multiple lines""")

# Generated at 2022-06-13 19:47:01.366443
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """\
    Divide a number by zero.

    This function is used to divide numbers by zero repeatedly.

    Parameters
    ----------
    dividend : float
        The number to be divided by zero.
    output : OutputFormat, optional
        The result of the division by zero.
        The default is `OutputFormat.INTEGER`.

    Returns
    -------
    int
        The result of the division by zero.
    """
    d = NumpydocParser().parse(text)
    p = Docstring()
    p.short_description = "Divide a number by zero."
    p.blank_after_short_description = True
    p.blank_after_long_description = True
    p.long_description = (
        "This function is used to divide numbers by zero repeatedly."
    )

# Generated at 2022-06-13 19:47:14.434307
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_text = """
    This is an example docstring.

    Parameters
    ----------
    arg1 : int
        The first parameter.
    arg2 : str
        The second parameter.

    Returns
    -------
    int
        An integer return value.

    Raises
    ------
    ValueError
        If something goes wrong.
    """

    doc = parse(test_text)

    for name in [
        "short_description",
        "long_description",
        "blank_after_short_description",
        "blank_after_long_description",
    ]:
        assert getattr(doc, name) is not None

    assert doc.long_description == "The second parameter."
    assert doc.meta[0].type_name == "int"
    assert doc.meta[1].type_name == "str"


# Generated at 2022-06-13 19:47:22.208569
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = """
    This is the first line
    and the second one

    Parameters
    ----------
    arg1 : type
        arg1 description
    arg2 : {'first', 'second'}
        arg2 description

    Returns
    -------
    return_name : type
        return description
    """
    docstring_parsed = parser.parse(docstring)
    assert docstring_parsed.short_description == "This is the first line and the second one"
    assert docstring_parsed.long_description is None
    assert docstring_parsed.blank_after_short_description == True
    assert docstring_parsed.blank_after_long_description == False

# Generated at 2022-06-13 19:47:34.855378
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

# Generated at 2022-06-13 19:47:46.552265
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    docstring = """
    Test numpy-style docstring parsing.

    Parameters
    ----------
    text: str
        text to parse
    name: str
        name of parsed string
    """

# Generated at 2022-06-13 19:47:57.914981
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:48:10.550027
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text="""\
        This is a docstring
        Second paragraph

        Parameters
        ----------
        param1 : str
            A str param
        other_param : str, optional
            Default is 'test'
        Parameter without type

        Raises
        ------
        ValueError
            This method raises ValueError
        TypeError
            On bad input type

        Returns
        -------
        int
            The param count

        Example
        -------
        >>> foo(3)
        6
        >>> foo("hello")
        Traceback (most recent call last):
            ...
        ValueError: invalid value

        """

    result = NumpydocParser().parse(text)
    assert result.short_description == 'This is a docstring'
    assert result.long_description == 'Second paragraph'
    assert result.blank_after_short_description

# Generated at 2022-06-13 19:48:20.025277
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print('\n\nUnit test for method parse of class NumpydocParser...\n')

    def parse_numpydoc(text: str) -> Docstring:
        return NumpydocParser().parse(text)

    assert parse_numpydoc("") == Docstring()
    assert parse_numpydoc("No titles.") == Docstring(
        short_description="No titles."
    )
    assert parse_numpydoc("\nNo titles with blank line.\n\n") == Docstring(
        short_description="No titles with blank line.",
        blank_after_short_description=True,
        blank_after_long_description=True,
        long_description="",
    )
    assert parse_numpydoc("\nNo titles with blank line.\n\nMore long.") == Docstring

# Generated at 2022-06-13 19:48:24.866496
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Short description.
    
    Long description.
    
    Parameters
    ----------
    arg_name
        arg desc
    arg_2 : int, optional
        more arg desc
    arg_3 : (3, 4), optional
        more arg desc
    arg_4
        arg desc
    
    Returns
    -------
    return_name : str
        return desc
    """
    docstr = NumpydocParser().parse(text)
    assert docstr.short_description == "Short description."
    assert docstr.long_description == "Long description."
    assert docstr.blank_after_short_description is True
    assert docstr.blank_after_long_description is False
    assert len(docstr.meta) == 1

# Generated at 2022-06-13 19:48:35.671022
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydoc_parser = NumpydocParser()
    sample_text = """
    sample description text
    Parameters
    ----------
    sample_parameter_name : type
        sample parameter description
    """
    parsed = numpydoc_parser.parse(sample_text)
    # (1) assert that the short description is parsed correctly
    assert(parsed.short_description == "sample description text")
    # (2) assert that the first meta element has the parsed parameter name
    assert(parsed.meta[0].args[1] == "sample_parameter_name")
    # (3) assert that the first meta element has the parsed parameter type
    assert(parsed.meta[0].type_name == "type")
    return parsed

# Generated at 2022-06-13 19:48:37.140051
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Should not raise any exception
    NumpydocParser().parse('')

# Generated at 2022-06-13 19:48:43.280084
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from ..utils import clean_whitespace
    parser = NumpydocParser()
    method_docstring = """Short description.
    Long description.
    """
    returned = parser.parse(method_docstring)
    expected = clean_whitespace("""Docstring(short_description='Short description.', long_description='Long description.', meta=[])""")
    assert clean_whitespace(f"{returned}") == expected

# Generated at 2022-06-13 19:48:45.260466
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .parser_tests import TestParserBase
    TestParserBase.test_class_parse(NumpydocParser)



# Generated at 2022-06-13 19:49:00.228758
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    class TempSection(_KVSection):
        def _parse_item(self, key: str, value: str) -> DocstringMeta:
            return DocstringMeta(["param"], description=_clean_str(value))

    temp = TempSection("Parameters", "param")

# Generated at 2022-06-13 19:49:09.749970
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:49:20.318711
# Unit test for constructor of class _KVSection
def test__KVSection():
    _KVSection('Parameters', 'param')
    _KVSection('Params', 'param')
    _KVSection('Arguments', 'param')
    _KVSection('Args', 'param')
    _KVSection('Other Parameters', 'other_param')
    _KVSection('Other Params', 'other_param')
    _KVSection('Other Arguments', 'other_param')
    _KVSection('Other Args', 'other_param')
    _KVSection('Receives', 'receives')
    _KVSection('Receive', 'receives')
    _KVSection('Raises', 'raises')
    _KVSection('Raise', 'raises')
    _KVSection('Warns', 'warns')

# Generated at 2022-06-13 19:49:22.003794
# Unit test for constructor of class ReturnsSection
def test_ReturnsSection():
    assert ReturnsSection.is_generator == False


# Generated at 2022-06-13 19:49:23.435081
# Unit test for constructor of class NumpydocParser
def test_NumpydocParser():
    assert NumpydocParser().__init__(sections)


# Generated at 2022-06-13 19:49:29.106480
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    text = r'''
        TypeError
            A description of what might raise TypeError
        KeyError
            A description of what might raise KeyError
        ValueError
            A description of what might raise ValueError
    '''
    a = RaisesSection('Raises', 'raises')
    b = a.parse(text)
    print(len(a.sections))



# Generated at 2022-06-13 19:49:38.450115
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    text = """.. deprecated:: 6.0.0

        Support for deprecated :py:func:`~.foo` will be removed in version 6.0.0.
    """
    factory = DeprecationSection("deprecated", "deprecation")
    result = factory.parse(text)
    result_list = list(result)
    assert len(result_list) == 1
    result = result_list[0]
    assert result.version == "6.0.0"
    assert result.description == "Support for deprecated :py:func:`~.foo` will be removed in version 6.0.0."

# Generated at 2022-06-13 19:49:40.393458
# Unit test for constructor of class ParamSection
def test_ParamSection():
    assert ParamSection("A", "b")


# Generated at 2022-06-13 19:49:45.902945
# Unit test for constructor of class ReturnsSection
def test_ReturnsSection():
    x = ReturnsSection("Returns", "returns")
    assert x.title == "Returns"
    assert x.key == "returns"
    assert x.is_generator == False
    # Can't test regular expression without having a partially compiled one
    #assert x.title_pattern == _ReturnsSection.title_pattern

# Generated at 2022-06-13 19:49:49.860127
# Unit test for constructor of class Section
def test_Section():
    a = Section("a", "b")
    assert a.title == "a"
    assert a.key == "b"
    assert a.title_pattern == r"^(a)\s*?\n\-+\s*$"

# Generated at 2022-06-13 19:50:02.669870
# Unit test for constructor of class RaisesSection
def test_RaisesSection():
    text_1 = '''
    .. deprecated:: 3.2.1
        Use ``a.b`` instead.
    '''
    text_2 = '''
    raise ValueError
        A description of what might raise ValueError
    '''
    text_3 = '''
    ValueError
        A description of what might raise ValueError
    '''
    text_4 = '''
    Exception
    '''
    text_5 = '''
    Warns
        A description of what might cause a warning
    '''
    text_6 = '''
    warn ValueError
        A description of what might raise ValueError
    '''
    text_7 = '''
    .. seealso::
        :meth:`~.RaisesSection.parse`
    '''

# Generated at 2022-06-13 19:50:06.167823
# Unit test for constructor of class _SphinxSection
def test__SphinxSection():
    section = _SphinxSection('title', 'key')
    assert section.title == 'title'
    assert section.key == 'key'
    assert section.title_pattern == "^\.\.\s*(title)\s*::"


# Generated at 2022-06-13 19:50:11.028213
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    kvtext = """
        key
            value
        key2 : type
            values can also span...
            ... multiple lines
    """
    kvtext = inspect.cleandoc(kvtext)
    kvsection = _KVSection("key", "key")
    kvsection.parse(kvtext)



# Generated at 2022-06-13 19:50:13.758182
# Unit test for method add_section of class NumpydocParser
def test_NumpydocParser_add_section():
    p = NumpydocParser()
    s = Section("TEST", "TEST")
    p.add_section(s)
    assert p.sections["TEST"] == s

# Generated at 2022-06-13 19:50:16.549828
# Unit test for constructor of class ReturnsSection
def test_ReturnsSection():
    ret = ReturnsSection("Returns",'return')
    print(ret.is_generator)


# Generated at 2022-06-13 19:50:25.014130
# Unit test for method parse of class Section
def test_Section_parse():
    # Testing the insides of a section object.
    section = Section('Attributes', 'attributes')
    text = '''
            attr1
                des1
            attr2 : type
                des2

            Attributes:
                attr1: des1
                attr2: des2
        '''
    expected = [
        DocstringMeta(['attributes', 'attr1'], description='des1'),
        DocstringMeta(['attributes', 'attr2'], description='des2')
    ]
    assert list(section.parse(text)) == expected

# Generated at 2022-06-13 19:50:26.505417
# Unit test for constructor of class DeprecationSection
def test_DeprecationSection():
    assert DeprecationSection("deprecation", "deprecation")



# Generated at 2022-06-13 19:50:33.975441
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    section = DeprecationSection("Deprecated", "deprecated")
    text = """.. deprecated:: 1.5
            This is deprecated
        """
    doc_list = section.parse(text)
    doc = list(doc_list)[0]
    
    assert doc.description == "This is deprecated"
    assert doc.version == "1.5"
    assert doc.args == ["deprecated"]
    
    # Test with empty description
    text = """.. deprecated:: 1.5
        """
    doc_list = section.parse(text)
    doc = list(doc_list)[0]
    
    assert doc.description is None
    assert doc.version == "1.5"
    assert doc.args == ["deprecated"]
    
    return

# Generated at 2022-06-13 19:50:46.538383
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    from io import StringIO
    from sphinx_toolbox import numpydoc_parse

    print("Starting test for method parse of class DeprecationSection")

    # Create an instance of class DeprecationSection
    section = numpydoc_parse.DeprecationSection("deprecated", "deprecation")

    # Create a string object to be parsed
    string_to_parse = """.. deprecated:: 0.1.0
        Use :class:`FancyClass` instead."""

    # Parse the string
    results = section.parse(string_to_parse)

    # Print the deterministic data 
    print("factory = ", section)
    print("string_to_parse = ", string_to_parse)
    print("results = ", results)

    # Print the nondeterministic data

# Generated at 2022-06-13 19:50:50.360801
# Unit test for method parse of class Section
def test_Section_parse():
    from .common import DocstringMeta
    from .numpydoc import Section

    S = Section("title","key")
    text = 'key1\n    value1\nkey2 : type\n    value2'
    assert list(S.parse(text)) == [DocstringMeta([S.key],description='value1'),DocstringMeta([S.key],description='value2')]


# Generated at 2022-06-13 19:51:01.892638
# Unit test for constructor of class _SphinxSection
def test__SphinxSection():
    # test for title_pattern
    assert _SphinxSection(title='hello', key='world').title_pattern == '^\.\.\s*(hello)\s*::'
    return


# Generated at 2022-06-13 19:51:13.669591
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    test_docstring = r'''First line of docstring.
        Second line.

        Parameters
        ----------
        arg1 : str
            First argument.

        arg2 : type, optional
            Second argument. Default is 2.

        Returns
        -------
        None
            Return none.'''