

# Generated at 2022-06-13 19:41:31.304911
# Unit test for function parse
def test_parse():
    """Test for function parse"""
    doc1 = '''
    :param name:
    :type name: str
    :param age:
    :type age: int
    '''
    doc2 = '''
    :param name:
    :type name: str
    :param age:
    :type age: int

    :return:
    :rtype: list
    '''
    assert parse(doc1).specials != parse(doc2).specials
    assert parse(doc2).specials[2].name == "return"


# Generated at 2022-06-13 19:41:36.149158
# Unit test for function parse
def test_parse():
    docstring = parse("""\
        Parameters
        ----------
        a : int
            description
    """)
    assert docstring.params[0].name == "a"
    assert docstring.params[0].type == "int"
    assert docstring.params[0].desc == "description"

    # We can use either '.type' or '.annotation' for the same property.
    assert docstring.params[0].annotation == "int"

# Generated at 2022-06-13 19:41:41.459331
# Unit test for function parse
def test_parse():
    docstring = parse('''
    """This is a docstring.
    
    This is the second line of the docstring.
    
    Parameters
    ----------
    a : int
        The first parameter.
    b : str
        The second parameter.
    
    Returns
    -------
    retval1 : int
        Return value.  The first paragraph of the description.
        The second paragraph of the description.
    retval2 : str
        Return value.  The only description.
    """
    ''')
    print(docstring)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:41:49.283624
# Unit test for function parse
def test_parse():
    docstring = '''Description:
    This is a test docstring.
    
Args:
  arg1 (str): arg1 description
  arg2 (int): arg2 description
    
Returns:
  str: returns something
'''
    doc = parse(docstring)
    print(doc.short_description)
    print(doc.long_description)
    print(doc.args)
    print(doc.returns)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:41:52.571238
# Unit test for function parse
def test_parse():
    text="""
    This is a DocstringParser.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    ret = parse(text)
    print(ret)


# Generated at 2022-06-13 19:41:56.561021
# Unit test for function parse
def test_parse():
    from docstring_parser import parse
    from docstring_parser.styles.google import GoogleStyle
    text = '''
        The main parsing routine.

        Args:
            text: docstring text to parse
            style: docstring style
        Returns:
            parsed docstring representation
        '''
    assert parse(text) == GoogleStyle(text).get_docstring()

# Generated at 2022-06-13 19:42:04.448415
# Unit test for function parse
def test_parse():
    """Unit test for core.parse()."""

    raw = \
"""
Example function with types documented in the docstring.

Args:
  param1 (int): The first parameter.
  param2 (str): The second parameter.
Returns:
  bool: The return value. True for success, False otherwise.

"""
    pydocstyle = parse(raw, STYLES.pydocstyle)
    print(pydocstyle)
    numpydoc = parse(raw, STYLES.numpydoc)
    print(numpydoc)


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:42:10.412794
# Unit test for function parse
def test_parse():
    docstring = """
    Test function for `docstring_parser.parse`.
    
    Examples:
        >>> foo = "bar"
        >>> print(foo)
        "bar"
    """

    parsed = parse(docstring, style=Style.google)

    assert parsed.short_description == 'Test function for `docstring_parser.parse`.'
    assert parsed.long_description == '\nExamples:\n    >>> foo = "bar"\n    >>> print(foo)\n    "bar"'
    assert parsed.meta == {}

# Generated at 2022-06-13 19:42:19.919233
# Unit test for function parse
def test_parse():
    """Test the parse function."""
    ds = parse("""
    This function does some stuff.

    :param query: Query to search for
    :type query: str
    :param limit: Number of results to show
    :type limit: int
    :raises ValueError: If no query is provided
    :returns: Search results
    :rtype: dict
    """)
    print(ds.params)
    print(ds.returns)
    print(ds.raises)
    print(ds.meta)

# Generated at 2022-06-13 19:42:25.410739
# Unit test for function parse
def test_parse():
    import sys
    style = Style.auto
    text = """
        This is a simple string.
        This is a multi-line string.
        More lines.
    """
    if __name__ == '__main__':
        style = sys.argv[1]
        text = sys.argv[2]
        
    print(parse(text, style))

# Generated at 2022-06-13 19:42:32.714622
# Unit test for function parse
def test_parse():
    """Basic parse tests for func parse
    """
    text = '''
    This is a docstring
    '''
    return parse(text)
    #assert parse(text).short_description == 'This is a docstring'

# Generated at 2022-06-13 19:42:39.846345
# Unit test for function parse
def test_parse():
    assert parse('hello world') == Docstring(
        content=['hello world'],
        meta={},
        fields=[],
        warnings=[],
        style=Style.auto,
    )
    assert parse(':param x: abc', style=Style.google) == Docstring(
        content=[''],
        meta={},
        fields=[('param', 'x', ['abc'])],
        warnings=[],
        style=Style.google,
    )
    assert parse(':param x: abc', style=Style.numpy) == Docstring(
        content=[''],
        meta={},
        fields=[('param', 'x', ['abc'])],
        warnings=[],
        style=Style.numpy,
    )

# Generated at 2022-06-13 19:42:47.701037
# Unit test for function parse
def test_parse():
    text='\n        Create a new user.\n\n        :param str first_name: First name\n        :param str last_name: Last name\n        :param int age: Age\n        :param str phone: Phone\n        :param str address: Address\n        :param str occupation: Occupation\n        :returns: New user\n        :rtype: :py:class:`User <User>`\n        :raises: :py:exc:`ValueError`\n        \n        This is an example of a long description.\n        '

    style=Style.googledoc
    ret=parse(text=text, style=style)
    print(ret)


# unit test for class Docstring

# Generated at 2022-06-13 19:42:55.950467
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    text = '''\
    :param name: The name to use.
    :param state: Whether to print 'hello' or 'goodbye'
    :param exception: An exception to raise
    :raises: :exception:
    '''
    docstring = parse(text)
    assert docstring.params['name'] == 'The name to use.'
    assert docstring.params['state'] == "Whether to print 'hello' or 'goodbye'"
    assert docstring.params['exception'] == 'An exception to raise'
    assert docstring.raises['exception'] == None


# Generated at 2022-06-13 19:43:00.282234
# Unit test for function parse
def test_parse():
    docstring = """This is a docstring."""
    docstring_obj = parse(docstring, Style.google)
    print(docstring_obj.meta)
    print(docstring_obj.short_description) 
    print(docstring_obj.long_description) 
    print(docstring_obj.returns) 
    print(docstring_obj.raises) 
    print(docstring_obj.params) 
    print(docstring_obj.attributes) 
    print(docstring_obj.lineage) 
    print(docstring_obj.see_also) 
    print(docstring_obj.warnings) 

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:43:10.464395
# Unit test for function parse
def test_parse():
    text = """
    Function to perform PCA on the dataset
    Parameters
    ----------
    data: DataFrame
        Dataset that needs to be transformed
    y_cols: list, optional
        List of y columns (default: None)
    n_comp: int, optional
        Number of components to return (default: 8)
    Returns
    -------
    pca_data: DataFrame
        Data with principal components
    """
    docstring = parse(text, Style.google)
    assert docstring.short_description == "Function to perform PCA on the dataset"
    assert len(docstring.long_description) == 0
    assert len(docstring.features) == 3

# Generated at 2022-06-13 19:43:12.896866
# Unit test for function parse
def test_parse():
    assert parse('print "Hello, World!"').summary == 'print string'

if __name__=='__main__':
    test_parse()

# Generated at 2022-06-13 19:43:18.273304
# Unit test for function parse
def test_parse():
    docstring_text = """This is a test.
    :param n: the desired number
    :type n: int
    :returns: 1 or 0"""
    docstring = parse(docstring_text)
    assert docstring.meta['n']['type'] == 'int'
    assert docstring.meta['returns']['type'] == '1 or 0'


# Generated at 2022-06-13 19:43:25.088315
# Unit test for function parse
def test_parse():
    text = """
    Title
    -----
    This is the summary.

    :param x: The first argument.
    :param y: The second argument.
    :returns: A boolean value.
    """
    d = parse(text)
    assert d.title == 'Title'
    assert d.summary == 'This is the summary.'
    assert d.meta['args'] == ['x', 'y']
    assert d.meta['returns'] == 'A boolean value.'

# Generated at 2022-06-13 19:43:39.540742
# Unit test for function parse
def test_parse():
    text = """
        Test docstring

        Args:
        arg1: Arg 1
        arg2: arg 2

        Returns:
        ret1: Ret 1
        ret2: Ret 2

        Raises:
        err1: Err 1
    """
    d = parse(text)
    assert d.short_description == 'Test docstring'
    assert d.long_description == None
    assert d.sections[0].name == 'args'
    assert d.sections[1].name == 'returns'
    assert d.sections[2].name == 'raises'
    assert d.sections[0].content == d.sections[0].parsed()
    assert d.sections[1].content == d.sections[1].parsed()
    assert d.sections[2].content == d.sections[2].parsed

# Generated at 2022-06-13 19:43:53.402321
# Unit test for function parse
def test_parse():
    ds = parse('Summary line.\n\nThis is a description.')
    assert len(ds) == 2
    assert ds.summary == 'Summary line.'

    ds = parse('Summary line.\n\nThis is a description.\n\nArgs:\n    arg1 (int): This is the first argument.\n\nReturns:\n    int: This is a return value.')
    assert len(ds) == 5
    assert ds.args == [('arg1', 'int', 'This is the first argument.')]
    assert ds.returns == ['int', 'This is a return value.']

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:43:59.204187
# Unit test for function parse
def test_parse():
    text = '''
            Creates a new file

            :param path: path to create
            :raise IOError: if it cannot be created
            '''
    parsed_docstring = parse(text)
    assert parsed_docstring.short_description == 'Creates a new file'
    assert parsed_docstring.params['path'].description == 'path to create'
    assert parsed_docstring.raises['IOError'].description == 'if it cannot be created'

# Generated at 2022-06-13 19:44:08.995312
# Unit test for function parse
def test_parse():
    docstring = parse("""
    This function does something.
    """
    )
    assert docstring.short_description == 'This function does something.'

    docstring = parse("""
    This function does something.

    This is the long description.
    """
    )
    assert docstring.short_description == 'This function does something.'
    assert docstring.long_description == 'This is the long description.'

    docstring = parse("""
    This function does something.

    :param foo: parameter description
    :type foo: int
    :param bar: parameter description
    :type bar: str
    """
    )

# Generated at 2022-06-13 19:44:11.167540
# Unit test for function parse
def test_parse():
    from docstring_parser.common import ParseError
    try:
        parse("test")
    except ParseError:
        pass
    else:
        assert False

# Generated at 2022-06-13 19:44:19.063196
# Unit test for function parse
def test_parse():
    assert parse("This is a test.") == Docstring(meta=[], description="This is a test.")
    assert parse("This is a test.\nMore text.") == Docstring(meta=[], description="This is a test.\nMore text.")
    assert parse("""
            This is a test.

            More text.
            """) == Docstring(meta=[], description="""
            This is a test.

            More text.
            """)
    assert parse("""
            This is a test.

            This is a test.
            """) == Docstring(meta=[], description="""
            This is a test.

            This is a test.
            """)

# Generated at 2022-06-13 19:44:32.093755
# Unit test for function parse
def test_parse():
    text = '''
    Lorem ipsum dolor sit amet
    
    :param a: blah blah
    :param b: blah blah
    :return: blah blah
    '''
    assert parse(text) == parse(text,style=Style.google)
    assert parse(text) == parse(text,style=Style.numpy)
    assert parse(text) == parse(text,style=Style.pep257)
    assert parse(text) == parse(text,style=Style.auto)
    text = '''
    Lorem ipsum dolor sit amet
    
    Args:
        a (int): blah blah
        b (int): blah blah
    Returns:
        int: blah blah
    '''
    assert parse(text) == parse(text,style=Style.google)

# Generated at 2022-06-13 19:44:35.296411
# Unit test for function parse
def test_parse():
    import sys
    import os
    import doctest
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    import docstring_parser
    doctest.testmod(docstring_parser)

# Generated at 2022-06-13 19:44:36.672056
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()


# Generated at 2022-06-13 19:44:42.500575
# Unit test for function parse
def test_parse():
    text = """Summary line.
    Description.
    Description continued.
    Args:
        arg1 (int): Description.
        arg2 (str): Description continued.
        arg3 (Optional[str]): Description.
    Returns:
        bool: Description.
    Raises:
        AttributeError, KeyError: Description.
    """

    docstring = parse(text, Style.google)
    print(docstring)

test_parse()

# Generated at 2022-06-13 19:44:49.736989
# Unit test for function parse
def test_parse():
    text = '''
    """This is a docstring.
    
    I hope you enjoy it.
    
    Args:
        a: argument a
        b: argument b
    
    Returns
        c (float): something
    """
    '''
    doc = parse(text)
    assert doc.short_description.strip() == 'This is a docstring.'
    assert doc.long_description.strip() == 'I hope you enjoy it.'
    assert len(doc.arguments) == 2
    assert len(doc.returns) == 1
    assert doc.returns[0].type_annotation is not None


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:44:59.522395
# Unit test for function parse
def test_parse():
    expected = "Follows the google docstring format."
    output = parse("""
    Parse a string into a docstring object.
    Args:
      text (str):
        The docstring to parse.
    Returns:
      Docstring: The parsed docstring.
    Raises:
      ParseError:
        If there was a problem parsing ``text``.
      ValueError:
        If there was a problem parsing ``text``.
    """)

    assert expected == output.short_description

# Generated at 2022-06-13 19:45:10.658913
# Unit test for function parse
def test_parse():
    expected = [{'title': 'some docstring', 'text': 'some text', 'meta': '', 'tags': []},
                {'title': 'some docstring', 'text': 'other text', 'meta': '', 'tags': []}]
    result = parse('some title\n'
                   'some docstring\n'
                   '================\n'
                   '\n'
                   'some text\n'
                   '\n'
                   'some title\n'
                   'some docstring\n'
                   '================\n'
                   '\n'
                   'other text')
    assert isinstance(result, Docstring)
    assert result.title == expected[0]['title']
    assert result.text == expected[0]['text']
    assert result.meta == expected[0]['meta']
    assert result

# Generated at 2022-06-13 19:45:13.081757
# Unit test for function parse
def test_parse():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 19:45:23.317822
# Unit test for function parse
def test_parse():
    """Test function parse."""
    text = '''
    This is a docstring.

    :param one: the first parameter
    :param two: the second parameter
    :return: something
    '''
    docstring = parse(text)
    assert docstring.short_description == 'This is a docstring.'
    assert docstring.summary == docstring.short_description
    assert len(docstring.long_description) == 0
    assert len(docstring.meta) == 3
    assert docstring.meta['param'][0].args[0] == 'one'
    assert docstring.meta['param'][0].description == 'the first parameter'
    assert docstring.meta['param'][1].args[0] == 'two'
    assert docstring.meta['param'][1].description == 'the second parameter'
   

# Generated at 2022-06-13 19:45:32.240554
# Unit test for function parse
def test_parse():
    doc1 = """One-line summary.

Extended description.

Parameters
----------
arg1 : int
    Description of `arg1`
arg2 : str
    Description of `arg2`
"""
    doc2 = """One-line summary.

:param arg1: Description of arg1
:type arg1: int
:param arg2: Description of arg2
:type arg2: str
"""
    doc3 = """One-line summary.

:Parameters: **arg1** : int
    Description of arg1
    **arg2** : str
    Description of arg2
"""
    doc4 = """One-line summary.

Args:
    arg1 (int): Description of `arg1`
    arg2 (str): Description of `arg2`
"""

# Generated at 2022-06-13 19:45:38.275073
# Unit test for function parse
def test_parse():
    text = """A docstring.

       This is a docstring.
       Args:
           foo: The first parameter.
           bar: The second parameter.
       Returns:
           None
       """
    docstring = parse(text)

    assert docstring.short_description == "A docstring."
    assert docstring.long_description == "This is a docstring."
    assert docstring.returns == "None"

# Generated at 2022-06-13 19:45:46.082861
# Unit test for function parse
def test_parse():
    print('Testing function parse')
    docstring_text = '''
    Input: a list of integers
    Output: a list of integers
    Function: to remove the duplicates
    '''
    docstring_parse = Docstring(
        short_description = '',
        long_description = '',
        meta = {
            'Input': 'a list of integers',
            'Output': 'a list of integers',
            'Function': 'to remove the duplicates'
        },
        examples = [],
        references = [],
    )
    docstring = parse(docstring_text, style = 'google')
    assert docstring == docstring_parse
    print('Function parse is good!')

test_parse()

# Generated at 2022-06-13 19:45:53.584929
# Unit test for function parse
def test_parse():
    doc = '''This function does something.

:param a: first parameter
:param b: second parameter
:return: something
:raises TypeError: when something goes wrong

Examples:
    >>> print(something(42))
    None
'''
    ret = parse(doc)

    assert ret.short_description == 'This function does something.'
    assert ret.long_description == 'Examples:\n    >>> print(something(42))\n    None'
    assert ret.returns.description == 'something'
    assert ret.meta['param']['a'].description == 'first parameter'
    assert ret.meta['param']['b'].description == 'second parameter'
    assert ret.meta['raises']['TypeError'].description == 'when something goes wrong'



# Generated at 2022-06-13 19:45:55.540479
# Unit test for function parse
def test_parse():
    # Forgive me
    assert(parse("hello", Style.numpy).short_description == "hello")

# Generated at 2022-06-13 19:46:06.945056
# Unit test for function parse

# Generated at 2022-06-13 19:46:12.563626
# Unit test for function parse
def test_parse():
    docstring = '''hello world'''
    result = parse(docstring)
    print(result)
# test_parse()

# Generated at 2022-06-13 19:46:14.486618
# Unit test for function parse
def test_parse():
    assert parse('', Style.rst) == Docstring()


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:46:20.365275
# Unit test for function parse
def test_parse():
    doc1 = parse(
"""Description
-----------
A docstring for python.

Args:
    a: A arg to pass
    b: Another arg to pass.

Returns:
    parsed: The parsed value.
""")
    assert isinstance(doc1, Docstring)
    # Test the docstring's attribute
    assert doc1.short_description == "Description"
    assert doc1.long_description == """A docstring for python."""
    assert len(doc1.params) == 2
    assert len(doc1.returns) == 1
    assert doc1.returns[0].type == "parsed"
    assert doc1.returns[0].name == """The parsed value."""
    assert doc1.returns[0].description == None
    # Test the docstring's meta information

# Generated at 2022-06-13 19:46:25.116881
# Unit test for function parse
def test_parse():
    d = parse('rst', Style.rst)
    assert d.short_description == ''
    assert d.long_description == ''
    assert d.meta == {}
    assert d.notes == []
    assert d.examples == []

    d = parse('numpy', Style.numpy)
    assert d.short_description == ''
    assert d.long_description == ''
    assert d.meta == {}
    assert d.notes == []
    assert d.examples == []

    d = parse('google', Style.google)
    assert d.short_description == ''
    assert d.long_description == ''
    assert d.meta == {}
    assert d.notes == []
    assert d.examples == []

    d = parse('sphinx', Style.sphinx)

# Generated at 2022-06-13 19:46:36.584642
# Unit test for function parse
def test_parse():
    txt1 = '''
    This is a test for the docstring
    
    It is to test the functionality of the parse function

    :param test: This is a test parameter
    :returns: This is the return value
    '''

    #Test case 1: test for valid parameters
    ret = parse(txt1)
    assert ret.short_description == 'This is a test for the docstring'
    assert ret.long_description == 'It is to test the functionality of the parse function'

    txt2 = '''
    This is a test for the docstring.

    It is to test the functionality of the parse function
    '''

    #Test case 2: test for missing fields in the docstring
    ret = parse(txt2)
    assert ret.short_description == 'This is a test for the docstring.'
    assert ret

# Generated at 2022-06-13 19:46:45.914351
# Unit test for function parse
def test_parse():
    docstring = """One-line short summary.

One-line long summary.

Args:
  arg1(int): Description of arg1
  arg2(str): Description of arg2

Returns:
  Description of return value

Raises:
  ValueError: If something bad happens
"""
    ret = parse(docstring, Style.google)
    assert ret.short_description == 'One-line short summary.'
    assert ret.long_description == 'One-line long summary.'
    assert len(ret.params) == 2
    assert len(ret.returns) == 1
    assert len(ret.raises) == 1
    assert len(ret.meta) == 4


# Generated at 2022-06-13 19:46:53.027590
# Unit test for function parse
def test_parse():
    from docstring_parser import parse
    text = '''A line with a some text in it.
    A second line of text that comes after a line break.
    '''
    ret = parse(text)
    assert ret.meta == {'summary': 'A line with a some text in it.'}
    assert 'A second line of text that comes after a line break.' in ret.description.text


# Generated at 2022-06-13 19:47:02.074665
# Unit test for function parse
def test_parse():
    docstring = '''
    Here is the description

    :param arg1:   arg1 information
    :type arg1:    str
    :param arg2:   arg2 information
    :type arg2:    int
    :returns:      return value description
    :rtype:        str
    '''
    doc = parse(docstring, style=Style.google)
    assert doc.short_description == 'Here is the description'
    assert doc.long_description == ''
    assert doc.return_type == 'str'
    assert doc.return_desc == 'return value description'
    assert len(doc.params) == 2
    assert doc.params[0].arg_name == 'arg1'
    assert doc.params[0].arg_type == 'str'

# Generated at 2022-06-13 19:47:14.126372
# Unit test for function parse
def test_parse():
    text = """  One line summary.

        Extended description.

        Args:
            arg_a (int): Description of `arg_a`
            arg_b (str): Description of `arg_b`

        Returns:
            str: Description of return value

        Raises:
            ValueError: If `arg_a` is equal to `arg_b`
        """
    docstring = parse(text)
    assert docstring.short_description == "One line summary."

# Generated at 2022-06-13 19:47:19.077076
# Unit test for function parse
def test_parse():
    """ Parse the docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    text = """This is a docstring of a function
        :param text: docstring text to parse
        :param style: docstring style
        :returns: parsed docstring representation
    """
    test_parse.__doc__ == parse(text)

test_parse()

# Generated at 2022-06-13 19:47:27.939504
# Unit test for function parse
def test_parse():
    assert parse.__doc__.strip() == """Parse the docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation"""


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 19:47:35.640810
# Unit test for function parse
def test_parse():
    text = '''
    """This is a simple test of the doctsting parser.

    :param first_param: this is the first param
    :param second_param: this is a second param
    :returns: this is a description of what is returned
    :raises keyError: raises an exception
    """
    '''
    expected_result = {
        'first_param':   'this is the first param',
        'second_param':  'this is a second param',
        'returns':       'this is a description of what is returned',
        'raises keyError':  'raises an exception'
    }
    actual_result = parse(text)
    assert expected_result == actual_result

# Generated at 2022-06-13 19:47:46.944578
# Unit test for function parse
def test_parse():
    text = "This is a test docstring.\n\nArgs: arg1 (int): Arg 1."
    docstring = parse(text, style = Style.google)
    assert docstring.short_description == "This is a test docstring."
    assert len(docstring.long_description) == 0
    assert len(docstring.params) == 1
    assert docstring.params[0].arg_name == "arg1"
    assert docstring.params[0].param_type == "int"
    assert docstring.params[0].description == "Arg 1."

    text = "This is a test docstring.\n\nArgs:\n\targ1 (int): Arg 1."
    docstring = parse(text, style = Style.numpydoc)

# Generated at 2022-06-13 19:47:58.113123
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleStyle
    text = """
            Short summary.
            More description.

            Args:
                arg1 (int): Description of arg1
                arg2 (str): Description of arg2
            Returns:
                bool: Description of return value
        """
    result = parse(text)
    assert result.title == ""
    assert result.description == "Short summary.\nMore description."
    assert result.returns == "bool: Description of return value"
    assert result.returns_description == "Description of return value"
    assert result.short_description == "Short summary."
    assert result.long_description == "More description."
    assert result.meta["args"]["arg1"] == "Description of arg1"

# Generated at 2022-06-13 19:48:10.754735
# Unit test for function parse
def test_parse():
    from docstring_parser.__version__ import __version__
    from docstring_parser.conf import Config
    from docstring_parser.docstring import Parameter
    from docstring_parser.styles import Style
    from docstring_parser import parse 
    
    text = '''
        Adds two numbers.
        
        Args:
            param1 (int): The first parameter.
            param2 (int, optional): The second parameter. Defaults to None.
        
        Returns:
            int: The return value.
    '''
    docstring = parse(text) 
    assert docstring.short_description == 'Adds two numbers.'
    assert docstring.long_description == ''
    assert len(docstring.params) == 2
    assert docstring.params[0].type == 'int'

# Generated at 2022-06-13 19:48:20.169540
# Unit test for function parse
def test_parse():
    text = '''\
    function(
        # this is a arg
        arg1=None,
        arg2=None,
        # this is a kwarg
        *kwargs,
        # this is a vararg
        **varkwargs,
        # this is a arg
        arg3=None,
        arg4=None,
        # this is a kwarg
        *kwargs,
        # this is a vararg
        **varkwargs,
    )
        '''
    print(text)
    print()


# Generated at 2022-06-13 19:48:30.807836
# Unit test for function parse
def test_parse():
    text = """
        Not a docstring
    """
    try:
        doc = parse(text)
        assert False
    except ParseError:
        pass

    text = """
    This is a docstring
    """
    doc = parse(text)
    assert doc.short_description == "This is a docstring"

    text = """
    This is a docstring

    This is a longer description.
    """
    doc = parse(text)
    assert doc.short_description == "This is a docstring"
    assert doc.long_description == "This is a longer description."

    text = """
    Args:
        x: the x coordinate
    Returns:
        None
    """
    doc = parse(text)
    assert doc.meta["Args"][0].arg_name == "x"
    assert doc

# Generated at 2022-06-13 19:48:41.483161
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Docstring, Parameter
    text = """
    Parse the docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation    
    """
    docstring = parse(text)
    assert isinstance(docstring, Docstring)
    assert docstring.summary == "Parse the docstring into its components."
    assert len(docstring.extended_summary) == 0
    assert len(docstring.params) == 2
    assert isinstance(docstring.params[0], Parameter)
    assert docstring.params[0].name == "text"
    assert docstring.params[0].description == "docstring text to parse"
    assert isinstance(docstring.params[1], Parameter)

# Generated at 2022-06-13 19:48:49.644607
# Unit test for function parse
def test_parse():
    text = '''This function parses some text.

:param string text: text to parse
:param bool as_int: parse as integer
:returns: some representation
:rtype: dict
:raises ValueError: if some value is invalid
:raises TypeError: if some type is invalid
'''

    # Ensure we can parse a docstring with the auto style
    ds = parse(text)

    # Ensure that a docstring is parsed correctly
    assert ds.short_description == 'This function parses some text.'
    assert ds.long_description == ''
    assert ds.returns.type_name == 'dict'
    assert ds.returns.description == 'some representation'
    assert len(ds.params) == 2
    assert ds.params[0].arg_name == 'text'
    assert d

# Generated at 2022-06-13 19:49:00.009360
# Unit test for function parse
def test_parse():
    docstring_text = """\
    Function to send an email.

    :param str to: recipient email
    :param str from_: sender email
    """

    docstring = parse(docstring_text, STYLES[Style.google])

    assert docstring.params['to'] == 'recipient email'
    assert docstring.params['from_'] == 'sender email'

    docstring_text = """\
    Function to send an email.

    Parameters
    ----------
    to : str
        recipient email
    from_ : str
        sender email
    """

    docstring = parse(docstring_text, STYLES[Style.numpy])

    assert docstring.params['to'] == 'recipient email'
    assert docstring.params['from_'] == 'sender email'


# Generated at 2022-06-13 19:49:06.128373
# Unit test for function parse
def test_parse():
    assert '''
    test
    ''' == parse(
        '''
    test
    '''
    )

    assert '''
    test
    '''

# Generated at 2022-06-13 19:49:15.160143
# Unit test for function parse
def test_parse():
    text = '''\
"""
This is a test docstring.
    """'''
    parse_any = parse(text, Style.any)
    parse_auto = parse(text)
    assert parse_any.short_description == 'This is a test docstring.'
    assert parse_any.long_description.startswith('    This is a test docstring.')
    assert parse_any.long_description.splitlines()[1] == '    ~~~'
    assert parse_auto.short_description == 'This is a test docstring.'

# Generated at 2022-06-13 19:49:22.938400
# Unit test for function parse

# Generated at 2022-06-13 19:49:32.598486
# Unit test for function parse
def test_parse():
    docstring = '''
    This is a example.

    :param f1: first parameter
    :type f1: int
    :param f2: second parameter
    :return: return value
    :rtype: int
    '''
    assert parse(docstring, style=Style.google) == Docstring(['This is a example.'],
                ['first parameter','second parameter'],['int','int'],['return value','int'])
    assert parse(docstring, style=Style.sphinx) == Docstring(['This is a example.'],
                ['first parameter','second parameter'],['int','int'],['return value','int'])

# Generated at 2022-06-13 19:49:42.658797
# Unit test for function parse
def test_parse():

    from docstring_parser.styles.google import GoogleDocstring
    from docstring_parser.styles.sphinx import SphinxDocstring

# Generated at 2022-06-13 19:49:48.416649
# Unit test for function parse
def test_parse():
    assert parse("Test docstring") == Docstring(short_description="Test docstring",
                                                long_description=None,
                                                style=Style.google, content=[],
                                                meta=[],
                                                examples=[])

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:49:57.706665
# Unit test for function parse

# Generated at 2022-06-13 19:50:07.923916
# Unit test for function parse
def test_parse():
    """Test function parse"""

    docstring = '''\
:param a: first param
:param b: second param
:returns: two params added
'''

    docstring_doc = parse(docstring)
    assert docstring_doc.meta['param'][0] == ('a', 'first param')
    assert docstring_doc.meta['param'][1] == ('b', 'second param')
    assert docstring_doc.meta['returns'] == 'two params added'

    docstring = '''\
:param a: first param
:param b: second param
:returns: two params added
:raises ValueError: if any param is negative
'''

    docstring_doc = parse(docstring)
    assert docstring_doc.meta['param'][0] == ('a', 'first param')

# Generated at 2022-06-13 19:50:15.509014
# Unit test for function parse
def test_parse():
    """Parse the docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """

    assert parse("""
    This is a module docstring.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """) == Docstring(summary='This is a module docstring.',
                      description='',
                      params=[
                          ('text', 'docstring text to parse', ''),
                          ('style', 'docstring style', '')
                      ],
                      returns=('parsed docstring representation', ''))


# Generated at 2022-06-13 19:50:25.280303
# Unit test for function parse
def test_parse():
    text = """
    Keyword arguments:
    arg1 -- This is the first argument.
    arg2 -- This is a second argument.
    """
    ret = parse(text)
    assert len(ret.meta) == 2
    assert ret.meta[0].name == "arg1"
    assert not ret.meta[0].type_name
    assert ret.summary == None
    assert ret.description == None
    assert ret.extended_summary == None
    assert not ret.params
    assert not ret.examples
    assert not ret.yields
    assert not ret.warns
    assert not ret.raises

# Generated at 2022-06-13 19:50:37.250270
# Unit test for function parse
def test_parse():
    parse("""Test docstring.
    :a:      a
    :b:      b
    :c:      c
    :d:      d
    :e:      e
    :f:      f
    :g:      g
    :h:      h
    :i:      i
    :j:      j
    :k:      k
    :l:      l
    :m:      m
    :n:      n
    :o:      o
    :p:      p
    :q:      q
    :r:      r
    :s:      s
    :t:      t
    """)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:50:38.453272
# Unit test for function parse
def test_parse():
	pass

# Generated at 2022-06-13 19:50:48.442360
# Unit test for function parse
def test_parse():
	docstring = """One line summary.
	
	Extended summary.
	
	:param a: Parameter a
	:param b: Parameter b
	:returns: Something
	:raises keyError: raises an exception
	"""
	d = parse(docstring)
	assert d.short_description == "One line summary."
	assert d.long_description == "Extended summary."
	assert d.params == [{"name": "a", "type": None, "desc": "Parameter a"}, {"name": "b", "type": None, "desc": "Parameter b"}]
	assert d.returns == [{"type": None, "desc": "Something"}]
	assert d.rtype == None

# Generated at 2022-06-13 19:50:54.090202
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleDocstring
    goo = GoogleDocstring("""\
blah blah blah

    Args:
      key: the value to store
    """)

    goo.params
    goo.params[0].description
    goo.params[0].name

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 19:51:06.636503
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Docstring, ParseError
    from docstring_parser.styles import STYLES, Style
    text = """This function does something.
\n
    Args:
        param1: The first parameter.
        param2: The second parameter.
    Returns:
        bool: The return value. True for success, False otherwise.
"""
    style = Style.auto
    if style != Style.auto:
        return STYLES[style](text)
    rets = []
    for parse_ in STYLES.values():
        try:
            rets.append(parse_(text))
        except ParseError as e:
            exc = e
    if not rets:
        raise exc
    return sorted(rets, key=lambda d: len(d.meta), reverse=True)[0]
    print

# Generated at 2022-06-13 19:51:11.878969
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    text = '''This is a test for function parse.
        :param text: docstring text to parse
        :param style: docstring style
        '''
    docstring = parse(text)
    #print(docstring)
    assert docstring.full == text

test_parse()

# Generated at 2022-06-13 19:51:14.852607
# Unit test for function parse
def test_parse():
    assert parse('This is a simple paragraph\n') == Docstring(description='This is a simple paragraph\n')
