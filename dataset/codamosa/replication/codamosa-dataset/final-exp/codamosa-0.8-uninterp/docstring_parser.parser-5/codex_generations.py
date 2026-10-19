

# Generated at 2022-06-13 19:41:38.176032
# Unit test for function parse
def test_parse():
    assert parse(text="""
    :param x: (Optional)
    """) == Docstring(
        meta={'param': [{'name': 'x', 'type': '', 'value': '(Optional)', 'desc': ''}]},
        params=[{'name': 'x', 'type': '', 'value': '(Optional)', 'desc': ''}],
    )
    assert parse(text="""
    :param x: (Optional)
    :type x: int
    """) == Docstring(
        meta={'param': [{'name': 'x', 'type': 'int', 'value': '(Optional)', 'desc': ''}]},
        params=[{'name': 'x', 'type': 'int', 'value': '(Optional)', 'desc': ''}],
    )


# Generated at 2022-06-13 19:41:48.898952
# Unit test for function parse
def test_parse():
    assert parse('').short_description == ''
    assert parse(
        'Short summary.',
    ).short_description == 'Short summary.'
    assert parse(
        'Short summary.\n'
        '\n'
        'Long description.',
    ).short_description == 'Short summary.'
    assert parse(
        'Short summary.\n'
        '\n'
        'Long description.',
    ).long_description == 'Long description.'
    assert parse(
        'Short summary.\n'
        '\n'
        '  First paragraph of long description.\n'
        '\n'
        '  Second paragraph of long description.',
    ).long_description == (
        'First paragraph of long description.\n\n'
        'Second paragraph of long description.'
    )

# Generated at 2022-06-13 19:41:55.637424
# Unit test for function parse
def test_parse():
    docstr = """This is a function that takes any number of arguments and returns their average.

Args:
    *args: Numerical arguments to be averaged.

Returns:
    The average value of given arguments.
"""
    parse_ = parse(docstr)

    assert parse_.summary == "This is a function that takes any number of arguments and returns their average."
    assert parse_.description == ""
    assert parse_.style == "google"
    assert parse_.params["*args"].name == "*args"
    assert parse_.params["*args"].description == "Numerical arguments to be averaged."
    assert parse_.returns["returns"].description == "The average value of given arguments."


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:42:05.200909
# Unit test for function parse
def test_parse():
    '''Test function parse'''


# Generated at 2022-06-13 19:42:13.151355
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Docstring
    from docstring_parser.styles import Style

    def test_simple():
        text = '''\
            Description.

            Arguments:
                arg1: Description
                arg2: Description
            '''
        expected = Docstring(
            summary='Description.',
            description='',
            params=[
                {'name': 'arg1', 'desc': 'Description'},
                {'name': 'arg2', 'desc': 'Description'},
            ],
            returns=[],
            other=[],
            meta=[],
        )
        assert parse(text) == expected


# Generated at 2022-06-13 19:42:24.373553
# Unit test for function parse
def test_parse():
    assert parse("").short_description == ""
    assert parse("").long_description == ""
    assert len(parse("").meta) == 0
    assert parse("").meta[''] == ""
    assert len(parse("").sections) == 0
    assert parse("").sections[''] == ""
    assert len(parse("@param").meta) == 1
    assert parse("@param").meta['@param'] == ""
    assert len(parse("@return").meta) == 1
    assert parse("@return").meta['@return'] == ""
    assert len(parse("@").meta) == 0
    assert parse("@").meta[''] == "@"

# Generated at 2022-06-13 19:42:27.475890
# Unit test for function parse
def test_parse():
    """Unit Test for function parse."""
    class TestClass:
        """This is a TestClass."""
        def test_func(self) -> None:
            """This is a TestFunc.
            """
            pass
    text = TestClass.test_func.__doc__
    style = Style.auto
    Doc = parse(text, style)
    assert len(Doc.summary) > 0

# Generated at 2022-06-13 19:42:30.104800
# Unit test for function parse
def test_parse():
    assert parse("""first line
second line
third line""").short_description == "second line\nthird line"


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:42:32.948641
# Unit test for function parse

# Generated at 2022-06-13 19:42:38.662901
# Unit test for function parse
def test_parse():
    assert parse('Testing') == Docstring(summary='Testing',)
    assert parse('Testing\n\nMore') == Docstring(summary='Testing', body='More')
    assert docstring_parser.parse('''Testing

:param foo: bar

More
''') == Docstring(
    summary='Testing',
    body='More',
    metadata={
        'parameters': [
            {
                'type': None,
                'name': 'foo',
                'description': 'bar',
                'meta': {}
            }
        ]
    }
)


# Generated at 2022-06-13 19:42:49.180430
# Unit test for function parse
def test_parse():
    input = """\
Test docstring.

Tests a few things.

:param param: parameter description
:type param: str
:returns: whatever
:rtype: int
"""
    docstring = parse(input)
    print(docstring.short_description)
    print(docstring.long_description)
    print(docstring.meta["param"][0].description)
    print(docstring.meta["param"][0].type_name)
    print(docstring.meta["returns"][0].description)
    print(docstring.meta["returns"][0].type_name)

# Generated at 2022-06-13 19:42:59.460989
# Unit test for function parse
def test_parse():
    """
    Test function for function parse
    :return:
    """

    # Test ParseError
    with pytest.raises(ParseError):
        parse('')

    # Test rst
    text = '''
    :param int foo: This is foo
    :return: bar
    '''
    docstring = parse(text, style=Style.rst)
    assert docstring.short_description == ''
    assert len(docstring.long_description) == 0
    assert docstring.meta['param'][0]['type'] == 'int'
    assert docstring.meta['param'][0]['arg'] == 'foo'
    assert docstring.meta['param'][0]['description'] == 'This is foo'
    assert docstring.meta['return'][0]['description'] == 'bar'


# Generated at 2022-06-13 19:43:09.207545
# Unit test for function parse
def test_parse():
    assert parse('one\n\ntwo\n\nthree\n\nfour')
    assert parse('one\n\ntwo\n\nthree\n\nfour', style=Style.numpy)
    assert parse('one\n\ntwo\n\nthree\n\nfour', style=Style.google)
    assert parse('one\n\ntwo\n\nthree\n\nfour', style=Style.sphinx)
    assert parse('one\n\ntwo\n\nthree\n\nfour', style=Style.sphinx_google)

test_parse()

# Generated at 2022-06-13 19:43:10.572681
# Unit test for function parse
def test_parse():
    assert  parse("test")

# Generated at 2022-06-13 19:43:19.014507
# Unit test for function parse
def test_parse():
    text = """This function is used to get the raw data from the files.
    :param filepath: the path of the input file
    :type filepath: str
    :param dataset: the name of the dataset
    :type dataset: str
    :return: the raw data of the file (a dict)
    :rtype: dict
    """
    docstring = parse(text)
    assert docstring.short_description == "This function is used to get the raw data from the files."
    assert docstring.long_description == ''
    assert docstring.returns == {'description': 'the raw data of the file (a dict)',
                                 'types': ['dict'],
                                 'name': None}
    assert len(docstring.params) == 2

# Generated at 2022-06-13 19:43:27.954920
# Unit test for function parse
def test_parse():
    
    # Test 1
    try:
        text = None
        parse(text)
    except AttributeError:
        print(True)
    else:
        print(False)

    # Test 2
    text = "This is a test"
    style = Style.auto
    print(parse(text, style))
    print(parse(text))

    # Test 3
    try:
        text = "This is a test"
        style = "auto"
        parse(text, style)
    except AttributeError:
        print(True)
    else:
        print(False)
    
if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:43:41.348680
# Unit test for function parse
def test_parse():
    docstring = parse("""
    This function does something.

    :param int param1: the first parameter
    :param str param2: the second parameter
    :param bool optional1: first optional parameter (default: True)
    :param bool optional2: second optional parameter (default: None)
    :param list optional3: third optional parameter (default: [1, 2, 3])
    :rtype: int
    :raises ValueError: if something is wrong
    :returns: 1 if successful, 0 otherwise
    """)

    assert isinstance(docstring, Docstring)

    # Test the docblock
    assert docstring.short_description == "This function does something."
    assert not docstring.long_description

    # Test each of the 4 parameters
    assert docstring.params[0].arg_name == 'param1'

# Generated at 2022-06-13 19:43:50.145155
# Unit test for function parse
def test_parse():
    assert parse('') == Docstring('', '', '', '', '', '', [], '')
    assert parse('a') == Docstring('a', '', '', '', '', '', [], '')
    assert parse('a\nb') == Docstring('a', 'b', '', '', '', '', [], '')
    assert parse('a\n\nb') == Docstring('a', 'b', '', '', '', '', [], '')
    assert parse('a\n\nb\n\n') == Docstring('a', 'b', '', '', '', '', [], '')

    assert parse('a\n\nb\n\nc') == Docstring('a', 'b', 'c', '', '', '', [], '')

# Generated at 2022-06-13 19:43:58.594945
# Unit test for function parse
def test_parse():
    text = '''This function creates a new database in the path provided.
             IN:
                 name
             OUT:
             error message'''
    text = text.replace(" ","")
    parsed = parse(text, style = Style.numpy)
    assert parsed.short_description == "This function creates a new database in the path provided."
    assert parsed.long_description == ['IN:',
                                       '    name',
                                       'OUT:',
                                       'error message']
    assert parsed.returns is None
    assert parsed.raises is None
    assert parsed.yields is None
    assert parsed.meta.get('parameters') is None

# Generated at 2022-06-13 19:44:05.111346
# Unit test for function parse
def test_parse():
    text = """\
    This is the first line of the docstring.

    This is the second line.

    This is the third line.
    """
    assert parse(text).short_description == "This is the first line of the docstring."
    assert parse(text).long_description == "This is the second line.\n\nThis is the third line."

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:44:17.583902
# Unit test for function parse
def test_parse():
    """Test of function parse"""
    from docstring_parser import parse
    from docstring_parser.common import Docstring
    from docstring_parser.styles import reStructuredText
    from docstring_parser.styles import GoogleDocstring
    from docstring_parser.styles import epytext
    from docstring_parser.styles import NumpyDocstring
    
    text = '''
    """
    This is a doc string

    :param words: Describing words
    :type words: str
    :param status: Status code
    :type status: int
    :returns: Describing returns
    :rtype: int
    :raises ValueError: Raises if value is wrong
    """
    '''

    doc = parse(text)
    assert isinstance(doc, Docstring)

# Generated at 2022-06-13 19:44:31.505970
# Unit test for function parse
def test_parse():
    text = """
    Metadata

    :param param1: this is a first param
    :param param2: this is a second param
    :returns: description of return
    :raises keyError: raises an exception
    """

    parsed = parse(text, Style.numpy)
    assert len(parsed.meta) == 4
    assert any(
        meta.arg_name == 'param1' and meta.kind == 'param' for meta in parsed.meta
    )
    assert any(
        meta.arg_name == 'param2' and meta.kind == 'param' for meta in parsed.meta
    )
    assert any(
        meta.arg_name == 'returns' and meta.kind == 'return' for meta in parsed.meta
    )

# Generated at 2022-06-13 19:44:39.410275
# Unit test for function parse
def test_parse():
    assert parse("""A short summary.
    Long description

    - x: 1
    - y: 2
    """) == Docstring(summary="A short summary.",
        description="Long description",
        meta=[
            Docstring.Meta(
                key="x",
                value=1,
            ),
            Docstring.Meta(
                key="y",
                value=2,
            ),
        ],
    )
    
    assert parse("""A short summary.
    Long description
    """) == Docstring(summary="A short summary.",
        description="Long description",
        meta=[],
    )

# Generated at 2022-06-13 19:44:48.507233
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import SphinxStyle as SS
    from docstring_parser.styles import GoogleStyle as GS
    from docstring_parser import Docstring
    """
    Simple test for function parse
    """
    text = """
:param url: the url to test
:param email: the email to test
:raises SomeError: if something bad happens
:returns: a very useful value
:rtype: int
    """

    doc = parse(text)
    assert type(doc) == Docstring
    doc = parse(text,GS)
    assert type(doc) == Docstring
    doc = parse(text,SS)
    assert type(doc) == Docstring
    try:
        doc = parse(text,SS)
    except Exception as exc:
        assert type(exc) == ParseError



# Generated at 2022-06-13 19:44:56.625429
# Unit test for function parse
def test_parse():
    docstr = r'''Class for important thing

    blah blah blah

    Meta data stuff:
        meta_key: meta_value
        another_key: another_value

    Parameters
    ----------
    arg1 : int
        The first parameter.
    arg2 : str
        The second parameter.

    Returns
    -------
    arg1 + arg2
    '''
    test = parse(docstr)
    assert test.short_description == 'Class for important thing'
    assert test.long_description == 'blah blah blah'
    assert test.meta == {"meta_key": "meta_value", "another_key": "another_value"}

# Generated at 2022-06-13 19:44:57.658270
# Unit test for function parse
def test_parse():
    import doctest
    doctest.testmod()
     

# Generated at 2022-06-13 19:44:59.805364
# Unit test for function parse
def test_parse():
    from docstring_parser.parser import parse as ds_parse

    docstring = """
    This is a
    multiline
    docstring
    """

    d = ds_parse(docstring)
    print("The docstring is : " , d)

# test_parse()

# Generated at 2022-06-13 19:45:10.946412
# Unit test for function parse
def test_parse():
    text = """
        .. _my-text:
        my text

        :param foo: p1
        :param bar: p2
        :returns: r1
        :rtype: int
        :key foo: v1
        :key bar: v2
        :key baz: v3

        my description


        my more description

        """
    result = parse(text)
    assert result.short_description == 'my text'
    assert result.long_description == 'my description\nmy more description'
    assert result.params == {
        'foo': 'p1',
        'bar': 'p2'}
    assert result.returns == 'r1'
    assert result.rtype == 'int'

# Generated at 2022-06-13 19:45:21.334143
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    test_text = '''function name: test
    Single line description
    Args:
        arg1: test arg 1
        arg2: test arg 2
    Returns:
        Return list[str]
    '''
    doc = parse(test_text, style = Style.google)
    print(doc.summary)
    print(doc.description)
    print(doc.returns)
    print(doc.meta['Args'])
    print(doc.returns)


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:45:30.871966
# Unit test for function parse
def test_parse():
    """Test function parse"""
    print("Testing parse...", end="")
    # Test 1
    docstring = "This is the docstring"
    docstring_parsed = parse(docstring)
    assert docstring_parsed.summary  == "This is the docstring"
    assert docstring_parsed.return_ == None
    assert docstring_parsed.meta == {}
    # Test 2
    docstring = """
This is the docstring

And this is the description
    """
    docstring_parsed = parse(docstring)
    assert docstring_parsed.summary  == "This is the docstring"
    assert docstring_parsed.return_   == None
    assert docstring_parsed.meta["description"] == "This is the description"
    # Test 3
   

# Generated at 2022-06-13 19:45:44.504927
# Unit test for function parse
def test_parse():
    # Positive
    assert parse("""\
    Args:
        param1: The first parameter.
        param2: The second parameter.
    Returns:
        True if successful, False otherwise.
""")


# Generated at 2022-06-13 19:45:50.157352
# Unit test for function parse
def test_parse():
    print("Function parse:")
    text = """@param S: input S
@type S: str
@param t: input t
@type t: int
@return: int
@rtype: int"""
    print(parse(text))

if __name__ == "__main__":
    text = """@param S: input S
@type S: str
@param t: input t
@type t: int
@return: int
@rtype: int"""
    Doc = parse(text)
    print(Doc)

# Generated at 2022-06-13 19:46:00.819004
# Unit test for function parse
def test_parse():
    text = '''
    A module for a simple calculator.

    This module provide a class for number
    processing.

    Attributes
    ----------
    first_number: int
        The first number

    second_number: int
        The second number
    '''

    parsed_text = parse(text)
    assert parsed_text.description == 'A module for a simple calculator.\n\nThis module provide a class for number processing.\n\n'
    assert parsed_text.attributes[0]["name"] == "first_number"
    assert parsed_text.attributes[0]["type"] == "int"
    assert parsed_text.attributes[0]["description"] == "The first number"

    # for test module parse
    '''
    import doctest
    doctest.testmod()
    '''

# Generated at 2022-06-13 19:46:02.802020
# Unit test for function parse
def test_parse():
    parse("""
    This is the first paragraph
    """)

# Generated at 2022-06-13 19:46:13.849196
# Unit test for function parse
def test_parse():
    dop = parse("""This is the module docstring.
    This is the second line.

    This is a third line.
    """)
    print(dop)
    assert dop.__dict__ == {'description': "This is the module docstring.\n    This is the second line.\n\n    This is a third line.", 'summary': "This is the module docstring.\n    This is the second line."}

    dop = parse("""This is the module docstring.
    This is the second line.

    This is a third line.""")
    print(dop)

# Generated at 2022-06-13 19:46:24.218611
# Unit test for function parse
def test_parse():
    text = """
        short summary here.

        Long(er) description here.

        :param name: description here
        :param foo: description here
        """
    doc = parse(text)
    assert doc.summary == 'short summary here.'
    assert doc.description == '(er) description here.\n\n'
    assert doc.returns is None
    assert len(doc.params) == 2
    assert doc.params[0].arg_name == 'name'
    assert doc.params[1].arg_name == 'foo'
    print('unit test for function parse success.')

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:46:39.010119
# Unit test for function parse
def test_parse():
    text = """
            One sentence summary.

            Extended description.

            - No bullets.
            - No bullets, again.

            :param x: Parameter x.
            :type x: int
            :returns: Nothing
            :raises KeyError: Raises an exception.
            """

    text2 = """
            One sentence summary.
            """
    text3 = """
            One sentence summary.

            Extended description.

            No bullets.

            :param x: Parameter x.
            :type x: int
            :param z: Parameter z.
            :type z: int
            :returns: Nothing
            :raises KeyError: Raises an exception.
            """
    doc = parse(text)
    doc2 = parse(text2)
    doc3 = parse(text3)

# Generated at 2022-06-13 19:46:42.555552
# Unit test for function parse
def test_parse():
    assert parse("")
    assert parse("test text")
    assert parse("test text", Style.google)
    assert parse("test text", Style.pep257)
    assert parse("test text", Style.numpy)
    assert parse("test text", Style.auto)

# Generated at 2022-06-13 19:46:56.513352
# Unit test for function parse
def test_parse():
    assert parse("""Single-line docstring.""") == Docstring(summary='Single-line docstring.', body='', meta={})
    assert parse("""One-line docstring with "quotes".""") == Docstring(summary='One-line docstring with "quotes".', body='', meta={})
    assert parse("""Multi-line docstring.

With body.""") == Docstring(summary='Multi-line docstring.', body='With body.', meta={})
    assert parse("""\
        """
                    ) == \
        Docstring(summary='', body='', meta={})
    assert parse("""\
        A one-liner.
        """
                    ) == \
        Docstring(summary='A one-liner.', body='', meta={})

# Generated at 2022-06-13 19:47:03.959566
# Unit test for function parse
def test_parse():
    from docstring_parser import parse
    #napoleon_text = '''
    #    Function description.
    #
    #    Args:
    #        a: Integer
    #        b: Integer
    #
    #    Return:
    #        return_value: Integer
    #    '''
    numpy_text = '''
    Function description.

    Parameters
    ----------
    a : int
        integer
    b : int
        integer

    Returns
    -------
    return_value : int
        integer
    '''
    epytext_text = '''
    Function description.

    @param a: integer
    @type  a: int

    @param b: integer
    @type  b: int

    @return: integer
    @rtype:  int
    '''
    google_text

# Generated at 2022-06-13 19:47:18.496767
# Unit test for function parse
def test_parse():
    """
    Function that test parse function

    """
    print("Testing Function parse(text, style)")
    from docstring_parser.styles import parse_google, parse_numpy
    text = """
    Main function that parse a docstring.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    try:
        result = parse(text, Style.google)
        assert result.short_description == "Main function that parse a docstring."
    except ParseError as e:
        print("Error during execution of the parse function")
        print("Error Message: " + str(e))
        exit(1)
    else:
        print("Function parse(text, style) executed successfully.")

# Generated at 2022-06-13 19:47:26.632167
# Unit test for function parse
def test_parse():
    assert parse("test") == Docstring()
    assert parse("test", Style.sphinx) == Docstring()
    assert parse("test", Style.google) == Docstring()
    assert parse("test", Style.numpy) == Docstring()
    assert parse("test", Style.sphinx_numpy) == Docstring()
    assert parse("test", style = Style.sphinx) == Docstring()
    assert parse("test", style = Style.google) == Docstring()
    assert parse("test", style = Style.numpy) == Docstring()
    assert parse("test", style = Style.sphinx_numpy) == Docstring()

# Generated at 2022-06-13 19:47:28.573409
# Unit test for function parse
def test_parse():
    s = """
    This is a test Paragraph
    """
    y = parse(s)
    assert y.long_description == s

# Generated at 2022-06-13 19:47:35.009534
# Unit test for function parse
def test_parse():
    # some tests
    
    # 1st test
    return parse("""
    Sample docstring in google style.

    Parameters
    ----------
    x : int
        sample parameter
    """)

    # 2nd test
    return parse("""
    Sample docstring in numpy style.

    Parameters
    ----------
    x : int
        sample parameter
    """)

    # 3rd test
    return parse("""
    Sample docstring in sphinx style.

    :param x: sample parameter
    :type x: int
    """) 


# Generated at 2022-06-13 19:47:35.935026
# Unit test for function parse
def test_parse():
    pass

# Generated at 2022-06-13 19:47:45.923558
# Unit test for function parse
def test_parse():
    doc = parse('''
Parameters
----------
a : int
    The first parameter.
b : str
    The second parameter.
x : float
    The third parameter.
''')
    assert isinstance(doc.meta, list)
    assert len(doc.meta) == 3
    assert doc.meta[0]['name'] == 'a'
    assert doc.meta[1]['type_name'] == 'str'
    assert doc.meta[2]['type_name'] == 'float'
    assert doc.meta[1]['description'] == 'The second parameter.'
    assert doc.meta[2]['description'] == 'The third parameter.'


# Generated at 2022-06-13 19:47:48.088016
# Unit test for function parse
def test_parse():
    assert parse("text") == Docstring(summary="text", meta=[])


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:47:58.985859
# Unit test for function parse
def test_parse():
    # test for correct parse
    text = '''Hello, World!

This is a test docstring.

:param param1: Description of `param1`
:type param1: str
:param param2: Description of `param2`
:type param2: int
:returns: Description of return value
:rtype: str
:Raises ValueError: If `param2` is equal to zero
'''
    style = Style.google

    doc = parse(text, style)
    assert len(doc.lines) == 2
    assert doc.meta['param1'][0] == 'Description of `param1`'
    assert doc.meta['param2'][0] == 'Description of `param2`'
    assert doc.meta['returns'][0] == 'Description of return value'

# Generated at 2022-06-13 19:48:11.427187
# Unit test for function parse
def test_parse():
    """
    check different output for different styles
    check for exception if style does not exist
    """
    docstring = parse(
        """this is a sample docstring
        with some content
        """
    )
    assert docstring.short_description == "this is a sample docstring"
    assert docstring.long_description == "with some content"
    assert docstring.style == "numpy"


    docstring = parse(
        """this is a sample docstring
        """
    )
    assert docstring.short_description == "this is a sample docstring"
    assert docstring.long_description == ""
    assert docstring.style == "numpy"

    docstring = parse(
        '''this is a sample docstring
        """
        with some content
        """
        '''
    )
    assert docstring

# Generated at 2022-06-13 19:48:13.980150
# Unit test for function parse
def test_parse():
    parse()
    parse(text = None)
    parse(text = None, style = None)
    parse(text = '', style = None)

# Generated at 2022-06-13 19:48:24.395112
# Unit test for function parse
def test_parse():
	style = Style.auto
	
	# test case: no docstring
	text = None
	assert parse(text, style) == None
	
	# test case: empty docstring
	text = ""
	assert parse(text, style) == Docstring(meta=None, content=None, description=None)
	
	# test case: empty content
	text = "sometags"
	assert parse(text, style) == Docstring(meta=None, content=None, description=None)
	
	# test case: normal case, no tag, standard docstring
	text = """
	This is a function.
	
	:param x: a variable x
	:param y: a variable y
	:returns: x + y
	"""

# Generated at 2022-06-13 19:48:36.481111
# Unit test for function parse
def test_parse():
    assert(parse("Hello") == Docstring("Hello"))
    assert(parse("Hello", Style.google) == Docstring("Hello"))
    assert(parse("Hello World!") == Docstring("Hello World!"))
    assert(parse("Hello World!", Style.google) == Docstring("Hello World!"))
    assert(parse("Hello World!", Style.numpy) == Docstring("Hello World!"))
    assert(parse("Hello World!\n") == Docstring("Hello World!\n"))
    assert(parse("Hello World!\n", Style.google) == Docstring("Hello World!\n"))
    assert(parse("Hello World!\n", Style.numpy) == Docstring("Hello World!\n"))
    assert(parse("Hello World!\n\n") == Docstring("Hello World!\n\n"))

# Generated at 2022-06-13 19:48:46.361945
# Unit test for function parse
def test_parse():
    text = """Summary line.

Extended description.

:param x: first param
:param y: second param

:returns: return value
:rtype: int
    """
    doc = parse(text)

    # The below tests test the return value of parse.
    # These tests should be run only if the values are correctly
    # returned by parse.
    assert doc.summary == 'Summary line.'
    assert doc.extended_summary == 'Extended description.'
    assert doc.meta['x'] == 'first param'
    assert doc.meta['y'] == 'second param'
    assert doc.return_meta['returns'] == 'return value'
    assert doc.return_meta['rtype'] == 'int'



# Generated at 2022-06-13 19:48:57.398933
# Unit test for function parse
def test_parse():
    text = """
    This is a docstring for a function.

    Parameters
    ----------
    test1: int
        Test string for parameter 1
    test2: float
        Test string for parameter 2

    Returns
    -------
    float
        Description of return value
    """
    docstring = parse(text)
    assert docstring.short_description == 'This is a docstring for a function.'
    assert docstring.long_description == ''
    assert docstring.meta['Parameters'][0].arg_name == 'test1'
    assert docstring.meta['Parameters'][0].arg_type == 'int'
    assert docstring.meta['Parameters'][0].description == 'Test string for parameter 1'
    assert docstring.meta['Parameters'][1].arg_name == 'test2'

# Generated at 2022-06-13 19:49:06.147352
# Unit test for function parse
def test_parse():
    import os
    import sys
    sys.path.append(os.getcwd())
    from docstring_parser.common import Docstring, ParseError

    try:
        from docstring_parser.styles import STYLES, Style

    except:
        print("error")

    text = '''
    This is a test for parse function.
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    '''

    doc = parse(text, style=Style.auto)
    print(doc)

# Generated at 2022-06-13 19:49:18.289392
# Unit test for function parse
def test_parse():
    a = parse("""The parse function is implemented in Python""")
    assert a.short_description == "The parse function is implemented in Python"

    b = """
        test
        """
    b = parse(b)
    assert b.short_description == "test"

    c = """
        test
        - a
        - b
        - c
        """
    c = parse(c)
    assert c.short_description == "test"
    assert "a" in c.long_description
    assert "b" in c.long_description
    assert "c" in c.long_description

    d = """
        test
        - a
        - b
        - c
        :param int a
        """
    d = parse(d)
    assert d.short_description == "test"

# Generated at 2022-06-13 19:49:29.499198
# Unit test for function parse
def test_parse():
    doc_string = """This is a test function.
Args:
    test1: test1 description.
    test2: test2 description.
Returns:
    test3: test3 description.
    test4: test4 description.
"""
    aret = parse(doc_string)
    assert aret.short_description == "This is a test function."
    assert len(aret.long_description) == 0
    assert len(aret.meta) == 4
    assert aret.meta["args"]["test1"] == "test1 description."
    aret.meta["returns"]["test4"] = "test4 description."
    assert aret.meta["returns"]["test4"] == "test4 description."
    aret.meta["returns"]["test5"] = "test5 description."

# Generated at 2022-06-13 19:49:40.562202
# Unit test for function parse
def test_parse():
    test_str = '''
    This is a test function.

    :param param1: this is a first param
    :param param2: this is a second param
    :param param3: this is a third param
    :returns: None
    :raises keyError: raises an exception
    '''

    doc = parse(test_str, style=Style.numpy)
    assert(doc.short_description == 'This is a test function.')
    assert(doc.long_description == '')
    assert(str(doc.meta['param1']) == 'this is a first param')
    assert(str(doc.meta['param2']) == 'this is a second param')
    assert(str(doc.meta['param3']) == 'this is a third param')

# Generated at 2022-06-13 19:49:43.285178
# Unit test for function parse
def test_parse():
    text = """
    * A Test
    * B Test
    * No Test
    """
    assert parse(text) == text

# Generated at 2022-06-13 19:49:55.179600
# Unit test for function parse
def test_parse():
    text="""
        Parameters
        ----------
        arg1 : int
            The first parameter.

        arg2 : str
            The first parameter.
        """
    docstring = parse(text)
    assert isinstance(docstring, Docstring)
    assert docstring.params[0].name == 'arg1'
    assert docstring.params[0].type_name == 'int'
    assert docstring.params[0].desc == 'The first parameter.'
    assert docstring.params[1].name == 'arg2'
    assert docstring.params[1].type_name == 'str'
    assert docstring.params[1].desc == 'The first parameter.'


# Generated at 2022-06-13 19:50:08.793549
# Unit test for function parse
def test_parse():
    docstring = """Summary line.
    Extended description.
    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2
    Returns:
        bool: Description of return value
    """
    parsed_docstring = parse(docstring)
    assert parsed_docstring.short_description == 'Summary line.'
    assert parsed_docstring.long_description == 'Extended description.'
    assert parsed_docstring.return_type == 'bool'
    assert parsed_docstring.return_annotation == 'Description of return value'
    assert parsed_docstring.parameters[0].name == 'arg1'
    assert parsed_docstring.parameters[0].type == 'int'
    assert parsed_docstring.parameters[0].description == 'Description of arg1'
    assert parsed_docstring

# Generated at 2022-06-13 19:50:12.392696
# Unit test for function parse
def test_parse():
    docstring = """
    This is a module docstring.

    This module is for testing the docstring parser.
    """
    document = docstring_parse(docstring)
    assert document.short_description == "This is a module docstring."
    assert document.long_description == "\nThis module is for testing the docstring parser.\n"

# Generated at 2022-06-13 19:50:25.122954
# Unit test for function parse
def test_parse():
    import pytest
    from operator import add

    text = '''    A not-so-simple function that does nothing.

    Args:
        a (int): first parameter
        b (int): second parameter

    Returns:
        int: many times of a and b
    '''

    docstring = parse(text, style=Style.numpy)

    assert docstring.summary == 'A not-so-simple function that does nothing.'
    assert docstring.short_description == 'A not-so-simple function that does nothing.'
    assert docstring.long_description == '' 
    assert docstring.parameters == ['a (int): first parameter', 'b (int): second parameter']
    assert docstring.parameters_long == ['first parameter', 'second parameter']
    assert docstring.parameters_name == ['a', 'b']


# Generated at 2022-06-13 19:50:32.575292
# Unit test for function parse
def test_parse():
    desc = 'This is a module docstring'
    params = {'x': 'some value', 'y': 'some other value'}
    nps = {'res': 'the result'}
    rets = 'This is what the function returns'
    examples = '>>> do_something()\n42'
    todo = '- Write real tests\n- Add type annotations'
    meta = {'authors': 'John Doe', 'date': 'today', 'status': 'beta'}
    doc = Docstring(desc, params, returns=rets, examples=examples,
                    non_params=nps, todo=todo, meta=meta)
    assert parse(doc.text) == doc

# Generated at 2022-06-13 19:50:35.542481
# Unit test for function parse
def test_parse():
    for i in range(len(st)):
        #print(parse(st[i]))
        print(parse(st[i]).sections)


# Generated at 2022-06-13 19:50:40.449165
# Unit test for function parse
def test_parse():
    text = '''acc: Accuracy metric.
    asd: asd metric
    '''
    meta = ''
    r = parse(text, style=Style.google)
    assert r.summary == '' and r.meta == '' and r.extras == ''

# Generated at 2022-06-13 19:50:41.919071
# Unit test for function parse
def test_parse():
   assert parse("""This is a test""") == """This is a test"""

# Generated at 2022-06-13 19:50:52.940248
# Unit test for function parse
def test_parse():
    text = '''\
    Parameters
    ----------
    arg1 : int
        The first argument.
    arg2 : str
        The second argument.
    '''

    doc = parse(text, Style.numpy)

    assert doc.meta['arg1'].arg_type == 'int'
    assert doc.meta['arg1'].description == 'The first argument.'
    assert doc.meta['arg2'].arg_type == 'str'
    assert doc.meta['arg2'].description == 'The second argument.'

    text = '''\
    param arg1: int
        The first argument.
    param arg2: str
        The second argument.
    '''

    doc = parse(text, Style.google)

    assert doc.meta['arg1'].arg_type == 'int'
    assert doc.meta

# Generated at 2022-06-13 19:51:04.110213
# Unit test for function parse
def test_parse():
    docstring = "This is a short description.\n\n\
    This is a long description. It should be indented with the same\n\
    number of spaces as the short description. While it's line-wrapped\n\
    to fit into 78 characters or so. Good luck!"
    doc = parse(docstring)
    assert doc.short_description == "This is a short description."
    assert doc.long_description == "This is a long description. It should be indented with the same number of spaces as the short description. While it's line-wrapped to fit into 78 characters or so. Good luck!"
    assert list(doc.meta.keys()) == ['param', 'return']
    assert list(doc.meta.values()) == [['a'],['b']]

# Generated at 2022-06-13 19:51:11.749436
# Unit test for function parse
def test_parse():
    parse_test = parse('''This is the docstring for this function
    :param d: description
    :type d: int
    :param b: description
    :type b: int
    ''')
    assert(parse_test.short_description == 'This is the docstring for this function')
    assert(len(parse_test.params) == 2)
    assert(not parse_test.returns)
    assert(not parse_test.meta)

# Generated at 2022-06-13 19:51:24.595466
# Unit test for function parse
def test_parse():
    from docstring_parser.common import FunctionDocstring, ClassDocstring
    from docstring_parser.pep257 import parse as parse_pep257
    from docstring_parser.numpy import parse as parse_numpy
    from docstring_parser.google import parse as parse_google
    from docstring_parser.sphinx import parse as parse_sphinx
    from docstring_parser.sphinx_napoleon import parse as parse_sphinx_napoleon

    def _assert_function(function_docstring, description, params, returns, raw):
        assert function_docstring.description == description
        assert function_docstring.params.to_dict() == params
        assert function_docstring.returns.to_dict() == returns
        assert function_docstring.raises.to_dict() == {}
        assert function