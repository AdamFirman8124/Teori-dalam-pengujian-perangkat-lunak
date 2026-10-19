

# Generated at 2022-06-13 19:41:35.482963
# Unit test for method parse of class Section
def test_Section_parse():

    for s in DEFAULT_SECTIONS:
        print(s.title)
        print(s.parse('type\n\nvalue'))


# Generated at 2022-06-13 19:41:42.393756
# Unit test for method parse of class _KVSection
def test__KVSection_parse():

    class TestSection(_KVSection):
        def __init__(self, title, key):
            super().__init__(title, key)

        def _parse_item(self, key: str, value: str) -> DocstringMeta:
            return DocstringMeta(args=[self.key, key], description=_clean_str(value))

    test_str = '''
    first_item: notdef
        some text
    second_item: int
        simple integer
    third_item: str, optional
        string, optional
    fourth_item: str(optional)
        string, optional
    fifth_item: str, optional(opt)
        string, optional
    '''


# Generated at 2022-06-13 19:41:45.422621
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    text = ""
    ds = NumpydocParser().parse(text)
    assert ds.short_description == None
    assert ds.long_description == None


# Generated at 2022-06-13 19:41:49.914174
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    d = DeprecationSection("deprecated", "deprecation")
    text = (
        """.. deprecated:: 0.2.2\n"""
        """   Test"""
    )
    r = d.parse(text)
    assert next(r)[0].version == '0.2.2'



# Generated at 2022-06-13 19:41:57.233362
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    expected = Docstring(
        short_description='This is short',
        long_description="This is long\n\nThis is long too!",
        blank_after_short_description=True,
        blank_after_long_description=False,
        meta=[
            DocstringMeta(["param", "a"], description="foo\nbar\n\nbaz"),
            DocstringMeta(["param", "b"], description="bar"),
            DocstringMeta(["param", "c"], description="baz"),
            DocstringMeta(["param", "d"], description=None),
        ],
    )


# Generated at 2022-06-13 19:42:06.299698
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Test simple docstring
    text = """
    Test doc string.

    Parameters
    ----------
    arg1 : int
        First important argument
    arg2 : dict
        Second important argument

    Returns
    -------
    output : int
        Result of the function
    """
    docstring = Docstring()
    docstring.short_description = "Test doc string."
    docstring.long_description = None
    docstring.blank_after_short_description = True
    docstring.meta.append(
        DocstringParam(
            args=["param", "arg1"],
            description="First important argument",
            arg_name="arg1",
            type_name="int",
            is_optional=False,
            default=None,
        )
    )

# Generated at 2022-06-13 19:42:11.911955
# Unit test for method parse of class Section
def test_Section_parse():
    section = Section(title="Returns", key="returns")
    text = """Return x^y element-wise.
    Parameters
    ----------
    x : array_like
        The bases.
    y : array_like
        The exponents.
    Returns
    -------
    out : array_like
        The bases raised to the exponents.
    """
    assert list(section.parse(text))[0].args == ["returns"]
    assert list(section.parse(text))[0].description == "Return x^y element-wise."

# Generated at 2022-06-13 19:42:21.445021
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    assert DeprecationSection('deprecated', 'deprecation').parse('1.5\nThis is a deprecation warning.\n') == [DocstringDeprecated([_DeprecationSection__DeprecationSection__key], description='This is a deprecation warning.', version='1.5')]

    assert DeprecationSection('deprecated', 'deprecation').parse('') == [DocstringDeprecated([_DeprecationSection__DeprecationSection__key], description=None, version='')]

# Generated at 2022-06-13 19:42:32.997420
# Unit test for method parse of class DeprecationSection
def test_DeprecationSection_parse():
    class DeprecatedSection:
        def __init__(self, title: str, key: str) -> None:
            self.title = title
            self.key = key

        @property
        def title_pattern(self) -> str:
            return r"^\.\.\s*({})\s*::".format(self.title)

        def parse(self, text: str) -> T.Iterable[DocstringDeprecated]:
            version, desc, *_ = text.split(sep="\n", maxsplit=1) + [None, None]

            if desc is not None:
                desc = _clean_str(inspect.cleandoc(desc))

            yield DocstringDeprecated(
                args=[self.key], description=desc, version=_clean_str(version)
            )
    ds = Deprecation

# Generated at 2022-06-13 19:42:35.949468
# Unit test for method parse of class Section
def test_Section_parse():

    teststring = """
    Parameters
    ----------
    x : ndarray
    """
    section = Section('Parameters', 'param')
    assert section.parse(teststring) == [DocstringMeta(['param'], description='ndarray')]


# Generated at 2022-06-13 19:42:49.714478
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
	ex1 = """Name-value pair.

	:param name:  Name
	:type name:  string
	:param value:  Value
	:type value:  number
	"""
	ex2 = """Returns a list of dict of the modules it imported

	:returns:  list of dict of the modules it imported
	:rtype:  list
	"""
	assert parse(ex1).short_description == "Name-value pair."
	assert parse(ex1).long_description == "Name-value pair."
	assert parse(ex1).meta[0].args[0] == "param"
	assert parse(ex1).meta[1].args[0] == "type"
	assert parse(ex1).meta[2].args[0] == "param"
	assert parse(ex1).meta[3].args[0]

# Generated at 2022-06-13 19:42:50.658372
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    NumpydocParser().parse('')

# Generated at 2022-06-13 19:43:00.787664
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = '''
    first line
    second line

    Parameters
    ----------
    param1: int
        description of param1

    param2 : str
        description of param2

    param3, optional
        description of param3
    '''
    ret = NumpydocParser().parse(text)

# Generated at 2022-06-13 19:43:12.748101
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Create a string of the form of a docstring
    text = """
    Numpy docstring.

    Parameters
    ----------
    key : type
        This is a long description of the key parameter.

    Returns
    -------
    returns
        This is a long description of the returns.
    """
    docstring = NumpydocParser().parse(text)
    assert docstring.short_description == 'Numpy docstring.'
    assert docstring.long_description == 'This is a long description of the key parameter.\n'
    assert docstring.blank_after_short_description
    assert docstring.blank_after_long_description
    assert docstring.meta[2].args == ['returns']
    assert docstring.meta[2].description == 'This is a long description of the returns.'

    # Create a string of the form

# Generated at 2022-06-13 19:43:23.812683
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    test_docstring = '''
    This is a one-line explanation of the function/method. It should
    be no longer than necessary.

    Here is the first paragraph of the explanation, which is set in
    regular text.

    More paragraphs can follow, separated by empty lines.

    Parameters
    ----------
    param1 : type
        First parameter

    param2 : {'hello', 'bye'}, optional
        Second parameter

    Returns
    -------
    type
        description

    Notes
    -----
    Some explanatory notes can be given
    as bullet points:
    - point 1
    - point 2

    Another paragraph of the explanation.

    References
    ----------
    The reference section is optional.

    .. [1] Donald Knuth, The TeXbook, 2007.
    '''
    numpydoc_parser = Numpydoc

# Generated at 2022-06-13 19:43:32.117187
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text_under_test = '''
        simple text
        
        Parameters
        ----------
            something : int
                description
                can be multiline
    '''
    parser = NumpydocParser()
    docstring = parser.parse(text=text_under_test)
    assert str(docstring)=='<Docstring(short_description=simple text, long_description=, blank_after_short_description=True, blank_after_long_description=False, meta=<DocstringMeta(args=[param, something], description=description\ncan be multiline, type_name=int, default=None)>)>'
    
    
    

# Generated at 2022-06-13 19:43:42.223417
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Short description.

    Long description.
    Blah blah blah...

    Parameters
    ----------
    arg1 : str
        Use this to do this.
    arg2 : int
        Use this to do that.
    """

# Generated at 2022-06-13 19:43:46.195185
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    import json

    text_paragraphs = [
        """
        A short description of the function.

        A long description of the function.

        Parameters
        ----------
        arg1 : type
            Description of arg1
        arg2 : type
            Description of arg2

        Returns
        -------
        retval : type
            Description of return value
        """
    ]

    for text in text_paragraphs:
        docstring = parse(text)
        json_string = docstring.to_json()
        json_dict = json.loads(json_string)
        check_json_dict_defined(json_dict)


# Generated at 2022-06-13 19:43:57.012013
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print("Executing test_NumpydocParser_parse")
    doc_string = """This is a test docstring
    
    For testing the parsing of an numpydoc style docstring.
    
    Parameters
    ----------
    test : str
        Test parameter
    another_test : int = 7
        Another test parameter; this one has an optional default value
    """
    doc = NumpydocParser().parse(doc_string)

# Generated at 2022-06-13 19:44:07.265164
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """\
        A test sentence.

        A longer sentence.

        Parameters
        ----------
        a : bool
            A bool
        b, optional
            A bool

        Other Parameters
        ----------------
        b : int, optional
            A bool

        Returns
        -------
        bool
            A bool

        Yields
        ------
        x : bool, optional
            A bool

        Raises
        ------
        ValueError
            A bool

        Examples
        --------
        A bool

        Warnings
        --------
        A bool

        See Also
        --------
        A bool

        Notes
        -----
        A bool

        References
        ----------
        A bool

        Example
        -------
        A bool
        """
    parser = NumpydocParser()
    docstring = parser.parse(text)
    assert isinstance

# Generated at 2022-06-13 19:44:18.963871
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """A short summary of the method
    A long description of the method.
    This can span multiple lines.

    Parameters
    ----------
    arg_1 : int
        A description of the first argument.
    arg_2 : str
        A description of the second argument, which also has a : in it.
    arg_3 : (float, float)
        A description of the third argument.

    Returns
    -------
    return_1 : list
        A description of the first return value.
    return_2 : int
        A description of the second return value.

    """
    ds = parse(text)
    assert(ds.__class__ == Docstring)
    assert(ds.short_description == "A short summary of the method")

# Generated at 2022-06-13 19:44:32.013237
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Test method parse of class NumpydocParser."""
    npdp = NumpydocParser()
    test_str = """
    :param arg1: description of arg1
    :type arg1: int
    :param arg2: description of arg2
    :type arg2: str
    :return: None
    """

# Generated at 2022-06-13 19:44:42.247079
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    text = """
    Function to be tested.
    This is a long description
    of the function.

    Parameters
    ----------
    param1 : type
        description of param1

    param2 : type
        description of param2

    Returns
    -------
    type
        description of return value

    See Also
    --------
    another_function : description of the function
        with a second line of description
    """
    parsed = parser.parse(text)
    assert parsed.short_description == "Function to be tested."
    assert parsed.blank_after_short_description == False
    assert parsed.blank_after_long_description == True
    assert parsed.long_description == "This is a long description\nof the function."
    assert len(parsed.meta) == 4
    assert parsed

# Generated at 2022-06-13 19:44:50.344604
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    f = None # parse the docstring with " = " as default

# Generated at 2022-06-13 19:44:52.146766
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    np = NumpydocParser()
    text = """
    # Example docstring

    Parameters
    ----------
    a : int
        The number of times to say hello.

    Returns
    -------
    None
    """
    np.parse(text)

# Generated at 2022-06-13 19:44:59.187261
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    assert NumpydocParser().parse("") == Docstring()
    assert NumpydocParser().parse("something") == Docstring(
        short_description="something", blank_after_short_description=True,
        blank_after_long_description=True)
    assert NumpydocParser().parse("something\n") == Docstring(
        short_description="something", blank_after_short_description=False,
        blank_after_long_description=True)
    assert NumpydocParser().parse("something\n\n") == Docstring(
        short_description="something", blank_after_short_description=True,
        blank_after_long_description=False)

# Generated at 2022-06-13 19:45:10.390813
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:45:22.757486
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    # Documenting a module
    docstring = '''
    Module doctests

    This module contains a function and a classes used in different doctests.
    '''
    assert parser.parse(docstring).short_description == 'Module doctests'
    assert parser.parse(docstring).long_description == 'This module contains a function and a classes used in different doctests.'

    # Documenting a function
    docstring = '''
    A sample function

    This is a sample function that does nothing but making a print.

    .. note::
        This is a note

    Parameters
    ----------
    arg : int
        The argument to print
    '''

    docstring = parser.parse(docstring)
    assert docstring.short_description == 'A sample function'
    assert docstring.long_description

# Generated at 2022-06-13 19:45:31.825025
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

# Generated at 2022-06-13 19:45:42.851480
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # test case 1
    text = """
    foo()
        Test description

        Parameters
        ----------
        p : int, optional
             parameter description

        Returns
        -------
        str
            return description

        Raises
        ------
        RuntimeError
            if error encountered
    """
    docstring = NumpydocParser().parse(text)
    # test for short_description
    assert docstring.short_description == "foo()"
    # test for blank_after_short_description
    assert docstring.blank_after_short_description is True
    # test for long_description
    assert docstring.long_description == "Test description"
    # test for blank_after_long_description
    assert docstring.blank_after_long_description is True
    # test for param

# Generated at 2022-06-13 19:46:02.685570
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:46:13.765299
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:46:26.403240
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .common import DocstringMeta
    text = '''
    This is a short description of rewind_y
    This is a long description of rewind_y
    It can span many rows
    It can span even more
    Parameters
    ----------
    arg1: int
        arg1 description
    arg2: str
        arg2 description
    bla
    bla
    Params
    ------
    arg3: int
        arg3 description
    arg4: str
        arg4 description
    bla
    bla
    Returns
    -------
    type
        return description
        it can span many rows
        and even more

    '''

    docstring = NumpydocParser().parse(text)

    assert docstring.short_description == 'This is a short description of rewind_y'
    assert docstring.long

# Generated at 2022-06-13 19:46:33.434012
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()
    docstring = inspect.getdoc(parse)
    parsed = parser.parse(docstring)
    assert parsed.short_description == "Parse the numpy-style docstring into its components."
    assert len(parsed.meta) == 0
    assert parsed.long_description is None
    assert parsed.blank_after_short_description
    assert not parsed.blank_after_long_description

# Generated at 2022-06-13 19:46:40.977111
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    a = """This is a short description of the function.

And this is a long description.

The long description is optional and may be omitted.

Parameters
----------
arg1 : int
    The first argument.
arg2 : str
    The second argument.

Raises
------
ValueError
    If *arg2* is equal to ``'raised'``.

Returns
-------
bool
    Whether or not the arguments are equal.

"""
    print(parse(a))
    print(parse(a).long_description)


if __name__ == "__main__":
    d = """This is a short description of the function.

And this is a long description.

The long description is optional and may be omitted.

"""

    print(parse(d))
    print(parse(d).long_description)

# Generated at 2022-06-13 19:46:54.254755
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:47:02.748939
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Test for method parse of class NumpydocParser"""
    text = """Takes a string and reverses it.
    This method should be used for testing only.

    Parameters
    ----------
    text : str
        The string to reverse.

    Returns
    -------
    str
        The reversed string.

    Raises
    ------
    ValueError
        If the passed text is not actually a string.
    """

    docstring_meta = Docstring()
    docstring_meta.short_description = "Takes a string and reverses it."
    docstring_meta.long_description = "This method should be used" \
                                      "for testing only."
    docstring_meta.blank_after_long_description = True
    docstring_meta.blank_after_short_description = True

    docstring_param = DocstringParam

# Generated at 2022-06-13 19:47:14.441084
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    ndp = NumpydocParser()

# Generated at 2022-06-13 19:47:22.194662
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from tests.test_docstring import DocstringTestCase

    docstring = '''   A short summary
    
    A longer description
    
    Parameters
      arg_name: type
        A description of what this arg does and why it's required
      arg2 : int
        A description of this optional arg
    
      multiple
      lines
    
      other_arg(optional): another_type
    
      final_arg : str, optional, defaults to 'string'
        A description of the final arg; the type is optional but the
          default is required.
    
    Returns
      return_name: int
        A description of the return value; this can also span multiple lines
      float
        Return names are optional, types are required
    '''

    parser = NumpydocParser(None)
    self = DocstringTestCase(parser)
   

# Generated at 2022-06-13 19:47:27.023588
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    parser = NumpydocParser()

    # code snippet from https://numpydoc.readthedocs.io/en/latest/format.html#information-fields
    # Original docstring

# Generated at 2022-06-13 19:47:45.565045
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    text = """Summary line.

    Extended description of this method.

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
    """
    parser = NumpydocParser()
    r = parser.parse(text)

    assert r.short_description == 'Summary line.'
    assert r.long_description == 'Extended description of this method.'

    assert r.meta[0].args == [ 'param', 'arg1' ]
    assert r.meta[0].description == 'Description of `arg1`'

    assert r.meta[1].args == [ 'param', 'arg2' ]
    assert r.meta[1].description == 'Description of `arg2`'


# Generated at 2022-06-13 19:47:56.983161
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print("Testing for NumpydocParser_parse...")
    parser = NumpydocParser()
    docstring = parser.parse("""This is the short description.

And this is the long one.

Parameters
----------
first_param : :class:`int`
    The first parameter.

second_param : :class:`str`
    The second one.

Raises
------
:exc:`~exceptions.TypeError`
    When a parameter is not a string.

:exc:`~exceptions.ValueError`
    When a parameter is empty.

""")
    assert len(docstring.meta) == 2
    assert docstring.meta[0].name == "param"
    assert len(docstring.meta[0].args) == 2

# Generated at 2022-06-13 19:48:09.839932
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    data = """
    pydocstring.parse_numpy(text)
    Parse the numpy-style docstring into its components.

    :returns: parsed docstring

    Parameters
    ----------
    text : str
        Docstring to parse.

    Raises
    ------
    ValueError
        Raises this error if ``text`` is not a valid numpy docstring.
    """

    result = NumpydocParser().parse(data)
    assert len(result.meta) == 2
    assert result.meta[0].args == ['returns']
    assert result.meta[0].description == "parsed docstring"
    assert result.meta[1].args == ['param', 'text']
    assert result.meta[1].description == "Docstring to parse."

# Generated at 2022-06-13 19:48:19.514077
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    # Test case 1
    text = """Test description.
              Parameter
                  Test description.
              Return
                  Test description.
              See Also
                  Test description."""

    ret = Docstring()
    ret.short_description = "Test description."
    ret.long_description = "Parameter\n    Test description.\nReturn\n    Test description.\nSee Also\n    Test description."

# Generated at 2022-06-13 19:48:23.915974
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    docstring = NumpydocParser().parse("""
    One sentence summary

    Parameters
    ----------
    arg1 : str
        Description for arg1.
    arg2 : float
        Description for arg2.
    arg3 : int, optional
        Description for arg3.
    arg4 : int, optional
        Description for arg4. Default is 0.

    Other Parameters
    ----------------
    other_arg1 : str
        Description for other_arg1.

    Raises
    ------
    ValueError
        Description of what could raise ValueError.

    Returns
    -------
    return1 : str
        Description of return1.
    return2 : float
        Description of return2.
    """)

    assert docstring.short_description == "One sentence summary"
    assert docstring.long_description == ""
    assert docstring.blank

# Generated at 2022-06-13 19:48:26.423959
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .test_common import test_parse
    test_parse(parse)

# Generated at 2022-06-13 19:48:37.556274
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """\
    This is an example
    
    Parameters
    ----------
    
    arg1 : str
        arg1 description
    arg2 : float
        arg2 description
    arg3, optional : bool
        arg3 description
    
    Raises
    ------
    
    TypeError
        If arg1 is not str
    ValueError
        If arg2 is not in [0, 1]
    
    Returns
    -------
    
    return_a : int
        Return a description
    
    Yields
    ------
    
    return_b : str
        Return b description
    
    """
    docstring = NumpydocParser().parse(text)
    assert docstring.short_description == 'This is an example'
    assert docstring.long_description == None
    assert docstring.blank_after

# Generated at 2022-06-13 19:48:47.265129
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:48:58.240764
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    example1 = """
    Parameters
    ----------

    doc:
        A valid numpydoc docstring.
    """
    example2 = """
    Args
    ----
    arg_name : type_name
        description
    arg_name : type_name, optional
        description
    arg_name : type_name, default=value
        description
    arg_name : type_name, default=value (optional)
        description
    arg_name (type_name, default=value)
        description
    arg_name (type_name)
        description
    arg_name (type_name)
        description
    """

    docstring = NumpydocParser().parse(example1)
    assert docstring.meta[0].args == ['param', 'doc']

# Generated at 2022-06-13 19:49:03.308111
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
        docstring_1
            This is short description.
            It also includes long description.
        Parameters
            param_1 : type_1
                Description of first parameter
            param_2 : type_2
                Description of second parameter
        Raises
            ValueError
                If a value is wrong
        Returns
            param_1
                Description of the return value
    """
    print(parse(text))


# Generated at 2022-06-13 19:49:23.090535
# Unit test for method parse of class NumpydocParser

# Generated at 2022-06-13 19:49:32.689249
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    text = """
    Short description.

    Longer description.

    Parameters
    ----------
    foo
        Description of foo.
    bar : str
        Description of bar.
    kwarg : True or False, optional
        This is True by default.
    """
    docstring = NumpydocParser().parse(text)
    assert docstring.short_description == "Short description."
    assert docstring.long_description == "Longer description."
    assert docstring.meta[0].args == ["param", "foo"]
    assert docstring.meta[0].description == "Description of foo."
    assert docstring.meta[1].args == ["param", "bar"]
    assert docstring.meta[1].description == "Description of bar."
    assert docstring.meta[1].type_name == "str"
    assert doc

# Generated at 2022-06-13 19:49:39.654225
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    docstring = '''
        This is a function.

        Parameters
        ----------
        arg1 : int
            first argument.
        arg2 : int
            second argument.

        Returns
        -------
        int
            return value
        '''
    docstring_parser = NumpydocParser.parse(docstring)
    print(docstring_parser)

if __name__ == '__main__':
    test_NumpydocParser_parse()

# Generated at 2022-06-13 19:49:43.853751
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    print('[py2docstring] - [test_NumpydocParser_parse] - [Start]')
    print('[py2docstring] - [test_NumpydocParser_parse] - [End]')
    
    

# Generated at 2022-06-13 19:49:56.974728
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():

    def docstring():
        """
        short desc
        long desc

        Parameters:
            a: int
                param desc
            b : str, optional
                optional param desc
            c(optional) : bool

        Returns:
            something

        Raises:
            KeyError
                something raises keyerror

        Warns:
            UserWarning
                something warns userwarning

        Examples:
            >>> a = 2
            >>> b = 3

        Warnings:
            use wisely

        See Also:
            :func:`foo`

        Notes:
            some notes

        References:
            .. [1] A reference

        Deprecated: 1.0
            use :func:`foo` instead
        """

    cls = NumpydocParser()
    cls.parse(docstring())



parse.__doc__ = Numpydoc

# Generated at 2022-06-13 19:50:07.382466
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    from .test_common import get_test_data
    test_dataset = get_test_data("numpydoc")
    for data in test_dataset:
        str_docstring = data["docstring"]
        # Parse numpydoc to Docstring object
        docstring = NumpydocParser().parse(str_docstring)
        # Unit tests
        if data["meta"]["short-description"]:
            assert docstring.short_description == data["meta"]["short-description"]
            assert docstring.long_description == data["meta"]["long-description"]
        else:
            assert docstring.short_description == ''
            assert docstring.long_description == ''
        if data["meta"]["blank-after-short-description"]:
            assert docstring.blank_after_short

# Generated at 2022-06-13 19:50:12.349802
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    #para = parse(text)
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test_NumpydocParser_parse()

    #
    import doctest
    doctest.testmod()
    #doctest.testfile(test, module_relative=True)
    #print (parse(text))

# Generated at 2022-06-13 19:50:25.073745
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    """Unit test for method parse of class NumpydocParser.

    """
    # Test case 1, Description part, short description
    test_docstring = """\
    pydocstyle is purely written in Python and
    has many features.
    Parameters
    ----------
    arg1 : type
        The first argument.
    arg2 :   str
        The second argument.
    Returns
    -------
    str
        The return value. True on success, False otherwise.
    """
    ret = NumpydocParser().parse(test_docstring)
    assert ret.short_description == "pydocstyle is purely written in Python and"
    assert ret.blank_after_short_description is False
    assert ret.blank_after_long_description is False
    assert ret.long_description == "has many features."

    # Test case

# Generated at 2022-06-13 19:50:28.137646
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    INPUT='docstring'
    EXPECTED=Docstring(short_description='docstring',
                       long_description=None,
                       blank_after_short_description=False,
                       blank_after_long_description=False,
                       meta=[])
    RETURNED=NumpydocParser().parse(INPUT)
    assert RETURNED == EXPECTED


# Generated at 2022-06-13 19:50:39.620127
# Unit test for method parse of class NumpydocParser
def test_NumpydocParser_parse():
    ndp = NumpydocParser()

# Generated at 2022-06-13 19:50:56.155087
# Unit test for constructor of class YieldsSection
def test_YieldsSection():
    test_yields = YieldsSection('Yields', 'yields')
    assert test_yields.is_generator == True
    assert test_yields.key == 'yields'
    assert test_yields.title == 'Yields'
    assert test_yields.title_pattern == r'^\.\.\s*(Yields)\s*::'


# Generated at 2022-06-13 19:51:02.464425
# Unit test for method add_section of class NumpydocParser
def test_NumpydocParser_add_section():
    parser = NumpydocParser()
    test_section = Section("test", "test")
    parser.add_section(test_section)
    assert parser.sections[test_section.title] == test_section
    assert parser.sections["test"].title == "test"
    assert parser.sections["test"].key == "test"




# Generated at 2022-06-13 19:51:12.311164
# Unit test for constructor of class ParamSection
def test_ParamSection():
    test_text = r'''
    x : int
        The x coordinate
    y : int
        The y coordinate
    '''
    param_section = ParamSection("Parameters", "param")
    docstring = Docstring()
    docstring.meta = [meta for meta in param_section.parse(test_text)]
    assert [meta.arg_name for meta in docstring.meta] == ['x', 'y']
    assert [meta.type_name for meta in docstring.meta] == ['int', 'int']
    assert [meta.is_optional for meta in docstring.meta] == [False, False]

# Generated at 2022-06-13 19:51:13.227419
# Unit test for constructor of class NumpydocParser
def test_NumpydocParser():
    pass


# Generated at 2022-06-13 19:51:18.154164
# Unit test for constructor of class RaisesSection
def test_RaisesSection(): 
    parser = NumpydocParser()
    assert(parser.sections["Raises"].title == "Raises")
    assert(parser.sections["Raises"].key == "raises")
    assert(parser.sections["Raises"].title_pattern == r"^(Raises)\s*?\n-*\s*$")
