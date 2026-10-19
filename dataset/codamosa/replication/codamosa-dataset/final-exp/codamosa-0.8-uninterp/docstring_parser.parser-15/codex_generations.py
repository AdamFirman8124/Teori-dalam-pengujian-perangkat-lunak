

# Generated at 2022-06-13 19:41:26.628938
# Unit test for function parse
def test_parse():
    text = "This is the module docstring\nwith multiple lines.\n"
    assert parse(text) == Docstring(description=('This is the module docstring\nwith multiple lines.', '', ''), meta={}, returns=None)

# Generated at 2022-06-13 19:41:39.023214
# Unit test for function parse
def test_parse():
    assert parse("") == Docstring(
        summary="",
        description="",
        args=[],
        kwargs=[],
        returns=None,
        yields=None,
        exceptions=[],
        meta={},
    )

    assert parse("one-line docstring") == Docstring(
        summary="one-line docstring",
        description="",
        args=[],
        kwargs=[],
        returns=None,
        yields=None,
        exceptions=[],
        meta={},
    )


# Generated at 2022-06-13 19:41:45.027165
# Unit test for function parse
def test_parse():
    text = '''
    Test test

    :param a: Test a
    :type a: str
    '''
    docstring = parse(text)
    assert isinstance(docstring, Docstring)
    assert docstring.short_description == 'Test test'
    assert len(docstring.long_description) == 0
    assert docstring.meta['parameters']['a']['type'] == 'str'

# Generated at 2022-06-13 19:41:54.142116
# Unit test for function parse
def test_parse():
    import os
    import textwrap
    from docstring_parser import parse
    from docstring_parser import styles
    from unittest import TestCase

    class ParseTestCase(TestCase):

        def test_parse_gflat(self):
            input_ = """
                @method
                @author Foo Bar <foo@bar.com>
                @param arg1 arg1 description
                @returns arg1
                @raises KeyError always
            """
            expected = """
                @method:
                @author: Foo Bar <foo@bar.com>
                @param arg1: arg1 description
                @returns: arg1
                @raise: KeyError always
            """
            docstring = parse(textwrap.dedent(input_), style=styles.gflat)

# Generated at 2022-06-13 19:42:00.503081
# Unit test for function parse
def test_parse():
    text = """
        This is a module docstring.

        :param message: message to log
        :type message: str
        :param logger: logger instance (optional)
        :type logger: logging.Logger
        """
    ds = parse(text, style=Style.pep257)
    assert ds.short_description == 'This is a module docstring.'
    assert ds.long_description == ''
    assert len(ds.meta) == 2
    assert ds.meta[0].args == ['message']
    assert ds.meta[0].description == 'message to log'
    assert ds.meta[0].annotation == 'str'
    assert ds.meta[1].args == ['logger']
    assert ds.meta[1].description == 'logger instance (optional)'

# Generated at 2022-06-13 19:42:07.591832
# Unit test for function parse
def test_parse():
    """Unit test for function parse."""
    return parse("""
    This is a docstring.
        - With a list.
        - Made of a few items.
    And an indented paragraph.

    :param x: First parameter.
    :type x: int
    :param y: Second parameter.
    :type y: str
    :returns: Something straightforward.
    :rtype: float
    :raises ValueError: When the value is invalid.
    """)


if __name__ == '__main__':
    print(test_parse())

# Generated at 2022-06-13 19:42:22.141073
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import Google, NumPy
    style = NumPy

# Generated at 2022-06-13 19:42:33.080276
# Unit test for function parse
def test_parse():
    docstring = """Summary line.

This is a multi-line summary. It should include a high-level
description of the function's purpose and should not be confused
with an abstract.

Parameters
----------
x : array_like
    A vector.
y : array_like
    Another vector.

Returns
-------
mag : float
    Vector magnitude.
"""
    parsed_docstring = parse(docstring, style='numpy')
    assert parsed_docstring.summary() == 'Summary line.'
    assert parsed_docstring.description() == 'This is a multi-line summary. It should include a high-level description of the function\'s purpose and should not be confused with an abstract.'
    assert len(parsed_docstring.params) == 2
    assert len(parsed_docstring.returns) == 1
    params = parsed_

# Generated at 2022-06-13 19:42:39.222766
# Unit test for function parse
def test_parse():
    import pytest
    example = """
    Args:
        arg1 (int): The first number.
        arg2 (int): The second number.
    Returns:
        The sum of the numbers.
    """
    result = parse(example)
    assert result.args == ['arg1 (int): The first number.',
                           'arg2 (int): The second number.']
    assert result.returns == ['The sum of the numbers.']


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 19:42:47.758595
# Unit test for function parse
def test_parse():
    docstring = '''"""Takes two numbers from the user and returns the sum.

    :param a: First number
    :param b: Second number
    :returns: Sum of the two numbers
    """'''
    res = parse(docstring)
    if res.short_description != 'Takes two numbers from the user and returns the sum.':
        raise Exception('Incorrect short description parsed')
    if res.long_description != '':
        raise Exception('Incorrect short description parsed')
    if len(res.meta) != 2:
        raise Exception('Incorrect meta parsed')
    if res.meta[0].key != 'param':
        raise Exception('Incorrect meta parsed')
    if res.meta[0].value != 'a: First number':
        raise Exception('Incorrect meta parsed')

# Generated at 2022-06-13 19:43:01.208005
# Unit test for function parse
def test_parse():
    text = '''
    This function does something.

    :param str x: a string argument
    :param int y: an integer argument
    :raises IOError: if the file cannot be written

    :returns: True if successful
    '''

    docstring = parse(text)
    assert docstring.summary == 'This function does something.'
    assert docstring.meta['x'] == 'a string argument'
    assert docstring.meta['y'] == 'an integer argument'
    assert docstring.raises['IOError'] == 'if the file cannot be written'
    assert docstring.returns == 'True if successful'

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:43:05.274955
# Unit test for function parse
def test_parse():
    parse('function description')
    parse('function description', style='pep257')
    parse('function description', style='google')
    parse('function description', style='numpy')
    parse('function description', style='auto')

test_parse()

# Generated at 2022-06-13 19:43:06.036389
# Unit test for function parse
def test_parse():
    """parse('the text')"""
    assert parse('the text') == 'the text'

# Generated at 2022-06-13 19:43:08.696240
# Unit test for function parse
def test_parse():
    doc = """This is a long description
of this function.
parameter:
    x: first parameter
    y: second parameter
return: a long description of what returns
this function does
a lot
of things but
not that much useful
    """
    assert parse(doc).short_description == 'This is a long description'
    assert parse(doc).short_description == 'This is a long description'

# Generated at 2022-06-13 19:43:18.014104
# Unit test for function parse
def test_parse():
    import re

    docstring = parse("""
    Summary line.

    Extended description.

    :param arg1: Description of arg1
    :type arg1: str
    :param arg2: Description of arg2
    :type arg2: int, optional
    :returns: Description of return value
    :rtype: bool
    :raises keyError: raises Exception
    """, style="numpy")

    assert docstring.short_description == "Summary line."
    assert docstring.long_description.strip() == "Extended description."
    assert docstring.returns == "Description of return value"
    assert docstring.returns_annotation == "bool"

# Generated at 2022-06-13 19:43:28.604361
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GoogleDocstring, NumPyDocstring

    def parse1():
        """
        1. Title line.

        First line after the title is considered as the first line
        of the description.

        Parameters:
            arg1 (int): Description of arg1
            arg2 (str): Description of arg2

        Returns:
            bool: Description of return value

        Raises:
            AttributeError: The ``Raises`` section is a list of all exceptions
                that are relevant to the interface.
            ValueError: If `param2` is equal to `param1`.
        """

        GoogleDocstring(text)
    parse1()


# Generated at 2022-06-13 19:43:41.952716
# Unit test for function parse
def test_parse():
    text = """
    測試機台程式碼

    Description:
    2D Scan

    Args:
        a (list): 兩維座標陣列
        b (list): 運行程式碼架構

    Returns:
        out (str): 流程結果
        code (str): 程式碼影像

    """
    assert parse(text, Style.numpy).description == "2D Scan"
    assert parse(text, Style.numpy).returns[0].type_name == "str"

# Generated at 2022-06-13 19:43:48.561450
# Unit test for function parse
def test_parse():
    """
    Unit test function for function parse.
    """
    parsed_docstring = parse('''This project is part of DOLFIN.

    DOLFIN is a software package for solving partial differential
    equations (PDEs) using the finite element method (FEM).
    ''')
    assert parsed_docstring.brief == 'This project is part of DOLFIN.'
    assert parsed_docstring.extended == "\nDOLFIN is a software package for solving partial differential\nequations (PDEs) using the finite element method (FEM)."

    parsed_docstring = parse('''Function.

    Parameters
    ----------
    u : Function
        Some function.
    mesh : UnitSquareMesh
        Some mesh.
    ''')
    assert parsed_docstring.brief == 'Function.'

# Generated at 2022-06-13 19:43:57.248869
# Unit test for function parse
def test_parse():
    """
    Test function parse
    """
    def f(x):
        """This is a test function.
        :param x: this is a param
        :return: this is a param
        """
        return x
    f.__doc__ = parse(f.__doc__, style=Style.google)
    assert(f.__doc__.summary == "This is a test function.")
    assert(len(f.__doc__.params) == 1 and f.__doc__.params[0].name == "x")

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:44:02.042908
# Unit test for function parse
def test_parse():
    txt = '''
    :param a:
    :type a: int
    :param b:
    :type b: str
    :returns:
    :rtype: int
    :raises Exception:
    '''
    ret = parse(txt)
    assert ret.params['a'] == 'int'
    assert ret.params['b'] == 'str'
    assert ret.return_type == 'int'


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:44:15.714859
# Unit test for function parse
def test_parse():
    text = """\
    Example docstring.

    Args:
        arg1 (int): The first value.
        arg2 (str): The second value.

    Returns:
        bool: The return value. True for success, False otherwise.

    """
    val = parse(text)
    assert val.short_description == "Example docstring."
    assert val.long_description == ""
    assert val.meta["Args"] == {"arg1": {"type": "int", "description": "The first value."},
                                "arg2": {"type": "str", "description": "The second value."}}
    assert val.meta["Returns"] == {"return": {"type": "bool", "description": "The return value. True for success, False otherwise."}}

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:44:21.737918
# Unit test for function parse
def test_parse():
    text = '''\
This function returns a float

        :param integer i: the value to square
        :param float f: the value to multiply by
        :raises ValueError: if i < 0
        :return: i*f
        :rtype: float
'''
    assert type(parse(text)) == Docstring


# Generated at 2022-06-13 19:44:32.613666
# Unit test for function parse
def test_parse():
    assert parse('').summary == ''
    assert parse('    ').summary == ''
    assert parse('\n    \n').summary == ''
    assert parse('\n\n').summary == ''
    assert parse('\n\n\n').summary == ''
    assert parse('\n\n\n\n').summary == ''

    d = parse('foo')
    assert d.summary == 'foo'
    assert d.description == ''
    assert d.meta == []
    assert d.raises == []
    assert d.returns == []
    assert d.other == []
    assert d.sections == []
    assert d.decorators == []

    d = parse('foo\nbar')
    assert d.summary == 'foo'
    assert d.description == 'bar'


# Generated at 2022-06-13 19:44:34.033941
# Unit test for function parse
def test_parse():
    docstring = """
    test function
    """
    parse(docstring)

# Generated at 2022-06-13 19:44:44.533090
# Unit test for function parse
def test_parse():
    ds = parse("""
    Text before
    Text after

    Parameters
    ----------
    arg1 : str
        The first argument.
    arg2 : int, optional
        The second argument.

    Returns
    -------
    str
        The return value.

    Other Parameters
    ----------------
    arg3 : list of ints
        Variable length list of integers.

    arg4 : {'spam', 'eggs'}, optional
        Items in collection.

    arg5 : str or None, optional
        The default is None.

    Yields
    ------
    int
        Next number.""")
    assert ds.short_description == 'Text before\nText after'
    assert ds.long_description == ''

# Generated at 2022-06-13 19:44:53.793275
# Unit test for function parse
def test_parse():
    assert parse("""\
        Short description

        Args:
          a: first argument
          b: second argument

        Returns:
          something

        Raises:
          ValueError: in case of error
    """) == Docstring(
        summary="Short description",
        description="",
        args={"a": "first argument", "b": "second argument"},
        returns="something",
        raises={"ValueError": "in case of error"},
        meta={},
    )


# Generated at 2022-06-13 19:45:03.093144
# Unit test for function parse
def test_parse():
	text = """\
	SUMMARY
		This is a simple test docstring I made.
		The purpose of this docstring is to test the parse function
		in the docstring_parser.py file.

	:param x: This is some sort of parameter
	:type x: int
	:param y: This is some sort of parameter
	:type y: int
	"""
	d = parse(text)
	assert d.summary == ["This is a simple test docstring I made.",
		"The purpose of this docstring is to test the parse function",
		 "in the docstring_parser.py file."]
	assert d.description == None
	assert d.meta["x"] == ["This is some sort of parameter"]
	assert d.meta["y"] == ["This is some sort of parameter"]
	return True

# Generated at 2022-06-13 19:45:14.017267
# Unit test for function parse
def test_parse():
    docstring_text1 = """
    Extract relevant info from a feature and a patient. Append this info to a dataframe.

    :param feature: name of the feature
    :param patient: patient object
    :param df: dataframe to append to
    :returns: df with added info
    """
    docstring_text2 = """
    Extract relevant info from a feature and a patient. Append this info to a dataframe.

    Args:
        param1 (type): description

    Returns:
        description

    Yields:
        type: description
    """
    # print(parse(docstring_text1, style=Style.numpy))
    print(parse(docstring_text2, style=Style.numpy))

if __name__ == "__main__":
    test_parse()

# Generated at 2022-06-13 19:45:23.250017
# Unit test for function parse
def test_parse():
    ds = 'This is a module docstring.'
    assert parse(ds) == Docstring(summary=ds)
    ds = '''This is a module docstring.

    - with a list
    - in it
    '''
    assert parse(ds) == Docstring(summary=ds)
    ds = '''This is a module docstring.

    This is a module docstring.
    '''
    assert parse(ds) == Docstring(summary=ds)
    ds = '''This is a module docstring.

    This is a module docstring.
    - with a list
    - in it
    '''
    assert parse(ds) == Docstring(summary=ds)

# Generated at 2022-06-13 19:45:32.171152
# Unit test for function parse
def test_parse():
    Meta = Docstring.Meta
    import re

    def meta_match(meta: Meta, *, args: list = None, returns: str = None):
        if args:
            assert meta.args
            for arg, arg_ in zip(meta.args, args):
                assert arg.name == arg_[0]
                if len(arg_) > 1:
                    assert re.match(arg_[1], arg.description)
        if returns:
            assert meta.returns
            assert re.match(returns, meta.returns.description)

    # line based
    s = """
    Parse the docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation

    test
    """

# Generated at 2022-06-13 19:45:45.843311
# Unit test for function parse
def test_parse():
	text = """This is a test docstring.
		
		Args:
		    arg1(int): The first value.
		    arg2(str): The second value.
		
		Returns:
		    str: The returned value.
		"""
	
	docstring = parse(text)
	
	print("This is a test docstring.",docstring.short_description)
	print("\n")
	print("The first value.\nThe second value.",docstring.long_description)
	
	for arg in docstring.args:
	    print("\n")
	    print("arg1(int)",arg.arg_name)
	    print("The first value.",arg.description)
	    
	for arg in docstring.args:
	    print("\n")
	   

# Generated at 2022-06-13 19:45:53.492454
# Unit test for function parse
def test_parse():
    text = '''
    Test docstring.

    This description should not be part of the parsed result.

    :param param1: The first parameter.
    :param param2: The second parameter.
    :return: The return value.
    :rtype: int
    :raises KeyError: The exception type.
    :raises ValueError: The exception type.
    '''
    docstring = parse(text)
    assert docstring.short_description == 'Test docstring.'
    assert docstring.long_description == ''
    assert docstring.returns.type_name == 'int'
    assert docstring.returns.description == 'The return value.'
    assert docstring.pos_args == []
    assert docstring.pos_arg_names == []
    assert docstring.kw_args == []
    assert docstring.kw

# Generated at 2022-06-13 19:46:04.844158
# Unit test for function parse
def test_parse():
    text = '''\
"""This is a description.

This is a description too.

:param param1: this is a param
:param param2: this is a second param
:returns: this is a return
:raises keyError: raises an exception
"""
'''
    docstring = parse(text)
    assert docstring.short_description == 'This is a description.'
    assert '\n\n'.join(docstring.long_description) == 'This is a description too.\n'
    assert list(docstring.params.keys()) == ['param1', 'param2']
    assert list(docstring.params.values()) == ['this is a param', 'this is a second param']
    assert docstring.returns == 'this is a return'

# Generated at 2022-06-13 19:46:14.942935
# Unit test for function parse
def test_parse():
    from docstring_parser import parse
    docstring = parse(
        """
        Short summary.

        Extended description.

        :param arg1: Description of arg1
        :param arg2: Description of arg2
        :returns: Description of return value
        :raises keyError: raises an exception
        """
    )
    assert docstring.short_description == "Short summary."
    assert docstring.extended_description == "Extended description."
    assert docstring.params["arg1"] == "Description of arg1"
    assert docstring.params["arg2"] == "Description of arg2"
    assert docstring.returns == "Description of return value"
    assert docstring.raises["keyError"] == "raises an exception"


# Generated at 2022-06-13 19:46:24.531577
# Unit test for function parse
def test_parse():
    text = '''\
        *sum*
        Sums two numbers and returns the result.

        :param a: first number
        :param b: second number
        :returns: sum of the two numbers
        '''
    d = parse(text)
    assert d.summary == 'Sums two numbers and returns the result.'
    assert d.meta['param'] == [
        ('a', 'first number'),
        ('b', 'second number')
    ]
    assert d.meta['returns'] == ['sum of the two numbers']

# Generated at 2022-06-13 19:46:33.217716
# Unit test for function parse
def test_parse():
    assert parse('') == Docstring('')

    text = "Return the Fibonacci sequence up to n"
    assert parse(text).content == text
    assert parse(text).meta == {}
    text = "Title with spaces"
    assert parse(text).content == text
    assert parse(text).meta == {}

    text = ":param x: The x param"
    assert parse(text).content == ''
    assert parse(text).meta == {'param': {'x': 'The x param'}}

    text = ":param int x: The x param"
    assert parse(text).content == ''
    assert parse(text).meta == {'param': {'type': 'int', 'x': 'The x param'}}

    text = ":param int x: The x param\n:return: The return value"
   

# Generated at 2022-06-13 19:46:37.558025
# Unit test for function parse
def test_parse():
    """Unit test for parse function"""

    from docstring_parser.styles import NumpyStyle as np
    from docstring_parser.styles import GoogleStyle as gs

    text = "Short description.\n\nLong description."

    assert(parse(text, style=Style.google) == gs(text))
    assert(parse(text, style=Style.numpy) == np(text))

# Generated at 2022-06-13 19:46:46.497101
# Unit test for function parse
def test_parse():
    doc = 'Parse the docstring into its components.'
    text = '''This is a test docstring.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    '''
    style = Style.auto
    text = parse(text,style)
    assert(text.short_description == doc)
    assert(text.params[0].arg_name == "text")
    assert(text.params[0].type_name == "")
    assert(text.params[1].arg_name == "style")
    assert(text.returns.type_name == "parsed docstring representation")
    # print(text.short_description)
    # print(text.long_description)
    # for i in range(text.params.__len__()):

# Generated at 2022-06-13 19:46:47.842419
# Unit test for function parse
def test_parse():
    assert isinstance(parse(""), Docstring)

# Generated at 2022-06-13 19:46:51.383904
# Unit test for function parse
def test_parse():
    from requests import get
    f = open('../../LICENSE')
    text = f.read()
    assert parse(text).summary

# Generated at 2022-06-13 19:46:56.552417
# Unit test for function parse
def test_parse():
    pass

# Generated at 2022-06-13 19:47:03.985233
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    text1 = '''This is description.
        :param arg1: This is argument 1
        :type arg1: str
        :param arg2: This is argument 2
        :type arg2: bool, optional
        :param arg3: This is argument 3
        :type arg3: int
        :returns: This is what is returned
        :rtype: str'''
    print(parse(text1))
    text2 = '''This is description.

        :param str arg1: This is argument 1
        :param list[str] arg2: This is argument 2
        :param bool arg3: This is argument 3
        :returns str: This is what is returned'''
    print(parse(text2))

# Generated at 2022-06-13 19:47:14.715271
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    assert parse(r"""
        This is an example docstring.

        Args:
            arg1 (int): The first argument.
            arg2 (str): The second argument.
        """) == Docstring(
        summary="This is an example docstring.",
        body="",
        meta={
            "args": [
                {"type": "int", "name": "arg1", "description": "The first argument."},
                {"type": "str", "name": "arg2", "description": "The second argument."}
            ],
            "kwargs": []
        }
    )

# Generated at 2022-06-13 19:47:18.933097
# Unit test for function parse
def test_parse():
    text = "\"\"\"Test docstring.\n\n    Args: a, b, c\n    Returns: True\"\"\""
    expected = "Test docstring.\n\n    Args: a, b, c\n    Returns: True"
    assert parse(text).content == expected
    print("Unit test for function parse PASSED:", expected)

if __name__ == "__main__":
    # Unit test for function parse
    test_parse()

# Generated at 2022-06-13 19:47:28.871965
# Unit test for function parse
def test_parse():
    assert(parse("") == Docstring())
    assert(parse("test this.\n") == Docstring(
        content="test this.\n", meta={}))
    assert(parse("test this.\n:param x: this",
                 style=Style.google) == Docstring(
                     content="test this.\n",
                     meta={'param': {'x': {'description': 'this'}}}))
    assert(parse("test this.\n@param x this",
                 style=Style.numpy) == Docstring(
                     content="test this.\n",
                     meta={'param': {'x': {'description': 'this'}}}))

# Generated at 2022-06-13 19:47:37.342499
# Unit test for function parse
def test_parse():
    parse_docstring_1 = '''Parse the docstring into its components.
    
    :param text: docstring text to parse
    :param style: docstring style
    '''
    parse_result = parse(parse_docstring_1)
    assert parse_result.short_description == 'Parse the docstring into its components.'
    assert parse_result.long_description == ''
    assert parse_result.params == [{'name': 'text', 'type': None, 'desc': 'docstring text to parse'}, 
                                    {'name': 'style', 'type': None, 'desc': 'docstring style'}]
    assert parse_result.returns == None
    assert parse_result.raises == None


# Generated at 2022-06-13 19:47:44.554322
# Unit test for function parse
def test_parse():
    assert parse(
        '''"""
    This is a summary. Description goes here.

    :param name: description
    :type name: str
    :param age: description
    :type age: int

     less indented
    """''')

    assert parse(
        '''"""
    This is a summary. Description goes here.
    Arguments:
        name (str): description
        age (int): description
    Returns:
        less indented
    """''')

# Generated at 2022-06-13 19:47:46.823588
# Unit test for function parse
def test_parse():
    text = 'Define the name.'
    print(parse(text))
    
test_parse()

# Generated at 2022-06-13 19:47:53.693389
# Unit test for function parse
def test_parse():
    text = '''
    Some python code and docstring.
    :param hello: Some arg text
    :type hello: str
    :returns: Something
    :rtype: str
    '''
    docstr = parse(text)
    print(docstr.args_raw)
    print(docstr.meta)
    return

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:48:01.614463
# Unit test for function parse
def test_parse():
    ex1 = """\
    This is the short description.

    This is the long description.  It can go on and on
    and on and on and on and on and on and on and on and
    on and on and on and on and on and on and on and on
    and on and on and on and on and on and on and on and
    on and on and on and on and on.

    :param param1: this is a first param
    :param param2: this is a second param
    :returns: this is a description of what is returned
    :raises keyError: raises an exception
    """

    result = parse(ex1)

# Generated at 2022-06-13 19:48:11.904401
# Unit test for function parse
def test_parse():
    text = '''\
    Parameters
    ----------
    text : str
        docstring text to parse
    style : Style =Style.auto, optional
        docstring style
    Returns
    -------
    d : Docstring
        parsed docstring representation
    '''
    print(parse(text))

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:48:14.762748
# Unit test for function parse
def test_parse():
  assert parse("This is a docstring.")
  assert parse("This is a docstring.").short_description == "This is a docstring."

# NOSE TESTS BELOW THIS

# Generated at 2022-06-13 19:48:18.610137
# Unit test for function parse
def test_parse():
    assert parse('single-line docstring') == parse('single-line docstring', Style.google)
    assert parse('def func():\n    """\n    multi-line docstring\n    """', Style.google).short_description == 'multi-line docstring'


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:48:24.088890
# Unit test for function parse
def test_parse():
    text = '''
    aaa + bb
    '''
    docstring = parse(text)
    assert docstring.short_description == 'aaa + bb'

    text = '''
    aaa + bb
    :param aa: xxx
    :return: xxx
    '''
    docstring = parse(text)
    assert docstring.short_description == 'aaa + bb'
    assert docstring.params[0].arg_name == 'aa'
    assert docstring.params[0].description == 'xxx'
    assert docstring.returns.description == 'xxx'

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:48:36.132789
# Unit test for function parse
def test_parse():
    """Testing function parse"""
    assert parse("\n")
    assert parse("a")
    assert parse("aa\n")
    assert parse("aa\n\n")
    assert parse("aa\n\n\n")
    assert parse("aa\n\n\n\n")
    assert parse("aa\n\n\n\n\n\n\na")
    assert parse("aa") == parse("a\na") == parse("aa\n\n")
    assert parse("aa") == parse("aa\n\n") == parse("aa\n\n\n") == parse("aa\n\n\n\n")
    assert parse("a\na\n") == parse("a\na") == parse("a\na\n\n") == parse("a\na\n\n\n")
    assert parse

# Generated at 2022-06-13 19:48:46.129794
# Unit test for function parse
def test_parse():
    from docstring_parser.common import ReturnItem
    text = '''This is a docstring.
        
        Args:
            a (str): this is a
            b (int): this is b
        Returns:
            str: this is a
            int: this is b
        '''
    doc = parse(text)
    assert doc.short_description == 'This is a docstring.'
    assert doc.long_description == ''
    assert doc.meta['Args']['a'].name == 'a'
    assert doc.meta['Args']['a'].annotation == 'str'
    assert doc.meta['Args']['a'].description == 'this is a'
    assert doc.meta['Args']['b'].name == 'b'
    assert doc.meta['Args']['b'].annotation

# Generated at 2022-06-13 19:48:57.067402
# Unit test for function parse
def test_parse():
    from docstring_parser.common import Docstring, Description, Params, Return
    docstring = parse("""Return True if the answer is True, False otherwise.

    Args:
        arg1 (int): The first argument.
        arg2 (str, optional): The second argument. Defaults to 'default'.

    Returns:
        bool: The return value. True for success, False otherwise.
    """)

# Generated at 2022-06-13 19:49:07.072690
# Unit test for function parse
def test_parse():
    text = """Unit test docstring

    :param arg1: the first argument
    :param arg2: the second argument
    :returns: arg1 / arg2
    """
    docstring = parse(text, style=Style.numpy)
    print(docstring)
    print(docstring.returns)
    print(docstring.params)
    print(docstring.meta)
    assert docstring.short_description == "Unit test docstring"
    assert docstring.returns.name == "returns"
    assert docstring.returns.type_name == None
    assert docstring.returns.description == "arg1 / arg2"
    assert docstring.params["arg1"].name == "arg1"
    assert docstring.params["arg2"].name == "arg2"
    assert docstring.params

# Generated at 2022-06-13 19:49:18.941926
# Unit test for function parse
def test_parse():
  from docstring_parser.styles import Style
  from docstring_parser.utils import docstring_to_str

  docstring = parse("""This function does something.

  Args:
      arg1:The first argument.
      arg2 (int, optional): The second argument. Defaults to 42.
      *args: Variable length argument list.
      **kwargs: Arbitrary keyword arguments.

  Returns:
      bool: The return value. True for success, False otherwise.
  """)

  print(docstring.short_description)
  print(docstring.long_description)

  assert len(docstring.args) == 3
  assert len(docstring.options) == 2
  assert len(docstring.returns) == 1
  assert docstring.returns[0].type == 'bool'

# Generated at 2022-06-13 19:49:23.387320
# Unit test for function parse
def test_parse():
    text = '''
    :param a: a parameter
    :return: return value
    '''
    assert parse(text) == Docstring("", "", [('a', 'a parameter')], 'return value', "", "")


if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:49:34.302683
# Unit test for function parse
def test_parse():
    from docstring_parser.styles.google import Docstring as GoogleDocstring
    from docstring_parser.styles.numpy import Docstring as NumpyDocstring
    from docstring_parser.styles.epytext import Docstring as EpydocDocstring
    from docstring_parser.styles.napoleon import Docstring as NapoleonDocstring

    paragraph = """
    First paragraph.

    Second paragraph.

    Third paragraph.
    """

    google_docstring = """
    Single-line summary.

    Extended description.

    Args:
        arg1 (int): Description of `arg1`
        arg2 (str): Description of `arg2`

    Returns:
        bool: Description of return value

    Raises:
        AttributeError: The ``BaseException.message`` attribute does not exist.
    """


# Generated at 2022-06-13 19:49:42.909695
# Unit test for function parse
def test_parse():
    """Unit test for function parse"""
    docstring = parse("""\
    This is a docstring.
    Multiline.
    """
    )
    assert isinstance(docstring,Docstring)
    assert isinstance(docstring.short_description,str)
    assert docstring.short_description == "This is a docstring."
    assert isinstance(docstring.long_description,str)
    assert docstring.long_description == "Multiline."
    assert docstring.meta == {}
    assert isinstance(docstring.returns,tuple)
    assert len(docstring.returns) == 0
    assert docstring.raises == None
    assert isinstance(docstring.params,tuple)
    assert len(docstring.params) == 0

# Generated at 2022-06-13 19:49:55.279195
# Unit test for function parse
def test_parse():
    doc = """
        Args:
          arg1 (int): The arg1
          arg2 (str): The arg2
        Returns:
          str: The return value
    """
    parsed = parse(doc)

    func = parsed.funcname
    args = ' '.join([arg for arg in parsed.args])
    items = ' '.join([item for item in parsed.items])
    meta = ' '.join([meta for meta in parsed.meta])

    assert(func is None)
    assert(args == 'arg1 (int) The arg1 arg2 (str) The arg2')
    assert(items == 'Returns: The return value')
    assert(meta == 'Args:')


# Generated at 2022-06-13 19:50:03.877358
# Unit test for function parse
def test_parse():
    assert parse('').short_description == ''
    assert parse('').long_description == ''
    assert parse('').params == []

    src = '''
    Function to add two numbers

    Args:
        x(int): First number
        y(int): Second number

    Returns:
        int: Sum of the two numbers
    '''

    assert len(parse(src).params) == 2
    assert parse(src).params[0].name == 'x'
    assert parse(src).params[0].types == ['int']
    assert parse(src).params[0].description == 'First number'
    assert parse(src).params[1].name == 'y'
    assert parse(src).params[1].types == ['int']
    assert parse(src).params[1].description == 'Second number'

    assert parse

# Generated at 2022-06-13 19:50:06.450350
# Unit test for function parse
def test_parse():
    print("Testing Function parse")
    print("Functionality is in accordance with the function's specification")
    import doctest
    doctest.testmod()



# Generated at 2022-06-13 19:50:15.912157
# Unit test for function parse
def test_parse():
    text = '''
    Parameters:
        a: a variable
    '''
    ds = parse(text)
    assert ds.section('parameters') == ['a: a variable']

    text = '''
    Parameters
        a: a variable
    '''
    ds = parse(text)
    assert ds.section('parameters') == ['a: a variable']

    text = '''Parameters:
        a: a variable
    '''
    ds = parse(text)
    assert ds.section('parameters') == ['a: a variable']

    text = '''Parameters
        a: a variable
    '''
    ds = parse(text)
    assert ds.section('parameters') == ['a: a variable']


# Generated at 2022-06-13 19:50:26.255490
# Unit test for function parse
def test_parse():
    """Testing function parse"""
    print("Testing function parse")

    # Test parse with a good text
    doc = parse("""
    This is a test.
    """)
    print(doc)

    # Test parse with a bad text
    try:
        doc = parse("""
        This is a test.
        """, style=Style.numpy)
    except ParseError as e:
        print("Caught an exception: {}".format(e))

    # Test parse with an empty text
    try:
        doc = parse("", style=Style.numpy)
    except ParseError as e:
        print("Caught an exception: {}".format(e))

# Generated at 2022-06-13 19:50:34.302334
# Unit test for function parse
def test_parse():
    # Tests for Google style
    docstring = """
    This is a longer description.

    :param kevins_mistake: only kevin understands how kevin is wrong
    :param a: first parameter
    :param b: second parameter
    :returns: The return type
    :raises TypeError: when a type error has occurred
    """

    doc = parse(docstring)

    assert len(doc.params) == 3
    assert len(doc.sections) == 2

    assert doc.params['a'] == ""
    assert doc.params['b'] == ""
    assert doc.params['kevins_mistake'] == "only kevin understands how kevin is wrong"

    assert doc.sections[0].title == ""
    assert doc.sections[0].content == "This is a longer description.\n"

# Generated at 2022-06-13 19:50:46.783935
# Unit test for function parse
def test_parse():
    text = """The main parsing routine.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """

    style = Style.auto

    doc = parse(text, Style.auto)

# Generated at 2022-06-13 19:50:56.389639
# Unit test for function parse
def test_parse():
    text = """Summary line.

Description of the object.
The first paragraph is the summary and should be one sentence.
For multi-paragraphs, each subsequent paragraph should be indented.

:param str text: Description of `text`.
:param bool strict: Description of `strict`.
:raises ValueError: Description of `text` and `strict` validation errors.
    :excmsg:`Provide a useful message.`
:raises TypeError: Description of type errors.
:returns: Description of the return value.
:rtype: type of the return value
"""

# Generated at 2022-06-13 19:51:09.679524
# Unit test for function parse
def test_parse():
    res1 = parse('''
    parser
    ''')
    res2 = Docstring()
    assert(res1.brief == res2.brief)

if __name__ == '__main__':
    test_parse()

# Generated at 2022-06-13 19:51:19.905344
# Unit test for function parse
def test_parse():
    from docstring_parser.styles import GOOGLE, NUMPYDOC
    text = """One line summary.

    Extended summary.

    Parameters
    ----------
    arg1 : int
        Description of `arg1`.
    arg2 : str
        Description of `arg2`.

    Returns
    -------
    bool
        Description of return value.
    """
    docstring = parse(text)
    assert docstring == parse(text, style=Style.google)
    assert docstring == parse(text, style=Style.numpy)

    r = parse(text, Style.numpy)
    assert r == parse(text, NUMPYDOC)
    # check instance
    assert isinstance(r, NUMPYDOC)

    r = parse(text, Style.google)
    assert r == parse(text, GOOGLE)