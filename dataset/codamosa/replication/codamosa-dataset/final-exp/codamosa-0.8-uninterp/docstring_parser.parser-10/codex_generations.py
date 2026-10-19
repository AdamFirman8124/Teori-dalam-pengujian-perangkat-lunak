

# Generated at 2022-06-13 19:41:31.494989
# Unit test for function parse
def test_parse():
    docstring = "Summary of the method.\n\n    Longer summary, which can contain multiple paragraphs.\n    Follows the summary\n    and can contain any markup.\n    \n    :param name: Parameter description.\n    :type name: One of the string, int, long, bool types\n    :param optional: Optional parameter description. If not specified,\n        then defaults to ``False``.\n    \n    :raises ValueError: If something goes wrong.\n    :return: a string\n    :rtype: str\n    "
    parsed = parse(docstring, style=Style.numpy)
    assert 'Summary of the method.' == parsed.short_description
    assert 'Longer summary, which can contain multiple paragraphs.\nFollows the summary\nand can contain any markup.' == parsed.long_

# Generated at 2022-06-13 19:41:39.415963
# Unit test for function parse
def test_parse():
    """Test function parse."""

    input_str = '''
    """
    This is a section.

    This is another section.
    """
    '''
    output_str = '''
    """
    This is a section.

    This is another section.
    """
    '''
    assert parse(input_str) == parse(output_str)

    input_str = '''
    """This is a section.
    This is another section.
    """
    '''
    output_str = '''
    """
    This is a section.

    This is another section.
    """
    '''
    assert parse(input_str) == parse(output_str)

    input_str = '''
    """This is a section.
    This is another section.
    """
    '''
    output_

# Generated at 2022-06-13 19:41:50.531005
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Parameter, Variable, SeeAlso
    from docstring_parser.styles import STYLES, Style

    print(parse('Test docstring.'))
    assert parse('Test docstring.') is not None

    print(parse('Test docstring.', style=Style.auto))
    assert parse('Test docstring.', style=Style.auto) is not None

    print(parse('Test docstring.', style="numpy"))
    assert parse('Test docstring.', style="numpy") is not None

    print(parse('Test docstring.', style=Style.numpy))
    assert parse('Test docstring.', style=Style.numpy) is not None

    print(parse('Test docstring.', style=STYLES['numpy']))

# Generated at 2022-06-13 19:41:55.830147
# Unit test for function parse
def test_parse():
    """
    Test the function parse
    """
    from docstring_parser.common import Docstring, ParseError
    from docstring_parser.styles import STYLES, Style

    text = '''
    docstring text to parse
    '''
    style = Style.google
    try:
        print(parse(text, style))
    except:
        print('发生异常')

# Generated at 2022-06-13 19:42:05.339833
# Unit test for function parse
def test_parse():
    text = '''
    :param int a: aaaaaaa
    :param int b: bbbbbbb
    :type str c: ccccccc
    :type int d: ddddddd
    :returns: None, 3
    :raises RuntimeError: if something bad occurs
    :returns: 4
    :returns: None
    :param int a: aaaaaaa_none
    '''
    docs = parse(text, style=Style.google)
    assert docs.raises == [('RuntimeError', 'if something bad occurs')]
    assert docs.returns == ['4', 'None', '3']
    assert docs.meta['param']['a'][0] == {'content': 'aaaaaaa', 'type': 'int', 'required': True}

# Generated at 2022-06-13 19:42:12.554398
# Unit test for function parse
def test_parse():
    text = """
    This is a game.
    :param name: the name of the player
    :type name: string
    :returns: nothing
    :rtype: none
    """
    d = parse(text)
    assert isinstance(d, Docstring)
    assert d.short_description == "This is a game."
    assert d.long_description == ""
    assert d.meta["name"].description == "the name of the player"
    assert d.meta["name"].annotation == "string"
    assert d.returns.description == "nothing"
    assert d.returns.annotation == "none"
    assert d.returns.directive == "returns"

# Generated at 2022-06-13 19:42:22.060111
# Unit test for function parse
def test_parse():
    """Parses a docstring"""
    docstring = """
    This is a docstring.

    :param str foo: description for foo
    :returns:
      return value description
    """
    # parse the docstring
    parsed_docstring = parse(docstring)
    print(parsed_docstring)
    print(parsed_docstring.params)
    print(parsed_docstring.params['foo'])
    print(parsed_docstring.returns)

# Generated at 2022-06-13 19:42:30.886932
# Unit test for function parse
def test_parse():
    assert parse(' ').meta == {}
    text = ':param x: A dummy param\n'
    assert parse(text).params == {'x': 'A dummy param'}
    assert parse(text).returns == ''
    text = ':param x: A dummy param\n' + ':returns: Dummy return\n'
    assert parse(text).returns == 'Dummy return'
    text = ':param x: A dummy param\n' + ':returns: Dummy return\n' + ':author: John Doe'
    assert parse(text).meta == {'author': 'John Doe'}

# Generated at 2022-06-13 19:42:39.019239
# Unit test for function parse
def test_parse():
    text = '''
    This is a test.

    :param a: param a
    :param b: param b
    :returns: nothing or something
    '''
    parse_ = parse(text)
    assert parse_.short_description == 'This is a test.'
    assert parse_.long_description == ''
    assert len(parse_.params) == 2
    assert parse_.params[0].arg_name == 'a'
    assert parse_.params[0].description == 'param a'
    assert parse_.params[1].arg_name == 'b'
    assert parse_.params[1].description == 'param b'
    assert len(parse_.returns) == 1
    assert parse_.returns[0].type_name == 'nothing or something'
    assert parse_.returns[0].description == ''


# Generated at 2022-06-13 19:42:47.584630
# Unit test for function parse
def test_parse():
    def test_func(a: int, b: int, c: int) -> int:
        """A testing function with parameters and returns.

        :param a: a test parameter.
        :param b: a test parameter.
        :param c: a test parameter.
        :returns: a test return value.
        """
        #Dummy

# Generated at 2022-06-13 19:42:57.957566
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleStyle

    text = "Parse the docstring into its components.\n\nParam:\n\ttext: docstring text to parse\n\tstyle: docstring style\n\treturns: parsed docstring representation"
    docstring = parse(text, style=Style.google)
    assert isinstance(docstring, GoogleStyle)

# Generated at 2022-06-13 19:42:59.555489
# Unit test for function parse
def test_parse():
    assert parse("Hello, world!") == Docstring(('Hello, world!'), {})



# Generated at 2022-06-13 19:43:08.799969
# Unit test for function parse
def test_parse():
    text = """
    Args:
        arg1 (int): The first parameter.
        arg2 (str): The second parameter.
    Returns:
        bool: The return value. True for success, False otherwise.
    """
    # print(parse(text))
    # args = parse(text).args
    # print(args)
    # print(args[0])
    # print(args[0].name)
    # print(args[0].type_name)
    # print(args[0].description)

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:43:17.744673
# Unit test for function parse
def test_parse():
    text = '''Hello
    :param name: Your name.
    :type name: str
    :param verbose: Be verbose?
    :type verbose: bool
    :returns: None
    '''

    result = parse(text)
    assert result.short_description == 'Hello'
    assert len(result.params) == 2
    assert result.params[0].arg_name == 'name'
    assert result.params[0].description == 'Your name.'
    assert result.params[0].type_name == 'str'
    assert result.params[1].arg_name == 'verbose'
    assert result.params[1].description == 'Be verbose?'
    assert result.params[1].type_name == 'bool'
    assert result.returns.type_name is None
    assert result.returns

# Generated at 2022-06-13 19:43:23.601361
# Unit test for function parse
def test_parse():
    docstring_text = """\
    Demo

    Parameters
    ----------
    text : str
        Documentation for the text parameter.
        It's not that long, but has multiple lines.

    Returns
    -------
    int
        Returns an integer. This line is not indented properly.
        The next one is.
            It is indented.
    """
    docstring1 = parse(docstring_text)
    assert len(docstring1.meta) == 2
    assert len(docstring1.meta[0].content) == 1
    assert docstring1.meta[0].name == 'Parameters'
    assert docstring1.meta[0].content[0].type == 'str'
    assert docstring1.meta[0].content[0].name == 'text'
    assert docstring1.meta[0].content[0].desc

# Generated at 2022-06-13 19:43:33.546805
# Unit test for function parse
def test_parse():
    """Test function parse.

    Unit tests for the function parse function.
    """
    text = """
    Function to multiply two numbers.

    :param x: first number
    :param y: second number
    :returns: the product of two numbers
    :raises ValueError: x is 0
    """
    docstring = parse(text)
    assert docstring.short_description == "Function to multiply two numbers."
    assert docstring.long_description == "Function to multiply two numbers."
    assert docstring.raises[0].type == "ValueError"
    assert docstring.raises[0].description == "x is 0"
    assert docstring.returns.type == "the product of two numbers"
    assert docstring.params[0].name == "x"

# Generated at 2022-06-13 19:43:43.013957
# Unit test for function parse
def test_parse():
    text = """one line.
    
    :param arg1: the first argument
    :param arg2: the second argument
    :returns: description of return value
    :raises keyError: raises an exception
    """
    lines = text.split('\n')
    ds = parse(text)
    assert ds.short_description == lines[0]
    assert ds.long_description == '\n'.join(lines[1:]) + '\n'
    assert len(ds.params) == 2
    assert ds.returns_doc == 'description of return value'
    assert len(ds.raises) == 1
    assert len(ds.meta) == 3
    
    
if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:43:46.743381
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleDocstring
    from docstring_parser.common import Docstring
    result=parse('''This function does something.
    :param x: a parameter named x
    :type x: int
    :param y: a parameter named y
    :type y: str
    :returns: None
    :rtype: None
    ''')
    assert(isinstance(result,Docstring))

# Generated at 2022-06-13 19:43:51.405160
# Unit test for function parse
def test_parse():
    assert parse("")
    assert parse("", Style.spinx)
    assert parse("", Style.google)
    assert parse("", Style.numpy)
    assert parse("", Style.auto)

    try:
        parse("", Style.pep257)
        assert False
    except ParseError:
        pass

# Generated at 2022-06-13 19:43:57.202925
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import Google
    google_style = "A short summary.\n"
    google_style += "\n"
    google_style += "A longer description."
    doc = parse(google_style)
    assert doc.short_description == "A short summary."
    assert doc.long_description == "A longer description."
    assert doc.style == Style.google
    assert google_style == str(doc)

# Generated at 2022-06-13 19:44:04.236547
# Unit test for function parse
def test_parse():
    text = '''
    A text to illustrate usage of parse function from module parser.py
    '''
    result = parse(text)
    assert result

# Generated at 2022-06-13 19:44:07.734821
# Unit test for function parse
def test_parse():
    text = '''\
    :param a: aaa
        foofoo
    :param b: bbb
    :param c: ccc
        fooooo
        :returns: maybe
    '''
    do = parse(text)
    assert do.meta.get_value("returns") == "maybe"

# Generated at 2022-06-13 19:44:15.468411
# Unit test for function parse
def test_parse():
    text = '''\
    :param name: The name to use.
    :param state: Whether to start or stop.
    :raises ValueError: Raised with invalid input.
    :rtype: int

    This is the first line.
    And this is the second line.
    '''

    result = parse(text)

    assert result.description == 'This is the first line.\nAnd this is the second line.'
    assert result['parameters'] == [
        {'name': 'name',
         'description': 'The name to use.'},
        {'name': 'state',
         'description': 'Whether to start or stop.'}]
    assert result['return'] == {'description': 'int'}

# Generated at 2022-06-13 19:44:17.008677
# Unit test for function parse
def test_parse():
    assert parse('Test docstring')

# Generated at 2022-06-13 19:44:25.339232
# Unit test for function parse
def test_parse():
    ret = parse('test')
    assert(ret.short_description == 'test')
    assert(ret.long_description == None)
    assert(ret.meta == [])
    assert(ret.params == [])
    assert(ret.returns == None)
    assert(ret.raises == [])

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:44:27.359857
# Unit test for function parse
def test_parse():
    docstring = """Simple one line docstring"""
    print(parse(docstring))

# Generated at 2022-06-13 19:44:30.554202
# Unit test for function parse
def test_parse():
    """Test the parse function"""
    string = parse("""
    This is a docstring
    """)
    assert(str(string) == "This is a docstring")

# Generated at 2022-06-13 19:44:35.444698
# Unit test for function parse
def test_parse():
    global text, style
    text = """
    This is a test docstring.
    Args:
        x (int): an integer
        y (float): a float
    """
    style = Style.numpy
    assert parse(text, style) == Docstring(description="This is a test docstring.\n",
                                           parameters=[(Parameter(argname='x', type='int',
                                                                  description='an integer'),
                                                        Parameter(argname='y', type='float',
                                                                  description='a float')),
                                                       ],
                                           returns=[],
                                           meta=[])

# Generated at 2022-06-13 19:44:45.645277
# Unit test for function parse
def test_parse():
    docstring_test_1 = """Example docstring.
        Parameters
        ----------
        arg1 : int
            The first argument.
        arg2 : str
            The second argument.

        Returns
        -------
        str
            The return value. True for success, False otherwise.
    """
    docstring_test_2 = """Example 2 docstring.
        Parameters
        ----------
        arg1 : int
            The first argument.
        arg2 : str
            The second argument.

        Returns
        -------
        str
            The return value. True for success, False otherwise.

        Other Parameters
        ----------------
        arg3 : int
            The third argument.
    """


# Generated at 2022-06-13 19:44:48.290147
# Unit test for function parse
def test_parse():
    """
    The test_parse function check the default case (auto)
    """
    docstring = """
    This function tests the function parse
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    parse(docstring)
    print('parse function: ok')


# Generated at 2022-06-13 19:44:55.765345
# Unit test for function parse
def test_parse():
    text = """
    Dummy docstring
    """
    expected = Docstring(description="Dummy docstring", meta=[])

# Generated at 2022-06-13 19:44:56.460551
# Unit test for function parse
def test_parse():
    print(parse.__doc__)



# Generated at 2022-06-13 19:45:03.227351
# Unit test for function parse
def test_parse():
    assert "Project-wide" in parse(
        """
    Project-wide TODOs
    *******************

    * Write the tests.
    * Document the code.
    * Make the code beautiful.
    """
    ).description
    assert "Project-wide" in parse(
        """
    Project-wide TODOs

    *******************

    * Write the tests.
    * Document the code.
    * Make the code beautiful.
    """
    ).description
    assert "Project-wide" in parse(
        """
    Project-wide TODOs

    *******************

    * Write the tests.
    * Document the code.
    * Make the code beautiful.
    """
    ).description

# Generated at 2022-06-13 19:45:11.061397
# Unit test for function parse
def test_parse():
    assert "Hi, this is the summary" in parse(docstring).summary
    assert "Bye, this is a description" in parse(docstring).description
    assert parse(docstring).parameters[0].arg_name == "arg1"
    assert parse(docstring).parameters[0].type_name == "int"
    assert "summary" in parse(docstring).returns.description
    assert parse(docstring).returns.type_name == "int"

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:45:19.176917
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Parameter, ReturnValue, Type, Docstring
    from docstring_parser.styles import Style

    text = '''
        Single line summary.

        Extended description.

        Parameters
        ----------
        arg1 : str
            Description of arg1
        arg2 : int
            Description of arg2

        Returns
        -------
        str
            Description of return value

        Raises
        ------
        ValueError
            If `arg2` is equal to `arg1`.
    '''

    docstring = parse(text)

    assert docstring.summary == 'Single line summary.'
    assert docstring.extended_summary == 'Extended description.'

    params = docstring.params

# Generated at 2022-06-13 19:45:27.709912
# Unit test for function parse
def test_parse():
    parse_str = """Description.
    
    Args:
        arg0: A positional argument.
        arg1 (str): A keyword argument.
    
    Returns:
        int: The return value.
    
    
    
    
    
    
    
    
    
    
    """
    docstring = parse(parse_str)
    assert docstring.short_description == "Description."
    assert docstring.long_description == ""
    assert docstring.meta["args"] == [
        "arg0: A positional argument.",
        "arg1 (str): A keyword argument."
    ]
    assert docstring.meta["returns"] == ["int: The return value."]

# Generated at 2022-06-13 19:45:29.419807
# Unit test for function parse
def test_parse():
    ds = parse("""First line.
    second line.
    """)
    assert isinstance(ds, Docstring)



# Generated at 2022-06-13 19:45:40.723394
# Unit test for function parse
def test_parse():
    text_1 = "This is a function."
    docstring_1 = parse(text_1)
    assert docstring_1.full == text_1
    assert docstring_1.summary == text_1

    text_2 = """
    This is a function.

    This is a short explanation.

    This is a long explanation.
    This is a long explanation.
    This is a long explanation.

    :param expression: expression described
    :param operator: operator described
    :returns: true if the expression is valid
    """
    docstring_2 = parse(text_2)
    assert docstring_2.full == text_2
    assert docstring_2.summary == "This is a function."
    assert docstring_2.description == "This is a short explanation."

# Generated at 2022-06-13 19:45:51.554824
# Unit test for function parse
def test_parse():
    text = '''\
One line summary.

Extended description.

:type param1: int
:param param2: description
:returns: description
:rtype: str

```python
Some code
```
'''
    docstring = parse(text)
    assert docstring.short_description == 'One line summary.'
    assert docstring.long_description == 'Extended description.'
    assert docstring.metadata[0].arg_name == 'param1'
    assert docstring.metadata[0].arg_type == 'int'
    assert docstring.metadata[0].arg_desc == ''
    assert docstring.metadata[1].arg_name == 'param2'
    assert docstring.metadata[1].arg_type == ''
    assert docstring.metadata[1].arg_desc == 'description'
   

# Generated at 2022-06-13 19:46:02.953467
# Unit test for function parse
def test_parse():
    text = """Summary line.

Extended description.

:param int a: The first parameter.
:param b: The second parameter.
:raises AttributeError: The ``Raises`` section is a list of all exceptions
    that are relevant to the interface.
:returns: The return value.
:rtype: int

"""

# Generated at 2022-06-13 19:46:13.972617
# Unit test for function parse
def test_parse():
    t0 = ".. codeauthor:: Daniel Sank <daniel.sank@gmail.com>\n"
    t1 = ".. codeauthor:: Daniel Sank <daniel.sank@gmail.com>\n"
    t1 += "    Foo Bar <foo@bar.com>\n"
    test_parse_help(t0)
    test_parse_help(t1)


# Generated at 2022-06-13 19:46:26.547590
# Unit test for function parse
def test_parse():
    res = parse(text, style= Style.auto)
    res1 = parse(text, style=Style.numpy)
    assert res == res1


# Generated at 2022-06-13 19:46:37.255565
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import SphinxStyle
    import pytest
    def test_parse(text, style):
        assert parse(text, style=style) == SphinxStyle(text)
    text1 = """"
    :param foo: a list of something
    :type foo: list of ints
    :returns: bar
    :rtype: str
    """
    test_parse(text1, style=Style.sphinx)
    text2 = """"
    :name foo: a list of something
    :type foo: list of ints
    :returns: bar
    :rtype: str
    """
    test_parse(text2, style=Style.sphinx)

# Generated at 2022-06-13 19:46:45.452177
# Unit test for function parse
def test_parse():
    assert parse('') == Docstring(
        '', '', [], [], [], [], [], [], '', '', {}, {}, None
    )
    assert parse('''
        some desc

        :arg: some argument
        :returns: some return
    ''') == Docstring(
        'some desc', '', [], [], [], [], [], [], '', '', {}, {}, None
    )
    assert parse('''
        :param str: some parameter
        :rtype: int
    ''') == Docstring(
        '', '', [], [], [], [], [], [], '', '', {}, {}, None
    )



# Generated at 2022-06-13 19:46:50.963482
# Unit test for function parse
def test_parse():
    text   = "Line 1\nLine 2\n\nLine 3"
    result = parse(text)
    assert result.short_description == "Line 1\nLine 2"
    assert result.long_description == "Line 3"

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:46:54.907831
# Unit test for function parse
def test_parse():
    test1 = """This is one line summary.

    It can have multiple paragraphs.
    """
    docstring1 = parse(test1)
    assert docstring1._summary == 'This is one line summary.'
    a

# Generated at 2022-06-13 19:47:02.249378
# Unit test for function parse
def test_parse():
    example_docstring = parse("""\
    Short summary.

    Long summary

    Meta

    Args:
        arg1: first argument
        arg2: second argument

    Returns:
        return: one return
        return: another return
    """)
    assert example_docstring.short_description == 'Short summary.'
    assert example_docstring.long_description == 'Long summary'
    assert example_docstring.meta == ['Meta']
    assert example_docstring.args == [('arg1', 'first argument'),
                                      ('arg2', 'second argument')]
    assert example_docstring.returns == [('return', 'one return'),
                                         ('return', 'another return')]

# Generated at 2022-06-13 19:47:14.207416
# Unit test for function parse

# Generated at 2022-06-13 19:47:15.318968
# Unit test for function parse
def test_parse():
    parse('parse')
    parse('parse')
    parse('')
    parse.__doc__ == 'parse'


# Generated at 2022-06-13 19:47:20.301406
# Unit test for function parse
def test_parse():
    # Define a docstring and expected outcome
    text = '''
    Parameters
    ----------
    func: callable
        Function to be wrapped
    '''
    ds = Docstring(params=[
        Docstring.Param('func', 'callable', 'Function to be wrapped'),
    ])

    # Test that the parse function works and produce desired result
    assert parse(text) == ds

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:47:27.155227
# Unit test for function parse
def test_parse():
    parse(text = 'hello world!')

import doctest
doctest.testmod(optionflags = doctest.NORMALIZE_WHITESPACE, verbose = True)

# Generated at 2022-06-13 19:47:35.566291
# Unit test for function parse
def test_parse():
    text = """\
    Parameters
    ----------
    x : float
        X coordinate.
    y : float
        Y coordinate.
    """

    docstring = parse(text)
    assert docstring.summary == ''
    assert docstring.extended_summary == ''
    assert docstring.body == ''
    assert len(docstring.meta) == 2
    assert docstring.meta[0].argname == 'x'
    assert docstring.meta[0].type_name == 'float'
    assert docstring.meta[0].description == 'X coordinate.'
    assert docstring.meta[1].argname == 'y'
    assert docstring.meta[1].type_name == 'float'
    assert docstring.meta[1].description == 'Y coordinate.'

# Generated at 2022-06-13 19:47:46.942917
# Unit test for function parse

# Generated at 2022-06-13 19:47:58.111225
# Unit test for function parse
def test_parse():
    text = ""

    docstring = parse(text)

    assert docstring.short_description == ""
    assert docstring.long_description == ""
    assert docstring.params == []
    assert docstring.returns == None
    assert docstring.yields == None
    assert docstring.meta == {}

    text = """Summary line.

Description of what the function does.
"""

    docstring = parse(text)

    assert docstring.short_description == "Summary line."
    assert docstring.long_description == "Description of what the function does."
    assert docstring.params == []
    assert docstring.returns == None
    assert docstring.yields == None
    assert docstring.meta == {}


# Generated at 2022-06-13 19:48:06.698792
# Unit test for function parse
def test_parse():
    test_case = '''This is line1
    This is line2
    This is line3
    '''
    result = parse(test_case)
    assert result.body == 'This is line1\nThis is line2\nThis is line3\n', 'Parse body incorrectly'
    assert result.short_desc == '', 'Parse short description incorrectly'
    assert result.long_desc == '', 'Parse long description incorrectly'
    assert result.meta == {}, 'Parse meta incorrectly'


# Generated at 2022-06-13 19:48:16.461688
# Unit test for function parse
def test_parse():
    # default parameter
    text = 'test'
    style = Style.auto
    docstring = parse(text,style)
    assert docstring.summary=='test'
    assert docstring.meta=={}

    text = 'test: xxxxxxx'
    style = Style.reST
    docstring = parse(text,style)
    assert docstring.summary=='test'
    assert docstring.meta=={'test':'xxxxxxx'}

    text = 'test:\n    xxxxxxx'
    style = Style.Numpy
    docstring = parse(text,style)
    assert docstring.summary=='test'
    assert docstring.meta=={'test':'xxxxxxx'}

# Generated at 2022-06-13 19:48:32.888944
# Unit test for function parse
def test_parse():
    """
    Test case for function parse
    """
    # Case 1
    text1 = '''    Retrieve meta informations on the dataset.

    Parameters
    ----------
    dataset_id : int or str
        The id or name of the dataset
    '''
    assert parse(text1)
    # Case 2
    text2 = '''Retrieve meta informations on the dataset.
    Parameters
    ----------
    dataset_id : int or str
        The id or name of the dataset
    '''
    assert parse(text2)
    # Case 3
    text3 = '''
    Retrieve meta informations on the dataset.
    Parameters
    ----------
    dataset_id : int or str
        The id or name of the dataset
    '''
    assert parse(text3)



# Generated at 2022-06-13 19:48:40.888320
# Unit test for function parse
def test_parse():
    text = '''\
    This is the summary.

    It can have multiple lines.

    :param arg1: description
    :type arg1: type description
    :var1: description
    :var2: description
    :returns: description
    :rtype: type description'''
    docstring = parse(text)
    assert docstring.summary == 'This is the summary.'
    assert docstring.body == 'It can have multiple lines.'
    assert docstring.returns is not None
    assert docstring.returns.raw_type == 'type description'

# Generated at 2022-06-13 19:48:46.630112
# Unit test for function parse
def test_parse():
    text = """
    Parse the docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    style = Style.numpy
    ds = parse(text, style)
    print(ds.params)
    print(ds.returns)
    print(ds.meta)
    print(ds.summary)
    print(ds.description)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:48:57.751393
# Unit test for function parse
def test_parse():
    # Test 1
    style = Style.auto
    text = """This is a short description.

    This is a *longer* description, with a few more
    paragraphs.

    :param param1: description of param1
    :param param2: description of param2
    :type param1: str
    :returns: description of return
    :rtype: int
    :raises ValueError: description of exception
    """
    actual = parse(text, style)

# Generated at 2022-06-13 19:49:06.534732
# Unit test for function parse
def test_parse():
    text = '''Summary line.
    Extended description.
    Args:
        arg1 (int): Description of `arg1`
        arg2 (str, optional): Description of `arg2`
    Returns:
        bool: Description of return value
    '''
    ds = parse(text)
    assert ds.summary == 'Summary line.'
    assert ds.extended_summary == 'Extended description.'

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:49:13.406116
# Unit test for function parse
def test_parse():
    text = '''
    This function will be used to parse the docstring
    :param text:
    :param style:
    :returns:
    '''
    assert parse.__annotations__ == {'text': str, 'style': Style, 'return': Docstring}
    assert type(parse('This is a test')) == Docstring

test_parse()

# Generated at 2022-06-13 19:49:16.448701
# Unit test for function parse
def test_parse():
    text = '''
    Args:
        x: The x argument
        y: The y argument which has a
            second line
    '''
    print(parse(text))



# Generated at 2022-06-13 19:49:20.670394
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    text = """
    I am a docstring
    """
    parsed = parse(text)
    assert parsed.short_description == "I am a docstring"
    assert parsed.long_description == ""

if __name__ == "__main__":
    # Unit test
    test_parse()
    print("All Passed")

# Generated at 2022-06-13 19:49:22.145548
# Unit test for function parse
def test_parse():
    x = parse.__code__
    assert parse == parse(x)

# Generated at 2022-06-13 19:49:32.058295
# Unit test for function parse
def test_parse():
    style = 'google'
    text = """A utility function for converting python's basic data structures into JSON strings. To use this, you must add the "json" module to your code - required by all scripts.

    :param x: the variable to convert to JSON
    :type x: list or dict
    :param top: True if this is the topmost call
    :type top: bool
    :param cls: the class of the data type to be converted
    :type cls: class

    :returns: JSON string
    """
    assert parse(text,style).style == style



# Generated at 2022-06-13 19:49:42.602583
# Unit test for function parse
def test_parse():
    docstring = parse(
        """
        A function for adding two numbers.

        :param x: The first number
        :type x: number
        :param y: The second number
        :type y: number
        :returns: The sum of two numbers
        :rtype: number

        .. note::

           You can add two numbers only.

        #. This is the first item in an enumerated list.
        #. This is the second item in an enumerated list.

        Here is some example Python code:

        >>> print(2 + 3)
        5
        """,
        style=Style.google
    )
    assert len(docstring.short_description) > 0
    assert len(docstring.long_description) > 0
    assert len(docstring.params) == 2

# Generated at 2022-06-13 19:49:56.186383
# Unit test for function parse
def test_parse():
    from docstring_parser.common import MultiLine, OneLine
    assert parse('def a():\n    """\n    blah\n    """\n') == MultiLine(
        summary='',
        body=[],
        meta=['blah'])
    assert parse('def a():\n    """\n    blah\n    """\n',
                 style=Style.numpy) == MultiLine(
        summary='',
        body=[],
        meta=['blah'])
    assert parse('def a():\n    """\n    blah\n    """\n',
                 style=Style.google) == MultiLine(
        summary='',
        body=[],
        meta=['blah'],
        style=Style.google)

# Generated at 2022-06-13 19:50:00.101273
# Unit test for function parse
def test_parse():
    assert parse('hello world', 'google').summary == 'hello world'
    assert parse('hello world', 'numpy').summary == 'hello world'
    assert parse('hello world', 'auto').summary == 'hello world'

test_parse()

# Generated at 2022-06-13 19:50:09.571112
# Unit test for function parse
def test_parse():
    # print(parse.__doc__)
    docstring = '''\
    I love Python.
    I want to be a Pythonista.
    '''
    print(parse(docstring))
    # <Docstring (summary="I love Python. I want to be a Pythonista.")>

    docstring = '''\
    Main parsing routine.

    :param text: docstring text to parse
    :param style: docstring style
    '''
    print(parse(docstring))
    # <Docstring (summary="Main parsing routine.",
    #             params=["text: docstring text to parse", "style: docstring style"])>
    #
    # docstring = '''\
    # Main parsing routine.
    #
    # :param text: docstring text to parse
    # :param style: docstring style
   

# Generated at 2022-06-13 19:50:24.737017
# Unit test for function parse
def test_parse():
    ds = """This is a summary.

    This is the description.

    Args:
        arg1 (int): This is the first argument.
        arg2 (str): This is the second argument.
    Kwargs:
        kwarg1 (str): This is the first keyword argument.
        kwarg2 (str): This is the second keyword argument.
    """

# Generated at 2022-06-13 19:50:33.453662
# Unit test for function parse
def test_parse():
    text = (
        "Check the model classification with measurements.\n"
        "\n"
        "Parameters\n"
        "----------\n"
        "predictions :  array-like, shape = [n_samples]\n"
        "    Predicted class label per sample.\n"
        "measurements : array-like, shape = [n_samples]\n"
        "    Actual class label per sample.\n"
        "Returns\n"
        "-------\n"
        "score : float\n"
        "    Score between 0 and 1, the bigger the better.\n"
    )

    docstring = parse(text)

    assert docstring.summary == "Check the model classification with measurements."
    assert docstring.description == ""

# Generated at 2022-06-13 19:50:46.163463
# Unit test for function parse

# Generated at 2022-06-13 19:50:53.746560
# Unit test for function parse
def test_parse():
    """Test for the parse() function"""
    test_in = """\
==================================
the header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header header
==================================
:param text: docstring text to parse
:param style: docstring style
:returns: parsed docstring representation
"""


# Generated at 2022-06-13 19:51:02.222872
# Unit test for function parse
def test_parse():
    ''' Test to check parse() without any style'''
    def test_function():
        '''Dummy test function

        :param str1: prameter 1
        :param str2: parameter 2
        :returns: this is return

        This is a long description line.
        '''

    doc = parse(test_function.__doc__)
    assert doc.short_description == "Dummy test function"
    assert doc.long_description == "This is a long description line."



# Generated at 2022-06-13 19:51:03.485381
# Unit test for function parse
def test_parse():
    assert parse(test_text) == test_d

# Generated at 2022-06-13 19:51:09.418046
# Unit test for function parse
def test_parse():
    doc = """
    This is a short description.

    And here's the detail description.
    """

    docstring = parse(doc)
    print(docstring.short_description, '\n', docstring.long_description)


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:51:19.734608
# Unit test for function parse
def test_parse():
    """Tests the function parse()

    Checks whether the docstring could be parsed using
    the function parse() and if the parsing result is
    equal to the expected result.

    :return: returns whether the test was successful or not
    :rtype: boolean
    """
    text = """
    Function to change the image we are working with.

    This will check for the validity of the file,
    then load it as a PyGame Surface object.

    :param color: The color to create the surface with.
    :type color: RGBA sequence (e.g. (255, 0, 0, 255))

    :param size: Size of the surface.
    :type size: 2-tuple of int

    :return: The newly created surface.
    :rtype: pygame.Surface
    """

    result = parse(text)

    expected_