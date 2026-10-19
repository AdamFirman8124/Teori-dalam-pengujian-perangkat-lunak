

# Generated at 2022-06-13 19:41:36.205341
# Unit test for function parse
def test_parse():
    # actual parsed output
    docstring = parse("""
        This is a docstring.

        Does it work?

        :returns: whether it worked
        :rtype: bool

        """)

    # manually parsed output

# Generated at 2022-06-13 19:41:42.825303
# Unit test for function parse
def test_parse():
    text = '''\
Parameters
----------
start_date: str, datetime, date
    Start date for range of data.
end_date: str, datetime, date
    End date for range of data.
Returns
-------
foo: str
    Foo parameter.
bar: str
    Bar parameter.
'''
    assert parse(text) == parse(text.replace('str', 'str '))
    assert parse(text) == parse(text.replace('date', 'date '))
    assert parse(text) == parse(text.replace('\n', '\r\n'))
    assert parse(text) == parse(text.replace('\n', '\r'))
    assert parse(text) == parse(text.replace('range of data', 'range of data '))

# Generated at 2022-06-13 19:41:52.784663
# Unit test for function parse
def test_parse():
    text = '''
    This is a long summary.

    This is an extended summary. It can span multiple lines.

    :param name: a name
    :param age: an age
    :returns: a person
    :rtype: Person
    :raises ValueError: when bad things happen
    '''
    d = parse(text)
    assert d.summary == "This is a long summary."
    assert d.extended_summary == "This is an extended summary. It can span multiple lines."
    assert len(d.params) == 2
    assert d.params[0].arg_name == "name"
    assert d.params[0].description == "a name"
    assert d.params[1].arg_name == "age"
    assert d.params[1].description == "an age"
    assert d.returns

# Generated at 2022-06-13 19:41:59.734356
# Unit test for function parse
def test_parse():
    text = '''Summary line.

    Extended description of function.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2, arg3 : str
        Description of arg2 and arg3

    Returns
    ------
    str
        Description of return value.

    Other Parameters
    ----------------
    kwarg1 : bool
        Description of `kwarg1`
    kwarg2, kwarg3 : str
        Description of `kwarg2` and `kwarg3`
    '''
    a = parse(text)
    assert a.summary == 'Summary line.'
    assert a.extended_summary == 'Extended description of function.'
    assert len(a.params) == 2
    assert len(a.other_params) == 2
    assert a.returns.type_name == 'str'

# Generated at 2022-06-13 19:42:05.679747
# Unit test for function parse
def test_parse():
    text = '''
    Some first line
    Second line
    '''

    try:
        result = parse(text)
        assert len(result.description) == 2
        assert result.description[0] == 'Some first line'
        assert result.description[1] == 'Second line'
        assert len(result.meta) == 0
        assert len(result.sections) == 0
    except:
        print('function [parse] error:')
        print(result.meta)
        print(result.description)
        print(result.sections)
        raise

# Generated at 2022-06-13 19:42:13.526616
# Unit test for function parse
def test_parse():
    if __name__ == "__main__":
        source = """\
        This is a sample docstring.

        :param str name: (required) name,
               at least 3 characters long
        :param str description: description
        :type description: text
               this is a continuation of the description
        :param int age: (required) age of the
               person
        :param list[str] stuff:  (required) list of
               things
        :param bool is_active: is the person
               active?
        :returns: this is the return description
                  which is pretty long
        :rtype: bool
        :raises: ValueError, KeyError
        """


# Generated at 2022-06-13 19:42:16.591523
# Unit test for function parse
def test_parse():
    text = """this is some text.
    """
    style = Style.google
    parse(text, style)



# Generated at 2022-06-13 19:42:20.858660
# Unit test for function parse
def test_parse():
    docstring = '''
    This is a simple sentence.
    
    :param x: Parameter x.
    :returns: Return value.
    
    '''
    parse(docstring)
    # Should work.
    assert True


# Generated at 2022-06-13 19:42:32.101902
# Unit test for function parse
def test_parse():
    docstring = """Single-line docstring."""
    expected = Docstring(summary='Single-line docstring.')
    assert parse(docstring) == expected

    docstring = """Single-line docstring.
    """
    expected = Docstring(summary='Single-line docstring.')
    assert parse(docstring) == expected

    docstring = """Single-line docstring with a description.

    The description can be several lines long.
    """
    expected = Docstring(summary='Single-line docstring with a description.',
                         description='The description can be several lines long.')
    assert parse(docstring) == expected

    docstring = """Single-line docstring with a description.

    The description can be several lines long.

    Ignored line.

    """

# Generated at 2022-06-13 19:42:38.275067
# Unit test for function parse
def test_parse():
    text = """\
        Arguments:
            arg1 (int): first argument
            arg2 (str): second argument
        """
    assert parse(text) == Docstring(
        content=text,
        meta=[
            ('arguments', [
                ('arg1', {'type': 'int',
                          'desc': 'first argument'}),
                ('arg2', {'type': 'str',
                          'desc': 'second argument'}),
            ]),
        ],
        style=0,
    )


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:42:51.331284
# Unit test for function parse
def test_parse():
    # Test Google style
    google_text = """
                 This is a google style
                 function example.
                 Args:
                     arg1: first argument
                     arg2: second argument
                 Returns:
                     returns result
                 """
    google_doc = Docstring(meta={'Args': ['arg1: first argument', 'arg2: second argument'],
                             'Returns': 'returns result'},
                    content='This is a google style\nfunction example.')
    assert parse(google_text) == google_doc
    assert parse(google_text, Style.google) == google_doc

    # Test Numpy style

# Generated at 2022-06-13 19:43:01.318250
# Unit test for function parse
def test_parse():
    # Parser a standard google docstring
    d1 = parse("""This is a docstring.
    Args:
        arg1: The first argument.
        arg2: The second argument.
    """)
    assert d1.short_description == 'This is a docstring.'
    assert len(d1.args) == 2
    assert d1.args[0].arg_name == 'arg1'
    assert d1.args[0].description == 'The first argument.'
    assert d1.args[1].arg_name == 'arg2'
    assert d1.args[1].description == 'The second argument.'

    # Parse a numpy docstring

# Generated at 2022-06-13 19:43:13.150130
# Unit test for function parse
def test_parse():
    def function_with_docstring(a,b):
        """Returns sum of a and b.

        :param a: the first operand
        :param b: the second operand
        :type a: int
        :type b: int
        :returns: sum of a and b

        """
        return a + b

    docstring = parse(function_with_docstring.__doc__)
    assert docstring.short_description == "Returns sum of a and b."
    assert docstring.long_description == ""
    assert [tag.name for tag in docstring.tags] == ['param', 'type', 'param', 'type', 'returns']
    assert docstring.tags[0].name == 'param'
    assert docstring.tags[0].annotation == 'a'

# Generated at 2022-06-13 19:43:16.855199
# Unit test for function parse
def test_parse():
    doc = "Hello World! This is a multiline docstring for test.\n"
    doc += "For test purpose, please ignore it."
    parse_result = parse(doc)
    print(parse_result)


# Generated at 2022-06-13 19:43:23.040969
# Unit test for function parse
def test_parse():
    text_1 = """Summarize what the function does.
    Multiline docstring
    """
    text_2 = """Summarize what the function does.
    Multiline docstring
    :param[in] arg1: first arg
    :return: arg1+1, arg2+2
    """
    text_3 = """Summarize what the function does.

    Multiline docstring

    Args:
        arg1 (int): first arg
        arg2 (int): second arg

    Returns:
        int: return value

    Raises:
        ValueError: if something bad happens
    """


# Generated at 2022-06-13 19:43:29.906713
# Unit test for function parse
def test_parse():
    """
    Test function pase
    :return:
    """
    doc = """
    Function that test parse function

    :param text:
    :param style:
    :returns:
    """
    docstring = parse(doc)

    assert docstring.short_description == "Function that test parse function"
    assert docstring.long_description == ""
    assert docstring.params == {"text": None, "style": None}
    assert docstring.returns == None
    assert docstring.type == None
    assert docstring.meta == {}

# Generated at 2022-06-13 19:43:40.813371
# Unit test for function parse
def test_parse():
    # Determine if the docstring has been properly processed.
    text = """
This is a summary.

This is the first line of the first paragraph.
This is the second line of the first paragraph.

This is the first line of the second paragraph.
This is the second line of the second paragraph.
"""
    mydoc = parse(text)
    assert "summary" in mydoc.summary.lower()
    assert "first line of the first paragraph" in mydoc.description[0].lower()
    assert "first line of the second paragraph" in mydoc.description[1].lower()


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:43:43.385033
# Unit test for function parse
def test_parse():
    text = """
    Short summary.
 
    Longer description
    with
    multiple lines
    """
    assert parse(text).short_description == 'Short summary.'
    assert parse(text).long_description == 'Longer description\nwith\nmultiple lines'

# Generated at 2022-06-13 19:43:53.859125
# Unit test for function parse
def test_parse():
    docstring = parse("""Hello
        :param arg1:
        :type arg1:
        :param arg2:
        :type arg2:
        :returns:
        :rtype:
    """)
    assert docstring.short_description == "Hello"
    assert docstring.long_description == None
    assert docstring.returns == None
    assert docstring.rtype == None
    assert len(docstring.meta) == 2
    assert docstring.meta[0].arg_name == "arg1"
    assert docstring.meta[1].arg_name == "arg2"


# Generated at 2022-06-13 19:44:02.288568
# Unit test for function parse
def test_parse():
    assert parse(
        '''
        :param name: name
        :type name: str
        '''
    ) == Docstring(
        params=[
            {'name': 'name', 'type': 'str', 'description': ''}
        ],
        returns=[],
        yields=[],
        raises=[],
        other=[],
        summary='',
        description='',
        meta={'param': {'name': 'name', 'type': 'str', 'description': ''},
              'return':{}, 'yield':{}, 'raise':{}}
    )


# Generated at 2022-06-13 19:44:16.387363
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring(Summary(""), [], None, None, [])
    assert parse(
        "test\n\n"
        ":args a: a desc\n"
        ":args b: b desc\n") == Docstring(
        Summary("test"),
        [Argument("a", "a desc"), Argument("b", "b desc")], None, None, [])
    assert parse(
        "test\n\n"
        ":arg a: a desc\n"
        ":arg b: b desc\n") == Docstring(
        Summary("test"),
        [Argument("a", "a desc"), Argument("b", "b desc")], None, None, [])

# Generated at 2022-06-13 19:44:29.668856
# Unit test for function parse
def test_parse():
    docstring_raw = """one line summary

extended description, which can
span multiple lines

:param x: description of x
:type x: str
:returns: description of return value
:rtype: int
"""
    d = parse(docstring_raw)
    assert len(d.meta) == 2
    assert d.short_description == "one line summary\n"
    assert d.long_description == "extended description, which can\nspan multiple lines\n"
    assert d.meta['x'].arg_name == 'x'
    assert d.meta['x'].arg_type == 'str'
    assert d.meta['x'].description == 'description of x'
    assert d.meta['returns'].arg_name == 'returns'
    assert d.meta['returns'].arg_

# Generated at 2022-06-13 19:44:36.643935
# Unit test for function parse
def test_parse():
    test_text = """This is a test docstring.
    :param str var:
        This is a description for var.
        It has three lines.
        This is the third line
    :yields: The output
    :rtype: int
    :rtype: str: This is a third type.
"""

    docstring = parse(test_text)

    assert docstring.short_description == "This is a test docstring."
    assert len(docstring.long_description) == 3
    assert docstring.long_description[0] == 'This is a description for var.'
    assert docstring.long_description[1] == 'It has three lines.'
    assert docstring.long_description[2] == 'This is the third line'

# Generated at 2022-06-13 19:44:46.409541
# Unit test for function parse
def test_parse():
    text = '''
    Multi lines description
    :param method: the http method
    :param url: the url to request
    :param callback: the callback function
    :returns: the response if no callback provided
    '''
    ret = parse(text)
    assert ret.meta['method'] == 'the http method'
    assert ret.meta['url'] == 'the url to request'
    assert ret.meta['callback'] == 'the callback function'
    assert ret.desc == 'Multi lines description\n'
    assert ret.returns == 'the response if no callback provided\n'

if __name__ == '__main__':
    # restore bug
    # https://github.com/agronholm/sphinxcontrib-napoleon/issues/131
    parse('''
    .. code::

    ''')

# Generated at 2022-06-13 19:44:48.044591
# Unit test for function parse
def test_parse():
    assert parse("""
    A simple example.
    """) == Docstring("A simple example.", [])



# Generated at 2022-06-13 19:44:56.297930
# Unit test for function parse
def test_parse():
    text = """One line summary.

    Extended description.

    :param arg1: description 1
    :param arg2: description 2
    :returns: description
    :raises keyError: raises an exception
    """

    docstring = parse(text)
    assert docstring.short_description == "One line summary."
    assert docstring.long_description == "Extended description.\n\n"
    assert len(docstring.params) == 2
    assert docstring.params['arg1'].arg_name == 'arg1'
    assert docstring.params['arg1'].description == 'description 1'
    assert docstring.params['arg2'].arg_name == 'arg2'
    assert docstring.params['arg2'].description == 'description 2'
    assert docstring.returns.description == 'description'


# Generated at 2022-06-13 19:45:00.629087
# Unit test for function parse
def test_parse():
    """
    This function tests the function parse.
    It takes in a doc string, and a style type and then tests for the function
    parse.
    """
    text = "This is a docstring"
    style = Style.google
    output = parse(text, style)
    assert isinstance(output, Docstring)


if __name__ == '__main__':
    text = "This is a docstring"
    style = Style.google
    print(parse(text, style))

# Generated at 2022-06-13 19:45:03.702796
# Unit test for function parse
def test_parse():
    from docstring_parser.styles.docstring_parser import parse
    docstring = 'This is an example docstring.'
    doctest = parse(docstring)
    assert doctest.summary == "This is an example docstring."

# Generated at 2022-06-13 19:45:14.440561
# Unit test for function parse
def test_parse():
    from difflib import unified_diff
    from io import StringIO
    from docstring_parser import parse_docstring, parse_oneline
    s = """
    This is a description.

    :param int arg1: The first argument.
    :param: arg2: The second argument.
    :type arg2: str
    :returns: Wether the answer is true.
    :rtype: str
    """
    result = parse(s)

# Generated at 2022-06-13 19:45:14.899842
# Unit test for function parse
def test_parse():
    pass

# Generated at 2022-06-13 19:45:22.045959
# Unit test for function parse
def test_parse():
    sample_docstring = '''
        Test this.
        Test that.
        - Things
        - Stuff
    '''

    res = parse(sample_docstring)
    print(res)

# test_parse()

# Generated at 2022-06-13 19:45:31.282758
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Docstring, FunctionDocstring
    from docstring_parser.styles import GoogleStyle
    ret = parse("""
        Hello world.

        :param arg: an argument.
        :returns: something
    """.strip())
    ret2 = parse("""
        Hello world
        :arg arg: an argument.
        :returns: something
    """.strip(), style=Style.google)
    assert isinstance(ret, FunctionDocstring)
    assert isinstance(ret2, FunctionDocstring)
    assert ret == ret2
    assert ret.description == "Hello world."
    assert ret.returns == "something"
    assert ret.arguments == {"arg": "an argument."}
    ret = parse.__doc__.strip()
    ret2 = parse.__doc__.strip()

# Generated at 2022-06-13 19:45:42.478141
# Unit test for function parse
def test_parse():
    """Test function parse"""
    correct = [
        ('', 'short desc', 'long desc', 'closing'),
        ('single', 'short desc', 'long desc', 'closing'),
        ('single, multi', 'short desc', 'long desc', 'closing'),
        ('multi1, multi2', 'short desc', 'long desc', 'closing'),
    ]
    styles = ['google', 'pep257', 'numpy', 'numpy_napoleon']
    docs = []


# Generated at 2022-06-13 19:45:49.488092
# Unit test for function parse
def test_parse():
    text = """\
    :param name: name
    """
    assert parse(text)
    assert parse(text, style=Style.numpy)
    assert parse(text, style=Style.google)
    # Expected to fail - default fallback is `numpy` which comes
    # first alphabetically.
    assert not parse(text, style=Style.auto)
    assert parse(text, style=Style.reST)
    # Expected to fail - invalid style
    assert not parse(text, style='invalid')

# Generated at 2022-06-13 19:45:54.211623
# Unit test for function parse
def test_parse():
    long_text = """
    this is long text
    this is long text
    this is long text
    this is long text
    this is long text
    this is long text
    """
    assert len(parse(long_text).summary) == len(long_text)
    assert parse(None).summary == None
    assert parse(None).meta == {}

# Generated at 2022-06-13 19:46:03.923704
# Unit test for function parse
def test_parse():
    assert parse("string").short_description == "string"
    assert parse("string\n  more").short_description == "string"
    assert parse("string\n\n  more").short_description == "string"
    assert parse("string\n\n  more", Style.google).short_description == "string"
    assert parse("string\n\n\n  more", Style.google).short_description == "string"
    assert parse("string", Style.google).short_description == "string"
    assert parse("string\n  more", Style.google).short_description == "string"

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:46:06.019712
# Unit test for function parse
def test_parse():
    style = Style.auto
    text = '''
    this is a test function
    '''

    parse(text, style)

# Generated at 2022-06-13 19:46:07.172911
# Unit test for function parse
def test_parse():
  parse(text, style)


# Generated at 2022-06-13 19:46:17.026857
# Unit test for function parse
def test_parse():
    test_text = '''\
    This is a google style docstring

    Args:
    foo (int): foo is an int
    bar (str): bar is a string

    Returns:
    int. the return code.

    '''
    doc = parse(test_text)
    assert doc.summary == 'This is a google style docstring', "Summary is wrong"
    assert doc.long_description == '', "Long description is wrong"
    assert len(doc.meta['Args']) == 2, "Meta is wrong"
    assert doc.meta['Args']['foo']['type'] == 'int', "Meta is wrong"
    assert doc.meta['Args']['bar']['type'] == 'str', "Meta is wrong"
    # Test that we can pass a number as the style

# Generated at 2022-06-13 19:46:28.742628
# Unit test for function parse
def test_parse():
    from docstring_parser.styles.default import DefaultStyle
    from docstring_parser.styles.numpy import NumpyStyle
    from docstring_parser.styles.google import GoogleStyle
    from docstring_parser.styles.sphinx_numpy import SphinxNumpyStyle
    docstring = '''A docstring.'''
    assert parse(docstring).summary == 'A docstring.'

    docstring = """
    A docstring.

    :param foo: a foo
    """
    assert parse(docstring).summary == 'A docstring.'



# Generated at 2022-06-13 19:46:38.051455
# Unit test for function parse
def test_parse():
	parse()


#main method
if __name__ == "__main__":
	test_parse()

# Generated at 2022-06-13 19:46:46.777891
# Unit test for function parse
def test_parse():

    from docstring_parser.__main__ import main

    main(argv=["prog_name", "-s", "google"])

   # assert parse("") == Docstring()
   # assert parse("Hello world!") == Docstring()
   # assert parse("Args: ...") == Docstring()
   # assert parse("Arguments: ...") == Docstring()
   # assert parse("Arguments:\n    param1: ...") == Docstring()
   # assert parse("Returns:\n    return value") == Docstring()

   # assert parse(
   #     "Hello world!\n"
   #     "Args:"
   #     "    param1: the first parameter\n"
   #     "    param2: the second parameter\n"
   #     "Returns:\n"
   #     "    return value\n"
  

# Generated at 2022-06-13 19:46:57.281950
# Unit test for function parse
def test_parse():
    text = '''
        """
        This is a test.
        
        Args: 
            a (int): a is an int
            b (double): b is float
        """
    '''
    assert parse(text) == parse(text, style=Style.google)
    assert parse(text, style=Style.numpy) == parse(text, style=Style.numpy)
    assert parse(text, style=Style.pep257) == parse(text, style=Style.pep257)
    params = [param for param in parse(text) if not param.optional]
    assert [param.type_name for param in params] == ['int', 'float']

# Generated at 2022-06-13 19:47:10.596030
# Unit test for function parse
def test_parse():
    """Test the parse function."""

    assert (parse(None) == Docstring())
    assert (parse('') == Docstring())
    assert (parse('hello') == Docstring(short_description='hello'))
    assert (parse('hello\n') == Docstring(short_description='hello'))
    assert (parse('hello\n\n') == Docstring(short_description='hello'))
    assert (parse('hello\n\nworld') == Docstring(
        short_description='hello',
        long_description='world',
        meta=dict()
    ))
    assert (parse('hello\n\nworld\n\nfoo: bar\n') == Docstring(
        short_description='hello',
        long_description='world',
        meta=dict(foo='bar')
    ))

##########################################################################################

# Generated at 2022-06-13 19:47:19.603313
# Unit test for function parse
def test_parse():

    # Test case 1
    text = "This is a test"
    style = Style.numpy
    DocTest = Docstring(
        summary=text,
        description='',
        parameters=[],
        returns='',
        see_also=[]
    )
    assert parse(text, style) == DocTest

    # Test case 2
    text = "This is a test"
    style = Style.numpy
    DocTest = Docstring(
        summary=text,
        description='',
        parameters=[],
        returns='',
        see_also=['More', 'Info']
    )
    assert parse(text, style) != DocTest

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:47:29.547625
# Unit test for function parse
def test_parse():
    from docstring_parser.styles.pep257 import parse as pep257_parse
    from docstring_parser.styles.google import parse as google_parse
    from docstring_parser.styles.numpy import parse as numpy_parse

# Generated at 2022-06-13 19:47:35.852464
# Unit test for function parse
def test_parse():
    text = ("""\
    This is a docstring.
    With *italic* and **bold** and some`inline code`."""
            )

    assert parse(text).__str__() == \
        "Docstring(summary='This is a docstring.', description='With *italic* and **bold** and some`inline code`.', tags=[])"
    assert parse(text, style=Style.pep257).__str__() == \
        "Docstring(summary='This is a docstring.', description='With *italic* and **bold** and some`inline code`.', tags=[])"

# Generated at 2022-06-13 19:47:45.260598
# Unit test for function parse
def test_parse():
    test_docstring = """
    Parse the docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    docstring = parse(test_docstring, Style.auto)
    parts = docstring.split_parts()
    #print(dir(docstring))
    print(parts.pop(0))
    #print(parts[1])
    #print(parts[2])
    #print(parts[3])
    #print(parts[4])
    #print(parts[5])

test_parse()

# Generated at 2022-06-13 19:47:56.856747
# Unit test for function parse
def test_parse():
    # Tests for each section of the docstring
    short_desc = "Short description"
    long_desc = "Long description"
    tags = {"param": [
            {"name": "first_arg", "annotation": "int", "desc": "Description of the first argument"},
            {"name": "second_arg", "annotation": "str", "desc": "Description of the second argument"},
            ],
            "returns": {"annotation": "bool", "desc": "Description of the return value"},
            "raises": [
                {"type": "TypeError", "desc": "If `second_arg` is not a string"},
                ],
            "warns": [
                {"type": "RuntimeWarning", "desc": "If `second_arg` is 'foo'"},
                ]
            }

# Generated at 2022-06-13 19:48:09.839699
# Unit test for function parse
def test_parse():
    docstring = """This is a multi-line docstring.
    
       This is the second line.

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
    doc = parse(docstring)
    assert doc.short_description == 'This is a multi-line docstring.'
    assert doc.long_description == 'This is the second line.'

# Generated at 2022-06-13 19:48:19.363618
# Unit test for function parse
def test_parse():
    docstring_text = """\
    Docstring example

    This example shows a docstring with type annotations.

    Parameters
    ----------
    arg1 : str
        A string argument.
    arg2 : int, optional
        An integer argument.

    Returns
    -------
    str
        The string 'hello'.

    Notes
    -----
    Some footnotes.

    """

    assert parse(docstring_text) == parse(docstring_text, style=Style.google)

# Generated at 2022-06-13 19:48:23.038406
# Unit test for function parse
def test_parse():
    text = """This is a function.

    :param a: is a
    :returns: whatever
    """
    doc = parse(text, style = Style.google)
    assert doc.short_description == "This is a function."
    assert doc.long_description == ""
    assert doc.params[0].arg_name == "a"
    assert doc.params[0].type_name == ""
    assert doc.params[0].description == "is a"
    assert doc.returns.type_name == ""
    assert doc.returns.description == "whatever"
    assert doc.returns.arg_name == ""

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:48:34.847528
# Unit test for function parse
def test_parse():
    assert parse("a\nb") == Docstring(summary="", description="a\nb")
    assert parse("a\n\nb") == Docstring(summary="", description="a\n\nb")
    assert parse("a\n\nb", style=Style.numpy) == Docstring(summary="", description="a\n\nb")
    assert parse("a\n\nb", style=Style.google) == Docstring(summary="", description="a\n\nb")
    assert parse("a\n\nb", style=Style.sphinx) == Docstring(summary="", description="a\n\nb")

    assert parse("a\n:b") == Docstring(summary="a", description="", meta={"b": ""})

# Generated at 2022-06-13 19:48:37.046998
# Unit test for function parse
def test_parse():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:48:40.887793
# Unit test for function parse
def test_parse():
    text = '''
    Usage:
        test([params])

    Params:
        var_1: description_1
        var_2: description_2
    '''
    assert parse(text).params == ['var_1', 'var_2']

# Generated at 2022-06-13 19:48:49.253031
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Docstring
    from docstring_parser.styles import Style

    rst_input = """\
    Some heading

    This is some content. You can have **Markdown** syntax here.

    --------------
    Keyword Arguments
     a -- this is a
     b -- this is b
    --------------"""
    assert isinstance(parse(rst_input, Style.restructuredtext), Docstring)
    assert isinstance(parse(rst_input), Docstring)

    pep257_input = """\
    This is some content. You can have **Markdown** syntax here.

    Args:
        a: this is a
        b: this is b"""
    assert isinstance(parse(pep257_input, Style.pep257), Docstring)

# Generated at 2022-06-13 19:48:56.071755
# Unit test for function parse
def test_parse():
    text = """
    this is a command that test how to parse with docstring-parser

    Usage:
        python test.py -h

    Options:
        --h, --help    print this message
    """
    d = parse(text)
    print(d.content)
    print(d.meta['args'])
    print(d.meta.get('options'))
    # print(d.meta.get('others'))


# Generated at 2022-06-13 19:48:59.381759
# Unit test for function parse
def test_parse():
    r = parse.__annotations__
    assert r['text'] == str
    assert 'return' in r['return']
    assert isinstance(r['return']['return'], Docstring)
    assert r['style'] == Style
    assert Style.auto in r['style']

# Generated at 2022-06-13 19:49:09.120103
# Unit test for function parse
def test_parse():
    print("\n=== test_parse ===")
    import textwrap
    ds = textwrap.dedent(
        '''
        :param name:  name of the person
        :type name: str
        :returns:  a string with the greeting and name.
        :rtype: str
            This function greets the person passed as parameter.
        ''').strip()
    d = parse(ds, style=Style.sphinx)
    assert d.short_description == "This function greets the person passed as parameter."
    assert d.long_description == ""
    assert len(d.meta) == 2
    assert d.meta['parameters']['name'] == {'type': 'str',
                                            'description': 'name of the person'}

# Generated at 2022-06-13 19:49:16.079571
# Unit test for function parse
def test_parse():
    assert parse('hello', Style.google).short_description == 'hello'
    assert parse('hello', Style.google).long_description == ''
    assert len(parse('hello', Style.google).meta) == 0
    assert parse('hello', Style.numpy).short_description == 'hello'
    assert parse('hello', Style.numpy).long_description == ''
    assert len(parse('hello', Style.numpy).meta) == 0

# Generated at 2022-06-13 19:49:27.028957
# Unit test for function parse
def test_parse():
    docstring = """\
    A brief description of the class.
    
    Longer description of the class.

    This can have multiple paragraphs.

    Parameters
    ----------
    first_param : int
        The first parameter.
    second_param : str
        The second parameter.

    Returns
    -------
    str
        Some kind of class information.

    Raises
    ------
    ValueError
        If `first_param` is negative.

    """

    style = Style.numpy
    print(parse(docstring, style))


# Generated at 2022-06-13 19:49:29.411977
# Unit test for function parse
def test_parse():
    parse('The best documentation for use')
    parse('The best documentation for use', style='numpy')


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:49:40.526809
# Unit test for function parse
def test_parse():
    docstring = """
    :param ds:
    :param vs:
    :param hoge:
    :param foobar:
    """
    ret = parse(docstring)
    assert isinstance(ret, Docstring)
    expected = [
        dict(
            name='ds',
        ),
        dict(
            name='vs',
        ),
        dict(
            name='hoge',
        ),
        dict(
            name='foobar',
        ),
    ]
    for r in ret.meta:
        assert isinstance(r, dict)
    for index, r in enumerate(ret.meta):
        for k, v in r.items():
            assert expected[index][k] == v

# Generated at 2022-06-13 19:49:47.581577
# Unit test for function parse
def test_parse():
    doc = parse("""
    Args:
        name (str): the name of the person
        age (int): the age of the person
    """)
    assert doc.summary == ""
    assert doc.description == ""
    assert doc.tags[0].__dict__ == {"type_": "Args", "arguments": [("name", "str"), ("age", "int")]}


# Generated at 2022-06-13 19:49:51.622438
# Unit test for function parse
def test_parse():
    text = """This is a docstring.
    """
    assert parse(text).description == "This is a docstring."

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:50:01.248921
# Unit test for function parse
def test_parse():
    text = '''
    Summary line.

    Extended description.

    Args:
        arg1 (str): Description
        arg2 (bool, optional): Description

    Kwargs:
        kwarg1: Description
        kwarg2: Description

    Returns:
        int: Description

    Raises:
        AttributeError: Description
        ValueError: Description

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function/class.
        >>>
    '''

# Generated at 2022-06-13 19:50:10.457584
# Unit test for function parse
def test_parse():
    text = '''\
    Header

    :param a: first param
    :param b: second param
    :return: the return value
    '''
    docstring = parse(text)
    assert docstring.short_description == 'Header'
    assert docstring.long_description == ''
    assert docstring.params['a'] == 'first param'
    assert docstring.params['b'] == 'second param'
    assert docstring.returns == 'the return value'
    assert not docstring.raises
    assert not docstring.meta
    assert not docstring.empty

    text = '''\
    :raises Exception: when things go wrong
    '''
    docstring = parse(text)
    assert not docstring.short_description
    assert not docstring.long_description
    assert not docstring.params


# Generated at 2022-06-13 19:50:18.749402
# Unit test for function parse
def test_parse():
    ds = parse("""This is a docstring.
    list:
     * item 1
     * item 2
    list2:
      * item 1
      * item 2
    """)
    assert ds.short_description == "This is a docstring."
    assert ds.long_description == ""
    assert ds.params == {'list': ' * item 1\n * item 2', 'list2': '  * item 1\n  * item 2'}
    assert ds.returns == {}

    ds = parse("""text1
    text2
    :arg arg1: arg1_desc
    :arg arg2: arg2_desc
    :return ret1: ret1_desc
    :return ret2: ret2_desc
    text3
    text4
    """)

# Generated at 2022-06-13 19:50:29.644962
# Unit test for function parse
def test_parse():
    docstring = '''
    Args:
        param1: The first parameter.
        param2: The second parameter.
    Returns:
        bool: The return value. True for success, False otherwise.
        
    '''
    result = parse(docstring)
    print(result.params)
    print(result.returns)
    print(result.summary)
    
'''
{'param1': {'type': None, 'desc': 'The first parameter.'}, 'param2': {'type': None, 'desc': 'The second parameter.'}}
{'type': 'bool', 'desc': 'The return value. True for success, False otherwise.'}
The main parsing routine.
'''

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:50:33.343447
# Unit test for function parse
def test_parse():
    text = """The main parsing routine."""
    style = Style.google
    parse(text, style)


if __name__ == "__main__":
    text = """The main parsing routine."""
    style = Style.google
    parse(text, style)

# Generated at 2022-06-13 19:50:39.510058
# Unit test for function parse
def test_parse():
    text = 'Docstring for the function parse'
    print(parse(text))



if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:50:44.412730
# Unit test for function parse
def test_parse():
    text = """Example function with types documented in the docstring.

    :param arg1: The first parameter.
    :param arg2: The second parameter.
    :returns: The return value.
    :raises arg3: This is an exception
    """
    docstring = parse(text)
    assert d

# Generated at 2022-06-13 19:50:47.321413
# Unit test for function parse
def test_parse():
    text = "This is my docstring"
    assert parse(text) == 'This is my docstring'
    text2 = "This is my docstring."
    assert parse(text2) == 'This is my docstring.'

# Generated at 2022-06-13 19:50:56.289970
# Unit test for function parse
def test_parse():
    from pprint import pprint
    from docstring_parser.common import Description, Param
    text = '''\
Module template and function template
=====================================

This module provides a function to reverse a list.

Function template
------------------

reverse_list(l)
    Reverses a list
    
    :param l: List to reverse
    :type l: list
    :rtype: list

'''
    ds = parse(text)
    assert ds.meta['Module template and function template'] == Description(
        'This module provides a function to reverse a list.\n')
    assert ds.params['l'] == Param(
        'Reverses a list', ['list'], 'list', None, None)

# Generated at 2022-06-13 19:51:11.367737
# Unit test for function parse
def test_parse():
    test_string = '''\
    Tells you the current default branch.
    :param file: the file to look in
    :returns: the branch
    :rtype: string
    :raises ValueError: if the file is bad
    '''
    assert(parse('\n'.join([line.strip() for line in test_string.splitlines()])) ==
    Docstring(brief='Tells you the current default branch.',
    body='',
    returns=Docstring.Return(type_='string',
    description='the branch'),
    raises=Docstring.Raises(type_='ValueError',
    description='if the file is bad'),
    args=[Docstring.Param(name='file',
    type_=None,
    description='the file to look in')]))

# Generated at 2022-06-13 19:51:16.173531
# Unit test for function parse
def test_parse():
    from docstring_parser import parse
    import io
    import sys

    # Capture the output
    capturedOutput = io.StringIO()          
    sys.stdout = capturedOutput

    parse("""This is a sample docstring that has no style""")
    assert capturedOutput.getvalue() == """docstring_parser.common.ParseError"""