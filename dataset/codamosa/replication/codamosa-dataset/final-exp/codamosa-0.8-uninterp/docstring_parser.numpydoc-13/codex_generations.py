

# Generated at 2022-06-13 19:41:56.617020
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = ("Simple docstring\n"
            "Params:\n"
            "  x: int\n"
            "    The meaning of x...\n"
            "    ...continued\n"
            "    ...continued again\n"
            "  y: int, optional\n"
            "    The meaning of y. Defaults to 1\n"
            "    ...continued\n"            
            "Returns:\n"
            "  int\n"
            "    The meaning of return value\n")
    print(parser.parse(
        text
    ))


if __name__ == "__main__":
    import sys
    import ast

    if len(sys.argv) > 1:
        text = sys.argv[1]

# Generated at 2022-06-13 19:42:05.921247
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = parse('''
    A function that does one thing.

    And then another.

    Parameters
    ----------
    param1 : something
        A parameter.
    param2 (optional)
        Another parameter.
    other_param : something else
        Next parameter.
    attribute : read-only
        An attribute.
    yields : another type
        A yielded value.
    receives : third type
        A received value.
    References
    ----------
    * read-only
    * optional, defaults to foo
    * parameter
    ''')
    assert docstring.short_description == 'A function that does one thing.'
    assert docstring.long_description.split('\n') == [
        'And then another.']
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long

# Generated at 2022-06-13 19:42:13.628560
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc_text = """
        Parse the numpy-style docstring into its components.

        :returns: parsed docstring
    """
    expected_docstring = Docstring(
        short_description='Parse the numpy-style docstring into its components.',
        long_description='Parsed docstring',
        blank_after_short_description=True,
        blank_after_long_description=True,
        meta=[
            DocstringReturns(
                args=['returns'],
                description='parsed docstring',
                type_name=None,
                is_generator=False,
                return_name=None,
            ),
        ],
    )

    parser = NumpydocParser()
    result = parser.parse(doc_text)

    assert(expected_docstring == result)

# Generated at 2022-06-13 19:42:25.898688
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Next() with return value"""
    from .common import Docstring, DocstringMeta, DocstringParam, DocstringRaises, DocstringReturns
    from .numpydoc_parser import NumpydocParser
    from .common import Docstring, DocstringMeta, DocstringParam, DocstringRaises, DocstringReturns
    from .numpydoc_parser import NumpydocParser

# Generated at 2022-06-13 19:42:29.096431
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    parser = NumpydocParser()
    section = writer.DeprecationSection('deprecated', 'deprecation')
    text = '.. deprecated:: 1.0\n\n   This function is deprecated.'
    assert next(section.parse(text)) == DocstringDeprecated(
        args=[u'deprecation'],
        description=u'This function is deprecated.',
        version='1.0'
    )


# Generated at 2022-06-13 19:42:37.732918
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:42:44.743660
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    section = DeprecationSection(title="Deprecation Warning", key="deprecated")
    text = '''DeprecationWarning: some_function is deprecated!\n
                                 Use another_function instead
              '''
    expected_description = '''DeprecationWarning: some_function is deprecated!\n
                            Use another_function instead'''
    expected_version = 'DeprecationWarning'
    result = section.parse(text)
    result_meta = next(result)
    assert result_meta.description == expected_description
    assert result_meta.version == expected_version


# Generated at 2022-06-13 19:42:51.614448
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:43:01.548921
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
        This function computes the sum of two numbers.

        Parameters
        ----------
        a : int, float or complex
            First element to sum
        b : int, float or complex
            Second element to sum

        Returns
        -------
        res : int, float or complex
            Sum of `a` and `b`
        '''

    doc = NumpydocParser().parse(text)
    assert doc.short_description == 'This function computes the sum of two numbers.'
    assert doc.long_description == None
    assert doc.blank_after_long_description == False
    assert doc.blank_after_short_description == True
    assert len(doc.meta) == 2
    assert doc.meta[0].key == 'param'
    assert doc.meta[0].args == ['param', 'a']


# Generated at 2022-06-13 19:43:13.399254
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from ..tests.fixtures import TestCase


# Generated at 2022-06-13 19:43:27.083246
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import unittest

    class MyTest(unittest.TestCase):
        def test_NumpydocParser_parse(self):
            text = """
            mytest

            testtest

            Parameters
            ----------

            test

            Raises
            ------

            test
            """
            parser = NumpydocParser()
            doc = parser.parse(text)
            self.assertIsNotNone(doc)
            self.assertEqual(len(doc.meta), 2)
            self.assertEqual(doc.meta[0].args[0], 'param')
            self.assertEqual(doc.meta[1].args[0], 'raises')

    unittest.main()

# Generated at 2022-06-13 19:43:40.552943
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    ds = r"""
    Compute the sum of a list of numbers.
    This function does some stuff.

    Parameters:
        x: list of numbers to be summed.

    Returns:
        The sum of numbers in x.
    """
    nd_parser = NumpydocParser()
    res = nd_parser.parse(ds)
    assert(res.short_description == 'Compute the sum of a list of numbers.')
    assert(res.long_description == 'This function does some stuff.')
    assert(res.blank_after_short_description == True)
    assert(res.blank_after_long_description == True)
    assert(res.meta[0].args == ['param', 'x'])
    assert(res.meta[0].description == 'list of numbers to be summed.')

# Generated at 2022-06-13 19:43:47.381882
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    # error message when text is None
    text = None
    ret = parser.parse(text)
    assert isinstance(ret, Docstring)
    
    # error message when text is not None and it dosen't need inspect.cleandoc() 
    text = "first line\nsecond line\n"
    ret = parser.parse(text)
    
    assert ret.short_description == "first line"
    assert ret.long_description == "second line"
    assert ret.blank_after_short_description == False
    assert ret.blank_after_long_description == True
    
    # error message when text is not None and it needs inspect.cleandoc()
    text = """
    First paragraph.

    Second paragraph.
    """
    ret = parser.parse(text)


# Generated at 2022-06-13 19:43:58.037833
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    sample_docstring = """pytest_bdd_ext package.

    Use this package when you want to write BDD tests using pytest.
    See http://pytest-bdd.readthedocs.org/en/latest/ for more info
    about pytest-bdd.

    :param string: name
       This is a string.

    :param int value: This is an integer.

    :param dict some_dict:
       This is a dict.

    :param list some_list:
       This is a list.

    :param list some_list:
       This is another list.

    :param list some_list:
       This is a third list.

    :return: dict
       This is a dict.

    :param int value: This is a forth integer.
    """

    parsed_docstring = Numpydoc

# Generated at 2022-06-13 19:44:08.083556
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    def test_case(docstring, expected):
        assert parser.parse(docstring) == expected


# Generated at 2022-06-13 19:44:15.715444
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    @NumpydocParser.add_section(Section("Unit test", "unittest"))
    def parse(text: str) -> Docstring:
        """Parse the numpy-style docstring into its components.

        :returns: parsed docstring
        """
        ret = Docstring()
        if not text:
            return ret

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
        parts = desc

# Generated at 2022-06-13 19:44:23.254808
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    get_user_model()

        Returns the User model that is active in this project.
    """
    docstring = NumpydocParser().parse(text)
    assert docstring.short_description == "get_user_model()"
    assert docstring.long_description == (
        "Returns the User model that is active in this project."
    )

# Generated at 2022-06-13 19:44:33.332223
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .common import DocstringReturns
    text = """
A function with a docstring that does not follow the numpydoc format.

Parameters
----------
    func1:
        returns: the first function
    func2:
        returns: the second function
Returns
-------
    list
        List of functions"""

    docstring = NumpydocParser().parse(text)
    assert docstring.short_description == 'A function with a docstring that does not follow the numpydoc format.'

    assert docstring.long_description == '\n    Parameters\n    ----------\n        func1:\n            returns: the first function\n        func2:\n            returns: the second function\n    Returns\n    -------\n        list\n            List of functions'

    meta_returns = docstring.meta[0]

# Generated at 2022-06-13 19:44:43.846660
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_cases = [
        # docstring, (expected_factory_titles, expected_meta_count)
        [
            """
            A description of this class.

            Parameters
            ----------
            arg1 : str

            Other Parameters
            ----------------
            arg2 : int
                A description of arg2
                that spreads over multiple lines
            """,
            (("Parameters", "Other Parameters"), 2),
        ],
        [
            """
            A description of this class.

            Raises
            ------
            TypeError
                When you cannot type.

            Warnings
            --------
            DeprecationWarning
                I mean, maybe...

            Examples
            --------
            >>> print("Hello World")
            """,
            (("Raises", "Warnings", "Examples"), 3),
        ],
    ]

# Generated at 2022-06-13 19:44:51.277559
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # General case
    GENERAL_CASE = NumpydocParser().parse("""
    Short Description

    Long Description

    Parameters
    ----------
    param : type, optional
        Description of the parameter.
    other_param : type
        Description

    Returns
    -------
    type
        Description

    Raises
    ------
    ValueError
        Description

    Warns
    -----
    Warning
        Description

    Returns
    -------
    type
        Description

    Yields
    ------
    type
        Description

    Examples
    --------
    >>> a
    1
    """)

    assert GENERAL_CASE.short_description == "Short Description"
    assert GENERAL_CASE.long_description == "Long Description"
    assert len(GENERAL_CASE.meta) == 8

# Generated at 2022-06-13 19:45:02.358884
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    print("Test NumpydocParser...")
    assert parser.parse("") == Docstring()
    assert parser.parse("   ") == Docstring()
    assert parser.parse("\n") == Docstring()
    assert parser.parse("\n \n") == Docstring()
    assert parser.parse("  \n   ") == Docstring()

    docstring = parser.parse("short\nlong")
    assert docstring.short_description == "short"
    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is False
    assert docstring.long_description == "long"
    assert docstring.meta == []

    docstring = parser.parse("short\n long")

# Generated at 2022-06-13 19:45:10.743374
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    numpydoc_parser = NumpydocParser()
    ret = numpydoc_parser.parse.__func__(numpydoc_parser, """
    Short description.

    Longer description.
    
    Parameters
    ----------
    arg1 : str
        Description of `arg1`.
    arg2 : float
        Description of `arg2`.
    
    Returns
    -------
    str
        Description of return value.
    
    Raises
    ------
    ValueError
        If `arg2` is equal to zero.
    """)
    print (ret)

# Generated at 2022-06-13 19:45:22.859610
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = "short description\n\nlong description"
    assert parser.parse(docstring).short_description == "short description"
    assert parser.parse(docstring).long_description == "long description"
    assert parser.parse(docstring).blank_after_short_description is True
    assert parser.parse(docstring).blank_after_long_description is False
    assert parser.parse(docstring).meta == []

    docstring = "short description\nlong description"
    assert parser.parse(docstring).short_description == "short description"
    assert parser.parse(docstring).long_description == "long description"
    assert parser.parse(docstring).blank_after_short_description is False
    assert parser.parse(docstring).blank_after_long_description is False


# Generated at 2022-06-13 19:45:31.930536
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # test_parse_docstring
    def f(a, b, c=3.5, d=7):
        """
        f(a, b[, c, d])

        Short desc.

        This is a long description.

        Parameters
        ----------
        a : type1
            First parameter

        b
            Second parameter.

        c : int, optional
            Third parameter.

        d, optional
            Fourth parameter.

        Returns
        -------
        values: iterable[int]
            The return value.
        """
        return (a, b, c, d)

    # test_parse_docstring_none
    def f():
        pass

    if __name__ == "__main__":
        parser = NumpydocParser()
        print(parser.parse(f.__doc__))

# Unit test

# Generated at 2022-06-13 19:45:42.879182
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    #
    # long_description: ...
    #
    docstring = NumpydocParser().parse("""
    long_description
    """)
    assert docstring.short_description is None
    assert docstring.blank_after_short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_long_description is None
    assert docstring.meta is not None
    assert len(docstring.meta) == 0

    #
    # short_description: ...
    #
    # long_description
    #
    docstring = NumpydocParser().parse("""
    short_description
    long_description
    """)
    assert docstring.short_description == "short_description"
    assert docstring.blank_after_short_description is True
    assert docstring.long_

# Generated at 2022-06-13 19:45:48.959719
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
    Short description.

    Long description.

    Parameters
    ----------
    par1: str
        Parameter 1.
    par2: bool, optional
        Parameter 2. (defaults to True)
    par3 : str,
        Parameter 3.
    '''
    parser = NumpydocParser()
    docstring = parser.parse(text)
    assert docstring.short_description == "Short description."



# Generated at 2022-06-13 19:45:59.120929
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = '''
    An example docstring in Numpy format

    This is the short description.
    This is the long description that lasts multiple lines and
    introduces more formal documentation.

    Parameters
    ----------
    arg1 : type, optional
        description
    arg2 : type
        description [default is some_default]
    arg3 : type
        description

    Returns
    -------
    None
        return
    '''
    doc = parser.parse(text)
    print(doc.short_description)
    print(doc.long_description)
    for meta in doc.meta:
        print(meta.args)
        print(meta.description)
        print()


# Generated at 2022-06-13 19:46:02.888498
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    config = NumpydocParser()
    text = """Method to parse docstring.
    
    Parameters
    ----------
        text : str
            Text to parse
    """
    doc = config.parse(text)
    assert doc.short_description == "Method to parse docstring."
    assert len(doc.meta) == 1
    assert doc.meta[0].args == ["param", "text"]
    assert doc.meta[0].type_name == "str"
    assert doc.meta[0].description == "Text to parse"

# Generated at 2022-06-13 19:46:13.931176
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Test
    docstring = parse(
        """
        Short summary.

        Longer description.

        Parameters
        ----------
        param_name : type, optional
            Description of the parameter.

        Other Parameters
        ----------------
        other_param_name : type
            Description of another parameter.

        Returns
        -------
        return_name : type
            Description of the returns.

        Examples
        --------
        Example usage of function.

        See Also
        --------
        * Other function to see.

        Warnings
        --------
        Warnings.

        References
        ----------
        * References.

        .. deprecated:: 1.0.0
            Use new_function instead.
        """
    )

    # Assert
    assert docstring.short_description == "Short summary."
    assert docstring.blank_after_short_description


# Generated at 2022-06-13 19:46:26.502143
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstr = """Parameters
    ----------
    param1 : type
        description
    param2
        description
    param3 : type, optional
        description
    """
    doc = parser.parse(docstr)
    assert doc.short_description == None
    assert doc.long_description == None
    assert doc.blank_after_short_description == True
    assert doc.blank_after_long_description == True
    assert len(doc.meta) == 4
    assert doc.meta[0].key == "param"
    assert doc.meta[0].arg_name == "param1"
    assert doc.meta[0].type_name == "type"
    assert doc.meta[0].description == "description"
    assert doc.meta[0].is_optional == False
    assert doc

# Generated at 2022-06-13 19:46:38.456737
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_string = """Compute the maximal virtual work.

    Parameters
    ----------
    a : array_like
        shape (n)
    b : array_like
        shape (n)
    c : array_like
        shape (n)
    d : array_like
        shape (n)

    Returns
    -------
    wvm : float
        TODO

    See Also
    --------
    TODO
    """

    doc_string = NumpydocParser().parse(test_string)
    assert doc_string.short_description == "Compute the maximal virtual work."
    assert doc_string.long_description == "TODO"
    assert doc_string.meta[0] == DocstringMeta(
        ["param", "a"], description="shape (n)"
    )



# Generated at 2022-06-13 19:46:46.981189
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Test docstring

    This is a long description.

    Parameters
    __________
    arg1 : str
        Description of arg1
    arg2 : int, optional
        Description of arg2
    
    Example
    _______
    >>> print('hello world')
    hello world
    """

# Generated at 2022-06-13 19:46:58.862461
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:47:11.998140
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    nd_parser = NumpydocParser()

    text_0 = """A nice short description

A longer description, with some examples:

>>> s = "Python syntax highlighting"
>>> print s
Python syntax highlighting

Args:
    arg1: The first argument.
    arg2: The second argument.
Return:
    The return value. True for success, False otherwise.
"""

# Generated at 2022-06-13 19:47:18.540071
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = """
        This is a single-line description.

        This is a multi-line description
        that uses a blank second line.

            This is a multi-line description
            that uses indentation.

        Parameters
        ----------
        param_1 : str
            First param.
        param_2 (int):
            Second param.

        Raises
        ------
        ValueError
            Raises value error.

        Returns
        -------
        str
            This returns something.

        Notes
        -----
        Note text.

        Examples
        --------
        Single-line example.

            >>> example

        Multi-line example:
        >>> example

        >>> example

        Warns
        -----
        Warning text.
    """

    ds = parser.parse(text)

    # test description
   

# Generated at 2022-06-13 19:47:28.407251
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text="""
    Func
        interesting
        func
        ... stuff
        .. note::
            A note about this function
    Parameters
    ----------
    arg : str
        A string argument
    kwarg : int, optional
        A keyword argument
    Returns
    -------
    ret_val : str
        A return value
    See Also
    --------
    :meth:`funky() <foo.bar.funky>`
    :meth:`bunky() <foo.bar.funky>`
    """
    parser = NumpydocParser()
    ret = parser.parse(text)
    assert ret.short_description == "Func"
    assert ret.long_description == "interesting\nfunc\n... stuff"
    assert ret.blank_after_short_description == False
    assert ret.blank

# Generated at 2022-06-13 19:47:36.960359
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

# Generated at 2022-06-13 19:47:39.119236
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import doctest
    return doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

# Generated at 2022-06-13 19:47:48.513484
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print("Test method parse of class NumpydocParser")


# Generated at 2022-06-13 19:47:59.192940
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    t = """
An example numpy docstring using reStructuredText
=================================================

This docstring demonstrates the numpydoc reStructuredText format and
how it can be parsed by sphinx, numpy-style docstrings.

Parameters
----------
foo : str
  A string describing the foo parameter.

bar : int, optional
    A description of the bar parameter.

Returns
-------
str
    A string describing the return value.
"""
    docstring = NumpydocParser().parse(t)
    assert docstring.short_description == "An example numpy docstring using reStructuredText"
    assert docstring.blank_after_short_description == True

# Generated at 2022-06-13 19:48:16.802859
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    
    # Examples given in numpydoc documentation.
    
    # Example 1
    docstring = """One line summary
    Extended description

    Parameters
    ----------
    arg1 : int
        Description of `arg1`
    arg2 : str
        Description of `arg2`

    Returns
    -------
    bool
        Description of return value

    Raises
    ------
    ValueError
        Description of exception
    """
    
    doc = parser.parse(docstring)
    
    # Example 2

# Generated at 2022-06-13 19:48:17.758311
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    pass


# Generated at 2022-06-13 19:48:34.296642
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """\
    This is the docstring for a method.

    More documentation for the method (if needed) goes here.

    Parameters
    ----------
    arg : str
        The string argument for the method. The default value for this
        argument is 'abc'.
    arg2 : int
        Another argument. No default value specified

    Raises
    ------
    ValueError
        If the method failed.

    Returns
    -------
    bool
        A boolean value indicating success (True) or failure (False)
    """
    doc = NumpydocParser().parse(text)
    assert doc.short_description == "This is the docstring for a method."
    assert doc.long_description == \
        "More documentation for the method (if needed) goes here."

    assert doc.blank_after_short_description == True
    assert doc

# Generated at 2022-06-13 19:48:44.288724
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = """
    Parameters:
        In order to use the nested-folds cross-validation, your estimator must
        have either a `fit`, `predict_proba`, or `predict_log_proba` method.
        n_splits : int, optional
            Number of folds in cross-validation. Default is 3.
        criterion : string, optional (default="gini")
            The function to measure the quality of a split. Supported criteria
            are "gini" for the Gini impurity and "entropy" for the information
            gain.
    Returns:
        transformed : DataFrame
    """
    docstring = parser.parse(text)
    print(docstring)



# Generated at 2022-06-13 19:48:54.314773
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docs = """
    This is the short description.

    This is the long description,
    which is possibly multi-line.

    Parameters
    ----------
    arg_a : type, optional
        Description of arg_a.
    arg_b
        Description of arg_b.
    arg_c : type
        Description of arg_c.

    Other Parameters
    ----------------
    arg_d
        Description of arg_d.

    Examples
    --------
    >>> 1 + 1
    2

    >>> 2 + 2
    4
    """

    x = NumpydocParser()
    ret = x.parse(docs)
    assert ret.short_description == "This is the short description."
    assert ret.long_description == "This is the long description,\
    which is possibly multi-line."
    assert ret.blank_after_

# Generated at 2022-06-13 19:49:04.651262
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:49:15.161291
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring: str = '''
        Parse the numpy-style docstring into its components.

        :returns: parsed docstring

        Parameters
        ----------
        text: int
            Description of parameter `text`.
        '''

    my_parser = NumpydocParser()
    result: Docstring = my_parser.parse(docstring)

    assert result.short_description == "Parse the numpy-style docstring into its components."
    assert result.long_description == None

    assert len(result.meta) == 1
    assert isinstance(result.meta[0], DocstringParam)
    assert result.meta[0].args == ['param', 'text']
    assert result.meta[0].description == 'Description of parameter `text`.'

# Generated at 2022-06-13 19:49:22.960394
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
        Args:
            param1 (type1):
                param1 description
            param2:
            param3, optional:
            param4, optional:
            param5 (type2, optional, default=10):
                param6 description
            *args: 
                *args description
            **kwargs: 
                **kwargs description
        '''
    text = inspect.cleandoc(text)
    doc = NumpydocParser().parse(text)
    assert doc.short_description is None
    assert doc.long_description is None
    assert len(doc.meta) == 7

    assert doc.meta[0].args[0] == 'param'
    assert doc.meta[0].description == 'param1 description'

    assert doc.meta[1].args[0] == 'param'

# Generated at 2022-06-13 19:49:32.628329
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    doc = """
    This is a description of the function.

    Descriptions can span multiple lines, separated by
    line breaks and no actual content.

    Parameters
    ----------
    fab : str, optional
        String to return.
    gab : bool
        Boolean indicating whether to return string.

    Returns
    -------
    str
        The string.

    Notes
    -----
    This is a note.

    Raises
    ------
    Exception
        An exception.
    """

    ret = Docstring()

    ret.short_description = "This is a description of the function."
    ret.blank_after_short_description = False
    ret.blank_after_long_description = False
    ret.long_description = """
    Descriptions can span multiple lines, separated by
    line breaks and no actual content.
    """

    ret

# Generated at 2022-06-13 19:49:42.657908
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:50:08.518005
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:50:11.187985
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text= """Summary line.
    Extended description of function.
    Args:
        param1: Description of arg1
    Returns:
        Description of return value.
    """
    n=NumpydocParser()
    n.parse(text)

# Generated at 2022-06-13 19:50:16.670204
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''This is the short description.

    This is the long description.  The long description
    is useful for e.g. an API that has multiple signatures for
    its methods.

    Parameters
    ----------
    arg1 : int
        The first command-line argument.
    arg2 : str
        The second command-line argument.
    arg3 : int
        The third command-line argument.

    Returns
    -------
    int
        The return code.
    '''
    assert parse(text).short_description == "This is the short description."
    assert parse(text).blank_after_short_description == True

# Generated at 2022-06-13 19:50:28.544524
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:50:30.661752
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import doctest   
    doctest.testmod(extraglobs={'np': doctest.mock.NonCallableMock()})

# Generated at 2022-06-13 19:50:42.690458
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # docstring = """one-liner

    # long description

    # Parameters
    # ----------
    # param_1 : type
    #     param_1 description

    # param_2 : type, optional
    #     param_2 description

    # param_3 : type
    #     default: 20
    #     param_3 description

    # param_4 : type, optional
    #     default: 30
    #     param_4 description
    # """
    docstring = """Parameters
    ----------
    param_1 : type
        param_1 description

    param_2 : type, optional
        param_2 description

    param_3 : type
        default: 20
        param_3 description

    param_4 : type, optional
        default: 30
        param_4 description
    """
    sut = parse(docstring)

# Generated at 2022-06-13 19:50:53.605861
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

# Generated at 2022-06-13 19:51:06.357081
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = '''
    This is a short description.

    This is a long description.

    Parameters
    ----------
    name : str, required
        Name of the person.

    Returns
    -------
    unk : bool
        Success.

    Raises
    ------
    ValueError
        If `name` is "Bad Person"
    '''
    ret = parser.parse(docstring)
    assert ret.short_description == "This is a short description."
    assert ret.long_description == "This is a long description."
    assert ret.blank_after_short_description == True
    assert ret.blank_after_long_description == True
    assert ret.meta[0].args == ['param', 'name']

# Generated at 2022-06-13 19:51:17.038464
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print("#-----------Test NumpydocParser_parse-----------------#")
    text = """
    Test method __init__.

    This method is for passing test cases.

    Parameters
    ----------
    text: String
        The input string

    Returns
    -------
    number: int
        length of input string
    """
    # Initialize a NumpydocParser object
    parser = NumpydocParser()
    # Parse the docstring
    result = parser.parse(text)

    # Test the short_description
    if result.short_description == "Test method __init__.":
        print("short_description = ", result.short_description, " is passed.")
    else:
        print("short_description = ", result.short_description, " is failed.")

    # Test the long_description