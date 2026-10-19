

# Generated at 2022-06-13 19:41:40.682059
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    # Given
    deprecation_section = DeprecationSection("deprecated", "deprecation")
    deprecation_body = "0.0.3\n    Some message\n    next line"
    deprecation_docstring = DocstringDeprecated(args=[
        deprecation_section.key], description="Some message\nnext line",
        version="0.0.3")

    # When
    deprecation_meta = list(deprecation_section.parse(deprecation_body))

    # Then
    assert deprecation_meta == [deprecation_docstring]

# Generated at 2022-06-13 19:41:43.938387
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    kv_text = '''
        key
            value
        key2 : type
            values can also span...
            ... multiple lines
    '''
    section = _KVSection("Params", "param")
    result = list(section.parse(kv_text))

    assert len(result) == 2
    assert result[0].description == 'value'
    assert result[1].description == 'values can also span...\n... multiple lines'

# Generated at 2022-06-13 19:41:47.442605
# Unit test for method parse of class Section
def test_Section_parse():
    section = ParamSection("test", "somekey")
    p = NumpydocParser([section])
    assert p.parse("test\n---").meta == [DocstringMeta(["somekey"])]


# Generated at 2022-06-13 19:41:56.128910
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    t1 = "Bug\n  This is a bug."
    t2 = "Bug    This is a bug."
    t3 = "Bug: This is a bug."

    section = _KVSection("Bug", "bug")
    result = list(section.parse(t1))
    assert len(result) == 1
    assert result[0].args == ["bug"]
    assert result[0].description == "This is a bug."

    section = _KVSection("Bug", "bug")
    result = list(section.parse(t2))
    assert len(result) == 1
    assert result[0].args == ["bug"]
    assert result[0].description == "This is a bug."

    section = _KVSection("Bug", "bug")
    result = list(section.parse(t3))

# Generated at 2022-06-13 19:42:02.910277
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    section_parser = DeprecationSection("deprecated", "deprecation")
    text = """
    .. deprecated:: version

        This is a deprecation warning.
    """
    text = inspect.cleandoc(text)
    assert(section_parser.parse(text)[0].args==['deprecation'])
    assert(section_parser.parse(text)[0].description=="This is a deprecation warning.")
    assert(section_parser.parse(text)[0].version=="version")

# Generated at 2022-06-13 19:42:05.577780
# Unit test for method parse of class Section
def test_Section_parse():
    s = Section("Title", "key")
    assert list(s.parse("text")) == [DocstringMeta(["key"], "text")]



# Generated at 2022-06-13 19:42:10.261588
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    def test_function(p1, p2):
        """Loads the requested sample from the list of currently available
        testing samples.

        Parameters
        ==========
        p1 : str
            parameter 1
        p2 : str, optional
            parameter 2

        Returns
        =======
        tuple
            (param1, param2)
        """
        pass

    print(parse(inspect.getdoc(test_function)))

# Generated at 2022-06-13 19:42:16.310951
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    actual = list(_KVSection("", "").parse("""
        key
            value
        key2 : type
            values can also span...
            ... multiple lines"""))
    expected = [("key", "value"), ("key2 : type", "values can also span...")]
    assert actual == expected


# Generated at 2022-06-13 19:42:24.225725
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    text = ".. deprecated:: 1.2.3\n    This is deprecated\n"
    g = DeprecationSection("deprecated", "deprecation")
    results = list(g.parse(text))
    assert len(results) == 1
    assert results[0].args == ['deprecation']
    assert results[0].description == "This is deprecated"
    assert results[0].version == "1.2.3"

# Generated at 2022-06-13 19:42:33.678666
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    class DeprecationSection:
        @staticmethod
        def parse(text: str) -> T.Iterable[DocstringDeprecated]:
            version, desc, *_ = text.split(sep="\n", maxsplit=1) + [None, None]

            if desc is not None:
                desc = _clean_str(inspect.cleandoc(desc))

            yield DocstringDeprecated(
                args=[self.key], description=desc, version=_clean_str(version)
            )

    assert DeprecationSection.parse('--deprecated--\nDeprecated since version 3.2.0') == DocstringDeprecated(['--deprecated--'],  'Deprecated since version 3.2.0',  version='--deprecated--')

# Generated at 2022-06-13 19:42:44.007417
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    text = """
    key
        value
    key2 : type
        values can also span...
        ... multiple lines
     """
    assert list(ParamSection("Parameters", "param").parse(text)) == [
        DocstringMeta(["param", "key"], description="value"),
        DocstringMeta(["param", "key2"], description="values can also span...\n... multiple lines"),
    ]


# Generated at 2022-06-13 19:42:51.107382
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    # A value without keywords
    content = """
    a
        b
    c
        d
    """
    docstring = parse(content)
    assert docstring.meta[0].args == ["a"]
    assert docstring.meta[0].description == "b"
    assert docstring.meta[1].args == ["c"]
    assert docstring.meta[1].description == "d"

    # A value with keywords
    content = """
    a: b
        c
    d: e
        f
    """
    docstring = parse(content)
    assert docstring.meta[0].args == ["a:b"]
    assert docstring.meta[0].description == "c"
    assert docstring.meta[1].args == ["d:e"]
    assert docstring.meta[1].description == "f"

# Generated at 2022-06-13 19:42:59.910753
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    doc = Docstring()
    doc.short_description = 'Testing...'
    doc.long_description = 'Testing long description...'
    doc.blank_after_short_description = False
    doc.blank_after_long_description = False
    doc.meta = [
        DocstringMeta(['param', 'height'], 'Description...'),
        DocstringMeta(['param', 'width'], 'Description...')
    ]
    s = 'Testing...\n\nTesting long description...\n\nParameters\n----------\n\nheight\n    Description...\nwidth : int\n    Description...'
    assert NumpydocParser().parse(s) == doc

# Generated at 2022-06-13 19:43:11.986626
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Short description
    
    Long description
    
    Parameters
    ----------
    alpha : int
        description of alpha
       
    beta : str
        description of beta
    
    gamma : str, optional
        description of gamma
    
    Attributes
    ----------
    attr1 : str
        attribute 1
    
    attr2 : str
        attribute 2
    
    Returns
    -------
    str
        return description
    """
    obj = NumpydocParser().parse(text)
    assert isinstance(obj, Docstring)
    assert obj.short_description == "Short description"
    assert obj.long_description == "Long description"
    param1 = obj.meta[0]
    assert isinstance(param1, DocstringParam)
    assert param1.args == ['param', 'alpha']

# Generated at 2022-06-13 19:43:19.747091
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:43:30.245019
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    txt = """
    Sample docstring:

    Args:
        arg_1 (type, optional): Description may span multiple lines
        arg_2 (type): Description can also span multiple lines
        arg_3 (type): Description does not necessarily span lines

    Attributes:
        attr_1 (type): Description for an attribute
        attr_2 (type): Description for another attribute, with *markup*

    Returns (type): Description can span multiple lines

    Warns:
        UserWarning: If the user does something silly, they'll be warned.

    Raises:
        ValueError: If the function gets invalid input, we'll raise a ValueError
        NotImplementedError: There is no method for the given input
    """
    res = parse(txt)
    assert res.short_description is None
    assert res.long_description is None


# Generated at 2022-06-13 19:43:43.032274
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    """
    Test for the _KVSection class' parse function.
    """
    # PASS
    text = """
    name : type
        Description of the parameter.

    name2 : type2
        Description of the parameter.
    """
    test_section = _KVSection('title', 'key')

    result = list(test_section.parse(text))

# Generated at 2022-06-13 19:43:47.106437
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    section = _KVSection("title", "key")
    # Simple test case
    text = inspect.cleandoc("""
        arg_name
            arg_description
        arg_2 : type, optional
            descriptions can also span...
            ... multiple lines
        """)
    meta = section.parse(text)
    assert len(list(meta)) == 2
    # Test that multiline descriptions are parsed correctly
    desc = list(section.parse(text))[1].description
    assert desc[-6:] == "lines"



# Generated at 2022-06-13 19:43:57.767675
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:44:04.666699
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    parser = _KVSection('Parameters', 'parameters')
    docstring = """
    Parameters
    ----------
    a_param
        param_description
    b_param : str
        description
        can span multiple lines
    """
    parsed = parser.parse(docstring)
    assert next(parsed).args == ['parameters', 'a_param']
    assert next(parsed).args == ['parameters', 'b_param']


# Generated at 2022-06-13 19:44:17.760605
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    np = NumpydocParser()
    text = """Brief description.

This is a rather long
description of something that
we want to do here.

It can even contain enumerations:

    item 1

    item 2

.. note:: This is a note.

And we can add a reference...

.. [1] See me.

"""
    result = np.parse(text)
    assertion = isinstance(result, Docstring)
    assert assertion
    assert result.short_description == "Brief description."
    assert result.long_description == "This is a rather long\ndescription of something that\nwe want to do here.\n\nIt can even contain enumerations:\n\n    item 1\n\n    item 2"
    assert result.blank_after_short_description
    assert not result.blank_

# Generated at 2022-06-13 19:44:31.626425
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    ndp = NumpydocParser()
    assert ndp.parse("") == Docstring()
    assert ndp.parse("a") == Docstring(short_description='a', long_description=None,
                                       blank_after_long_description=None,
                                       blank_after_short_description=False,
                                       meta=[])
    assert ndp.parse("a\nb") == Docstring(short_description='a', long_description='b',
                                          blank_after_long_description=False,
                                          blank_after_short_description=False,
                                          meta=[])

# Generated at 2022-06-13 19:44:41.979250
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

# Generated at 2022-06-13 19:44:47.986610
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    if __name__ == "__main__":
        parser = NumpydocParser()
        parser.parse("""
                Function description

                Parameters
                ----------
                a : int
                    a number.
                b : str, optional
                    a string.

                Raises
                ------
                ValueError
                    If a is negative or b is too long.

                Returns
                -------
                result
                    The result of the calculation.

                Example
                -------
                >>> print(test_function(1, 'a'))
                """
        )

# Generated at 2022-06-13 19:44:56.264229
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:45:03.060662
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
        unit test for method parse of class NumpydocParser.

        Parameters
        ----------
            test_param1 : bool
                test bool param

        Returns
        -------
            test_returns : str
                test returns str

        Raises
        ------
            ValueError
                test raises ValueError

        Examples
        --------
            test_examples

        Warnings
        --------
            test_warnings

        See Also
        --------
            test_See_Also

        Related
        -------
            test Related

        Notes
        -----
            test_Notes

        References
        ----------
            test_References

        deprecated
        ----------
            test_deprecated
        """
    parsed = NumpydocParser().parse(text)

# Generated at 2022-06-13 19:45:14.017576
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = '''
    No return_type and no return_description in this docstring
    '''
    docstring_expected = {
        'short_description': 'No return_type and no return_description in this docstring',
        'long_description': None,
        'blank_after_short_description': True,
        'blank_after_long_description': None,
        'meta': []
    }
    numpy_parser = NumpydocParser()
    docstring_actual = numpy_parser.parse(docstring)
    assert docstring_actual == docstring_expected

    docstring = '''
    :return: The new array with the dimensions and data content of the input array
    '''

# Generated at 2022-06-13 19:45:23.249822
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:45:25.180269
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert (parse("Hellow World")) == Docstring(short_description='Hellow World', meta=[])


# Generated at 2022-06-13 19:45:33.448763
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:45:45.599092
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = """\
    Short description.

    Long description.

    Parameters
    ----------
    arg1 : int
        Name of the first argument.
    arg2 : str
        Name of the second argument.
    """
    docstring = parser.parse(text)
    # ensure we get a Docstring
    assert isinstance(docstring, Docstring)
    # ensure we get a parsed Docstring
    assert docstring.short_description
    assert docstring.long_description
    assert docstring.meta
    assert len(docstring.meta) == 1
    assert docstring.meta[0].args[0] == "param"
    assert docstring.meta[0].args[1] == "arg1"
    assert docstring.meta[0].type_name == "int"

# Generated at 2022-06-13 19:45:47.732846
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Returns: parsed docstring
    # Returns: parsed docstring
    assert parse(" ") == Docstring()
    assert parse("") == Docstring()

# Generated at 2022-06-13 19:45:58.877969
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """\
        Deprecated:: 0.3.0
            Deprecation version
        Warnings
            Something might happen...
        Parameters
            arg1 : str
                First arg

            arg2 : int, optional
                Second arg
        Returns
            int
                return value
        Yields
            str
                generator value
        Raises
            ValueError
                if stuff goes wrong
        """
    docstring = NumpydocParser().parse(text)
    assert docstring.short_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.long_description is None
    assert docstring.blank_after_long_description is True
    assert len(docstring.meta) == 7

    assert docstring.meta[0].args == ["deprecation"]

# Generated at 2022-06-13 19:46:04.024597
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
        Asserts that no message is logged by the given logger.
    '''

    # case description
    ret = NumpydocParser().parse(text)
    assert ret.short_description == 'Asserts that no message is logged by the given logger.'


# Generated at 2022-06-13 19:46:14.868145
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

# Generated at 2022-06-13 19:46:27.529371
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .formatters import NumpydocFormatter
    from .render import render_docstring

    doctext = """
    Single line description.

    Multiple lines description
    that goes on for a while.
    Does not need to end with empty line.

    Parameters
    ----------
    foo : int
        Some description.
    bar : str = 'BAR'
        Some other description
        with a linebreak.
    baz : int (optional)
        Another description.
    qux : str, optional
        Yet another description with
        a linebreak.

    """

    docdict = parse(doctext)
    assert docdict["short_description"] == "Single line description."

# Generated at 2022-06-13 19:46:37.927753
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    Unit test for method parse of class NumpydocParser
    """
    # Invalid cases
    # Case 1
    res = NumpydocParser().parse(None)
    assert res.short_description == None
    assert res.long_description == None
    assert res.blank_after_long_description == False
    assert res.blank_after_short_description == False
    assert len(res.meta) == 0
    # Case 2
    res = NumpydocParser().parse("")
    assert res.short_description == None
    assert res.long_description == None
    assert res.blank_after_long_description == False
    assert res.blank_after_short_description == False
    assert len(res.meta) == 0
    # Case 3

# Generated at 2022-06-13 19:46:46.717443
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:46:49.714562
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = parser.parse(text)



# Generated at 2022-06-13 19:46:59.682016
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    # Test single line description
    text = "Description"
    parsed_text = parser.parse(text).short_description
    assert parsed_text == "Description"

    # Test multi-line description
    text = """Description
    Another description"""
    parsed_text = parser.parse(text).long_description
    assert parsed_text == "Another description"

    # Test that 'short_description' value is None if no description is given
    text = "Parameters:\n arg : type\n    Description"
    parsed_text = parser.parse(text).short_description
    assert parsed_text is None

    # Test that 'long_description' value is None if no description is given
    text = """Description
    Parameters:\n arg : type\n    Description"""

# Generated at 2022-06-13 19:47:14.338954
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Test doc strings parsing."""

# Generated at 2022-06-13 19:47:22.152538
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Test case 1
    docstring_text = """\
    Short docstring

    Long docstring
    """
    expected = Docstring(
      short_description="Short docstring",
      long_description="Long docstring",
      blank_after_short_description=True,
      blank_after_long_description=False,
    )
    assert NumpydocParser().parse(docstring_text) == expected

    # Test case 2
    docstring_text = """\
    Short docstring

    Long docstring

    """
    expected = Docstring(
      short_description="Short docstring",
      long_description="Long docstring",
      blank_after_short_description=True,
      blank_after_long_description=True,
    )
    assert NumpydocParser().parse(docstring_text) == expected

# Generated at 2022-06-13 19:47:31.590657
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    # Test basic parsing
    text = '''
    Short description.

    Long description.

    Parameters
    ----------
    arg1 : str
        arg1 description.
    arg2 : type (optional)
        arg2 description.
        Default is 'default'.
    arg3, optional
        arg3 description.
        Default is 1.
    arg4 : :class:`Class`
        arg4 description.

    Keyword Arguments
    -----------------
    karg1 : bool
        karg1 description.

    Returns
    -------
    str
        return description.
    '''

    result = parser.parse(text)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert len(result.meta) == 4

# Generated at 2022-06-13 19:47:36.922747
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = 'Numpy style docstring parser\n'
    text += '\n'
    text += 'Parameters\n'
    text += '----------\n'
    text += 'text : string\n'
    text += '    Text to parse\n'
    text += '\n'
    text += 'Returns\n'
    text += '-------\n'
    text += 'docstring : Docstring\n'
    text += '    Parsed docstring\n'

    ds = NumpydocParser().parse(text)
    assert ds.short_description == 'Numpy style docstring parser'
    assert ds.long_description == ''
    assert ds.blank_after_short_description == True
    assert ds.blank_after_long_description == False
    assert len(ds.meta) == 2

# Generated at 2022-06-13 19:47:47.356249
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test1 = \
    """
    This function does something great.

    Parameters
    ----------
    arg1 : str
        The first argument.
    arg2 : bool, optional
        The second argument.

    Returns
    -------
    bool
        True if successful, False otherwise.
    """
    test2 = ""
    test3 = "A short description"
    test4 = \
    """
    This function does something great.

    First line of longer description

    Second line of longer description

    Parameters
    ----------
    arg1 : str
        The first argument.
    arg2 : bool, optional
        The second argument.

    Returns
    -------
    bool
        True if successful, False otherwise.
    """

# Generated at 2022-06-13 19:47:58.485395
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydoc_parser = NumpydocParser()
    docstring = numpydoc_parser.parse('Function that returns a value.\n\nParameters\n----------\narg1 : str\n    The first argument.\narg2 : int, optional\n    The second argument.\n\nReturns\n-------\nstr\n    The return value.\n')
    assert docstring.short_description == "Function that returns a value."
    assert docstring.long_description is None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == True
    docstring.meta[0].args == [
        "param",
        "arg1",
    ]
    docstring.meta[0].type_name == "str"

# Generated at 2022-06-13 19:48:03.037814
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .common import Docstring
    txt = """\
    It's like a :class:`~._Vec2D`, except we use a namedtuple
    instead of a tuple, so we have x and y attributes instead of
    indexes.

    Attribute ``xy`` is a read-only alias for ``tuple(self)``.

    :param scalar: Object to be promoted to :class:`~._Vec2D`.
    :return: New :class:`~._Vec2D` instance.
        
        """
    assert type(parse(txt)) == Docstring

# Generated at 2022-06-13 19:48:15.022271
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    str = '''
    Parameters
    ----------
    param : {'a', 'b'}, optional
        The parameter \`param\` of this query.
        Allowed values are:

        - 'a': This is the letter "a".

        - 'b': This is the letter "b".

    Returns
    -------
    str
        This query's result.
    '''

    doc = NumpydocParser().parse(str)

# Generated at 2022-06-13 19:48:31.217859
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .utils import print_meta_info
    parser = NumpydocParser()
    test_docstring = """
    Parses the numpydoc docstring into its components.

    :returns: parsed docstring

    Parameters
    ----------
    text : str
        the docstring text

    Returns
    -------
    Docstring
        parsed docstring

    Raises
    ------
    ParserException
        if the docstring is not parsable

    Attributes
    ----------
    short_description : str
        short description
    long_description : str
        long description
    blank_after_short_description : bool
        whether there is a blank line after the short description
    blank_after_long_description : bool
        whether there is a blank line after the long description
    meta : list
        meta-data components
    """
    print

# Generated at 2022-06-13 19:48:39.784365
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = """Short description.

    Long description. It can span
    multiple lines.

    Parameters
    ----------
    arg_name
        arg_description
    param_name : type, optional
        param_description

    Returns
    -------
    return_name : return_type
        -- return_description
    """
    ret = parser.parse(text)
    assert len(ret.meta) == 2
    assert len(ret.meta[0]) == 3
    assert len(ret.meta[1]) == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-13 19:48:50.496981
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

# Generated at 2022-06-13 19:48:55.970530
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    f_numpydoc = '/Users/shulin/test/test_parse.py'
    with open(f_numpydoc) as f:
        text = f.read()
        ds = NumpydocParser().parse(text)


if __name__ == "__main__":
    test_NumpydocParser_parse()

# Generated at 2022-06-13 19:49:04.976157
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    This function tests if the NumpydocParser can parse all types of strings.
    
    :return: 1 if successful, 0 otherwise.
    """
    parser = NumpydocParser()

# Generated at 2022-06-13 19:49:11.097648
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Case when there is only short description
    text = "Short description"
    expected_short_description = "Short description"
    expected_meta = []
    test_obj = NumpydocParser()
    assert test_obj.parse(text).short_description == expected_short_description
    assert test_obj.parse(text).meta == expected_meta
    # Case when there is only short description and meta
    text = "Short description \nParameters \nmy_param : type \nLong description"
    expected_short_description = "Short description"
    expected_meta = [DocstringMeta(["param", "my_param"], description="Long description", arg_name="my_param", type_name="type")]
    test_obj = NumpydocParser()
    assert test_obj.parse(text).short_description == expected_short

# Generated at 2022-06-13 19:49:21.085658
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    def assert_text_docstring_parse(text, expected_result):
        result = NumpydocParser().parse(text)
        assert isinstance(result, Docstring), "@NumpydocParser.parse returned wrong type"
        
        assert result.short_description == expected_result.short_description, \
            "@NumpydocParser.parse short_description mismatch"
        
        assert result.blank_after_short_description == expected_result.blank_after_short_description, \
            "@NumpydocParser.parse blank_after_short_description mismatch"
        
        assert result.blank_after_long_description == expected_result.blank_after_long_description, \
            "@NumpydocParser.parse blank_after_long_description mismatch"
        
        assert result.long_description == expected_result.long

# Generated at 2022-06-13 19:49:31.422048
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:49:42.240106
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:49:54.038594
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    np = NumpydocParser()
    docstring = """Calculates the sum of numbers

    Parameters
    ----------
    a: int, array_like
        Number(s) to be added
    b: int, optional
        Another number to be added
    c: int, array_like
        Another set of numbers to be added

    Raises
    ------
    TypeError
        if unable to convert to list

    Returns
    -------
    list_sum: int
        Sum of numbers

    Other Parameters
    ----------------
    repeat: bool
        Flag to repeat calculation

    References
    ----------
    https://docs.python.org/3/library/functions.html#sum
    """
    result = np.parse(docstring)
    assert result.short_description == "Calculates the sum of numbers"
    assert result.blank

# Generated at 2022-06-13 19:50:02.699813
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    One-line summary of the object.
    
    Extended summary, which can contain multiple paragraphs.
    
    Parameters
    ----------
    arg_name : str
        standard argument
    arg_2 : str, optional
        optional argument
    arg_3 : str
        Another one
    
    See Also
    --------
    `See also`_ documentation.
    
    Examples
    --------
    Examples be good.
    """
    npp = NumpydocParser()
    npp.add_section(ParamSection("New", "new"))
    ret = npp.parse(text)
    
    assert ret.short_description == "One-line summary of the object."
    assert ret.long_description == \
        "Extended summary, which can contain multiple paragraphs."
    assert ret.blank_after_short_

# Generated at 2022-06-13 19:50:13.116394
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:50:28.500017
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This is a short description

    This is a long description. It can span multiple lines
    and contain almost arbitrary text.

    .. deprecated:: 3.2
       Deprecated warning, spanning multiple lines.

    Other Parameters
    ----------------
    arg_name : type, optional
        arg_description
        with multiple lines
    arg_2 : type
        A second argument. Listing more than one is
        optional.

    Returns
    -------
    returns_name : type
        return_description
    another_type
        Return names are optional, types are required

    Raises
    ------
    ValueError
        A description of what might raise ValueError

    Examples
    --------
    >>> foo(42)
    1337

    References
    ----------
    [1] http://example.com
    """

# Generated at 2022-06-13 19:50:40.213394
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .common import DocstringMeta, DocstringParam, DocstringReturns, DocstringRaises, DocstringDeprecated

# Generated at 2022-06-13 19:50:51.288110
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:50:58.763723
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    assert parser.parse("") == Docstring()
    assert (
        parser.parse("function(a, b)")
        == Docstring(
            short_description="function(a, b)",
            long_description=None,
            blank_after_short_description=False,
            blank_after_long_description=False,
            meta=[],
        )
    )
    assert (
        parser.parse("function(a, b)\n")
        == Docstring(
            short_description="function(a, b)",
            long_description=None,
            blank_after_short_description=True,
            blank_after_long_description=True,
            meta=[],
        )
    )

# Generated at 2022-06-13 19:51:12.386377
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # test short and long description: short description only
    text1 = """short description"""
    assert NumpydocParser().parse(text1) == Docstring(short_description="short description")

    # test short and long description: long description only
    text2 = """
    long description
    """
    assert NumpydocParser().parse(text2) == Docstring(long_description="long description")

    # test short and long description: short and long descriptions
    text3 = """
    short description

    long description
    """
    assert NumpydocParser().parse(text3) == Docstring(short_description="short description", long_description="long description")

    # test large long description: neither long nor short description
    text4 = """
        """