

# Generated at 2022-06-13 19:41:33.904815
# Unit test for function parse
def test_parse():
    text = """
summary line

deprecated: True

extended description

:param int count: number of times
:returns: None
"""

    docstring = parse(text)

    assert docstring.summary == 'summary line'
    assert docstring.deprecated == True
    assert docstring.extended_summary == 'extended description'

    param = docstring.params['count']
    assert param.name == 'count'
    assert param.type == 'int'
    assert param.description == 'number of times'

    return_ = docstring.returns
    assert return_.type == 'None'

# Generated at 2022-06-13 19:41:38.251714
# Unit test for function parse
def test_parse():
    text = '''
        Args:
            arg1 (int): The arg1
            arg2: The arg2

        Raises:
            TypeError: if arg2 is invalid
    '''
    arg_text = '''\
            arg1 (int): The arg1
            arg2: The arg2\
    '''
    raise_text = '''\
            TypeError: if arg2 is invalid\
    '''
    res = parse(text)
    assert res.full_text == text
    assert res.meta.args.full_text == arg_text
    assert res.meta.returns.full_text == ''
    assert res.meta.raises.full_text == raise_text

# Generated at 2022-06-13 19:41:48.980222
# Unit test for function parse

# Generated at 2022-06-13 19:41:56.570054
# Unit test for function parse
def test_parse():
    """Test parse function on each style."""
    example = """Summary line.

Extended description.

:param arg1: Description of arg1
:param arg2: Description of arg2
:returns: Description of return value
:raises keyError: raises an exception
"""
    docstring = parse(example)

# Generated at 2022-06-13 19:42:01.943783
# Unit test for function parse
def test_parse():
    text = """
    This is a module docstring for test purposes.

    :param int arg1: the first argument
    :param arg2: the second argument
    :returns: description of return value

    """
    parts = parse(text, style=Style.numpy)
    print(parts.meta)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:42:07.631515
# Unit test for function parse
def test_parse():
    text = 'Description goes here.\n'
    text += ':param int a: parameter a\n'
    text += ':param str b: parameter b\n'
    text += ':returns: None\n'
    text += ':raises ValueError: if something bad happens\n'
    d = parse(text, style=Style.pep257)
    assert d.short_description == 'Description goes here.'
    assert d.long_description == ''
    assert d.params['a'].description == 'parameter a'
    assert d.returns.description == ''
    assert d.raises['ValueError'].description == 'if something bad happens'

# Generated at 2022-06-13 19:42:22.129007
# Unit test for function parse
def test_parse():
    """Test parse function."""
    import textwrap
    text = textwrap.dedent(r"""
        Sample docstring with

        :var abc: the a literal
        :var def: the b literal
        :param ghi: the c literal
        :rtype: the return type
        :return: something
        :raises ValueError: if something bad happens
        :raises TypeError: if something terrible happens
        """)
    docstring = parse(text)
    assert docstring.meta['var']['abc'] == 'the a literal'
    assert docstring.meta['var']['def'] == 'the b literal'
    assert docstring.meta['param']['ghi'] == 'the c literal'
    assert docstring.meta['rtype'] == 'the return type'
    assert docstring.meta['return']

# Generated at 2022-06-13 19:42:30.083948
# Unit test for function parse
def test_parse():
    text = '''\
    def foo(a, b=1, c=None):
        """Function foo.\n
        Note: All positional parameters are required.

        Args:
            a (str): The first positional parameter.
            b (int, optional): The second positional parameter. Defaults to 1.
            c (int, optional): The third positional parameter. Defaults to None.
        """

    '''
    result = parse(text)
    print(result)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:42:37.308905
# Unit test for function parse
def test_parse():
	assert parse("Docstring") == parse("Docstring", style=Style.google), "Style.google"
	assert parse("Docstring", style=Style.numpy) == parse("Docstring", style=Style.google), "Style.numpy"
	assert parse("Docstring", style=Style.pep256) == parse("Docstring", style=Style.google), "Style.pep256"
	assert parse("Docstring", style=Style.sphinx) == parse("Docstring", style=Style.google), "Style.sphinx"
	assert parse("Docstring", style=Style.google) == parse("Docstring", style=Style.auto), "auto"



# Generated at 2022-06-13 19:42:46.217949
# Unit test for function parse
def test_parse():
    result = parse("""
    title: My Docstring
    summary: |
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
      Donec rhoncus sagittis consectetur. Aliquam
      lobortis vehicula semper.
    extended: |
      Nunc tristique turpis eu pharetra elementum. Ut id
      ultricies purus. In urna augue, cursus vel velit
      non, vestibulum tempor quam. Maecenas gravida
      lorem non iaculis faucibus. Curabitur dictum justo
      ac nulla pellentesque, in hendrerit libero dignissim.
      Fusce eu erat eu orci pulvinar porttitor.
    """)
   

# Generated at 2022-06-13 19:42:54.870640
# Unit test for function parse
def test_parse():
    return
    try:
        text = parse(text)
        print(text.summary)
        print(text.description)
    except ParseError as e:
        print(e)

if __name__ == '__main__':
    text = """
    A test for docstring
    :param x: Integer
    """
    test_parse()

# Generated at 2022-06-13 19:43:00.917660
# Unit test for function parse
def test_parse():
    doc = '''
one-line description here

This is a nice description.
Long.

:param foo: description of foo
:keyword bar: description of bar
:returns: description of return value
:raises ValueError: when a value error occurs

.. deprecated:: 0.2
    This function is deprecated
    '''
    parsed = parse(doc)
    assert parsed.summary == 'one-line description here'
    assert parsed.description == ('This is a nice description.\n'
                                  'Long.\n')
    assert parsed.meta == {
        'param foo': 'description of foo',
        'keyword bar': 'description of bar',
        'returns': 'description of return value',
        'raises ValueError': 'when a value error occurs',
    }

# Generated at 2022-06-13 19:43:10.264366
# Unit test for function parse
def test_parse():
    """Test function parse"""
    STYLES[Style.numpy]._test_setup()
    docstring = "Parse the docstring into its components.\n"
    result = parse(docstring)
    print(result)
    docstring = "Parse the docstring into its components."
    result = parse(docstring)
    print(result)
    docstring = "Parse the docstring into its components.\n\n"
    result = parse(docstring)
    print(result)


if __name__ == '__main__':
    test_parse()
    # print(parse.__doc__)

# Generated at 2022-06-13 19:43:18.786438
# Unit test for function parse
def test_parse():
    docstring = \
"""Summary line.

    Extended description.

:param arg1: Description of `arg1`
:param arg2: Description of `arg2`
:type arg1: str
:type arg2: int
:returns: Description of return value
:rtype: bool
"""
    answer = parse(docstring)
    assert answer.short_description == "Summary line."
    assert answer.long_description == "\nExtended description.\n"
    assert answer.meta["arg1"].description == "Description of `arg1`"
    assert answer.meta["arg2"].description == "Description of `arg2`"
    assert answer.meta["arg1"].type_name == "str"
    assert answer.meta["arg2"].type_name == "int"

# Generated at 2022-06-13 19:43:27.164977
# Unit test for function parse
def test_parse():
    text = """The main parsing routine.

:param text: docstring text to parse
:param style: docstring style
:returns: parsed docstring representation
:raises: Exception for assert
    """
    result = parse(text)
    assert(len(result.summary) == 2)
    assert(isinstance(result.meta, dict))
    assert(result.meta.get('params') == ['text', 'style'])
    assert(result.meta.get('returns') == ['parsed docstring representation'])
    assert(result.meta.get('raises') == ['Exception for assert'])


# Generated at 2022-06-13 19:43:30.991628
# Unit test for function parse
def test_parse():
    # This is a normal test case
    input_string = 'This is a normal test case'
    target_string = 'This is a normal test case'
    assert parse(input_string) == target_string

# Generated at 2022-06-13 19:43:36.464505
# Unit test for function parse
def test_parse():
  t = parse("This is an introduction")
  assert t.meta == None
  assert t.summary == 'This is an introduction'
  assert t.fields == ' '
  assert t.raises == None
  assert t.params == None
  assert t.returns == None
  assert t.yields == None

# Generated at 2022-06-13 19:43:44.937422
# Unit test for function parse
def test_parse():
    import pytest
    text = '''
    Test function.
    
    :param arg1: First argument
    :type arg1: str
    :param arg2: Second argument
    :type arg2: int
    :returns: something
    :rtype: str
    :raises Exception: Some exception
    :raises TypeError: Another exception
    '''

# Generated at 2022-06-13 19:43:46.794526
# Unit test for function parse
def test_parse():
    assert parse(__doc__).short_description == "The main parsing routine."

# Generated at 2022-06-13 19:43:57.384300
# Unit test for function parse
def test_parse():
    assert str(parse("""\
    This is a test function.

    This function does nothing.

    :param int a: first parameter
    :param str b: second parameter
    :returns: return value
    """)) == """\
This is a test function.

This function does nothing.

:param int a: first parameter
:param str b: second parameter
:returns: return value
:rtype: None"""

# Generated at 2022-06-13 19:44:02.883618
# Unit test for function parse
def test_parse():
    docstring = '''
    This is a test.
    '''
    print(parse(docstring))

# Generated at 2022-06-13 19:44:08.955626
# Unit test for function parse
def test_parse():
    docstring = parse('''
    Returns a minimal Docstring instance.

    :param arg0: the first argument
    :param arg1: the second argument
    :returns: the return value
    :raises AttributeError: if something bad happens
    ''')

    assert_equal(1, len(docstring.meta))
    assert_equal(1, len(docstring.meta['returns']))
    assert_equal(2, len(docstring.params))
    assert_equal(1, len(docstring.raises))



# Generated at 2022-06-13 19:44:11.755343
# Unit test for function parse
def test_parse():
    docstring = """
    Args:
        param1: The first parameter.
        param2: The second parameter.
    Returns:
        True if successful, False otherwise.
    """

    assert parse(docstring)


# Generated at 2022-06-13 19:44:19.376912
# Unit test for function parse
def test_parse():
    """Test the main parsing function.
    
    Fail: Parsed result doesn't have the right format."""
    docstring = """
    This is a docstring.
    
    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.
    param3 : :obj:`list` of :obj:`str`
        The third parameter.
    
    Returns
    -------
    bool
        The return value. True for success, False otherwise.
    
    Raises
    ------
    AttributeError
        The ``Raises`` section is a list of all exceptions
        that are relevant to the interface.
    KeyError
        When a key error is encountered.
    """
    #print(parse(docstring).returns)
    #print(parse(docstring).parameters)

# Generated at 2022-06-13 19:44:32.198151
# Unit test for function parse
def test_parse():
    text = '''\
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
        Description of return value

    '''
    docstring = parse(text)
    assert docstring.summary == 'Summary line.'
    assert len(docstring.description) == 2
    assert docstring.description[0] == 'Extended description.'
    assert docstring.description[1] == ''
    assert len(docstring.params) == 2
    assert docstring.params['arg1'].arg_type == 'int'
    assert docstring.params['arg1'].description == ['Description of arg1']
    assert docstring.params['arg2'].arg_type == 'str'
   

# Generated at 2022-06-13 19:44:36.126977
# Unit test for function parse
def test_parse():
    """
    GIVEN a docstring with good formatting
    WHEN parse() is called with text
    THEN verify that correct output is returned
    """
    text = "Test string with good parameters"
    ret = parse(text)
    assert ret == "Test string with good parameters"


# Generated at 2022-06-13 19:44:45.995403
# Unit test for function parse
def test_parse():
    docstring_text = """
    Single line description.

    Multiple line description

    single line description (Too short).

    Extended description
    extended description
    extended description

    Parameters
    ----------
    arg1 : str
        Description of `arg1`
    arg2 : int
        Description of `arg2`
    arg3 : tuple
        Description of `arg3`

    Returns
    -------
    dict
        Description of `arg3`
    """
    docs = parse(docstring_text)
    print(f"Description: {docs.short_description}\n{docs.long_description}")
    print(f"Arguments: {docs.arguments}")
    print(f"Keyword_arguments: {docs.keyword_arguments}")
    print(f"Return: {docs.returns}\n\n")

# Generated at 2022-06-13 19:44:54.717323
# Unit test for function parse
def test_parse():
    assert parse("", Style.google).summary == ""
    assert parse("example", Style.google).summary == "example"
    assert parse("example", Style.google).short_description == "example"
    assert parse("example\n".encode(), Style.google).summary == "example"
    assert parse("example\n", Style.google).summary == "example"
    assert parse("example\n\n").summary == "example"
    assert parse("example\n\n").short_description == "example"
    assert parse("example\n\n").long_description == ""
    assert parse("example\n\n", Style.numpy).summary == "example"
    assert parse("example\n\n", Style.numpy).short_description == "example"

# Generated at 2022-06-13 19:44:59.918944
# Unit test for function parse
def test_parse():
    DOCSTRING_STYLE = """
Usage:
    $ python[3] your_program.py (-h | --help | --version)
    $ python[3] your_program.py <input> [--type=<type>] [--output=<path>]

Options:
    -h --help        Show this screen.
    --version        Show version.
    --type=<type>    Type of input: yaml or json
    --output=<path>  Path of output file."""

    print(parse(DOCSTRING_STYLE))
    return

# Generated at 2022-06-13 19:45:00.911085
# Unit test for function parse
def test_parse():
    """Test function parse"""
    pass

# Generated at 2022-06-13 19:45:10.525879
# Unit test for function parse
def test_parse():
    text = '''
    Hello, world!
    :param test: test param
    :type test: str
    :return: test return
    :rtype: int
    '''
    style = Style.numpy

    assert str(parse(text, style)) == str(STYLES[style](text))

    if __name__ == '__main__':
        test_parse()

# Generated at 2022-06-13 19:45:22.785682
# Unit test for function parse
def test_parse():
    text = '''one line summary
    one line summary:

    Extended description

    Args:
        a: first argument
        b: second argument
    Returns:
        first return
        second return
    Raises:
        ValueError: if the input is not valid
    '''
    result = parse(text)
    assert result.short_description == 'one line summary'
    assert result.extended_description == 'Extended description'
    assert result.params == {'a': 'first argument', 'b': 'second argument'}
    assert result.returns == {'first return', 'second return'}
    assert result.raises == {'ValueError': 'if the input is not valid'}


# Generated at 2022-06-13 19:45:30.037520
# Unit test for function parse
def test_parse():
    import os
    import doctest
    doctest.testmod()
    docstring = open(os.path.expanduser('~/.vimrc'), 'r').read()
    proj_dir = '/home/sunfmin/Projects/python/docstring_parser'
    path = os.path.join(proj_dir, 'docstring_parser/parser.py')
    with open(path, 'r') as fh:
        docstring += fh.read()
    assert len(parse(docstring).meta) > 0
    return True

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:45:36.183483
# Unit test for function parse
def test_parse():
    text = """
    Function to parse docstrings.

    Parameters
    ----------
    text: str
        docstring text to parse
    style: docstring_parser.Style
        docstring style, defaults to docstring_parser.Style.auto

    Returns
    -------
    parsed docstring representation
    """
    expected = """<Docstring sections=[<Section: description: ['\n    Function to parse docstrings.']>, <Section: parameters: ['\n    text: str\n        docstring text to parse', '\n    style: docstring_parser.Style\n        docstring style, defaults to docstring_parser.Style.auto']>, <Section: returns: ['\n    parsed docstring representation']>]>"""
    assert str(parse(text)) == str(expected)

# Generated at 2022-06-13 19:45:45.504389
# Unit test for function parse
def test_parse():
    path = 'test/test.py'
    with open(path, 'r') as file:
        text = file.read()

    doc = parse(text)
    print(doc,'\n')
    assert doc.summary == "takes a string and reverses it"
    assert doc.description == "This is a long multiline description of this function. It goes on for quite a while. Hopefully it is long enough to pass the test."
    assert doc.positional == {'s': 'the string to reverse'}
    assert doc.keyword_only == {'quote': 'if true, reverse double quote characters'}
    assert doc.returns == "the reversed string"
    assert 'deprecated' in doc.meta
    assert doc.meta['deprecated'] == "use `reversed` instead"



# Generated at 2022-06-13 19:45:53.287142
# Unit test for function parse
def test_parse():
    """Parsing function for docstring."""
    from docstring_parser.styles import google
    text = """google
        Summary line.

        Extended description of function.

        Args:
            arg1 (int): Description of arg1
            arg2 (str): Description of arg2

        Returns:
            bool: Description of return value

        """
    docstring = parse(text, style="google")
    assert docstring.summary == 'Summary line.'
    assert len(docstring.params) == 2
    assert docstring.params['arg1'].type.name == 'int'
    assert docstring.params['arg1'].description == 'Description of arg1'

    # assert docstring.params['arg1'] == {'type' : 'int', 'description' : 'Description of arg1'}
    # assert docstring.params['

# Generated at 2022-06-13 19:46:04.666531
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Param, Return
    from docstring_parser.styles import Style

    docstring_text = '''
    Parametrized constructor.

    :param x: x
    :type x: int
    :param y: y
    :param z: z
    :return: x + y
    :rtype: int
    '''
    docstring = parse(docstring_text)
    assert isinstance(docstring, Docstring)
    assert docstring.short_description == 'Parametrized constructor.'
    assert docstring.long_description == ''

# Generated at 2022-06-13 19:46:15.390627
# Unit test for function parse
def test_parse():
    from docstring_parser.auto_style import parse as auto_parser
    from docstring_parser.google_style import parse as google_parser
    from docstring_parser.numpy_style import parse as numpy_parser

    assert parse('\n'.join(['Hello', 'Docstring!', '']), style=Style.auto)  # auto
    assert parse('\n'.join(['Hello', 'Docstring!', '']), style=Style.auto) == auto_parser('\n'.join(['Hello', 'Docstring!', '']))
    assert parse('\n'.join(['Hello', 'Docstring!', '']), style=Style.auto) == google_parser('\n'.join(['Hello', 'Docstring!', '']))

# Generated at 2022-06-13 19:46:26.452748
# Unit test for function parse
def test_parse():
    assert parse('''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

    :param int arg1: the first argument
    :param arg2: the second argument
    :type arg2: str

    :returns: description of return value
    :rtype: int
    ''')

    assert parse('''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

    @param arg1 the first argument
    @type arg1 int
    @param arg2 the second argument
    @type arg2 str
    @return description of return value
    @rtype int
    ''')

# Generated at 2022-06-13 19:46:37.255838
# Unit test for function parse
def test_parse():
    text = '''Single line summary.

    Extended description.

    Some bold text. Some italic text. Some inline code: "foo".
    Some block code::

        print('bar')

    Parameters
    ----------
    arg1
        description of arg1
    arg2
        description of arg2
    '''
    d = parse(text)
    print(text)
    print(d)
    print(d.meta['summary'])
    print(d.meta['description'])
    print('{} inlines'.format(len(d.meta['inlines'])))
    print('{} code blocks'.format(len(d.meta['code_blocks'])))
    print('{} params'.format(len(d.meta['params'])))
    print(len(d.meta))
    #print(d.meta)


# Generated at 2022-06-13 19:46:47.510118
# Unit test for function parse
def test_parse():
    doc_text = """This is a function.
    :param name: name of the person
    :param age: age of the person
    :return: something
    """
    doc_components = parse(doc_text)
    print(doc_components.description)
    print(doc_components.params)
    print(doc_components.returns)


# Generated at 2022-06-13 19:46:59.076474
# Unit test for function parse
def test_parse():
    """Test the parse function"""
    docstring_text = 'Test Doc string for function test_parse'
    result = parse(docstring_text)
    assert result.summary == 'Test Doc string for function test_parse'
    assert result.description == ''
    assert result.extended_summary == ''
    assert result.params == {}
    assert result.returns == {}
    assert result.raises == {}
    assert result.yields == {}
    assert result.meta == {}
    assert result.examples == {}
    assert result.notes == {}
    assert result.see_also == {}
    assert result.references == {}
    assert result.todo == {}


# Generated at 2022-06-13 19:47:06.125517
# Unit test for function parse
def test_parse():
    '''Test function parse'''
    text = '''This is the function description.
    Args:
        arg1: 1-D Tensor with type keyword arg.
        arg2: 2-D Tensor with dtype keyword arg.
    Return:
        ret: 1-D Tensor with shape and dtype keyword args.
    '''

    obj = parse(text)

    _validate_function(obj)


# Generated at 2022-06-13 19:47:17.770389
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Docstring, ParseError
    # Test for auto
    doc = '''
        Example function with types documented in the docstring.

        :param :class:`int` a: The operaand
        :param b: The second operand
        :returns: The sum of the two parameters
    '''
    print(parse(doc))
    # Test for numpy
    try:
        parse(doc, style="numpy")
    except ParseError as e:
        print("ParseError", e)
    # Test for google
    try:
        parse(doc, style="google")
    except ParseError as e:
        print("ParseError", e)
    # Test for sphinx

# Generated at 2022-06-13 19:47:26.039712
# Unit test for function parse
def test_parse():
    text = """
        This function does something.
        :param Dataset dataset: Dataset to be converted.
        :param Saver saver: saver function.
        :param str save_dir: directory to store dataset
        :returns: converted dataset.
    """
    docstring = parse(text)
    assert(len(docstring.meta) == 3)
    assert(docstring.meta[0].args == 'Dataset dataset')
    assert(docstring.meta[1].args == 'Saver saver')
    assert(docstring.meta[2].args == 'str save_dir')



# Generated at 2022-06-13 19:47:34.892716
# Unit test for function parse
def test_parse():
    from docstring_parser import parse
    from docstring_parser.styles import GoogleStyle, NumpyStyle

    docstring = (
        "A sample function with types documented in the docstring.\n"
        "    "
        "Args:\n"
        "    arg1 (int): The first argument.\n"
        "    arg2 (str): The second argument.\n"
        "    "
        "Returns:\n"
        "    bool: The return value. True for success, False otherwise.\n"
    )

    result = parse(docstring)
    assert isinstance(result, GoogleStyle)
    assert result.summary == "A sample function with types documented in the docstring."
    assert result.description == ""
    assert len(result.args) == 2
    assert len(result.returns) == 1

    doc

# Generated at 2022-06-13 19:47:39.517207
# Unit test for function parse
def test_parse():
    from pprint import pprint
    from docstring_parser.styles import Google
    pprint(parse("""This is a module docstring."""))
    pprint(parse("""This is a module docstring.""", style=Google))

# Generated at 2022-06-13 19:47:48.721489
# Unit test for function parse
def test_parse():
    code1 = '''
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    '''
    code2 = '''
    @param text: docstring text to parse
    @param style: docstring style
    @returns: parsed docstring representation
    '''
    code3 = '''
    Parameters
    ----------
    text: docstring text to parse
    style: docstring style
    Returns
    -------
    parsed docstring representation
    '''
    texts = [code1, code2, code3]
    try:
        for text in texts:
            output = parse(text).__str__()
            assert output == text, "Unit test for function parse failed."
    except AssertionError as e:
        print(e)

test_

# Generated at 2022-06-13 19:47:53.392267
# Unit test for function parse
def test_parse():
    text = """
       Keyword arguments:
         value: description
         value2: description2
    """
    result = parse(text, style=Style.google)
    assert result.meta[0].keyword == 'value'


# Generated at 2022-06-13 19:48:01.448212
# Unit test for function parse
def test_parse():
    text = '''
        Remove the first occurrence of *value*. If *value* is not a member of
        the list, it raises a ``ValueError``.

        The returned value is the removed item.

        The operation is performed in ``O(n)`` time where ``n`` is the length of
        the list.'''

    doc = parse(text)
    assert doc.short_description == "Remove the first occurrence of *value*."

# Generated at 2022-06-13 19:48:16.421877
# Unit test for function parse
def test_parse():
    text= """Return a tuple of information about the file (name, type, encoding,
lines) or, the object passed as a parameter, i.e. 
return a tuple (object, 0) or raise a TypeError if the object is not a 
readable and seekable file, or raise a ValueError if the object has 
no attribute named "name". If the optional argument name is not given, 
the filename is taken from the first line of the file, the "shebang" line. 
If the optional argument line is not given, the line number is taken from 
the second line of the file, the "coding" line."""

    style = Style.auto
    style1 = Style.numpy
    style2 = Style.google
    style3 = Style.aalto

    # print(parse(text, style))

# Generated at 2022-06-13 19:48:28.295127
# Unit test for function parse
def test_parse():
    doc = parse('''
    Hello world.
    :param arg1: This is argument 1.
    :param arg2: This is argument 2.
    :return: A string.''',style = Style.sphinx)
    assert doc.content[0][0] == 'Hello world.'
    assert doc.params[0].arg_name == 'arg1'
    assert doc.params[1].arg_name == 'arg2'
    assert doc.returns.desc[0] == 'A string.'
    assert doc.summary() == 'Hello world.'



# Generated at 2022-06-13 19:48:39.853525
# Unit test for function parse
def test_parse():
    text = '''\
This is a one-line summary.

This is a multi-line overview.

:param name: the name of a person
:type name: str

:param age: person's age
:type age: int
:default age: 0
:raises ValueError: if age is less than 0

:returns: a boolean value
:rtype: bool

:keyword address: the address of a person
:type address: str
:default address: ""

This is a one-line conclusion.
'''

    docstring = parse(text, style=Style.numpy)

# Generated at 2022-06-13 19:48:42.038032
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    assert parse.__doc__


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:48:49.252207
# Unit test for function parse
def test_parse():
    from docstring_parser.tests.test_data import (
        simple_example_1,
        simple_example_2,
        simple_example_3,
    )
    parsed_example_1 = parse(simple_example_1, Style.google)
    parsed_example_2 = parse(simple_example_2, Style.google)
    parsed_example_3 = parse(simple_example_3, Style.google)

    assert parsed_example_1.short_description == 'Parses epydoc docstrings.'
    assert parsed_example_2.returns is None
    assert parsed_example_3.short_description == ''


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:48:51.137720
# Unit test for function parse
def test_parse():
    parse()

# Generated at 2022-06-13 19:48:52.416710
# Unit test for function parse
def test_parse():
    assert parse("Hello, world.") == parse("Hello, world.")



# Generated at 2022-06-13 19:49:02.413831
# Unit test for function parse
def test_parse():
    text = '''
    [Hello, world](example.com)
    ======
    :param b: A byte string.
    :param c: A unicode string.
    :param i: An integer.
    :param f: A float.
    :param l: A list.
    :param t: A tuple.
    :param d: A dictionary.
    :param bs: A byte string (no coercion).
    :param us: A unicode string (no coercion).
    '''
    s = parse(text)
    assert s.short_description == 'Hello, world'
    assert s.long_description == '======'

# Generated at 2022-06-13 19:49:05.351439
# Unit test for function parse
def test_parse():
    text = '''
    """
    This is a function testing function parse
    """
    '''
    docstring = parse(text)
    assert docstring.short_description == "This is a function testing function parse"

# Generated at 2022-06-13 19:49:09.846493
# Unit test for function parse
def test_parse():
    def test_func():
        """This is a test function.

        :param arg1: the first argument
        :param arg2: the second argument

        Keyword Args:
            kwarg1: the first keyword argument
            kwarg2: the second keyword argument

        Examples:
            >>> print(1)
            1
        """

    result = parse(test_func.__doc__)
    assert isinstance(result, Docstring)


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:49:22.223327
# Unit test for function parse
def test_parse():
    doc = """
    This is a module docstring.

    Some text.

    :param alpha: first parameter
    :type alpha: int
    """
    parsed = parse(doc)

    assert parsed.summary == 'This is a module docstring.'
    assert str(parsed.description) == 'Some text.'

    # Test the meta block
    assert parsed.description.meta[0].name == 'param'
    assert str(parsed.description.meta[0].value) == 'first parameter'
    assert parsed.description.meta[0].type == 'int'
    assert parsed.description.meta[0].tags[0].tag == 'param'
    assert str(parsed.description.meta[0].tags[0].value) == 'alpha'

# Generated at 2022-06-13 19:49:32.126234
# Unit test for function parse
def test_parse():
	docstring = """


		This is a test docstring.

		:param ReturnVal: The return value of the function.
		:param ParamVal: Accepts a parameter value.

		:example:

			This is the example
			Defined in the docstring.

		:return: [value, value * 2]

		"""
	parsed_docstring = parse(docstring)
	assert parsed_docstring.short_description == "This is a test docstring."
	assert parsed_docstring.long_description.strip() == ""
	assert parsed_docstring.meta['ParamVal'][0] == "Accepts a parameter value."
	assert parsed_docstring.meta['ReturnVal'][0] == "The return value of the function."
	assert parsed_docstring.returns.strip()

# Generated at 2022-06-13 19:49:36.437499
# Unit test for function parse
def test_parse():
    assert parse('"""Hello World"""') == Docstring('Hello World')


if __name__ == "__main__":
    main()

# Generated at 2022-06-13 19:49:50.592585
# Unit test for function parse
def test_parse():
    from pprint import pprint
    """docstring_parser.parse test
    """
    text = """\
        This is a summary line.

        Args:
            description¶
            is a multiline description
            this is the third line
        Returns:
            description¶
            is a multiline description
            this is the third line
        Raises¶
            KeyError, ValueError
        """
    docstring = parse(text)
    pprint(docstring)
    d = vars(docstring)
    assert d['summary'] == 'This is a summary line.'
    assert d['args']['description']['description'] == 'is a multiline description\nthis is the third line'

# Generated at 2022-06-13 19:49:58.214382
# Unit test for function parse
def test_parse():
    text = """
        Description of function.

        Args:
            arg0: first argument.
            arg1: second argument.

        Returns:
            nothing
        """

    d = parse(text)
    assert d.short_description == 'Description of function.'
    assert len(d.args) == 2
    assert 'arg1' in d.args
    assert d.args['arg1'] == 'second argument.'
    assert len(d.returns) == 1
    assert d.returns[0].description == 'nothing'

# Generated at 2022-06-13 19:50:03.699528
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Docstring
    from docstring_parser.styles import STYLES
    assert isinstance(parse('a'), Docstring)
    assert parse('a').summary == 'a'
    assert len(parse('A\nB').meta) == 0
    assert len(parse('a', style='numpy').meta) == 1



# Generated at 2022-06-13 19:50:05.581760
# Unit test for function parse
def test_parse():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:50:13.351668
# Unit test for function parse
def test_parse():
    from docstring_parser.utils import parse_docstring
    d1 = """Single line docstring."""
    docstring = parse_docstring(d1)
    assert isinstance(docstring, Docstring)
    assert len(docstring.meta) == 1
    assert docstring.meta == ['Single line docstring.']

    d2 = """Multiline
    docstring."""
    docstring = parse_docstring(d2)
    assert isinstance(docstring, Docstring)
    assert len(docstring.meta) == 1
    assert docstring.meta == ['Multiline\ndocstring.']


# Generated at 2022-06-13 19:50:25.998819
# Unit test for function parse

# Generated at 2022-06-13 19:50:34.189698
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Return, Parameter
    from docstring_parser.styles import GoogleStyle

    text = '''
    :param a: This is A
    :param b: This is B
    :param c: This is C
    :returns: This is D
    '''

    docstring = parse(text, style=GoogleStyle)
    assert docstring.params['a'].type_name == Parameter.empty
    assert docstring.params['a'].description == 'This is A'
    assert docstring.params['b'].type_name == Parameter.empty
    assert docstring.params['b'].description == 'This is B'
    assert docstring.params['c'].type_name == Parameter.empty
    assert docstring.params['c'].description == 'This is C'

# Generated at 2022-06-13 19:50:45.205342
# Unit test for function parse
def test_parse():
    docstring = '''"""This module implements the core of the parser and
                    ast transformer."""
'''
    #print(parse(docstring))
    assert parse(docstring) == {'__package__': '', '__name__': 'parser', '__doc__': 'This module implements the core of the parser and ast transformer.', '__all__': []}

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:50:48.233720
# Unit test for function parse
def test_parse():
    docstr = "This docstring for function parse"
    style = Style.google
    assert parse(text=docstr, style=style) == 'This docstring for function parse'

# Generated at 2022-06-13 19:50:54.856614
# Unit test for function parse
def test_parse():
    """test_parse"""
    text = '''\
        docstring_parser.py
        
        This is a test module

        """parse(text: str, style: Style = Style.auto) -> Docstring:
            Parse the docstring into its components.
        
            :param text: docstring text to parse
            :param style: docstring style
            :returns: parsed docstring representation
        
            """
        '''
    style = Style.auto
    parse(text=text,style=style)

# Generated at 2022-06-13 19:51:07.503289
# Unit test for function parse

# Generated at 2022-06-13 19:51:17.940348
# Unit test for function parse
def test_parse():
    """docstring for test_parse"""
    text = """
    aaa
    bbb
    """
    assert parse(text, style=Style.google) == Docstring(summary='aaa',
                                                        description='bbb',
                                                        returns=(None, None),
                                                        raises=(), args=[])
    assert parse(text, style=Style.numpy) == Docstring(summary='aaa',
                                                       description='bbb',
                                                       returns=(None, None),
                                                       raises=(), args=[])
    assert parse(text, style=Style.auto) == Docstring(summary='aaa',
                                                      description='bbb',
                                                      returns=(None, None),
                                                      raises=(), args=[])