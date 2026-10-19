

# Generated at 2022-06-13 19:41:32.538705
# Unit test for function parse
def test_parse():
    docstring = parse("""
The color of a shape.

Example
-------
>>> print(circle.color)
green
""")

    assert docstring.short_description == "The color of a shape."
    assert docstring.long_description == ""
    assert docstring.sections == [
        ("Example", """\
>>> print(circle.color)
green\
""")
    ]
    assert docstring.meta == {}
    assert docstring.style == Style.google

# Generated at 2022-06-13 19:41:39.792125
# Unit test for function parse
def test_parse():
    text = '''\
    :param dist: The distribution as a :class:`pkg_resources.Distribution` object
    :type dist: :class:`pkg_resources.Distribution`
    :param attrs: The metadata attributes to set (optional)
    :type attrs: dict
    :param precedence: Precedence to search for ``.pth`` files
    :type precedence: :class:`pkg_resources.EGG_DIST` or :class:`pkg_resources.DEVELOP_DIST`
    :return: A :class:`pkg_resources.Distribution` object
    :rtype: :class:`pkg_resources.Distribution`
    '''

    docstring = parse(text, style='google')
    assert docstring.params[0].name == 'dist'

# Generated at 2022-06-13 19:41:51.005388
# Unit test for function parse
def test_parse():
    def test_parse_int():
        doc = """
        title:
            int hello
        """
        d = parse(doc)
        assert d.title == "title"
        assert d.parameters[0].name == "hello"
        assert d.parameters[0].type == "int"

    def test_parse_float():
        doc = """
        title:
            float hello
        """
        d = parse(doc)
        assert d.title == "title"
        assert d.parameters[0].name == "hello"
        assert d.parameters[0].type == "float"

    def test_parse_bool():
        doc = """
        title:
            bool hello
        """
        d = parse(doc)
        assert d.title == "title"
        assert d.parameters[0].name

# Generated at 2022-06-13 19:42:01.312990
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Docstring
    from docstring_parser.styles import Style
    ds = parse('', style=Style.numpy)
    assert ds.short_description.description == ''
    assert ds.short_description.indent == 0
    assert ds.short_description.line_number == 1
    assert ds.short_description.start_col_number == 1
    assert ds.summary_description.description == ''
    assert ds.extended_description.description == ''
    assert ds.extended_description.indent == 0
    assert ds.extended_description.line_number == 1
    assert ds.extended_description.start_col_number == 1
    assert ds.meta == {}
    assert ds.content == ''


# Generated at 2022-06-13 19:42:05.215402
# Unit test for function parse
def test_parse():
    """Test the parse function."""
    text = '''\
        test docstring
        with multi-line.
        '''
    docstring = parse(text)
    assert docstring.summary == 'test docstring\nwith multi-line.'
    assert docstring.style is not None

# Generated at 2022-06-13 19:42:12.707063
# Unit test for function parse
def test_parse():
    from docstring_parser.docstring import Docstring
    text = '''\
        This function parse a docstring into several parts.

        Args:
            text:  text to parse
            style: docstring style

        Returns:
            parsed docstring representation
        '''
    parsed = parse(text)

    assert isinstance(parsed, Docstring)
    assert parsed.short_description == 'This function parse a docstring into several parts.'
    assert parsed.long_description == ''
    assert parsed.returns.type_name == 'parsed docstring representation'
    assert parsed.returns.description == ''
    assert parsed.style == Style.google


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:42:23.862868
# Unit test for function parse
def test_parse():
    docstring = """one line summary

One line summary continuing here.

:param name: parameter name
:type name: str
:returns: something
:rtype: str
:raises: ValueError
:Example:
    >>> parse("Hello World!")
    Hello World!
"""
    assert parse(docstring) == Docstring("""one line summary

One line summary continuing here.

:param name: parameter name
:type name: str
:returns: something
:rtype: str
:raises: ValueError
:Example:
    >>> parse("Hello World!")
    Hello World!
""")

# Generated at 2022-06-13 19:42:34.101641
# Unit test for function parse
def test_parse():
    text = """Parses the docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    assert(parse(text).short_description == 'Parses the docstring into its components.')
    assert(parse(text).sections[0].args[0].arg_name == 'text')
    assert(parse(text).sections[0].args[0].arg_type == 'str')
    assert(parse(text).sections[0].args[0].description == 'docstring text to parse')
    assert(parse(text).sections[0].args[1].arg_name == 'style')
    assert(parse(text).sections[0].args[1].arg_type == 'Style')

# Generated at 2022-06-13 19:42:36.765575
# Unit test for function parse
def test_parse():
    assert parse('hello world') == parse('hello world', style=Style.numpy)
    assert parse('hello world', style=Style.google) == parse('hello world', style=Style.google)

test_parse()

# Generated at 2022-06-13 19:42:44.129044
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Docstring
    docstring = Docstring.parse("""
    f(a, b, c=3)

    Lorem ipsum...
    """)
    assert(docstring.short_description == 'f(a, b, c=3)')
    assert(docstring.long_description.strip() == 'Lorem ipsum...')
    assert(docstring.params == {'a': '', 'b': '', 'c': '3'})
    assert(docstring.returns == '')

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:42:57.638964
# Unit test for function parse
def test_parse():
    text = '''\
    Generate a sample of points from the mixture of Gaussians.
    The model has to be initialized first with `init_gauss`.
    :param num: Number of points to generate
    :returns: Array of points
    '''

    func = parse
    res = func(text)
    assert res is not None
    assert res.meta.title == 'Generate a sample of points from the mixture of Gaussians.'
    assert res.meta.params[0].name == 'num'
    assert res.meta.params[0].args == ''
    assert res.meta.params[0].desc == "Number of points to generate"
    assert res.meta.returns == "Array of points"


# Generated at 2022-06-13 19:43:02.220465
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    parse(
        """
        Here is a test docstring,
        with known fields.

        :param param1: A first test parameter
        :type param1: str, optional
        :param param2: A second test parameter
        :type param2: bool, optional
        :returns: A test return type, of type `str`
        :rtype: str
        """
    )


# Generated at 2022-06-13 19:43:13.765511
# Unit test for function parse
def test_parse():
    import docstring_parser.rst as rst_parser
    import docstring_parser.google as google_parser
    import docstring_parser.sphinx as sphinx_parser

    text = "short description\n\nlong description\n\n:param arg1: description\n:type arg1:  int\n:returns: description\n:rtype: str"
    docstring = rst_parser.parse(text)
    assert rst_parser.parse(text) == docstring
    assert google_parser.parse(text) == docstring
    assert sphinx_parser.parse(text) == docstring

    text = "short description\n\nlong description\n\nArgs:\n\targ1 (int): description\n\nReturns:\n\tdescription (str)"
    docstring = google_parser

# Generated at 2022-06-13 19:43:20.878058
# Unit test for function parse
def test_parse():
    assert parse("\n\nstring\n\n", Style.numpy)
    assert parse("\n\nstring\n\n", Style.numpy)
    assert parse("\n\nstring\n\n", Style.numpy)
    assert parse("\n\nstring\n\n", Style.numpy)
    assert parse("\n\nstring\n\n", Style.numpy)
    assert parse("\n\nstring\n\n", Style.numpy)
    assert parse("\n\nstring\n\n", Style.numpy)
    assert parse("\n\nstring\n\n", Style.numpy)
    assert parse("\n\nstring\n\n", Style.numpy)
    assert parse("\n\nstring\n\n", Style.numpy)

# Generated at 2022-06-13 19:43:30.783482
# Unit test for function parse
def test_parse():
    docstring = """Summary line.

Extended description of function.

Parameters:
    param1: Description of `param1`
    param2: Description of `param2`

"""
    expected = Docstring(
        summary='Summary line.',
        description=['Extended description of function.'],
        params={
            'param1': 'Description of `param1`',
            'param2': 'Description of `param2`'
        },
        meta={
            'param1': [],
            'param2': []
        }
    )
    assert parse(docstring) == expected

    docstring = """Summary line.

Extended description of function.

Args:
    param1: Description of `param1`
    param2: Description of `param2`

"""

# Generated at 2022-06-13 19:43:41.451565
# Unit test for function parse
def test_parse():

    docstring = parse("""
    This is docstring for funtion parse
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """)

    assert docstring.short_description == 'This is docstring for funtion parse'
    assert docstring.long_description == ''
    assert len(docstring.params) == 2
    assert docstring.params[0].arg_name == 'text'
    assert docstring.params[0].description == 'docstring text to parse'
    assert len(docstring.returns) == 1
    assert docstring.returns[0].type_name == 'None'
    assert docstring.returns[0].description == 'parsed docstring representation'


# Generated at 2022-06-13 19:43:43.698498
# Unit test for function parse
def test_parse():
    doc = """Summary line.

Extended description.
    """
    docstring = parse(doc, Style.numpy)
    docstring.summary
    docstring.extended_summary


# Generated at 2022-06-13 19:43:46.944203
# Unit test for function parse
def test_parse():
    ds = '''Some description

    :param int bar: bar comment
    '''
    parse(ds, Style.google)
    parse(ds, Style.google).parameters
test_parse()

# Generated at 2022-06-13 19:43:54.175975
# Unit test for function parse
def test_parse():
    # Test parse function of docstring_parser
    doc_text = '''Test for function parse
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation'''
    doc_obj = parse(doc_text)
    assert (doc_obj.params[0][0]=='text')
    assert (doc_obj.params[1][0]=='style')
    assert (doc_obj.returns.strip()== 'parsed docstring representation')


# Generated at 2022-06-13 19:44:02.467540
# Unit test for function parse
def test_parse():
    """Docstring for a test.

    Extra line.

    :param arg1: The first argument.
    :type arg1: str
    :param arg2: The first argument.
    :type arg2: int, optional

        The description of arg2 continues here.
        And, extends to these lines.

    :raises exception1: Because I said so.
    :raises KeyError: Because of this,
        and this continues
        and continues...

    :returns: None
    :rtype: None

    :Example:

        >>> import foo
        >>> parsed = foo.parse(__doc__)
    """

    parsed = parse(test_parse.__doc__, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.short_description == "Docstring for a test."

# Generated at 2022-06-13 19:44:11.208335
# Unit test for function parse
def test_parse():
    assert parse('Test docstring') == Docstring(summary='Test docstring')
    assert parse('Test docstring\nwith two lines') == Docstring(summary='Test docstring\nwith two lines')
    assert parse('Test docstring\n\nwith two lines and blank line') == Docstring(summary='Test docstring',
                                                                                 description='with two lines and blank line')
    assert parse('Test docstring\n\nwith two lines and blank line\nand two paragraphs') == Docstring(summary='Test docstring',
                                                                                                     description='with two lines and blank line\nand two paragraphs')

# Generated at 2022-06-13 19:44:14.287628
# Unit test for function parse
def test_parse():
    parse("""\
        summ

        long  summ

        :param a: param a
        :type a: int
        :raises Exception: raises Exception
        :returns: None
        :rtype: NoneType
    """)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:44:27.688901
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import numpy
    from docstring_parser.styles import google
    from docstring_parser.styles import numpy
    from docstring_parser.styles import numpydoc
    from docstring_parser.styles import reStructuredText
    from docstring_parser.styles import sphinx

    def f():
        """
        My functions

        :param param: this is a parameter

        :type param: int, float, str

        :returns:
        :rtype: int
        """
        pass

    ################################
    d = parse(f.__doc__)
    print(d)
    ################################
    d = parse(f.__doc__, style=google)
    print(d)
    ################################

# Generated at 2022-06-13 19:44:31.101294
# Unit test for function parse

# Generated at 2022-06-13 19:44:40.893419
# Unit test for function parse
def test_parse():
    text = '''
    Summary line.
    
    Extended description.
    
    :param arg1: Description of arg1
    :param arg2: Description of arg2
    :returns: Description of return value
    :raises keyError: raises an exception
    '''
    docstring = parse(text)
    assert docstring.long_description == 'Extended description.'
    assert docstring.short_description == 'Summary line.'
    assert docstring.summary == 'Summary line.'
    assert docstring.extended_description == 'Extended description.'
    assert len(docstring.params) == 2
    assert docstring.params['arg1'].declaration == 'arg1'
    assert docstring.params['arg1'].arg_type is None

# Generated at 2022-06-13 19:44:45.495742
# Unit test for function parse
def test_parse():
    text = parse('''Single line docstring.

::

    Code example.
''')
    text.short_description
    text.long_description
    text.raw_docstring
    print(text.meta)
    print(text.sections)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:44:50.860813
# Unit test for function parse
def test_parse():
    docstring = """Single-line short summary

Multi-line long description

    Args:
        arg1 (str): Description of `arg1`
        arg2 (int, optional): Description of `arg2`
    Returns:
        str: Description of return value
    Raises:
        ValueError: When `arg2` is equal to zero.
    """

# Generated at 2022-06-13 19:44:58.903517
# Unit test for function parse
def test_parse():
    """
    Unit test for function ``parse``.
    """
    # Parse a multiline docstring
    text1 = """
    This is a demo docstring that only has a summary line.

    Attributes:
        a: This is a type int variable
        b: This is a type float variable
        c: This is a type str variable
    """

    # Parse a singleline docstring
    text2 = "This is a singleline docstring that only has a summary line."

    # Parse a docstring that contains parameter and return section

# Generated at 2022-06-13 19:45:03.552082
# Unit test for function parse
def test_parse():
    text = """
    This is a function with no arguments.
    
    :param arg1: this is the first argument
    :type arg1: int
    :param arg2: this is the second argument
    :type arg2: str, optional
    :return: nothing
    :rtype: None
    """

    docstring = parse(text, style=Style.google)
    assert isinstance(docstring, Docstring)
    assert docstring.short_description == 'This is a function with no arguments.'
    assert docstring.long_description == None
    assert isinstance(docstring.returns, list)
    assert isinstance(docstring.returns[0], Docstring)
    assert docstring.returns[0].type_name == 'None'
    assert len(docstring.params) == 2

# Generated at 2022-06-13 19:45:08.726490
# Unit test for function parse
def test_parse():
    """
    Test function parse
    """
    text = """
    This is a test function.

    :param x: integer
    :param y: integer
    :returns: sum of x and y
    :raises KeyError: when a key error
    """
    print(parse(text))


# Generated at 2022-06-13 19:45:18.278509
# Unit test for function parse
def test_parse():
    print(parse.__doc__)
    test_text = """
        Summary line.

        Extended description.

        :param arg1: Description of arg1
        :param arg2: Description of arg2
        :returns: Description of return value
        :raises keyError: raises an exception
        """
    print(parse(text=test_text, style="google"))
    print(parse(text=test_text, style="google"))
    print(parse(text=test_text, style="google"))

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:45:28.253420
# Unit test for function parse

# Generated at 2022-06-13 19:45:35.460809
# Unit test for function parse
def test_parse():
    docstring = """Single line summary.

    This is a multiline description. The description is separated from the summary by a empty line.

    :param str arg1: The first argument.
    :param arg2: The second argument.
    :type arg2: int
    :param arg3: The third argument
    :type arg3: int
    :raises ValidationError: If a problem occurs.
    :return: A value.
    :return: None
    :rtype: str
    """
    args = parse(docstring)
    assert args.summary == "Single line summary."
    assert args.description == "This is a multiline description. The description is separated from the summary by a empty line."

# Generated at 2022-06-13 19:45:43.769084
# Unit test for function parse
def test_parse():
    docstring = '''This is a Unit Test for function parse
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation'''

    doc = parse(docstring)

    assert doc.short_description == "This is a Unit Test for function parse"
    for param in doc.params:
        assert param.arg_name == 'text' or param.arg_name == 'style'
    assert doc.params[0].arg_name == 'text'
    assert doc.params[1].arg_name == 'style'
    assert doc.returns.description == 'parsed docstring representation'

# Generated at 2022-06-13 19:45:52.272041
# Unit test for function parse
def test_parse():
    class Test:
        """
        Test class is used to test the docstring_parser

        'param1' and 'param2' are two parameters which are strings

        'var1' and 'var2' are two variables that are tuples
        """

        def __init__():
            pass

    docstring = Test.__doc__
    docstring_parser = parse(docstring)
    assert len(docstring_parser.meta) == 4
    assert docstring_parser.summary == "Test class is used to test the docstring_parser"
    assert len(docstring_parser.description) == 1
    assert docstring_parser.return_type is None
    assert len(docstring_parser.date) == 0
    assert len(docstring_parser.params) == 2
    assert len(docstring_parser.vars) == 2

# Generated at 2022-06-13 19:46:03.748074
# Unit test for function parse
def test_parse():
    from docstring_parser import parse
    from docstring_parser.common import Docstring


# Generated at 2022-06-13 19:46:08.618159
# Unit test for function parse
def test_parse():
    test_str = """
    A test docstring

    This docstring has a long description, which can be
    multiple paragraphs.
    
    The long description can also contain subsections
    in the form of:
    
    * A bullet list
    * With a second item
    * Where the the list goes on...

    Paragraphs follow a blank line.

    :param f: a test variable
    :type f: str
    :param g: another test variable
    :type g: dict


    :returns: a string 
    :rtype: str
    """
    print(parse(test_str, style=Style.google))

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:46:12.013909
# Unit test for function parse
def test_parse():
    doc_string = " :param a: test arg \n :param b: test arg2 \n :return: test return"
    assert(parse(doc_string) != None)

# test_parse()

# Generated at 2022-06-13 19:46:16.873042
# Unit test for function parse
def test_parse():
    """Unit test for function parse."""

    from docstring_parser.common import Return

    doc = """
        Return parameters
        -----------------
        a (int):
            Description for a.
        b (float):
            Description for b.
    """
    ret = parse(doc, style=Style.numpy)
    assert ret.returns == [
        Return(type='int', description='Description for a.'),
        Return(type='float', description='Description for b.')
    ]

# Generated at 2022-06-13 19:46:28.594691
# Unit test for function parse

# Generated at 2022-06-13 19:46:40.206506
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Arg, Param, Return, Exception
    d = parse('''docstring_parser

    Utility to parse docstrings.
    
    
    Usage::
    
        >>> import docstring_parser
        >>> docstring_parser.parse(\"\"\"
        ... docstring_parser
        ... 
        ... Utility to parse docstrings.
        ... 
        ... \"\"\")
        <Docstring at 0x10e7fa320>
    
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    
    :raises ParseError: if the docstring is not in the expected format
    ''', style = Style.auto)
    assert d.summary == "Utility to parse docstrings."

# Generated at 2022-06-13 19:46:46.435452
# Unit test for function parse
def test_parse():
    from docstring_parser.parse import parse
    text = ("""
        Hello, world
        """)

    result = parse(text)
    # TODO: Check all attributes to test the right output
    print(result.description)


if __name__ == '__main__':
    test_parse()
    help(parse)

# Generated at 2022-06-13 19:46:58.600200
# Unit test for function parse
def test_parse():
    # Test case 1
    text = """
    function1
    Args:
        p1: param1
        p2: param2
    Returns:
        return1
    """
    ds = parse(text, style=Style.google)
    print(ds.parsed)
    assert ds.parsed['Return'] == 'return1'
    assert ds.parsed['Args'] == {'p1': 'param1', 'p2': 'param2'}

    # Test case 2
    text = """
    function1
    Args:
        p1: param1
        p2: param2
    """
    ds = parse(text, style=Style.google)
    print(ds.parsed)

# Generated at 2022-06-13 19:47:11.613115
# Unit test for function parse
def test_parse():
    docstr = """Summary line.

Extended description.

:param arg1: Description of `arg1`
:type arg1: Any type
:param arg2: Description of `arg2`
:type arg2: Any other type
:returns: Description of return value
:rtype: The return type
:raises Exception1: When things go wrong
:raises Exception2: When other things go wrong
"""
    result = parse(docstr)

# Generated at 2022-06-13 19:47:20.951328
# Unit test for function parse
def test_parse():
    """Unit test for parse supports all styles."""

    def _compare(text: str, style: Style, expected: dict) -> None:
        doc = parse(text, style)
        assert doc.short_description == expected["short_description"]
        assert doc.long_description == expected["long_description"]
        assert doc.raw_meta == expected["raw_meta"]
        assert list(doc.get_sections()) == expected["sections"]

    doc = """
    """
    expected = {"raw_meta": "", "short_description": "", "long_description": "", "sections": []}
    for style in Style:
        _compare(doc, style, expected)

    doc = """
    Parse docstring.
    """

# Generated at 2022-06-13 19:47:30.894125
# Unit test for function parse
def test_parse():
    text = '''What a great documentation!

:param arg1: argument 1
:type arg1: str
:arg arg2: argument 2
:type arg2: int
:key arg3: argument 3
:key type arg3: float
:keyword arg4: argument 4
:keyword type arg4: bool
:returns: return value
:rtype: float
:example:
    >>> my_func(1, 2, 3.0, False)
    3.0
'''
    d = parse(text, style=Style.numpy)
    assert d.short_description == 'What a great documentation!'
    assert d.long_description == ''


# Generated at 2022-06-13 19:47:38.650761
# Unit test for function parse
def test_parse():
    assert parse('').short_description == ''
    assert parse('short').short_description == 'short'
    assert parse('short\n').short_description == 'short'
    assert parse('short\n\n').short_description == 'short'
    assert parse('short\nlong').short_description == 'short'
    assert parse('\nshort\n\nlong').short_description == 'short'
    assert parse('\nshort\n\nlong').long_description == 'long'
    assert parse('\nshort\n\n::\n\n    code\n\nlong').long_description == 'long'
    assert parse('\nshort\n\n::\n\n    code\n\nlong').code_block == '    code'

# Generated at 2022-06-13 19:47:45.477924
# Unit test for function parse
def test_parse():
    from docstring_parser.common import ParseError
    text = """Example docstring.

:param int foo:
    An example parameter.
"""
    assert parse(text)

    text = """Example docstring.

:param foo:
    An example parameter.
"""
    try:
        parse(text)
    except ParseError as e:
        assert 'Invalid type' in e.args[0]




if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:47:56.896003
# Unit test for function parse
def test_parse():
    from docstring_parser.repr import Docstring
    from docstring_parser.styles import Style
    from docstring_parser.parser import parse
    doc = parse("""Calculate the mean value.\n
    :param x: Input
    :param y: Input
    :returns: Mean value

    Calculate the mean value.
    :param x: Input
    :param y: Input
    :returns: Mean value
    """)
    assert( isinstance( doc, Docstring) )
    assert(doc.long_description == "\nCalculate the mean value.\n\nCalculate the mean value.\n")
    assert(doc.summary == "Calculate the mean value.")
    assert(len(doc.params) == 2)
    assert(doc.params['x'].type_name == "Input")

# Generated at 2022-06-13 19:48:06.989820
# Unit test for function parse
def test_parse():
    text = '''
    This is the summary line.

    This is the first section.
    '''
    style = Style.auto
    doc = parse(text, style)
    assert doc.text.startswith('This is the summary line.')
    assert doc.sections['This is the first section'] == 'First section'

if __name__ == '__main__':
    text = '''
    This is the summary line.

    This is the first section.
    '''
    style = Style.auto
    doc = parse(text, style)
    print(doc.text)

# Generated at 2022-06-13 19:48:13.355487
# Unit test for function parse
def test_parse():
    assert parse('docstring') == Docstring(
        'docstring', summary='docstring', description='', returns=None,
        raises=None)



# Generated at 2022-06-13 19:48:21.705331
# Unit test for function parse
def test_parse():
    from docstring_parser import parse
    from docstring_parser.styles import GoogleStyle, NumpyStyle

    doc = """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.
            Defaults to ''.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: The return value. True for success, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """

   

# Generated at 2022-06-13 19:48:25.821840
# Unit test for function parse
def test_parse():
    text = """
    """
    assert parse(text) == Docstring(description='', meta_type='', meta_description='',
                                    examples='', returns='', raises='', notes='',
                                    warnings='', references='', warnings='', warnings='', warnings='')

# Generated at 2022-06-13 19:48:34.109768
# Unit test for function parse
def test_parse():
    text = """
    Docstring
    """
    docstring = parse(text)
    assert docstring.short_description == "Docstring"

    text = """
    MyFunction
    ==========

    This is my function.

    A test example::

        >>> import x
        >>> x.hello()
        Hello
    """
    docstring = parse(text)
    assert docstring.short_description == "MyFunction"
    assert docstring.long_description.strip() == "This is my function."
    assert docstring.examples[0].strip() == ">>> import x"

# Generated at 2022-06-13 19:48:37.417563
# Unit test for function parse
def test_parse():
    text = '''
    """This is a docstring"""
    '''
    docstring = parse(text)
    assert(docstring.description == 'This is a docstring')


# Generated at 2022-06-13 19:48:42.384861
# Unit test for function parse
def test_parse():
    text = """The main parsing routine.
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    result = parse(text)
    assert result.short_description
    assert result.long_description
    assert result.params
    assert result.returns

# Generated at 2022-06-13 19:48:50.139695
# Unit test for function parse
def test_parse():
    ds = """Summary line.

Extended description.

:param arg1: Description of arg1
:type arg1: str
:param arg2: Description of arg2
:type arg2: int, optional
:returns: Description of return value
:rtype: bool
:raises keyError: raises an exception
"""
    doc = parse(ds)
    assert len(doc.args) == 2
    assert doc.args[0].arg_name == 'arg1'
    assert doc.args[0].type_name == 'str'
    assert doc.args[0].description == 'Description of arg1'
    assert doc.args[1].arg_name == 'arg2'
    assert doc.args[1].type_name == 'int, optional'
    assert doc.args[1].description == 'Description of arg2'

# Generated at 2022-06-13 19:48:55.893401
# Unit test for function parse
def test_parse():
    text = '''
    Examples:
        >>> True
        True
        >>> False
        False
    '''
    d = parse(text)
    assert d.short_description == ''
    assert d.long_description == ''
    assert d.sections == [
        ('Examples', ['>>> True\nTrue\n>>> False\nFalse'])]


# Generated at 2022-06-13 19:49:05.995402
# Unit test for function parse
def test_parse():
    # Function parse
    text = """This is a short summary.

    This is a long summary...
    """
    exp = Docstring(
        summary=Docstring.Summary(
            short="This is a short summary.",
            long="This is a long summary...",
        )
    )
    assert parse(text, style=Style.google) == exp, 'Should be equal'

    # Function parse
    text = '''This is a short summary.

    This is a long summary...

    Args:
        arg1: Arg one.
        arg2: Arg two.

    Returns:
        None
    '''

# Generated at 2022-06-13 19:49:08.921838
# Unit test for function parse
def test_parse():
    docstring = """Parses a docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    assert str(parse(docstring)) == docstring

# Generated at 2022-06-13 19:49:18.289050
# Unit test for function parse
def test_parse():
    doc_str = '''
    This is a docstring.

    Arguments:
        arg1(int): description for arg1.
        arg2(int): description for arg2.
        arg3(int): description for arg3.
        arg4(int): description for arg4.

    Returns:
        int: description for returns.
    '''
    result = parse(doc_str, style=Style.numpy)
    print(result.args)

# Generated at 2022-06-13 19:49:27.728370
# Unit test for function parse
def test_parse():
    def foo():
        """This is a function foo

        :param int x: (optional) x desc
        :param str y: (optional) y desc
        :return: (optional) return desc
        :rtype: object
        """

    assert parse(foo.__doc__) == Docstring(
        content=['This is a function foo'],
        summary='This is a function foo',
        meta={
            'param int x': '(optional) x desc',
            'param str y': '(optional) y desc',
            'return': '(optional) return desc',
            'rtype': 'object',
        },
    )

# Generated at 2022-06-13 19:49:34.302649
# Unit test for function parse
def test_parse():
    assert getattr(parse, '__doc__', None) is not None

    from pprint import pprint
    from docstring_parser.styles import NumpyDocstring, GoogleDocstring

    def check(text, style, **kwargs):
        docstring = parse(text, STYLES[style])
        assert isinstance(docstring, NumpyDocstring if style == 'numpy' else GoogleDocstring)
        for k, v in kwargs.items():
            assert getattr(docstring, k) == v

    check('', 'numpy')
    check('', 'google')
    check('First line\n\nSecond line\n\n', 'numpy', summary='First line')
    check('First line\n\nSecond line\n\n', 'google', summary='First line')

# Generated at 2022-06-13 19:49:38.202250
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import google
    text='test'
    style=Style.google
    docstring=parse(text,style)
    print(docstring)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:49:52.204564
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import Style
    from docstring_parser.common import Parameter, Attribute, Return
    # Test case for Doxygen style docstring
    doxygen = parse("""This is a function. This function does something.


        Args:
            arg1: The first argument.
            arg2: The second argument.

        Returns:
            This is what is returned.

        Raises:
            KeyError: Raises an exception.
    """, style=Style.doxygen)
    assert(doxygen.summary == "This is a function. This function does something.")
    assert(doxygen.description == "")
    assert(doxygen.extended_summary == "")
    assert(doxygen.extended_description == "")

# Generated at 2022-06-13 19:49:56.667375
# Unit test for function parse
def test_parse():
    x = parse("""
        Lorem ipsum dolor sit amet consectetur
        adipisicing elit. Sint voluptatum similique,
        illo provident pariatur facere quam ab?
        """)
    print(x)


# Generated at 2022-06-13 19:50:05.631343
# Unit test for function parse
def test_parse():
    text = '''\
    :param x: The first parameter.
    :param y: The second parameter.
    :type x: float
    :type y: str
    :returns: The return value.
    :rtype: int
    '''
    f = parse(text)
    print(f)
    assert f.params[0].arg_type == 'float'
    assert f.returns.arg_type == 'int'
    assert f.params[0].description == 'The first parameter.'
    assert f.returns.description == 'The return value.'

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:50:09.386951
# Unit test for function parse
def test_parse():
    assert parse.__doc__ == "Parse the docstring into its components.\n\n    :param text: docstring text to parse\n    :param style: docstring style\n    :returns: parsed docstring representation\n    "

# Generated at 2022-06-13 19:50:14.276655
# Unit test for function parse
def test_parse():
    assert parse("Return None.\n") == parse("Return None.\n", style='numpy')
    assert parse("Return None.\n") == parse("Return None.\n", style='google')
    assert parse("Return None.\n") == parse("Return None.\n", style='epytext')
    assert parse("Return None.\n") == parse("Return None.\n", style='sphinx')
    assert parse("Return None.\n") == parse("Return None.\n", style='top')


# Generated at 2022-06-13 19:50:25.023417
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Docstring
    from docstring_parser.styles import STYLES

    # Sample docstring:
    samp = '''
    This is a sample docstring.

    :param name1: This is the first paramter.
    :param name2: This is a second parameter.
        The second line is indented.
    :returns: This is what is returned.
        The second line is indented.
    :raises keyError: We get a key error
        sometimes.
    '''
    print(parse(samp))

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:50:32.214439
# Unit test for function parse
def test_parse():
    '''
    >>> ds = "Create a new Deque object"
    >>> parse(ds)
    Docstring(summary=['Create a new Deque object'], args=[], returns=[], meta={})
    '''
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 19:50:35.219551
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring()
    assert parse("string") == Docstring("string")
    assert parse("string\n" * 3) == Docstring("string")

# Generated at 2022-06-13 19:50:47.449358
# Unit test for function parse
def test_parse():
    docstring = parse("""\
this is a test docstring

:param a: param a
:param b: param b
:return: return
""")
    assert docstring.short_description == 'this is a test docstring'
    assert docstring.long_description is None
    assert docstring.meta['a'].arg_type == 'param'
    assert docstring.meta['a'].type_name == 'a'
    assert docstring.meta['a'].description == 'param a'
    assert docstring.meta['b'].arg_type == 'param'
    assert docstring.meta['b'].type_name == 'b'
    assert docstring.meta['b'].description == 'param b'
    assert docstring.meta['return'].arg_type == 'return'

# Generated at 2022-06-13 19:50:56.839077
# Unit test for function parse
def test_parse():
    docstring = '''\
    """
    First line of summary.
    The second line.

    .. function:: function_name(arg1, arg2)

    .. autosummary::
        :nosignatures:

        :meth:`~.Docstring.field`

    :param arg1: argument #1
    :type arg1: int
    :param arg2: argument #2
    :type arg2: str
    :returns: nothing
    :rtype: None
    """'''

    ans = parse(docstring)
    ans_meta = {'arg1': {'type': 'int', 'desc': 'argument #1'},
               'arg2': {'type': 'str', 'desc': 'argument #2'},
               'returns': {'type': 'None', 'desc': 'nothing'}}

# Generated at 2022-06-13 19:50:58.128077
# Unit test for function parse

# Generated at 2022-06-13 19:51:05.704609
# Unit test for function parse
def test_parse():
    raw_text = """\
    This is Free software, see AUTHORS
    for copying information.
    """
    parsed = parse(raw_text, style=Style.auto)
    assert len(parsed.short_description) == 2
    assert parsed.short_description[0] == "This is Free software, see AUTHORS"
    assert parsed.short_description[1] == "for copying information."

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:51:13.420392
# Unit test for function parse
def test_parse():
    from .examples import GOOGLE, NUMPYDOC, EPYDOC, SPHINX
    assert parse(GOOGLE) == STYLES[Style.google](GOOGLE)
    assert parse(NUMPYDOC) == STYLES[Style.numpydoc](NUMPYDOC)
    assert parse(EPYDOC) == STYLES[Style.epytext](EPYDOC)
    assert parse(SPHINX) == STYLES[Style.sphinx](SPHINX)



# Generated at 2022-06-13 19:51:22.126397
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    def func():
        """This is a test. A simple test to verify the unit test framework.

        Parameters
        ----------
        a : float
            This is a parameter.
        b : float
            This is another one.
        """
        pass

    ds = parse(func.__doc__)
    assert ds.short_description == "This is a test."
    assert ds.long_description == "A simple test to verify the unit test framework."
    assert ds.params[0].arg_name == 'a'
    assert ds.params[1].arg_name == 'b'

test_parse()