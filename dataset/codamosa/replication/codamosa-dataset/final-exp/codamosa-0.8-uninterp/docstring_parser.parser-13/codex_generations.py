

# Generated at 2022-06-13 19:41:27.871196
# Unit test for function parse
def test_parse():
	# exemple d'un docstring
	text = """This module is a simple example of docstring."""
	# test de la fonction parse avec la docstring précédente
	assert parse(text, Style.google)

if __name__ == "__main__" :
    test_parse()

# Generated at 2022-06-13 19:41:33.842308
# Unit test for function parse
def test_parse():

    docstring = """
    Some summary.

    :param name: function name
    :param args: function args
    :returns: return value
    """

    doc = parse(docstring)
    assert doc.short_description == "Some summary."
    assert doc.long_description == ""
    assert doc.returns.type_name == "return value"
    assert len(doc.params) == 2
    assert "name" in doc.params
    assert doc.params["name"].type_name == "function name"
    assert "args" in doc.params
    assert doc.params["args"].type_name == "function args"


# Generated at 2022-06-13 19:41:40.934650
# Unit test for function parse
def test_parse():
    test_docstring = """Parameters
----------
img : array, shape (M, N) or (M, N, 3) or (M, N, 4)
    Image to be modified.
alpha : float
    The constant value to use.
Other Parameters
----------------
mode : {'reflect', 'constant', 'edge', 'symmetric', 'wrap'}, optional
    The mode parameter determines how the array borders are handled, where
    cval is the value when mode is equal to 'constant'. Default is 'reflect'
cval : scalar, optional
    Value to fill past edges of input if mode is 'constant'. Default is 0.0
"""
    doc = parse(test_docstring)
    assert doc.sections == ['Parameters', 'Other Parameters']
    assert doc.short_description == None
    assert doc.long_description == None

# Generated at 2022-06-13 19:41:43.044034
# Unit test for function parse

# Generated at 2022-06-13 19:41:52.925694
# Unit test for function parse
def test_parse():
    from docstring_parser import parse
    from .doc_narrative import doc_narrative

    rets = parse(doc_narrative)

    assert(rets.short_desc == "A small function.")
    assert(rets.long_desc == "Wasn't that a nice function?\n\n" +
           "It had a nice docstring which demonstrated that it did nothing at all.\n\n" +
           "It was also nice and big.")
    assert(rets.returns == "RETURN_VALUE\n   None")
    assert(rets.raises == "ARG_ERROR\n   if the arg wasn't valid")
    assert(rets.meta['param1'][0] == 'arg1')
    assert(rets.meta['param1'][1] == 'some argument')

# Generated at 2022-06-13 19:41:59.818871
# Unit test for function parse

# Generated at 2022-06-13 19:42:02.749411
# Unit test for function parse
def test_parse():
    doc = '''
    The main parsing routine.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    '''
    assert parse(doc)

# Generated at 2022-06-13 19:42:06.153258
# Unit test for function parse
def test_parse():
    import pytest

    # raise an exception if the style is not supported
    with pytest.raises(KeyError):
        parse(text="", style="invalid")

    # raise an exception if the docstring cannot be parsed
    with pytest.raises(ParseError):
        parse(text="", style="reStructuredText")


# Generated at 2022-06-13 19:42:13.723815
# Unit test for function parse
def test_parse():
    sample_docstring = """Parse the docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    

# Generated at 2022-06-13 19:42:19.635089
# Unit test for function parse
def test_parse():
    docstring = '''This is a short description.
    This is a long description.
    Attributes:
    attr1 (int): Description of `attr1`
    attr2 (:obj:`str`, optional): Description of `attr2`
    '''
    print(parse(docstring))

test_parse()

# Generated at 2022-06-13 19:42:29.873102
# Unit test for function parse
def test_parse():

    # Testing with a style parameter
    docstring = """
    This is a function.

    :param param1: this is a first parameter
    :param param2: this is a second parameter
    :returns: description of return value
    :raises keyError: raises an exception
    """
    parsed = parse(docstring, style=Style.google)
    assert parsed.summary == "This is a function."
    assert parsed.params['param1'] == "this is a first parameter"
    assert parsed.params['param2'] == "this is a second parameter"
    assert parsed.returns == "description of return value"
    assert parsed.raises['keyError'] == "raises an exception"

    # Testing with auto style by passing only the parameter value
    parsed = parse(docstring)
    assert parsed.summary == "This is a function."

# Generated at 2022-06-13 19:42:38.307929
# Unit test for function parse
def test_parse():
    """Parse docstring."""
    from docstring_parser.common import Docstring
    from docstring_parser.utils import dedent
    text = dedent(
        """
    Short summary.

    Extended description.

    :param int param1: The first parameter.
    :param str param2: The second parameter.
    :returns: Description of return value.
    :rtype: int
    """
    )
    expected = Docstring(
        summary="Short summary.",
        description="Extended description.",
        params={"param1": "The first parameter.", "param2": "The second parameter."},
        returns="Description of return value.",
        rtype="int",
    )
    parsed = parse(text)
    assert parsed == expected

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:42:43.964603
# Unit test for function parse
def test_parse():
    raw_docstring = """This is a short summary.

This is a long description.

Args:
    arg1 (str): Description of `arg1`.
    arg2 (int): Description of `arg2`.

Returns:
    int: Description of return value.
"""
    docstring_obj = parse(raw_docstring)

    assert isinstance(docstring_obj, Docstring)

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:42:45.736718
# Unit test for function parse
def test_parse():
    from .examples.example_1 import __doc__
    d = parse(__doc__)
    assert d.short_description == 'Simple example with types'

# Generated at 2022-06-13 19:42:52.291836
# Unit test for function parse
def test_parse():
    text = """
    Args:
        arg1 (str): The first argument.
        arg2 (int, optional): The second argument. Defaults to 2.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    """

# Generated at 2022-06-13 19:42:58.484597
# Unit test for function parse
def test_parse():
    def func():
        """This is a docstring.

        It can have many paragraphs.

        * With a bullet point list.

        - Or a dash point list.
        """

    doc = parse(func.__doc__)
    assert doc.short_description == "This is a docstring."
    assert doc.long_description == """It can have many paragraphs.

* With a bullet point list.

- Or a dash point list.
"""

# Generated at 2022-06-13 19:43:05.018108
# Unit test for function parse
def test_parse():
    text = '''One line summary.

Longer, multi-line description.

Args:
    arg1 (int): The first argument.
    arg2 (str): The second argument.

Returns:
    bool: The return value. True for success, False otherwise.
'''

    doc = parse(text)
    assert doc.short_description == 'One line summary.'
    assert doc.long_description == 'Longer, multi-line description.'
    assert doc.meta['Args'][0].arg_name == 'arg1'
    assert doc.meta['Args'][0].type_name == 'int'
    assert doc.meta['Args'][0].description == 'The first argument.'
    assert doc.meta['Args'][1].arg_name == 'arg2'
    assert doc.meta['Args'][1].type_

# Generated at 2022-06-13 19:43:15.524504
# Unit test for function parse
def test_parse():

    import pytest

    def test_valid(text, style):
        """Test a piece of valid docstring."""
        docstring = parse(text, style)
        assert docstring.short_description == 'Parses a docsting.'

    def test_no_description(text, style):
        """Test a piece of docstring without a short description."""
        docstring = parse(text, style)
        assert docstring.short_description == ''

    def test_valid_multiline(text, style):
        """Test a piece of valid docstring."""
        docstring = parse(text, style)
        assert docstring.short_description == 'Parses a docsting.'
        assert docstring.long_description == '\nCarry out some other\n' \
            'processing here.\n'


# Generated at 2022-06-13 19:43:26.724412
# Unit test for function parse
def test_parse():
    import os.path
    import glob
    os.chdir(os.path.join(os.path.dirname(__file__), 'fixtures'))
    for path in sorted(glob.glob('*.doctest')):
        print('#' * len(path))
        print(path)
        print('#' * len(path))
        with open(path) as fp:
            text = fp.read()
        print(text[:79])
        try:
            parsed = parse(text)
        except ParseError as exc:
            print(exc)
            print()
            continue
        else:
            print()
        print('Short description:')
        print(parsed.short_description)
        print()
        print('Long description:')

# Generated at 2022-06-13 19:43:39.904854
# Unit test for function parse
def test_parse():
    text = \
"""This is the summary.

This is the description.

:param a: description for a
:type a: int
:param b: description for b
:type b: str
:returns: description for return value
:rtype: list
"""
    docstring = parse(text)
    assert docstring.short_description == "This is the summary."
    assert docstring.long_description == "This is the description."
    assert docstring.returns.description == "description for return value"
    assert docstring.returns.type_annotation == "list"
    assert docstring.params["a"].description == "description for a"
    assert docstring.params["a"].type_annotation == "int"
    assert docstring.params["b"].description == "description for b"
    assert docstring

# Generated at 2022-06-13 19:43:55.353696
# Unit test for function parse
def test_parse():
    assert parse(
        """
args:
    port: port number
    host: host name
""")

    assert parse(
        """
Multi-line parameters are allowed.

Parameters:
    param1:
        first parameter
    param2:
        second parameter
""")

    assert parse(
"""
:param int port: port number
:param str host: host name
""")

    assert parse(
"""
:param int port: port number
:param str host: host name
""")

    assert parse(
"""
:param int port: port number
:param str host: host name
""")

    assert parse(
"""
:param int port: port number
:param str host: host name
""")

    assert parse(
"""
:param int port: port number
:param str host: host name
""")


# Generated at 2022-06-13 19:44:03.127088
# Unit test for function parse
def test_parse():
    doc_string = '''This function is used to test the function parse of docstring_parser.
    :params key: a key word
    :returns: Nothing'''
    ans = parse(doc_string)
    assert ans.short_description == 'This function is used to test the function parse of docstring_parser.'
    assert len(ans.params) == 1
    assert ans.params['key'].description == 'a key word'
    assert ans.returns.description == 'Nothing'
    assert ans.new_line_counts == 1

# print(parse('''This function is used to test the function parse of docstring_parser.
#     :params key: a key word
#     :returns: Nothing''').params['key'])
# print(parse('''This function is used to test the function parse of docstring_

# Generated at 2022-06-13 19:44:11.727733
# Unit test for function parse

# Generated at 2022-06-13 19:44:15.645448
# Unit test for function parse
def test_parse():
    text = '''
    Args:
        arg1: Arg1 description
        arg2: Arg2 description
    '''
    doc = parse(text)
    assert isinstance(doc, Docstring)
    assert len(doc.args) == 2

test_parse()

# Generated at 2022-06-13 19:44:29.160854
# Unit test for function parse
def test_parse():
    from docstring_parser.common import ReturnItem
    from docstring_parser.styles import Amazon
    ret = parse('', Amazon)
    assert ret.summary == ''
    assert ret.description == ''
    assert ret.returns == []
    assert ret.raises == []
    assert ret.meta == {}
    ret = parse('summary.')
    assert ret.summary == 'summary.'
    assert ret.description == ''
    assert ret.returns == []
    assert ret.raises == []
    assert ret.meta == {}
    ret = parse('summary.\ndescription.')
    assert ret.summary == 'summary.'
    assert ret.description == 'description.'
    assert ret.returns == []
    assert ret.raises == []
    assert ret.meta == {}

# Generated at 2022-06-13 19:44:33.392064
# Unit test for function parse
def test_parse():

    def docstring():
        '''
        Short summary.

        Extended description.
        '''

    ds = docstring.__doc__

    def test_with_style(style):
        parsed = parse(ds, style)

        assert parsed.summary == 'Short summary.'
        assert parsed.description == 'Extended description.'
        assert parsed.meta is None

    for style in STYLES:
        test_with_style(style)

# Generated at 2022-06-13 19:44:36.223209
# Unit test for function parse
def test_parse():
    assert parse(__doc__, Style.google)
    assert parse(__doc__, Style.numpy)
    assert parse(__doc__, Style.sphinx)

# Generated at 2022-06-13 19:44:46.068715
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Parameter, ReturnValue
    from docstring_parser.parse import parse
    text = '''
    This is the description.

    :param foo: this is the description of foo
    :type foo: str
    :param bar: this is the description of bar
    :returns: this is the description of the return value
    :rtype: bool
    '''
    docstring = parse(text)
    assert docstring.short_description == 'This is the description.'
    assert docstring.long_description == ''
    assert docstring.meta['foo'] == Parameter('this is the description of foo', 'str')
    assert docstring.meta['bar'] == Parameter('this is the description of bar')
    assert docstring.returns == ReturnValue('this is the description of the return value', 'bool')

# Generated at 2022-06-13 19:44:53.077956
# Unit test for function parse
def test_parse():
    from docstring_parser.styles.google import GoogleStyle
    text = '''\
    :param name: The name of the child.
    :type name: str
    :param age: The age of the child.
    :type age: int
    :returns: None
    :rtype: None
    '''
    parsed = parse(text)
    assert isinstance(parsed, Docstring)
    assert parsed.short_description == ""
    assert parsed.long_description == ""
    assert len(parsed.params) == 2 
    assert parsed.params[0].arg_name == "name"
    assert parsed.params[0].arg_type == "str"
    assert parsed.params[0].description == "The name of the child."
    assert len(parsed.returns) == 1
    assert parsed

# Generated at 2022-06-13 19:45:02.272271
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import Google
    out = parse(Google.doc, style=Style.google)
    assert out.summary == 'Dummy docstring for testing purpose.\n'

# Generated at 2022-06-13 19:45:10.926159
# Unit test for function parse

# Generated at 2022-06-13 19:45:18.862228
# Unit test for function parse
def test_parse():
    text = '''\
    Purpose
    -------
    This is the purpose.

    Returns
    -------
    x: int
        The x value.

    Notes
    -----
    This is a note.'''
    assert parse(text).returns
    text = '''\
    Returns
    -------
    x: int
        The x value.

    Notes
    -----
    This is a note.'''
    assert parse(text).returns
    text = '''\
    Parameters
    ----------
    x: int
        The x value.

    y: real
        The y value.

    Returns
    -------
    x or y: whatever
        The x or y value.

    Notes
    -----
    This is a note.'''
    assert parse(text).returns

# Generated at 2022-06-13 19:45:25.630347
# Unit test for function parse
def test_parse():
    text = '''
        Example function with types documented in the docstring.

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
    '''
    docstring = parse(text)
    return docstring.params[0]['type'].dumps() == 'int'

if __name__ == "__main__":
    print(test_parse())

# Generated at 2022-06-13 19:45:32.213018
# Unit test for function parse
def test_parse():
    text = '''
        some text
        :param param1: the first parameter
        :param param2: the second parameter
        :returns: description of return value
    '''
    docstring = parse(text)
    assert docstring.short_description == 'Some text'
    assert docstring.meta['param1'].description == 'the first parameter'
    assert docstring.meta['param2'].description == 'the second parameter'
    assert docstring.returns.description == 'description of return value'
    assert docstring.long_description == ''


# Generated at 2022-06-13 19:45:38.102958
# Unit test for function parse
def test_parse():
    """Test file"""
    from docstring_parser.styles import NumpyStyle
    doc = parse("""A small test file.""")
    assert(doc.short_description == "A small test file.")
    doc = parse("""A small test.

and more text
    """, style=Style.auto)
    assert(doc.short_description == "A small test.")
    assert(doc.long_description == "\nand more text")
    doc = parse("""A small test """, style=Style.auto)
    assert(doc.short_description == "A small test ")
    try:
        doc = parse("""A small test """, style=Style.auto)
        assert(False)
    except ParseError:
        assert(True)

# Generated at 2022-06-13 19:45:44.110349
# Unit test for function parse
def test_parse():
    text = '''Removes the specified key and its value.

:param key: The key to be deleted.
:type key: string
:param bool force: Optional flag to force deletion.
:raises: KeyNotFoundError
'''

    ret = parse(text)
    print(ret)
    print(ret.short_description)
    print(ret.long_description)
    print(ret.meta)


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:45:46.211692
# Unit test for function parse
def test_parse():
	string = 'This parses a docstring.'
	assert parse(string) == Docstring(description = 'This parses a docstring.', lineno = 1)

# Generated at 2022-06-13 19:45:53.440244
# Unit test for function parse
def test_parse():
    style = Style.numpy
    text = '''This function finds the sum of all numbers in a list.
             :returns: sum of numbers
             :rtype: int
             :raises NotANumber: if any of the items cannot be added
             '''
    docstring = parse(text, style)
    assert docstring.returns.description == 'sum of numbers'
    assert docstring.returns.type == 'int'
    assert docstring.raises[0].type == 'NotANumber'
    assert docstring.raises[0].description == 'if any of the items cannot be added'
    assert docstring.short_description == 'This function finds the sum of all numbers in a list.'
    assert docstring.long_description == ''


# Generated at 2022-06-13 19:45:54.046392
# Unit test for function parse
def test_parse():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 19:46:05.229409
# Unit test for function parse
def test_parse():
    text = """
    @param: description: This is a description.
    @return: description: This is a description
    @returns: description: This is a description
    @meta: description: This is a description
    @keyword: description: This is a description
    @parameter: description: This is a description
    """


# Generated at 2022-06-13 19:46:18.130408
# Unit test for function parse
def test_parse():
    text = '''\
    The quick brown fox jumps over the lazy dog.
    :param fox: has any foxes
    :param dog: has any dogs
    
    :raises ValueError: if fox <= 0
    '''
    docstring = parse(text)
    assert docstring.short_description == 'The quick brown fox jumps over the lazy dog.'
    assert docstring.long_description == ''
    assert docstring.tags == [('param', 'fox', 'has any foxes'), ('param', 'dog', 'has any dogs')]
    assert docstring.meta == {}
    assert docstring.examples == []
    assert docstring.raises == [('ValueError', 'if fox <= 0')]
    assert docstring.see_also == []
    assert docstring.warns == []

# Generated at 2022-06-13 19:46:29.265855
# Unit test for function parse

# Generated at 2022-06-13 19:46:38.844482
# Unit test for function parse
def test_parse():
    test_docstring = """
    This is a test of the function.

    Args
        arg1 (int): the first argument
        arg2 (str): the second argument
    Returns:
        str: the return value
    """
    assert parse(test_docstring) == parse(test_docstring, style=Style.numpy)
    assert parse(test_docstring) == parse(test_docstring, style=Style.google)

    # Fails on a Google style
    test_docstring = """
    This is a test of the function.

    Args:
        arg1 (int): the first argument
        arg2 (str): the second argument
    Returns:
        str: the return value
    """
    assert parse(test_docstring, style=Style.numpy) != parse(test_docstring)
    assert parse

# Generated at 2022-06-13 19:46:41.445338
# Unit test for function parse
def test_parse():
    text = '''
            Test docstring.
            '''
    docstring = parse(text)
    assert docstring.short_description == "Test docstring."

# Generated at 2022-06-13 19:46:55.408579
# Unit test for function parse
def test_parse():
    text = """
        One line summary.
        
        Extended description.
        
        Args:
            param1 (int): The first parameter.
            param2 (str): The second parameter.
            
        Return:
            bool: The return value. True for success, False otherwise.
            
        Raises:
            KeyError: The key is not in the cache 
            ValueError: The value is invalid
            TypeError: Raises an exception.
        
        """

    docstring = parse(text)
    assert docstring.short_description == "One line summary."
    assert docstring.long_description == "Extended description."
    assert len(docstring.params) == 2
    assert len(docstring.returns) == 1
    assert len(docstring.raises) == 3

# Generated at 2022-06-13 19:47:03.321086
# Unit test for function parse
def test_parse():
    text = '''
    This is a test docstring for parse.

    foo
    bar
    '''
    title = 'This is a test docstring for parse.'
    summary = 'This is a test docstring for parse.'
    text = '''
    This is a test docstring for parse.

    foo
    bar
    '''
    d = parse(text)
    assert d.title == title, 'title should be "{}" but is "{}"'.format(title, d.title)
    assert d.summary == summary, 'summary should be "{}" but is "{}"'.format(summary, d.summary)
    assert d.text == text, 'text should be "{}" but is "{}"'.format(text, d.text)

# Generated at 2022-06-13 19:47:07.998435
# Unit test for function parse
def test_parse():
    text = """description
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation"""
    print(parse(text))



# Generated at 2022-06-13 19:47:10.787966
# Unit test for function parse
def test_parse():
    assert bool(parse("""Hello!""")) == True

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:47:15.829016
# Unit test for function parse
def test_parse():
    # As the docstring of the function parse is empty, we only test the style of the docstring
    style = Style.auto
    docstring = """ As the docstring of the function parse is empty, we only test the style of the docstring
    """
    assert parse(docstring, style) == docstring

# Generated at 2022-06-13 19:47:23.040464
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleDocstring
    from docstring_parser.lexers import GoogleStyleLexer
    from docstring_parser.parsers import GoogleStyleParser
    text = '''\
    This function does something.

    :param a: The function's first parameter.
    :param b: The function's second parameter.
    :returns: Description of the return value.
    :raises keyError: The function raises an exception.\
    '''
    with GoogleDocstring(text) as d:
        print('PARSE FROM STRING')
        print(d)
        print()


# Generated at 2022-06-13 19:47:29.630690
# Unit test for function parse
def test_parse():
    parse("this is a classifier", Style.google)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:47:37.887483
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleStyleDocstring, NumpyStyleDocstring
    from docstring_parser.styles import GoogleStyleSectionParser
    from docstring_parser.styles import NumpyStyleSectionParser

    class DummyGoogleStyleSectionParser(GoogleStyleSectionParser):
        def _parse_description(self):
            self.description = 'description is here'
        def _parse_args(self):
            self.params['arg1'] = 'arg1 description'
        def _parse_returns(self):
            self.returns = 'returns description'

    class DummyNumpyStyleSectionParser(NumpyStyleSectionParser):
        def _parse_first_section(self):
            self.short_description = 'short description'

# Generated at 2022-06-13 19:47:46.801424
# Unit test for function parse
def test_parse():
    assert repr(parse(r'''
        This function add 2 numbers.
        
        Args:
            x (int): first number
            y (int): second number
        
        Returns:
            sum of x and y
        ''')) == repr(Docstring(summary='This function add 2 numbers.', description='',
                        params=[{'name': 'x', 'type': 'int', 'description': 'first number'},
                                {'name': 'y', 'type': 'int', 'description': 'second number'}],
                        returns={'type': '', 'description': 'sum of x and y'},
                        raises=[],
                        meta={}))

test_parse()

# Generated at 2022-06-13 19:47:58.071582
# Unit test for function parse
def test_parse():
    assert len(parse(
        '\n'
        'A line.\n'
        '\n'
        ':param args:   a list of arguments\n'
        ':type args:    list\n'
        ':returns:      the sum of squares\n'
        ':rtype:        int\n'
    ).meta) == 4
    assert len(parse(
        ':param foo: a foo\n'
        ':param bar: a bar\n'
        '\n'
        'A line.\n'
    ).meta) == 2
    assert not parse(':param foo: a foo\n').meta
    assert not parse(':param foo: a foo').meta
    with pytest.raises(ParseError):
        assert not parse(':\n').meta

# Generated at 2022-06-13 19:48:05.780257
# Unit test for function parse
def test_parse():
    actual = parse("""\
        A *markdown* paragraph
        with *two* lines.

        Returns:
            str: a return value
        """, Style.google)
    assert actual.short_description == 'A *markdown* paragraph with *two* lines.'
    assert actual.long_description == ''
    assert actual.returns == [dict(type_name='str', description='a return value')]
    # TODO: the rest

# Generated at 2022-06-13 19:48:16.692746
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Meta, Section
    from docstring_parser.styles import DefaultStyle

    docstring = parse(DefaultStyle.__doc__)
    assert docstring.summary == "Abstract docstring style.\n"
    assert docstring.extended_summary == "All derived classes **must** implement this class.\n\n"
    assert docstring.sections == [
        Section(
            heading="Args",
            content=Meta([
                ("text", "docstring text to parse"),
                ("style", "docstring style")
            ]),
            style=DefaultStyle
        ),
        Section(
            heading="Returns",
            content=Meta([
                ("parsed_docstring", "parsed docstring representation")
            ]),
            style=DefaultStyle
        )
    ]

# Generated at 2022-06-13 19:48:26.004802
# Unit test for function parse
def test_parse():
    text = """\
This is a test docstring.

:param x: int
:param y: (int) The number of y's
    """
    result = parse(text)

    assert result.short_description == "This is a test docstring."
    assert result.long_description is None
    assert result.meta == {
        "x": "int",
        "y": "(int) The number of y's"
    }

# Generated at 2022-06-13 19:48:37.233842
# Unit test for function parse
def test_parse():
    assert parse("This is a test docstring") == Docstring(
        content = "This is a test docstring",
        summary = "This is a test docstring",
        full = "This is a test docstring",
        style = Style.numpy,
        meta = {},
        opts = {},
        pos = [],
        raw = "This is a test docstring",
        before = "",
        after = "",
    )

# Generated at 2022-06-13 19:48:46.666163
# Unit test for function parse
def test_parse():
    text = '''
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    '''
    result = parse(text, Style.pep287)
    correct = Docstring(meta = {'param': [{'text': 'text'}, {'style': 'style'}], 'returns': [{'parsed docstring representation': ' '}]})
    assert result.meta == correct.meta
    assert result.description == correct.description
    assert result.extended_summary == correct.extended_summary
    assert result.tags == correct.tags
    assert result.examples == correct.examples


if __name__ == '__main__':
    import pytest
    pytest.main()

# Generated at 2022-06-13 19:48:56.398941
# Unit test for function parse
def test_parse():
    doc = """
    The summary line for a function docstring should always be a short,
    one-line summary of the object's purpose.

    If there is more to say, follow the summary with a new line and a
    blank line.

    Multiple paragraphs are supported.

    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.

    Returns:
        bool: The return value. True for success, False otherwise.

    """

#     result = parse(doc, Style.google)
#     print(result)
    result = parse(doc, Style.numpy)
    print(result)
    result = parse(doc, Style.auto)
    print(result)


# Generated at 2022-06-13 19:49:02.585090
# Unit test for function parse
def test_parse():
    assert len(parse("")) == 1
    assert len(parse("")) == 2
    assert len(parse("")) == 3
    assert len(parse("")) == 4

# Generated at 2022-06-13 19:49:06.568297
# Unit test for function parse
def test_parse():
    # Writing a simple test, I will later write a detailed test
    text="""
    This is a docstring
    """
    assert(isinstance(parse(text, style=Style.numpy), Docstring))

if __name__ == '__main__':
    print(parse.__doc__)
    test_parse()

# Generated at 2022-06-13 19:49:18.625552
# Unit test for function parse
def test_parse():
    docstring = '''One line summary.
    Extended description.

    Args:
      arg1 (int): Description of arg1
      arg2 (str): Description of arg2

    Returns:
      bool: Description of return value

    '''
    res = parse(docstring)
    assert res.short_description == 'One line summary.'
    assert res.long_description == 'Extended description.'
    assert res.returns.type_name == 'bool'
    assert res.returns.description == 'Description of return value'
    assert res.parameters[0].type_name == 'int'
    assert res.parameters[0].name == 'arg1'
    assert res.parameters[0].description == 'Description of arg1'
    assert res.parameters[1].type_name == 'str'

# Generated at 2022-06-13 19:49:29.542106
# Unit test for function parse
def test_parse():
    """Test parse function with various docstring styles."""
    docstring_string = """
    Function to sum two numbers.

    Args:
        arg1(int): first arg
        arg2(int): second arg

    Returns:
        int: addition result
    """
    docstring_two_line = """Function to sum two numbers.
    Args:
        arg1(int): first arg
        arg2(int): second arg
    Returns:
        int: addition result
    """
    docstring_google = """Function to sum two numbers.

    Args:
        arg1 (int): first arg
        arg2 (int): second arg

    Returns:
        int: addition result
    """

# Generated at 2022-06-13 19:49:39.729616
# Unit test for function parse
def test_parse():
    text = '''Given a matrix A, return the transpose of A.

    The transpose of a matrix is the matrix flipped over it's main diagonal, 
    switching the row and column indices of the matrix.

    Example 1:
        Input: [[1,2,3],[4,5,6],[7,8,9]]
        Output: [[1,4,7],[2,5,8],[3,6,9]]

    Example 2:
        Input: [[1,2,3],[4,5,6]]
        Output: [[1,4],[2,5],[3,6]]

    Note:
        1 <= A.length <= 1000
        1 <= A[0].length <= 1000
    '''
    parse(text)

# Generated at 2022-06-13 19:49:52.786875
# Unit test for function parse
def test_parse():
    # Negative test cases (exceptions)
    text = """Line1
Line2
Line3"""
    try:
        parse(text)
        raise Exception("Expected an exception")
    except ParseError as e:
        assert "No docstring styles" in str(e)

    text = """One-line docstring."""
    try:
        parse(text)
        raise Exception("Expected an exception")
    except ParseError as e:
        assert "No docstring styles" in str(e)

    # Positive test cases (valid docstrings)
    text = """One-line docstring."""
    assert parse(text, Style.google).short_description == text

    text = """One-line docstring.

    Description below."""
    assert parse(text, Style.google).short_description == "One-line docstring."

# Generated at 2022-06-13 19:50:01.694032
# Unit test for function parse
def test_parse():
    assert parse("")==Docstring(short_description='',long_description='',content_type='text/x-rst',meta={},tags=[])
    docstring=parse("This is docstring of function")
    assert docstring.short_description=="This is docstring of function"
    assert docstring.long_description==''
    assert docstring.content_type=='text/x-rst'
    assert docstring.meta=={}
    assert docstring.tags==[]

    docstring=parse("This is docstring of function\n with new line\n")
    assert docstring.short_description=="This is docstring of function\n with new line"
    assert docstring.long_description==''
    assert docstring.content_type=='text/x-rst'
    assert docstring.meta=={}

# Generated at 2022-06-13 19:50:10.691314
# Unit test for function parse
def test_parse():
    text = \
    """Finds the most similar documents to a query by calculating the cosine similarity between query and documents in the corpus.

    :param query: Query text
    :param corpus: List of document texts
    :return: List of (document, similarity score) tuples

    >>> find_similar("I want to eat", ["I want to drink", "I want to sleep"])
    [("I want to drink", 1.0), ("I want to sleep", 1.0)]
    """
    docstring = parse(text)
    assert docstring.summary == 'Finds the most similar documents to a query by calculating the cosine similarity between query and documents in the corpus.'

# Generated at 2022-06-13 19:50:18.610761
# Unit test for function parse
def test_parse():
    import os
    import docstring_parser

    doc_dir = os.path.dirname(os.path.abspath(docstring_parser.__file__))
    test_dir = os.path.join(doc_dir,'..','testdata')
    fname = os.path.join(test_dir,'test_parse.py')
    with open(fname,'r') as fp:
        text = fp.read()

    docstr = parse(text)

    assert docstr.summary == 'This is a one line summary.'
    assert docstr.body == 'This is the body.\n'
    assert docstr.meta['Args'] == '*args\n    description'
    #assert docstr.meta['random_key'] == 'random_value'

# Generated at 2022-06-13 19:50:28.501876
# Unit test for function parse
def test_parse():
    text = """\
    Parse the docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    parsed_text = parse(text)
    assert parsed_text.short_description == "Parse the docstring into its components."
    assert parsed_text.long_description == None
    assert parsed_text.returns == "parsed docstring representation"
    assert parsed_text.meta == [{'name': "text" , 'type': None, 'description': "docstring text to parse"}, {'name': "style", 'type': None, "description": "docstring style"}]

# Generated at 2022-06-13 19:50:33.830107
# Unit test for function parse
def test_parse():    
    text = '''
    This is a test
    '''
    assert isinstance(parse(text), Docstring)


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:50:39.672691
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import PEP257
    text = '''
    This is a sample docstring.

    Args:
        arg1 (str): description
        arg2 (str): description
    '''
    assert parse(text).meta['Args'] == PEP257().parse(text).meta['Args']

# Generated at 2022-06-13 19:50:41.242464
# Unit test for function parse
def test_parse():
    return None


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:50:48.355421
# Unit test for function parse
def test_parse():
    text = '''Bla bla bla
    :param arg1: my arg1
    :param arg2: my arg2, second line
        third line, and fourth
    :returns: something
    '''
    assert parse(text)
    text = '''Bla bla bla
    :param arg1: my arg1
    :param arg2: my arg2, second line
        third line, and fourth
    :returns: something
    :param arg3:
    '''
    assert parse(text)

# Generated at 2022-06-13 19:50:57.099383
# Unit test for function parse
def test_parse():
    text = '''Parse the docstring into its components.
    
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    '''
    style = Style.sphinx
    res = parse(text, style)
    print(res.args)
    print(res.retval)
    print(res.meta)
    print(res.content)
    assert res.args == ['text: docstring text to parse', 'style: docstring style']
    assert res.retval == 'parsed docstring representation'
    assert res.meta == {'param': ['text: docstring text to parse', 'style: docstring style'], 'returns': ['parsed docstring representation']}


# Generated at 2022-06-13 19:51:02.902628
# Unit test for function parse
def test_parse():
    print(parse.__doc__)

# test_parse()


# Generated at 2022-06-13 19:51:11.684791
# Unit test for function parse
def test_parse():

    style = parse("""Summary line.

This is a multiline description.  You should use in the interpreter a
triple-quoted string such as this to define multiline docstrings.

See https://www.python.org/dev/peps/pep-0257/

:param str arg1: The first argument.
:param int arg2: The second argument.
:returns: Description of return value.
:raises: AttributeError, KeyError
""")
    print(style)


test_parse()

# Generated at 2022-06-13 19:51:26.128755
# Unit test for function parse
def test_parse():
	"""
	Testing function parse.
	"""
	from docstring_parser import parse

	# numpydoc style
	docstring = """	
	One line summary.

	Extended description.

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
	parsed_docstring = parse(docstring)
	assert parsed_docstring.short_description == "One line summary."
	assert parsed_docstring.long_description == "Extended description."
	assert len(parsed_docstring.params) == 2
	assert len(parsed_docstring.returns) == 1