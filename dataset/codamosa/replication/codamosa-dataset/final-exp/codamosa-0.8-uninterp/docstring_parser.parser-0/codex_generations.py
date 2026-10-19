

# Generated at 2022-06-13 19:41:37.624349
# Unit test for function parse

# Generated at 2022-06-13 19:41:44.245942
# Unit test for function parse
def test_parse():
    tests = [
        ('hello', 'hello'),
        ('hello ', 'hello'),
        (' hello', 'hello'),
        (' hello ', 'hello'),
        (' hello world', 'hello world'),
        (' hello world ', 'hello world'),
    ]
    for test in tests:
        text, expected = test
        doc = parse(text, style=Style.google)
        assert doc.short_description.split("\n")[0] == expected
    # print("Unit test for function parse: Done!")

# Generated at 2022-06-13 19:41:45.241862
# Unit test for function parse
def test_parse():
    assert parse.__doc__ is not None



# Generated at 2022-06-13 19:41:51.778519
# Unit test for function parse
def test_parse():
    doc = """\
    This is a test doc.

    :param foo: swag
    :returns: turd

    :param bar: wag
    """

    d = parse(doc)
    assert d.short_description == 'This is a test doc.'
    assert d.meta['foo'].description == 'swag'
    assert d.meta['bar'].description == 'wag'
    assert d.long_description == ''
    assert d.returns.description == 'turd'

# Generated at 2022-06-13 19:41:57.137617
# Unit test for function parse
def test_parse():
    text = '''
        @param p1: meaning of param1
        @param p2: meaning of param2
        @return meaning of return
    '''
    ret = parse(text)
    assert ret.meta['param']['p1'] == 'meaning of param1'
    assert ret.meta['param']['p2'] == 'meaning of param2'
    assert ret.meta['return'] == 'meaning of return'

# Generated at 2022-06-13 19:42:06.246832
# Unit test for function parse

# Generated at 2022-06-13 19:42:13.542096
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import Google, Numpy
    text = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
            ' Praesent quis laoreet dui, vel fermentum velit.')
    assert str(parse(text)) == text

    assert isinstance(parse(text, style=Style.google), Google)

# Generated at 2022-06-13 19:42:25.869827
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    text = """Function that converts fahrenheit to celsius
    :param fahrenheit: The temperature in fahrenheit.
    :type fahrenheit: float
    :return: The temperature in celsius
    :rtype: float
    """
    docstring = parse(text)
    assert docstring.short_description == 'Function that converts fahrenheit to celsius'
    assert docstring.long_description == ''

    # test arguments
    assert len(docstring.args) == 1
    assert 'fahrenheit' in docstring.args
    assert docstring.args['fahrenheit'].type_name == 'float'
    assert docstring.args['fahrenheit'].desc == 'The temperature in fahrenheit.'
    assert docstring.args['fahrenheit'].default is None

    #

# Generated at 2022-06-13 19:42:33.864954
# Unit test for function parse
def test_parse():
    text = '''The first line is a summary of what the function does.
    The second line is blank.

    Example:

        The example is indented four spaces.

    Args:
        first_arg (int): The first argument.
        second_arg (str): The second argument.

    Returns:
        bool: The return value. True for success, False otherwise.

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.

    '''
    print(parse(text))
    assert True

# Generated at 2022-06-13 19:42:43.351230
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Meta, Blankline, Section, Param, Return
    docstring_parser.parser.parse('a') == Docstring([], Meta('a'), [])
    docstring_parser.parse.parse('a') == Docstring([], Meta('a'), [])
    docstring_parser.parse.parse('a\n\nb') == Docstring([Blankline(), Meta('b')], Meta('a'), [])
    docstring_parser.parse.parse('a\n\nb\n\n\n') == Docstring([Blankline(), Meta('b'), Blankline()], Meta('a'), [])
    docstring_parser.parse.parse('a\n\nb\nc') == Docstring([Meta('c'), Blankline(), Meta('b')], Meta('a'), [])
    docstring_parser.parse.parse

# Generated at 2022-06-13 19:42:49.998526
# Unit test for function parse
def test_parse():
    text="""This is the docstring text."""
    style = Style.auto
    assert parse(text, style).body == text

# Generated at 2022-06-13 19:42:53.015194
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleStyle
    text = 'Testing parse'
    doc = parse(text)
    assert(isinstance(doc, Docstring))
    assert(str(doc) == text)

# Generated at 2022-06-13 19:42:57.682713
# Unit test for function parse
def test_parse():
    text = '''
    Parameter:
        text: Raw input text.
        style: Style, one of (google, numpy, reStructuredText, auto)
    Returns:
        a docstring instance
    '''

    ret = parse(text)
    print(ret)

test_parse()

# Generated at 2022-06-13 19:43:03.054837
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import Google
    test_parse = parse(text = ":param arg1: param1\nparam desc\n:type arg2: int\n:rtype: int", style = Style.google)
    assert isinstance(object = test_parse, classinfo = Docstring) == True
    assert test_parse.short_description == None
    assert test_parse.long_description == None
    assert test_parse.meta['arg1'] == "param1\nparam desc"
    assert test_parse.meta['arg2'] == "int"
    assert test_parse.meta['rtype'] == "int"
    assert test_parse.meta['return'] == None
    assert test_parse.meta['returns'] == None

# Generated at 2022-06-13 19:43:14.202437
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    # test style auto
    assert(str(parse('Test')) == "Docstring([('', ['Test'])])")
    assert(str(parse('    Test')) == "Docstring([('', ['Test'])])")
    assert(str(parse('Test\nTest')) == "Docstring([('', ['Test', 'Test'])])")
    assert(str(parse('    Test\n    Test')) ==
           "Docstring([('', ['Test', 'Test'])])")
    assert(str(parse('Test\n\nTest')) == "Docstring([('', ['Test', 'Test'])])")
    assert(str(parse('    Test\n\n    Test')) ==
           "Docstring([('', ['Test', 'Test'])])")

    # test

# Generated at 2022-06-13 19:43:25.709682
# Unit test for function parse
def test_parse():
    text = '''\
        Summary line.
        Extended description.

        :param foo: Description of `foo`.
        :type foo: int
        :param bar: Description of `bar`.
        :type bar: str
        :returns: Description of return value.
        :rtype: bool

        .. rubric:: Rubric
        .. [#] Footnote reference

        .. [#] Footnote
        '''
    expected = Docstring(summary="Summary line.",
                         description="Extended description.",
                         params=[
                             ("foo", "Description of `foo`.", "int", None),
                             ("bar", "Description of `bar`.", "str", None),
                         ],
                         returns=("Description of return value.", "bool"),
                         rubric=["Rubric"],
                         footnotes=['Footnote', 'Footnote'])
    actual

# Generated at 2022-06-13 19:43:39.657977
# Unit test for function parse
def test_parse():
    text = '''"""
    This is a multiline docstring.
    This is the first line.

    This is the second line.
    """'''
    docstring = parse(text)
    assert docstring.short_description == 'This is a multiline docstring.'
    assert docstring.long_description == 'This is the first line.\n\nThis is the second line.'
    assert docstring.meta == 'This is the second line.'
    text = '''
    This is a multiline docstring.
    This is the first line.

    This is the second line.
    '''
    docstring = parse(text)
    assert docstring.short_description == 'This is a multiline docstring.'

# Generated at 2022-06-13 19:43:47.100460
# Unit test for function parse
def test_parse():
    text = '''The quick brown

Summary line.

Description:

The first paragraph.

The second paragraph.

:param str a: the first param
:param str b: the second param
:param str c: the third param
:raises ValueError: if something bad happens
'''

    docstring = parse(text)

    assert 'The quick brown' == docstring.summary
    assert 'The first paragraph.\n\nThe second paragraph.' == docstring.description
    assert {'a', 'b', 'c'} == set(docstring.params.keys())
    assert 'the first param' == docstring.params['a'].description
    assert 'the second param' == docstring.params['b'].description
    assert 'the third param' == docstring.params['c'].description
    assert 'ValueError'

# Generated at 2022-06-13 19:43:57.726021
# Unit test for function parse
def test_parse():
    text = """Basic Return."""
    assert parse(text)
    text = """
        Parameters
        ----------
            name : str, Required.
                Description.
            age : int, Optional, default 18.
                Description.
        Returns
        -------
        int
            Description.
        """
    d = parse(text)
    assert len(d.meta) == 3
    meta, _, meta2 = d.meta
    assert meta.name == "name" and meta.type == "str" and meta.kind == "Required"
    assert meta.description == "Description."
    assert meta2.name == "age" and meta2.type == "int" and meta2.kind == "Optional"
    assert meta2.options == "default 18."
    meta3, *_ = d.meta2

# Generated at 2022-06-13 19:44:03.101192
# Unit test for function parse
def test_parse():
    # Check parse function when style is defined
    docstr = parse(text="Test docstring", style=Style.google)
    assert type(docstr).__name__ == "GoogleDocstring"

    # Check parse function when style is auto
    docstr = parse(text="Test docstring")
    assert type(docstr).__name__ == "NumpyDocstring"

# Generated at 2022-06-13 19:44:14.183892
# Unit test for function parse
def test_parse():
    """
    Testing function parse
    :return:
    """

# Generated at 2022-06-13 19:44:24.298197
# Unit test for function parse
def test_parse():
    text = "the first line\n\nThis is a method to do the job. The method is\n" \
           "very difficult to implement."
    D = parse(text, style=Style.google)
    assert D.short_description == "the first line"
    assert D.long_description == ("This is a method to do the job. The method is "
                                  "very difficult to implement.")
    assert D.meta["parameters"][0].description == "the first line\n"
    assert D.meta["parameters"][1].description == "This is a method to do the job. The method is"

# Generated at 2022-06-13 19:44:33.800330
# Unit test for function parse
def test_parse():
    import sys
    import os
    sys.path.append(os.getcwd())
    from docstring_parser.common import Meta, Return

    __doc__ = """
        An example docstring
        -------------------

            hello there

        Args:
            a (int): first number
            b (int): second number
            c (int, optional): third number

        Returns:
            int: the sum of a, b, c
    """

    ret: Docstring = parse(__doc__)

# Generated at 2022-06-13 19:44:44.262961
# Unit test for function parse
def test_parse():
    docstring = """
    This is a short description.

    This is a long description.

    Args:
        arg1 (str): The first argument.
        arg2 (Optional[str]): The second argument. Defaults to None.
            This argument has a long description too, which should
            be indented properly.

    Returns:
        bool: The return value. True for success, False otherwise.

    Raises:
        AttributeError: The ``AttributeError`` exception.
    """
    # style: noqa
    result = parse(docstring)
    assert result.short_description == "This is a short description."
    assert result.long_description == "This is a long description."
    assert len(result.args) == 2
    assert result.args[0].arg_name == "arg1"

# Generated at 2022-06-13 19:44:47.657963
# Unit test for function parse
def test_parse():
    from pprint import pprint
    from docstring_parser.styles import Style
    docstring = """\
    :param float a:
    :param str b:
    """

    assert docstring.strip() == str(parse(docstring,style=Style.numpy))
    #pprint(docstring)


# Generated at 2022-06-13 19:44:53.907230
# Unit test for function parse
def test_parse():
    text = """\
A first-level header
====================

A second-level header
---------------------

Now is the time for all good men to come to
the aid of their country. This is just a
regular paragraph.

The quick brown fox jumped over the lazy
dog's back.
"""
    doc = parse(text)
    assert doc.full_name == 'A first-level header'
    assert doc.short_description == 'A second-level header'

    text = 'A docstring with no body'
    doc = parse(text)
    assert doc.short_description == text

# Generated at 2022-06-13 19:45:00.264486
# Unit test for function parse
def test_parse():
    assert parse("A docstring") == parse("A docstring", style=Style.rest)
    assert parse("A docstring") == parse("A docstring", style=Style.numpy)
    assert parse("A docstring") == parse("A docstring", style=Style.google)
    assert parse("A docstring") == parse("A docstring", style=Style.auto)
    assert parse("A docstring", style=Style.auto) == Docstring(
        short_description="A docstring", long_description="",
        return_type=None, return_description=None, args=[],
        kwargs=[], meta={})

# Generated at 2022-06-13 19:45:04.157917
# Unit test for function parse
def test_parse():
    """Test case"""
    assert parse('hello world') == Docstring(
        content="hello world",
        meta={},
        params=[],
        sections=[],
        returns=None,
        style="google",
        title=""
    )


# Generated at 2022-06-13 19:45:14.773909
# Unit test for function parse
def test_parse():
    from docstring_parser.parse import parse
    from docstring_parser.styles import Style, Google, Numpy

    docstring = """This function does something.

    Parameters
    ----------
    param1 : str
        The first parameter.
    param2 : int, optional
        The second parameter.

    Returns
    -------
    str
        The return value.

    """

    parsed = parse(docstring)
    google_parsed = parse(docstring, Style.google)
    numpy_parsed = parse(docstring, Style.numpy)

    assert parsed == google_parsed
    assert parsed == numpy_parsed
    assert parsed.short_description == "This function does something."
    assert len(parsed.params) == 2
    assert parsed.returns.description == "The return value."
   

# Generated at 2022-06-13 19:45:23.669641
# Unit test for function parse
def test_parse():

    text = '''\
@todo: this is a todo
This is a summary.

    >>> import spam
    42

This is the extended summary.

This is the first paragraph of the body.
Another line of the body.

This is the second paragraph of the body.

Args:
    param1(int): the first parameter
    param2(str): the second parameter
        with more explanation
        and spans multiple lines

Returns:
    str: description
'''

    r = parse(text)
    assert r.summary == 'This is a summary.'
    assert r.description == '\nThis is the extended summary.\n\nThis is the first paragraph of the body.\nAnother line of the body.\n\nThis is the second paragraph of the body.\n'

# Generated at 2022-06-13 19:45:32.534613
# Unit test for function parse
def test_parse():
    assert(parse('''
        @type var_a: str
        @type var_b: int
        @type var_c: str
        @type var_d: list
        @param var_a: param
        @param var_b: param
        @param var_c: param
        @param var_d: param
        @return: return
        @return: return
        ''') == Docstring(
        params = {
            "var_a" : "str"
        },
        returns = {
            "var_b" : "int"
        })
    )

test_parse()

# Generated at 2022-06-13 19:45:43.425733
# Unit test for function parse
def test_parse():
    string = (
            'Arguments:\n'
            '  arg1 (int): the first argument.\n'
            '  arg2 (str): the second argument.\n'
            'Returns:\n'
            '  str: the return value.\n'
    )
    docstring = parse(string)
    assert docstring.short_description == ""
    assert docstring.long_description == ""
    assert docstring.tags == {'arguments': [
        {'name': 'arg1', 'type': 'int', 'description': 'the first argument.'},
        {'name': 'arg2', 'type': 'str', 'description': 'the second argument.'}
        ], 'returns': {'type': 'str', 'description': 'the return value.'}}

# Generated at 2022-06-13 19:45:45.865126
# Unit test for function parse
def test_parse():
    text = """
This is a very short docstring.

:Parameters:
    **arg1**: first argument of the function
    **arg2**: second argument of the function
    **arg3**: third argument of the function
:Returns:
    **ret1**: first return value

"""
    assert parse(text, style=Style.google) == parse(text, style=Style.auto)

## Unit test for function parse_google

# Generated at 2022-06-13 19:45:47.980559
# Unit test for function parse
def test_parse():
    assert parse('''

Returns: a
''', Style.numpy) is None
if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:45:54.606458
# Unit test for function parse
def test_parse():
    """Test parse()"""
    text = """
    test_parse()
    Test parse()

    Args:
        foo: The foo argument

    Returns:
        None
    """
    ds = parse(text, style=Style.google)
    print(ds.__dict__)
    assert(str(ds) == text)
    print("test parse: OK")

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:46:05.795919
# Unit test for function parse
def test_parse():
    assert parse(
        '''
    This is a docstring
    '''
    ) == Docstring(content='This is a docstring\n', meta=[])

# Generated at 2022-06-13 19:46:16.218443
# Unit test for function parse

# Generated at 2022-06-13 19:46:26.633526
# Unit test for function parse
def test_parse():
    doc = parse("""
    This is a sample docstring.

    :param param1: this is a first param
    :param param2: this is a second param
    :returns: this is a return
    :raises keyError: raises an exception
    """)
    assert len(doc.meta) == 4
    assert doc.short_description == "This is a sample docstring."
    assert doc.long_description == None
    assert doc.returns.type_name == "this is a return"
    assert doc.params[0].arg_name == "param1"
    assert doc.params[0].description == "this is a first param"


# Generated at 2022-06-13 19:46:37.255308
# Unit test for function parse
def test_parse():
    text = """\
A test docstring.

:param arg: arg description
:type arg: str
"""
    docstring = parse(text)
    assert docstring.short_description == "A test docstring."
    assert docstring.long_description == ""
    assert docstring.meta["arg"]["type"] == "str"
    assert docstring.meta["arg"]["desc"] == "arg description"
    assert docstring.examples == ""
    assert docstring.returns == ""


text = """\
Short desc

Long desc

Meta:
:param arg: arg desc
:type arg: str

Extra:
:source: foo.py

Examples:
>>> foo(arg)
bar

Returns:
str
"""

docstring = parse(text)

print("Short description:")


# Generated at 2022-06-13 19:46:41.621044
# Unit test for function parse
def test_parse():
    from docstring_parser.tests.common import read_data

    expected = read_data('expected/numpy.txt')
    docstring = parse(read_data('data/numpy.txt'))
    assert docstring.to_dict() == expected

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:46:57.079382
# Unit test for function parse
def test_parse():
    test_doc = '''
    This function computes the sum of two numbers.

    Parameters
    ----------
    a : int
        the first number
    b : int
        the second number

    Returns
    -------
    the sum : int
        a + b

    Examples
    --------
    >>> foo(1, 2)
    3

    >>> foo(1, '2')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    '''
    parsed_doc = parse(test_doc)
    assert parsed_doc.short_description == 'This function computes the sum of two numbers.'
    assert 'Returns' in parsed_doc.long_description
    assert parsed_doc.returns.description == 'a + b'
    assert parsed

# Generated at 2022-06-13 19:47:04.261743
# Unit test for function parse
def test_parse():
    text = """
    This is some arbitrary text
    """
    assert parse(text, style=Style.restructuredtext).summary == text
    assert parse(text, style=Style.numpy).summary == text
    assert parse(text, style=Style.google).summary == text
    assert parse(text, style=Style.auto).summary == text
    text = """Another arbitrary text"""
    assert parse(text, style=Style.restructuredtext).summary == text
    assert parse(text, style=Style.numpy).summary == text
    assert parse(text, style=Style.google).summary == text
    assert parse(text, style=Style.auto).summary == text
    text = """
    This is the summary.

    This is the extended summary.

    This is some arbitrary text
    """

# Generated at 2022-06-13 19:47:14.743421
# Unit test for function parse
def test_parse():
    import docstring_parser as dp
    import pprint
    text = '''\
    This is one paragraph.

    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.

    Returns:
        bool: The return value. True for success, False otherwise.

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.

    Warns:
        UserWarning: This is a warning.
        DeprecationWarning: This is a warning.
    '''
    ret = dp.parse(text, dp.Style.google)
    print(ret)
    pprint.pprint(vars(ret))
    print('-'*80)

# Generated at 2022-06-13 19:47:22.814352
# Unit test for function parse
def test_parse():
    from pprint import pprint

    docstring = """\
    This is the docstring for the example.

    This will be a great module.

    :param apples: the number of apples
    :type apples: int
    :param bananas: the number of bananas
    :type bananas: int
    :returns: the total number of fruit
    :rtype: int
    """

    pprint(parse(docstring))


# Generated at 2022-06-13 19:47:32.378429
# Unit test for function parse
def test_parse():
    """Test parse function"""
    text = """This is a docstring.
    
    This is a docstring with multi
    line.
    
    This is a docstring with multi line.
    This is a docstring with multi line.
    ==============
    Arguments:
    some - value
    some - value
    
    Returns:
    some - value
    some - value
    
    Raises:
    exception1 - exception1
    exception2 - exception2
    """
    # TODO: This is still buggy because it is a single line file
    #       Actually it should work because there is a "\\n\\n"
    #       Therefore it should be able to parse the name and summary
    # The test passes on the CI so the problem might be that between lines
    # there is only one "\n" and not "\n\n

# Generated at 2022-06-13 19:47:44.277145
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleStyle, NumpyStyle
    text = """\
    This is a short description.

    This is a long description.

    :param a: foo
    :param b: bar
    :return: baz
    """
    parsed_style = parse(text, style=Style.auto)

    try:
        parsed_google = parse(text, style=Style.google)
    except ParseError:
        assert isinstance(parsed_style, GoogleStyle)

    try:
        parsed_numpy = parse(text, style=Style.numpy)
    except ParseError:
        assert isinstance(parsed_style, NumpyStyle)

    assert parsed_style == parsed_google or parsed_style == parsed_numpy

# Generated at 2022-06-13 19:47:56.412242
# Unit test for function parse
def test_parse():
    docstring = '''Summary line.

Extended description.

:param int arg1: the first argument
:param arg2: the second argument
:returns: description of the return value
:raises keyError: raises an exception
:var var1: description of the variable
:var var2: description of another variable
:todo: description of a todo
:bug: description of a bug
:attention: description of something dangerous
:warning: description of a warning
:note: description of a note
:see: url1, url2
:see also: url3, url4
:examples:
    >>> print(1)
    1
    >>> print(2)
    2
    >>> raise ValueError
    Traceback (most recent call last):
    ValueError
    '''
    parsed_docstring = parse(docstring)


# Generated at 2022-06-13 19:48:03.129105
# Unit test for function parse
def test_parse():
    text = """
        This is my docstring.

        It is a paragraph.

        It is another paragraph.

        This is a third paragraph.
        """
    docstring = parse(text)
    assert docstring.short_description == 'This is my docstring.'
    assert docstring.long_description == 'It is a paragraph.\n\nIt is another paragraph.\n\nThis is a third paragraph.\n'
    assert docstring.meta == {}

    text = """
        This is my docstring.

        This is my second paragraph. It contains a 
        reference [1].

        This is my last paragraph.

        [1] This is the reference.
        """

    docstring = parse(text)
    assert docstring.short_description == 'This is my docstring.'

# Generated at 2022-06-13 19:48:10.949270
# Unit test for function parse
def test_parse():
    text = '''
    Parameters
    ----------
    text : str
        Hello world
    style : Style, optional
        Python style, default to auto
    '''
    doc = parse(text)
    assert len(doc.params) == 2
    assert doc.params['text'].description == 'Hello world'
    assert 'Style' in doc.params['style'].types
    assert 'default to auto' in doc.params['style'].description
    #
    assert doc.meta['parameters'] == 2

# Generated at 2022-06-13 19:48:11.948337
# Unit test for function parse
def test_parse():
    text = '''
        """
        Dummy parser that returns empty docstring
        """
        '''
    assert parse(text).description == ''

# Generated at 2022-06-13 19:48:17.604407
# Unit test for function parse
def test_parse():
    docstring = '''
    Args:
        x: the x value of the point
    '''
    d = parse(docstring)
    assert d.meta['Args'][0].argname == 'x'
    assert d.meta['Args'][0].type_name == 'the x value of the point'


# Generated at 2022-06-13 19:48:23.654458
# Unit test for function parse
def test_parse():
    func = parse('''
        @param rst_example
        @return:
        @param: param1: blah blah @return:
        @param: none       
    ''')
    assert len(func.params) == 2, "params did not match"

# Generated at 2022-06-13 19:48:36.625994
# Unit test for function parse
def test_parse():
    assert parse("a-style snippet") == Docstring(
        summary="a-style snippet",
        description=None,
        args=None,
        returns=None,
        example=None,
        meta={},
    )

    assert parse("a-style snippet\n\nA summary") == Docstring(
        summary="A summary",
        description="a-style snippet",
        args=None,
        returns=None,
        example=None,
        meta={},
    )

    assert parse("a-style snippet\n\nA summary\n\nKey: value\n") == Docstring(
        summary="A summary",
        description="a-style snippet",
        args=None,
        returns=None,
        example=None,
        meta={"Key": "value"},
    )


# Generated at 2022-06-13 19:48:46.477426
# Unit test for function parse
def test_parse():
    """
    Function test_parse() is used to test the functionality callded when the function parse() is called.
    """
    from docstring_parser.common import Docstring
    from docstring_parser.styles import STYLES, Style

    def parse(text: str, style: Style = Style.auto) -> Docstring:
        """Parse the docstring into its components.

        :param text: docstring text to parse
        :param style: docstring style
        :returns: parsed docstring representation
        """

        if style != Style.auto:
            return STYLES[style](text)
        rets = []
        for parse_ in STYLES.values():
            try:
                rets.append(parse_(text))
            except ParseError as e:
                exc = e
        if not rets:
            raise

# Generated at 2022-06-13 19:48:57.557140
# Unit test for function parse
def test_parse():
    text = """This is a description.
    This is a description.

    :param int a: parameter a
    :param bool b: parameter b
    :returns: nothing
    :raises ValueError: if something bad happens
    """
    assert parse(text).short_desc == "This is a description."
    assert parse(text).long_desc == "This is a description."
    assert parse(text).meta["parameters"]["a"].description == "parameter a"
    assert parse(text).meta["parameters"]["b"].description == "parameter b"
    assert parse(text).meta["returns"].description == "nothing"
    assert parse(text).meta["raises"]["ValueError"].description == "if something bad happens"
    assert parse(text).style == Style.numpy

# Generated at 2022-06-13 19:49:07.472453
# Unit test for function parse
def test_parse():
    import python_docstring_parser as docstring_parser

    docstring = """
        A multi-line docstring.

        :param a: parameter a
        :param b: parameter b
        :returns: something
        :raises Exception: optional
    """

    parsed = docstring_parser.parse(docstring)['Returns'][0]
    assert parsed['type'] == 'something'

    docstring = """
        :type name: str
        :param name: The name to use.

        :type state: bool
        :param state: Current state to be in.

        :raises: AttributeError, KeyError
    """

    parsed = docstring_parser.parse(docstring)
    assert parsed['Parameters'][1]['name'] == 'state'

# Generated at 2022-06-13 19:49:17.556089
# Unit test for function parse
def test_parse():
    doc_string = """
    This is a docstring.
    If a function has a docstring, then the function can be called with ?
    ipython will show the docstring
    """
    doc = parse(doc_string)
    assert doc.short_description == "This is a docstring."
    assert doc.long_description == "If a function has a docstring, then the function can be called with ?\nipython will show the docstring"
    assert doc.signature is None
    assert doc.returns is None
    assert doc.raises is None
    assert doc.yields is None
    assert doc.meta == {}


# Generated at 2022-06-13 19:49:20.860387
# Unit test for function parse
def test_parse():
    assert parse("""This is a docstring
    
    Arguments:
        a (int): test
        b (int): test
    Returns:
        int: test
    """).returns == "int: test"



# Generated at 2022-06-13 19:49:23.536268
# Unit test for function parse
def test_parse():
    text = '''
    Testing the parse function.
    '''
    s = parse(text)
    assert s.short_description == 'Testing the parse function.'

# Generated at 2022-06-13 19:49:31.050682
# Unit test for function parse
def test_parse():
    docstring = '''
    Square root of x.

    :param x: int
    :returns: int
    '''
    doc_parse = parse(docstring)
    print(doc_parse)
    print(doc_parse.params)
    assert doc_parse.short_description == "Square root of x."
    assert doc_parse.long_description == ''
    assert doc_parse.returns.type_name == 'int'
    assert doc_parse.returns.description == ''

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:49:42.631930
# Unit test for function parse
def test_parse():
    text = '''Spam.
    :param eggs: a parameter
    :param ham: another parameter
    '''
    docstring = parse(text)
    #print(docstring)  #class style

    text = '''Spam.
    Parameters
    ----------
    eggs : int
        a parameter
    ham : str, optional
        another parameter
    '''
    d = parse(text)
    print(d) #class style

    text = '''Spam.
    :param eggs: a parameter
    :param ham: another parameter
    '''
    d = parse(text, style='numpydoc')
    print(d) #class style
    print(d.summary) #Spam.
    print(d.sections) #[Parameter(args=['eggs'], description='a parameter'), Parameter(args

# Generated at 2022-06-13 19:49:56.190984
# Unit test for function parse
def test_parse():

    """
    Test the parse method.
    """

    text = """
        This is a test docstring

        :args a: description of a
        :args b: description of b
        :returns: description of c
        :raises e: description of e
        """
    docstring = parse(text)
    print(docstring)
    assert isinstance(docstring.summary, str)
    assert isinstance(docstring.extended, str)
    assert isinstance(docstring.meta, list)
    assert isinstance(docstring.meta[0], Docstring)
    assert isinstance(docstring.meta[1], Docstring)
    assert isinstance(docstring.meta[2], Docstring)
    assert isinstance(docstring.meta[3], Docstring)


# Generated at 2022-06-13 19:50:00.915284
# Unit test for function parse
def test_parse():

    text = '''
Test function to check the parse function 
for the basic reST format

    :param int arg1: The first parameter.
    :param str arg2: The second parameter.
    :returns:  str
    :raises keyError: raises an exception
    '''
    print(parse(text))

# Generated at 2022-06-13 19:50:10.205785
# Unit test for function parse
def test_parse():
    """unit test for function parse"""
    print(parse.__doc__)
    print(parse.__name__)
    docstring = """Summary line.

    Extended description.

    Args:
        arg1 (int): Description of `arg1`
        arg2 (str): Description of `arg2`
    Returns:
        bool: Description of return value

    """
    docstring_parsed = parse(docstring, style=Style.google)
    print(docstring_parsed)
    print(docstring_parsed.meta)
    print(docstring_parsed.short_description)
    print(docstring_parsed.long_description)
    for k, v in docstring_parsed.params.items():
        print(k, v)

# Generated at 2022-06-13 19:50:13.950713
# Unit test for function parse
def test_parse():
    assert parse.__doc__ == """Parse the docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """


# Generated at 2022-06-13 19:50:26.658298
# Unit test for function parse

# Generated at 2022-06-13 19:50:32.508469
# Unit test for function parse
def test_parse():
  if __name__ == '__main__':
    parser = ArgumentParser(
        description='Mock unit test for function parse of docstring_parser.py file')
    parser.add_argument('text', nargs='?', default='""', help='docstring text to parse')
    parser.add_argument('--style', choices=['Google', 'Numpy', 'Auto'], default='Auto', help='docstring style')
    args = parser.parse_args()
    print(parse(args.text, args.style))



# Generated at 2022-06-13 19:50:44.830447
# Unit test for function parse
def test_parse():
    text = '''
    function_name(arg1=None, arg2=None)
    
    One line summary.

    This function does awesome things.
    It can be really really long.

    Parameters
    ----------
    arg1 : str
        Description of arg1.
    arg2 : int
        Description of arg2.

    Returns
    -------
    res : bool
        What the function should return.
    '''
    
    assert parse(text).meta['function_name'] == 'function_name'
    
test_parse()


# %% [markdown]
# ## Function parse_docstring_parts
# %% [markdown]
# ![](function_parse_docstring_parts.png)

# %%
# function parse_docstring_parts

# Generated at 2022-06-13 19:50:54.971862
# Unit test for function parse
def test_parse():
    """Test for the parse function"""

    class Foo(object):

        """
        Basic method.

        :param bar: Test parameter.
        :type bar: int
        :returns: None
        :raises Exception: Because it can.
        """

        def __init__(self, bar=None):
            self.bar = bar


    doc = parse(Foo.__doc__)
    assert doc.short_description == 'Basic method.'
    assert len(doc.long_description) > 10
    assert doc.params[0].name == 'bar'
    assert doc.params[0].type == 'int'
    assert doc.returns.type == 'None'
    assert len(doc.exceptions) == 1
    assert doc.exceptions[0].type == 'Exception'


# Generated at 2022-06-13 19:51:07.616325
# Unit test for function parse
def test_parse():
    """
    Unit test for function parse
    """
    docstring = """This is a one-line docstring.

    This is a multi-line docstring.

    Parameters
    ----------
    arg1 : int
        The first argument.
    arg2 : str
        The second argument.

    Examples
    --------
    >>> example
    """
    parsed_docstring = parse(docstring)
    assert parsed_docstring.summary == 'This is a one-line docstring.\n'
    assert parsed_docstring.description == 'This is a multi-line docstring.\n'
    assert parsed_docstring.meta['parameters'][0].name == 'arg1'
    assert parsed_docstring.meta['parameters'][0].arg_type == 'int'

# Generated at 2022-06-13 19:51:18.994495
# Unit test for function parse
def test_parse():
    ds = """
    Args:
        arg1 (str): the first argument.
        arg2 (str): the second argument.

    Returns:
        str: the return value.
    """
    args = parse(ds).args
    assert args[0].type_name == 'str'
    assert args[0].description == 'the first argument.'
    assert args[0].name == 'arg1'

    assert args[1].type_name == 'str'
    assert args[1].description == 'the second argument.'
    assert args[1].name == 'arg2'

    ret = parse(ds).returns
    assert ret.type_name == 'str'
    assert ret.description == 'the return value.'

