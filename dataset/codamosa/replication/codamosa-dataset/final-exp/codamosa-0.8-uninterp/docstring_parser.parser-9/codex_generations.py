

# Generated at 2022-06-13 19:41:34.513973
# Unit test for function parse
def test_parse():
    d = parse("""\
    First line of docstring.

    More line of docstring.
    And some more lines!""")
    assert d.meta == [{'title': '', 'desc': 'More line of docstring.\nAnd some more lines!'}]
    assert str(d) == '    First line of docstring.\n\n    More line of docstring.\n    And some more lines!'
    assert len(d.meta) == 1

# Generated at 2022-06-13 19:41:41.492164
# Unit test for function parse
def test_parse():
    text = '''
    This tests that the parser properly parses docstrings with varying style
    indentation.

    :param name: The name to say hello to
    :type name: str
    :param ttl: The number of times to say hello
    :type ttl: int, optional
    :returns: None
    :raises TypeError: If ``name`` is not a string
    '''

    docstring = parse(text, style=Style.numpy)
    assert docstring.short_description == 'This tests that the parser properly parses docstrings with varying style indentation.'
    assert str(docstring.long_description) == '<BLANKLINE>'
    assert docstring.returns.type_name == 'None'
    assert docstring.raises[0].type_name == 'TypeError'

# Generated at 2022-06-13 19:41:52.429127
# Unit test for function parse
def test_parse():
    ds = parse('Test docstring')
    assert ds['title'] == 'Test docstring'

    ds = parse('Test docstring\nMore stuff')
    assert ds['title'] == 'Test docstring'

    ds = parse('Test docstring\n---------------\nMore stuff')
    assert ds['title'] == 'Test docstring'

    ds = parse('Test docstring\n---------------\n\nMore stuff')
    assert ds['title'] == 'Test docstring'
    assert ds['description'] == 'More stuff'

    ds = parse('Test docstring\n---------------\n\nMore stuff\n\nMore stuff')
    assert ds['title'] == 'Test docstring'
    assert ds['description'] == 'More stuff\n\nMore stuff'


# Generated at 2022-06-13 19:41:59.299916
# Unit test for function parse
def test_parse():
    import copy
    import pytest
    from docstring_parser.common import Docstring, ParseError
    from docstring_parser.styles import Style
    from docstring_parser.utils import indent_text
    from docstring_parser._utils import FunctionInfo


# Generated at 2022-06-13 19:42:06.020508
# Unit test for function parse
def test_parse():
    import unittest
    class TestParse(unittest.TestCase):
        """Unit test for function parse."""
        def test_parse(self):
            text = '''Test parse function.
            '''
            d = parse(text)
            self.assertEqual(d.summary, 'Test parse function.')
            self.assertEqual(d.args, {})
            self.assertEqual(d.params, {})
            self.assertEqual(d.ret, [])

    unittest.main()

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:42:13.668602
# Unit test for function parse
def test_parse():
    """Test function parse"""
    from docstring_parser.styles import GoogleStyle, NumpydocStyle
    from docstring_parser.common import Docstring, Params, Return, Yield, Raises, SeeAlso, Note
    from docstring_parser.common import Param, Field, FieldList, DataType, Type
    from docstring_parser.common import Examples, Example

    google_docstring = """This is a sample docstring for the function (Google Style)

Args:
    param1 (int): The first parameter.
    param2 (str): The second parameter.
    *args: Variable length argument list.
    **kwargs: Arbitrary keyword arguments.

Returns:
    bool: The return value. True for success, False otherwise.

Raises:
    AttributeError, KeyError, ValueError

"""
    numpy_docstring

# Generated at 2022-06-13 19:42:18.083081
# Unit test for function parse
def test_parse():
    docstring = "Parse the docstring into its components."

    doc = parse(docstring)
    assert doc.short_description == docstring
    assert doc.summary == docstring
    assert doc.meta.title == "parse"
    assert doc.meta.type == "function"

# Generated at 2022-06-13 19:42:29.390147
# Unit test for function parse
def test_parse():
    from .common import ParseError
    from .styles.google import GoogleStyle, ParseError
    from .styles.numpy import NumpyStyle, ParseError
    from .styles.restructuredtext import ReStructuredTextStyle, ParseError
    from .styles.sphinx import SphinxStyle, ParseError
    from .utils import short_repr

    s = "Example docstring."
    d = parse(s)
    assert d.short_description == s
    assert d.long_description == ""
    assert d.meta == {}

    s = parse.__doc__
    d = parse(s)
    assert d.short_description
    assert d.long_description
    assert d.meta
    assert d.meta["param"][0].name == "text"


# Generated at 2022-06-13 19:42:37.886705
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import google
    from docstring_parser.styles import numpy
    from docstring_parser.styles import pandas
    from docstring_parser.styles import reST
    from docstring_parser.styles import sphinx
    from docstring_parser.styles import google
    from docstring_parser.styles import numpy
    from docstring_parser.styles import pandas
    from docstring_parser.styles import reST
    from docstring_parser.styles import sphinx
   
    # All style tests
    assert isinstance(parse(text, style=Style.google), google.Docstring)
    assert isinstance(parse(text, style=Style.numpy), numpy.Docstring)
    assert isinstance(parse(text, style=Style.pandas), pandas.Docstring)

# Generated at 2022-06-13 19:42:40.210969
# Unit test for function parse
def test_parse():
    Docstring.parse("")
    Docstring.parse("")
    Docstring.parse("")
    Docstring.parse("")
    Docstring.parse("")

# Generated at 2022-06-13 19:42:51.667773
# Unit test for function parse
def test_parse():
    """Test function parse."""

    text = '''
    This is a summary.

    This is a description.

    And this is another paragraph.

    :param x: param foo
    :type x: str, default 'foo'
    :raises RuntimeError: if something bad happens
    :returns: 42
    :rtype: int
    '''
    docstring = parse(text)

    # Test metadata (meta)
    assert docstring.meta["param"]["x"]["annotation"] == "str, default 'foo'"
    assert docstring.meta["param"]["x"]["description"] == "param foo"
    assert docstring.meta["raises"]["RuntimeError"]["description"] == "if something bad happens"
    assert docstring.meta["returns"]["description"] == "42"


# Generated at 2022-06-13 19:42:58.702815
# Unit test for function parse
def test_parse():
    import example
    doc = """first line

    :param str a: test a
    :param str b: test b
    :returns: xxx

    """
    ret = parse(doc)
    print(ret)
    assert doc == ret.content
    assert ret.meta['returns'] == 'xxx'
    assert ret.meta['param str a'] == 'test a'
    assert ret.meta['param str b'] == 'test b'


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:43:09.444034
# Unit test for function parse
def test_parse():
    text = '''
    :param int num: the number
    :param str name: the name
    :return: the result
    :rtype: str
    '''
    doc = parse(text, Style.google)
    params = doc.params
    assert doc.return_type == 'str'
    assert len(params) == 2
    assert params[0].name == 'num'
    assert params[0].type == 'int'
    assert params[0].description == 'the number'
    assert params[1].name == 'name'
    assert params[1].type == 'str'
    assert params[1].description == 'the name'
    return True

# Generated at 2022-06-13 19:43:14.626550
# Unit test for function parse
def test_parse():
    """Test case for function parse."""
    docstring_text = '''
    """Parse the docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation

    """
    '''
    result = parse(docstring_text)
    print(result)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:43:18.609442
# Unit test for function parse
def test_parse():
    docstring = '''Unit test for function parse.
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    '''
    assert parse(docstring) != 'docstring'

# Generated at 2022-06-13 19:43:27.324336
# Unit test for function parse
def test_parse():
    text = """\
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    docstring = parse(text)
    assert docstring.short_description == ""
    assert docstring.long_description == ""
    assert len(docstring.params) == 2
    assert docstring.returns.name == "parsed docstring representation"
    assert docstring.returns.type == ""
    assert docstring.returns.desc == ""
    assert len(docstring.raises) == 0

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:43:40.740257
# Unit test for function parse
def test_parse():
    text = '''
    This is a test for the parse function.
        :param text: docstring text to parse
        :param style: docstring style
        :returns: parsed docstring representation
    '''

    text2 = '''
    This is a test for the parse function.
        @param text: docstring text to parse
        @param style: docstring style
        @returns: parsed docstring representation
    '''
    #print(parse(text, Style.numpy))
    assert parse(text, Style.numpy) == parse(text2, Style.google) == parse(text, Style.auto)
    assert parse(text, Style.numpy).short_description == 'This is a test for the parse function.'
    assert parse(text, Style.numpy).long_description == ''

# Generated at 2022-06-13 19:43:46.427775
# Unit test for function parse
def test_parse():
    comment = """
        Utility method to create a class with a metaclass.
        """

    method_name = 'test_method'
    return_type = 'str'
    parameters = [('arg', 'str', 'First argument'), ('kwarg', 'int', 'Second argument')]

    doc = parse(comment)
    assert doc.short_description == comment.strip()
    assert doc.long_description == ''
    assert doc.tags == {}

    print(doc)

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:43:53.132572
# Unit test for function parse

# Generated at 2022-06-13 19:44:01.754743
# Unit test for function parse

# Generated at 2022-06-13 19:44:09.076540
# Unit test for function parse
def test_parse():
    text = '''
    Example function with types documented in the docstring.

    :param int n: The integer to test
    :param float x: The float to test
    :param str s: The string to test
    :param bool b: The boolean to test
    :return: True
    '''
    parse(text)

# Generated at 2022-06-13 19:44:16.434695
# Unit test for function parse
def test_parse():
    text = '''\
    Summary line.

    Extended description.

    :param foo: description of foo
    :type foo: str
    :param bar: description of bar
    :type bar: int

    :returns: description of return value
    :rtype: float
    '''
    docstring = parse(text)
    assert docstring.short_description == 'Summary line.'
    assert docstring.long_description == 'Extended description.'
    assert docstring.params['foo'].description == 'description of foo'
    assert docstring.params['foo'].types == ['str']
    assert docstring.params['bar'].description == 'description of bar'
    assert docstring.params['bar'].types == ['int']
    assert docstring.returns.description == 'description of return value'

# Generated at 2022-06-13 19:44:31.020091
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Docstring, ParseError
    from docstring_parser.styles import STYLES, Style

    #text = '''\
    #    :param text: docstring text to parse
    #    :param style: docstring style
    #    :returns: parsed docstring representation
    #'''
    text = '''\
        :param text: docstring text to parse
        :returns: parsed docstring representation
    '''

    if Style != Style.auto:
        return STYLES[Style](text)
    rets = []
    for parse_ in STYLES.values():
        try:
            rets.append(parse_(text))
        except ParseError as e:
            print(e)
    if not rets:
        print(rets)

# Generated at 2022-06-13 19:44:34.081151
# Unit test for function parse
def test_parse():
    text = '''
:param param1: the first parameter
:param param2: the second parameter
:returns: description of what is returned
:raises keyError: raises an exception
'''

    p = parse(text)
    print(p.to_dict())

#if __name__ == '__main__':
#    test_parse()

# Generated at 2022-06-13 19:44:44.620828
# Unit test for function parse
def test_parse():
    """
    Unit test for function parse
    """

    test_text = '''
    This function is used to test function parse
    :param data: input data
    :param k: the order parameter
    :returns: k neighbors
    '''

    test_doc = parse(test_text, style='numpy')

    assert test_doc.short_description == 'This function is used to test function parse'
    assert test_doc.long_description == ''

    assert test_doc.returns.type_name == 'k neighbors'
    assert test_doc.returns.description == ''

    assert test_doc.params['data'].type_name == 'input data'
    assert test_doc.params['data'].description == ''
    assert test_doc.params['k'].type_name == 'the order parameter'

# Generated at 2022-06-13 19:44:49.196060
# Unit test for function parse
def test_parse():

    doc = r"""Single line docstring."""
    assert parse(doc) == Docstring(short_description="Single line docstring.")

    doc = r"""Single line docstring with a period."""
    assert parse(doc) == Docstring(short_description="Single line docstring with a period.")

    doc = r"""Single line docstring with a period.\n"""
    assert parse(doc) == Docstring(short_description="Single line docstring with a period.")

    doc = r"""Single line docstring with a period.

    And nothing else.
    """
    assert parse(doc).short_description == "Single line docstring with a period."

    doc = r"""Single line docstring with a period.

    Args:
    arg1 (str): The first argument.
    arg2 (int): The second argument.
    """

# Generated at 2022-06-13 19:44:54.020802
# Unit test for function parse
def test_parse():
    from docstring_parser.parser import parse
    from docstring_parser.styles import NumpydocStyle, GoogleStyle
    from docstring_parser.utils import parse_type_annotation

    assert isinstance(parse('hello world'), NumpydocStyle)
    assert isinstance(parse('param x: foo', style=GoogleStyle), GoogleStyle)
    assert parse('param x: foo').params[0].type_annotation == parse_type_annotation('foo')

# Generated at 2022-06-13 19:44:55.718718
# Unit test for function parse
def test_parse():
	print(parse('@author jbasko'))

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:45:01.501188
# Unit test for function parse
def test_parse():
    text = """This function does something.

Args:
  really (bool): Does it do it really?
  hard (bool): Does it do it hard?

Returns:
    bool: If this function does something hard.

Examples:
    >>> from docstring_parser import parse
    >>> parse('''This function does something.
    ...
    ... Args:
    ...   really (bool): Does it do it really?
    ...   hard (bool): Does it do it hard?
    ...
    ... Returns:
    ...     bool: If this function does something hard.
    ... ''')
    ['Args:', '  really (bool) = Does it do it really?', '  hard (bool) = ', 'Returns:', '    bool = If this function does something hard.']
"""
    docstring = parse(text)
   

# Generated at 2022-06-13 19:45:06.903532
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleStyle
    print(parse("""
        >>> print("Foo")
        Foo
        """))
    print(parse("""
    >>> print("Foo")
    Foo
    """, style=GoogleStyle))


# Generated at 2022-06-13 19:45:22.370163
# Unit test for function parse
def test_parse():

    class TestClass:
        """Here is a docstring.

        Some intresting/required information.

        :param a: parameter a
        :param b: parameter b
        """
        def __init__(self, a, b):
            pass

    assert parse('').short_description == ''

    assert parse("Here is a docstring.").short_description == "Here is a docstring."

    assert parse("Here is a docstring.\nand some more information.").short_description == "Here is a docstring."

    assert parse("Here is a docstring.\nand some more information.\n").short_description == "Here is a docstring."

    assert parse("Here is a docstring.\nand some more information.\n\n").short_description == "Here is a docstring."


# Generated at 2022-06-13 19:45:27.286811
# Unit test for function parse
def test_parse():
    from pprint import pprint
    doc = """This is a Test Module.
    This is second line.

    :param logger: An instance of a standard Python logger.
    :type logger: object
    :param debug: Boolean to enable debug logging

    :return: An instance of a standard Python logger.
    :rtype: object
    """
    pprint(parse(doc))


# Generated at 2022-06-13 19:45:29.796633
# Unit test for function parse
def test_parse():
    assert parse('hello world') == Docstring(summary="hello world")

    with pytest.raises(ParseError) as err:
        assert parse('hello')
    assert str(err.value) == 'no summary provided'

# Generated at 2022-06-13 19:45:41.123052
# Unit test for function parse
def test_parse():
    text = """
    The first line of the docstring.
    It may be a brief description of the function.
    It should fit in one line, unless the line becomes too long.
    In that case, break the line into multiple lines.

    The following lines are the detailed description.
    It should explain the arguments taken by the function,
    and explain what the function does.
    """
    assert parse(text).short_description == "The first line of the docstring."
    assert (parse(text).long_description ==
            "It may be a brief description of the function.\n"
            "It should fit in one line, unless the line becomes too long.\n"
            "In that case, break the line into multiple lines.")

# Generated at 2022-06-13 19:45:51.621535
# Unit test for function parse
def test_parse():
    text = '''
    Python function example
    This is a python function
    :type: gdf
    :python_version: 3.6
    :param x: the first element
    :type x: float
    :param y: the second element
    :type y: float
    :return: the result of add x and y
    :rtype: float
    '''

# Generated at 2022-06-13 19:46:03.048720
# Unit test for function parse
def test_parse():
    docstring = """
    Single-line docstring.

    :param arg1: The first argument.
    :type arg1: str
    :param arg2: The second argument.
    :type arg2: int, optional
    :param arg3: The third argument.
    :type arg3: list of str, optional
    :param arg4: The fourth argument.
    :type arg4: int or str
    :returns: str
    :raises: ValueError, TypeError
    """
    meta, body = parse(docstring)
    assert meta.summary == 'Single-line docstring.'
    assert len(meta.params) == 4
    assert meta.returns == 'str'
    assert len(meta.raises) == 2
    assert meta.raises[0] == 'ValueError'
    assert meta.raises

# Generated at 2022-06-13 19:46:05.976147
# Unit test for function parse
def test_parse():
    assert parse("Test this docstring.", style=Style.google) == Docstring(
        summary="Test this docstring."
    )


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:46:11.377797
# Unit test for function parse
def test_parse():
    d1 = parse('test')

    # Test for the style of docstring
    # Input the text of docstring
    # print the style of the docstring
    if d1.style == 'sphinx':
        print('sphinx')
    else:
        print('other')



# Generated at 2022-06-13 19:46:16.496468
# Unit test for function parse
def test_parse():
    test_cases = [
        ('Hello World', Style.auto),
        ('Hello World', Style.numpy),
        ('Hello World', Style.google),
        ('Hello World', Style.sphinx),
    ]


    for text, style in test_cases:
        try:
            parsed = parse(text, style)
            print(parsed)
        except:
            print('Fail')





if __name__ == "__main__":    
    test_parse()

# Generated at 2022-06-13 19:46:28.331693
# Unit test for function parse
def test_parse():
    # test parsing reST style docstrings
    rst_doc = """One line summary.

Longer description.

:param param1: This is a first param
:param param2: This is a second param
:returns: This is a description of what is returned
:raises keyError: raises an exception
"""
    result = parse(rst_doc)
    assert result.short_description == "One line summary."
    assert result.long_description == ["Longer description."]
    assert result.meta['parameters'] == [
        dict(name='param1', description='This is a first param', type=None),
        dict(name='param2', description='This is a second param', type=None)
    ]

# Generated at 2022-06-13 19:46:33.621634
# Unit test for function parse
def test_parse():
    print('Running function test in parse.py')
    text = '''
    This is a docstring.
    
    Multiline
    header
    '''
    d = parse(text)
    assert d.short_description == 'This is a docstring.'
    assert d.long_description == 'Multiline\nheader'

# Generated at 2022-06-13 19:46:37.294502
# Unit test for function parse
def test_parse():
    docstring = '''Function that does division
    :param str a: devisor
    :param str b: dividend
    :returns str: division result
    '''
    assert parse(docstring).as_dict() == {'a': 'devisor', 'b': 'dividend'}

# Generated at 2022-06-13 19:46:40.578262
# Unit test for function parse
def test_parse():
    text = """
    .. meta::
        :key: val
        :key: val
    """
    ret = parse(text)
    assert ret.meta[0].key == "key"
    assert ret.meta[0].val == "val"
    assert ret.meta[1].key == "key"
    assert ret.meta[1].val == "val"


# Generated at 2022-06-13 19:46:54.846195
# Unit test for function parse
def test_parse():
    text = """\
    :param input: input data
    :type input: numpy.ndarray
    :param key: sort key (optional)
    :type key: str
    :raises: TypeError

    The description...
    """
    docstring = parse(text, Style.numpy)

    assert docstring.short_description == 'The description...'
    assert docstring.long_description == ''
    assert docstring.params == [
        {
            'arg': 'input',
            'annotation': 'numpy.ndarray',
            'description': 'input data'
        }, {
            'arg': 'key',
            'annotation': 'str',
            'description': 'sort key (optional)',
            'optional': True
        },
    ]
    assert docstring.returns == {}
    assert doc

# Generated at 2022-06-13 19:47:03.007390
# Unit test for function parse
def test_parse():
    assert parse('Hello world') == Docstring(
        summary='Hello world',
        description='',
        params={},
        returns=None,
    )

    assert parse('Hello world.\n\nBye world.') == Docstring(
        summary='Hello world.',
        description='Bye world.',
        params={},
        returns=None,
    )

    assert parse('Hello world.\n\n  By world.\n\nYeah.') == Docstring(
        summary='Hello world.',
        description='By world.\n\nYeah.',
        params={},
        returns=None,
    )


# Generated at 2022-06-13 19:47:14.540820
# Unit test for function parse
def test_parse():
    import textwrap
    docstring = """
    Unit test for function parse in docstring_parser.__init__.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    print("Parse with style Google")
    print(parse(docstring, style=Style.google))
    print("Parse with style Numpy")
    print(parse(docstring, style=Style.numpy))
    docstring = """
    Unit test for function parse in docstring_parser.__init__.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    print("Parse with style Google")
    print(parse(docstring, style=Style.google))

# Generated at 2022-06-13 19:47:22.286995
# Unit test for function parse
def test_parse():
    """Test docstring parsing."""
    text = '''
        Summary line.

        Extended description.

        Parameters
        ----------
        arg1 : int
            Description of arg1
        arg2 : str
            Description of arg2

        Returns
        -------
        bool
            Description of return value.
        '''

    docstring = parse(text)
    # Tests for class docstring_parser.common.Docstring:
    assert docstring.summary == 'Summary line.'
    assert docstring.extended_summary == 'Extended description.'
    assert docstring.body == 'Summary line.\n\nExtended description.'
    assert docstring.params[0].arg_name == 'arg1'
    assert docstring.params[0].type_name == 'int'

# Generated at 2022-06-13 19:47:23.448524
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import Style

# Generated at 2022-06-13 19:47:33.087612
# Unit test for function parse
def test_parse():
    data1 = parse(
        '''
        A short summary line.

        A longer description of the module with separate paragraphs.

            >>> print('foo')
            foo

        :param int bar: a parameter named `bar`
        :param str baz: another parameter named `baz`
        :returns: What this function returns
        :rtype: str


        '''
    )
    data2 = parse(
        '''
        A short summary line.

        A longer description of the module with separate paragraphs.

            >>> print('foo')
            foo

        Args:
            bar (int): a parameter named `bar`
            baz (str): another parameter named `baz`

        Returns:
            What this function returns
        '''
    )
    data2.style = 'numpy'

# Generated at 2022-06-13 19:47:42.381699
# Unit test for function parse
def test_parse():
    test_str = """docstring_parser.parse(text: str, style: Style = Style.auto) -> Docstring:
    """
    test_par = parse(test_str)
    assert test_par.meta == {
            'text': ('str', ''),
            'style': ('Style', 'Style.auto'),
            }
    assert test_par.summary == 'parse'
    assert test_par.description == 'docstring_parser.parse'
    assert test_par.returns == ('Docstring', '')
    assert test_par.extras == {}

# Generated at 2022-06-13 19:47:56.013180
# Unit test for function parse
def test_parse():
    """Test different types of docstring styles and exceptions"""
    # Test one line docstring
    try:
        parse('Return the sum of a and b.')
    except ParseError as exc:
        assert exc.args[0] == 'Single line docstring.'
    # Test empty docstring
    try:
        parse('')
    except ParseError as exc:
        assert exc.args[0] == 'Empty docstring.'
    # Test epytext
    text = """
    @param foo: This is foo
    @type foo: string
    """
    result = parse(text)
    assert result.meta['foo'] == 'This is foo'
    # Test numpydoc
    text = """
    Parameters
    ----------
    foo : str
        This is foo.
    """
    result = parse(text)

# Generated at 2022-06-13 19:48:02.489245
# Unit test for function parse
def test_parse():
    text = """This is a function with multiple lines.
    
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
    
    """
    docstring = parse(text)
    assert docstring.short_description == "This is a function with multiple lines."
    assert docstring.long_description == "This is a function with multiple lines."
    assert docstring.params["param1"] == "The first parameter."
    assert docstring.params["param2"] == "The second parameter."
    assert docstring.returns == "True if successful, False otherwise."
    print("tests passed!", __file__)

# Generated at 2022-06-13 19:48:14.891151
# Unit test for function parse
def test_parse():
    docstring = """\
One line summary.

Extended description.

:param arg1: Description of arg1.
:type arg1:  int
:param arg2: Description of arg2.
:type arg2:  str
:returns: Description of return value.
:rtype:  int

:raises keyError: When a key error is encountered.
:raises ImportError: When an import error is encountered.
"""


# Generated at 2022-06-13 19:48:22.527447
# Unit test for function parse
def test_parse():
    docstring = """
        Test function for a function.
        Test function. Test function.
        Test function. Test function.
        Test function. Test function.
        Test function. Test function.
        Test function. Test function.
        Test function. Test function.
        Test function. Test function.

        :param str param1: parameter 1
        :param int param2: parameter 2
        :param str param3: parameter 3
        :return: returns something
        :rtype: str
    """
    test = parse(docstring)
    assert test.short_description == 'Test function for a function.'

# Generated at 2022-06-13 19:48:34.357594
# Unit test for function parse
def test_parse():
    docstring = """
    This is a sample docstring

    :param test: the parameter1
    :type test: int
    :param test2: the parameter 2
    :type test2: bool
    :return: the return
    :rtype: str
    :raises ValueError: if something goes wrong
    """
    docstring_object = parse(docstring)
    assert docstring_object.short_description == "This is a sample docstring"
    assert len(docstring_object.params) == 2
    assert docstring_object.params['test'].location == 'param'
    assert docstring_object.params['test'].arg_type == 'int'
    assert docstring_object.params['test'].description == 'the parameter1'
    assert docstring_object.returns.type_name == 'str'


# Generated at 2022-06-13 19:48:45.007422
# Unit test for function parse
def test_parse():
    parse('Para1\n    Para2')
    parse('''Para1
    Para2
    Para3
''')
    parse('''Para1
    Para2
    Para3

''')
    parse('''Para1
    Para2
    Para3
        
''')
    parse('''Para1
         Para2
         Para3
''')
    parse('''Para1
         Para2
         Para3
        
''')
    parse('\n    Para1\n    Para2')
    parse('''\n    Para1
         Para2\n    Para3
''')
    parse('''\n
    Para1
C1: xxx
\n''')

# Generated at 2022-06-13 19:48:51.335526
# Unit test for function parse

# Generated at 2022-06-13 19:49:01.850429
# Unit test for function parse
def test_parse():
    docstring = parse("""
        This is a short description.

        This is a long description.

        :param foo: A foo parameter
        :param bar: A bar parameter
        :returns: A return value
        :raises TypeError: if bar is wrong
    """)
    assert docstring.short_description == "This is a short description."
    assert docstring.long_description == "This is a long description."
    assert docstring.params == [
        {"name": "foo", "type": "", "desc": "A foo parameter"},
        {"name": "bar", "type": "", "desc": "A bar parameter"},
    ]
    assert docstring.returns == {
        "type": "", "desc": "A return value"
    }

# Generated at 2022-06-13 19:49:06.218752
# Unit test for function parse
def test_parse():
    text = """
    Parameters
    ----------
    a: int
        A integer
    b: dict
        A dict
    """

    doc = parse(text, style = Style.numpy)
    print(doc)

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:49:09.261450
# Unit test for function parse
def test_parse():
    assert parse('abc') == 'abc'
    assert parse('abc', style=Style.numpy) == 'abc'

# Generated at 2022-06-13 19:49:20.811760
# Unit test for function parse
def test_parse():
    text = """\
    A docstring.

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

    """
    expected = Docstring(
        summary="A docstring.",
        body="The first parameter.\n\nThe second parameter.",
        parameters=[
            {'name': 'param1', 'type': 'int', 'summary': 'The first parameter.'},
            {'name': 'param2', 'type': 'str', 'summary': 'The second parameter.'},
        ],
        returns=[{'name': None, 'type': 'bool', 'summary': 'True if successful, False otherwise.'}]
    )
    assert parse(text) == expected

# Generated at 2022-06-13 19:49:27.486820
# Unit test for function parse
def test_parse():
    doc = parse('')
    assert len(doc.__dict__) == 9
    assert doc.short_description == ''
    assert doc.long_description == ''
    assert doc.params == []
    assert doc.returns == None
    assert doc.raises == []
    assert doc.yields == None
    assert doc.warns == []
    assert doc.versionadded == None
    assert doc.versionchanged == None

# Generated at 2022-06-13 19:49:32.954758
# Unit test for function parse
def test_parse():
    from docstring_parser.parser import parse
    docstring = """Simple function.
    :param arg1: The first argument.
    :param arg2: The second argument.
    :returns: Description of return value.
    :raises keyError: raises an exception
    """
    parsed = parse(docstring)
    assert len(parsed.meta) == 4
    assert len(parsed.sections) == 1
    assert parsed.sections[0].title == "Args"
    assert len(parsed.sections[0].content) == 2

# Generated at 2022-06-13 19:49:34.453312
# Unit test for function parse
def test_parse():
    test_string = '''This is a test module
    
    It is a test!
    '''

    assert parse(text=test_string, style=Style.numpy).docstring == test_string

# Generated at 2022-06-13 19:49:42.301542
# Unit test for function parse
def test_parse():
    text = """Summary line.
    Description. Extended description.
    Args:
        param1: Description of `param1`.
        param2: Description of `param2`
    Returns:
        Description of return value.
    """
    exp_doc = {'summary': 'Summary line.',
                'description': 'Description. Extended description.',
                'meta': {'Args': {'param1': 'Description of `param1`.',
                                  'param2': 'Description of `param2`'},
                         'Returns': 'Description of return value.'}}
    
    doc = parse(text)
    assert doc == exp_doc

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:49:54.038914
# Unit test for function parse
def test_parse():
    text = """key1, key2: This is a function.
    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.
            Does not have to be a string.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    """
    result = parse(text)
    assert result.short_description == "This is a function."
    assert result.long_description == ""
    assert result.meta.get("key1") == ""
    assert result.meta.get("key2") == ""
    assert result.params[0].arg_name == "arg1"
    assert result.params[0].type_name == "int"
    assert result.params[0].description == "The first argument."
    assert result.returns.type_name == ""

# Generated at 2022-06-13 19:50:02.699178
# Unit test for function parse
def test_parse():
    text = """This is a test docstring for function parse.
    This is meta data for test docstring.\n
    This is the first line of the docstring.

    This is the second line of the docstring.

    This is the third line of the docstring.

    This is the fourth line of the docstring.

    This is the last line(fifth) of the docstring.
    """

    style = Style.sphinx

    result = parse(text, style)

    assert result.meta == 'This is meta data for test docstring.\n'
    assert result.short_description == 'This is a test docstring for function parse.'

# Generated at 2022-06-13 19:50:10.474326
# Unit test for function parse
def test_parse():
    text = """
    Get IP address.

    This function is used to get IP address of the device.

    Parameters
    ----------
    ret : int
        Return the IP address.
    """

    val = parse(text,style = Style.numpy)
    str_assert = str(val)
    assert(str_assert.find("Function: Get IP address") == 0)
    assert(str_assert.find("Source: This function is used to get IP address of the device.") > 0)
    assert(str_assert.find("Parameters: {ret: {Description: Return the IP address., Params: , Type: int}}") > 0)

# Generated at 2022-06-13 19:50:17.891150
# Unit test for function parse
def test_parse():
    docstring_text = """
    Unit test for function parse

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    actual = parse(docstring_text)
    assert actual.short_description == 'Unit test for function parse'
    assert actual.long_description == ''
    
    assert actual.params['text'].arg_type == 'str'
    assert actual.params['style'].arg_type == 'Style'
    assert actual.returns.arg_type == 'Docstring'
    assert actual.returns.description == 'parsed docstring representation'

# Generated at 2022-06-13 19:50:22.694551
# Unit test for function parse
def test_parse():
    s = parse("This is a test string")
    assert(s.short_description == "This is a test string")

    s2 = parse("hello world")
    assert(s2.short_description == "hello world")

test_parse()


# Generated at 2022-06-13 19:50:24.605544
# Unit test for function parse
def test_parse():
    pass

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:50:29.016492
# Unit test for function parse
def test_parse():
  string = "I like this function, it is cool"
  converted = parse(string)
  assert converted == [
        ('line', 'I like this function, it is cool'),
        ('blank', ''),
  ], "Failed"

if __name__ == "__main__":
  test_parse()

# Generated at 2022-06-13 19:50:35.636022
# Unit test for function parse
def test_parse():
    """Unit test for function parse()."""
    docstring1 = parse(
        """\
        Function for adding two numbers.

        Args:
            param1 (int): The first parameter.
            param2 (int): The second parameter.

        Returns:
            int: The sum of the two parameters.

        """
    )
    assert docstring1.short_description == 'Function for adding two numbers.'
    assert docstring1.long_description == ''
    assert len(docstring1.params) == 2
    assert len(docstring1.returns) == 1
    assert len(docstring1.meta) == 1


# Generated at 2022-06-13 19:50:47.991695
# Unit test for function parse
def test_parse():
    text = '''
This is a test docstring.

:param x: A test parameter
:param y: Another test parameter
:returns: The test return value
:raises Exception: Test exception
    '''
    parsed = parse(text)
    assert parsed.short_description == 'This is a test docstring.'
    assert parsed.long_description == ''
    assert len(parsed.meta) == 4
    assert parsed.meta['param'][0].arg_name == 'x'
    assert parsed.meta['param'][0].description == 'A test parameter'
    assert parsed.meta['param'][1].arg_name == 'y'
    assert parsed.meta['param'][1].description == 'Another test parameter'
    assert parsed.meta['returns'][0].arg_name == ''
    assert parsed.meta

# Generated at 2022-06-13 19:50:48.858792
# Unit test for function parse

# Generated at 2022-06-13 19:50:57.604798
# Unit test for function parse
def test_parse():
    # Ignore unused import as pytest only used when unit tests run
    from docstring_parser.common import ParseError  # noqa
    # Ignore unused import as pytest only used when unit tests run
    from docstring_parser.styles import Style  # noqa

    assert parse("""
    """
        , Style.google
    ) == Docstring(summary='\n    ',
                    description='',
                    meta=None,
                    params=[],
                    returns=None,
                    examples=[])

    assert parse("""
    This is the first line
    This is the second line
    """, Style.google
    ) == Docstring(summary='\n    This is the first line',
                    description='\n    This is the second line',
                    meta=None,
                    params=[],
                    returns=None,
                    examples=[])


# Generated at 2022-06-13 19:51:10.441521
# Unit test for function parse
def test_parse():

    docstring = parse("""
    test function

    Parameters
    ----------
    a : str
        The first string to be compared.
    b : str
        The second string to be compared.

    Returns
    -------
    c : int
        The number of times the second string contains
        the first string.  Will be zero if the first string
        is not a substring of the second.

    Raises
    ------
    IndexError
        If the first string is not a substring of the
        second.

    Other Parameters
    ----------------
    d : str
        The optional string.

    """)
    print(docstring)
    #assert docstring.short_description == 'test function'
    assert docstring.full_description == 'The first string to be compared.'
    assert len(docstring.params) == 4


test_parse

# Generated at 2022-06-13 19:51:21.158745
# Unit test for function parse
def test_parse():
    doc1 = parse("""
    Function to test parsing

    Args:
        foo : this is foo
        bar : this is bar

    Returns:
        returns something
    """)
    doc2 = parse("""
    Function to test parsing

    :param foo: this is foo
    :param bar: this is bar
    :return: returns something
    """)
    doc3 = parse("""
    Function to test parsing

    :param foo: this is foo
    :param bar: this is bar
    :returns: returns something
    """)

    assert doc1.short_description == doc2.short_description == doc3.short_description == "Function to test parsing"