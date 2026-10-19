

# Generated at 2022-06-13 19:41:52.162941
# Unit test for method parse of class _KVSection
def test__KVSection_parse():
    test_string = """
    key
        value
    key2 : type
        values can also span...
        ... multiple lines
    """
    section = _KVSection("test", "test")
    result = section.parse(test_string)
    expected_result = [DocstringMeta(["test", "key"], description='value'), 
                       DocstringMeta(["test", "key2"], description='values can also span...\n... multiple lines')]
    assert result == expected_result


# Generated at 2022-06-13 19:42:02.287492
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:42:06.733662
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    text = ".. deprecated:: 0.9\n    .. deprecated:: 1.0\n    Deprecated test"
    doc = NumpydocParser().parse(text)
    print(doc.meta)
    assert doc.meta[0].args[2] == "1.0"
    assert doc.meta[0].args[1] == None
    assert doc.meta[0].args[0] == "deprecation"
    assert doc.meta[0].description == 'Deprecated test'

# Generated at 2022-06-13 19:42:14.879244
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    text = '.. deprecated:: version.0\n'
    text = text + '   deprecated description'
    factory = DeprecationSection('deprecated', 'deprecation')
    expected = DocstringDeprecated(
            args=['deprecation'], description='deprecated description', version='version.0')
    result = factory.parse(text)
    assert next(result).__dict__ == expected.__dict__


# Generated at 2022-06-13 19:42:20.202136
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    """Test the method parse of class DeprecationSection."""
    text = """
.. deprecated:: 0.5
   The interface is deprecated."""
    result = NumpydocParser().parse(text)
    assert result.meta[0].description == "The interface is deprecated."


# Generated at 2022-06-13 19:42:28.150938
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    short desc

    long desc
    that spans
    multiple lines

    Raises
        ValueError
            when a bad input is given
        TypeError
            when a bad input is given.

    Returns
        This method returns None
    """
    result = NumpydocParser().parse(text)
    assert result.short_description == "short desc"
    assert result.long_description == "long desc\nthat spans\nmultiple lines"
    assert result.blank_after_short_description is True
    assert result.blank_after_long_description is True
    assert isinstance(result.meta[0], DocstringRaises)
    assert isinstance(result.meta[1], DocstringRaises)
    assert isinstance(result.meta[2], DocstringReturns)


# Generated at 2022-06-13 19:42:33.335488
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    parsedDocstring = Docstring()
    parsedDocstring.meta.append( 
        DocstringDeprecated(
            args=['deprecated'], description="test description", version=None
        )
    )
    assert NumpydocParser(
        sections = [DeprecationSection("deprecated", "deprecation")]
    ).parse(".. deprecated::\n   test description\n") == parsedDocstring

# Generated at 2022-06-13 19:42:42.540491
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:42:50.703301
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser_1 = NumpydocParser(DEFAULT_SECTIONS)
    assert parser_1.parse(text="") == Docstring()
    parser_2 = NumpydocParser(DEFAULT_SECTIONS)
    assert parser_2.parse(text="Methode qui permet d'ajouter des poissons") == Docstring(short_description="Methode qui permet d'ajouter des poissons")
    assert parser_2.parse(text="Methode qui permet d'ajouter des poissons").short_description == "Methode qui permet d'ajouter des poissons"
    assert parser_2.parse(text="Methode qui permet d'ajouter des poissons").long_description == None

# Generated at 2022-06-13 19:43:00.825759
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_docstring = '''
    Example docstring.

    The first paragraph is a short summary and is not indented.

    The second paragraph starts with a blank line, and belongs to the
    long description.  The long description starts immediately after the
    second paragraph and extends up to the first blank line that precedes
    the next paragraph (or the end of the docstring).
    The second paragraph is indented to match the first line of the first
    paragraph, and any subsequent paragraphs are similarly indented.  The
    short summary ends at the first blank line.

    Parameters
    ----------
    arg1 : int
        Description of `arg1` (with type).

    Returns
    -------
    int
        Description of return value.
    '''
    # calling the 'parse' method with the above docstring instance as the
    # docstring parameter.
   

# Generated at 2022-06-13 19:43:10.535393
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This is a description.
    This is a description.
    This is a description.
    This is a description.
    This is a description.

    This is another description.

    Parameters
    ----------
    arg1 : arg
        description
    arg2 : arg
        description
    arg3 : arg
        description
        description
        description
        description
        description
        description

    """

    assert parse(text).short_description=='This is a description.'
    assert parse(text).long_description=='This is another description.'
    assert parse(text).blank_after_long_description==True
    assert parse(text).blank_after_short_description==True
    assert len(parse(text).meta)==3



# Generated at 2022-06-13 19:43:18.981617
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    code = """
    Check that the test works.

    :param param1: The first parameter.
    :type param1: int
    :param param2: The second one.
    :returns: None
    :rtype: None
    """
    p = NumpydocParser()
    result = p.parse(code)
    assert result.short_description == 'Check that the test works.'
    assert result.long_description == 'The second one.'
    assert len(result.meta) == 4
    assert result.meta[0].args == ['param', 'param1']
    assert result.meta[0].description == 'The first parameter.'
    assert result.meta[1].args == ['type', 'param1']
    assert result.meta[1].description == 'int'

# Generated at 2022-06-13 19:43:29.680657
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert parse("") == Docstring()
    assert parse("\n").meta == Docstring().meta
    assert parse("hello").short_description == "hello"
    assert parse("hello\nworld").long_description == "world"
    assert parse("hello\n\nworld").long_description == "world"
    assert parse("hello\n\nworld\n").long_description == "world"
    assert parse("hello\nworld\n\n").long_description == "world"
    assert parse("hello\n\n\nworld\n\n\n").long_description == "world"
    assert parse("hello\nworld\n\n").short_description == "hello"
    assert parse("hello\n\nworld\n\n\n").short_description == "hello"

# Generated at 2022-06-13 19:43:42.792703
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc = parse("""
        First line
        Second line.

        Parameters
        ----------
        args : str, optional
            An optional argument.
        kwarg : str, optional
            A keyword argument.

        Returns
        -------
        str
            A return value.
        """)

    assert doc.short_description == "First line\nSecond line."
    assert doc.long_description is None
    assert doc.blank_after_short_description
    assert not doc.blank_after_long_description
    assert len(doc.meta) == 2
    assert doc.meta[0] == DocstringParam(
        args=["param", "args"],
        description="An optional argument.",
        type_name="str",
        is_optional=True,
        arg_name="args",
    )

# Generated at 2022-06-13 19:43:48.533447
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    class A:
        """Given a start_time and an end_time,
        and optionally a resolution,
        return a dict of lists of datetime objects on the given
        resolution.

        Parameters
        ----------
        start_time: datetime
            Starting time for the query
        end_time: datetime
            Ending time for the query
        resolution: int, optional
            Resolution for the query in seconds. Default is 1.

        Returns
        -------
        dict
            Dict of lists of datetime objects on the given resolution

        """
        pass

    doc = NumpydocParser().parse(A.__doc__)
    assert len(doc.meta) == 1
    assert doc.meta[0].args == ['param']
    args_dict = dict(doc.meta[0].kwargs)

# Generated at 2022-06-13 19:43:53.131849
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
        assert inspect.getdoc(NumpydocParser.parse) == 'Parse the numpy-style docstring into its components.\n\n        :returns: parsed docstring'
        assert NumpydocParser.parse.__name__ == 'parse'


# Generated at 2022-06-13 19:44:01.787388
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    This is the short description.
    This is the long description.

    Parameters
    ----------
    a : type
        description of a
    b : type
        description of b

    Raises
    ------
    ValueError
        description of a ValueError exception

    Returns
    -------
    str
        description of the return value
    """

    result = parse(text)

    assert result.short_description == "This is the short description."
    assert result.blank_after_short_description is False

    assert result.long_description == "This is the long description."
    assert result.blank_after_long_description is True

    assert len(result.meta) == 5

    assert result.meta[0].args == ['param', 'a']
    assert result.meta[0].type_name == 'type'

   

# Generated at 2022-06-13 19:44:10.604323
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
        This function does something.
        It does it by calling the function named `func`.

        Parameters
        ----------
        arg_name
            A parameter with a type.
            And a second line.
        arg2 : type, optional
            A parameter with a type.
            And a second line.

        Returns
        -------
        return_name : type
            A return value.
            And a second line.

        Raises
        ------
        ValueError
            If things go wrong.
        """
    doc = NumpydocParser().parse(text)
    assert "This function does something" in doc.short_description
    assert "It does it by calling the function named `func`" in doc.long_description
    assert doc.short_description == "This function does something."
    assert doc.blank_after_short_description

# Generated at 2022-06-13 19:44:18.676628
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc = '''Single line summary
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

    Warnings
    --------
    Some warning about this function.

    See Also
    --------
    :meth:`some_other_func`
        '''

    ds = NumpydocParser().parse(doc)
    assert ds.short_description == 'Single line summary'
    assert ds.long_description == 'More detailed description.'
    assert len(ds.meta) == 4
    assert ds.meta[0].args == ['param', 'arg1']
    assert ds.meta[1].args == ['param', 'arg2']
    assert ds

# Generated at 2022-06-13 19:44:28.377172
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser(sections=DEFAULT_SECTIONS)
    text = """A one-line summary that does not use variable names or the
    function name.
    Extended Summary
    More extended summary that goes to the next line.
    Args:
        arg1 (int): Description of arg1
            More documentation for arg1
        arg2 (str): Description of arg2
            More documentation for arg2
    Returns:
        int
            Description of return value

    """
    result = parser.parse(text)
    print(result)



# Generated at 2022-06-13 19:44:31.431921
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert False

# Generated at 2022-06-13 19:44:33.866155
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = open("numpy.txt", "r", encoding="utf-8").read()
    parser = NumpydocParser()
    parser.parse(docstring)



# Generated at 2022-06-13 19:44:44.353132
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    input = """
    Estimate the distribution of a statistic from discrete samples.

    .. versionadded:: 0.1.0

    .. code-block:: python

        # Binomial distribution
        s = bin_estimator([1,1,1])
        plot_estimator(s)

        # Uniform distribution
        s = uni_estimator([1,2,2,2])
        plot_estimator(s)

    :param samples: array of samples
    :param plot: True to plot results
    :returns: estimated distribution
    """
    parser = NumpydocParser()
    res = parser.parse(input)


# Generated at 2022-06-13 19:44:53.675147
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():  # type: ignore[no-redef]
    title1 = "Attributes"
    title1_pattern = r"^\.\.\s*({})\s*::"
    key1 = "attribute"
    item1 = '''
        Returns
            int or None: The attribute, if set
    '''
    title2 = "Returns"
    title2_pattern = r"^{}\s*?\n{}\s*$"
    key2 = "returns"
    item2 = '''
            The value
    '''

    text = textwrap.dedent(
        '''
        .. title:: {}
            possibly over multiple lines
        {}
        {}
        '''.format(
            title1,
            item1,
            item2,
        )
    )

    # Add new section
    section1 = _S

# Generated at 2022-06-13 19:45:02.968179
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print(parse.__doc__)
    parser = NumpydocParser()

# Generated at 2022-06-13 19:45:13.936856
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from ..models import DocstringParam
    docstring = inspect.cleandoc("""
    Function description

    Arguments
    ---------
    arg_1 : type, optional
        This is an argument description.
    arg_2 : type
        Default is 5.

    Returns
    -------
    return_value : type
        Return description.
    """)
    numpydoc_parser = NumpydocParser()
    docstring = numpydoc_parser.parse(docstring)
    assert docstring.short_description == "Function description"
    assert docstring.long_description is None
    assert len(docstring.meta) == 2

# Generated at 2022-06-13 19:45:20.359790
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Test that the parsing only considers the text of a docstring,
    # not its indentation and not the header which may contain docstring types.
    text = """\
    This is the header

    This is the description

    Parameters
    ----------
        arg1 : str
            This is a parameter.

        arg2 : int
            This is another parameter.

    """
    assert len(text) == 111
    docstr = NumpydocParser().parse(text)
    assert len(docstr.meta) == 1
    assert len(docstr.meta[0].args) == 3



# Generated at 2022-06-13 19:45:30.079590
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print('Testing function NumpydocParser.parse')

    test_name = 'Test Name'
    test_text = 'Test description'
    test_description = test_name + '\n' + test_text
    test_parameter = 'Test Parameter'
    test_type = 'Test Type'
    test_parameter_type = test_parameter + ' : ' + test_type
    test_parameter_description = 'Test Parameter Description'
    test_parameter_type_description = test_parameter_type + '\n' + test_parameter_description
    test_examples = 'Test Examples'
    test_deprecated = 'Test Deprecated'


# Generated at 2022-06-13 19:45:32.088903
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    parser.parse("an example")


# Generated at 2022-06-13 19:45:38.035940
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = inspect.cleandoc(
        """
        Short description of the test_func function.

        Parameters
        ----------
        arg1 : str
            Description of `arg1`

        param2 : int
            Description of param2

        Returns
        -------
        bool
            Description of return value
        """
    )

# Generated at 2022-06-13 19:45:51.552366
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    def f():
        """short summary

        full description
        with multiple lines
        multi-line section

        Parameters
        ----------
        arg1
            first argument
        arg2 : type, optional
            second argument, default is 3.14

        Returns
        -------
        return_name : type
            return value description

        Raises
        ------
        ValueError
            if something goes wrong

        Warns
        -----
        UserWarning
            if something goes right

        See Also
        --------
        something(arg)

        Notes
        -----
        Optional

        Examples
        --------
        Examples can be given using either the ``Example`` or ``Examples``
        sections. Sections are distinguished by a title that is followed
        immediately by a colon and a block of indented text.

        >>> print('example')
        example

        """
        pass

    n

# Generated at 2022-06-13 19:45:56.974599
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    ds = NumpydocParser.parse(text="Test Parser")
    assert ds.short_description == "Test Parser"
    assert ds.long_description == None
    assert ds.blank_after_short_description == False
    assert ds.blank_after_long_description == False
    assert ds.meta == []



# Generated at 2022-06-13 19:45:59.756181
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    parser.parse("This is a test docstring.\n\nThis is the long description.")
    assert 1


# Generated at 2022-06-13 19:46:00.746519
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    pass


# Generated at 2022-06-13 19:46:03.138401
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import doctest
    parser = NumpydocParser()
    doctest.testmod(parser)

# Generated at 2022-06-13 19:46:14.173773
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Test method parse of class NumpydocParser"""
    parser = NumpydocParser()


# Generated at 2022-06-13 19:46:26.799930
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc_string = """
    aaaaa 
    
    Parameters
    ----------
    arg : int
        An integer argument
    arg2 : str, optional
        arg2 is optional
    
    Returns
    -------
    None
    """
    parsed_doc_string = NumpydocParser().parse(doc_string)

# Generated at 2022-06-13 19:46:37.294500
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Test the numpydoc parsing function."""
    deftest_NumpydocParser_parse_str = """
    Test the numpydoc parsing function.

    Parameters
    ----------
    arg1 : int
        The first parameter.
    arg2 : list of float
        The second parameter.

    Returns
    -------
    int
        The sum of the two parameters.

    Raises
    ------
    ValueError
        If xyz.

    See Also
    --------
    :py:meth:`test_NumpydocParser_parse`
        This function.
    """

# Generated at 2022-06-13 19:46:46.365556
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import numpydoc
    text =  """
    Silly example docstring.

    Very silly indeed. It even spans multiple lines.

    Parameters
    ----------
    a : type
        Paramness.

    b : type, optional
        More paramness, default is 42.

    Returns
    -------
    int
        Something silly, very silly indeed.
    """
    docstring = numpydoc.parse(text)
    assert docstring.short_description == 'Silly example docstring.'
    assert docstring.long_description == 'Very silly indeed. It even spans multiple lines.'
    assert docstring.meta[0].description == 'Paramness.'
    assert docstring.meta[1].description == 'More paramness, default is 42.'
    assert docstring.meta[2].description == 'Something silly, very silly indeed.'

# Generated at 2022-06-13 19:46:58.293784
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = parser.parse("""\
    This is the first line of the docstring.

    This is the second line of the docstring.\n""")
    assert docstring.short_description == 'This is the first line of the docstring.'
    assert docstring.blank_after_short_description == False
    assert docstring.long_description == 'This is the second line of the docstring.'
    assert docstring.blank_after_long_description == False
    assert len(docstring.meta) == 0

    docstring = parser.parse("""\
    This is the first line of the docstring.

    This is the second line of the docstring.

    This is the third line of the docstring.\n""")

# Generated at 2022-06-13 19:47:09.501383
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = """short description
    long description

    Parameters
    ----------
    test : int
        Test parameter.

    Returns
    -------
    test2 : str
        Test 2 return.
    """
    docstring = parser.parse(text)
    assert docstring.short_description == 'short description'
    assert docstring.long_description == 'long description'
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False

# Generated at 2022-06-13 19:47:12.446299
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:47:21.328021
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    testStr = "A multi-line docstring. This can be as long as we want.\n\
            Parameters:\n\
                arg1 (int): The first argument.\n\
                arg2 (int): The second argument.\n\
            Returns:\n\
                int: The return value.\n\
            Raises:\n\
                ValueError: If `arg2` is equal to `arg1`.\n\
            Examples:\n\
            >>> func(1, 2) # doctest: +SKIP"
    parsedDocstring = parse(testStr)
    parsedDocstring_2 = NumpydocParser().parse(testStr)
    assert str(parsedDocstring) == str(parsedDocstring_2)

# Generated at 2022-06-13 19:47:31.244172
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    def test_string(str_input: str, expected_value_list: T.List[str]) -> bool:
        sut = NumpydocParser().parse(str_input)
        # print(str_input)
        # print(sut)
        ret = []
        ret.append(str(sut.short_description))
        ret.append(str(sut.blank_after_short_description))
        ret.append(str(sut.blank_after_long_description))
        ret.append(str(sut.long_description))
        ret.extend([str(m) for m in sut.meta])
        return ret == expected_value_list

    # Test data

# Generated at 2022-06-13 19:47:36.093682
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
# This is a comment
# Another comment

"""
This is a docstring.
"""
'''
    expected = Docstring()
    expected.short_description = 'This is a docstring.'
    expected.blank_after_short_description = True
    expected.blank_after_long_description = False
    expected.long_description = None
    expected.meta = []

    assert NumpydocParser().parse(text) == expected

# Generated at 2022-06-13 19:47:47.072735
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Test for method NumpydocParser.parse"""

# Generated at 2022-06-13 19:47:58.225273
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
A function that does something.

Parameters
----------
x
    The first argument
y
    The second argument

Returns
-------
string
    A string describing the output

Raises
------
ValueError
    raised by this function if something bad happens
"""
    doc = parse(text)
    assert doc.short_description == "A function that does something."
    assert doc.long_description == None
    # Test meta
    meta = doc.meta
    assert len(meta) == 3
    assert len(meta[0].args) == 2
    assert meta[0].description == "The first argument"
    assert len(meta[1].args) == 1
    assert meta[1].description == "A string describing the output"
    assert len(meta[2].args) == 2

# Generated at 2022-06-13 19:48:09.537133
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_doc = """Guess the encoding of a file.

    Tries to find out the encoding that should be used to decode a Python
    source file. It returns ``'utf-8'`` if detection fails.

    :param f: opened python source file
    :param default: default encoding
    """

    parser = NumpydocParser()
    result = parser.parse(inspect.cleandoc(test_doc))
    assert result.short_description == "Guess the encoding of a file."
    assert len(result.meta) == 1
    assert result.meta[0].args == ['param', 'f']
    assert result.meta[0].description == 'opened python source file'



# Generated at 2022-06-13 19:48:13.357314
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = "lib\n" + "-" * 3 + "\n" + "hello world\n"
    parser = NumpydocParser()
    ret = parser.parse(text)
    desc = ret.short_description
    assert desc == "hello world"

# Generated at 2022-06-13 19:48:18.044429
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    assert 'Parameters' in parser.sections
    text = '''
    This is description of function.

    Parameters
    ----------
    arg1: type
        This is description of arg1.
    arg2 : type
        This is description of arg2
    arg3
        This is description of arg3

    Returns
    -------
    return_value : type
        This is description of return_value

    Examples
    --------
    >>> foo(1)
    This is description for func foo.

    Notes
    -----
    This is notes section.

    '''
    docstring = parser.parse(text)
    assert docstring.long_description == (
        ">>> foo(1)\n"
        "This is description for func foo."
    )

# Generated at 2022-06-13 19:48:37.719734
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Test parsing of numpydoc docstrings."""


    def test(text):
        return NumpydocParser().parse(text)

    assert test("") == Docstring()

    assert test("Description.") == Docstring(
        short_description="Description.",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )

    assert test("Description.\n") == Docstring(
        short_description="Description.",
        blank_after_short_description=False,
        blank_after_long_description=False,
        long_description=None,
        meta=[],
    )


# Generated at 2022-06-13 19:48:47.409937
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    def dummy_method():

        """
        This is a short description.

        This is a long description.

        Args:
            arg1 (int): description for arg1
            arg2 (str): description for arg2

        Returns:
            str: description for return

        """

    docstring = parse(inspect.getdoc(dummy_method))
    assert docstring.short_description == "This is a short description."
    assert docstring.blank_after_short_description == True
    assert docstring.long_description == "This is a long description."
    assert docstring.blank_after_long_description == True

# Generated at 2022-06-13 19:48:59.707218
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:49:08.191838
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """
    This function test the NumpydocParser class.
    """
    parsed_docstring = NumpydocParser().parse(docstring_example)
    # testing the short and long description
    assert parsed_docstring.short_description == "test"
    assert parsed_docstring.long_description == "hello world"
    # testing the meta information
    assert parsed_docstring.meta[0].args == ["param", "arg"]
    assert parsed_docstring.meta[0].description == "a description of arg"
    assert parsed_docstring.meta[0].arg_name == "arg"
    assert parsed_docstring.meta[0].type_name == "optional"
    assert parsed_docstring.meta[0].is_optional is True
    assert parsed_docstring.meta[0].default is None
    assert parsed

# Generated at 2022-06-13 19:49:19.465882
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    ndp = NumpydocParser()
    rd = ndp.parse(r'''
        This is a my first docstring test.
        No docstring has been tested yet.
        Parameters -- None
    ''')
    assert rd.short_description == "This is a my first docstring test."
    assert rd.blank_after_short_description == True
    assert rd.blank_after_long_description == True
    assert rd.long_description == "No docstring has been tested yet."
    assert len(rd.meta) == 0

    rd = ndp.parse(r'''
    This is a my first docstring test.
    No docstring has been tested yet.
    Parameters -- None
    ''')
    assert rd.short_description == "This is a my first docstring test."


# Generated at 2022-06-13 19:49:30.182580
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    docstring_without_long = r"""\
        Title here.

        Short description.

        Parameters
        ----------
        param1
            First parameter.
        param2 : int
            Second parameter.

        Returns
        -------
        return
            Return value.

        Examples
        --------
        This is an example.

        References
        ----------
        * References go here
        * More references go here

        """


# Generated at 2022-06-13 19:49:41.082723
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """First line of the docstring
    This function does something

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.
    param3 (optional) : bool
        The third, optional parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    Examples
    --------
    >>> message = 'test'
    >>> test_function(message)
    False
    """
    doc = NumpydocParser().parse(text)
    assert doc.short_description == "First line of the docstring"
    assert doc.long_description == "This function does something"
    assert doc.blank_after_short_description == False
    assert doc.blank_after_long_description == True
    assert len(doc.meta) == 5

# Generated at 2022-06-13 19:49:54.947389
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

# Generated at 2022-06-13 19:50:05.582616
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''\
    Short description
    Long description over
    multiple lines

    Parameters
    ----------
    param_1 : some_type
        Description of param_1
    param_2 : some_type, optional
        Description of param_2
    other_param_1 : some_type
    other_param_2 : some_type
    param_3
    param_4

    Raises
    ------
    ValueError
        Raises ValueError on
        invalid input
    IndexError
    TypeError

    Yields
    ------
    int
        An integer

    Returns
    -------
    bool
        A bool
    '''
    
    parser = NumpydocParser()
    result = parser.parse(text).meta

    assert result[0].args == ['param', 'param_1']

# Generated at 2022-06-13 19:50:13.381165
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Example of a docstring

    This is the same text seen in the first section:

        * foo
        * bar

    This is the short description.

    This is the long description. It can span multiple lines
    and contain *any* kind of information.

    Parameters
    ----------
    arg1 : str
        The first argument.
    arg2 : Optional[int]
        The second argument. It is optional.
    arg3 : str, optional
        The third argument. It is optional as well.

    Returns
    -------
    None
        This function does not return anything.

    Other Parameters
    ----------------
    kw1 : dict
        A keyword-only argument

    """

# Generated at 2022-06-13 19:50:30.014361
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    sections = {
        "Parameters": ParamSection("Parameters", "param"),
        "Raises": RaisesSection("Raises", "raises"),
        "Returns": ReturnsSection("Returns", "returns")
    }
    parser = NumpydocParser(sections)

    # test basic numpydoc docstring format (short and long descriptions)
    docstring = """
    This is the short description:

    This is the long description. It can span
    several lines.

    Parameters
    ----------
    x: int
        The first argument
    y: str
        The second argument.

    Returns
    -------
    int
        The return value.
    """
    parsed = parser.parse(docstring)
    assert parsed.short_description == "This is the short description:"
    assert parsed.blank_after_short_description == True


# Generated at 2022-06-13 19:50:42.193576
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:50:44.520880
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    sample_docstring = """
        """
    assert NumpydocParser().parse(sample_docstring) == Docstring()

# Generated at 2022-06-13 19:50:54.739254
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
	"""
	This test case will be used to check if function parses docstring is working properly.
	
		- docstring: a numpy-style docstring
		- expected : expected output
		- method_name : name of the method for which docstring needs to be parsed
		- arguments: list of arguments for the given method
		- return : return type of the given method

		Note: We are testing only for docstring with only two sections. For more sections, we will add more test cases.
	"""
	docstring = """
	This is demarked long description of the method
	Args : list of arguments
		This is description of first arg
		This is description of second arg
	Returns :
		This is description of the ret
	"""

# Generated at 2022-06-13 19:50:59.594247
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = """
    Parse the numpy-style docstring into its components.
    :returns: parsed docstring
    """
    assert NumpydocParser().parse(docstring).short_description == 'Parse the numpy-style docstring into its components.'

# Generated at 2022-06-13 19:51:12.817433
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    source_code = """
        Test docstring.

        Parameters
        ----------
        arg: str
            test arg

        Returns
        -------
        dict
            test dict
    """
    parser = NumpydocParser()
    docstring = parser.parse(source_code)
    assert docstring.short_description == "Test docstring."
    param_arg = docstring.meta[0].args[0]
    assert param_arg['name'] == "arg"
    assert param_arg['type_name'] == "str"
    assert param_arg['description'] == "test arg"
    return_arg = docstring.meta[1].args[0]
    assert return_arg['type_name'] == "dict"
    assert return_arg['description'] == "test dict"


# Generated at 2022-06-13 19:51:23.125894
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring_example = """
    This is the short description.

    This is the long description.  The short description is up until the first
    blank line.

    The long description is already-paragraph-wrapped text that explains, in
    detail, what the function does.  The long description can be several
    paragraphs, and include enumerations and lists.

    :param int arg1: The first argument.
    :param str arg2: The second argument.
    :returns:  int -- the return code.
    :raises: AttributeError, KeyError
    """
    docstring = NumpydocParser().parse(docstring_example)
    assert docstring.short_description == "This is the short description."