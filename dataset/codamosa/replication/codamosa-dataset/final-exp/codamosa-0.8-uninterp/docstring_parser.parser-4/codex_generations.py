

# Generated at 2022-06-13 19:41:37.539679
# Unit test for function parse
def test_parse():
    # text = '....'
    # style = Style.auto
    # parse(text, style)

    text = '''
            Unit test for function parse

            Parameters:
                text: first parameter
                style: second parameter

            Returns:
                the parsed string here
            '''

    try:
        docstring = parse(text)
        assert docstring.params == {'text': 'first parameter', 'style': 'second parameter'}
        assert docstring.returns == 'the parsed string here'
    except Exception as e:
        raise e
    else:
        print("Unit test for function parse in `parse.py` passed")

# Unit test
if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:41:48.142320
# Unit test for function parse
def test_parse():
    docstring = parse(test_docstring)
    assert docstring.content == 'test line one\ntest line two'
    assert docstring.short_description == 'test line one'
    assert docstring.long_description == [
        'test line one',
        'test line two'
    ]
    assert docstring.meta == {
        'name': 'test_name',
        'type': 'object',
        'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}],
        'return': {'type': 'int'},
        'raises': [{'type': 'ValueError'}]
    }



# Generated at 2022-06-13 19:41:54.490446
# Unit test for function parse
def test_parse():
  
  class abc:
    """
      A class doc
    """
    @classmethod
    def func_test(cls, a, b):
      """
          A Function doc

          :param a: First parameter
          :type a: int
          :param b: Second parameter
          :type b: str
          :return: int
      """
      print(a)
      print(b)
      return a

  print(parse(abc.func_test.__doc__))

  print(abc.func_test.__doc__)


if __name__=="__main__":
  test_parse()

# Generated at 2022-06-13 19:42:00.780435
# Unit test for function parse
def test_parse():
    text = '''\
This function does something.

Args:
    arg1(int): the first argument
Returns:
    bool: True if successful
'''
    docstring = parse(text)
    assert docstring.short_description == 'This function does something.'

    assert len(docstring.long_description) == 0

    assert len(docstring.params) == 1
    assert 'arg1' in docstring.params
    assert docstring.params['arg1'].arg_type == 'int'
    assert docstring.params['arg1'].description == 'the first argument'
    assert docstring.params['arg1'].default is None

    assert len(docstring.returns) == 1
    assert docstring.returns['return'].description == 'True if successful'

# Generated at 2022-06-13 19:42:06.118121
# Unit test for function parse
def test_parse():
    test_docstring = '''
    Some text to test.

    :param value: some value
    '''

    assert(parse(test_docstring).short_description == 'Some text to test.')
    assert(parse(test_docstring).long_description == '')
    assert(parse(test_docstring).meta == [{'type':'param', 'name':'value', 'values':'some value'}])


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:42:13.704539
# Unit test for function parse
def test_parse():
    from docstring_parser import parse

    docstring = \
        """Single line summary.

Multiple lines of description.

Args:
    param1: The first parameter.
    param2: The second parameter.
Returns:
        bool: The return value. True for success, False otherwise.
Raises:
    AttributeError, KeyError
"""
    result = parse(docstring)
    assert result.short_description == 'Single line summary.'
    assert result.long_description == 'Multiple lines of description.'
    assert len(result.params) == 2
    assert result.params[0]['name'] == 'param1'
    assert result.params[0]['description'] == 'The first parameter.'
    assert result.params[1]['name'] == 'param2'

# Generated at 2022-06-13 19:42:25.925117
# Unit test for function parse

# Generated at 2022-06-13 19:42:35.413330
# Unit test for function parse
def test_parse():
    text = '''\
    Return the function's docstring as a string.

    An empty string is returned if the docstring is undefined and
    the `legacy` argument is false.

    The docstring is parsed into its constituent parts using the
    :func:`~.parse` function and returned as a parsed docstring object.

    :param legacy: If true, return the built-in ``__doc__`` attribute if it
        is defined (and falls back to an empty string for undefined
        docstrings).
    :return: string or parsed docstring'''
    print(parse(text))
    # Docstring(description='\n    Return the function\'s docstring as a string.\n\n    ... constituent parts using the\n    :func:`~.parse` function and returned as a parsed docstring object.\n',
    # body='\

# Generated at 2022-06-13 19:42:44.901933
# Unit test for function parse
def test_parse():
    class_doc_string = '''
    This is a class docstring.

    It can contain multiple paragraphs.

    Attributes:
        attr1 (str): Description of `attr1`
        attr2 (str): Description of `attr2`
        attr3 (str): Description of `attr3`

    Methods:
        get_attr1(self)
            Returns the value for `attr1`
        set_attr1(self, value)
            Sets the value for `attr1`
    '''


# Generated at 2022-06-13 19:42:54.253056
# Unit test for function parse

# Generated at 2022-06-13 19:42:59.089887
# Unit test for function parse
def test_parse(): 
    pass

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:43:08.570495
# Unit test for function parse
def test_parse():
    """Test the main parsing function"""
    text = """
    A very short function.

    :param a: a parameter
    :type a: int
    :returns: a return value
    :rtype: int
    """
    parsed = parse(text)
    assert len(parsed.description) == 2
    assert parsed.params == {'a': 'a parameter'}
    assert parsed.returnd == {'returns': 'a return value'}
    assert parsed.return_type == 'int'
    assert parsed.params_type == {'a': 'int'}

# Generated at 2022-06-13 19:43:12.975472
# Unit test for function parse
def test_parse():
    text = '''\
    The ``example`` module.

    :param arg1: The first argument.
    :type arg1: int, float, str or list

    :raises ValueError: If `arg2` is equal to `arg1`.
    '''
    print(parse(text))

# Generated at 2022-06-13 19:43:24.141616
# Unit test for function parse
def test_parse():
    docstring = """
    This function does something interesting.
    This is a longer description, which spans multiple lines.
    There is no blank line in between.

    This is a short description
    and this line is not indented.
    """
    doc = parse(docstring)
    assert type(doc) == Docstring, "Parse docstring error"
    assert doc.short_description == "This function does something interesting.", "Parse docstring error"
    assert doc.long_description == "This is a longer description, which spans multiple lines.\nThere is no blank line in between.", "Parse docstring error"
    assert doc.long_description == "This is a longer description, which spans multiple lines.\nThere is no blank line in between.", "Parse docstring error"
    assert "line is not indented" in doc.extended_summary

# Generated at 2022-06-13 19:43:32.791951
# Unit test for function parse
def test_parse():
    docstring = '''
    Parses the docstring into its components.
    
    Parameters
    ----------
    text : str
        docstring text to parse
    style : :class:`Style`, optional
        docstring style
    
    Returns
    -------
    parsed : :class:`Docstring`
        parsed docstring representation
    '''
    parsed=parse(docstring)
    #print(parsed.summary)
    #print(parsed.description)
    print(parsed.params)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:43:34.052741
# Unit test for function parse
def test_parse():
    import doctest
    doctest.testmod()

# test_parse()

# Generated at 2022-06-13 19:43:39.464928
# Unit test for function parse
def test_parse():
    print(parse(
        """
        Returns a basic docstring.

        :param name: A name
        :type name: str
        :returns: A docstring
        :rtype: docstring_parser.Docstring
        """))

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:43:45.715337
# Unit test for function parse
def test_parse():
    expect = Docstring(
    'This is a summary.\n\n    This is a body.',
    'This is a summary.',
    [],
    'This is a body.',
    type='numpydoc',
    metadata={'Signature': '(foo, bar=None)', 'Summary': 'This is a summary.',
     'Extended Summary': 'This is a summary.\n\nThis is a body.', 'Returns': '', 'Docstring Body': 'This is a body.'}
)
    assert parse(
        """
        This is a summary.

            This is a body.
        """
    ) == expect

# Generated at 2022-06-13 19:43:53.551398
# Unit test for function parse
def test_parse():
    text = '''
    :param int x:
      x
    :param int y:

      y
    '''
    result = parse(text)
    assert result.meta == [
        {
            'name': 'x',
            'type': 'int',
            'desc': 'x'
        },
        {
            'name': 'y',
            'type': 'int',
            'desc': 'y'
        }
    ]
    assert result.doc == ""
    assert result.short_desc == ""
    assert result.long_desc == ""

# Generated at 2022-06-13 19:43:57.156570
# Unit test for function parse
def test_parse():
    assert parse.__doc__ == "Parse the docstring into its components.\n\n    :param text: docstring text to parse\n    :param style: docstring style\n    :returns: parsed docstring representation\n    "

# Generated at 2022-06-13 19:44:04.819863
# Unit test for function parse
def test_parse():
    parse_string = """
    Function to calculate the addition of two numbers.

    Parameters
    ----------
    a : int
        First number
    b : int
        Second number
    c : int, optional
        Third number

    Returns
    -------
    addition : int
        Sum of all three numbers

    """
    print(parse(parse_string,style=Style.numpy))

# Generated at 2022-06-13 19:44:11.876314
# Unit test for function parse
def test_parse():
    text = '''   :param a: a test param
        :param b: test param two
        :param c: test param three
        :returns: Returns sum of two params

        :raises ValueError: Raises an error if either parameters
            are negative.
        
        Hello World

        .. math::

           \\Gamma(x) = \\int_0^\\infty t^{x-1}e^{-t}dt\\,.

        \\alpha \\beta \\gamma 

        :raises ValueError: Raises an error if either parameters
            are negative.'''

    print(parse(text))

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:44:16.767018
# Unit test for function parse
def test_parse():
    str = """
    Args:
        a: bar
        b: foo
    Raises:
        IndexError: something
        ValueError: something else
        TypeError: something really odd
    Returns:
        return value
    """
    docstrings = parse(str)
    print(docstrings)
    # TODO: Add proper unit test

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:44:29.228437
# Unit test for function parse
def test_parse():
    
    # test with auto style
    try:
        docstring = """
        A simple test function.
        Some more text.
        """
        parse(docstring)
        assert True
    except:
        assert False

    # test with numpy style
    try:
        docstring = """
        A simple test function.

        Parameters
        ----------
        param1 : int
            The first parameter.
        param2 : str
            The second parameter.

        Returns
        -------
        str
            The return value.
        """
        parse(docstring, style=Style.numpy)
        assert True
    except:
        assert False

# Generated at 2022-06-13 19:44:35.839543
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import google
    from docstring_parser.styles import numpy
    from docstring_parser.common import Docstring

    def test_parse_func(input_text, style, name = None, summary = None,
                        parameters = None, raises = None, returns = None,
                        warnings = None, text = None, examples = None,
                        see_also = None, meta = None, attributes = None):
        className = str(style).split('.')[-1]
        parsed_doc = parse(input_text, style)
        assert parsed_doc.name == name
        assert parsed_doc.summary == summary
        if parameters is not None:
            if isinstance(parameters, list):
                assert isinstance(parsed_doc.parameters, list)

# Generated at 2022-06-13 19:44:39.919151
# Unit test for function parse
def test_parse():
    text = '''\
    This is a summary.

    This is a description.
    '''
    res = parse(text)
    assert res.summary == 'This is a summary.'
    assert res.description == 'This is a description.'


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:44:42.296281
# Unit test for function parse
def test_parse():
    text = """
        This is a test for function parse.
    """ 
    print(parse(text,style="google"))
# test_parse()

# Generated at 2022-06-13 19:44:50.374999
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Docstring
    from docstring_parser.styles import GoogleStyle, NumpyStyle, ReStructuredTextStyle
    text = """
    This is a function that does something.

    Args:
        arg1 (int): The first arg.
        arg2 (str): The second arg.

    Returns:
        bool: The return value. True for success, False otherwise.

    """

# Generated at 2022-06-13 19:44:52.584617
# Unit test for function parse
def test_parse():
    docString = """test
        test2
        test3
        test4
        """
    ret = parse(docString)
    assert ret.descr == "test\ntest2\ntest3\ntest4\n"


# Generated at 2022-06-13 19:44:59.210086
# Unit test for function parse
def test_parse():
    text = 'Return the sum of a and b.'
    parsed_obj = parse(text)
    assert(parsed_obj.content == 'Return the sum of a and b.')
    text = 'Return the sum of a and b.\n\nArgs:\n\na: int: the first number\n\nb:int: the second number'
    parsed_obj = parse(text)
    assert(parsed_obj.content == 'Return the sum of a and b.')
    assert(parsed_obj.params['a'].description == 'the first number')
    assert(parsed_obj.params['b'].description == 'the second number')
    assert(parsed_obj.params['a'].type_name == 'int')

# Generated at 2022-06-13 19:45:08.588864
# Unit test for function parse
def test_parse():
    def fooBBB(a, b):
        """fooBBB(a, b)

        Add a and b.

        :param a: first addend
        :param b: second addend
        :return: sum of a and b

        """

        return a + b

    print(parse(fooBBB.__doc__))

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:45:18.599940
# Unit test for function parse
def test_parse():

    test_input = ["""
        """
    ]
    test_output = [
        {
        'desc':'',
        'params':[],
        'meta':{},
        'returns':None
        }
    ]
    for i in range(len(test_input)):
        assert(parse(test_input[i])==test_output[i])
    print("test_parse passed")

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:45:22.819871
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    from docstring_parser.styles import GoogleDocstring
    assert isinstance(parse(""), GoogleDocstring)
    assert isinstance(parse("", style=Style.google), GoogleDocstring)

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:45:25.932823
# Unit test for function parse
def test_parse():
    """
    TODO: Write test cases.
    For now, we only test the docstring is parsed without any errors.
    """
    docstr = parse.__doc__
    assert docstr
    assert parse(docstr)

# Generated at 2022-06-13 19:45:33.875267
# Unit test for function parse
def test_parse():
    """docstring_parser.parse(text: str, style: Style = Style.auto) -> Docstring"""

    from docstring_parser.styles import numpy

    class Doc(Docstring):
        short_description = None
        long_description = None
        return_type = None
        returns = None
        yield_type = None
        yields = None
        parameters = None
        raises = None
        see_also = None
        examples = None
        meta = None
        style = numpy
        indent = 4
        truncate = 80

    # normal docstring
    text1 = '''
    func()

    input:

    :param a: int
    :return: str

    output:

    :raises ValueError: error
    '''
    result1 = parse(text1)

# Generated at 2022-06-13 19:45:36.268321
# Unit test for function parse
def test_parse():
    parse_result = parse('fdsafdsafdsafdas')
    print(parse_result)


# Generated at 2022-06-13 19:45:45.535054
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""

# Generated at 2022-06-13 19:45:53.327904
# Unit test for function parse
def test_parse():
    text = \
    '''
    This is a function which does stuff.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    str
        Description of return value
    '''

    parsed_text = parse(text)
    assert len(parsed_text) == 6
    assert parsed_text.summary == 'This is a function which does stuff.'
    assert parsed_text.description == ''
    assert len(parsed_text.params) == 2
    assert parsed_text.params[0].name == 'arg1'
    assert parsed_text.params[0].arg_type == 'int'
    assert parsed_text.params[0].description == 'Description of arg1'

# Generated at 2022-06-13 19:46:04.666377
# Unit test for function parse
def test_parse():
    text = '''
    min func(a, b)
    min func

    min func(a, b)
    returns:
        minimum(a, b)

    parameters:
        a: first value to compare
        b: second value to compare

    returns:
        minimum(a, b)

    notes:
        I am a note.
    '''
    ps = parse(text)
    assert ps.new_line == False
    assert ps.short_description == 'min func'
    assert ps.long_description == 'min func(a, b)\nmin func'

# Generated at 2022-06-13 19:46:15.390278
# Unit test for function parse
def test_parse():
    from docstring_parser.styles.google import GoogleStyle
    text = '''def foo():
        """
        A bar

        :param bar:
        :param baz:
        :rtype:
        """'''
    style = parse(text)
    assert style == GoogleStyle
    loc = locals().copy()
    glob = globals().copy()
    exec(text)
    foo = loc['foo']
    foo.__doc__ = parse(foo.__doc__)
    assert foo.__doc__ == parse(foo.__doc__)
    # docstring = parse(foo.__doc__)
    # assert docstring.summary == "A bar"
    # assert docstring.meta["param"]["bar"] == ""
    # assert docstring.meta["param"]["baz"] == ""
    # assert doc

# Generated at 2022-06-13 19:46:28.631407
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import google
    from docstring_parser.styles import numpy
    from docstring_parser.styles import epytext
    from docstring_parser.styles import javadoc

    ds = '''
    :param arg1: the first argument
    :param arg2: the second argument
    :returns: the return value
    '''
    gs = google.parse(ds)
    assert gs.args == ['arg1', 'arg2']
    assert gs.returns == 'the return value'

    ds = '''
    :Keyword arguments:
    :param arg1: the first argument
    :param arg2: the second argument
    :returns: the return value
    '''
    gs = google.parse(ds)

# Generated at 2022-06-13 19:46:32.570984
# Unit test for function parse
def test_parse():
    text = """
    triangulate(x, y, triangles, mask=None)
    Returns the interpolated points of a surface at given points.
    """
    doc = parse(text)
    return doc


# Generated at 2022-06-13 19:46:40.438477
# Unit test for function parse
def test_parse():
    assert parse("").meta == {}
    assert parse("").title == None
    assert parse("").description == ""

    # Python style docstring (all in one line)
    assert parse("This is a title.", Style.google).title == "This is a title."
    assert parse("This is a title.", Style.google).description == ""

    # NumPy style docstring (one parameter per line)
    assert parse(
        """This is a title.
This is the description.""",
        Style.numpy,
    ).title == "This is a title."
    assert parse(
        """This is a title.
This is the description.""",
        Style.numpy,
    ).description == "This is the description."

    # Google style docstring (one parameter per line)

# Generated at 2022-06-13 19:46:54.720627
# Unit test for function parse
def test_parse():
    example = """Summary line.

Description of what the function does.

Args:
    param1 (int): The first parameter.
    param2 (str): The second parameter.

Returns:
    str: The return value. True for success, False otherwise.
"""
    ret = parse(example)
    assert ret.meta['summary'].strip() == "Summary line."
    assert ret.meta['parameters'] == [
        {
            "name": "param1",
            "type_name": "int",
            "summary": "The first parameter."
        },
        {
            "name": "param2",
            "type_name": "str",
            "summary": "The second parameter."
        }
    ]

# Generated at 2022-06-13 19:46:56.592198
# Unit test for function parse
def test_parse():
    assert parse.__doc__ is not None

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:47:03.102446
# Unit test for function parse
def test_parse():
    style = Style.numpy

    assert(parse("", style) == Docstring(description=None, meta={}, errors=[], examples=[], see_also=[], notes=[], references=[], warnings=[], style=style))
    assert(parse("test", style) == Docstring(description="test", meta={}, errors=[], examples=[], see_also=[], notes=[], references=[], warnings=[], style=style))
    assert(parse("test\n", style) == Docstring(description="test", meta={}, errors=[], examples=[], see_also=[], notes=[], references=[], warnings=[], style=style))
    with pytest.raises(ParseError):
        parse(None, style)

# Generated at 2022-06-13 19:47:15.649131
# Unit test for function parse
def test_parse():
    ds = """
        A simple mathematical function ::

            >>> f(1, 2)
            3
    """
    parsed = parse(ds)
    assert parsed.summary == 'A simple mathematical function'
    assert parsed.description == ['::']
    assert parsed.meta == []
    assert parsed.examples == ['>>> f(1, 2)', '3']


    ds = """
        A simple mathematical function.

        :type param: str
        :param param: This is a parameter.
        :raises TypeError: if param is not str
    """
    parsed = parse(ds)
    assert parsed.summary == 'A simple mathematical function.'
    assert parsed.description == []

# Generated at 2022-06-13 19:47:16.482677
# Unit test for function parse
def test_parse():
    assert parse('Hello there').short_description == 'Hello there'



# Generated at 2022-06-13 19:47:26.296802
# Unit test for function parse
def test_parse():
    """Testing docstring_parser's parse function

    :returns: True if the test fails, False otherwise
    :rtype: boolean
    """
    text = """A simple docstring.
    :param int a: the first argument"""
    assert parse(text) == Docstring(
        summary='A simple docstring.',
        description='',
        meta={'param': [
            {'text': 'the first argument', 'arg_name': 'a', 'type_name': 'int'}
        ]}
    )

    text = """A simple docstring.

    :param int a: the first argument
    :param int b: the second argument
    :param int c: the third argument"""


# Generated at 2022-06-13 19:47:29.589968
# Unit test for function parse
def test_parse():
    from pprint import pprint as pp
    text = '''
    This is a docstring.
    '''
    docstr = parse(text)
    pp(docstr)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:47:34.656841
# Unit test for function parse
def test_parse():
    t = '''\
    This is the description.

    Use like so:
        result = parse(text)

    :param text: A text string.
    :returns: The parsed docstring.
    '''
    assert parse(t)
    assert parse('', style='sphinx')


# Generated at 2022-06-13 19:47:41.723873
# Unit test for function parse
def test_parse():
    def f(x, y=True):
        """One line summary.

        Extended description.

        :param x: parameter 1
        :type x: int
        :param y: parameter 2
        :type y: bool
        :returns: nothing
        :raises KeyError: raises an exception
        """
        pass
    print(parse(f.__doc__))

# Generated at 2022-06-13 19:47:49.491207
# Unit test for function parse
def test_parse():
    text = """This is a short summary"""
    assert parse(text) == Docstring(summary=text)
    text = """This is a short summary\n\nThis is multi-line summary"""
    assert parse(text) == Docstring(summary=text)
    text = """This is a short summary\n\nThis is multi-line summary\n\nStuff
    to know about arguments.\n\n:param arg1: description for arg1\n:param arg2: description for arg2"""
    assert parse(text) == Docstring(summary=text)

# Generated at 2022-06-13 19:47:56.234637
# Unit test for function parse
def test_parse():
    doc_string = '''
    :param x: x description
    :param y: y description
    :returns: returns
    :raises ValueError: value error
    '''
    result = parse(doc_string)
    assert list(result.params.keys()) == ['x', 'y']
    assert result.returns == 'returns'
    assert result.raises[0].args == ('ValueError',)


# Generated at 2022-06-13 19:48:03.037398
# Unit test for function parse

# Generated at 2022-06-13 19:48:13.300398
# Unit test for function parse
def test_parse():
    from docstring_parser.tests.test_data import TEST_DATA

    for data in TEST_DATA:
        for style, meta in data['meta'].items():
            try:
                ds = parse(data['string'], style)
                if style == Style.google:
                    assert ds.meta['args'] == meta['args']
                else:
                    assert ds.meta['parameters'] == meta['parameters']
            except AssertionError:
                try:
                    assert ds.get_meta() == meta
                except AssertionError:
                    assert ds.meta == meta


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:48:21.648720
# Unit test for function parse
def test_parse():
    docstring = parse("""Summary line.

Description:
    Additional description.

Args:
    arg1 (int): The first argument.
    arg2 (str): The second argument.

Returns:
    bool: The return value. True for success, False otherwise.

Raises:
    AttributeError: The ``AttributeError`` exception.
    ValueError: The ``ValueError`` exception.

Examples:
    Examples should be written in doctest format, and should illustrate how
    to use the function/class.
    >>> print([i for i in example_generator(4)])
    [0, 1, 2, 3]
""")
    assert docstring.short_description == "Summary line."
    assert docstring.long_description.strip() == "Additional description."

# Generated at 2022-06-13 19:48:33.320835
# Unit test for function parse
def test_parse():
    test = parse("""
    Parameters
    ----------
    a : int
        The a of the foo
    """)
    if test.params[0]['name'] != 'a':
        raise Exception("test_parse_params failed")

    test = parse("""
    Parameters
    ----------
    a : int
        The a of the foo
    
    """)
    if test.params[0]['name'] != 'a':
        raise Exception("test_parse_params failed")

    test = parse("""
    Parameters
    ----------

    a : int
        The a of the foo
    
    """)
    if test.params[0]['name'] != 'a':
        raise Exception("test_parse_params failed")


# Generated at 2022-06-13 19:48:44.026573
# Unit test for function parse
def test_parse():
    import sys
    import os
    import json
    from colorama import init, Fore, Style
    init(autoreset=True)
    import unittest
    from unittest.mock import patch

    path_dir = os.path.dirname(__file__)
    path1 = os.path.join(path_dir, "fixtures/test_parse1.json")
    test_cases1 = open(path1).read()
    test_cases1 = json.loads(test_cases1)

    path2 = os.path.join(path_dir, "fixtures/test_parse2.json")
    test_cases2 = open(path2).read()
    test_cases2 = json.loads(test_cases2)

    # def __init__(self, method, output, input):

# Generated at 2022-06-13 19:48:54.025543
# Unit test for function parse
def test_parse():
    """ Test for method parse"""
    # Test for method parse with param text = '' and style = Style.auto
    text = ''
    style = Style.auto
    try:
        # Call method parse and expect to throw exception
        rets = parse(text, style)
    except ParseError as e:
        print('Exception thrown')

    # Test for method parse with param text = 'Sample docstring for function parse' and style = Style.auto
    text = 'Sample docstring for function parse'
    style = Style.auto
    # Call method parse and expect to return Docstring
    rets = parse(text, style)
    assert rets.__class__.__name__ == 'Docstring'

    # Test for method parse with param text = 'Sample docstring for function parse' and style = Style.numpy

# Generated at 2022-06-13 19:49:05.399536
# Unit test for function parse
def test_parse():
    text = """
    This is a multi-line docstring.

    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.

    Returns:
        bool: The return value. True for success, False otherwise.
    """
    expected = Docstring(
        summary="This is a multi-line docstring.",
        description=[],
        returns=Docstring.Returns(
            description="The return value. True for success, False otherwise.",
            type="bool"
        ),
        args=[
            Docstring.Args(
                name="arg1",
                description="The first argument.",
                type="int"
            ),
            Docstring.Args(
                name="arg2",
                description="The second argument.",
                type="str"
            )
        ],
        meta={}
    )

# Generated at 2022-06-13 19:49:17.207450
# Unit test for function parse
def test_parse():
    docstring = """
    Example Google style docstrings.

    Attributes:
        module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        attr2 (list): This is a module variable too.

    Returns:
        dict: Return type is a dict with the following properties:

          dict.a (int): Returns a.
          dict.b (int): Returns b.
          dict.c (int): Returns c.

    Raises:
        ValueError: If `param2` is equal to `param1`.

    """
    parser = parse(docstring)
    assert parser.short_description == "Example Google style docstrings."
    assert parser.long_description == ""

# Generated at 2022-06-13 19:49:23.934074
# Unit test for function parse
def test_parse():
    docstring = parse("""
    Some description.
    
    :param param1: description of param 1
    :param param2: description of param 2, not optional
    :returns: description of return
    """)
    assert docstring.short_description == 'Some description.'
    assert docstring.long_description == None
    assert docstring.params == {'param1': 'description of param 1', 'param2': 'description of param 2, not optional'}
    assert docstring.returns == 'description of return'

# Generated at 2022-06-13 19:49:25.728014
# Unit test for function parse
def test_parse():
    assert isinstance(parse(""), Docstring)

# Generated at 2022-06-13 19:49:33.098360
# Unit test for function parse
def test_parse():

    # can be a valid docstring
    text = """Short summary.

Longer description.

Args:
  arg1 (str): description for arg1
  arg2 (int): description for arg2

Returns:
  bool. whether arg2 is greater than arg1
"""
    d = parse(text)
    assert len(d.args) == 2
    assert len(d.returns) == 1
    assert len(d.raises) == 0
    assert len(d.yields) == 0
    assert len(d.meta) == 2

    # not a valid docstring
    text = text.replace('Args', 'Arg')
    with pytest.raises(ParseError):
        parse(text)

# Generated at 2022-06-13 19:49:42.685595
# Unit test for function parse
def test_parse():
    doc = """\
    Summary line.
    Extended description of function.
    :param str arg1: The first argument.
    :param int arg2: The second argument.
    :returns: Description of return value.
    :raises TypeError: if required parameter types are not met."""
    parsed = parse(doc)
    assert isinstance(parsed, Docstring)
    assert parsed.short_description == "Summary line."
    assert parsed.long_description == "Extended description of function."
    assert parsed.params == {
        "arg1": {"type": str, "description": "The first argument."},
        "arg2": {"type": int, "description": "The second argument."},
    }
    assert parsed.returns == {"type": None, "description": "Description of return value."}
    assert parsed.ra

# Generated at 2022-06-13 19:49:46.221384
# Unit test for function parse
def test_parse():
    docstring = parse(u'''
    Single-line docstring.
    ''')
    assert docstring.short_description == 'Single-line docstring.'

# Generated at 2022-06-13 19:49:58.179844
# Unit test for function parse
def test_parse():
    text = '''Hello world,
    this is a function.
    :param a: the first parameter
    :param b: the second parameter
    :returns: some values
    '''
    parsed = parse(text)
    assert hasattr(parsed, 'short_description')
    assert hasattr(parsed, 'long_description')
    assert hasattr(parsed, 'meta')
    assert getattr(parsed, 'meta') == {
        'returns': ':returns: some values',
        'param a': ':param a: the first parameter',
        'param b': ':param b: the second parameter'
    }
    assert hasattr(parsed, 'returns')
    assert getattr(parsed, 'returns') == ':returns: some values'
    assert has

# Generated at 2022-06-13 19:50:08.297327
# Unit test for function parse
def test_parse():
    """Test function parse."""

    docstring = """\
    This is a test function.

    :param str name: The name to say hello to
    :param int repeat: The number of times to repeat the greeting
    :returns: The generated message or None
    :raises ValueError: If repeat is negative
    """
    parsed = parse(docstring)
    assert parsed.short_description == "This is a test function."

    assert parsed.long_description == ""

    assert len(parsed.meta) == 3
    assert parsed.meta["param"][0].arg_name == "name"
    assert parsed.meta["param"][0].arg_type == "str"
    assert parsed.meta["param"][0].description == "The name to say hello to"
    assert parsed.meta["param"][1].arg_name

# Generated at 2022-06-13 19:50:11.908818
# Unit test for function parse
def test_parse():
    text = '''
        # a function that echos the input
        def echo(text):
            print(text)
    '''
    style = Style('numpy')
    docstring = parse(text, style)
    assert docstring.short_description == '# a function that echos the input'


# Generated at 2022-06-13 19:50:24.626611
# Unit test for function parse
def test_parse():
    """
    Test suite for function parse
    :return: None
    """
    def fn():
        """
        This is a test function

        Args:
            x: integer (default: 3)
            y (int, optional): integer (default: 3)
            s: string

        Returns:
            None
        """
        pass

    docstring_parser = parse(fn.__doc__)
    assert docstring_parser.short_description == 'This is a test function'
    assert docstring_parser.params['x'].description == '(default: 3)'
    assert docstring_parser.params['s'].description == ''

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:50:28.318190
# Unit test for function parse
def test_parse():
    """Function unit test"""
    text = "This is a wonderful function."
    ret = parse(text)
    assert ret.short_description == 'This is a wonderful function.'

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:50:35.253526
# Unit test for function parse
def test_parse():
    text_1 = """
    This is a function with a docstring.

    Args:
        x: a parameter
        y: another parameter

    Returns:
        A :class:`~pkg.AwesomeClass`.
    """
    doc = parse(text_1)
    assert doc.short_description == "This is a function with a docstring."
    assert doc.long_description == ""
    assert doc.args[0].arg_name == "x"
    assert doc.args[0].description == "a parameter"
    assert doc.args[1].arg_name == "y"
    assert doc.args[1].description == "another parameter"
    assert doc.returns.description == "A :class:`~pkg.AwesomeClass`."

# Generated at 2022-06-13 19:50:38.818065
# Unit test for function parse
def test_parse():
    assert parse("one\ntwo") == Docstring(
        summary="one", description="two", __style__=Style.pep257
    )

# Generated at 2022-06-13 19:50:49.723075
# Unit test for function parse
def test_parse():
    example_docstring = parse('''
    This is an example of a Google style docstring.

    Args:
        param1 (int): The first parameter.
        param2 (str, optional): The second parameter. Defaults to 'world'.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: The return value. True for success, False otherwise.

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
        that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.
    ''')
    print(example_docstring)

    assert example_docstring.short_description == 'This is an example of a Google style docstring.'

# Generated at 2022-06-13 19:50:58.113556
# Unit test for function parse
def test_parse():
    doc = ("This is a test docstring.\n"
           "It will return a string.\n"
           "\n"
           "    This is a line with leading whitespaces.\n"
           "\n"
           "Parameters\n"
           "----------\n"
           "param1 : string\n"
           "    A parameter named param1.\n"
           "\n"
           "Returns\n"
           "-------\n"
           "string\n"
           "    Return value result.")
    d = parse(doc)

# Generated at 2022-06-13 19:51:01.365154
# Unit test for function parse
def test_parse():
    test_text = '''\
    This is a function
    '''
    style = Style.google
    parse(test_text, style)
    assert 1

# Generated at 2022-06-13 19:51:04.388375
# Unit test for function parse
def test_parse():
    print(parse.__doc__)
    print(parse(None))

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:51:13.088691
# Unit test for function parse
def test_parse():

    expected = Docstring(summary='foo', description='desc')
    assert parse('foo\n\ndesc\n') == expected

    expected = Docstring(description='desc')
    assert parse('desc\n') == expected

    expected = Docstring(description='desc\n')
    assert parse('desc\n\n') == expected

    expected = Docstring(summary='foo', description='desc')
    assert parse('foo\n\ndesc') == expected

    expected = Docstring(summary='foo', description='desc')
    assert parse('foo\n\ndesc\n\n') == expected

# Generated at 2022-06-13 19:51:18.714245
# Unit test for function parse
def test_parse():
    import os
    import docstring_parser.__main__ as main
    cwd = os.getcwd()
    try:
        os.chdir(os.path.dirname(__file__))
        os.chdir('..')
        main.main(['--dump', 'docstring_parser'])
    finally:
        os.chdir(cwd)
    return True
