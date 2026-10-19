

# Generated at 2022-06-13 19:41:37.345127
# Unit test for function parse
def test_parse():
    """
    Tests the parse function.
    """

    # Setup
    text_good = """\
        Performs some function.

        :param arg1: first arg (this is the same line)
        :type arg1: int
        :param arg2: second arg
        :type arg2: str
        :returns: None
        :rtype: bool
        """
    text_bad = """\
        Performs some function.

        :param arg1: first arg
        :param arg2: second arg
        :returns: None
        :rtype: bool
        """

    # Test 1: valid text
    docstring = parse(text_good)
    assert type(docstring) == Docstring
    assert docstring.short_description == "Performs some function."
    assert len(docstring.long_description) == 0

# Generated at 2022-06-13 19:41:46.459851
# Unit test for function parse
def test_parse():
    docstring = '''A small sentence.

    A longer definition.

    Parameters:
        foo (str): the foo parameter.
        bar (str): the bar parameter.

    Returns:
        str: the return value.
    '''

# Generated at 2022-06-13 19:41:54.883429
# Unit test for function parse
def test_parse():
    docstring = ("Properties defined here:"
                "\n\n    author -- who created this class"
                "\n    version -- version of last change"
                "\n"
                "\n    AUTHOR -- all caps version of author"
                "\n"
                "\n"
                "\n    def method1(self, a=1, b=2):"
                "\n        \"\"\"Do nothing, but document it.\"\"\""
                "\n        pass"
                "\n"
                "\n    def method2(self, c, d):"
                "\n        \"\"\"And so is this.\"\"\""
                "\n        return c + d")
    x = parse(docstring, style=Style.numpy)

# Generated at 2022-06-13 19:42:00.788552
# Unit test for function parse
def test_parse():
    import textwrap

    doc = """
    :param int param1: the first parameter
    :param param2: the second parameter
    :returns: description of the return value
    :raises keyError: goes here
    """
    parsed = parse(textwrap.dedent(doc))

    assert parsed.params[0].arg_name == 'param1'
    assert parsed.params[0].description == 'the first parameter'

    assert parsed.params[1].arg_name == 'param2'
    assert parsed.params[1].description == 'the second parameter'

    assert parsed.returns.description == 'description of the return value'

    assert parsed.exceptions[0].type == 'keyError'
    assert parsed.exceptions[0].description == 'goes here'

# Generated at 2022-06-13 19:42:10.446573
# Unit test for function parse
def test_parse():
    f = open('testcases.txt','r')
    lines = f.readlines()
    d = {}
    l = []
    for i in range(0,len(lines)):
        if i % 5 == 0:
            l.append(lines[i].replace('\n',''))
        elif i % 5 == 1:
            l.append(lines[i].replace('\n',''))
        elif i % 5 == 2:
            l.append(lines[i].replace('\n',''))
        elif i % 5 == 3:
            l.append(lines[i].replace('\n',''))
        elif i % 5 == 4:
            l.append(lines[i].replace('\n',''))
            d[i] = l
            l = []
    f.close()


# Generated at 2022-06-13 19:42:24.482296
# Unit test for function parse
def test_parse():
    text = '''Summary line. This is a long summary.

This is the first paragraph of the body.

This is the second.

Parameters
----------
arg1 : int
    Description of `arg1` goes here.
arg2 : str
    Description of `arg2` goes here.

Returns
-------
int
    returns : int

Raises
------
ValueError
    raises: ValueError
'''

    docstring = parse(text)
    assert docstring.short_description == 'Summary line.'
    assert docstring.long_description == 'This is a long summary.\n\n' \
    'This is the first paragraph of the body.\n\n' \
    'This is the second.'
    assert docstring.returns is not None
    assert docstring.returns.arg_name == 'int'


# Generated at 2022-06-13 19:42:31.633306
# Unit test for function parse
def test_parse():
    # test parse
    import doctest
    doctest.testmod()
    docstring = """One line summary.

    Extended description.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Raises:
        ValueError: If `bar` is not `'baz'`

    Returns:
        bool: Description of return value

    """
    parsed = parse(docstring)
    print(parsed)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:42:33.389496
# Unit test for function parse
def test_parse():
    assert parse('hello_world()', Style.auto) == style.parse(text)


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:42:42.583278
# Unit test for function parse
def test_parse():
    s = """Summary line.\n
    Extended description.\n
    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.
    Returns:
        bool: The return value. True for success, False otherwise.
    """
    docstring = parse(s)
    assert docstring.short_description == 'Summary line.'
    assert docstring.long_description == \
        'Extended description.'
    assert docstring.returns.args == 'bool'
    assert docstring.returns.desc == 'The return value. True for success, False otherwise.'
    assert docstring.params[0].args == 'param1'
    assert docstring.params[0].desc == 'The first parameter.'
    assert docstring.params[1].args == 'param2'
    assert docstring.params

# Generated at 2022-06-13 19:42:44.949528
# Unit test for function parse
def test_parse():
    from docstring_parser import parse
    text = 'This is a test sentence.'
    doc = parse(text)
    assert doc.short_description == 'This is a test sentence.'

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:42:54.864357
# Unit test for function parse
def test_parse():
    text1 = """
Attributes
----------
a : float
    Random attribute.
b : int
    Random integer.
"""
    assert parse(text1).meta['a'] == 'float'
    text2 = """
:param a: Random attribute.
:type a: float
:param b: Random integer.
:type b: int
"""
    assert parse(text2).meta['a'] == 'float'

if __name__ == '__main__':
    print('Executing doctest.')
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 19:42:56.654993
# Unit test for function parse
def test_parse():
    print(parse.__doc__)

# test_parse()

# Generated at 2022-06-13 19:43:04.103378
# Unit test for function parse
def test_parse():
    docstring = '''
    Return x raised to the power y.

    :param x: The base.
    :type x: :class:`int`, optional
    :param y: The exponent.
    :type y: :class:`int`, optional
    :returns: :data:`x` raised to the power :data:`y`.
    :rtype: :class:`float`
    '''
    doc = parse(docstring)
    assert doc.short_description == 'Return x raised to the power y.'
    assert doc.summary == doc.short_description
    assert doc.long_description == ''
    assert len(doc.params) == 2
    assert len(doc.returns) == 1
    assert doc.raises == []
    assert len(doc.see_also) == 0

# Generated at 2022-06-13 19:43:11.777356
# Unit test for function parse
def test_parse():
    doc = '''\
Title.

arg_1 -- param_1.

arg_2 -- param_2.

return -- specified output.
'''
    result = parse(style=Style.numpy, text=doc)
    assert result.meta == {
        'arg_1': 'param_1.',
        'arg_2': 'param_2.',
        'return': 'specified output.',
    }


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:43:18.029719
# Unit test for function parse
def test_parse():
    s = """
    This is a function to simulate normal distribution
    :param mu: mean of the distribution
    :param sigma: standard deviation of the distribution
    :returns: random generated number
    """
    d = parse(s)
    print(d.meta)
    assert d.meta['param']['mu'] == 'mean of the distribution'
    assert d.meta['param']['sigma'] == 'standard deviation of the distribution'
    assert d.meta['returns'] == 'random generated number'
    for k, v in d.meta.items():
        print(k, v)

# Generated at 2022-06-13 19:43:28.604544
# Unit test for function parse
def test_parse():
    docstring = """\
Short description.

Long description.

Args:
    arg1 (int): The first argument.
    arg2 (str): The second argument.

Returns:
    bool: The return value. True for success, False otherwise.

"""

# Generated at 2022-06-13 19:43:40.987707
# Unit test for function parse
def test_parse():
    text = """
    This is a function.
    
    :param x: X parameter
    :param y: Y parameter
    :returns: X+Y
    """
    pars = parse(text, Style.numpy)
    assert pars.summary == 'This is a function.'
    assert pars.description == ''
    assert pars.meta['Returns'] == ['X+Y']
    assert pars.meta['Param'] == ['X parameter', 'Y parameter']
    pars = parse(text, Style.google)
    assert pars.summary == 'This is a function.'
    assert pars.description == ''
    assert pars.meta['Returns'] == ['X+Y']
    assert pars.meta['Args'] == ['X parameter', 'Y parameter']



# Generated at 2022-06-13 19:43:49.706909
# Unit test for function parse
def test_parse():
    docstring = '''
    Foo bar.

    Args:
        first_arg (int): First argument.
        second_arg (str): Second argument.
    '''
    res = parse(docstring)
    assert res.long_description == 'Foo bar.'
    assert res.short_description == 'Foo bar.'
    assert len(res.params) == 2
    assert res.params[0].arg_name == 'first_arg'
    assert res.params[0].type_name == 'int'
    assert res.params[0].description == 'First argument.'
    assert res.params[1].arg_name == 'second_arg'
    assert res.params[1].type_name == 'str'
    assert res.params[1].description == 'Second argument.'
    assert res.returns is None
   

# Generated at 2022-06-13 19:43:59.773964
# Unit test for function parse
def test_parse():
    from docstring_parser.docstring import Docstring
    from docstring_parser.common import ParseError

    docstring = parse.__doc__
    assert isinstance(parse(docstring), Docstring)

    def func():
        """
        Args:
            arg1 (type1): doc1
        """

    assert isinstance(parse(func.__doc__, style=Style.numpy), Docstring)
    assert isinstance(parse(func.__doc__, style=Style.google), Docstring)

    try:
        parse(func.__doc__, style=Style.reST)
        assert False
    except ParseError:
        assert True


# Generated at 2022-06-13 19:44:01.801648
# Unit test for function parse
def test_parse():
    pass
    # TODO

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:44:13.223110
# Unit test for function parse
def test_parse():
    docstr = """
    Get some stuff from the DB.

    :param a: this is a
    :param b: this is b
    :returns: a thing
    """

    docstring = parse(docstr, style=Style.numpy)
    assert docstring.short_description == 'Get some stuff from the DB.'
    assert docstring.long_description == ''
    assert docstring.params[0].arg_name == 'a'
    assert docstring.params[0].description == 'this is a'
    assert docstring.params[1].arg_name == 'b'
    assert docstring.params[1].description == 'this is b'
    assert docstring.returns.description == 'a thing'
    assert docstring.raises == []

    docstring = parse(docstr, style=Style.google)


# Generated at 2022-06-13 19:44:15.873477
# Unit test for function parse

# Generated at 2022-06-13 19:44:29.275711
# Unit test for function parse
def test_parse():
    def f():
        """this is a docstring

        this is the first line,
        this is the second line.

        Args:
            arg1: the first argument
            arg2: the second argument, it is the best

        Returns:
            the return value

        Raises:
            ValueError: if something wrong happens
            IOError: if something else wrong happens

        .. versionadded:: 0.8
            Support to parse Google style docstrings as well.
        """


# Generated at 2022-06-13 19:44:35.864475
# Unit test for function parse
def test_parse():
    text = """Single line docstring.
    """
    actual = parse(text)
    assert actual.short_description == 'Single line docstring.'
    assert actual.long_description == ''
    assert actual.meta == {}

    text = """
    Single line docstring.
    """
    actual = parse(text)
    assert actual.short_description == 'Single line docstring.'
    assert actual.long_description == ''
    assert actual.meta == {}

    text = """
    Single line docstring.
    More information.
    """
    actual = parse(text)
    assert actual.short_description == 'Single line docstring.'
    assert actual.long_description == 'More information.'
    assert actual.meta == {}

    text = """
    Single line docstring.
    :param foo: parameter description
    """
    actual

# Generated at 2022-06-13 19:44:45.480494
# Unit test for function parse
def test_parse():
    example_docstring = """Short description.
Long description.
Args:
    first_arg (int): the first argument
    second_arg (str): the second argument
Returns:
    str: the return value
Raises:
    ValueError: if something bad happens"""

    expected_result = Docstring(
        short_description="Short description.",
        long_description="Long description.",
        params=[
            ("first_arg", "int", "the first argument"),
            ("second_arg", "str", "the second argument")
        ],
        returns=("str", "the return value"),
        exceptions=[("ValueError", "if something bad happens")])

    assert parse(example_docstring) == expected_result

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:44:50.758898
# Unit test for function parse
def test_parse():
    assert isinstance(parse("""Sphinx
===========
Sphinx is a tool that makes it easy to create intelligent and beautiful documentation.

It was originally created for the Python documentation, and it has excellent facilities for the documentation of software projects in a range of languages. 

Sphinx is a tool that makes it easy to create intelligent and beautiful documentation.

It was originally created for the Python documentation, and it has excellent facilities for the documentation of software projects in a range of languages.
"""), Docstring)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 19:44:51.341915
# Unit test for function parse
def test_parse():

    assert parse("description")


# Generated at 2022-06-13 19:44:57.210195
# Unit test for function parse
def test_parse():
    # test for parse()
    result = parse("""This is a module docstring""")
    assert result.summary == "This is a module docstring"

    # test for parse() if style is auto
    result = parse("""This is a module docstring""", style='numpy')
    assert result.summary == "This is a module docstring"

    # test for parse() if style is auto
    result = parse("""
    This is a module docstring
    """, style='autodetect')
    assert result.summary == "This is a module docstring"
    print('Unit test complete')

if __name__ == '__main__':
    test_parse()

# test/parse.py ends here

# Generated at 2022-06-13 19:45:03.781863
# Unit test for function parse
def test_parse():
    text = '''
        This function does something computing factorial

        Args:
            input (int): An integer

        Returns:
            int: The input factorialed.
    '''
    expected = Docstring(
        summary='This function does something computing factorial',
        description='',
        params=[
            Docstring.Param(name='input', type='int', description='An integer', default=None)
            ],
        returns=Docstring.Param(name='', type='int', description='The input factorialed.', default=None),
        meta={}
    )
    assert parse(text) == expected



"""The main function for cli module"""

import click

from docstring_parser.cli import main
from docstring_parser.docstring import Docstring
from docstring_parser.parsers import parse




# Generated at 2022-06-13 19:45:07.733630
# Unit test for function parse
def test_parse():
    docstring = '''This is a
    docstring.'''
    ret = parse(docstring)
    assert ret.summary == 'This is a\ndocstring.'
    assert ret.body == ''


# Generated at 2022-06-13 19:45:22.943435
# Unit test for function parse
def test_parse():
    text = """
    This is a sample docstring.
    This line is not a parameter.
    :param int arg1: The first argument.
    :returns: Nothing
    :raises ValueError: When the value is invalid.
    """
    d = parse(text)
    assert 'arg1' in d.params
    assert 'returns' in d.returns
    assert 'raises' in d.raises
    assert d.returns['returns'].type_name == 'None'
    assert d.raises['raises'].type_name == 'ValueError'
    assert d.summarize() == "This is a sample docstring."
    assert d.body == 'This line is not a parameter.\n'

# Generated at 2022-06-13 19:45:27.458104
# Unit test for function parse
def test_parse():
    text = """\
    Short summary.

    This function performs some operation.

    :param name: The name to use.
    :param state: Current state to be in.
    :raises: AttributeError, KeyError

    Extra content.
    """
    d = parse(text)
    print (d)

test_parse()

# Generated at 2022-06-13 19:45:37.722480
# Unit test for function parse
def test_parse():
    text = """This is a docstring.\n
              \n
              :param arg1: The first argument.
              :type arg1: int, optional
              :param arg2: The second argument.
              :type arg2: str, optional
              :raises KeyError: Raises an exception.
              :rtype: int
              \n
              """

# Generated at 2022-06-13 19:45:46.467950
# Unit test for function parse
def test_parse():
    # Case 1:
    s = "Maximize linear function subject to linear inequality constraints"
    print(s)
    print(parse(s))
    # Case 2:
    s = "Maximize a linear function subject to linear inequality constraints"
    print(s)
    print(parse(s))
    # Case 3:
    s = "Maximize a linear function subject to linear inequality constraints with bounds on some of the variables."
    print(s)
    print(parse(s))
    # Case 4:

# Generated at 2022-06-13 19:45:51.234453
# Unit test for function parse
def test_parse():
    style = Style.pep257
    text = '"""short description\nLong description.\n\n:param x: description of x\n:param y: description of y\n:returns: x + y\n"""'
    assert(str(parse(text, style)) == str(STYLES[style](text)))

# Generated at 2022-06-13 19:45:52.214410
# Unit test for function parse
def test_parse():
    assert parse('') == Docstring()

# Generated at 2022-06-13 19:45:58.499697
# Unit test for function parse
def test_parse():
    text = """    This is a docstring.

    This is the first line of a multi-line description.

    :param func: some function
    :type func: int
    :returns: description of what is returned
    """
    ret = parse(text, style=Style.pep257)
    print(ret)
    assert isinstance(ret, Docstring)


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:46:03.550043
# Unit test for function parse
def test_parse():
    assert parse("""
    Hello, world!

    :param a: the ``a`` parameter
    """) == Docstring(content='Hello, world!', meta={'param': {'a': {'description': 'the ``a`` parameter'}}})

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:46:14.539401
# Unit test for function parse
def test_parse():
    """
    >>> parse("test")
    Docstring([])

    >>> parse("test", style=Style.numpy) #doctest: +ELLIPSIS
    Docstring([...])

    >>> parse("test", style=Style.google) #doctest: +ELLIPSIS
    Docstring([...])

    >>> parse("test", style=Style.pep257) #doctest: +ELLIPSIS
    Docstring([...])

    >>> parse("test", style=Style.auto) #doctest: +ELLIPSIS
    Docstring([...])

    >>> parse("test", style=Style.auto) #doctest: +ELLIPSIS
    Docstring([...])
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 19:46:16.874494
# Unit test for function parse
def test_parse():
    assert(parse('test') is not None)

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:46:30.422791
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleDocstring, NumpyDocstring
    doc_string = '''
        Calculates the squared difference between two tensors.

    Args:
        tensor1 (Tensor): First input tensor
        tensor2 (Tensor): Second input tensor

    Returns:
        Tensor: The output tensor has the same shape as input
    '''
    docstring = parse(doc_string)
    assert isinstance(docstring, GoogleDocstring)
    assert len(docstring.meta) == 3
    assert docstring.meta['Args'][0]['name'] == 'tensor1'
    assert docstring.meta['Args'][1]['name'] == 'tensor2'
    assert len(docstring.params['Args']) == 2

# Generated at 2022-06-13 19:46:30.886456
# Unit test for function parse
def test_parse():
    pass

# Generated at 2022-06-13 19:46:35.914999
# Unit test for function parse
def test_parse():
    """Unit testing for parse function"""
    assert parse('a : int')
    assert parse('a : int\nb : str')
    assert parse('''a : int
        b : str''')
    assert parse('''a : int
            b : str
            c : str''')
    assert parse(''':param a: int''')
    assert parse(''':param a: int
        :param b: int''')

# Generated at 2022-06-13 19:46:42.310144
# Unit test for function parse
def test_parse():
    from docstring_parser.styles.numpy import NumpyDocstring
    from docstring_parser.styles.google import GoogleDocstring
    from docstring_parser.styles.sphinx import SphinxDocstring

    # good numpy
    numpy_example1 = '''
    numpy example

    :Author: Jacky Chen
    :Date: 20181211
    :param str name: My name
    :param int age: My age

    :Example:

    >>> print(age)
    23
    '''
    docstring = parse(numpy_example1, style=Style.numpy)
    if not isinstance(docstring, NumpyDocstring):
        raise TypeError('Type is not correct')
    if not docstring.author == ' Jacky Chen':
        raise ValueError('Author is not correct')

    # bad n

# Generated at 2022-06-13 19:46:51.120265
# Unit test for function parse
def test_parse():
    assert parse("test") == Docstring("test\n\n")
    assert parse("test", style=Style.sphinx) == Docstring("test\n\n")
    assert parse("test", style=Style.google) == Docstring("test\n\n")
    assert parse("test", style=Style.numpy) == Docstring("test\n\n")
    assert parse("test", style=Style.napoleon) == Docstring("test\n\n")

# Generated at 2022-06-13 19:46:55.525764
# Unit test for function parse
def test_parse():
    text = """import math\nfrom fractions import Fraction\ndef add(a: int, b: [int, Fraction]) -> str:\n    """
    output = parse(text)
    assert len(output.meta) == 2

# Generated at 2022-06-13 19:46:58.032391
# Unit test for function parse
def test_parse():
    params = "key1=value1, key2=value2, key3=value3"
    docstring = """Single line docstring."""
    assert parse(docstring) == parse(docstring, Style.numpy)


# Generated at 2022-06-13 19:47:06.126008
# Unit test for function parse
def test_parse():
    from docstring_parser.common import ParseError
    from docstring_parser.styles import Style, STYLES

    # Test Style.auto.
    for style in STYLES.keys():
        try:
            docstring = parse('test', style)
            assert isinstance(docstring, STYLES[Style.google])
        except ParseError as e:
            docstring = e
            assert not isinstance(docstring, STYLES[Style.google])

# Generated at 2022-06-13 19:47:17.769807
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    import os, sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    import docstring_parser
    lib_path = os.path.dirname(docstring_parser.__file__)
    with open(os.path.join(lib_path, "tests", "test_parse", "test_str.txt"), "r") as f:
        test_str = f.read()
    assert isinstance(test_str, str)
    docstr = parse(test_str)
    assert docstr.short_description == "blah, blah, blah"
    assert docstr.long_description == "blah, blah, blah"

# Generated at 2022-06-13 19:47:24.006913
# Unit test for function parse
def test_parse():
    line_length = 90
    text = '''
    Return a copy of the string with leading and trailing whitespace remove.
    If chars is given and not None, remove characters in chars instead.
    '''
    assert len(parse(text).short_description) <= line_length
    assert parse(text).short_description == 'Return a copy of the string with leading and trailing whitespace remove.'

# Tests for parse()
if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:47:35.886806
# Unit test for function parse
def test_parse():
    docstring = r'''Module documentation
    Variables:
        var1 - first variable
        var2 - second variable
'''
    doc_item = parse(docstring)
    assert doc_item.short_description == 'Module documentation'
    assert doc_item.long_description == ''
    assert doc_item.meta == {'Variable': [['', 'first variable'], ['', 'second variable']]}
    assert doc_item.style == Style.sphinx
    assert doc_item.tags == {}

    docstring = r'''Function returns True if condition is True
        :param cond: Condition to be checked
        :type cond: bool
        :rtype: bool
'''
    doc_item = parse(docstring)
    assert doc_item.short_description == 'Function returns True if condition is True'
    assert doc

# Generated at 2022-06-13 19:47:43.816136
# Unit test for function parse
def test_parse():
    text = '''
    :param int seed: Random seed
    :type seed: int
    :returns: random value
    :rtype: float
    '''
    docstring = parse(text)
    assert docstring.params == [{'name': 'seed', 'type': 'int', 'desc': 'Random seed'}]
    assert docstring.returns['type'] == 'float'
    assert docstring.returns['desc'] == 'random value'


# Generated at 2022-06-13 19:47:47.373103
# Unit test for function parse
def test_parse():
    # Common docstring format
    docstring = """
    This is a summary.

    This is a long description.
    """
    doc = parse(docstring)
    assert doc.short_descri

# Generated at 2022-06-13 19:47:58.486838
# Unit test for function parse
def test_parse():
    from docstring_parser.common import ParseError
    from docstring_parser.sphinx import parse as sphinx_parse

    assert parse("").to_dict() == sphinx_parse("")
    assert parse("No style").to_dict() == sphinx_parse("No style")

# Generated at 2022-06-13 19:48:09.642789
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Docstring, ParseError
    from docstring_parser.styles import STYLES, Style

    text = """Twos-complement integer addition.

    For example,
        >>> 3 + -2
        1
        >>> -3 + 2
        -1
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
        raise exc
    return sorted(rets, key=lambda d: len(d.meta), reverse=True)[0]

# Generated at 2022-06-13 19:48:13.107102
# Unit test for function parse
def test_parse():
    d = parse("""Summary line\n\n    Extended description\n\n""")
    assert d['summary'] == 'Summary line'
    assert d['extended_summary'] == 'Extended description'



# Generated at 2022-06-13 19:48:21.568876
# Unit test for function parse
def test_parse():
    test_input = """\
The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

Parameters
----------
one: int
    The first param.
two: int
    The second param.
three: int
    The third param.

Returns
-------
str
    The return value. True for success, False otherwise.
"""
    expected_output = {'Params': [('one: int', '\tThe first param.'), ('two: int', '\tThe second param.'), ('three: int', '\tThe third param.')], 'Return': 'str\n    The return value. True for success, False otherwise.', 'Name': 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'}

# Generated at 2022-06-13 19:48:33.232875
# Unit test for function parse
def test_parse():
    testcase = "Some dummy text for test"
    assert parse(testcase).body == testcase
    assert parse("").body == ""
    assert parse("").body == ""
    assert parse("\n\n").body == ""
    assert parse("\n\n").body == ""
    assert parse("\n\n").body == ""
    assert parse("\n\n").body == ""
    assert parse("\n\n").body == ""
    assert parse("\n\n").body == ""
    assert parse("\n\n").body == ""
    assert parse("\n\n").body == ""
    assert parse("\n\n").body == ""
    assert parse("\n\n").body == ""
    assert parse("\n\n").body == ""
    assert parse("\n\n").body == ""
   

# Generated at 2022-06-13 19:48:35.717194
# Unit test for function parse
def test_parse():
    """Test function parse."""
    parse("")

##
# API
##
__all__ = [
    "parse",
]

# Generated at 2022-06-13 19:48:37.924322
# Unit test for function parse
def test_parse():
    assert parse("")
    assert parse("asdf")
    assert parse("""
asdf
blah
""")


# Generated at 2022-06-13 19:48:49.406844
# Unit test for function parse
def test_parse():
    """Unit test for parse()"""
    assert parse("") == Docstring("", "", "", "", "", "", "", "", "", "")
    assert parse("a") == Docstring("a", "", "", "", "", "", "", "", "", "")
    assert parse("a\n\n") == Docstring("a", "", "", "", "", "", "", "", "", "")
    assert parse("a\n\nb") == Docstring("a", "", "b", "", "", "", "", "", "", "")
    assert parse("a\n\nb\n\nc") == Docstring("a", "", "b", "", "", "", "c", "", "", "")
    assert parse("a\n\nb\n\nc\n\n")

# Generated at 2022-06-13 19:48:54.769306
# Unit test for function parse
def test_parse():
  def foo():
    """Description
    :param p1: p1 description
    :type p1: int
    :param p2: p2 description
    :type p2: str
    :returns: 
    """
    return 'bar'
  assert parse(foo.__doc__).params['p1'].desc == 'p1 description'

# Generated at 2022-06-13 19:49:01.983222
# Unit test for function parse
def test_parse():
    text = """\
    Multiline header.

    Multiline description paragraph.

    Multiline description paragraph 2.

    Multiline description paragraph 3.

    Args:
        arg_1 (str): description of arg1

    Kwargs:
        kwarg_1 (str): description of kwarg1

    Returns:
        return_value (str): description of return value

    Raises:
        AttributeError: if attr not found
    """
    print(parse(text))


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:49:09.519557
# Unit test for function parse

# Generated at 2022-06-13 19:49:12.589890
# Unit test for function parse
def test_parse():
    text = """
    multi
    line
    docstring
    """
    assert isinstance(parse(text), Docstring)
    parse(text)

# Generated at 2022-06-13 19:49:21.631375
# Unit test for function parse
def test_parse():
    """The unit test for function parse."""
    from docstring_parser.styles import google

    text = ("This is a text.\n\n"
            "Args:\n"
            "    a: first argument\n"
            "    b: second argument\n"
            "    c: third argument\n")

    # Google style
    parsed = parse(text)
    assert type(parsed) is google.GoogleDocstring

    # Numpy style
    parsed = parse(text, Style.numpy)
    assert type(parsed) is STYLES[Style.numpy]

    # Default style
    parsed = parse(text, Style.default)
    assert type(parsed) is STYLES[Style.default]

    # Google style (auto)
    parsed = parse(text, Style.auto)
   

# Generated at 2022-06-13 19:49:31.709372
# Unit test for function parse
def test_parse():
    docstring = """Brief description.

Longer description.

:param arg1: Description of `arg1`.
:param arg2: Description of `arg2`, which has a type annotation.
:returns: Description of what is returned.
:raises AttributeError: If `arg2` is not supplied.
:raises SomeClassError: If `arg1` has an error.
"""
    assert(parse(docstring, Style.numpy).summary == "Brief description.")
    assert(parse(docstring, Style.numpy).description == "Longer description.")
    assert(parse(docstring, Style.numpy).returns == "Description of what is returned.")
    assert(parse(docstring, Style.numpy).raises == ["AttributeError", "If `arg2` is not supplied."])



# Generated at 2022-06-13 19:49:35.814262
# Unit test for function parse
def test_parse():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:49:46.098790
# Unit test for function parse
def test_parse():
    d = parse('Hello\n')
    assert d == Docstring(raw='Hello\n')

    d = parse('Hello\n\nWorld\n', style=Style.google)
    assert d == Docstring(
        summary='Hello',
        description='World',
        raw='Hello\n\nWorld\n')

    d = parse('* Hello\n* World\n', style=Style.numpy)
    assert d == Docstring(
        summary='Hello',
        extended_summary='World',
        raw='* Hello\n* World\n')


# Generated at 2022-06-13 19:49:48.544280
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    assert isinstance(parse('test docstring', Style.google), Docstring)

# Generated at 2022-06-13 19:49:58.802774
# Unit test for function parse
def test_parse():
    text = '''\
    This text is a description.

    :param str name: Name of user
    :return: json file
    '''
    style = Style.reStructuredText
    doc = parse(text, style)
    assert doc.short_description == 'This text is a description.'
    assert list(doc.params.keys()) == ['name']
    assert list(doc.params.values()) == ['Name of user']
    assert list(doc.returns.keys()) == []
    assert list(doc.returns.values()) == ['json file']

# Generated at 2022-06-13 19:50:07.715750
# Unit test for function parse
def test_parse():
    text = """
    This is the first line of the docstring
    and this is the second line.
    This is the last line.
    
    :param a: A parameter to the function
    :type a: list
    
    :Example:
    >>>
    """
    parsed = parse(text)
    assert parsed.short_description == "This is the first line of the docstring"
    assert parsed.long_description == """and this is the second line.\nThis is the last line."""
    assert parsed.meta['param']['a'].description == ['A parameter to the function']
    assert parsed.meta['param']['a'].type_name == ['list']
    assert parsed.meta['example'] == [['>>>']]

# Generated at 2022-06-13 19:50:16.768416
# Unit test for function parse
def test_parse():
    text = """
    One-line summary.

    Extended description.

    Args:
        arg1 (type): Description of arg1
        arg2 (type): Description of arg2

    Raises:
        Exception1: When things go wrong
        Exception2: When other things go wrong
    """

# Generated at 2022-06-13 19:50:28.588846
# Unit test for function parse
def test_parse():
    doc_string = \
    """
    :param param1: The first parameter.
    :param param2: The second parameter.
    :returns: The return value.
    :rtype: int
    """
    param_name = ['param1', 'param2']
    param_description = ['The first parameter.', 'The second parameter.']
    return_description = ['The return value.']
    return_type = ['int']

    
    expected_docstring = Docstring(
            meta = {
                'param_name': param_name, 
                'param_description':param_description, 
                'return_description':return_description, 
                'return_type':return_type
                }
            )
    actual_docstring = parse(doc_string)
    
    assert actual_docstring == expected_doc

# Generated at 2022-06-13 19:50:31.694881
# Unit test for function parse
def test_parse():
    docstring = """
    Parses docstring text into Docstring
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    assert parse(docstring, Style.sphinx)

# Generated at 2022-06-13 19:50:44.359708
# Unit test for function parse
def test_parse():
    assert parse('', Style.numpy) == Docstring(meta=[], content='')
    assert parse('a', Style.numpy) == Docstring(meta=[], content='a')
    assert parse('a\nb', Style.numpy) == Docstring(meta=[], content='a\nb')

    assert parse('a\n:c: _\n\nb', Style.numpy) == Docstring(meta=[{'c': '_'}], content='a\n\nb')

    assert parse('a\n:c: _\n:d: e\n\nb', Style.numpy) == Docstring(meta=[{'c': '_', 'd': 'e'}], content='a\n\nb')


# Generated at 2022-06-13 19:50:49.350072
# Unit test for function parse
def test_parse():
    #print(parse("""Test docstring. """))
    #print(parse("""Test docstring. \n """))
    st = """Test docstring. \n\tThis is a test. \n\n\tThis line should be ignored"
    """
    print(parse(st, 1))
    print(parse(st, 2))


# Generated at 2022-06-13 19:50:54.816787
# Unit test for function parse
def test_parse():
    ds = parse(r"""
    Title.

    Paragraph one.

    :param x: param x
    :returns: returns something
    :raises Exception: exception raised
    """)
    assert ds.meta['x'] == 'param x'
    assert ds.returns == 'returns something'
    assert ds.raises['Exception'] == 'exception raised'


# Generated at 2022-06-13 19:51:07.448546
# Unit test for function parse
def test_parse():
    text = """    A Sparse Array class.
    Supports arbitrary indices.
    Only stores non-zero entries.

    :param lines: number of lines in the matrix
    :type lines: long
    :param columns: number of columns in the matrix
    :type columns: long
    """
    ds = parse(text)
    assert ds.meta['param lines'] == 'number of lines in the matrix'
    assert ds.meta['type lines'] == 'long'
    assert ds.meta['param columns'] == 'number of columns in the matrix'
    assert ds.meta['type columns'] == 'long'
    assert ds.content[0] == 'A Sparse Array class.'
    assert ds.content[1] == 'Supports arbitrary indices.'

# Generated at 2022-06-13 19:51:18.568705
# Unit test for function parse
def test_parse():
    assert parse('') == Docstring(summary=None, description=None, tags=[], meta={})
    assert parse('Toto is a cool guy') == Docstring(summary='Toto is a cool guy', description=None, tags=[], meta={})
    assert parse('This function does this.\n') == Docstring(summary='This function does this.', description=None, tags=[], meta={})
    assert parse('This function does this.\n\nAnd more!\n') == Docstring(summary='This function does this.', description='And more!', tags=[], meta={})
    assert parse('This function does this.\n\nAnd more!\n', style='google') == Docstring(summary='This function does this.', description='And more!', tags=[], meta={})